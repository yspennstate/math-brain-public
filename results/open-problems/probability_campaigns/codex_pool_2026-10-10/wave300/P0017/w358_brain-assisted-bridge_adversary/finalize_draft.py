"""Finalize owned draft text/receipts; preserve every unrelated file and live store."""
from pathlib import Path
import difflib
import json
from prepare_review import validate

root=Path(__file__).parent
dest=Path('~/math-brain-inbox/w358/bundle_001.json')
before=(root/'bundle_001.json').read_text(encoding='utf-8')
assert dest.read_text(encoding='utf-8')==before, 'Published draft changed; do not overwrite'
bundle=json.loads(before)
for e in bundle['entries']:
    if e['key']=='appell-calibration':
        e['statement']=e['statement'].replace('the normalized tilt coefficient T_d f=F_f^(d)(0)/d!',
            'define F_f(s)=E[f(X)exp(sX)]/E[exp(sX)]. The normalized tilt coefficient T_d f=F_f^(d)(0)/d!')
    if e['key']=='posterior-nonstrict':
        e['statement']=e['statement'].replace('and T_t f=E[f(X)|Y].',
            'and T_t f(y)=E[f(X)|Y=y]. For a law rho, D_rho(g)=integral |grad g|^2 d rho.')
    if e['key']=='strict-gap':
        e['statement']=e['statement'].replace('For log-concave mu with finite K=CP(mu),',
            'Let X~mu, G~N(0,I) independent, Y=X+sqrt(t)G, nu_t=Law(Y), T_t f(y)=E[f(X)|Y=y], and D_rho(g)=integral |grad g|^2 d rho. Write Q_t(mu)=sup_f D_nu_t(T_t f)/D_mu(f) over Sobolev functions with positive finite energy. For log-concave mu with finite K=CP(mu),')
    if e['key']=='posterior-tail':
        e['statement']=e['statement'].replace('DRAFT special-case derivation awaiting independent referee check.',
            'DRAFT independently checked special-case derivation (w359 KEEP).')
        e['statement']=e['statement'].replace('test f_a(x)=exp(a x),',
            'let Y=X+sqrt(t)G with independent G~N(0,1), nu_t=Law(Y), T_t f(y)=E[f(X)|Y=y], and D_rho(g)=integral |gprime|^2 d rho. Test f_a(x)=exp(a x),')
        e['review_note']='w359 KEEP sections 1-3 and finite >0.7 test; ~/brain_workers/w359/REVIEW_w358_POSTERIOR.md. Derivation: ~/brain_workers/w358/POSTERIOR_BRIDGE_CHECK.md'
receipt=validate(bundle,json.loads((root/'brain_target_lookup.json').read_text(encoding='utf-8')))
payload=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
(root/'bundle_001.json').write_text(payload,encoding='utf-8')
part=dest.with_suffix('.part')
assert str(part.resolve()).lower().startswith(str(dest.parent.resolve()).lower()+'\\')
part.write_text(payload,encoding='utf-8')
# Replace only this worker's unchanged, leased DRAFT, not a live math store.
assert dest.read_text(encoding='utf-8')==before
part.replace(dest)
assert dest.read_text(encoding='utf-8')==payload
(root/'STRUCTURAL_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
target='math-brain-inbox/w358/bundle_001.json'
diff=''.join(difflib.unified_diff([],payload.splitlines(True),fromfile='a/'+target,tofile='b/'+target))
(root/'patches/01_p0017_boundary_bundle.diff').write_text(diff,encoding='utf-8')
key_map={e['key']:e for e in bundle['entries']}
edges=[json.loads(s) for s in (root/'EDGE_REVIEW.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for r in edges:
    r['from_quote']=key_map[r['from_key']]['statement']
    if 'to_key' in r:r['to_quote']=key_map[r['to_key']]['statement']
(root/'EDGE_REVIEW.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edges),encoding='utf-8')
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for c in claims:
    if c['id']=='w358-S1.8':
        c['status']='independently checked proof'
        c['independent_reviewer']='w359 KEEP; ~/brain_workers/w359/REVIEW_w358_POSTERIOR.md'
        c['remaining_gap']='Does not refute existence of some uniform q<1; no general KLS or tensor proof'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
life=json.loads((root/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life['reviewed_claims']=sorted(set(life['reviewed_claims']+['w358-S1.8']))
life['additional_review_receipt']='~/brain_workers/w359/REVIEW_w358_POSTERIOR.md'
life['reviewed']=False
life['local_schema_validation']=receipt
(root/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
submission=json.loads((root/'SUBMISSION_RECEIPT.json').read_text(encoding='utf-8'))
submission['final_text_check']='definitions completed; exact edge ends and owned published JSON synchronized'
(root/'SUBMISSION_RECEIPT.json').write_text(json.dumps(submission,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'final_schema':receipt,'owned_draft_synchronized':True,'reviewed_claims':life['reviewed_claims']}))
