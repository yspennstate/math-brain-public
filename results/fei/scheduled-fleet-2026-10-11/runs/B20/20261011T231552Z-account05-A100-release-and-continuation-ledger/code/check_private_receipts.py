from pathlib import Path
import json, hashlib
ROOT=Path(r'~\mop_fei100\reports\fei-2026-10-11')
RUN=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'verification'/'B19_ORIGINAL_SOURCE_READBACKS.json').read_text(encoding='utf-8-sig'))
out=[]
for r in rows:
    b=r['content'].encode(r['encoding'])
    # Recompute the stored Git blob identity as a hash; no git invocation.
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert blob==r['sha'],r['file']
    local=None
    if r['file']!='Brain_REPORT.md':
        p=ROOT/'runs'/'B19'/'20261011T195038Z-account01-B19-independent-review'/r['file']
        local=p.read_bytes().replace(b'\r\n',b'\n')==b
        assert local,r['file']
    out.append({'file':r['file'],'stored_private_url':r['display_url'],'stored_blob_sha':r['sha'],'embedded_bytes_blob_verified':True,'local_copy_matches_after_CRLF_normalization':local,'current_remote_readback':False})
result={'historical_saved_private_payloads_verified':len(out),'local_source_copies_verified':3,'records':out,'meaning':'Integrity of historical canonical and Brain payloads, not current remote availability or new-run persistence.'}
(RUN/'out'/'PRIVATE_RECEIPT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
report=RUN/'REPORT.md'
s=report.read_text(encoding='utf-8')
needle='This run has no verified supervisor copy, private mirror or native Brain graph ingestion, and no public release.'
replacement='check_private_receipts.py also independently rehashed four historical B19 private payloads (canonical report, claims, checker and Brain report) against their stored blob identities, and matched the three canonical local copies after explicit CRLF normalization. out/PRIVATE_RECEIPT_CHECK.json records this durable historical-payload check; current remote availability remains unverified. '+needle
assert needle in s
report.write_text(s.replace(needle,replacement),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
