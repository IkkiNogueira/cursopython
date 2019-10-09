# https://www.game-debate.com/hardware/index.php?make=AMD&model=R-500%20Series&type=Desktop%20Graphics%20Card
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:\\Users\\Usuario\\Documents\\Python\\cursopython\\driver\\chromedriver.exe")

vga = []
release = []

driver.get("https://www.game-debate.com/hardware/index.php?make=AMD&model=R-500%20Series&type=Desktop%20Graphics%20Card")

content = driver.page_source
soup = BeautifulSoup(content)
page = soup.find_all('div', attrs={'class':'hardwareRow'})

for a in page:
    deriv = a.find('div', attrs={'class': 'hardwareDeriv'})
    date = a.find('div', attrs={'class': 'hardwareRelease'})

    vga.append(deriv.text)
    release.append(date.text)
    continue

df = pd.DataFrame({'Placa de video': vga, 'Data de lançamento': release})
df.to_csv('C:\\Users\\Usuario\\Documents\\Python\\cursopython\\output\\resultados.csv', index=False, encoding='utf-8')
