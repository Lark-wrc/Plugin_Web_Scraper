from Project_Scrap import Project_Scrap
from selenium import webdriver
from Investor_Scrap import Investor_Scrap
import json
import sys
import os
import urllib
import MySQLdb
from time import sleep

plugin_dir = './Plugins'
plugins = []


#Read in the plugins
files = os.listdir(plugin_dir)

for f in files:
	if os.path.isdir(f):
		continue
	
	with open('Plugins/'+f) as plug:
		plugins.append(json.loads(plug.read()))
	

def detail_page(url,plugin,pagetype):
	#Download the HTML for the page in question.
	urllib.urlretrieve (url, "html.html")
	ret = ''
	#make the data storage class
	if plugin['list_type'] == 'Project':
		ret = Project_Scrap()
	else:
		ret = Investor_Scrap()
	
	#Scraper itself
	for p in plugin['details']:
		f = open("html.html", 'r')
		
		#indiviual read in type
		if p['type'] == 'line':
			output = ''
			#skip to the the line specified if it exists.
			if p['skip'] != '':
				while f.readline() != p['skip']+'\n':
					pass
			
			
			#readlines until the tag starting the information we need is read.
			while f.readline() != p['start']+'\n':
				pass
			
			
			#add any lines in between the start line just read and the close
			#tag to the output string.
			while 1:
				x = f.readline()
				output = output + x
				if x == p['end']+'\n':
					break
			
			
			#removes all dollar signs from the output.
			output = output.replace("$", "")
			output = output.replace("\n", "")
			
			#Pulls links out of a long tag.
			if 'href' in output:
				out = output.split(' ')
				for o in out:
					if o[0:4] == 'href':
						output = o[4:-1]
			if 'src' in output:
				out = output.split(' ')
				for o in out:
					if o[0:3] == 'src':
						output = o[3:-1]	
			if output.isdigit():
				output = int(output)
			
			
			#sets the scrap variable named specified in the plugin to the output.
			exec('ret.' + p['name'] + ' = output')
			
		#block read in type
		elif p['type'] == 'block':
			while f.readline() != p['start']+'\n':
				pass
			
			#read every line between a start and end tag. each line is checked for a start or
			#end tag, depending on the last one seen. in between them is stored in an array,
			#outside is not. This is done until the block end tag is found.
			scanned = []
			flag = False
			output = ''
			print p['start_tags']
			while 1:
				x = f.readline()
				print x[:-1], flag
				if x == p['end']+'\n':
					break
				elif x[:-1] in p['start_tags'] and flag == False:
					flag = True
					output = ''
				elif x[:-1] in p['end_tags'] and flag == True:
					flag = False
					scanned.append(output)
				elif flag == True:
					x = x.replace("$", "")
					x = x.replace("\n", "")
					output= output + x
				elif flag == False:
					pass
				else:
					print 'Something dun fucked up'
			print scanned
                        #Look at the scanned data, and store it appropriately. 
			for x in range(1, len(scanned)):
				if scanned[x] in p['translations']:
					var = p['translations'][scanned[x]]
					exec('ret.' + var + ' = ' + repr(scanned[x-1]))
		f.close()
	return ret			
					
	def list_page(plugin):
		#loadButton = "//div[contains(@class, 'warning') and contains(@class, 'btn-warning') and contains(@class, 'button')]"
		loadButton = plugin['loader']
		driver = webdriver.Firefox()
		driver.get(plugin['list_page'])
		
		try:
			while 1:
				duck.find_element_by_xpath(loadButton).click()
				sleep(2)
		except:
			pass
		f = open('list.html','w')
		f.write(driver.page_source.encode('ascii','ignore'))
		f.close()
		f = open('list.html', 'r')
		
		while 1:
			line = f.readline()
			if line == '<div class="project">':
				line = f.readline()
				line = line.split(' ')
				for o in line:
					if o[0:8] == 'ng-href="':
						line = o[8:-1]
						break
				ret = detail_page("crowdrabbit.com/"+line,plugin)
				send_scrap(ret,plugin)
		f.close()
		
	def send_scrap(scrap, plugin):
		#db=MySQLdb.connect('softengine.cyjkgej2ippd.us-east-1.rds.amazonaws.com:3306','CrowdFund','12345678')
		db=MySQLdb.connect(plugin['address'],plugin['user'],plugin['pass'])
		c=db.cursor()
		c.execute(scrap.insert_Command())
	
	if __name__ == '__main__':
		for p in plugins:
			list_page(p)