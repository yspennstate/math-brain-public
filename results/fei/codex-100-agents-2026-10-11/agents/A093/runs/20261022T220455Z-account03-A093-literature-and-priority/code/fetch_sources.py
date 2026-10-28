from pathlib import Path
import urllib.request, hashlib, json, datetime
R=Path(__file__).resolve().parents[1]
rows=[]
for name,url in [('www14v1','https://arxiv.org/pdf/1312.3003v1'),('shalev19v2','https://arxiv.org/pdf/1806.03646v2')]:
    row=dict(name=name,url=url,at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        with urllib.request.urlopen(url,timeout=20) as response:
            data=response.read(3000000)
        assert data.startswith(b'%PDF') and len(data)<3000000
        (R/'out'/f'{name}.pdf').write_bytes(data)
        row.update(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),status='FETCHED_PRIMARY_PDF')
    except Exception as e:
        row.update(status='LOCAL_FETCH_BLOCKED_PRIMARY_WEB_READ_SUCCEEDED',error=str(e))
    rows.append(row)
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows))
