import requests
from bs4 import BeautifulSoup

# Step 1: Send GET request to the news website
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find all headline tags (h2)
    headlines = soup.find_all("h2")

    # Step 4: Save headlines in a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            text = h.get_text(strip=True)
            if text:
                file.write(text + "\n")

    print("Headlines saved successfully in headlines.txt")

else:
    print("Failed to retrieve website. Status code:", response.status_code)
