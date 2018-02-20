import requests, bs4
# -*- coding: utf-8 -*-
my_file = open('snake.txt', 'w')

s=requests.get('https://sinoptik.com.ru/погода-москва')

b=bs4.BeautifulSoup(s.text, "html.parser")

p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()

p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()

p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()

p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()

print('Утром :' + pogoda1 + ' ' + pogoda2 + "\n" 'Днём :' + pogoda3 + ' ' + pogoda4)


p=b.select('.rSide .description')
pogoda=p[0].getText()

# -*- coding: utf-8 -*-
my_file = open('snake.txt', 'w')
text_for_file =('Утром :' + pogoda1 + '' + pogoda2 + "\n" 'Утром:' ' ' + pogoda3 + '' + pogoda4 + "\n" + pogoda)

my_file.write(text_for_file)

my_file.close()

print(pogoda.strip())


