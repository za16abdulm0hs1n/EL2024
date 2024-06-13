import webbrowser

# define Websites
favorite_websites = {
    1: {"name": "Facebook", "url": "https://www.facebook.com"},
    2: {"name": "Instagram", "url": "https://www.instagram.com"},
    3: {"name": "X", "url": "https://www.x.com"},
    4: {"name": "YouTube", "url": "https://www.youtube.com"},
    5: {"name": "Google", "url": "https://www.google.com"},
    6: {"name": "Yahoo", "url": "https://www.yahoo.com"},
    7: {"name": "MSN", "url": "https://www.msn.com"},
    8: {"name": "Nasa", "url": "https://www.nasa.gov/"},
    9: {"name": "AlJazeera", "url": "https://www.aljazeera.com/"},
    10: {"name": "Amazon", "url": "https://www.amazon.de"}}


def show_websites():
    print("List of the Websites:")
    for id , website in favorite_websites.items():
        print('{} : {}'.format(id,website['name']))

def open_website(url = "https://www.google.com"):
    webbrowser.get('chrome').open(url)
