import re
from bs4 import BeautifulSoup

f = open('test.html', 'r', encoding='utf-8')
bs = BeautifulSoup(f, 'html.parser')
print(bs.prettify())

# t = "ui(event, 'hyunju3685',3,'소소한','10050146','me', 'false', 'true', 'joonggonara', 'false', '0'); return false;"
# print(t.split("'")[1])


# text = [
#     '010-2182-2220',
#     '010    2182 2220'
# ]



# for t in text:
#     phone = re.compile('\d{3}\s*-{0,1}\s*\d{4}\s*-{0,1}\s*\d{4}').finditer(t)
#     for n in phone:
#         test = re.sub('\s+', '-', n.group())
#         print(test)