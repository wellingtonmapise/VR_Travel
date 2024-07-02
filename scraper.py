"""
Author: Wellington Paidamoyo Mapise
Date: 01 July 2024
"""
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def get_experiences(emotion):
    # URLs for different virtual experiences based on emotion
    url_map = {
        "Sad": 'https://www.youtube.com/results?search_query=relaxing+nature+walks',
        "Disgust": 'https://www.youtube.com/results?search_query=artistic+tours',
        "Anger": 'https://www.youtube.com/results?search_query=family+friendly+virtual+parks',
        "Anticipation": 'https://www.youtube.com/results?search_query=thrilling+adventure+tours',
        "Fear": 'https://www.youtube.com/results?search_query=soothing+beach+experiences',
        "Enjoyment": 'https://www.youtube.com/results?search_query=exciting+city+tours',
        "Trust": 'https://www.youtube.com/results?search_query=historical+tours',
        "Surprise": 'https://www.youtube.com/results?search_query=unique+cultural+experiences'
    }

    # Retrieve the URL for the specified emotion or default to YouTube's homepage
    url = url_map.get(emotion, 'https://www.youtube.com')

    try:
        # HTTP GET request to fetch the HTML content
        response = HTTP.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = SOUP(response.text, "lxml")

        # Extract video titles from the parsed HTML
        titles = soup.find_all("a", attrs={"href": re.compile(r'\/watch\?v=')})

        # Return the list of titles found
        return titles

    except HTTP.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
