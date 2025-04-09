from flask import Flask, Response, send_from_directory
import boto3
import os
app = Flask(__name__)
s3 = boto3.client('s3')
# Replace with your bucket + keys
BUCKET = 'capstone-outputs-bucket'
INDEX_KEY = 'output/index.html'
NEWSFEED_KEY = 'output/newsfeed-2.html'
@app.route('/')
def serve_index():
    obj = s3.get_object(Bucket=BUCKET, Key=INDEX_KEY)
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')
@app.route('/newsfeed-2')
def serve_newsfeed():
    obj = s3.get_object(Bucket=BUCKET, Key=NEWSFEED_KEY)
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
