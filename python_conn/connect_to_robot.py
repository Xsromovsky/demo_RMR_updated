import socket
import struct

# Robot and RPLIDAR configuration
ROBOT_IP = '192.168.1.3'  # Replace with the actual IP address of the robot
RPLIDAR_PORT = 52999      # The port number for sending commands to RPLIDAR
LISTEN_PORT = 5299        # The local port for receiving RPLIDAR data

# Create a UDP socketd for sending commands
sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_send.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Create a UDP socket for receiving data
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind(('', LISTEN_PORT))  # Bind to the listening port

def send_command(command):
    """Send a command to the RPLIDAR via the robot."""
    sock_send.sendto(command.encode(), (ROBOT_IP, RPLIDAR_PORT))

def receive_rplidar_data():
    """Receive data from RPLIDAR."""
    try:
        while True:
            data, addr = sock_recv.recvfrom(1024)  # Buffer size is 1024 bytes
            print("Received message:", data.decode())
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == '__main__':
    # Sending command to start RPLIDAR data stream
    send_command('')
    print("Command sent to start RPLIDAR. Listening for data...")
    
    # Listen for incoming data from RPLIDAR
    receive_rplidar_data()
    
    # Close sockets
    sock_send.close()
    sock_recv.close()
