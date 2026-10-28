"""Independent aggregate census: no gate, exporter, or inventory module imported.

This checks identities and arithmetic, not semantic acceptance. The reference
inventory supplies the acceptance disposition; its evidence pins are checked.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3

def strict_members(pairs):
    value={}
    for k,v in pairs:
        if k in value:raise ValueError('duplicate JSON member')
        value[k]=v
    return value

def parse(data):
    return json.loads(data,object_pairs_hook=strict_members,
        parse_constant=lambda value:(_ for _ in ()).throw(ValueError('nonfinite JSON')))

def pin(record):
    data=Path(record['path']).read_bytes()
    if hashlib.sha256(data).hexdigest()!=record['sha256']:raise ValueError('input drift')
    return data

def main():
    p=argparse.ArgumentParser();p.add_argument('--spec',type=Path,required=True);p.add_argument('--reference',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    raw=a.spec.read_bytes();spec=parse(raw);reference=parse(a.reference.read_bytes())
    if hashlib.sha256(raw).hexdigest()!=reference['spec_sha256']:raise ValueError('spec differs from reference')
    db=sqlite3.connect(':memory:')
    db.execute('create table census (item text primary key, proof text, family text, split text)')
    for batch in spec['legacy_packets']+spec['reviewed_packets']:
        if 'packet' in batch:
            review=parse(pin(batch['review']));folder=Path(batch['packet']);blobs={}
            for name in ['sources','pairs']:
                data=(folder/(name+'.jsonl')).read_bytes()
                if hashlib.sha256(data).hexdigest()!=review['input_files'][name+'.jsonl']:raise ValueError('review input drift')
                blobs[name]=data
            pairs=[parse(line) for line in blobs['pairs'].splitlines() if line.strip()]
            split_rows=[dict(item_id=item,split=pair['split']) for pair in pairs for item in pair['item_ids']]
        else:blobs={name:pin(batch[name]) for name in ['sources','splits']}
        sources=[parse(line) for line in blobs['sources'].splitlines() if line.strip()]
        if 'packet' not in batch:split_rows=[parse(line) for line in blobs['splits'].splitlines() if line.strip()]
        splits={r['item_id']:r['split'] for r in split_rows}
        if len(splits)!=len(split_rows):raise ValueError('duplicate split')
        if set(splits)!={r['item_id'] for r in sources}:raise ValueError('source/split identities differ')
        for row in sources:
            # Only the observed arXiv identifiers are accepted in this check.
            matched=re.fullmatch(r'(?:arxiv:)?(\d{4}\.\d{4,5})(?:v\d+)?',row['paper_id'].strip(),re.I)
            if not matched:raise ValueError('unhandled source identifier: '+row['paper_id'])
            split=splits[row['item_id']]
            if split not in ['calibration','heldout']:raise ValueError('unknown split')
            scope='calibration' if split=='calibration' else 'heldout_provisional_not_certified'
            db.execute('insert into census values (?,?,?,?)',(row['item_id'],row['proof_group'],matched[1],scope))
    counts={}
    for scope,forms,proofs,families in db.execute('select split,count(*),count(distinct proof),count(distinct family) from census group by split'):
        counts[scope]=dict(accepted_forms=forms,distinct_source_proofs=proofs,paper_families=families)
    if counts!=reference['summary']:raise ValueError('independent SQL census disagrees')
    cross=db.execute('select family from census group by family having count(distinct split)>1').fetchall()
    if cross:raise ValueError('family crosses splits')
    result=dict(schema='independent-sqlite-corpus-counts/v1',counts=counts,total_rows=db.execute('select count(*) from census').fetchone()[0],distinct_proofs=db.execute('select count(distinct proof) from census').fetchone()[0],family_cross_split_count=0,reference_sha256=hashlib.sha256(a.reference.read_bytes()).hexdigest(),spec_sha256=hashlib.sha256(raw).hexdigest(),scope='Independent identity/arithmetic check only; acceptance truth and utility are not tested.')
    with a.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
