import requests
import json
import sys
import os
from utils import md5

class Faces:
    BASE_URL = 'https://api.projectoxford.ai/face/v0/detections?'
    AZURE_KEY = "YOUR_KEY_HERE"
    data = None
    cache = {}

    def __init__(self, features = None):
        if not features:
            features = ["analyzesFaceLandmarks"]
        self.features = features

    def _get_faces(self, headers, data):
        url = self.BASE_URL
        for feature in self.features:
            url += feature + "=true&"
        url += "subscription-key=" + self.AZURE_KEY

        response = requests.post(url, data=data, headers=headers)
        if response.status_code != 200:
            raise BadResponseException(json.loads(response.content)['message'])
        return json.loads(response.text)

    def from_url(self, url):
        if md5(url) in self.cache:
            self.data = self.cache[md5(url)]
            return

        data = json.dumps({'url': url})
        headers = {'Content-Type': 'application/json'}
        self.data = self._get_faces(headers, data)
        self.cache[md5(url)] = self.data

    def from_file(self, path):
        if os.path.getsize(path) > 2*1024*1024:
            raise FileTooBigException('File must be under 2MB')

        if md5(path) in self.cache:
            self.data = self.cache[md5(path)]
            return

        data = open(path, 'rb').read()
        headers = {'Content-Type': 'application/octet-stream'}
        self.data = self._get_faces(headers, data)
        self.cache[md5(path)] = self.data

class BadResponseException(Exception):
    def __init__ (self, value):
        self.value = value

    def __str__(self):
        return self.value

class FileTooBigException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
