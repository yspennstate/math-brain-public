"""Download primary papers as text only; PDF bytes remain in memory."""
import hashlib, json, pathlib, subprocess, urllib.request, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]

def fetch(name, url):
    req = urllib.request.Request(url, headers={'User-Agent':'C0034 mathematics literature audit'})
    blob = urllib.request.urlopen(req, timeout=60).read()
    if blob.startswith(b'%PDF'):
        text = subprocess.run(['pdftotext','-layout','-','-'],input=blob,stdout=subprocess.PIPE,check=True).stdout.decode()
    else:
        from html.parser import HTMLParser
        class TextParser(HTMLParser):
            def __init__(self):
                super().__init__(); self.parts=[]
            def handle_data(self, data):
                if data.strip(): self.parts.append(data.strip())
        parser=TextParser(); parser.feed(blob.decode())
        text = '\n'.join(parser.parts)
    path = ROOT/'sources'/f'{name}.txt'
    path.write_text(text)
    meta = {'url':url,'download_sha256':hashlib.sha256(blob).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'characters':len(text)}
    (ROOT/'sources'/f'{name}.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(name, len(text), url, flush=True)

if __name__ == '__main__':
    fetch(sys.argv[1],sys.argv[2])
