import requests
import pyperclip

class Quotable():
    """Quotable is a free, open source quotations API"""
    def __init__(self,random_quote,random_quotes,list_quotes,list_authors,
                 search_quotes,search_authors,list_tags):
        #list of quotable attributes
        self.random_quote = random_quote
        self.random_quotes = random_quotes
        self.list_quotes = list_quotes
        self.list_authors = list_authors
        self.search_quotes = search_quotes
        self.search_authors = search_authors
        self.list_tags = list_tags

    def get_random_quote(self):
        """ Returns a single random quote from the database """
        response = requests.get(self.random_quote, timeout=10)
        quote = response.json()
        print("QUOTE_TYPE:",quote['tags'])
        pyperclip.copy("CONTENT:"+quote['content'])
        print(pyperclip.paste())
        #print(pyperclip.paste())
        print("AUTHOR: "+quote['author'])
     
    def get_random_quotes(self):
        """Get one or more random quotes from the database"""
        response = requests.get(self.random_quotes, timeout=10)
        quotes = response.json()
        for quote in quotes:
            print("QUOTE_TYPE:",quote['tags'])
            pyperclip.copy("CONTENT: "+quote['content'])
            print(pyperclip.paste())
            print("AUTHOR: "+quote['author'])
    
    def get_list_quotes(self):
        """Get all quotes matching a given query"""
        response = requests.get(self.list_quotes, timeout=10)
        quote = response.json()
        quotes = quote['results']
        for quote in quotes:
            print("QUOTE_TYPE:",quote['tags'])
            pyperclip.copy("CONTENT: "+quote['content'])
            print(pyperclip.paste())
            print("AUTHOR: "+quote['author'])
            print("-------------------")

    def get_author_list(self):
        """This endpoint can be used to list authors"""
        response = requests.get(self.list_authors, timeout=10)
        quote = response.json()
        quotes = quote['results']
        for quote in quotes:
            print(quote['name'])
            pyperclip.copy(quote['bio'])
            print(pyperclip.paste())
            print(quote['description'])
            print('---------------------------')
            
    def get_search_quotes(self,query):
        """This endpoint allows you to search for quotes by keywords,by giving the required query"""
        self.search_quotes += query
        response = requests.get(self.search_quotes, timeout=10)
        quotes = response.json()
        for quote in quotes["results"]:
            print(quote['tags'])
            pyperclip.copy(quote['content'])
            print(pyperclip.paste())
            print(quote['author'])
            print("----------------")
        
        
    def get_search_authors(self,query):
        """his endpoint allows you search for authors by name."""
        self.search_authors += query
        response = requests.get(self.search_authors, timeout=10)
        quotes = response.json()
        for quote in quotes['results']:
            print(quote['name'])
            pyperclip.copy(quote['bio'])
            print(pyperclip.paste())
            print(quote["description"])
            print('----------------------')
        
    def get_tags(self):
        """get a list of all tags"""
        response = requests.get(self.list_tags, timeout=10)
        quotes = response.json()
        for quote in quotes:
            pyperclip.copy(quote['name'])
            print(pyperclip.paste())
            print("----------------")

