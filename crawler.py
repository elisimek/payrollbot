import requests # library that fetches HTML content of a webpage
from bs4 import BeautifulSoup # parses HTML, allows us to extract data from it

def fetch_page(url):
    """
    Fetches a webpage and prints its title.
    """
    try:
        # Send a request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            html = response.text  # Get the page content
            soup = BeautifulSoup(html, 'html.parser')  # Parse HTML

            # Extract and print the page title
            title = soup.find('title').get_text() if soup.find('title') else "No title found"
            print(f"Page Title: {title}")

        else:
            print(f"Failed to fetch page. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")

# Test the function with a sample website
if __name__ == "__main__":
    url = "https://example.com"  # Replace with any website you want
    fetch_page(url)
