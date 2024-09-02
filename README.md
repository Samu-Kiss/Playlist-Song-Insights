# 🎼 Playlist Song Insights

## 🚀 Overview
Welcome to **Playlist Song Insights**! 🎧 This project allows you to extract detailed information from a Spotify playlist, including the BPM (beats per minute), key, and mode of each song. It's particularly useful for DJs and music enthusiasts who want to identify songs that mix well together based on these musical properties.

## ✨ Features
- Extracts **BPM** and **Key** of songs from a Spotify playlist.
- Generates an **Excel** file with the song's artist, title, album, BPM, and key.
- Supports Spotify's playlist pagination to handle large playlists efficiently.

## 💻 Technologies Used
![Spotify](https://img.shields.io/badge/Spotify-1ED760?&style=for-the-badge&logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

## ℹ️ About
This project was born out of a passion for music and a desire to make playlist management more insightful. By analyzing the songs' BPM and key, you can create more harmonious mixes and curate playlists that flow smoothly. Whether you're a DJ looking for the perfect transitions or just someone who enjoys making playlists, this tool will give you valuable insights into your music collection.

## 🛠️ Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/Samu-Kiss/Playlist-Song-Insights.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file in the project directory and add your Spotify API credentials:
   ```plaintext
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='your_redirect_uri'
   SPOTIPY_USERNAME='your_spotify_username'
   ```
4. Run the script:
   ```bash
   python playlist_insights.py
   ```

## 📊 Progress
- [x] Extracting BPM and key from Spotify playlists
- [x] Generating Excel files with track information
- [ ] Additional audio analysis features (e.g., loudness, energy)
- [ ] Playlist genre categorization

## 🔖 Notes
- Ensure that your Spotify app is properly configured in the Spotify Developer Dashboard, including setting the correct redirect URI.
- Large playlists may take some time to process depending on your internet connection and Spotify API rate limits.

## 🎶 Song Suggestion
While working on this project, listen to: **"Digital Love" by Daft Punk** – perfect for coding while staying in a groove!

## 📄 License
This project is licensed under the AGPL-3.0 License - see the LICENSE file for details.

## 🙌 Contributions
Feel free to submit pull requests or open issues if you have suggestions, improvements, or bug reports. Any contributions are welcome!
