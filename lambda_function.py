from __future__ import print_function

import json
import os
from elasticsearch import Elasticsearch
import certifi

es_host=os.environ['ELASTICSEARCH_HOST']
es_port=os.environ['ELASTICSEARCH_PORT']
es_user=os.environ['ELASTICSEARCH_USER']
es_password=os.environ['ELASTICSEARCH_PASSWORD']
es_index=os.environ['ELASTICSEARCH_INDEX']

print(certifi.where())

es = Elasticsearch(
    [es_host],
    http_auth=(es_user, es_password),
    scheme="https",
    ca_certs=certifi.where(),
    port=es_port,
)

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = json.dumps(event['Records'][0]['Sns'])
    print("From SNS: " + message)
    res = es.index(index=es_index, doc_type='doc', body=message)
    return res