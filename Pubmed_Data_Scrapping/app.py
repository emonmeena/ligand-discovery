from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
import json
from bson import json_util
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)

# client = MongoClient(
#     "mongodb+srv://Omkar:4Um9CsieuCGctpfi@cluster0.3gzyi1o.mongodb.net/?retryWrites=true&w=majority")
# db = client["PubmedDatabase"]
# # collection = db["PubMedCollection"]
# collection = db["CollectionData"]

title = []
author = []
cite = []
abstractUrl = []


def getHTMLdocument(url):
    response = requests.get(url)
    return response.text


def scrape(srchTxt, pgCount):
    t = []
    a = []
    c = []
    ab = []
    title = t
    author = a
    cite = c
    abstractUrl = ab
    # print(len(title), len(author))

    searchText = srchTxt
    pagecount = str(pgCount)
    pages = 0
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=" + \
        searchText+"&page="+str(pages)

    # pbar = tqdm(total=pgCount+1, desc="Scrapping the site...", colour="blue")
    while True:
        html_doc = getHTMLdocument(url)
        soupObject = bs(html_doc, 'html.parser')

        # Extracting Title
        titleContents = soupObject.findAll(
            'a', class_='docsum-title', href=True, limit=10)
        for titleContent in titleContents:
            title.append(titleContent.text)

        # EXtracting Authors
        authorContents = soupObject.findAll(
            'span', class_='docsum-authors full-authors', limit=10)
        for authorContent in authorContents:
            author.append(authorContent.text)

       # EXtracting Cite
        citeContents = soupObject.findAll(
            'span', class_='docsum-journal-citation full-journal-citation', limit=10)
        for citeContent in citeContents:
            cite.append(citeContent.text)

        # Getting Abstract
        for link in soupObject.findAll('a', class_='docsum-title', limit=10):
            abstractUrl.append(
                "https://pubmed.ncbi.nlm.nih.gov/"+link.get('href'))

        # for items in abstractUrls:
            # abstract.append(getAbstract(items))

        pages = pages+1
        url = "https://pubmed.ncbi.nlm.nih.gov/?term=" + \
            searchText+"&page="+str(pages)

        if (pages == int(pagecount)+1):
            break

    print(len(title), len(author), len(cite), len(abstractUrl))
    pipe = []
    for i in range(1, len(title)):
        entry = {
            "title": title[i],
            "author": author[i],
            "cite": cite[i],
            "url": abstractUrl[i]
        }
        pipe.append(entry)
    return pipe


def dataZip():
    # sno=list(range(1,len(title)+1))
    # pipe = [sno, title, author, cite , abstractUrl]
    print(len(title), len(author), len(cite), len(abstractUrl))
    pipe = []
    for i in range(1, len(title)):
        entry = {
            "title": title[i],
            "author": author[i],
            "cite": cite[i],
            "url": abstractUrl[i]
        }
        pipe.append(entry)
    return pipe


choice = True
valid_txt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ '-"

print("hi")
data = scrape("Acute Myeloid Leukemia", 1)
print(data)

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        while True:
            st = request.form.get('searchText')
            if all(char in valid_txt for char in st):
                break
            print("Invalid Search Text!, Please Try Again!")

        while True:
            try:
                pg = str(request.form.get("pageNo"))
                break
            except ValueError:
                print("Please Enter A NUMBER Value!")

        data = scrape(st, pg)
        # data = dataZip()
        # print(data)
        print(len(data))
        collection.insert_many(data)
        return render_template('index.html', data=data)
    return render_template('index.html')


@app.route("/data", methods=["GET"])
def data():
    # all_seeds = list(collection.find({}))
    all_seeds = list(collection.find({}))
    return json.dumps(all_seeds, default=json_util.default)
    # return all_seeds
#
