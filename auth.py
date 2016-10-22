#coding : utf-8
import requests
from bs4 import BeautifulSoup

class Iterpals(object):
	url = 'https://www.interpals.net/'

	def auth(self):
		session = requests.Session()
		url = self.url + 'login.php'	
		params ={
			'username':u'oleh.kostashchuk@gmail.com',
			'auto_login':1,
			'password':u'oleg12345',
			'csrf_token': u'OTBjY2U4Y2I=',
		} 
		r = session.post(url,params)
		print(r.text)





if __name__=='__main__':
	interpals=Iterpals()
	interpals.auth()