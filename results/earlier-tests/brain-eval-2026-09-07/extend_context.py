"""Serial continuation over downloaded math.PR papers absent from proof rows.

Archive-bound candidate contexts, never an accepted-question counter. The strict
source reader is loaded from the existing continuation implementation by hash.
No model, network, training, GPU, or production writes occur.
"""
from pathlib import Path
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode=True


def load_rows(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]


def admit(compute):
    state=json.loads(compute.read_text(encoding='utf-8'))
    # The governor's naive clock is local machine time.
    stamp=datetime.strptime(state['ts'],'%Y-%m-%d %H:%M:%S')
    age=(datetime.now()-stamp).total_seconds()
    if age < -5 or age > 120 or state['status']=='distress' or state['mode']=='throttle':
        raise RuntimeError('Resource admission paused: stale/distress/throttle')
    if state['mem_avail_mb']<12000 or state.get('hung_windows',0)>0 or state['cpu_pct']>85:
        raise RuntimeError('Resource admission paused: pressure or UI warning')
    return {'ts':state['ts'],'cpu_pct':state['cpu_pct'],'mem_avail_mb':state['mem_avail_mb'],'mode':state['mode']}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--reader',type=Path,required=True)
    p.add_argument('--reader-sha256',required=True); p.add_argument('--archive-root',type=Path,required=True)
    p.add_argument('--existing-proofs',type=Path,required=True); p.add_argument('--output',type=Path,required=True)
    p.add_argument('--compute',type=Path,required=True); p.add_argument('--limit',type=int,default=200)
    p.add_argument('--download-after',default='',help='Explicit local download timestamp lower bound; optional')
    p.add_argument('--offset',type=int,default=0,help='Skip this many eligible papers; keep a disjoint continuation')
    a=p.parse_args()
    if hashlib.sha256(a.reader.read_bytes()).hexdigest()!=a.reader_sha256:
        raise ValueError('Reader source changed')
    spec=importlib.util.spec_from_file_location('context_reader',a.reader)
    reader=importlib.util.module_from_spec(spec); spec.loader.exec_module(reader)
    completed=defaultdict(list)
    for r in load_rows(a.archive_root/'download_log.jsonl'):
        if r.get('kind') in ('tar','single_tex') and r.get('n_tex',0)>0:
            completed[r['base_id']].append(r)
    metadata={r['base_id']:r for r in load_rows(a.archive_root/'listing.jsonl')}
    existing={r['paper'] for r in load_rows(a.existing_proofs)}
    candidates=[iid for iid,rs in completed.items() if iid not in existing and len(rs)==1
        and metadata.get(iid,{}).get('primary_category')=='math.PR' and rs[0].get('bytes',0)<=2500000
        and (not a.download_after or rs[0].get('ts','')>a.download_after)]
    a.output.mkdir(parents=True,exist_ok=False)
    records=[]; counts=Counter(); proof_ids=set()
    plan={'schema':'unprocessed-source-plan/v1','as_of':datetime.now(timezone.utc).isoformat(),
          'eligible_papers_absent_from_existing_proof_rows':len(candidates),'selected_papers':candidates[a.offset:a.offset+a.limit],
          'download_after_local':a.download_after,
          'existing_proofs_sha256':hashlib.sha256(a.existing_proofs.read_bytes()).hexdigest(),
          'reader_sha256':a.reader_sha256,'meaning':'Selection before reading outputs; structural context only. Absence from proof rows does not prove no prior extraction attempt. All selected papers have exactly one successful download receipt, primary math.PR metadata and archives <=2.5MB.'}
    (a.output/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n',encoding='utf-8')
    for iid in candidates[a.offset:a.offset+a.limit]:
        try:
            resource=admit(a.compute)
        except RuntimeError as error:
            records.append({'status':'PAUSED','reason':str(error)}); break
        try:
            rows,receipt,body=reader.extract_paper(a.archive_root/'tex',iid,completed[iid][0],metadata[iid],archive=a.archive_root/'src'/(iid.replace('/','_')+'.bin'))
            summary=reader.write_extraction(a.output/'papers'/iid.replace('/','_'),rows,receipt,body)
            passed={r['source_proof_identity'] for r in rows if r['candidate_filter_pass']}
            proof_ids.update(passed)
            counts['papers_extracted']+=1; counts['all_proof_occurrences']+=len(rows)
            counts['structural_candidate_occurrences']+=summary['structural_candidate_filter_pass_occurrences']
            records.append({'paper':iid,'status':'EXTRACTED','summary':summary,'resource':resource})
        except Exception as error:
            counts['papers_failed']+=1; records.append({'paper':iid,'status':'FAILED','error_type':type(error).__name__,'reason':str(error)[:300],'resource':resource})
        if len(records)%25==0:
            print(json.dumps({'processed':len(records),'structural_distinct':len(proof_ids),'counts':counts}),flush=True)
        (a.output/'PROGRESS.json').write_text(json.dumps({'records':records,'counts':counts,'distinct_structural_proof_candidates':len(proof_ids),'semantic_accepted':0,'new_solver_questions':0},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'processed':len(records),'counts':counts,'distinct_structural_proof_candidates':len(proof_ids),'semantic_accepted':0,'new_solver_questions':0}))


if __name__=='__main__':
    main()
