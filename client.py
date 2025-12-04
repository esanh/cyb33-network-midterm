# client.py
"""
Simple TCP client for midterm.
- Connects to localhost:5000
- Sends a message typed by the user
- Receives a response from the server
"""

import socket

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def run_client():
    # Ask user for a message so your screenshots show interaction
    message = input("Enter a message to send to the server: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)  # seconds

    try:
        print(f"[CLIENT] Trying to connect to {HOST}:{PORT}")
        client_socket.connect((HOST, PORT))
        print("[CLIENT] Connected to server")

        # Send message
        client_socket.sendall(message.encode("utf-8"))
        print("[CLIENT] Message sent")

        # Wait for response
        data = client_socket.recv(BUFFER_SIZE)
        if data:
            response = data.decode("utf-8")
            print(f"[CLIENT] Response from server: {response}")
        else:
            print("[CLIENT] No response received from server")

    except ConnectionRefusedError:
        print("[CLIENT] Connection failed, server is not running")
    except socket.timeout:
        print("[CLIENT] Timed out waiting for server response")
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Disconnected")


if __name__ == "__main__":
    run_client()
