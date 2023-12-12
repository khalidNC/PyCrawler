import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://stackoverflow.com/questions"

def scrape_stackoverflow(url):

  # Send http request to stackoverflow
  response = requests.get(url)

  # Created soup object that stores the htmlfile which has been read and parsed by BeautifulSoup class
  # soup = BeautifulSoup(response.text, "html.parser")
  soup = BeautifulSoup(response.text, "lxml")

  # soup object has a method select() that takes a css selector for the first div and store in questions
  questions = soup.select(".s-post-summary")

  data = []

  # Now select the s-link class to get the title of question and get text then iterate over all the questions
  for question in questions:
    qu = {}
    qu["Questions"] = question.select_one(".s-link").get_text()
    # print(question.select_one(".s-link").get_text())

    qu["Vote"] = question.select_one(".s-post-summary--stats-item-number").get_text()
    #Print the vote count for each question
    # print(question.select_one(".s-post-summary--stats-item-number").get_text())

    data.append(qu)
  # print(data)

  return data

# Define a class that takes int, the number of pages and it return all the questions from thoses pages
def crawl_stackoverflow(num_page):

  # Iterate over a range of page numbers
  for page_num in range(1, num_page +1):
    # Make the url with page numbers
    page_url = f"{url}?tab=newest&page={page_num}"

    # Return the url from where scraping started for each pages
    print(f"Scraping data from {page_url}")

    # Execute the function that scrape the web and get questions title from html
    scrape_stackoverflow(page_url)

# Execute the function that goes to each page within the range and scrape
crawl_stackoverflow(4)

def export_data(data):
  df = pd.DataFrame(data)
  df.to_excel("stackover.xlsx")
  df.to_csv("stackover.csv")

if __name__ == '__main__':
  data = scrape_stackoverflow(url)
  print(data)
  export_data(data)
  print("Done!")