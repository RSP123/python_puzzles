# This program fetchs the data from webpage
from bs4 import BeautifulSoup
# Function for the fetching the data
def web_page(page):
    # Web page opening with Get response
    response = request.get(page)

    # Connection status
    if response.status_code == 200:

        # parsing from html
        result = BeautifulSoup(response.text,'html.parser')

        # list which contains data
        tag=result.find()


    return


# Main Function
if __name__=="__main__":
    page = 'www.google.com'
    web_page(page)
    print("Connection Success ")
    print("fetching the latest data")
    
