#using news api 
from newsapi import NewsApiClient
import requests
import json

newsapi = NewsApiClient(api_key='f76845297c1c4af08718512a92f324c8')
key = 'f76845297c1c4af08718512a92f324c8'

def worldNews(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={key}'
    req = requests.get(url)
    news = json.loads(req.text)
    for article in news['articles']:
        print(article['title'])
        print(article['description'])
        print("-----------------------------\n-----------------------------")

def headlines(query,category):
    url = f'https://newsapi.org/v2/top-headlines?q={query}&country=in&category={category}&apiKey={key}'
    req = requests.get(url)
    news = json.loads(req.text)
    for article in news['articles']:
        print(article['title'])
        print("-----------------------------\n-----------------------------")

def headline(query):
    url = f'https://newsapi.org/v2/top-headlines?q={query}&country=in&apiKey={key}'
    req = requests.get(url)
    news = json.loads(req.text)
    for article in news['articles']:
        print(article['title'])
        print("-----------------------------\n-----------------------------")


#main
ch = int(input('Enter "1" for world news\nEnter "2" for Indian news\n-----------------------------\n'))
if ch == 1:
    query = input("What news do you want?\n-----------------------------\n")
    worldNews(query)


elif ch == 2:
    choice = ' '
    choice = choice + input('Enter "1" for categorised search else ignore\n-----------------------------\n')
    if choice == ' ':
        query = input("What news do you want?\n-----------------------------\n")
        headline(query)


    elif choice == ' 1':
        query = input("What news do you want?\n-----------------------------\n") 
        category = int(input('Enter the "1" for business\nEnter the "2" for entertainment\nEnter the "3" for general\nEnter the "4" for health\nEnter the "5" science\nEnter the "6" for sports\nEnter the "7" for technology\n-----------------------------\n'))
        match category:
            case 1:
                headlines(query,"business")
            case 2:
                headlines(query,"entertainment")
            case 3:
                headlines(query,"general")
            case 4:
                headlines(query,"health")
            case 5:
                headlines(query,"science")
            case 6:
                headlines(query,"sports")
            case 7:
                headlines(query,"technology")
            case _:
                print('Wrong Input.')
else:
    print('Wrong input.Try again.')
           
