# ChatServer

Welcome to the Chat App with Python Sockets! This real-time chat application facilitates seamless communication among users through a server-client architecture. Built with Python sockets, it offers a range of features to enhance your chatting experience.

## Features

1. Real-Time Communication
   - Instantly connect and communicate with other users.
   - Messages are delivered in real-time, creating a responsive chat environment.
2. Anonymity and Customization
   - Join anonymously or choose a custom username.
   - Personalize your chatting experience to your liking.
3. Colorful Interface
   - Each user is assigned a unique color for easy identification.
   - A visually appealing interface enhances the chat experience.
4. Profanity Filter
   - Maintain a friendly atmosphere with an automatic profanity filter.
   - Inappropriate language is replaced, ensuring a positive environment.
5. URL Highlighting
   - URLs shared in the chat are highlighted for easy identification.
   - Clickable hyperlinks make navigation convenient.
  
## Getting Started

1. Server Setup:
   - Run server.py on a machine with a reachable IP address.
   - Ensure the specified SERVER_HOST and SERVER_PORT in server.py are accessible.
2. Client Setup:
   - Run client.py on individual machines to connect to the server.
   - Choose to join the chat anonymously or provide a custom username.
3. Start Chatting:
   - Begin chatting with other users in real-time.
   - Use the provided commands to interact with the chat.
  
## Commands

- Anonymous Join:
  - When prompted, type 'y' to join the chat anonymously.
- Named Join:
  - When prompted, type 'n' to enter your desired username.
- Sending Messages:
  - Type your message and press Enter to send.
  - Messages are limited to 200 characters.
- Quitting the Chat:
  - Type 'q' to exit the chat gracefully.

## Dependencies

- Colorama: Terminal color formatting.
- Plyer: Desktop notifications.
