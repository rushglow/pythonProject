import json

from flask import Flask, jsonify, request

import nmap3

app = Flask(__name__)




@app.route('/scan', methods=['POST'])
def process_json():
    nmap = nmap3.Nmap()
    post_rqst = request.json
    address = json.loads(post_rqst)["address"]
    result = nmap.nmap_version_detection("http://scanme.nmap.org/", args="--script vulners --script-args mincvss=6.5")
    print(address)



if __name__ == '__main__':
    app.run(debug=True)
