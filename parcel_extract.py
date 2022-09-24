from requests import get
from bs4 import BeautifulSoup

class Parcel_Information: 
    def __init__(self, parcel_id, prop_add, sale_price, date_of_sale):
        self.info = {
            'parcel_id': parcel_id,
            'prop_add': prop_add,
            'sale_price': sale_price,
            'date_of_sale': date_of_sale
        }

        self.get_add_details()


    def get_add_details(self):

        url = "http://www.vanderburghassessor.org/Default.aspx?PID=" + self.info['parcel_id']

        response = get(url)

        html_soup = BeautifulSoup(response.text, 'html.parser')

        details = html_soup.find_all('div', {"id": "TabContainer1_TabPanel1"})[0].table

        rows = details.find_all("tr")

        for i in rows:
            row = i.find_all("td")
            counts = len(row)
            for y in range(counts):
                if y % 2 == 0:
                    label = row[y].div.text
                    label = label.replace(" ", "_").strip()[:-1]
                    self.info[label] = row[y+1].div.text
    
    def get_info(self):
        return self.info
