import requests
import hashlib
import sys
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def matching(hashes , pass_tail):
	hashes = (lines.split(':')for lines in hashes.text.splitlines())
	for h,count in hashes:
		if h == pass_tail:
			return count
	return 0

def hashing(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char , tail = sha1password[:5] , sha1password[5:]
	response = request_api_data(first5_char)
	return matching(response, tail)

def main(args):
	for password in args:
		count = hashing(password)
		if count:
			print(f'Oops!! Your password : {password} has been pawned {count} times')
		else:
			print(f'Good to go!!!!')

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))