
import sys
def check_key(key):
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
	flag = open('flag.txt', 'r').read()
	#flag = flag[:-1]
	flag = flag.strip()
	if key == "whoop_whoop_thats_the_sound_of_da_police":
		print("As promised: ", flag)
	else:
		print("Busted! Don't try smuggling data while I'm in charge!")

if __name__ == "__main__":
  sys.stdout.flush()
  print('Enter the key for your flag:')
  user_input = input('==> ')
  check_key(str(user_input))
  sys.stdout.flush()


    