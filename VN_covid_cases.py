import requests
from bs4 import BeautifulSoup


def crawl():
    url = "https://suckhoedoisong.vn/Covid-19-cap-nhat-moi-nhat-lien-tuc-n168210.html"
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        return text
    else:
        return 'No Response'


def analyzeFile(text):
    soup = BeautifulSoup(text, "html.parser")
        
    box_covid = soup.find(class_="box_covid")

    head_box_covid = box_covid.find(class_="head_box_covid")
    time = head_box_covid.find(class_="fs12").text
    number = head_box_covid.find(class_="fs30").text

    province_cases = []
    table_box_covid = box_covid.find(class_="box_covid_info_city")
    table_body_box_covid = table_box_covid.find("table")
    rows = table_body_box_covid.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        province_cases.append([ele for ele in cols if ele])
    
    with open("box_covid.txt",'w', encoding="utf-8") as text_file:
        text_file.write("{} : {} \n".format(time, number))
        text_file.write("TỈNH | SỐ CA MỚI |TỔNG SỐ CA \n")
        for province in province_cases:
            for data in province:
                text_file.write('{} | '.format(data))
            text_file.write("\n")
        

text = crawl()
analyzeFile(text)
f = open("box_covid.txt", "r", encoding="utf-8")
print(f.read())