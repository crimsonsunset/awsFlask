import flask
import socket
from flask.ext.cors import CORS

application = flask.Flask(__name__)
cors = CORS(application)

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
application.debug=True

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


@application.route('/')
def return_token():
    return netcat("challenge2.airtime.com",2323,"")

@application.route('/token')
def return_token():
    return netcat("challenge2.airtime.com",2323,"")


@application.route('/identify')
def identify():
    return netcat("challenge2.airtime.com",2323,"")


if __name__ == '__main__':
    application.run(host='0.0.0.0')