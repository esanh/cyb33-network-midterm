# server.py
"""
Simple TCP server for midterm.
- Listens on localhost:5000
- Accepts a single client at a time
- Receives a message and sends a response
"""

import socket

HOST = "127.0.0.1"   # localhost
PORT = 5000          # you can change this, but keep client in sync
BUFFER_SIZE = 1024


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow quick restart of the server during testing
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            print("[SERVER] Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            print(f"[SERVER] Connection established with {client_address}")

            try:
                # Receive data from client
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    print("[SERVER] No data received, closing connection")
                else:
                    message = data.decode("utf-8")
                    print(f"[SERVER] Received from client: {message}")

                    # Create a response
                    response = f"Server received: {message}"
                    client_socket.sendall(response.encode("utf-8"))
                    print("[SERVER] Response sent to client")

            except ConnectionResetError:
                print("[SERVER] Connection reset by client")
            except Exception as e:
                print(f"[SERVER] Error while handling client: {e}")
            finally:
                client_socket.close()
                print("[SERVER] Client disconnected cleanly")

    except OSError as e:
        print(f"[SERVER] Socket error during setup: {e}")
    except KeyboardInterrupt:
        print("\n[SERVER] Keyboard interrupt, shutting down")
    finally:
        server_socket.close()
        print("[SERVER] Server socket closed")


if __name__ == "__main__":
    start_server()
