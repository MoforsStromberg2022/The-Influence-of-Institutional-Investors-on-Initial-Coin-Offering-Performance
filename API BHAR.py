# The Influence of Institutional Investors on Initial Coin Offering Performance
# Rebecka: 24864@student.hhs.se
# Maja: 24845@student.hhs.se

import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

# To run this code you first have to put in your own path to the CSV file for API Datum 1, 180, 360
# Furthermore, you have to put in your own API key from CoinMarketCap
# ID means the CoinMakretCap identifyer and Dag 1 is day one and Dag 2 is day 2 of trading
# To get day 180 and day 181, just change the names from Dag 1 to Dag 180
# Now you are ready to run the file

def read_data():
    data = pd.read_csv("PATH", delimiter=";")

    data["Dag 1"] = pd.to_datetime(data["Dag 1"])

    data = data[["Id", "Dag 1", "Dag 2"]].dropna()

    return data


def call_api(coinmarketcap_id, start_date, end_date):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/historical'

    parameters = {
        "id": coinmarketcap_id,
        'time_start': start_date,
        'time_end': end_date,
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '(Personal API key)',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def main():
    df = read_data()

    list = []
    for i in range(len(df)):
        time.sleep(2)
        api_data = call_api(int(df.loc[i, "Id"]), df.loc[i, "Dag 1"], df.loc[i, "Dag 2"])
        if api_data["status"]["error_code"] == 0:
            list.append(api_data)
        else:
            print(api_data)
            continue

    new_df = pd.DataFrame(list)
    print(new_df)
    new_df.to_csv("new_data_365.csv")


if __name__ == "__main__":
    main()
