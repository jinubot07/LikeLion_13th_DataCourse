# 3-6 실습 - 코스피 정보 가져오기
# 3-6 실습 - 거래량, 장중최고, 52주최고
# 3-7 (추가) 투자자별 매매동향, 프로그램 매매동향
# 3-8 실습 - 시황뉴스

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title,'\n')

# 코스피 정보가져오기
kospi_now = soup.find('em', id='now_value')
print('현재 코스피 : ',kospi_now.text)

# 거래량 천주 정보 가져오기
deal_info = soup.find('td', id='quant')
print('    거래량 : ', deal_info.text)

# 장중 최고, 52주 최고
high_value = soup.find('td', id='high_value')
low_value = soup.find('td', id='low_value')
high52_value = soup.find('td', class_= 'td')
low52_value = soup.find('td', class_= 'td2')
print('  장중최고 : ', high_value.text)
print('  장중최저 : ', low_value.text)
print('  52주최고 : ', high52_value.text)
print('  52주최저 : ', low52_value.text)

