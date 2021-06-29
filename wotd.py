#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def get_wotd():
    pre_blue = "\033[1;34m"
    post_blue = "\033[00m"
    try:
        res = requests.get("https://www.merriam-webster.com/word-of-the-day")
    except Exception as e:
        print("Unable to Retrieve Word of the Day:", e)

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        wotd = soup.find_all(class_="word-and-pronunciation")[0]("h1")[0].text
        definition_block = soup.find_all(class_="wod-definition-container")[0]("p")

        print(f'Word of the Day: {pre_blue}{wotd}{post_blue}')
        for definition in definition_block:
            if(definition.text[0].isnumeric() and ":" in definition.text ):
                print("\t"+definition.text)

if __name__ == "__main__":
    get_wotd()
