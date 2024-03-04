import socket
from threading import Thread, Lock
import re
import logging

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"

client_sockets = set()
client_sockets_lock = Lock()
running = True  # Variable to control the server loop

# Configure the logging
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

def log_message(message):
    logging.info(message)

def broadcast(message):
    # Regular expression to match URLs
    url_pattern = re.compile(r'https?://\S+')

    # Profanity filter - add or modify the list of inappropriate words
    profanity_list = ["badword1", "badword2", "badword3"]

    with client_sockets_lock:
        clients_to_remove = set()
        for cs in client_sockets:
            try:
                # Replace URLs with clickable hyperlinks
                message_with_links = re.sub(url_pattern, lambda x: f'\033[34m{x.group()}\033[0m', message)

                # Check for profanity in the message
                if any(word in message.lower() for word in profanity_list):
                    message_with_links = "[Profanity Filter] Message blocked due to inappropriate content."

                cs.send(message_with_links.encode())
            except Exception as e:
                error_message = f"[!] Error sending message to {cs.getpeername()}: {e}"
                print(error_message)
                log_message(error_message)

                # If sending fails, add the client to the removal set
                clients_to_remove.add(cs)

        # Remove disconnected clients
        for client in clients_to_remove:
            client_sockets.remove(client)
            client.close()

def handle_client_messages(client_socket):
    try:
        while running:
            msg = client_socket.recv(1024).decode()
            if not msg:
                # If an empty message is received, it means the client disconnected
                disconnect_message = f"[!] {client_socket.getpeername()} disconnected."
                print(disconnect_message)
                log_message(disconnect_message)

                # Broadcast leave message to all connected clients
                leave_message = f"[Server] User {client_socket.getpeername()} left the chat."
                broadcast(leave_message)
                break

            msg = msg.replace(separator_token, ": ")

            # Log the received message
            received_message = f"[{client_socket.getpeername()}] {msg}"
            print(received_message)
            log_message(received_message)

            # Broadcast the message to all connected clients
            broadcast(msg)

    except ConnectionAbortedError:
        # Handle cases where the connection was forcibly closed by the client
        disconnect_message = f"[!] {client_socket.getpeername()} forcibly disconnected by the client."
        print(disconnect_message)
        log_message(disconnect_message)

        # Broadcast leave message to all connected clients
        leave_message = f"[Server] User {client_socket.getpeername()} left the chat."
        broadcast(leave_message)

    except Exception as e:
        error_message = f"[!] Error handling messages for {client_socket.getpeername()}: {e}"
        print(error_message)
        log_message(error_message)

    finally:
        # Close the client socket when the thread ends
        with client_sockets_lock:
            clients_to_remove = set([cs for cs in client_sockets if cs == client_socket])
            for cs in clients_to_remove:
                client_sockets.remove(cs)
                cs.close()

try:
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    start_message = f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}"
    print(start_message)
    log_message(start_message)

    while running:
        try:
            client_socket, client_address = server_socket.accept()
            connect_message = f"[+] {client_address} connected."
            print(connect_message)
            log_message(connect_message)

            # Broadcast join message to all connected clients
            join_message = f"[Server] User {client_address} joined the chat."
            broadcast(join_message)

            with client_sockets_lock:
                client_sockets.add(client_socket)
            
            # Start a new thread to handle the client's messages
            t = Thread(target=handle_client_messages, args=(client_socket,))
            t.daemon = True
            t.start()

        except Exception as e:
            error_message = f"[!] Error accepting client connection: {e}"
            print(error_message)
            log_message(error_message)

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) to gracefully stop the server
    shutdown_message = "\n[!] Server shutting down..."
    print(shutdown_message)
    log_message(shutdown_message)
    running = False

finally:
    # Gracefully close client sockets
    with client_sockets_lock:
        for cs in client_sockets:
            cs.close()

    # Close server socket
    server_socket.close()

