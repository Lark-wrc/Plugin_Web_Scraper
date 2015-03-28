import Project_Scrap
import Investor_Scrap
import json
import sys
import os
import urllib


plugin_dir = './Plugins'
plugins = []


#Read in the plugins
files = os.listdir(plugin_dir)

for f in files:
	if os.path.isdir(f):
		continue
	with open(f) as plug:
		plugins.append(json.loads(f.read()))
	
#Error check all the plugins

def detail_page(url,plugin,pagetype):
	#Download the HTML for the page in question.
	urllib.urlretrieve (url, "html.html")
	ret = ''
	#make the data storage class
	if pagetype == 'Project':
		ret = Project_Scrap()
	else:
		ret = Investor_Scrap()
	
	#Scraper itself
	for p in plugin['detail']:
		f = open("html.html", 'w')
		
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
				output.append(x)
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
						ouput = o[4:-1]
			if 'src' in output:
				out = output.split(' ')
				for o in out:
					if o[0:3] == 'src':
						ouput = o[3:-1]	
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
			while 1:
				x = f.readline()
				if x == p['end']+'\n':
					break
				elif x+'\n' in p['start_tags']:
					flag = True
					output = ''
				elif x+'\n' in p['end_tags']:
					flag = False
					scanned.append(output)
				elif flag == True:
					x = x.replace("$", "")
					x = x.replace("\n", "")
					output.append(x)
				elif flag == False:
					pass
				else:
					print 'Something dun fucked up'
		

		#Look at the scanned data, and store it appropriately. 
				for x in range(1, len(scanned)):
					if scanned[x] in p['translations']:
						var = p['translations'][scanned[x]]
						exec('ret.' + var + ' = ' + repr(scanned[x-1]))
		f.close()
	return ret			
					
			
		

	#Connect to SQL

	#Send to server
