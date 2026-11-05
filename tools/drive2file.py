import sys, json, base64
d=json.load(open(sys.argv[1])); open(sys.argv[2],'wb').write(base64.b64decode(d['content'])); print(d.get('title'), d.get('mimeType'))
