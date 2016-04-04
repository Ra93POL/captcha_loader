import urllib2, os, time, common

captcha_dir = "pics_mail7"

start_i = common.getMaxPicIndex(captcha_dir)

'''for i in range(start_i,start_i+1000):
  i_str = '0'*(4-len(str(i)))+str(i)
  image = urllib2.urlopen('https://c.mail.ru/7').read()
  f = open(os.path.join(captcha_dir, i_str+'.jpg'), 'wb')
  f.write(image)
  f.close()

  print i
  #time.sleep(1)'''


def func():
  captcha = urllib2.urlopen('https://c.mail.ru/7').read()
  return captcha, True

common.cycle(captcha_dir, start_i, 1000, func)