#! /usr/bin/python3 
# download image from FLickr or Imgur
# generalized for any photo site with search feature

import os, sys, re, requests, bs4

# function for image downloader
def dwnldImg(url, catPhotos):
    os.makedirs(catPhotos, exist_ok=True)
    res = requests.get(url + "sarch?q=" + catPhotos)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    reg = re.compile(r'(.*?)b(.jpg)$')

    images = soup.select('#imagelist img')
    for i in images:
        if i.get("alt") == "":
            src = i.get("src")
            mo = reg.search(src)
            if mo != None:
                n_src = mo.group(1) + mo.group(2)
                n_src = "https:" + n_src
                imageFile = open(os.path.join(catPhotos, os.path.basename(n_src))), "wb"
                
                res = requests.get(n_src)
                res.raise_for_status

                for j in res.iter_content(100000):
                    imageFile.write(j)
                imageFile.close
    print("Finished")

url = "https://Flickr.com/"
# url = "https://imgur.com/"
# any url can be substituted

category = "images"

dwnldImg(url, category)