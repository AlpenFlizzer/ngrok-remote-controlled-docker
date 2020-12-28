import flask
import subprocess
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/ngrok_start', methods=['GET'])
def ngrok_start():
    proc = subprocess.Popen(["ngrok", "http", "http://127.0.0.1:80"],stdin=None, stdout=None, stderr=None)
    time.sleep(1)
    proc = subprocess.Popen(["curl", "http://localhost:4040/api/tunnels"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out

@app.route('/ngrok_start/<string:url>', methods=['GET'])
def ngrok_start_url(url):
    proc = subprocess.Popen(["ngrok", "http", "http://"+url],stdin=None, stdout=None, stderr=None)
    time.sleep(1)
    proc = subprocess.Popen(["curl", "http://localhost:4040/api/tunnels"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out

@app.route('/ngrok_stop', methods=['GET'])
def ngrok_stop():
    proc = subprocess.Popen(["pkill", "ngrok"], stdout=subprocess.PIPE)
    time.sleep(1)
    proc = subprocess.Popen(["pgrep", "ngrok"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run(host="0.0.0.0", port=5000)