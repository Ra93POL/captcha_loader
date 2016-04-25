import re, os, common
from urllib import request

#pattern = r'https\:\/\/nb\.captcha\.yandex\.net\/image\?key\=[0-9a-zA-Z]+'
pattern = rb'[a-z]+\.captcha\.yandex\.net\/image\?key=[0-9a-zA-Z]+'
captcha_dir = "pics_yandex"

start_i = common.getMaxPicIndex(captcha_dir)

def func():
  page = request.urlopen('https://passport.yandex.ru/registration').read()
  url = re.findall(pattern, page)
  if url:
    return request.urlopen('https://'+str(url[0], 'utf-8')).read(), True
  else:
    return page, False

common.cycle(captcha_dir, start_i, 1000, func)
