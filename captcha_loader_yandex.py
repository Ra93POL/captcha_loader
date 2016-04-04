import urllib2 as u, re, os, common

#pattern = r'https\:\/\/nb\.captcha\.yandex\.net\/image\?key\=[0-9a-zA-Z]+'
pattern = r'[a-z]+\.captcha\.yandex\.net\/image\?key=[0-9a-zA-Z]+'
captcha_dir = "pics_yandex"

start_i = common.getMaxPicIndex(captcha_dir)

'''for i in range(start_i,start_i+1000):
  i_str = '0'*(4-len(str(i)))+str(i)
  page = u.urlopen('https://passport.yandex.ru/registration').read()
  url = re.findall(pattern, page)
  #print url
  if url:
    f = open(os.path.join(captcha_dir, i_str+'.jpg'), 'wb')
    captcha = u.urlopen('https://'+url[0]).read()
    f.write(captcha)
  else:
    f = open(os.path.join(captcha_dir, i_str+'.html'), 'wb')
    f.write(page)
  f.close()'''

def func():
  page = u.urlopen('https://passport.yandex.ru/registration').read()
  url = re.findall(pattern, page)
  if url:
    return u.urlopen('https://'+url[0]).read(), True
  else:
    return page, False

common.cycle(captcha_dir, start_i, 1000, func)