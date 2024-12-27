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

Licensed under the MIT License - see the LICENSE file for details.


### Key Features:
1. **Single Script**: Both server and client code are combined in a single file (`UDP_server_client.py`) using threading to simulate parallel execution.
2. **Threading**: The server and client are run in separate threads to allow simultaneous execution within the same script.
3. **Instructions**: The `README` contains step-by-step instructions on how to run the script.

This version of the `README.md` consolidates everything into one code section and provides the user with a simple way to run both the server and the client in a single script.

