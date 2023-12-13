import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://stackoverflow.com/questions"

def scrape_stackoverflow(url):

  # Send http request to stackoverflow
  response = requests.get(url)

  # Created soup object that stores the htmlfile which has been read and parsed by BeautifulSoup class
  soup = BeautifulSoup(response.text, "html.parser")

  # We can also create soup object that could store lxml file but for this we need install lxml parser
  # soup = BeautifulSoup(response.text, "lxml")

  # soup object has a method select() that takes a css selector for the first div and store in questions
  questions = soup.select(".s-post-summary")

  # Create a data object and innitially it is an empty list, later we will return data on it after data is populated
  data = []

  # Now select the s-link class to get the title of question and get text then iterate over all the questions
  for question in questions:
    '''
      Create a qu object and innitially it is an empty dictionary. We want here to populate data in dictionary with
      key: value pair.
    ''' 
    qu = {}

    
    # Access the qu dictionary and set key as "Question" and store the result of get.text method of selector
    qu["Questions"] = question.select_one(".s-link").get_text()

    # Access the qu dictionary and set value as "Vote" and store the result of get.text method of selector
    qu["Vote"] = question.select_one(".s-post-summary--stats-item-number").get_text()

    '''
      Now append the result of the itteration in to data variable. Now the list is populated with list of 
      dictionaries with key: value as "Questions": "Vote"
    '''
    data.append(qu)

  # Now return the data so that we can get this.
  return data


# Define a class that takes int, the number of pages and it return all the questions from thoses pages
def crawl_stackoverflow(num_page):

  # Create a all_data object and innitially it is an empty list, later we will return data on it after data is populated
  all_data = []

  # Iterate over a range of page numbers
  for page_num in range(1, num_page +1):
    # Make the url with page numbers
    page_url = f"{url}?tab=newest&page={page_num}"

    # Print the url from where scraping started for each pages
    print(f"Scraping data from {page_url}")

    '''
      Execute the function that scrape the web and get questions title from the html with the passing the page
      url that has the pagination.

      Then extend the privious list with the itterable so the all_date list is populated and ready to return 
      a single list having all the questions and vote counts.
    '''
    all_data.extend(scrape_stackoverflow(page_url))

  return all_data

'''
  Define a function that takes data and export the data into csv and xlsx file. To do this we need to install 
  a package pandas.
'''
def export_data(data):
  # Pandas has a method DataFrame that takes parameter as we pass the data and store in df object
  df = pd.DataFrame(data)
  '''
    df object has method to export data in excel we pass the excel's file name that going to be created and 
    exported. We need to install lxml to export xlsx file.
  '''
  df.to_excel("stackover.xlsx")
  '''
    df object has method to export data in csv as well, we pass the csv's file name that going to be created and 
    exported. Python by default can export csv no need separate package.
  '''
  df.to_csv("stackover.csv")

'''
  To make this module as script also to import as module, we created a if block.
  This conditional(if __name__ == "__main__") block checks if the script is being run as the main program. 
  If so, it calls the crawl_stackoverflow() function, and then export_data() function. This structure 
  is commonly used to make the script reusable as a module and executable as a standalone script.
'''
if __name__ == '__main__':
  data = crawl_stackoverflow(4)
  export_data(data)
  print("Done!")
