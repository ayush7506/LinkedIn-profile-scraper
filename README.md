# LinkedIn-profile-scraper
A python repository which scrapes basic linkedin profile informations
To scrape linkedin profiles you need to signin with you own username/password. This program scrapes data for certain number of test profiles.
The scraped data are following
  1. Name
  2. Location
  3. Education
  4. Number of connections
  
# Requirements

  1. Python3 
  2. pip3
  3. Selenium
  4. Google Chrome
  5. Chromewebdriver

# Setup

1. Download the latest chromedriver
  https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
2. Unzip the file
3. chmod +x chromedriver
4. sudo mv -f chromedriver /usr/local/share/chromedriver
5. sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
6. sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
7. sudo pip3 install selenium

# Running the file
1. Run scraper.py (python3 scraper.py)
2. It will prompt for email/password for your linkedin profile
3. It will genrate a CSV file with all the scaped outputs
