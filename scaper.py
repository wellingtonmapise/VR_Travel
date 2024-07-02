""""
Author: Wellington Paidamoyo Mapise
Date: 01 July 2024
"""
#import required modules
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

"""
This function contains the logic for scrapping the appropriate VR content based on the detected emotion
"""
def get_expriences(emotion):
    #URLs for different virtual experiences based on emotion
    
