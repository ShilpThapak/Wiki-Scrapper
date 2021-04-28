import wikipedia
import wikipediaapi
import requests

# Setting up requests, sessions, and urls for Media Wiki API
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Setting up wikipedia API library
wiki_wiki = wikipediaapi.Wikipedia('en')

# Getting the list of queries to search wikipedia
queries = ["Deep learning", "Machine Learning", "NLP", "Computer Vision", "Mathematics", "Optimization",
"Statistics", "Linear Algebra", "Calculus", "Linguistics", "Computation", "Probability", "Database", "Biology",
"Physics", "Chemistry", "Economics", "Political Sciences", "Drama", "Poetry", "Arts"]

# Creating an empty string named data to store all the extracted data in the future.
data = []

# Using a for loop to search through the queries one by one
for query in queries:
    # Using wikipedia API to get first 20 search results and storing them in a list called titles
    titles = wikipedia.search(query, results = 20)
    for title in titles:
        # Extracting TITLE
        page = wiki_wiki.page(title)

        # Extracting URL
        url = page.fullurl

        # Extracting CATEGORIES
        categories = [category for category in page.categories]
        
        # Extracting TEXT CONTENT
        text = page.text

        # Calculating WORD COUNT
        word_count = len(text.split())

        # Creating a URL to get data from media wiki api
        PARAMS = {"action": "query", "titles": title, "prop": "contributors|extlinks|links|images", "format": "json", "ellimit": 500, "pllimit": 500, "pclimit": 500, "imlimit": 500}
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        pageid = list(DATA["query"]["pages"].keys())[0]
        
        # CONTRIBUTORS
        contributors = DATA["query"]["pages"][pageid]["contributors"]
        
        # EXTERNAL LINKS
        try:
            link_data = DATA["query"]["pages"][pageid]["extlinks"]
            extlinks = []
            for link in link_data:
                extlinks.append(link["*"])
        except:
            extlinks = []
            
        # INTERNAL LINKS
        internal_link_data = DATA["query"]["pages"][pageid]["links"]
        intlinks = []
        for link in internal_link_data:
            intlinks.append(link["title"])
        
        # IMAGES
        try:
            image_data = DATA["query"]["pages"][pageid]["images"]
            images = [] 
            for image in image_data:
                new_title = image['title'].replace(" ", "_")
                image_url = "https://en.wikipedia.org/wiki/" + new_title
                images.append(image_url)
        except:
            images = []
        
        print(title)

        # Adding data to the the "data" list
        data.append({"Title": title, "Categories": categories, "Contributors": contributors, "External Links": extlinks, "Internal Links": intlinks, "Images": images, "Word Count": word_count, "URL": url, "Text Content": text})

# Printing out final data
print(data)