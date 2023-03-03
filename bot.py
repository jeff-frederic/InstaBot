'''
    Instagram bot that unfollows people that are not following you back.

    Created by @jeff-frederic
'''

from instabot import Bot
import os, glob, time, csv
import numpy as np

USERNAME = ""
PASSWORD = ""

def load_credentials():
    credentials = []
    with open("credentials.csv", "r") as file:
        credentials = csv.reader(file, delimiter=",", skipinitialspace=True).__next__()
    USERNAME = credentials[0]
    PASSWORD = credentials[1]
    print(USERNAME, PASSWORD)

if __name__ == "__main__":
    # Remove bot cookies
    try: os.remove(glob.glob("config/*cookie.json")[0]) 
    except: pass
    
    # Load USERNAME & PASSWORD
    load_credentials()

    # Initialize instagram bot
    bot = Bot()
    
    bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True)
    followers = bot.get_user_followers(USERNAME)            # Get followers
    following = bot.get_user_following(USERNAME)            # Get following
    
    # Exit bot
    bot.logout()