import flask
import socket
import urllib
from flask.ext.cors import CORS
from flask import request

application = flask.Flask(__name__)
cors = CORS(application)

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
# application.debug=True

global token

def netcat(hostname, port, content):
    print("netcatting -- " + content)
    content = urllib.quote(content.encode('utf-8'))
    print("netcattingsss -- " + content)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    global token
    while 1:
        data = s.recv(1024)
        if data == "":
            # sendMe = "IAM:"+token+":"+"gg@aol.com"+":at\n"
            # sendMe = urllib.quote(sendMe.encode('utf-8'))
            # print (sendMe)
            # s.sendall(sendMe)
            break
        token = data
        # print "Received:", data

    # print(token)
    print "Connection closed."


    s.close()
    return token


@application.route('/')
def home():
    # print (str(netcat("challenge2.airtime.com",2323,"")).encode('utf-8','strict'))
    str = "this is string example..@@@..wow!!!";
    str = str.encode('utf8','strict');

    print "Encoded String: " + str;
    print "Decoded String: " + str.decode('utf-8','strict')
    return "home"

@application.route('/token')
def return_token():
    return netcat("challenge2.airtime.com",2323,"")


@application.route('/login')
def identify():
    print(request.args['email'])
    email = request.args['email']
    token = request.args['token']
    print("after login gives me -- " +netcat("challenge2.airtime.com",2323,"IAM:"+token+":"+email+":at\n"))
    return "zzz"


if __name__ == '__main__':
    application.run(host='0.0.0.0')

