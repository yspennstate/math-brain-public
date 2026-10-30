import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
receipt=read(R/'out/PERSISTENCE_RECEIPTS.json')
for row in receipt['files']:
 p=R/row['path'];b=p.read_bytes()
 assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'],p
for p in R.rglob('*.json'):read(p)
for c in read(R/'CLAIMS.json')['claims']:
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
one=read(R/'out/ONE_BIASED_CERTIFICATE.json')
assert one['rows'][0]['k']==1 and one['rows'][0]['Lambda_sign']=='negative'
assert all(x['Lambda_sign']=='positive' for x in one['rows'][1:])
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert report.rsplit('## Universal bridge',1)[1].strip().startswith('This stage moves C024')
assert 'Full FEI remains OPEN' in report
home=R.parents[1]
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for name in ('LEARNED.md','WORKLOG.md'):
 p=home/name;b=p.read_bytes();note='\nStage17 boundary audit: the one-balanced-child k1 net Lambda is NEGATIVE; the first blanket sign assertion failed and is preserved in out/ONE_BIASED_FAILURE.json. The positive-limit theorem and k>=2 payment do not rely on a k1 sign. Paper TXT files use Windows-1252 source bytes; decode explicitly, never blame the source for a failed UTF-8 read.\n'
 if b'Stage17 boundary audit:' not in b:p.write_bytes(b+note.encode('utf-8'))
out={'status':'PASS','checks':'all saved manifest hashes and byte counts; JSON parse; exact statement digests; delta identity; negative boundary disposition; two-line status; final Universal bridge paragraph','full_fei':'OPEN'}
(R/'out/FINAL_VERIFY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
