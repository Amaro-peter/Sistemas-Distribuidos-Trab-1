import rpyc
import sys
import os

if len(sys.argv) < 2:
    exit("Usage: {} SERVER [PORT]".format(sys.argv[0]))

endpoint = sys.argv[1].replace("tcp://", "")
port = None

if len(sys.argv) >= 3:
    try:
        port = int(sys.argv[2])
    except ValueError:
        exit("PORT must be an integer")

if ":" in endpoint and port is None:
    server, port_text = endpoint.rsplit(":", 1)
    try:
        port = int(port_text)
    except ValueError:
        exit("Invalid endpoint format. Use SERVER:PORT")
else:
    server = endpoint

if port is None:
    port = 18861

conn = rpyc.connect(server, port)
print(conn.root.get_question())