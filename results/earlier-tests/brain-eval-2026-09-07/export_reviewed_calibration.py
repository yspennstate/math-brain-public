"""Consume an exact independent review receipt; never create semantic attestations.

Published-source soundness and adapted-clean-form soundness are different claims.
This consumer preserves the independent receipt and source normalization disclosures.
It exports question text only into a private solver-input subdirectory. Nothing
here is a source-note ingestion path or an empirical utility measurement.
"""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, secrets

ITEM_FIELDS={'schema','item_id','bank_version','claim','argument_steps','prompt'}
DECISIONS={'ACCEPT_SIX_FOR_PRIVATE_CALIBRATION_ONLY':6,
           'ACCEPT_EIGHT_FOR_PRIVATE_CALIBRATION_ONLY':8}

def sha(data):return hashlib.sha256(data).hexdigest()
def digest(value):return sha(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
def object_pairs(pairs):
    result={}
    for k,v in pairs:
        if k in result:raise ValueError('duplicate JSON member')
        result[k]=v
    return result
def parse(data):
    def invalid(value):raise ValueError('non-finite JSON constant')
    return json.loads(data,object_pairs_hook=object_pairs,parse_constant=invalid)
def records(data):
    result=[parse(line) for line in data.decode('utf-8').splitlines() if line.strip()]
    if not all(isinstance(r,dict) for r in result):raise ValueError('non-object row')
    return result
def unique(rows):
    out={}
    for r in rows:
        identifier=r.get('item_id')
        if not isinstance(identifier,str) or not identifier or identifier in out:raise ValueError('invalid or duplicate item identity')
        out[identifier]=r
    return out

def count_matches(counts,names,expected):
    present=[counts[name] for name in names if name in counts]
    return bool(present) and all(type(value) is int and value==expected for value in present)

def validate_packet(blobs,review,author_id):
    if review.get('schema')!='independent-calibration-semantic-review/v1':raise ValueError('unknown review schema')
    expected=DECISIONS.get(review.get('decision'))
    if expected is None:raise ValueError('non-acceptance or unsupported decision')
    reviewer=review.get('reviewer')
    if not isinstance(reviewer,str) or not reviewer.strip() or reviewer==author_id:raise ValueError('reviewer identity absent or same as author')
    pins=review.get('input_files',{})
    if not {'items.jsonl','keys.jsonl','sources.jsonl','pairs.jsonl'}<=pins.keys():raise ValueError('incomplete reviewed input pins')
    for filename,expected_hash in pins.items():
        if filename not in blobs or sha(blobs[filename])!=expected_hash:raise ValueError('reviewed input drift')
    values={name:records(blobs[name+'.jsonl']) for name in ['items','keys','sources','pairs','splits']}
    indexed={name:unique(values[name]) for name in ['items','keys','sources','splits']}
    ids=set(indexed['items'])
    if len(ids)!=expected or any(set(rows)!=ids for rows in indexed.values()):raise ValueError('packet identity or count mismatch')
    judged=unique(review.get('items',[]))
    if set(judged)!=ids:raise ValueError('review does not cover exact item set')
    if not count_matches(review.get('counts',{}),['items','forms'],expected):raise ValueError('review count disagrees')
    for identifier,item in indexed['items'].items():
        key=indexed['keys'][identifier];source=indexed['sources'][identifier];judgment=judged[identifier]
        if set(item)!=ITEM_FIELDS:raise ValueError('unexpected solver-facing field')
        if not isinstance(item['claim'],str) or not item['claim'].strip():raise ValueError('empty claim')
        steps=item['argument_steps']
        if not isinstance(steps,list) or not steps:raise ValueError('empty steps')
        for n,step in enumerate(steps,1):
            if (set(step)!= {'n','text'} or type(step['n']) is not int or step['n']!=n or not isinstance(step['text'],str) or not step['text'].strip()):raise ValueError('malformed numbered steps')
        truth=key.get('truth');fault=key.get('fault_step')
        if truth not in {'clean','flawed'}:raise ValueError('unknown truth')
        if truth=='clean' and fault is not None:raise ValueError('clean has fault')
        if truth=='flawed' and (type(fault) is not int or not 1<=fault<=len(steps)):raise ValueError('invalid fault')
        if judgment.get('fault_step') is not None and type(judgment['fault_step']) is not int:raise ValueError('invalid review fault type')
        if (judgment.get('accepted_truth'),judgment.get('fault_step'))!=(truth,fault):raise ValueError('review/key disagreement')
        if source.get('item_sha256')!=digest(item) or source.get('key_sha256')!=digest(key):raise ValueError('source binding mismatch')
        if source.get('claim')!=item['claim']:raise ValueError('source claim differs')
        original=source.get('original_steps')
        if not isinstance(original,list) or len(original)!=len(steps):raise ValueError('missing adapted clean form')
        changed=[n for n,(old,step) in enumerate(zip(original,steps),1) if old!=step['text']]
        if changed!=([] if truth=='clean' else [fault]):raise ValueError('mutation does not match keyed step')
        if not isinstance(source.get('normalization_disclosure'),str) or not source['normalization_disclosure'].strip():raise ValueError('missing source adaptation disclosure')
        if indexed['splits'][identifier]['split']!='calibration':raise ValueError('exposed family cannot become heldout')
    covered=set();groups=set();families=set()
    for pair in values['pairs']:
        pair_ids=pair['item_ids'];group=pair['proof_group'];family=pair['paper_family']
        if pair.get('split')!='calibration' or len(pair_ids)!=2 or len(set(pair_ids))!=2 or covered&set(pair_ids) or not set(pair_ids)<=ids:raise ValueError('invalid pair coverage')
        if group in groups:raise ValueError('duplicate proof group')
        if {indexed['keys'][i]['truth'] for i in pair_ids}!={'clean','flawed'}:raise ValueError('pair lacks both forms')
        for i in pair_ids:
            if indexed['sources'][i]['proof_group']!=group or indexed['sources'][i]['paper_id']!=family:raise ValueError('pair source identity differs')
        covered.update(pair_ids);groups.add(group);families.add(family)
    if covered!=ids:raise ValueError('unpaired item')
    if not count_matches(review['counts'],['distinct_source_proofs','source_proofs'],len(groups)) or not count_matches(review['counts'],['paper_families'],len(families)):raise ValueError('review source counts differ')
    return values,dict(accepted_forms=len(ids),distinct_source_proofs=len(groups),paper_families=len(families),split='calibration',evaluated_forms=0,heldout_safe_forms=0,difficulty='UNMEASURED',brain_utility='UNMEASURED')

def load_packet(packet,review_path,review_sha256,author_id):
    review_bytes=review_path.read_bytes()
    if sha(review_bytes)!=review_sha256:raise ValueError('independent receipt drift')
    review=parse(review_bytes)
    blobs={name: (packet/name).read_bytes() for name in ['items.jsonl','keys.jsonl','sources.jsonl','pairs.jsonl','splits.jsonl']}
    manifest=parse((packet/'MANIFEST.json').read_bytes())
    for name,data in blobs.items():
        if manifest['sha256'].get(name)!=sha(data):raise ValueError('packet manifest mismatch')
    values,summary=validate_packet(blobs,review,author_id)
    for source in values['sources']:
        for stem in ['source_file','license_evidence']:
            if sha(Path(source[stem+'_path']).read_bytes())!=source[stem+'_sha256']:raise ValueError('source evidence drift')
    return values,summary,review

def write_private(values,summary,review,review_path,review_hash,output,private_root):
    target=output.resolve();root=private_root.resolve()
    if not target.is_relative_to(root) or target==root:raise ValueError('export must be a new child of declared private root')
    if target.exists():raise ValueError('output already exists')
    aliases={r['item_id']:'pt_'+secrets.token_hex(16) for r in values['items']}
    if len(set(aliases.values()))!=len(aliases):raise ValueError('alias collision')
    transported=[dict(r,item_id=aliases[r['item_id']]) for r in values['items']]
    transported.sort(key=lambda r:r['item_id'])
    data=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in transported).encode('utf-8')
    target.mkdir(parents=True);solver=target/'solver_input';solver.mkdir()
    (solver/'items.jsonl').write_bytes(data)
    (solver/'NO_INGEST.md').write_text('Private calibration tests, not notes. Serve one item per fresh solver context and at most one matched form from a proof in any accumulating session. Do not ingest into memory or literature-note stores.\n',encoding='utf-8')
    receipt=dict(schema='reviewed-private-calibration-export/v1',as_of=datetime.now(timezone.utc).isoformat(),summary=summary,
        review_path=str(review_path.resolve()),review_sha256=review_hash,reviewer=review['reviewer'],
        solver_items_sha256=sha(data),published_source_soundness='NOT_CERTIFIED_BY_THIS_EXPORTER',
        adapted_clean_form_status='ACCEPTED_BY_PINNED_INDEPENDENT_REVIEW',
        review_scope=review.get('scope'),source_adaptations=[dict(proof_group=r['proof_group'],normalization=r['normalization_disclosure']) for r in values['sources'] if r['item_id'] in {p['item_ids'][0] for p in values['pairs']}],
        transport_bindings=[dict(source_item_id=i,transport_item_id=alias) for i,alias in sorted(aliases.items())],
        use='PRIVATE_CALIBRATION_ONLY; no publication, license determination, solver call, source-note ingestion or utility claim')
    (target/'PRIVATE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    return receipt

def main():
    p=argparse.ArgumentParser()
    for arg in ['packet','review','output','private-root']:p.add_argument('--'+arg,type=Path,required=True)
    p.add_argument('--review-sha256',required=True);p.add_argument('--author-id',required=True);a=p.parse_args()
    values,summary,review=load_packet(a.packet,a.review,a.review_sha256,a.author_id)
    write_private(values,summary,review,a.review,a.review_sha256,a.output,a.private_root)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
