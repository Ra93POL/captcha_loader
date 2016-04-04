import os, re

def getMaxPicIndex(captcha_dir):
  if not os.path.exists(captcha_dir): os.mkdir(captcha_dir)
  names = os.listdir(captcha_dir)
  maxpic_i = [int(name[:-4]) for name in names if re.findall(r'[0-9]+\.jpg', name)]
  if maxpic_i: return max(maxpic_i)+1
  else: return 1 

def cycle(captcha_dir, start_i, count, func):
  for i in range(start_i,start_i+count):
    i_str = '0'*(4-len(str(i)))+str(i)

    captcha, is_good = func()

    if is_good:
      f = open(os.path.join(captcha_dir, i_str+'.jpg'), 'wb')
      f.write(captcha)
    else:
      f = open(os.path.join(captcha_dir, i_str+'.html'), 'wb')
      f.write(captcha)
    f.close()