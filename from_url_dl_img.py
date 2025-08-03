# Create .netrc file
#echo "machine example.com login your_username password your_password" > ~/.netrc
#chmod 600 ~/.netrc
#Parse HTML and Extract Links

import requests
from lxml import etree
from io import StringIO

def get_links(session, url):
    response = session.get(url)
    tree = etree.parse(StringIO(response.text), parser=etree.HTMLParser())
    return [a.get('href') for a in tree.xpath('//a') if a.get('href')]
# Recursively Traverse Directories

def is_image(link):
    return link.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))

def crawl_and_download(session, base_url, local_dir):
    links = get_links(session, base_url)
    for link in links:
        full_url = base_url + link
        if link.endswith('/'):  # It's a directory
            crawl_and_download(session, full_url, local_dir)
        elif is_image(link):
            img_data = session.get(full_url).content
            with open(f"{local_dir}/{link}", 'wb') as f:
                f.write(img_data)
#Run the Script
session = requests.Session()
session.auth = ('bkc', 'agro$0923')  # or use .netrc

crawl_and_download(session, 'http://103.62.239.78:8081/remote/Cropfield/', './images')
