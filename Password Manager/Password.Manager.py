import secrets
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

lengths = [22, 28, 34, 40]
for length in lengths:
    print ('Password is: ' + ''.join(secrets.choice(chars) for _ in range(length)))

wait = input('PRESS ENTER TO EXIT')
