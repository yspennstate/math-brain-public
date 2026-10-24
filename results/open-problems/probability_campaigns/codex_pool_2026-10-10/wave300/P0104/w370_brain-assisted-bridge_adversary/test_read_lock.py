"""Small local compatibility, integrity, and lock-fencing checks; no live writes."""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
from unittest.mock import patch
import uuid

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
import psutil
gate = {'cpu_percent':psutil.cpu_percent(interval=0.2), 'available_ram_bytes':psutil.virtual_memory().available,
        'maximum_cpu_percent':75,'minimum_available_ram_bytes':2*1024**3,
        'budget_seconds':20,'scope':'stdlib tests on tiny synthetic files; no model, GPU or store load'}
gate['admitted'] = gate['cpu_percent']<=75 and gate['available_ram_bytes']>=2*1024**3
if (ROOT/'fresh_compute_gate.json').exists():
    prior_gate=json.loads((ROOT/'fresh_compute_gate.json').read_text(encoding='utf-8'))
    with (ROOT/'compute_gate_history.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps(prior_gate)+'\n')
(ROOT/'fresh_compute_gate.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')
if not gate['admitted']:
    print(json.dumps({'gate':gate,'status':'not_run'}))
    raise SystemExit(2)
started=time.perf_counter()

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

baseline=load('w370_doc_baseline',ROOT/'copies/brain_node_documents.py')
candidate=load('w370_doc_candidate',ROOT/'prototype/brain_node_documents.py')
base=ROOT/'fixtures'/uuid.uuid4().hex
base.mkdir(parents=True)

def fixture(name, lock=b'0'):
    mem=base/name
    mem.mkdir()
    slug='fpp_bridge'
    (mem/(slug+'.md')).write_text('# Synthetic parent\n',encoding='utf-8')
    docs=candidate.bundle_dir(mem,slug)/'documents'
    docs.mkdir(parents=True)
    raw=b'Independent FPP bridge: weak scaling needs uniform integrability.\n'
    (docs/'bridge.md').write_bytes(raw)
    manifest=candidate._empty_manifest(slug)
    manifest['documents']=[{'name':'bridge.md','path':'documents/bridge.md','sha256':hashlib.sha256(raw).hexdigest(),
                           'bytes':len(raw),'description':'synthetic fixture','required':True,'auto_read':True,'wake':False}]
    candidate.manifest_path(mem,slug).write_text(json.dumps(manifest),encoding='utf-8')
    if lock is not None:
        (mem/candidate.WRITE_LOCK_NAME).write_bytes(lock)
    return mem,slug,raw

results=[]
def check(name,fun):
    assert time.perf_counter()-started<gate['budget_seconds'], 'fresh compute budget expired'
    t=time.perf_counter()
    try:
        detail=fun()
        results.append({'name':name,'passed':True,'seconds':round(time.perf_counter()-t,6),'detail':detail})
    except Exception as exc:
        results.append({'name':name,'passed':False,'seconds':round(time.perf_counter()-t,6),'error':type(exc).__name__+': '+str(exc)})

def expect_error(fn,fragment):
    try:
        fn()
    except candidate.AttachmentError as exc:
        assert fragment in str(exc), str(exc)
        return str(exc)
    raise AssertionError('expected AttachmentError: '+fragment)

mem,slug,raw=fixture('valid')
real_open=os.open
def guarded_trial(module):
    attempts=[]
    def read_only_open(path,flags,*args,**kw):
        if flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND):
            attempts.append(str(path))
            raise PermissionError('synthetic read-only permissions')
        return real_open(path,flags,*args,**kw)
    t=time.perf_counter()
    with patch.object(os,'open',read_only_open):
        try:
            docs=module.load_documents(mem,slug)
            assert len(docs)==1 and docs[0].text.encode()==raw
            result={'success':True}
        except module.AttachmentError as exc:
            result={'success':False,'error':str(exc)}
    result.update(write_open_attempts=len(attempts),seconds=round(time.perf_counter()-t,6))
    return result

before=guarded_trial(baseline)
after=guarded_trial(candidate)
def comparison():
    assert not before['success'] and before['write_open_attempts']==1
    assert after['success'] and after['write_open_attempts']==0
    return {'before':before,'after':after}
check('same_verified_bundle_under_read_only_permissions',comparison)

def writer_blocks_reader():
    with candidate._attachment_write_lock(mem,timeout_seconds=.04):
        def read():
            with candidate._attachment_read_lock(mem,timeout_seconds=.04):
                pass
        return expect_error(read,'timed out')
check('active_writer_fences_reader',writer_blocks_reader)

def reader_blocks_writer():
    with candidate._attachment_read_lock(mem,timeout_seconds=.04):
        def write():
            with candidate._attachment_write_lock(mem,timeout_seconds=.04):
                pass
        return expect_error(write,'timed out')
check('active_reader_fences_writer',reader_blocks_writer)
check('handles_unlock_after_context',lambda: {'documents':len(candidate.load_documents(mem,slug))})

def bad_digest():
    bad,bslug,_=fixture('bad_digest')
    (candidate.bundle_dir(bad,bslug)/'documents/bridge.md').write_bytes(b'x'*len(raw))
    return expect_error(lambda:candidate.load_documents(bad,bslug),'SHA-256 mismatch')
check('corrupted_attachment_still_rejected',bad_digest)

def orphan():
    bad,bslug,_=fixture('orphan')
    (candidate.bundle_dir(bad,bslug)/'documents/orphan.md').write_text('orphan',encoding='utf-8')
    return expect_error(lambda:candidate.load_documents(bad,bslug),'inventory mismatch')
check('unmanifested_document_still_rejected',orphan)

def absent_lock():
    bad,bslug,_=fixture('no_lock',None)
    text=expect_error(lambda:candidate.load_documents(bad,bslug),'missing or unreadable')
    assert not (bad/candidate.WRITE_LOCK_NAME).exists()
    return text
check('missing_sidecar_fails_closed_without_creating_it',absent_lock)

def empty_lock():
    bad,bslug,_=fixture('empty_lock',b'')
    return expect_error(lambda:candidate.load_documents(bad,bslug),'nonempty')
check('empty_sidecar_fails_closed',empty_lock)

numeric=[]
for exponent in [6,12,24,48,96,192]:
    n=10.0**exponent
    ln=math.log(n)
    prob=n**(-.25)
    relative_rare=math.exp(ln/12)/ln
    var=n**(2/3)*(1+relative_rare)
    kurt=(1+6*relative_rare+relative_rare**2/prob)/(1+relative_rare)**2
    numeric.append({'n_power_of_10':exponent,'chi_finite':math.log(var)/(2*ln),'kurtosis':kurt,
                    'variance_over_n_two_thirds':1+relative_rare,'weak_law_discrepancy_upper':prob})
receipt={'gate':gate,'before':before,'after':after,'tests':results,
         'passed':sum(r['passed'] for r in results),'total':len(results),
         'elapsed_seconds':round(time.perf_counter()-started,6),
         'counterexample_numeric_sanity_checks':numeric,
         'limitations':['fixture, not full recall benchmark','same-process lock checks on this Windows host',
                        'numeric table is not the proof; asymptotic derivation is INDEPENDENT_BRIDGE.md',
                        'no live patch or store ingestion performed']}
(ROOT/'repair_measurements.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
raise SystemExit(0 if all(r['passed'] for r in results) else 1)
