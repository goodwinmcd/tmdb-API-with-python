from lib.definitions import elements, sort_values, actions, query_params
import requests
import sys
from pprint import pprint

default_external = 'imdb_id'
default_element = 'movie' #defaultElement is what will be default value for all
                         #element_name function paramaters
baseUrl = 'https://api.themoviedb.org/3/'
tmdbKey = '85dd8aebef9b0ceff51463d49eaa2093'

def get_popular(element_name = default_element, query_options = None):
  url = constructURL(action = 'popular', element_name = element_name,
                     query_options = query_options)
  r = requests.get(url)
  return r.json()

def get_element_details(element_id, element_name = default_element):
  url = constructURL(action = 'details', element_id = element_id,
                     element_name = element_name)
  r = requests.get(url)
  return r.json()

def find_with_external_id(external_id,
                      return_first = True,
                      query_options = {
                        'external_source' : default_external,
                      }):
  url = constructURL(action = 'find', external_id = external_id,
                     query_options = query_options)
  r = requests.get(url)
  if return_first == True:
    r = get_element_details(r.json()['movie_results'][0]['id'])
  return r.json()

def get_genres(element_name = default_element):
  url = constructURL(action = 'genres', element_name = element_name)
  r = requests.get(url)
  return r.json()

def constructURL(action, element_id = None, element_name = None, external_id = None,
    query_options = None):
  check_errors(element_name = element_name, query_options = query_options)
  query_string = ''
  if query_options != None:
    for each in query_options:
      query_string = '&' + each + '=' + query_options[each]
  path = actions[action]['path'].format( element_id = element_id,
                                         element_name = element_name,
                                         external_id = external_id
  )
  url = baseUrl + path + '?api_key=' + tmdbKey + query_string
  print(url)
  return url

def check_errors(element_name = default_element, query_options = None):
  try:
    if query_options and not all(each in query_params for each in query_options):
      raise ValueError(each + ' is not a valid query param')
    if element_name and element_name not in elements:
      raise ValueError(element_name + ' is not a valid element')
  except ValueError as r:
    print(r.args[0])
    sys.exit()

pprint(get_popular())
pprint(get_genres())
#pprint(findWithExternalId('tt0133093'))
#pprint(find_with_external_id('tt0068646'))
