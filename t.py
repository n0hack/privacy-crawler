# import re
# from bs4 import BeautifulSoup

s = '01000000000'
print(s[:3] + '-' + s[3:7] + '-' + s[7:])


# f = open('test.html', 'r', encoding='utf-8')
# bs = BeautifulSoup(f, 'html.parser')
# f.close()

# p = r'아이디mj8396이메일'

# # 리스트
# t = bs.select('#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr')
# article_pattern = re.compile(r'articleid=\d+')
# # Article ID(articleid=161322100)랑 
# # Blogger ID(onclick="ui(event, 'hyunju3685',3,'소소한','10050146','me', 'false', 'true', 'joonggonara', 'false', '0'); return false;") 출력

# # blogger = 'mj8396'
# blogger = 'hyunju3685'
# article_id_list = []

# for article in t:
#     # 답글 패스
#     try:
#         article_id = article.get_text().split()[0]
#     except:
#         continue

#     if blogger in article.select('a.m-tcol-c')[0]['onclick']:
#         print('블로거의 글 : id({0}), writer({1})'.format(article_id, blogger ))
#         article_id_list.append(article_id)
#     else:
#         print('블로거의 글이 아님')

# print('{0} blogger의 article'.format(blogger))
# for article_id in article_id_list:
#     print(article_id)

# f = open('hyunju_157805371.html', 'r', encoding='utf-8')
# bs = BeautifulSoup(f, 'html.parser')

# ttt=  bs.select('.article_container')[0].get_text()
# phone = re.compile('\d{3}\s*-{0,1}\s*\d{4}\s*-{0,1}\s*\d{4}').findall(ttt)

# print(len(phone))
# for n in phone:
#     test = re.sub('\s+', '-', n)
#     print(test)
# f.close()


# print(t[0].get_text().split())
# matchOB = article_pattern.match(t[0].get_text())


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