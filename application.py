from flask import Flask
import socket
# from flask.ext.cors import CORS


global token

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    global token
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        token = data
        print "Received:", data

    # print(token)
    print "Connection closed."
    s.close()
    return token


app = Flask(__name__)
# cors = CORS(app)

@app.route("/")
def helloWorld():
    return netcat("challenge2.airtime.com",2323,"")

# print(zz)

if __name__ == '__main__':
    app.run(host='0.0.0.0')