"""Bounded positive and nearby-negative controls for the reused population reflex."""
from pathlib import Path
import argparse, csv, hashlib, json, re

POSITIVES = [
    'The full-history experiment used an inner join and silently removed sessions.',
    'The multi-year evaluation reported only the matched-data intersection.',
    'The intersection silently omitted sessions from the historical analysis.',
    'The pooled tiers were called primary despite the preregistered subgroup.',
    'The proof benchmark pooled both cohorts and was reported as primary despite its registered tier.',
    'The registered primary subgroup was replaced by pooled results.',
    'The preregistered primary stratum was substituted with a pooled estimate.',
    'Pooled accuracy was labeled primary instead of the registered cohort.',
]
NEGATIVES = [
    'The report names the predefined tier and complete row count.',
    'Read the protocol before computing the registered comparison.',
    'The pooled analysis is secondary and descriptive.',
    'The primary analysis uses its preregistered subgroup; pooled accuracy is secondary.',
    'The study preregistered pooled accuracy as its primary endpoint.',
    'The registered primary subgroup is reported alongside pooled descriptive results.',
    'There is no evidence that notes help or harm overall.',
    'Compute a pooled variance estimate in this probability exercise.',
    'The swimming pool has a primary filtration pump.',
    'We are considering a future preregistered pooled analysis.',
    'The proof bank has complete responses but its semantic validity is unresolved.',
    'The registered primary stratum was retained in the pooled data archive.',
    'The primary tier requires more source proofs before the next study.',
    'An inner join matches the two complete tables on their unique IDs.',
    'Compute the intersection of these two finite sets.',
    'The reported primary result agrees with the registered subgroup calculation.',
]

def main():
    p=argparse.ArgumentParser();p.add_argument('--tsv',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    rows=list(csv.DictReader(a.tsv.open(encoding='utf-8'),delimiter='\t'))
    target=next(r for r in rows if r['id']=='silent_intersection_changes_claimed_population')
    regex=re.compile(target['trigger'])
    controls=[dict(text=t,expected=expected,observed=bool(regex.search(t))) for expected,texts in [(True,POSITIVES),(False,NEGATIVES)] for t in texts]
    failures=[c for c in controls if c['expected']!=c['observed']]
    receipt=dict(reflex=target['id'],mode=target['mode'],source=target['source'],tsv_sha256=hashlib.sha256(a.tsv.read_bytes()).hexdigest(),trigger_sha256=hashlib.sha256(target['trigger'].encode()).hexdigest(),positive_count=len(POSITIVES),negative_count=len(NEGATIVES),controls=controls,failures=failures,scope='Authored bounded controls; not measured live precision or general behavioral benefit')
    with a.output.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
    print(json.dumps({k:receipt[k] for k in ['positive_count','negative_count','failures','scope']},indent=2))
    raise SystemExit(bool(failures))

if __name__=='__main__':main()
