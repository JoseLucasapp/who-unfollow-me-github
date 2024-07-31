# Who unfollow me github

## Overview
This app uses web scraping and multithreading to identify GitHub users you don't follow and users who don't follow you back. This bot helps you manage your GitHub follower relationships efficiently.

## Features
 - Web Scraping: Fetches data from GitHub to track followers and following lists.
 - Multithreading: Utilizes threads to perform web scraping operations concurrently, improving performance.
 - User-Friendly: Simple command-line interface to input your GitHub username and retrieve results.

## Requirements
 - Python 3.7+
 - The Python libraries on <a href="./requirements.txt">requirements.txt</a>:

## Installation
  1. Clone the repository:
  ```
  git clone https://github.com/yourusername/github-follower-tracker-bot.git
  cd github-follower-tracker-bot
  ```

  2. Install the required libraries:
  ```
  pip install -r requirements.txt
  ```

## Usage
  1. Run the script:
  ```
  python github_follower_tracker.py
  ```

  2. Enter your GitHub username when prompted.
  
  3. The bot will fetch your followers and the users you follow, and then display:
       - Users you follow who do not follow you back.
       - Users who follow you but you do not follow back.

## Example Output
```
Enter your GitHub username: yourusername

Fetching data...

Users you follow who do not follow you back:
- user1
- user2
- user3

Users who follow you but you do not follow back:
- user4
- user5
- user6
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Joselucasapp
