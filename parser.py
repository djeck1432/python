#coding: utf-8

import requests
from lxml import html
import urlparse
import smptlib

class Avito(object):
	MAX_SUMM = 60000
	RESULT = []

	def parse_avito_RUN(self):
		url = 'https://www.avito.ru/naberezhnye_chelny/zapchasti_i_aksessuary/audio-_i_videotehnika?view=gallery'
		r = requests.get(url)
		res = html.formstring(r.content)
		result = res.xpath(u'//*[contains(text(),"Последняя")]/@href')
		num = self.get_page_num(result[0])
		result =self.get_page_data(num)
		return result

	def get_page_data(self,num):
		url ='https://www.avito.ru/naberezhnye_chelny/zapchasti_i_aksessuary/audio-_i_videotehnika?view=gallery'
		for i in xrange(1,num):
			r = requests.get(url.format(i))
			self.get_all(r.content)
			return self.RESULT

	def get_page_num(self,href):
		result = urlparse.urlparse(href)
		result = urlparse.parse_qs(result.query)
		return int(result['p'][0])

