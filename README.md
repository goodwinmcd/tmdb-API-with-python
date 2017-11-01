# tmdb-API-with-python
A python script to easily interact with the tmdb api

I created functions to easily interact with the tmdb api.  The functions I have
created so far are for another specific project of mine to collect movie data
based on imdb id's.  It would be easy to expand upon the functions I have made
so far.  A lot of the heavy lifting is done by the dictionary that I created in
lib.  

By default the program checks movies.  To change this so that it checks persons
or genres just change the default_element variable to whatever element you want
the methods to search for by default.  You can supply element_names on a need to
basis by specifying element_name param in the fucntions that allow it.

To search movies, tvs, and persons based on an imdb id
find_with_external_id(imdb_id, return_first = false)

To search movies, tvs, and persons and get the first result of the default element
find_with_external_id(imdb_id)

Get genres for default_element
get_genres()

Get genres for specific element:
get_genres(element_name = 'name of element')

Continuously developing as I need to for my other projects. 
