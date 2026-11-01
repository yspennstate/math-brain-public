"""Record existing scoped peer verdicts; do not audit another review."""
import datetime
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ref=Path('~/brain_workers/w545/VERDICTS.jsonl')
adv=Path('~/brain_workers/w544/AUDIT_VERDICTS.jsonl')
refrows=[json.loads(s) for s in ref.read_text(encoding='utf-8').splitlines() if s.strip()]
advrows=[json.loads(s) for s in adv.read_text(encoding='utf-8').splitlines() if s.strip()]
refrows=[r for r in refrows if r.get('target','').startswith('w543:P0321-H')]
advrows=[r for r in advrows if r.get('target','').startswith('w543 ATTEMPT.md H')]
byh={r['target'].rsplit('-',1)[1]:r for r in refrows}
for h in ('H1','H2','H3','H4'):
    assert byh[h]['verdict']=='KEEP'
    matched=[r for r in advrows if h in r['target']]
    assert matched and all(r['verdict']=='KEEP' for r in matched)
snapshot=Path('~/brain_workers/w544/audit_snapshots/w543_ATTEMPT.md')
same=snapshot.read_bytes()==(ROOT/'ATTEMPT.md').read_bytes()
assert same,'Audited snapshot differs; no independent-check upgrade made'
receipt={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope':'H1-H4 Gaussian auxiliary model only; not a P0321 proof or cross-account admission',
    'referee':'w545','referee_path':str(ref),'referee_verdicts':refrows,
    'adversary':'w544','adversary_path':str(adv),'adversary_verdicts':advrows,
    'audited_snapshot_path':str(snapshot),'author_proof_matches_audited_snapshot_byte_for_byte':same,
    'different_login_provenance':'UNVERIFIED','store_or_source_admission':False,
    'formal_proof_receipt':None,'proof_statement_changed':False}
(ROOT/'AUDIT_RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
for name in ('CLAIMS_MODEL.jsonl','CLAIMS.jsonl'):
    rows=[json.loads(s) for s in (ROOT/name).read_text(encoding='utf-8').splitlines() if s.strip()]
    for c in rows:
        h=c['claim_id'].rsplit('-',1)[1]
        if h not in byh:continue
        c['status']='independently checked proof'
        c['independent_reviewer']='w544 and w545: scoped auxiliary-model KEEP; different-login provenance UNVERIFIED'
        c['independent_audits']=[{'reviewer':'w545','verdict':'KEEP','path':str(ref),'target':'w543:P0321-'+h},
            {'reviewer':'w544','verdict':'KEEP','path':str(adv),'target':next(r['target'] for r in advrows if h in r['target'])}]
        c['remaining_gap']='Microscopic Riesz identification and the defect-aware reduction remain open; different-login admission evidence not verified.'
    (ROOT/name).write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in rows),encoding='utf-8')
print(json.dumps({'independently_checked_auxiliary_claims':4,'referee_keep_rows':len(refrows),
                  'adversary_keep_rows':len(advrows),'snapshot_exact_match':same,'cross_account_admission':False}))
