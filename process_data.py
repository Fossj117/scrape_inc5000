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

	if yrs_ranked = 1:
		return None	
	else: 
		current_rank = yrs_ranked[0]['ify_rank']
		previous_rank = yrs_ranked[1]['ify_rank'] if yrs_ranked[1]['ify_year']=='2013' else None
		return current_rank - previous_rank if previous_rank else None

def expand_years_field(df, years='years'):
	"""
	INPUT: data frame, name of the 'years' field
	OUTPUT: data frame (w/extra columns)

	Expands the nested 'years' data in the JSON
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
	df = expand_years_field(df)
