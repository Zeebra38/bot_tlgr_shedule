import bs4
import requests
import wget
import os
from main import update


def download():
    site = requests.get("https://www.mirea.ru/schedule/")
    soup = bs4.BeautifulSoup(site.text, "html.parser")
    rasp = soup.find_all('div', class_='uk-width-1-2 uk-width-auto@s')
    for line in rasp:
        if str(line).find('КБиСП') != -1 and str(line).find('2 курс') != -1 and str(line).find('магистр') == -1 and \
                str(line).find('экз') == -1 and str(line).find('зач') == -1:
            pos_href = str(line).find('http')
            pos_target = str(line).find('target')
            link = str(line)[pos_href:pos_target-2]
            #r = requests.head(link, allow_redirects=True, auth=('user', 'pass'))
            #site1 = 'http://webservices.mirea.ru/upload/iblock/862/КБиСП 2 курс 1 сем.xlsx'
            filename = wget.download(link)
            if os.path.exists('./Raspisanie.xlsx'):
                os.remove('Raspisanie.xlsx')
            if os.path.exists('./Rasp.txt'):
                os.remove('./Rasp.txt')
            os.rename(filename, 'Raspisanie.xlsx')
            # f = open('aaaa.txt', 'w', encoding='utf8', errors='ignore')
            update()
    # # print(rasp)
    # if 4 > 2:
    #     print(4-2)
    # # strings = soup.find_all(string=re.compile('КБиСП'))
    # # for txt in strings:
    # #     print(" ".join(txt.split()))
    # for lok in soup:
    #     s = str(lok)
    #     f.write(s)
    #     if s.find('КБиСП') != -1:
    #         print(s.find('КБиСП'))
    #     if s.rfind('КБиСП')!= -1:
    #         print(s.find('КБиСП'))
    # f.close()
    # f = open('aaaa.txt', 'r', encoding='utf8', errors='ignore')
    # # for line in f:
    # #     if line.find('\n') != -1:
    # #         print(line)
    # f.close()


