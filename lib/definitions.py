

actions =  {
  'airing_today' : {
    'descript' : '''List of shows airing today.  Based only on the day and
      does not support times.''',
    'path' : '{element_name}/{element_id}',
    'elig_elements' : [
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'alternative_titles' : {
    'descript' : '''Returns alternative titles of the givin element_id''',
    'path' : '{element_name}/{element_id}/alternative_titles',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : {
      'element_id',
      'element_name',
    },
  },
  'changes' : {
    'descript' : '''Get a list of all of the element ids that have been changed
                        in the past 24 hours.  You can query it for up to 14
                        days worth of changed IDs at a time with the start_date
                        and end_date query parameters. 100 items are returned
                        per page.''',
    'path' : '{element_name}/changes',
    'elig_elements' : [
      'movie',
      'tv',
      'person',
    ],
    'requires' : {
      'element_id',
      'element_name',
    },
  },
  'combined_credits' : {
    'descript' : '''Returns all tv and movie credits for a given element.''',
    'path' : '{element_name}/{element_id}/combined_credits',
    'elig_elements' : [
      'person',
    ],
    'requires' : {
      'element_name',
      'element_id',
    },
  },
  'content_ratings' : {
    'descript' : '''List of ratings added to the show.''',
    'path' : '{element_name}/{element_id}/content_ratings',
    'elig_elements' : [
      'tv',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  'credits' : {
    'descript' : '''Returns the credit id, cast, and crew of a element.''',
    'path' : '{element_name}/{element_id}/credits',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : [
      'element_id',
      'element_name',
    ],
  },
  'details' : {
    'descript' : '''Returns the details of a given element from the element
      id.''',
    'path' : '{element_name}/{element_id}',
    'elig_elements' : [
      'collection',
      'company',
      'credits',
      'keywords',
      'movie',
      'networks',
      'person',
      'review',
      'tv',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  'discover' : {
    'descript' : '''This is used to discover tv and movies based on
      query_params.''',
    'path' : 'discover/{element_name}',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'external_ids' : {
    'descript' : '''Returns external ids for a given element.  Supported
      sources are IMDB, TVDB, and TVRage''',
    'path' : '{element_name}/{element_id}/external_ids',
    'elig_elements' : [
      'person',
      'tv',
    ],
    'requires' : [
      'element_id',
      'element_name',
    ],
  },
  'find' : {
    'descript' : '''Find elements based on external ids.  External sources
      supported are IMDB, TVDB, and TVRage.''',
    'path' : 'find/{external_id}',
    'elig_elements' : [
      'movie',
      'person',
      'tv',
    ],
    'requires' :[
      'external_id',
    ],
  },
  'genres' : {
    'descript' : '''Returns list of valid genres for a givin element.''',
    'path' : 'genre/{element_name}/list',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'images' : {
    'descript' : '''Returns images of a given element''',
    'path' : '{element_name}/{element_id}/images',
    'elig_elements' : [
      'collection',
      'movie',
      'person',
      'tv',
    ],
    'requires' : [
      'element_id',
      'element_name',
    ],
  },
  'jobs' : {
    'descript' : '''List of the job titles used on TMDB''',
    'path' : 'job/list',
  },
  'keywords' : {
    'descript' : '''Returns list of keywords and the associated ids''',
    'path' : '{element_name}/{element_id}/keywords',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  'latest' : {
    'descript' : '''Returns the last created element.''',
    'path' : '{element_name}/latest',
    'elig_elements' : [
      'movie',
      'person',
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'lists' : {
    'descript' : '''Returns the associated list with the element.''',
    'path' : '{element_name}/{element_id}/lists',
    'elig_elements' : [
      'movie',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  # 'movies' : {
  #   'descript' : '''Returns movies associated to a specific element_id''',
  #   'path' : 'movie/',
  #   'elig_elements' : [
  #     'company',
  #   ],
  #   'requires' : [
  #     'element_name',
  #     'element_id',
  #   ],
  # },
  'movie_credits' : {
    'descript' : '''Returns all movie credits for a given element.''',
    'path' : '{element_name}/{element_id}/movie_credits',
    'elig_elements' : [
      'person',
    ],
    'requires' : {
      'element_name',
      'element_id',
    },
  },
  'now_playing' : {
    'descript' : '''Returns list of elements currently in theatres.  Query based
      off release type.  Can optionally specify region param.''',
    'path' : '{element_name}/now_playing',
    'elig_elements' : {
      'movie',
    },
    'requires' : {
      'element_name',
    },
  },
  'on_the_air' : {
    'descript' : '''Shows that are currently airing.  Query based on whether a
      show has had an episode air in the last 7 days.''',
    'path' : '{element_name}/on_the_air',
    'elig_elements' : [
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'popular' : {
    'descript' : '''Returns list of elements that are currently popular on
      TMDB.  Updates daily.''',
    'path' : '{element_name}/popular',
    'elig_elements' : [
      'movie',
      'person',
      'tv',
    ],
    'requires' : {
      'element_name',
    },
  },
  'recommendations' : {
    'descript' : '''Other recomended elements based off the given element_id.''',
    'path' : '{element_name}/{element_id}/recomendations',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' :[
      'element_id',
      'element_name',
    ],
  },
  'release_dates' : {
    'descript' : '''Returns the release dates for a given element.  Different
      release types are premiere, theatrical(limited), theatrical, digital,
      physical, and TV.''',
    'path' : '{element_name}/{element_id}/release_dates',
    'elig_elements' : [
      'movie',
    ],
    'requires' : {
      'element_id',
      'element_name',
    },
  },
  'reviews' : {
    'descript' : 'Returns the reviews for a givin element.',
    'path' : '{element_name}/{element_id}/reviews',
    'elig_elements' : [
      'movie',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  'search' : {
    'descript' : '''Allows to search for specified elements with Strings.''',
    'path' : 'search/{element_name}',
    'elig_elements' : [
      'company',
      'collection',
      'keyword',
      'movie',
      'people',
      'tv',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'screened_theatrically' : {
    'descript' : '''Returns a list of seasons or episodes that were screened at
      film festival or theatre.''',
    'path' : '{element_name}/{element_id}/screened_theatrically',
    'elig_elements' : [
      'tv',
    ],
    'requires' : [
      'element_name',
      'element_id',
    ],
  },
  'search_multi' : {
    'descript' : '''Search for movie, person, and tv show with one request.''',
    'path' : 'search/multi/',
  },
  'similar' : {
    'descript' : '''Elements similar to given element based on keywords and
      genres.''',
    'path' : '{element_name}/{element_id}/similar',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : [
      'element_id',
      'element_name',
    ],
  },
  'tagged_images' : {
    'descript' : '''Returns tagged images of a given element''',
    'path' : '{element_name}/{element_id}/tagged_images',
    'elig_elements' : [
      'person',
    ],
    'requires' : [
      'element_id',
      'element_name',
    ],
  },
  'top_rated' : {
    'descript' : '''Top rated elements.''',
    'path' : '{element_name}/top_rated',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : {
      'element_name',
    },
  },
  'translations' : {
    'descript' : '''Available translations for the element.''',
    'path' : '{element_name}/{element_id}/translations',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : {
      'element_name',
      'element_id',
    },
  },
  'tv_credits' : {
    'descript' : '''Returns all tv credits for a given element.''',
    'path' : '{element_name}/{element_id}/tv_credits',
    'elig_elements' : [
      'person',
    ],
    'requires' : {
      'element_name',
      'element_id',
    },
  },
  'upcoming' : {
    'descript' : '''Elements that are about to be released.''',
    'path' : '{element_name}/upcoming',
    'elig_elements' : [
      'movie',
    ],
    'requires' : [
      'element_name',
    ],
  },
  'videos' : {
    'descript' : '''Related videos to the element.''',
    'path' : '{element_name}/{element_id}/videos',
    'elig_elements' : [
      'movie',
      'tv',
    ],
    'requires' : {
      'element_name',
      'element_id',
    },
  },
}

query_params = {
  'api_key' : {
    'descript' : 'your tmdb api key',
    'type' : 'str',
    'related_actions' : [
      'airing_today',
      'alternative_titles',
      'changes',
      'collection',
      'combined_credits',
      'content_ratings',
      'credits',
      'details',
      'discover',
      'external_ids',
      'find',
      'images',
      'jobs',
      'keywords',
      'latest',
      'lists',
      'movies',
      'movie_credits',
      'networks',
      'now_playing',
      'on_the_air',
      'popular',
      'recommendations',
      'release_dates',
      'reviews',
      'screened_theatrically',
      'search',
      'similar',
      'tagged_images',
      'top_rated',
      'translations',
      'tv_credits',
      'upcoming',
      'videos',
    ],
  },
  'air_date.gte' : {
    'descript' : '''A date that filters results to a specific release date
      greater than or equal''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'air_date.lte' : {
    'descript' : '''A date that filters results to a specific release date
      that is less than or equal to the date.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'append_to_response' : {
    'descript' : '''Append requests within the same namespace to the
    response.''',
    'type' : 'str',
    'related_actions' : [
      'details',
    ],
  },
  'certification' : {
    'descript' : '''Specify countries with a valid certificaiton.  Used with
      certification_country.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'certification.lte' : {
    'descript' : '''Filter for certifcation less than or equal.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'certification_country' : {
    'descript' : '''Specify countryies with a valid certification.  Used with
      certification.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'country' : {
    'descript' : '''Country to filter the query by.''',
    'type' : 'str',
    'related_actions' : [
      'alternative_titles',
    ],
  },
  'end_date' : {
    'descript' : 'End date for query.',
    'type' : 'str',
    'related_actions' : [
      'changes',
    ],
  },
  'external_source' : {
    'descript' : '''External source to find element by.  Supported sources
    are imdb, tvdb, and tvrage.''',
    'type' : 'str',
    'related_actions' : [
      'find/',
    ],
  },
  'first_air_date' : {
    'descript' : '''No descript in API docs''',
    'type' : 'int',
    'related_actions' : [
      'search',
    ],
  },
  'first_air_date.gte' : {
    'descript' : '''A date to filter results to elements with a air date
    greater than or equal to given date.  Can be used with
    include_null_first_air_dates''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'first_air_date.lte' : {
    'descript' : '''A date to filter results to elements with a air date
    less than or equal to given date.  Can be used with
    include_null_first_air_dates''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'include_adult' : {
    'descript' : '''Include adult results''',
    'type' : 'bool',
    'related_actions' : [
      'discover',
      'genres',
      'keywords',
      'search',
    ],
  },
  'include_null_first_air_dates' : {
    'descript' : '''Include elements that do not have an air date.  Used
    with first_air_date filter.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'include_video' : {
    'descript' : '''Filter to include videos.''',
    'type' : 'bool',
    'related_actions' : [
      'discover',
    ],
  },
  'include_image_language' : {
    'descript' : '''No documentation on this arg''',
    'type' : 'str',
    'related_actions' : [
      'images',
    ],
  },
  'language' : {
    'descript' : 'Translates data that can be translated.',
    'type' : 'str',
    'related_actions' : [
      'airing_today',
      'collection',
      'combined_credits',
      'content_ratings',
      'details',
      'discover',
      'external_ids',
      'find',
      'images',
      'genres',
      'keywords',
      'latest',
      'lists',
      'movies',
      'movie_credits',
      'on_the_air',
      'popular',
      'search',
      'recommendations',
      'reviews',
      'similar',
      'tagged_images',
      'top_rated',
      'translations',
      'tv_credits',
      'upcoming',
      'videos',
    ],
  },
  'page' : {
    'descript' : 'Which page to query.',
    'type' : 'int',
    'related_actions': [
      'airing_today',
      'changes',
      'discover',
      'lists',
      'now_playing',
      'on_the_air',
      'popular',
      'reviews',
      'search',
      'similar',
      'tagged_images',
      'top_rated',
      'upcoming',
    ],
  },
  'primary_release_year' : {
    'descript' : '''A filter to limit results to a specific release year.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'primary_release_year.gte' : {
    'descript' : '''Filter for elements greater than a certain release date''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'primary_release_year.lte' : {
    'descript' : '''Filter for elements less than a certain release date.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'query' : {
    'descript' : '''Pass a URI encoded query to search.''',
    'type' : 'str',
    'related_actions' : [
      'search',
    ],
  },
  'region' : {
    'descript' : 'Specify region.',
    'type' : 'str',
    'related_actions' : [
      'discover',
      'now_playing',
      'popular',
      'search',
      'top_rated',
      'upcoming',
    ],
  },
  'release_date.gte' : {
    'descript' : '''Filter for a release date greater than specified date (
      for all release date types)''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'release_date.lte' : {
    'descript' : '''Filter for a release date less than specified date (for
      all release dates)''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'screened_theatrically' : {
    'descript' : '''Filter to include elements that were screened in
    theatres or movie festivals''',
    'type' : 'bool',
    'related_actions' : [
      'discover',
    ],
  },
  'sort_by' : {
    'descript' : 'What value to sort by.',
    'type' : 'str',
    'related_actions' : [
      'discover',
      'genres',
    ],
  },
  'start_date' : {
    'descript' : 'start date for a query.',
    'type' : 'str',
    'related_actions' : [
      'changes',
    ],
  },
  'vote_average.gte' : {
    'descript' : '''Filter for vote count average that are greater than or equal
      to specified value''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'vote_average.lte' : {
    'descript' : '''Filter for vote count average that are lesser than or equal
      to specified value''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'vote_count.gte' : {
    'descript' : '''Filter for vote counts that are greater than or
      equal to specified value.''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'vote_count.lte' : {
    'descript' : '''Filter for vote counts that are less than or equal
      to specified value.''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'with_cast' : {
    'descript' : '''Comma seperated list of person ids and returns all
      elements that contain those actor ids''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_companies' : {
    'descript' : '''Comma seperated list of company ids and returns all
      elements that contain those ids''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_crew' : {
    'descript' : '''Comma seperated list of person ids and returns all
      elements that contain one of those ids.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_genres' : {
    'descript' : '''Comma seperated list of genres and returns all elements
      that match those genres.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_keywords' : {
    'descript' : '''Comma seperated list of keywords and returns all
      elements that contain those keywords ids.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_networks' : {
    'descript' : '''Comma seperated list of networks and returns all
      elements that contain those keywords ids.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_original_language' : {
    'descript' : '''Filter results on origianl language''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_people' : {
    'descript' : '''Comma seperated of person ids and returns all elements
      that contains the persons id.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'with_release_type' : {
    'descript' : '''Comma(AND) or pipe (OR) seperated values to filter
      release types by.  Release types map to the same values found
      on the movie release date method(min 1 and max is 6).''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'with_runtime.gte' : {
    'descript' : '''Filter to return elements that have a runtime
      greater than or equal to specified value.''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'with_runtime.lte' : {
    'descript' : '''Filter to return elements that have a runtime less
      than or equal to specified value.''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
  'without_genres' : {
    'descript' : '''List of genre ids that returns all elements that contain
      the id.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'without_keywords' : {
    'descript' : '''A list of keywords that filters results to only
      elemtns that contain those keywords.''',
    'type' : 'str',
    'related_actions' : [
      'discover',
    ],
  },
  'year' : {
    'descript' : '''Filter to limit results to within a specified year(
      including all release dates)''',
    'type' : 'int',
    'related_actions' : [
      'discover',
    ],
  },
}

elements = {
  'collection' : 'collection',
  'company' : 'company',
  'credits' : 'credits',
  'genre' : 'genre',
  'keyword' : 'keyword',
  'movie' : 'movie',
  'networks' : 'network',
  'person' : 'person',
  'review' : 'review',
  'tv' : 'tv',
}

sort_values = {
  'popularity.asc',
  'popularity.desc',
  'release_date.asc',
  'release_date.desc',
  'revenue.asc',
  'revenue.desc',
  'primary_release_date.asc',
  'primary_release_date.desc',
  'original_title.asc',
  'original_title.desc',
  'vote_average.asc',
  'vote_average.desc',
  'vote_count.asc',
  'vote_count.desc'
  #default: popularity.desc
}
