"""
Author: Wellington Paidamoyo Mapise
Date: 01 July 2024
"""
from scraper import get_experiences
#from emotion_detection import detect_emotion

def main():
    try:
        # In the future, you can implement more sophisticated emotion detection
        # emotion = detect_emotion()

        # For now, testing with direct user input
        emotion = input("Enter the emotion (e.g., Sad, Disgust, Anger, etc.): ")
        experiences = get_experiences(emotion)
        
        count = 0
        for experience in experiences:
            tmp = str(experience).split('>')
            if len(tmp) == 3:
                title = tmp[1][:-3]
                link = "https://www.youtube.com" + experience['href']
                print(f"{title}: {link}")
            
            if count > 4:
                break
            count += 1
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ =='__main__':
    main()
