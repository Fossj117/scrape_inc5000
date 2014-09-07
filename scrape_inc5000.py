import requests
import time
import json

class Inc5000_Scraper(object):

	BASE_URL = 'http://www.inc.com/rest/inc5000company/%s/full_list'

	def __init__(self):
		pass

	def scrape(self, fname): 
		"""
		Run the scraper
		"""

		biz_id = self.get_start_id()

		with open(fname, 'w') as out:

			while biz_id:

				next = get_data_by_id(biz_id, 5)

				out.write(json.dumps(next))
				out.write("\n")

				biz_id = next['next_id'] if next else None


	def get_data_by_id(self, biz_id, n_tries):
		"""
		INPUT: business ID, number of attempts
		OUPUT: None or JSON data

		Given a business ID, retrieve the data. 
		"""

		# base case for recursive re-try scheme
		if n_tries == 0: 
			return None

		# make the request
		endpoint = self.BASE_URL % biz_id
		response = requests.get(endpoint)

		# request was successful
		if response: 
			return response.json()['data']
		else: # try again
			print "Couldn't retrieve %s" % biz_id
			print "Sleeping and trying again"
			time.sleep(2)
			return get_data_by_id(biz_id, n_tries-1) # recursion


	def get_start_id(self):
		"""
		TODO: automate this
		"""
		return 22890 # manual

if __name__ == "__main__":
	
	scraper = Inc5000_Scraper()
	scraper.scrape('results.json')
