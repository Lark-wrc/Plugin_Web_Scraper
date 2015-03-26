import sys

class Project_Scrap(self):
	def __init__(self):
		name = ''
		current_funding = -1
		target_funding = -1
		catagories = []
		min_invest = -1
		end_date = ''
		backer_count = -1
		company_logo = '' #html link
		item_image = '' #html link
		source = '' #html link
		source_site = '' 
	def unassigned(self):
		flag = True
		if name == '':
			print >> sys.stderr, 'Warning: <name> variable not scanned.'
			flag = False
		if current_funding == -1:
			print >> sys.stderr, 'Warning: <current_funding> variable not scanned.'
			flag = False
		if target_funding == -1:
			print >> sys.stderr, 'Warning: <target_funding> variable not scanned.'
			flag = False
		if catagories == []:
			print >> sys.stderr, 'Warning: <catagories> variable not scanned.'
			flag = False
		if min_invest == -1:
			print >> sys.stderr,  'Warning: <mid_invest> variable not scanned.'
			flag = False
		if end_date == '':
			print >> sys.stderr,  'Warning: <end_date> variable not scanned.'
			flag = False
		if backer_count == -1:
			print >> sys.stderr,  'Warning: <backer_count> variable not scanned.'
			flag = False
		if company_logo == '':
			print >> sys.stderr, 'Warning: <company_logo> variable not scanned.'
			flag = False
		if item_image == '':
			print >> sys.stderr, 'Warning: <item_image> variable not scanned.'
			flag = False
		if source == '':
			print >> sys.stderr, 'Warning: <source> variable not scanned.'
			flag = False
		elif source_site == '' :
			print >> sys.stderr, 'Warning: <source_site> variable not scanned.'
			flag = False
		
		if flag:
			return False
		else:
			return True
	def insert_Command(self):
		return """INSERT INTO PROJECT(NAME,
         CURRENT_FUNDING, TARGET_FUNDING, CATAGORIES,
		 MIN_INVEST, END_DATE, BACKER_COUNT,COMPANY_LOGO,
		 ITEM_IMAGE, SOURCE, SOURCE_SITE)
         VALUES ('{}', {}, {}, '{}', {}, {}, '{}', {}, 
		 '{}', '{}', '{}', '{}', '{}')""".format(name, current_funding \
		 target_funding, catagories, min_invest, end_date, backer_count, \
		 company_logo, item_image, source, source_site)