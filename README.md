# UDP Server and Client Example

This repository demonstrates a simple UDP server and client implementation using Python's built-in `socket` library. The server listens for incoming messages from the client, processes them, and sends back a predefined response.

## How It Works

### UDP Server:
- The server listens on port `5050` for incoming messages from clients.
- Once a message is received, the server decodes the message and prints it to the terminal.
- The server then responds with a simple message: `"Hello, I'm UDP Server!"`.

### UDP Client:
- The client sends a message to the server at the specified IP address and port.
- After sending the message, the client waits for the server's response.
- Once the response is received, the client decodes and prints the server's reply.

## Requirements

- Python 3.x (no external dependencies, uses the built-in `socket` module)
