# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
 
class MbascraperPipeline(object):


	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mba', user='root', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)

	def process_item(self, item, spider):
		# run db query in thread pool
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		query.addErrback(self.handle_error)

		return item

	def _conditional_insert(self, tx, item):
		# create record if doesn't exist. 
 		# all this block run on it's own thread
		tx.execute("select * from bothies where bothy_id = %s", (item['bothy_id'][0], ))
		result = tx.fetchone()
		if result:
			print "Item already stored in db: %s" % item
		else:
			tx.execute(
				"""insert into bothies (bothy_id, name, region, gridref, description, images) values (%s,%s,%s,%s,%s,%s)""",
				(item['bothy_id'], item['name'], item['region'], item['gridref'], item['description'], ','.join(item['images']))
			)
			print "Item stored in db: %s" % item

	def handle_error(self, e):
		print e
		#log.err(e)



