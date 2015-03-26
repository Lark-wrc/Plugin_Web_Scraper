import sys

class Project_Scrap(object):
	def __init__(self):
		self.name = ''
		self.current_funding = -1
		self.target_funding = -1
		self.catagories = []
		self.min_invest = -1
		self.end_date = ''
		self.backer_count = -1
		self.company_logo = '' #html link
		self.item_image = '' #html link
		self.source = '' #html link
		self.source_site = '' 
	def unassigned(self):
		flag = True
		if self.name == '':
			print >> sys.stderr, 'Warning: <name> variable not scanned.'
			flag = False
		if self.current_funding == -1:
			print >> sys.stderr, 'Warning: <current_funding> variable not scanned.'
			flag = False
		if self.target_funding == -1:
			print >> sys.stderr, 'Warning: <target_funding> variable not scanned.'
			flag = False
		if self.catagories == []:
			print >> sys.stderr, 'Warning: <catagories> variable not scanned.'
			flag = False
		if self.min_invest == -1:
			print >> sys.stderr,  'Warning: <mid_invest> variable not scanned.'
			flag = False
		if self.end_date == '':
			print >> sys.stderr,  'Warning: <end_date> variable not scanned.'
			flag = False
		if self.backer_count == -1:
			print >> sys.stderr,  'Warning: <backer_count> variable not scanned.'
			flag = False
		if self.company_logo == '':
			print >> sys.stderr, 'Warning: <company_logo> variable not scanned.'
			flag = False
		if self.item_image == '':
			print >> sys.stderr, 'Warning: <item_image> variable not scanned.'
			flag = False
		if self.source == '':
			print >> sys.stderr, 'Warning: <source> variable not scanned.'
			flag = False
		if self.source_site == '' :
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
	'{}', '{}', '{}', '{}', '{}')""".format(self.name, self.current_funding,
		self.target_funding, self.catagories, self.min_invest,
                self.end_date, self.backer_count, self.company_logo,
                self.item_image, self.source, self.source_site)
