from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import sqlite3
import time

ROOT=Path(__file__).resolve().parent
BASE=Path('~')
snapshot_dir=ROOT/'audit_snapshots'
snapshot_dir.mkdir(exist_ok=True)
source=BASE/'brain_workers/w543/ATTEMPT.md'
data=source.read_bytes()
destination=snapshot_dir/'w543_ATTEMPT.md'
destination.write_bytes(data)
(ROOT/'AUDIT_SNAPSHOT.json').write_text(json.dumps({'source_path':str(source),'snapshot_path':str(destination),'sha256':hashlib.sha256(data).hexdigest(),'read_utc':datetime.now(timezone.utc).isoformat(),'mathematical_audit':'AUDIT.md','hash_is_not_a_proof':True},indent=2)+'\n',encoding='utf-8')

store=BASE/'math-brain-build/local/population/brain.sqlite3'
connection=sqlite3.connect(f'file:{store.as_posix()}?mode=ro',uri=True,timeout=5)
deadline=time.monotonic()+8
connection.set_progress_handler(lambda: int(time.monotonic()>deadline),10000)
rows=connection.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(title) LIKE '%hexatic%' LIMIT 10").fetchall()
records=[]
for node_id,kind,title,body,meta in rows:
    metadata=json.loads(meta)
    records.append({'id':node_id,'kind':kind,'title':title,'statement':body,'logical_id':metadata.get('logical_id'),'source_id':metadata.get('source_id'),'metadata_status':{k:v for k,v in metadata.items() if k in {'status','result_status','source_status','source_revision'}}})
connection.close()
(ROOT/'BRAIN_TARGET_RECEIPT.json').write_text(json.dumps({'store':str(store),'open_mode':'mode=ro','query':"SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(title) LIKE '%hexatic%' LIMIT 10",'records':records,'scope':'Target-only query; not a complete solved/retired-work audit.'},indent=2)+'\n',encoding='utf-8')
print('Target-only store records:',len(records))
for record in records:
    print(json.dumps(record,ensure_ascii=False))

gate={'created_utc':datetime.now(timezone.utc).isoformat(),'purpose':'Evaluate exact one-point negative-density tails and verify the angular coefficient used in the peer audit.','max_wall_seconds':15,'max_quadrature_points':1024,'hardware':'CPU only; no simulation, training, GPU or network.'}
(ROOT/'DENSITY_COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
start=time.monotonic()
density_rows=[]
for beta in [0.1,1.0,4.0]:
    rho,a,cutoff,s=1.0,1.3,1.0,1.0
    variance=rho*rho*cutoff**(4-s)/(2*math.pi*beta*a*(4-s))
    probability=0.5*math.erfc(rho/math.sqrt(2*variance))
    assert 0<probability<0.5
    density_rows.append({'beta':beta,'variance':variance,'negative_probability':probability})
max_error=0.0
count=0
for x0,x1 in [(1,0),(0,2),(1,3)]:
    for g0,g1 in [(1,0),(0,1),(2,-1)]:
        count+=1
        value=0.0
        N=1024
        for j in range(N):
            theta=2*math.pi*(j+0.5)/N
            c,sn=math.cos(theta),math.sin(theta)
            value+=(c*x0+sn*x1)**2*(-sn*g0+c*g1)**2*2*math.pi/N
        expected=math.pi/4*((g0*g0+g1*g1)*(x0*x0+x1*x1)+2*(g0*x1-g1*x0)**2)
        max_error=max(max_error,abs(value-expected))
assert max_error<1e-11
assert time.monotonic()-start<gate['max_wall_seconds']
(ROOT/'DENSITY_MEASUREMENTS.json').write_text(json.dumps({'command':'python -X utf8 ~/brain_workers/w544/collect_receipts.py','negative_density_tails':density_rows,'peer_H4_angular_cases':count,'max_absolute_angular_error':max_error,'elapsed_seconds':time.monotonic()-start,'all_assertions_passed':True,'scope':'Numbers check auxiliary formulas only. Almost-sure exceedance conclusion has a separate mathematical proof; no microscopic Gibbs transfer was tested.'},indent=2)+'\n',encoding='utf-8')
print('Density tails:',json.dumps(density_rows))
print('H4 angular cases:',count,'maximum error:',max_error)
