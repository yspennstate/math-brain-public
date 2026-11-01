"""Recompute counts from private source and acceptance evidence, without exporting proofs."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, sys

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rows(p): return [json.loads(line) for line in Path(p).read_text(encoding='utf-8').splitlines() if line.strip()]

def main():
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--prior-spec',type=Path,required=True);p.add_argument('--exporter',type=Path,required=True);p.add_argument('--review',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    # The pre-existing exporter itself verifies every pinned packet and replays its pinned gate.
    sys.path.insert(0,str(a.exporter.parent));import export_accepted_source_pairs as exporter
    previous=exporter.build(json.loads(a.prior_spec.read_text(encoding='utf-8')))
    summaries=[];all_papers=set();all_occurrences=set();all_proofs=set();later_papers=set();later_proofs=set()
    for name in ['context_extension_v1','context_extension_v2','context_extension_v3']:
        run=a.private_root/name;plan=json.loads((run/'PLAN.json').read_text(encoding='utf-8'));progress=json.loads((run/'PROGRESS.json').read_text(encoding='utf-8'))
        papers=set();occurrences=set();proofs=set();total_occurrences=0
        for folder in sorted((run/'papers').iterdir()):
            if not folder.is_dir(): continue
            papers.add(folder.name)
            manifest=json.loads((folder/'MANIFEST.json').read_text(encoding='utf-8'))
            # Source extractor receipts have a files hash table in each progress record.
            record=next(r for r in progress['records'] if r['paper']==folder.name)
            for filename,expected in record['summary']['files'].items():
                if sha(folder/filename)!=expected: raise ValueError('source extraction bytes drifted')
            for row in rows(folder/'proof_candidates.jsonl'):
                total_occurrences+=1;occurrences.add(row['source_occurrence_identity'])
                if row['candidate_filter_pass']:proofs.add(row['source_proof_identity'])
        if papers != set(plan['selected_papers']): raise ValueError('selected and extracted paper sets differ')
        if total_occurrences != progress['counts']['all_proof_occurrences']:raise ValueError('occurrence count differs')
        if len(proofs) != progress['distinct_structural_proof_candidates']:raise ValueError('structural proof count differs')
        all_papers.update(papers);all_occurrences.update(occurrences);all_proofs.update(proofs)
        if plan.get('download_after_local'):
            later_papers.update(papers);later_proofs.update(proofs)
        summaries.append(dict(run=name,papers=len(papers),all_proof_occurrences=total_occurrences,distinct_structural_candidates=len(proofs),plan_sha256=sha(run/'PLAN.json'),progress_sha256=sha(run/'PROGRESS.json'),download_after_local=plan.get('download_after_local')))
    packet=a.private_root/'source_pairs_v1';review=json.loads(a.review.read_text(encoding='utf-8'))
    if review['decision']!='ACCEPT_SIX_FOR_PRIVATE_CALIBRATION_ONLY':raise ValueError('unexpected review decision')
    for filename,expected in review['input_files'].items():
        if sha(packet/filename)!=expected:raise ValueError('reviewed packet changed')
    inputs={name:rows(packet/(name+'.jsonl')) for name in ['items','keys','sources','pairs','splits']}
    ids={r['item_id'] for r in inputs['items']};review_ids={r['item_id'] for r in review['items']}
    if len(ids)!=6 or ids!=review_ids or len(review_ids)!=len(review['items']):raise ValueError('review coverage mismatch')
    keys={r['item_id']:r for r in inputs['keys']}
    for r in review['items']:
        if (r['accepted_truth'],r['fault_step'])!=(keys[r['item_id']]['truth'],keys[r['item_id']]['fault_step']):raise ValueError('review key disagreement')
    if {r['item_id'] for r in inputs['splits']}!=ids or any(r['split']!='calibration' for r in inputs['splits']):raise ValueError('not complete calibration split')
    groups={r['proof_group'] for r in inputs['pairs']};families={r['paper_family'] for r in inputs['pairs']}
    old_groups={r['proof_group'] for r in previous['pairs']};old_families={r['paper_family'] for r in previous['pairs']}
    if groups&old_groups or families&old_families:raise ValueError('new packet overlaps recovered prior source families')
    for s in inputs['sources']:
        for key in ['source_file','license_evidence']:
            if sha(s[key+'_path'])!=s[key+'_sha256']:raise ValueError('source evidence changed')
    result=dict(schema='brain-corpus-recovery-inventory/v1',as_of=datetime.now(timezone.utc).isoformat(),
        source_extensions=summaries,distinct_extracted_papers=len(all_papers),extraction_attempts=sum(r['papers'] for r in summaries),distinct_structural_proof_candidates=len(all_proofs),later_download_papers=len(later_papers),later_download_distinct_structural_proof_candidates=len(later_proofs),
        recovered_prior=previous['summary'],new_packet=dict(accepted_forms=6,distinct_source_proofs=len(groups),source_families=len(families),review_path=str(a.review),review_sha256=sha(a.review),acceptance_basis='Independent receipt; legacy per-item review schema adaptation pending'),
        combined=dict(accepted_private_calibration_forms=previous['summary']['accepted_forms']+6,distinct_source_proofs=len(old_groups|groups),source_families=len(old_families|families),heldout_safe_forms=0,evaluated_forms=0,difficulty='UNMEASURED',brain_utility='UNMEASURED'),
        distinctions=['Structural extraction is not semantic acceptance.','Absence from old proof rows does not prove no prior extraction attempt.','The newly downloaded count uses the recorded local download timestamp cutoff, not paper publication date.','Different proofs from one paper are a shared family, not statistically independent observations.','Private source/key files remain excluded from memory indexes and public export.'])
    with a.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:result[k] for k in ['extraction_attempts','distinct_extracted_papers','distinct_structural_proof_candidates','later_download_papers','combined']},indent=2))

if __name__=='__main__':main()
