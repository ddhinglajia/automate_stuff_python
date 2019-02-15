#! /usr/bin/python3 

import os, sys, re, webbrowser, requests, bs4

def linkVerif():

    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code != requests.codes.ok:
        print("Encountered a problem")
    else:
        soup = bs4.BeautifulSoup(res.text)
        lele = soup.select("a")

        for i in range(len(lele)):
            link = lele[i].get("href")
            if link != None:
                if link.startswith("//"):
                    link = "https:" + link
                elif link.startswith("#"):
                    link = url + link
                elif not link.startswith("http"):
                    g = re.search("^(http(.*?)\.(.*?)\/)", url)
                    link = g.group(1) + link

                res = requests.get(link)

                try:
                    res.raise_for_status()
                    print(link + " - " + lele[i].getText())
                except Exception as ex:
                    print(ex)


linkVerif()