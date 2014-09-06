import requests
import time
import json

BASE_URL = 'http://www.inc.com/rest/inc5000company/%s/full_list'

def get_data_by_id(biz_id, n_tries):
	"""
	INPUT: business ID, number of attempts
	OUPUT: None or JSON data

	Given a business ID, retrieve the data. 
	"""

	# base case for recursive re-try scheme
	if n_tries == 0: 
		return None

	# make the request
	endpoint = BASE_URL % biz_id
	response = requests.get(endpoint)

	# request was successful
	if response: 
		return response.json()['data']
	else: # try again
		print "Couldn't retrieve %s" % biz_id
		print "Sleeping and trying again"
		time.sleep(2)
		return get_data_by_id(biz_id, n_tries-1) # recursion

def main(): 

	biz_id = 22890 # start

	with open('results.json', 'w') as out:

		while(True):

			next = get_data_by_id(biz_id, 5)

			out.write(json.dumps(next))
			out.write("\n")

			print "%s. Done with %s" % (next['rank'], next['ifc_company'])
			biz_id = next['next_id']

if __name__ == "__main__":
	main()

