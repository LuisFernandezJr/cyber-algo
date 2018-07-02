#source, layers, ip....

from pprint import pprint
import json

#json_data=open("C://Users//lffernan//Desktop//json//test.json")

import json
from pprint import pprint
import csv

packets = []
records = []

with open('all.json') as f:
    for line in f:
        packets.append(json.loads(line))

#data ["_id"]

headers = set()

for packet in packets:
    record = {}
    
    for field in ["_index", "_type", "_id", "_score", "timestamp", "@version", "protocol"]:
        headers.add(field)
        if field in packet:
            record.update({field: packet[field]})
    
    headers.add("@timestamp")
    record.update({"@timestamp": packet["_source"]["@timestamp"]})
    
    layers = packet["_source"]["layers"]
    for layer in layers:
        x = layers[layer]
        if type(x) is dict:
            headers.update(x.keys())
            record.update(x)
        else:
            headers.add(layer)
            record.update({layer: x})
    records.append(record)
    

with open('mycsvfile.csv', 'w', newline='') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, headers)
    w.writeheader()
    w.writerows(records)
