from pathlib import Path
import json, hashlib, re
from datetime import datetime, timezone
ROOT=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
def write(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
paths=[ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',ROOT/'claude/B20/SYNTHESIS.md']
paths += [CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
paths += list((ROOT/'agents').glob('A*/runs/*/CLAIMS.json'))+list((ROOT/'claude').glob('B*/runs/*/CLAIMS.json'))
paths += list((ROOT/'agents').glob('A*/runs/*/REPORT.md'))+list((ROOT/'claude').glob('B*/STREAM_NOTES.md'))
for a in ['A021','A023','A051','A087','A090','A096','A097','A098','A099']:
    for d in (ROOT/'agents'/a/'runs').glob('*'):
        paths += [p for p in d.glob('*.md') if p not in paths]
        paths += [p for p in d.glob('out/*') if p.is_file() and re.search(r'(CORRECTION|PROPAGATION|CONSUMED|CERTIFICATE_INTAKE|RESULTS)',p.name,re.I)]
paths += [p for p in (CAN/'verification').glob('*RECEIPTS*.json')]
paths += list((ROOT/'agents').glob('A*/STATUS.md'))
paths += [RUN.parent/'20261011T231552Z-fleet05-A100-release-and-continuation-ledger/out/THEOREM_RELEASE_LEDGER.json']
sources=[]; claims=[]; texts={}; failures=[]
for p in sorted(set(paths)):
    if p.is_relative_to(RUN) or not p.is_file(): continue
    raw=p.read_bytes(); sources.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    text=raw.decode('utf-8-sig',errors='replace'); texts[str(p)]=text
    if p.name=='CLAIMS.json' or p.name=='CLAIM_REGISTRY.json':
        try:
            x=json.loads(text); rows=x if isinstance(x,list) else x.get('claims',[])
            if not isinstance(rows,list): rows=list(rows.values())
            for c in rows:
                if isinstance(c,dict) and c.get('claim_id'):
                    claims.append({'source':str(p),'record':c,'statement_only_sha256':hashlib.sha256(c.get('exact_statement','').encode()).hexdigest()})
        except Exception as e: failures.append({'source':str(p),'error':str(e)})
write('SOURCE_RECEIPTS.json',{'snapshot_utc':datetime.now(timezone.utc).isoformat(),'files':sources,'interpretation':'Full byte intake; selected mathematical inspection, not full independent proof review.'})
write('CLAIM_CENSUS.json',claims); write('PARSE_FAILURES.json',failures)
hits=[]
patterns={'A096_SIGN':r'A096|J_X|singleton.half.tax','B11_EQUIVALENCE':r'K_desc|proper.block|block.descent|FEI.equivalent','MINIMUM_CALIBRATION':r'min_i|min_\(|min\{.*B_i|bounded.ratio|calibration','A021_RETRACTION':r'A021|remainder.sign|RETRACT|WITHDRAW|narrow.*accept'}
for path,t in texts.items():
    if Path(path).suffix!='.md': continue
    for i,l in enumerate(t.splitlines()):
        for tag,pattern in patterns.items():
            if re.search(pattern,l,re.I): hits.append({'tag':tag,'source':path,'line':i+1,'text':l})
write('CORRECTION_CITATIONS.json',hits)
edges=[]
for x in claims:
    c=x['record']
    for d in c.get('proof_dependencies',[]):
        if isinstance(d,dict): dep=d.get('claim_id'); version=d.get('version'); detail=d
        else: dep=str(d).split('@')[0]; version=str(d).split('@')[1] if '@' in str(d) else None; detail=d
        if dep: edges.append({'premise_id':dep,'premise_version':version,'conclusion_id':c['claim_id'],'conclusion_version':c.get('version'),'source':x['source'],'detail':detail})
write('DEPENDENCY_EDGES.json',edges)
bad={( 'A021-UNIFORM-RARE-CORE-EXPANSION',1)}; reached=set(bad); closure=[]
while True:
    changed=False
    for e in edges:
        premise=(e['premise_id'],e['premise_version'])
        # Unknown versions are potential consumers, never silently treated as exact dependencies.
        if premise in reached:
            if e not in closure: closure.append(e)
            target=(e['conclusion_id'],e['conclusion_version'])
            if target not in reached: reached.add(target); changed=True
    if not changed: break
write('A021_VERSIONED_CLOSURE.json',{'refuted_component':'Negative entropy-series remainder in A021-UNIFORM-RARE-CORE-EXPANSION@1','reachable_nodes':[{'claim_id':i,'version':v} for i,v in sorted(reached,key=str)],'exact_version_edges':closure,'version_unspecified_edges':[e for e in edges if e['premise_id']=='A021-UNIFORM-RARE-CORE-EXPANSION' and e['premise_version'] is None],'note':'Potential taint map only. Exact formulas and direct KL proofs may survive independently; human subclaim inspection decides status.'})
runs=[]
for a in sorted((ROOT/'agents').glob('A*')):
    for r in sorted((a/'runs').glob('*')):
        if not r.is_dir() or r==RUN: continue
        presence={n:(r/n).is_file() for n in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']}
        runs.append({'agent':a.name,'run':r.name,'path':str(r),'required_files':presence,'local_four_file_complete':all(presence.values()),'remote_copy_verified_this_stage':False,'public_release_verified_this_stage':False})
write('LOCAL_PERSISTENCE_CENSUS.json',runs)
(OUT/'BOARD_SNAPSHOT.md').write_bytes((ROOT/'BOARD.md').read_bytes())
(OUT/'B20_NOTES_SNAPSHOT.md').write_bytes((ROOT/'claude/B20/STREAM_NOTES.md').read_bytes())
print(json.dumps({'source_files':len(sources),'claim_records':len(claims),'parse_failures':len(failures),'local_runs':len(runs),'A021_exact_reachable_nodes':len(reached)},indent=2))
