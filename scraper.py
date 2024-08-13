import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse

def scrape_website(url):
  """
  Scrapes a given website and stores the extracted data in a CSV file with the same name as the URL domain.

  Args:
    url: The URL of the website to scrape.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for error HTTP statuses

    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract links and store them in a list
    data = []
    links = soup.find_all('a')
    for link in links:
      href = link.get('href')
      if href:
        data.append({'link': href})

    # Extract domain from URL
    domain = urllib.parse.urlparse(url).netloc
    output_file = f"{domain}.csv"

    # Write data to CSV file
    with open(output_file, 'w', newline='') as csvfile:
      fieldnames = ['link']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(data)

    print(f"Data extracted and saved to {output_file}")

  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  url = input("Enter the URL to scrape: ")
  scrape_website(url)
