
def email_process(email):
	#quyet@gmail.com
	email_username = email[0: email.index('@')]
	email_domain = email[email.index('@') + 1:]
	return [email_username, email_domain]
def print_msg(email_username, email_domain):
	print(f'Email username is: {email_username}')
	print(f'Email domain is: {email_domain}')

def main():
	email = input('Please enter your email address: ').strip()
	# print(f'hello {email}')
	email_username, email_domain = email_process(email)
	print_msg(email_username, email_domain)

if __name__ == "__main__":
	main()


# Bóc tách email thành username và domain
#	