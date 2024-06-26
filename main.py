import requests


#create an account in newsapi.org,
#after creating the account, you will get the api_key
api_key="f649ca5e35a04ab09a2dcd72ee8df3de"

url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f649ca5e35a04ab09a2dcd72ee8df3de"


# made a request
request = requests.get(url)

# get a dictionary with data
content= request.json()

# access the article titles and description
for article in content["articles"]:
    # print(content["articles"]) 
    print(article["title"])
    print(article["description"])

