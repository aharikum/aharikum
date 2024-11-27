
import sys


def exit():
  sys.exit(0)



def check_key(key):
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
	flag = open('flag.txt', 'r').read()
	#flag = flag[:-1]
	flag = flag.strip()
	if key == "wooimaboutto_makeanamefor_myselfhere63":
		print("As promised: ", flag)
	else:
		print("Wrong math... Get the right key!")

while(True):
  try:
    print('Enter the key for your flag:')
    user_input = input('==> ')
    check_key(str(user_input))
  except Exception as e:
    print(e)
    break
