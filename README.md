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

## Troubleshooting and FAQs

1. Connection Issues
   - Connection to the Server: Ensure that the server is up and running. Check the specified SERVER_HOST and SERVER_PORT in the client.py file to match the server's details.
   - Firewall Settings: Verify that your firewall allows communication through the specified server port. Adjust firewall settings if necessary.
2. Customization
   - Changing Username: If you joined anonymously and wish to change your username, simply exit the chat using 'q' and restart the client with a new username.
3. Feedback and Issues
   - Reporting Issues: If you encounter any issues or bugs, please open an issue on the GitHub repository. Provide detailed information about the problem, and we'll work to address it.
   - Feature Requests: Feel free to suggest new features or improvements. We appreciate user feedback and strive to enhance the chat app based on community input.
## Development and Contributions

1. Setting Up a Development Environment
   - Clone the repository: git clone https://github.com/yourusername/ChatApp.git
   - Install dependencies: pip install -r requirements.txt
   - Make your changes and test them locally.
2. Submitting Changes
   - Fork the repository.
   - Create a new branch for your changes: git checkout -b feature/your-feature
   - Commit your changes: git commit -m "Add your feature"
   - Push the branch to your fork: git push origin feature/your-feature
   - Open a pull request on the main repository.
3. Code Style
   Follow the existing code style to maintain consistency. Ensure your code is well-documented, and add comments where necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
