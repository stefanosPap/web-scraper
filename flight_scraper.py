import requests
from bs4 import BeautifulSoup

def scrape_skyscanner(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    flights = soup.find_all('div')
    
    for flight in flights:
        # Extract flight details such as price, departure time, arrival time, etc.
        price = flight.find('span', class_='price').text
        departure_time = flight.find('span', class_='depart-time').text
        arrival_time = flight.find('span', class_='arrival-time').text

        # Print or store the extracted data
        print(f"Price: {price}, Departure Time: {departure_time}, Arrival Time: {arrival_time}")

url = 'https://gr.skyscanner.com/transport/flights/skg/vie/240622/240624/?adultsv2=1&cabinclass=economy&childrenv2=&departure-times=0-990,0-1439&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=1'
scrape_skyscanner(url)