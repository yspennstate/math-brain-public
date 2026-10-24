from pathlib import Path
import json
j=json.loads(Path('crossref_dubedat.json').read_text())
for w in j['message']['items']:print(w.get('title'),w.get('author'),w.get('DOI'),w.get('published'),w.get('container-title'),w.get('volume'),w.get('page'))
