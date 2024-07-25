import warnings
from bs4 import BeautifulSoup
import requests

def get_bcv_exchange_rates():
    url = "https://www.bcv.org.ve"
    apiResponse = {
        'error': False,
        'error_message': [],
        'data': {}
    }

    try:
        response = requests.get(url=url)
    except requests.exceptions.SSLError:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(url=url, verify=False)
        except Exception as err:
            apiResponse['error'] = True
            apiResponse['error_message'].append(str(err))
    except Exception as err:
        apiResponse['error'] = True
        apiResponse['error_message'].append(str(err))

    if apiResponse['error']:
        return apiResponse

    soup = BeautifulSoup(response.text, "html.parser")

    currencies = ["euro", "yuan", "lira", "rublo", "dolar"]
    for currency in currencies:
        section = soup.find("div", {"id": currency})
        if section:
            value = section.find("strong").text.strip().replace(',', '.')
            symbol = section.find("span").text.strip()
            apiResponse['data'][currency] = {'symbol': symbol, 'value': value}
        else:
            apiResponse['data'][currency] = {'symbol': None, 'value': None}

    effective_date = soup.find("span", {"class": "date-display-single"})
    apiResponse['data']['effective_date'] = effective_date.text.strip() if effective_date else None

    return apiResponse
