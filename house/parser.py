import requests

from bs4 import BeautifulSoup as BS


def get_request(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError("Invalid url")



def get_html_data(html):
    data_list = []
    soup = BS(html, "html.parser")
    container = soup.find("div", class_="listings-wrapper")
    posts_list = container.find_all("div", class_="listing")
    for post in posts_list:
        top_info = post.find("div", class_="top-info")
        url = top_info.find("a").get("href")
        title = top_info.find("p", class_="title").text.strip()
        title_addition = top_info.find("p", class_="title-addition")
        address = top_info.find("div", class_="address").text.strip()
        desciption = post.find("div", class_="description").text.strip()
        price_dollar = top_info.find("div", class_="price").text.strip()
        price_som = top_info.find("div", class_="price-addition").text.strip()

        if title_addition:
            residential_complex_title = title_addition.text.strip()
            residential_complex_url = title_addition.find("a").get("href")
        else:
            residential_complex_title = None
            residential_complex_url = None

        data = {
            "url": url,
            "title": title,
            "address": address,
            "description": desciption,
            "price_dollar": price_dollar,
            "price_som": price_som,
            "residential_complex_title": residential_complex_title,
            "residential_complex_url": residential_complex_url
        }

        data_list.append(data)
    
    return data_list





def main(category: dict, room_quantity: str = False) -> list:
    if room_quantity:
        url_response = get_request(category.get(room_quantity))
    else:
        url_response = get_request(category)
    data = get_html_data(url_response)

    return data