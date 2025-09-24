# UDP Sender & Receiver

This project demonstrates a simple UDP sender and receiver implementation in Python.

## Files

- `udp_sender.py` – Contains the `UdpSender` class to send UDP messages.
- `udp_receiver.py` – Contains the `UdpReceiver` class to receive UDP messages.
- `main.py` – Provides a command-line interface to choose between sending or receiving messages.

## Requirements

- Python 3.10+ (for `match-case` statement)
- No external libraries required (uses Python standard library)

## Usage

1. Clone or download this repository.
2. Run the program:

```bash
python3 main.py
```

3. Choose a mode:
   - **1** → Run as UDP Sender
   - **2** → Run as UDP Receiver
   - **0** → Exit

### Example: Sending a Message

Run `main.py` and choose option **1**:

```
Enter receiver ip: 127.0.0.1
Enter receiver port: 5000
Enter the message: Hello World!
```

### Example: Receiving a Message

Run `main.py` and choose option **2**:

```
Enter receiver ip: 127.0.0.1
Enter receiver port: 5000
```

The program will wait for incoming messages and display them.

## Notes

- The `__pycache__` folder is automatically removed after sending a message.
- Make sure sender and receiver use the same IP and port.
- Works on localhost or across networked machines (ensure firewall rules allow UDP traffic).
