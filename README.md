# ngrok-remote-controlled-docker
control ngrok via Python Flask Rest API

# usage
- deploy via docker-compose
- a webserver is opened on <ip-of-your-server>:5000
- api endpoints: ngrok_start, ngrok_start/<string:host>, ngrok_stop
    - ngrok_start: a tunnel is created for a given host in the file ngrok_control.py
    - ngrok_start/<string:host>: a tunnel is created for the url provided in the API call. e.g. http://myserver:5000/ngrok_start/192.168.10.121:8080 will open a http-tunnel to the given host
    - ngrok_stop: kills all ngrok processes