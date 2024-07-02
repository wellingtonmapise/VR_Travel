"""
Author: Wellington Paidamoyo Mapise
Date: 01 July 2024
"""
from scraper import get_experiences_with_selenium
#from emotion_detection import detect_emotion

def main():
    # Example usage:
    emotion = input("Enter the emotion (e.g., Sad, Disgust, Anger, etc.): ")
    experiences = get_experiences_with_selenium(emotion)
    if experiences:
        for exp in experiences:
            print(exp)
    else:
        print("No experiences found.")
    