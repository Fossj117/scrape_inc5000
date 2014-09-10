import json
import pandas as pd

def ranking_delta(year_data):
	"""
	INPUT: year_data about a company
	OUTPUT: int or None (change in ranking)

	Utility for computing a company's change in ranking from 
	last year if applicable. Called in 'expand_years_field'
	"""

	yrs_ranked = len(year_data)

	if yrs_ranked in {0, 1}:
		return None	
	else: 
		current_rank = year_data[0]['ify_rank']
		previous_rank = year_data[1]['ify_rank'] if year_data[1]['ify_year']=='2013' else None
		return int(current_rank) - int(previous_rank) if previous_rank else None

def expand_years_field(df, years='years'):
	"""
	INPUT: data frame, name of the 'years' field
	OUTPUT: data frame (w/extra columns)

	Expands the nested 'years' data in the JSON and computes a few basic things: 

	- n_years_ranked : number of years company was ranked in INC 5000
	- which_years_ranked : space-delimited text field including the years ranked
	- rank_delta : change in a company's rank from previous ranking (if applicable), or NA
	"""

	df = df.copy()
	df['n_yrs_ranked'] = df[years].apply(lambda x: len(x))
	df['which_years_rankied'] = df[years].apply(lambda x: " ".join([yr['ify_year'] for yr in x]))
	df['rank_delta'] = df[years].apply(ranking_delta)

	return df

if __name__ == "__main__":

	FNAME = 'results.json'

	with open(FNAME, 'rb') as f: 
		raw = [json.loads(line) for line in f]

	df = pd.DataFrame(raw)

	# expand the nested years field
	df = expand_years_field(df)
