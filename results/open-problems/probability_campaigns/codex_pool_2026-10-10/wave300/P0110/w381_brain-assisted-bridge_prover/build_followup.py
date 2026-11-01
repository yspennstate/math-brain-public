"""Save the continued matching-gap deductions as an additional DRAFT, not a replacement."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
attempt=(root/'ATTEMPT.md').read_text(encoding='utf-8')
def proof(name):return attempt.split('## '+name+':',1)[1].split('\n## ',1)[0].split('\nNEXT:',1)[0].strip()
def entry(key,kind,title,statement,assumptions,body=None):
    return {'key':key,'namespace':'probability.first-passage-percolation','logical_name':'p0110-w381-'+key,
      'kind':kind,'title':title,'statement':statement,'proof_text':body,'assumptions':assumptions,
      'domain':'probability / fluctuation exponent matching',
      'source':{'source_id':'owner-p0110-w381-20261010:'+key,'url':'urn:owner-own-work:p0110:w381:20261010:'+key,
        'revision':'draft-20261010-independently-unchecked','license':'owner-own-work (campaign deduction; independent review pending)','excerpt':None}}
entries=[
 entry('variance-tightness-matching-shortcut','concept','Rejected inference from variance-normalized concentration to matching thresholds',
  'REJECTED GENERIC INFERENCE: uniform exponential concentration normalized by the actual standard deviation, bounded positive path weights, and linear mean passage times do not alone force the uniform upper concentration exponent to equal the uniform lower variance exponent. Uniform power regularity of the variance scale or additional model structure is required. This rejects a generic shortcut and does not assert failure for an iid stationary lattice FPP law.',
  ['The rejected implication concerns general passage-time families; it must not be attributed to the original iid-lattice theorem']),
 entry('bounded-ray-oscillating-variance','lemma','A bounded positive dependent ray metric has tight normalized concentration and unmatched thresholds',
  'Let S={4^k:k>=1}, sigma_n=min(sqrt(n)/4,1+dist(n,S)/4) for n>=0, and let epsilon be one fair random sign. On the ray with edges j-1 to j assign tau_j=1+(sigma_j-sigma_(j-1)) epsilon. These weights lie in [3/4,5/4], and their unique minimizing path to n has T_n=n+sigma_n epsilon. Its mean is n, variance is sigma_n^2, and E exp(alpha |T_n-E T_n|/sqrt(Var T_n))=exp(alpha) for every alpha>0. Define a as the upper uniform concentration threshold: inf q for which some alpha>0 makes sup_(n>=1) E exp(alpha |T_n-E T_n|/n^q) finite. Define b as the lower uniform variance threshold: sup q for which some N has inf_(n>N) Var T_n/n^(2q)>0. Then a=1/2 and b=0. The weights share epsilon and are nonstationary; this is not an iid undirected Z^2 law.',
  ['A ray graph','Dependent nonstationary edge weights driven by a common fair sign','The stated sigma_n sequence'],proof('L8')),
 entry('variance-regularity-matches-fluctuation-exponents','lemma','Normalized concentration plus uniform two-sided variance power regularity matches chi',
  'Let T_v, v in Z^d excluding 0, have finite means and 0<sigma(v)^2=Var T_v<infinity; put X_v=T_v-E T_v. Define chi_a as the infimum of q such that some alpha_q>0 gives sup_v E exp(alpha_q |X_v|/|v|^q)<infinity, and chi_b as the supremum of q such that some R gives inf_(|v|>R) Var T_v/|v|^(2q)>0. Suppose some alpha>0,K<infinity give sup_v E exp(alpha |X_v|/sigma(v))<=K. Suppose also that there is chi>=0 such that for every eta>0 there are c_eta,C_eta,R_eta>0 with c_eta |v|^(chi-eta)<=sigma(v)<=C_eta |v|^(chi+eta) for ALL |v|>=R_eta. Then chi_a=chi_b=chi. This is a sufficient criterion, not evidence that the uniform variance regularity or normalized concentration has been proved for iid Uniform[1,2] FPP. It addresses fluctuation matching only, not wandering matching.',
  ['Finite positive variance at every nonzero lattice displacement','The stated uniform normalized exponential-moment bound','The stated two-sided variance power envelope for every positive exponent slack and every sufficiently large displacement'],proof('L9'))
]
relations=[
 {'from_key':'bounded-ray-oscillating-variance','to_key':'variance-tightness-matching-shortcut','kind':'refutes','rationale':'The positive bounded dependent ray metric has exact normalized tight concentration and linear means, but its upper/lower thresholds are 1/2 and 0.'},
 {'from_key':'variance-regularity-matches-fluctuation-exponents','to_existing_logical':'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation','kind':'semantic_association','rationale':'An explicit sufficient bridge for the fluctuation-matching input in P0110; its variance regularity and normalized concentration have not been established for the concrete iid law, and wandering matching is still missing.'}
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w381','bundle_slug':'p0110-variance-regularity-20261010-002','entries':entries,'relations':relations}
keys={e['key'] for e in entries}
for e in entries:
    assert e['source']['license'].startswith('owner-own-work')
    assert bool(e['proof_text']) if e['kind']=='lemma' else e['proof_text'] is None
for r in relations:
    assert r['from_key'] in keys
    if 'to_key' in r:assert r['to_key'] in keys
(root/'drafts'/'bundle_002.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
ids={c['claim_id'] for c in claims}
with (root/'CLAIMS.jsonl').open('a',encoding='utf-8',newline='\n') as out:
    for ident,e in (('w381-L8',entries[1]),('w381-L9',entries[2])):
        if ident in ids:continue
        out.write(json.dumps({'claim_id':ident,'target':'P0110','exact_statement':e['statement'],'assumptions':e['assumptions'],
         'source':e['source'],'proof_or_counterexample':e['proof_text'],'independent_reviewer':'w383 (follow-up pending)',
         'remaining_gap':'The countermetric is dependent/nonstationary. The uniform variance power regularity and normalized concentration are not proved for iid Uniform[1,2]; wandering matching also remains open in this attempt.',
         'status':'proved special case','audit_status':'not independently checked','novelty_status':'no novelty claim','numerical_or_formal_check':'none; exact written auxiliary proof'},ensure_ascii=False)+'\n')
target=next(c for c in json.loads((root/'brain_cards.json').read_text(encoding='utf-8')) if c['metadata'].get('bundle_entry_key')=='op-p0110')
by_key={e['key']:e for e in entries}
support=[{**r,'from_statement_quote':by_key[r['from_key']]['statement'],'to_statement_quote':by_key[r['to_key']]['statement'] if 'to_key' in r else target['claim']['statement'],'review_status':'draft; w383 independent review pending'} for r in relations]
(root/'EDGE_SUPPORT_followup.jsonl').write_text(''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in support),encoding='utf-8')
validation={'entries':3,'relations':2,'both_edge_ends_quoted':True,'license_check':True,'all_lemma_proofs_present':True,'depends_on_acyclic':True,'independent_math_audit':False,'numerical_or_formal_check':False,'failures':0}
(root/'followup_validation_receipt.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
print(json.dumps({'claim_rows':len((root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()),'followup':validation,'submitted':False}))
