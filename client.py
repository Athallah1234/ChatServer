import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init
import re
from plyer import notification
import selectors

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
          ]

client_color = random.choice(colors)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002

try:
    socket.inet_aton(SERVER_HOST)
    assert 0 < SERVER_PORT < 65535
except (socket.error, AssertionError):
    print("[!] Invalid server host or port.")
    exit()

separator_token = "<SEP>"

try:
    s = socket.socket()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
except Exception as e:
    print(f"[!] Error: {e}")
    exit()

# Setup selector untuk I/O non-blok
sel = selectors.DefaultSelector()
sel.register(s, selectors.EVENT_READ, data=None)

def profanity_filter(message):
    profanity_list = ["badword", "inappropriate", "offensive"]
    message_lower = message.lower()
    return any(word in message_lower for word in profanity_list)

def notify_new_message(sender, message):
    notification_title = f"New Message from {sender}"
    notification_text = f"{sender}: {message}"
    notification.notify(
        title=notification_title,
        message=notification_text,
        timeout=10
    )

def send_welcome_message():
    welcome_message = f"{client_color}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Welcome to the chat, {name}!{Fore.RESET}"
    s.send(welcome_message.encode())

# Additional validation function
def validate_message(message):
    if not message or len(message) > 200:
        print("[!] Invalid message. Message must be between 1 and 200 characters.")
        return False
    return True

# Additional validation for user input
def validate_user_input(user_input):
    if not user_input:
        print("[!] Invalid input. Please enter a non-empty value.")
        return False
    return True

while True:
    anonymous_mode = input("Do you want to join anonymously? (y/n): ").lower()
    if anonymous_mode == 'y':
        name = "Anonymous" + str(random.randint(1000, 9999))
        break
    elif anonymous_mode == 'n':
        while True:
            name = input("Enter your name: ")
            if not validate_user_input(name) or len(name) > 30:
                print("[!] Please enter a valid name (up to 30 characters).")
            else:
                break
        break
    else:
        print("[!] Invalid option. Please enter 'y' or 'n'.")

# Send welcome message after setting the name
send_welcome_message()

def listen_for_messages():
    url_pattern = re.compile(r'https?://\S+')

    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            try:
                message = s.recv(1024).decode()
                if not message:
                    print("[!] Connection closed by the server.")
                    sel.unregister(s)
                    break

                message_with_links = re.sub(url_pattern, lambda x: f'{Fore.BLUE}{x.group()}{Fore.RESET}', message)

                print("\n" + message_with_links)

                if name.lower() in message.lower():
                    notify_new_message(sender="Chat", message=message)

            except Exception as e:
                print(f"[!] Error: {e}")
                sel.unregister(s)
                break

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

try:
    while True:
        to_send = input()

        if not validate_message(to_send) or profanity_filter(to_send):
            continue

        if to_send.lower() == 'q':
            leave_message = f"{client_color}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {name} left the chat.{Fore.RESET}"
            s.send(leave_message.encode())
            break

        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        s.send(to_send.encode())

except Exception as e:
    print(f"[!] Error: {e}")

s.close()

