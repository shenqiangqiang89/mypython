from collections import namedtuple

website_list = [
('Sohu', 'http://www.google.com/', u'张朝阳'),
('Sina', 'http://www.sina.com.cn/', u'王志东'),
('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('website',['name','url','founder'])

for website in website_list:
    website = Website._make(website)
    print(website)

print(dir(Website))