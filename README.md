# pyp2p

Simple library to send and receive objects.

## Usage

The sample code is shown below.

Server

```python
import socket
from pyp2p import Pyp2p


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 50000))
sock.listen(1)
conn, addr = s.accept()


peer = Pyp2p(conn)
peer.send_str("automata")
peer.send_int(255)
peer.send_dict({"coppelius": "coppelia"})
```

Client

```python
import socket
from pyp2p import Pyp2p


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 50000))

peer = Pyp2p(sock)
peer.recv_str()  # automata
peer.recv_int()  # 255
peer.recv_dict()  # {"coppelius": "coppelia"}
```

If you want to send and receive your own objects etc, please use `send_object` and `recv_object`.

```python
class Example:
	def __init__(self):
		pass


example = Example()

peer.send_object(example)
peer.recv_object()
```

## Founder

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
