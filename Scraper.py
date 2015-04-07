from Project_Scrap import Project_Scrap
from selenium import webdriver
from Investor_Scrap import Investor_Scrap
import json
import sys
import os
import urllib
import MySQLdb
from pprint import pprint
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
	

def detail_page(url,plugin):
	#Download the HTML for the page in question.
	urllib.urlretrieve (url, "html.html")
	ret = ''
	#make the data storage class
	if plugin['type'] == 'Project':
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
				if x == p['end']+'\n':
					break
				output = output + x
			
			#removes all dollar signs from the output.
			output = output.replace("$", "")
			output = output.replace("\n", "")
			
			#Pulls links out of a long tag.
			if 'href' in output:
				out = output.split(' ')
				for o in out:
					if o[0:4] == 'href':
						output = o[6:-1]
			if 'src' in output:
				out = output.split(' ')
				for o in out:
					if o[0:3] == 'src':
						output = o[7:-1]        
			if output.isdigit():
				output = int(output)
			
			cat = p['name']
			#sets the scrap variable named specified in the plugin to the output.
			exec('ret.' + cat + ' = output') in locals()
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
			while 1:
				x = f.readline()
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
			#Look at the scanned data, and store it appropriately. 
			for x in range(1, len(scanned)):
				if scanned[x] in p['translations']:
					var = p['translations'][scanned[x]]
					exec('ret.' + var + ' = ' + repr(scanned[x-1])) in locals()
		f.close()
	return ret                      
					
def mega_list_page(plugin):
        loadButton = "//div[contains(@class, 'warning') and contains(@class, 'btn-warning') and contains(@class, 'button')]"
        #loadButton = plugin['loader']
        driver = webdriver.Firefox()
        driver.get(plugin['list_page'])
        sleep(3)
        try:
                while 1:
                        driver.find_element_by_xpath(loadButton).click()
                        sleep(2)
        except:
                pass
        f = open('list.html','w')
        f.write(driver.page_source.encode('ascii','ignore'))
        f.close()
        driver.quit()
        f = open('list.html', 'r')
        flag = False
        for line in f:
                if flag:
                        flag = False
                        split = line.split(' ')
                        second = ''
                        for o in split:
                                if o[0:9] == 'ng-href="':
                                        second = o[9:-1]
                                        break
                        cat = 'http://crowdrabbit.com/'+''.join(second)+'.html'
                        print cat
                        ret = detail_page(cat,plugin)
                        send_scrap(ret,plugin)
                if line == plugin['project_start']+'\n':
                        flag = True
        f.close()
        
def send_scrap(scrap, plugin):
        pprint (vars(scrap))
        #db=MySQLdb.connect('host='+plugin['address']+',user='+plugin['user']+',pass='+plugin['pass']+',db='+plugin['db'])
        #c=db.cursor()
        #c.execute(scrap.insert_Command())

if __name__ == '__main__':
        for p in plugins:
                if p['list_type'] == 'mega':
                        mega_list_page(p)
