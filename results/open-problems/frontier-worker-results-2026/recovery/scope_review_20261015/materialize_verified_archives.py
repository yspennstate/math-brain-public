"""Make the already verified private audit archives readable on the local brain paths."""
from pathlib import Path
from datetime import datetime
import subprocess,json,hashlib,io,zipfile
HERE=Path(__file__).resolve().parent
REPO=Path('~/brain-repo')
PY='C:/Python314/python.exe';AGENT='codex-term-362ebe34'
MESH=REPO/'12_cognitive_architecture/agent_mesh/agent_mesh.py'
prefix='06_math_research/frontier/worker_results/recovery_362ebe34/'
owned=(REPO/prefix).resolve()
def sha(b):return hashlib.sha256(b).hexdigest()
def run(args):return subprocess.run(args,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
def git(*a):return run(['git','-C',str(REPO),*a])
def mesh(*a):return run([PY,str(MESH),*a,'--agent',AGENT])
t67=json.loads((HERE/'T067_ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
t186=json.loads((HERE/'T186_ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
extra=json.loads((HERE/'FRONTIER_EXTRA_BACKUP_RECEIPT.json').read_text(encoding='utf-8'))
assert t67['pushed'] and t186['pushed'] and extra['pushed']
snapshot=t186['commit'];git('merge-base','--is-ancestor',t67['commit'],snapshot)
expected={p:h for d in [t67,t186] for p,h in d['files'].items() if p.startswith(prefix)}
old=[p for p in extra['paths'] if p.startswith(prefix)]
git('diff','--quiet',extra['commit'],snapshot,'--',*old)
allowed=set(expected)|set(old)
archive=git('archive','--format=zip',snapshot,'--',prefix)
payloads={}
with zipfile.ZipFile(io.BytesIO(archive)) as z:
    for entry in z.infolist():
        if entry.is_dir():continue
        assert entry.filename in allowed,entry.filename
        payload=z.read(entry);path=(REPO/entry.filename).resolve()
        assert path.is_relative_to(owned)
        if entry.filename in expected:assert sha(payload)==expected[entry.filename]
        if path.exists():assert path.is_file() and path.read_bytes()==payload, 'Existing local archive differs: '+str(path)
        payloads[path]=payload
assert len(payloads)==len(allowed)==115
mesh('claim','--resource',str(owned),'--mode','write','--ttl','1800',
     '--purpose','Materialize115 already verified immutable audit artifacts, no rerun or overwrite')
mesh('assert','--resource',str(owned))
written=skipped=0
for path,payload in payloads.items():
    if path.exists():skipped+=1;continue
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:f.write(payload)
    assert path.read_bytes()==payload
    written+=1
scope_root=owned/'t067_review_20261015'
extra_scope=['T067_DEPENDENCY_SCOPE_ADDENDUM.md','audit_t067_rescale_scope.py',
             'T067_RESCALE_SCOPE_RECEIPT.json','run_polite.py']
scope_receipt=json.loads((HERE/'T067_RESCALE_SCOPE_RECEIPT.json').read_text(encoding='utf-8'))
assert scope_receipt['status'].startswith('PASS')
scope_payloads={name:(HERE/name).read_bytes() for name in extra_scope}
scope={'at':scope_receipt['at'],
    'main_subject':'T067-PIECEWISE-D0-001 v1',
    'main_proof_sha256':'9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226',
    'preserved_original_archive':t67['commit'],
    'source_scope':'RESCALE v1 full file FIX: unrestricted extra F1 corollary invalid. Only valid identity R is used in main D4. Main D3 uses F2 with eta<=16013/200000<2887/5000. No frontier promotion by this metadata.',
    'scope_files':{name:sha(b) for name,b in scope_payloads.items()}}
scope_payloads['SUBLEMMA_SCOPE.json']=(json.dumps(scope,indent=2)+'\n').encode('utf-8')
mesh('assert','--resource',str(owned))
for name,payload in scope_payloads.items():
    target=scope_root/name
    if target.exists():
        assert target.read_bytes()==payload,'Scope destination differs; version it explicitly'
    else:
        with target.open('xb') as f:f.write(payload)
        assert target.read_bytes()==payload
out={'at':datetime.now().astimezone().isoformat(),'snapshot':snapshot,
    'files':len(payloads),'written':written,'already_matching':skipped,
    'scope_files_staged_for_next_backup':list(scope_payloads),
    'status':'PASS exact verified Git objects copied locally; scope addendum staged beside original review; no existing bytes replaced'}
(HERE/'MATERIALIZE_ARCHIVE_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps(out))
