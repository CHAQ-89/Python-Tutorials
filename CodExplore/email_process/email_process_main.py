
def main():
	from email_process import email_process, print_msg
	emails = 'quyet@gmail.com' #'chaq@163.com', 'khoaictm@icloud.com']
	email_username, email_domain = email_process(emails)
	print_msg(email_username, email_domain)




if __name__ == "__main__":
	main()
