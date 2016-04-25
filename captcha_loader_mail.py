import os, time, common
from urllib import request

captcha_dir = "pics_mail7"

start_i = common.getMaxPicIndex(captcha_dir)

def func():
  captcha = request.urlopen('https://c.mail.ru/7').read()
  return captcha, True

common.cycle(captcha_dir, start_i, 1000, func)
