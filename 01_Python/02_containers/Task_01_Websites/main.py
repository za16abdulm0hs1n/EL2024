import websites

while True:
    websites.show_websites()
    website_id = int(input("Enter the number of the website: (or 0 to exit) : "))
    if website_id == 0:
        break
    if website_id in websites.favorite_websites:
        url = websites.favorite_websites[website_id]['url'] 
        websites.open_website(url)
        
