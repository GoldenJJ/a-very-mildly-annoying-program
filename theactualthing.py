import webbrowser
import keyboard
import random

# Url list
urlList = [
    'http://www.boredbutton.com', 
    'https://www.google.com', 
    'https://youtube.com', 
    'https://facebook.com', 
    'https://twitter.com', 
    'https://wikipedia.org',
    'https://instagram.com', 
    'https://baidu.com',
    'https://yahoo.com',
    'https://bing.com', 
    'https://reddit.com',
    ]
# Set url to a random index from the list above
url = urlList[random.randint(0, len(urlList))]

# Character list
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', ',', '.','?',':','"']
# Set char to a random index from the list above
char = charList[random.randint(0, len(charList))]

# Print the current character conditions
# print("Pressing '" + char + "' will open " + url + ".")


while True:
        if keyboard.is_pressed(char):
            # Open a new random url from urlList
            webbrowser.open(url, new=1)

            # Reset the active variables to new random values
            char = charList[random.randint(0, len(charList) - 1)]
            url = urlList[random.randint(0, len(urlList) - 1)]
            
            # Reprint the current character conditions
            # print("Pressing '" + char + "' will open " + url + ".")
