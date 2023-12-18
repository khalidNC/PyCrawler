# Web Scraping:
***
We have learned how to consume API's using request module. However, not every website has an API for us to work with. 
So in situation like that, the only way to get the data we want is to parse the html behind the page we get rid of all html tags, and extarct the actual data, this technique is called web scraping. So we scrape all the html tags and get the actual data we want. And that the things we are going to document here and we will do the project in a separate directory named - PyCrawler. 

I this project we are going to write a program in Python that will extract a list of questions on stackoverflow.com and we refer this kind of program as a web crawler or a web spider. Let's start...

## 1. Create a new project:
    a. Go to terminal and go to user: cd
    b. Make a derictory in user named PyCrawler: mkdir PyCrawler
    c. Go to the directory: cd PyCrawler
    d. Then open the directory in VScode: code .

## 2. Install package and virtual environment:
    a. Install beautifulsoup: pipenv install beautifulsoup4
       This is a very popular python package to extract data from html and xml files.
    b. Install requests module: pipenv install requests
       We also need requests module to download the web page that contains the newest questions on stackoverflow.

## 3. Create py file:
    a. Create a py file in source directory: Let's say crawler.py
    b. Then select the vertual environment in vscode

## 4. Start codding: Download the webpage stackoverflow where the newest questions are available:
    a. On the py file let's import erquests module
```python
        Codes:
                import requets
```
    b. Then we call the the get method to send request to the stackoverflow server.
```python
        Codes:
                import requests

                requests.get("https://stackoverflow.com/questions")
```
    c. Then store the response of the http request in response object
```python
        Codes:
                import requests

                response = requests.get("https://stackoverflow/questions")
```
    d. This response object has an attribute called .text this attribute returns the html content of this web page.
```python
        Codes:
                import requests

                response = requests.get("https://stackoverflow/questions")

                html_content = response.text 
```
    e. So using the html content we can create a beautifulsoup. Let's import beautifulsoup class from bs4 and create 
       BeautifulSpou class object and pass the html_content
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                BeautifulSoup(response.text)
```
    f. Now we need to pass the second argument as type of parser sinces we are going to parse htmlfile, so should
       parse html.parser and store the result in a variable soup.
```python
       Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")
```
       Now, the soup object mirrors the structure of our html document so we can easily navigate the document and
       find the various elements.

## 5. Html and find elements:
    a. Go back to the stackoverflow website and let's right click and inspect element of the first question. So this 
       is the structure of the document what we can see the console. 

    b. Here we have an anchor(<a>) that contains the title of the question. And all the questions are in a <div> with 
       id="questions"
    
    c. Let's look at one of these questions: 
            i. a div with a class, class="s-post-summary"
            ii. inside if this we have 2 div with class:
                1. class="s-post-summary--stats" : this has statistic like vote, views, answers in it
                2. class="s-post-summary--content" : this has content(the question), and summery of the questions

    d. So using our soup object we need find all the elements for the class s-post-summary

## 6. Codding again:
    a. Soup has a method call select that takes a css selector(Basically a string that helps to find an element in an 
       html document) so here we want to get all elements for the class s-post-summary so the codes looks like;
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")
```
        This should return a list so we can store this in a variable called questions. Each item in this list is an instance of a tag class. Let's take a look.
```python
        Codes: 
                print(type(questions[0]))
```
        Here we print the type of first question in the list. And it returns: <class 'bs4 element.tag'>
        So each item in the list is an instance of a tga class.

## 7. Html and css:
    a. Go back to the webpage and find element in console. And you can see, In this case, the tag object represents 
       the <div> in the html.

    b. Now as you see this <div> element has a couple of attributes class and id. These attributes are stored in a 
       dictionary in our tag object. Let's take a look going back to codding.

## 8. Back to codding:
    a. I am going to print attributes of first questions.
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)
```
        This returns: {"id": "question-summary-77634527", "class": ["s-post-summary js-post-summary"]} see it returns
        a dictionary with 2 key:value prair one id another on class. 

    b. Now we can easily read these attributes using square bracket so, we have to access the attributes dictionary 
       because we simply use square bracket(see as below) to get the value of the id attribute.  
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                pirnt(questions[0]["id"])
```
    c. Now if this element does not have this attribute then we may get an exception so a safer way is to call 
       the get method. And we can also optionally supply default value 0.
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                pirnt(questions[0].get("id"), 0)
```
    d. Now we need to get the title of each questions. Go back to html document on the webpage. 

## 9. Back to html doc on website:
    a. Here is the class 's-post-summary' in the html document, 
    b. Inside the div we have 2 divs with class 's-post-summary--stats', and 's-post-summary--content'
    c. Let's expand s-post-summary--content and we can see h3 with an anchor that contains the title of the question
    d. Now loot at the class attribute here, the class of this element is 's-link' 
    e. Bak to our code

## 10. Back to codding again:
    a. The tag object also has the select() method. So remove the get("id", 0) and use select method. and here you can
       pass another css selector in this case, this is 's-link'
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                pirnt(questions[0].select(".s-link"))
```
        Now save the changes and run the program and it returns: a list of bojects, you can see the first object is 
        our anchor. Now in this perticular case we know that each question has 1 title so do not need a list.
        We have another select method called select_one() that returns one object instead of a list. 
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                pirnt(questions[0].select_one(".s-link"))
```
        Save the changes and run the program  once again. This time it returns one anchor and the next step is to get 
        the title. The tag object has method called getText()
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                pirnt(questions[0].select_one(".s-link").getText())
```
        Save the changes and run the program and this time it returns the question. 

    b. Now we need to iterate over all the questions and get the title of each.
```python
        Codes:
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                for question in questions:
                    pirnt(question.select_one(".s-link").getText())
```
        Run the program one more time and it returns all the titles of the questions. 

    c. Now the last step is to get the votes for each question. So go back to the html documet.

## 11. Html document on the webpage:
    a. Expand the div with class s-post-summary
    b. here a child div with class s-post-summary--stats now expand this
    c. here another child div with class s-post-summary--stats-item
    d. here is a span with class s-post-summary--stats-item-number is the votes numbers. 
    e. Copy it and back to the codes

## 12. Back to the codes:
    a. Similarly we print the vote number with the selector ".s-post-summary--stats-item-number" for the itteration
```python
        Codes: 
                import requests
                from bs4 import BeautifulBoup

                response = requests.get("https://stackoverflow/questions")

                soup = BeautifulSoup(response.text, "html.parser")

                questions = soup.select(".s-post-summary")

                print(type(questions[0]))

                print(questions[0].attrs)

                for question in questions:
                    pirnt(question.select_one(".s-link").getText())
                    print(question.select_one(".s-post-summary--stats-item-number").getText())
```
        Now save the changes athe run the program and this time we get the titles as well as the vote counting. 

## 13. Crawl all the pages: 
    So we get all the questions on the first page of the webpage now to get the questions on 
    other pages we need to follow the same approach.
    a. First we need to fimd the pagination component of this page
    b. Here we can find the last page.
    c. So we extract that here and the run the above logic(codes) inside of a loop. In this loop, in each iteration
       we will get the questions for a specific page.
