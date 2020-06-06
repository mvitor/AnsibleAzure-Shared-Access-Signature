import requests
import datetime
import hmac
import hashlib
import base64
import sys
# Azure Rest Api Version
api_version = '2015-02-21'
request_time = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
storage_account_key = 'TNn8GaTfTUcr20n16BPHvxfo5wLyaxzFXh+kxezc7w+GE5ZtmhhE5nlLGNfK1/Vd/Evnw8iErx/VTEh0It7KPQ=='
storage_account_name = sys.argv[1]
container_name = sys.argv[2]
blob_name = sys.argv[3]
content_length = sys.argv[4]
string_params = {
    'verb': 'PUT',
    'Content-Encoding': '',
    'Content-Language': '',
    'Content-Length': content_length,
    'Content-MD5': '',
    'Content-Type': 'text/plain; charset=UTF-8',
    'Date': '',
    'If-Modified-Since': '',
    'If-Match': '',
    'If-None-Match': '',
    'If-Unmodified-Since': '',
    'Range': '',
    'CanonicalizedHeaders': 'x-ms-blob-type:BlockBlob' + '\nx-ms-date:' + request_time + '\nx-ms-version:' + api_version + '\n',
    'CanonicalizedResource': '/' + storage_account_name +'/'+container_name+ '/' + blob_name
}

string_to_sign = (string_params['verb'] + '\n' 
                  + string_params['Content-Encoding'] + '\n'
                  + string_params['Content-Language'] + '\n'
                  + string_params['Content-Length'] + '\n'
                  + string_params['Content-MD5'] + '\n' 
                  + string_params['Content-Type'] + '\n' 
                  + string_params['Date'] + '\n' 
                  + string_params['If-Modified-Since'] + '\n'
                  + string_params['If-Match'] + '\n'
                  + string_params['If-None-Match'] + '\n'
                  + string_params['If-Unmodified-Since'] + '\n'
                  + string_params['Range'] + '\n'
                  + string_params['CanonicalizedHeaders']
                  + string_params['CanonicalizedResource'])

signed_string = base64.b64encode(hmac.new(base64.b64decode(storage_account_key), msg=string_to_sign.encode('utf-8'), digestmod=hashlib.sha256).digest()).decode()

print (signed_string+";"+request_time)
