from pathlib import Path
import sqlite3
import subprocess
import json
import hashlib
import time
import importlib.util

root=Path(__file__).resolve().parent
receipt={}
research=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
records=[]
for name in ('problems.jsonl','attempts.jsonl'):
    result=subprocess.run(['rg','-n','C0044',str(research/name)],capture_output=True,text=True,encoding='utf-8')
    for line in result.stdout.splitlines():
        number,_,body=line.partition(':')
        row=json.loads(body)
        if row.get('problem_id')=='C0044': records.append({'path':str(research/name),'line':int(number),'record':row})
receipt['exact_intake_records']=records
(root/'EXACT_INTAKE.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')

store=Path('~/math-brain-build/local/population/brain.sqlite3')
if store.exists():
    started=time.monotonic()
    try:
        db=sqlite3.connect('file:'+store.as_posix()+'?mode=ro',uri=True,timeout=2)
        db.set_progress_handler(lambda: 1 if time.monotonic()-started>3 else 0,10000)
        tables=[r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('cards','nodes','sources')")]
        receipt['store']={'path':str(store),'mode':'ro','tables':tables,'cards':[]}
        for table in ('cards','nodes'):
            if table not in tables: continue
            columns=[r[1] for r in db.execute('PRAGMA table_info('+table+')')]
            receipt['store'][table+'_columns']=columns
            textcols=[c for c in ('title','logical_name','statement','text','content') if c in columns]
            if not textcols: continue
            predicates=[]
            args=[]
            for c in textcols:
                predicates.append('('+c+' LIKE ? AND ('+c+' LIKE ? OR '+c+' LIKE ?))')
                args.extend(('%directional%','%zero%','%0-1%'))
            selected=[c for c in ('id','card_id','namespace','logical_name','kind','title','statement','source_id','text','content') if c in columns]
            for row in db.execute('SELECT '+','.join(selected)+' FROM '+table+' WHERE '+' OR '.join(predicates)+' LIMIT 6',args):
                entry={k:(v[:1800] if isinstance(v,str) else v) for k,v in zip(selected,row)}
                receipt['store']['cards'].append(entry)
        db.close()
    except (sqlite3.Error,OSError) as exc:
        receipt['store_error']=str(exc)
else: receipt['store']={'path':str(store),'state':'exact named path absent'}

canonical=Path('~/math-research-brain')
receipt['canonical_named_root']={'path':str(canonical),'exists':canonical.exists(),'note':'No canonical-store path guessed or promoted.'}
export=Path('~/math-brain-build/export/population')
receipt['export_metadata']={'path':str(export),'matching_filenames':[p.name for p in export.glob('*direction*')]+[p.name for p in export.glob('*C0044*')], 'whole_export_read':False}

peer_sources=Path('~/brain_workers/w576/sources')
receipt['peer_primary_source_files']=[]
if peer_sources.exists():
    for p in peer_sources.iterdir():
        if not p.is_file(): continue
        item={'path':str(p),'bytes':p.stat().st_size}
        if p.suffix.lower()=='.pdf' and importlib.util.find_spec('fitz'):
            import fitz
            doc=fitz.open(p)
            item['pages']=len(doc)
            lowername=p.name.lower()
            if 'sabot' in lowername or '1007' in lowername:
                for page in range(min(5,len(doc))):
                    text=doc[page].get_text()
                    location=text.find('Theorem 1')
                    if location>=0:
                        item.setdefault('scoped_excerpts',[]).append({'page_index':page,'excerpt':text[max(0,location-600):location+2300]})
            elif 'direction' in lowername or 'zero' in lowername:
                item['first_page_excerpt']=doc[0].get_text()[:1800]
            doc.close()
        receipt['peer_primary_source_files'].append(item)

mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
result=subprocess.run(['python','-X','utf8',mesh,'--help'],capture_output=True,text=True,encoding='utf-8')
receipt['mesh_help']=result.stdout[:4500]

comm=[]
for recipient,body in [
 ('w576','C0044 scoped adversary audit: your L1-L6 are conditional and retain G1. My independent phase SHA256 8fb44a681ca30c5344ab57edf1f1b884d3756fb03e39ce8d64a43c893ccd39e7; exact iid P-invariance defect 1/12 in MEASUREMENT.json. New ATTEMPT.md V gives a concrete uniform-elliptic abstract chain: original energy 10/153, incoming Cesaro energy <=57/(340N). This refutes the generic L5-to-G1 inference, not iid C0044. ATTEMPT.md VI: pointwise incoming balance collapses iid rows to deterministic rows. Served identity UNVERIFIED; final referee w578 pending. Please route this narrow counterexample boundary to the other harmonic-energy triad; I am not duplicating your UI computations.'),
 ('w578','Additional w577 independent-check request: ~/brain_workers/w577/ATTEMPT.md V-VII; STARVATION_MEASUREMENT.json, check_starvation.py, CLAIMS.jsonl. Abstract uniformly elliptic chain has original energy 10/153 but Cesaro energy <=57/(340N); explicitly not iid spatial law. Incoming balance plus iid rows forces determinism. Historical C0044-A001 finite-region explanation does not invalidate the quenched martingale. Please return scoped mathematical verdict and actual served-model evidence if available; promotion gates remain pending.')
]:
    result=subprocess.run(['python','-X','utf8',mesh,'send','--agent','w577','--to',recipient,'--topic','probability300-C0044','--kind','message','--body',body],capture_output=True,text=True,encoding='utf-8')
    comm.append({'to':recipient,'returncode':result.returncode,'stdout':result.stdout[:4500],'stderr':result.stderr[:1500]})
    (root/'SECOND_COMM_RECEIPTS.json').write_text(json.dumps(comm,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(comm[-1]))

(root/'SCOPED_SOURCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='exact_intake_records'},indent=2,ensure_ascii=False))
