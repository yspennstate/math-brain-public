"""Materialize existing source-review backlog; generate no new proof questions."""
import argparse
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import export_reviewed_calibration as strict

def main():
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--inventory-spec',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--summary',type=Path,required=True);a=p.parse_args()
    spec=strict.parse(a.inventory_spec.read_bytes());reviewed=set()
    for packet in spec['reviewed_packets']:
        values,_,_=strict.load_packet(Path(packet['packet']),Path(packet['review']['path']),packet['review']['sha256'],spec['author_id'])
        reviewed.update(r['proof_group'] for r in values['sources'])
    found={};rejects=Counter();paper_states=Counter();context_issues=Counter();pins=[];occurrences=0;papers=set()
    for run in ['context_extension_v1','context_extension_v2','context_extension_v3']:
        root=a.private_root/run;progress_path=root/'PROGRESS.json';data=progress_path.read_bytes();progress=strict.parse(data)
        pins.append(dict(path=str(progress_path),sha256=hashlib.sha256(data).hexdigest()))
        for paper in progress['records']:
            paper_states[paper['status']]+=1
            if paper['status']!='EXTRACTED':continue
            if paper['paper'] in papers:raise ValueError('paper repeated across extraction runs')
            papers.add(paper['paper']);folder=root/'papers'/paper['paper'].replace('/','_')
            blobs={}
            for filename,expected in paper['summary']['files'].items():
                raw=(folder/filename).read_bytes()
                if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('extraction file changed')
                blobs[filename]=raw
            context=strict.parse(blobs['source_context.json'])
            context_issues.update(x['kind'] for x in context.get('issues',[]))
            for row in strict.records(blobs['proof_candidates.jsonl']):
                occurrences+=1
                if not row['candidate_filter_pass']:
                    rejects[row['candidate_filter_reject_reason']]+=1;continue
                key=row['source_proof_identity']
                record=dict(source_proof_identity=key,paper=row['paper'],source_version=row['source_version'],source_context_path=str(folder/'source_context.json'),source_context_sha256=paper['summary']['files']['source_context.json'],candidate_file_path=str(folder/'proof_candidates.jsonl'),candidate_file_sha256=paper['summary']['files']['proof_candidates.jsonl'],source_occurrence_identity=row['source_occurrence_identity'],n_steps=row['n_steps'],proof_chars=row['proof_chars'],status='REVIEWED_PRIVATE_CALIBRATION' if key in reviewed else 'SEMANTIC_REVIEW_REQUIRED',next_check='Read full localized source, explicit dependencies and license provenance; decide soundness before authoring any matched mutation. No semantic acceptance or utility is implied by this queue.')
                found.setdefault(key,record)
    if reviewed-set(found):raise ValueError('reviewed source not in the structural queue')
    rows=sorted(found.values(),key=lambda x:(x['status']=='REVIEWED_PRIVATE_CALIBRATION',x['paper'],x['source_proof_identity']))
    output=a.output.resolve();root=a.private_root.resolve()
    if output==root or not output.is_relative_to(root):raise ValueError('queue must remain private')
    with output.open('x',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps(row,sort_keys=True)+'\n')
    summary=dict(schema='existing-source-review-backlog/v1',as_of=datetime.now(timezone.utc).isoformat(),paper_states=dict(paper_states),distinct_extracted_papers=len(papers),proof_occurrences=occurrences,distinct_structural_proofs=len(found),independently_reviewed_new_proofs=len(reviewed),remaining_semantic_review_proofs=len(set(found)-reviewed),structural_reject_occurrences=dict(rejects),context_issue_occurrences=dict(context_issues),queue_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),input_pins=pins,scope='Existing source contexts only. No new source fetch, proof form, semantic acceptance, note, solver run or utility result. Rejection reasons count occurrences and are not distinct proof counts.')
    with a.summary.open('x',encoding='utf-8') as f:json.dump(summary,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='input_pins'},indent=2))

if __name__=='__main__':main()
