import sys

class Project_Scrap(self):
	def __init__(self):
		name = ''
		location = ''
		investments = ''
		average_invested = -1
		profession = ''
		target_market = ''
		target_location = ''
		company_title = '' 
		source_site_url = '' #html link
		source_site = '' 
	def unassigned(self):
		flag = True
		if name == '':
			print >> sys.stderr, 'Warning: <name> variable not scanned.'
			flag = False
		if location == '':
			print >> sys.stderr, 'Warning: <location> variable not scanned.'
			flag = False
		if investments == '':
			print >> sys.stderr, 'Warning: <investments> variable not scanned.'
			flag = False
		if average_invested == -1:
			print >> sys.stderr, 'Warning: <average_invested> variable not scanned.'
			flag = False
		if profession == '':
			print >> sys.stderr,  'Warning: <mid_invest> variable not scanned.'
			flag = False
		if target_market == '':
			print >> sys.stderr,  'Warning: <target_market> variable not scanned.'
			flag = False
		if target_location == '':
			print >> sys.stderr,  'Warning: <target_location> variable not scanned.'
			flag = False
		if company_title == '':
			print >> sys.stderr, 'Warning: <company_title> variable not scanned.'
			flag = False
		if source_url == '':
			print >> sys.stderr, 'Warning: <source_url> variable not scanned.'
			flag = False
		if source_site == '':
			print >> sys.stderr, 'Warning: <source_site> variable not scanned.'
			flag = False
		
		if flag:
			return False
		else:
			return True
	def insert_Command(self):
		return """INSERT INTO PROJECT(NAME,
         LOCATION, INVESTMENTS, AVERAGE_INVESTED, PROFESSION, TARGET_MARKET, 
		 TARGET_LOCATION,COMPANY_TITLE, SOURCE_URL, SOURCE_SITE)
         VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', 
		 '{}', '{}'')""".format(name, location \
		 investments, average_invested, profession, target_market, target_location, \
		 company_title, source_url, source_site,)