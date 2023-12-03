import requests

def get_movie_details_by_title(api_key, title):
    """
    Get details for a movie by title using the OMDb API.

    Parameters:
    - api_key: Your OMDb API key (get it from http://www.omdbapi.com/apikey.aspx)
    - title: Title of the movie

    Returns:
    - Movie details in JSON format
    """
    base_url = "http://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "t": title,
    }

    response = requests.get(base_url, params=params)
    movie_details = response.json()

    return movie_details



def search_movies(api_key, search_term):
    """
    Search for movies by a search term using the OMDb API.

    Parameters:
    - api_key: Your OMDb API key (get it from http://www.omdbapi.com/apikey.aspx)
    - search_term: Search term (title, actor, director, etc.)

    Returns:
    - List of movies matching the search term in JSON format
    """
    base_url = "http://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "s": search_term,
    }

    response = requests.get(base_url, params=params)
    movie_list = response.json().get("Search", [])

    return movie_list