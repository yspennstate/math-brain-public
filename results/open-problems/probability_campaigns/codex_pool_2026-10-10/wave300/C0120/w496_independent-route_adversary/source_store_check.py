import hashlib
import json
import sqlite3
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parent
status_path = root / 'SOURCE_STATUS.json'
status = json.loads(status_path.read_text(encoding='utf-8'))
try:
    with urllib.request.urlopen('https://arxiv.org/pdf/0810.4221v2', timeout=25) as r:
        data = r.read(2_000_001)
    assert data.startswith(b'%PDF') and len(data)<=2_000_000
    sha = hashlib.sha256(data).hexdigest()
    status['primary_source']['independent_download_sha256'] = sha
    status['primary_source']['independent_download_bytes'] = len(data)
    status['primary_source']['hash_status'] = 'Independently recomputed from public versioned PDF; this is provenance, not proof.'
    status['primary_source']['matches_recorded_intake_hash'] = sha == status['primary_source']['local_intake_recorded_sha256']
    print('primary_pdf_sha256', sha, 'bytes', len(data))
except Exception as e:
    status['primary_source']['independent_download_status'] = type(e).__name__ + ': ' + str(e)[:300]
    print('primary_download_not_verified', type(e).__name__)

target = Path('~/math-brain-build/local/population/brain.sqlite3')
try:
    conn = sqlite3.connect(target.as_uri()+'?mode=ro',uri=True,timeout=5)
    conn.execute('PRAGMA query_only=ON')
    hits = conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE '%C0120%' OR body LIKE '%C0120%' OR (title LIKE '%polymer%' AND (body LIKE '%n/log%' OR body LIKE '%fluctuation%')) LIMIT 20").fetchall()
    report=[]
    for node_id,kind,title,body,meta in hits:
        report.append({'id':node_id,'kind':kind,'title':title,'body':body[:2500],'metadata':meta[:1500]})
    conn.close()
    (root/'STORE_SCOPE_REPORT.json').write_text(json.dumps({'store':str(target),'read_only':True,'query_scope':'C0120 or polymer variance/fluctuation','hit_count_capped_at_20':len(report),'nodes':report},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    status['population_store_scope_check'] = {'read_only':True,'report':'STORE_SCOPE_REPORT.json','hit_count_capped_at_20':len(report),'exports':'Targeted export search for C0120/source id found no match.'}
    print('scoped_store_hits', len(report))
except Exception as e:
    status['population_store_scope_check'] = {'status':'not_verified','error':type(e).__name__+': '+str(e)[:250]}

status['recent_primary_literature'] = [
    {'url':'https://arxiv.org/abs/2604.01214','date':'2026-04-01','scope':'Power variance bound for rotationally invariant planar Riemannian FPP, a different model; no automatic transfer to iid Gaussian lattice last-passage maxima.'},
    {'url':'https://arxiv.org/abs/2603.06574','date':'2026-03-06','scope':'Continuous spatially correlated Gaussian polymers, with a high-temperature higher-dimensional result; different assumptions from the source-model maximum.'},
    {'url':'https://arxiv.org/abs/2509.16694','date':'2025-09-20','scope':'Intermediate-temperature correlated 1+2 polymer CLT; does not certify the source-model power variance bound.'},
]
status['current_openness']='UNKNOWN'
status['paired_proof_access']='Independent derivation saved first; subsequently read w495 precommit, S1/L0, and its originator ATTEMPT.md L1-L5.'
status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
