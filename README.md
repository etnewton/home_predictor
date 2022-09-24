# home_predictor
Model to predict sale price of home

In 2020 a new house was purchased so needed to sale the existing house. Wanted to get an estimate prior to relying on a realtor.

To get an estimate I utilized beautifulsoup to scrape our country assessor site houses that sold in the last year in our neighborhood. First manually extracted and search for the houses in our neighbor. This ended up being around 40 different houses in the area. Once these were identified ran script to pull in the assessor data and store as a pipe delimited csv file.

To keep things simple a linear regression model was fit utilizing sklearn. After this was fit prediction was ran using our house details.

The model output value of 104,013.57. A few months later we put our house on the market at the advisement of our realtor for price of 97,000. We got multiple offers same day, 2 for 105k and 1 for 110k, and ultimately accepted one of the 105k offers due to other terms of the offer.

Believe this was ultimately a decent model and should have pushed back on our realtor to put on market for higher amount.
