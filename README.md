# VR_Travel

Virtual travel experiences can evoke powerful emotions by immersing users in different environments and cultures. By leveraging users' current emotional states, we can tailor virtual experiences that resonate deeply, providing comfort, excitement, or relaxation.

## Overview

This project aims to recommend virtual reality (VR) travel experiences based on the user's current emotional state. It utilizes Selenium for web automation to fetch YouTube video titles and links related to specific emotions such as sadness, disgust, anger, anticipation, fear, enjoyment, trust, and surprise. The fetched data is then presented to the user in an HTML format, allowing them to explore virtual experiences that match their emotional needs and preferences.

## Usage

1. **Setup**: Ensure Python 3.x is installed on your system along with the required packages listed in `requirements.txt`.

2. **Running the Script**:
   - Clone the repository.
   - Navigate to the project directory.
   - Install dependencies using `pip install -r requirements.txt`.
   - Run `python main.py` and follow the prompts to enter an emotion (e.g., Sad, Disgust, Anger) to fetch related VR travel experiences from YouTube.

3. **Dependencies**:
   - Python 3.x
   - `selenium` for web automation
   - `webdriver_manager` for managing web drivers
   - Other dependencies as listed in `requirements.txt`.

## Future Enhancements

- Implement more sophisticated emotion detection methods to automatically determine the user's emotional state.
- Enhance the user interface to provide a more interactive and intuitive experience.
- Expand the range of virtual travel experiences by integrating with additional VR content platforms.

Feel free to contribute to this project by forking and submitting pull requests. Your feedback and contributions are highly appreciated!
