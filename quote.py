from portfolio import Quotable
import requests


my_result = Quotable(        
    random_quote = "https://api.quotable.io/random",
    random_quotes = "https://api.quotable.io/quotes/random",
    list_quotes = "https://api.quotable.io/quotes",
    list_authors = "https://api.quotable.io/authors",
    search_quotes = "https://api.quotable.io/search/quotes?query=",
    search_authors = "https://api.quotable.io/search/authors?query=",
    list_tags = "https://api.quotable.io/tags",
)
while True:
    try:
        categories = "random quote","random quotes","list quotes","list authors","search quotes","search authors","list quote topics"
        print(categories)
        print('enter quit to exit')
        user_option = input("choose the type of quote you need from the category lists: ")
        if user_option.lower() == "random quote":
            my_result.get_random_quote()
            print("The content has been copied to your clipboard: ")
    
        elif user_option.lower() == "random quotes":
            my_result.get_random_quotes()
            print("the content will be copied to your clipboard: ")
            
        elif user_option.lower() == "list quotes":
            my_result.get_list_quotes()
            print("the last content will be copied to your clipboard: ")

            
        elif user_option.lower() == "list authors":
            my_result.get_author_list()
            print("the biography of the last author will be copied to your clipboard: ")
           
        elif user_option.lower() == "list quote topics":
            my_result.get_tags()
            print("the last topic will be saved to your clipboard: ")
            
        elif user_option.lower() == "search quotes":
            query = input("Enter the quote you are looking for: ")
            my_result.get_search_quotes(query)
            print("the last content will be copied to your clipboard: ")

            
        elif user_option.lower() == "search authors":
            query = input("Enter the author you are looking for: ")
            my_result.get_search_authors(query)
            print("the biography of the  author will be copied to your clipboard: ")


        elif user_option.lower() == "quit":
            break
        
    except Exception as error:

        if requests.exceptions.ConnectTimeout:
            print("Timeout!!!:Check your internet connection and try again.")
        elif Exception:
            print(error)
            print("Please check the instruction and try again")
    
