"""
Author: Wellington Paidamoyo Mapise
Date: 01 July 2024
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import os

def get_experiences_with_selenium(emotion):
    # URLs for different virtual experiences based on emotion
    url_map = {
        "Sad": 'https://www.youtube.com/results?search_query=relaxing+nature+walks',
        "Disgust": 'https://www.youtube.com/results?search_query=artistic+tours',
        "Anger": 'https://www.youtube.com/results?search_query=family+friendly+virtual+parks',
        "Anticipation": 'https://www.youtube.com/results?search_query=thrilling+adventure+tours',
        "Fear": 'https://www.youtube.com/results?search_query=soothing+beach+experiences',
        "Enjoyment": 'https://www.youtube.com/results?search_query=exciting+city+tours',
        "Trust": 'https://www.youtube.com/results?search_query=historical+tours',
        "Surprise": 'https://www.youtube.com/results?search_query=unique+cultural+experiences',
        "Boredom": 'https://www.youtube.com/results?search_query=fun+virtual+games',
        "Loneliness": 'https://www.youtube.com/results?search_query=virtual+community+events',
        "Confusion": 'https://www.youtube.com/results?search_query=educational+tutorials',
        "Excitement": 'https://www.youtube.com/results?search_query=virtual+roller+coaster+rides',
        "Relief": 'https://www.youtube.com/results?search_query=guided+meditation+videos',
        "Love": 'https://www.youtube.com/results?search_query=romantic+virtual+walks',
        "Pride": 'https://www.youtube.com/results?search_query=inspirational+speeches',
        "Shame": 'https://www.youtube.com/results?search_query=self-compassion+talks',
        "Guilt": 'https://www.youtube.com/results?search_query=forgiveness+videos',
        "Happiness": 'https://www.youtube.com/results?search_query=happy+virtual+experiences',
        "Gratitude": 'https://www.youtube.com/results?search_query=gratitude+practices',
        "Awe": 'https://www.youtube.com/results?search_query=wonders+of+the+world+tours'
    }

    # Retrieve the URL for the specified emotion or default to YouTube's homepage
    url = url_map.get(emotion, 'https://www.youtube.com')

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Wait for page to load and find elements
    video_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/watch?v=")]')

    # Prepare HTML content
    html_content = '<html><body><h1>Virtual Experiences for Emotion: {}</h1><ul>'.format(emotion)
    for video in video_elements:
        title = video.text
        link = video.get_attribute('href')
        if title and link:
            html_content += '<li><a href="{}" target="_blank">{}</a></li>'.format(link, title)
    html_content += '</ul></body></html>'

    driver.quit()

    # Write HTML content to file
    file_path = os.path.abspath("experiences.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Open the HTML file in the default web browser
    webbrowser.open('file://' + file_path)

# Example usage:
emotion = input("Enter the emotion (e.g., Sad, Disgust, Anger, etc.): ")
get_experiences_with_selenium(emotion)
