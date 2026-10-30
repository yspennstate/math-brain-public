from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

RUN=Path(__file__).resolve().parents[1]
HOME=RUN.parents[1]
SHARED=HOME.parents[1]
REPORTS=Path('math-open-problems/reports/fei-2026-10-11')
PROTO=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,value):
    (RUN/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

statement=('Version7 preserves the explicit endpoint/envelope conclusions of A030@5/@6 and clarifies their cost scope. '
 'For every finite adaptive uniform physical restriction tree with normalized support-positive current output references, '
 'let d_v be current KL, e_vs inherited-child KL under the actual output phase channel, '
 'L_v=d_v-E_s e_vs>=0 and kappa_v=E_s(d_vs-e_vs). Then '
 'CE_root+sum_v w_v kappa_v=H_root+E_leaf d_leaf+sum_v w_v L_v; '
 'the entropy-path plus full terminal CE functional T is H_root+E_leaf d_leaf. '
 'For every k,L>=1 the actual two-source selector F_k,L of PROOF.md, made from products of k two-bit point defects '
 'and their first-coordinate translates with fresh length-L parity blocks, has H=2k,I=Lk+1/2. '
 'Its block-data-first then selector tree has max current KL1, raw replacement sum k, query-KL sum k+1, '
 'and raw transaction3k+1. Selector-first has raw replacement sum0, query-KL sum1 and transaction2k+1, '
 'with the same singleton physical leaf partition. At every restriction fixing q<=d<L distinct coordinates, '
 'on every assignment, H=2k,I=Lk+1/2-q/2 and all live influences are1/2. '
 'Thus these bounded-depth H/influence statistics do not distinguish the policies; CURRENT KL or the source decomposition does. '
 'A final x-block query has zero entropy drop and one bit of actual query-KL contraction. '
 'No constant depending only on label count2 bounds accumulated query KL. '
 'Earlier tagged-bent >3/16 and >1/4 reserve statements remain for T or an explicitly credited L ledger; '
 'an uncredited raw-transaction interpretation requires separate SAME-owner payment of sum w L. '
 'This is not an FEI disproof or a refutation of the earlier numerical rate4 quota. '
 'Universal arbitrary-core admission and raw query-KL payment remain open.')
claim={
 'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':7,'exact_statement':statement,
 'hypotheses':[
  'Finite uniform cubes, real normalized Walsh coefficients, Boolean actual restrictions, base2 information.',
  'Normalized current references positive on true support; retain reference-only mass, both full children and their own reference branch normalizers.',
  'Raw replacement invoices and query refunds are separate signed entries; no positive clipping, refreshed account or double spending.',
  'Family comparison uses exactly Qinc of the stated two-source representation and the two declared complete query policies.',
  'Local signature assertion fixes distinct coordinates and requires q<=d<L; it concerns H and the entire influence vector, not all possible local statistics.',
  'No statement gives a new influence-priced initial source or raw-transaction bound for arbitrary cores.'
 ],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A030','A094 (prior source-bound ledger objection, not independent acceptance of this extension)'],
 'proof_source':['PROOF.md','code/check.py','out/VALIDATION.json','code/independent.py','out/INDEPENDENT.json','code/signatures.py','out/SIGNATURES.json'],
 'proof_dependencies':['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@5 sections2,4 (reconstructed and extended)','A030-THREE-STATE-BOOLEAN-CUT-RESERVE@6 section3 (scope comparison)','A094 stage21 exact-ledger clause (independently reconstructed formula only)'],
 'review_records':[{'reviewer':'A030','status':'AUTHOR_PROOF_WITH_EXACT_FINITE_VALIDATION_EXTERNAL_REVIEW_PENDING','scope':'Independent direct-Walsh implementation checks raw query losses; not an external review. Scalar Lean attempt held, no compiler process.'}],
 'status':'AUTHOR_PROOF_SCOPED_CORRECTION_EXTERNAL_REVIEW_PENDING',
 'supersedes':['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@6 (raw-payment interpretation only; explicit T/envelope theorems preserved)','A030-THREE-STATE-BOOLEAN-CUT-RESERVE@5 (same scope clarification)'],
 'refutes':['Identification of an endpoint/envelope terminal functional with root CE plus signed raw replacements when accumulated physical-query KL is omitted'],
 'first_unproved_line':'For a REQUIRED compatible stopping policy, pay accumulated actual query KL from the SAME unused original reserve, or explicitly justify its release credit; separately fund arbitrary-core initial source in O(I).',
 'next_consumers':['B06 Claude lead','A028','A029','A087','A094','A011','A086','A096','B20']
}
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':PROTO['revision'],'run_id':RUN.name,'stream':'B06','packet_id':'A030',
 'gap_id':'C019-C024-UNEQUAL-MEAN-STRUCTURAL-CONVERSION',
 'attempt_id':'A030-raw-query-KL-plateau-policy-audit',
 'method':'Consume A094 new accounting objection; exact finite-tree telescoping, actual two-source Boolean pulses, parity-code support injection, direct-Walsh independent reproduction.',
 'mathematical_delta':'Identical all-restriction depth-d H/influence signatures for L>d coexist with raw bills3k+1 versus2k+1 on the same complete leaf partition. Explicit sum queryKL=k+1 versus1 isolates the extra raw-payment term absent from endpoint-only accounting. Earlier terminal bounds preserved.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_VERIFIED',
 'mathematical_status':'AUTHOR_PROOF_SCOPED_ACCOUNTING_CLARIFICATION_AND_POLICY_TEST; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@5','A030-THREE-STATE-BOOLEAN-CUT-RESERVE@6','A094 stage21 exact-ledger clause'],
 'claims_created_or_changed':['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@7'],
 'source_artifacts':['REPORT.md','PROOF.md','code/check.py','code/independent.py','code/signatures.py','out/FROZEN_SPEC.json','out/INDEPENDENT_SPEC.json','out/SIGNATURE_SPEC.json','out/VALIDATION.json','out/INDEPENDENT.json','out/SIGNATURES.json','out/LEAN_RECEIPT.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A028/A029/A087/A094 specify a REQUIRED stopping policy and pay its actual cumulative queryKL from SAME depleted original owner, retaining old debits/full terminals; a new terminal envelope alone cannot close this gap.',
 'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core original source influence price OPEN.','Raw cumulative query-KL payment OPEN beyond explicitly declared credit scope.','External review pending; Lean runtime admission held; supervisor copy unverified.'],
 'packet_ids':['A030']
}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)

sources=[
 (Path('~/AGENTS.md'),'complete rules read; printed output partly truncated'),
 (REPORTS/'EXECUTION_PROTOCOL.json','complete protocol'),
 (REPORTS/'README.md','complete'),(REPORTS/'CURRENT_STATUS.md','complete'),
 (REPORTS/'CLAIM_REGISTRY.json','selected relevant entries'),(REPORTS/'OBSTRUCTION_REGISTRY.json','selected relevant entries'),
 (REPORTS/'PACKET_STATUS.json','A030/B06 navigation'),(REPORTS/'STREAM_NEXT_ACTIONS.json','B06 navigation'),
 (REPORTS/'FEI_100_agent_research_plan.tex','A030/B06 and review locators'),
 (SHARED/'BOARD.md','current board scan including exact A094 issue'),
 (SHARED/'claude/B06/STREAM_NOTES.md','complete'),
 (HOME/'runs/20261023T132050Z-fleet03-A030-restriction-plateau-tests/PROOF.md','complete sections1-6'),
 (HOME/'runs/20261023T132050Z-fleet03-A030-restriction-plateau-tests/CLAIMS.json','claim@6 and @5 scopes'),
 (HOME/'runs/20261023T110419Z-fleet03-A030-restriction-plateau-tests/PROOF.md','complete sections1-6'),
 (SHARED/'agents/A094/runs/20261026T232939Z-fleet04-A094-proof-chain-challenger/REPORT.md','complete scoped objection and validation'),
 (SHARED/'agents/A094/LEARNED.md','last24 lines including exact-ledger clause')
]
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    sources.append((supp/name,'selected relevant extracts; earlier baseline readings inherited'))
sources.append((supp/'sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','sections1-2'))
for name in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    sources.append((SHARED/'context'/name,'theorem/abstract extracts only this stage; not a full new audit'))
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in sources])

stamp=datetime.now(timezone.utc).isoformat()
status=('STATE: A030@7 saved: endpoint bounds preserved; raw bill adds actual queryKL; identical depth-d H/I plateaux hide policy bills3k+1 vs2k+1; exact checks PASS; FEI OPEN.\n'
        'NEXT: A028/A029/A087/A094 pay REQUIRED-policy cumulative queryKL from SAME original unused owner/full old bills; arbitrary-core INITIAL source still unpaid; review@7.\n')
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
entry=f'\n{stamp} Stage {RUN.name}: reconstructed A094 ledger objection and clarified A030@5/@6 endpoint scope. Proved all-k,L raw bill3k+1 versus selector-first2k+1, queryKL k+1 versus1, identical all-restriction depth-d H/I signatures for L>d. Main834 nodes/10890 predicates; independent196/7480; signature964 restrictions PASS. Scalar Lean runtime held, no compiler. Raw arbitrary-policy payment and original arbitrary-core source remain OPEN.\n'
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson=('\n2026-10-27 A030@7: Root CE+sum signed raw replacement invoices equals Hroot+E terminalKL+sum actual queryKL contractions. The endpoint functional subtracts that last term; do not infer uncredited raw payment from its envelope bound. Earlier @5/@6 explicit endpoint theorems remain valid, numerical raw payment unresolved. Two-source PD2/translated-PD2 parity-block family has H2k,I=Lk+1/2, currentKL<=1, but data-first queryKL k+1 and raw bill3k+1; selector-first queryKL1/raw2k+1. Both trees share singleton leaves. For every q<=d<L restriction and assignment H2k,I=Lk+1/2-q/2, all live influences1/2: H/influence local statistics cannot see this policy difference, while CURRENT KL can. Raw bill/I<3, so no rate4 or FEI counterexample. NEXT must fund actual queryKL under a necessary policy from SAME old owner, alongside original arbitrary-core admission.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)

# Exact protocol-key checks; explanatory parentheses in the field catalog are labels only.
pf={x.split(' (')[0] for x in PROTO['required_per_run']['progress_fields']}
assert set(progress)==pf,(set(progress),pf)
assert set(claim)==set(PROTO['required_per_run']['claim_fields'])
assert json.loads((RUN/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((RUN/'PACKET_DELTA.json').read_text(encoding='utf-8'))
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for heading in PROTO['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n')[-2]=='## Universal bridge' or '## Universal bridge\n' in report
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for output,code in [('VALIDATION.json','check.py'),('INDEPENDENT.json','independent.py'),('SIGNATURES.json','signatures.py')]:
    result=json.loads((RUN/'out'/output).read_text(encoding='utf-8'))
    assert result['status']=='PASS' and result['code_sha256']==sha(RUN/'code'/code)
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'status':'PASS','timestamp':stamp,'protocol_keys_verified':True,'claim_statement_sha256':claim['statement_sha256'],
 'files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'rolling':[{'path':str(HOME/name),'sha256':sha(HOME/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],
 'external_copy':'UNVERIFIED','external_review':'PENDING','full_FEI':'OPEN'}
save('out/PERSISTENCE.json',receipt)
assert json.loads((RUN/'out/PERSISTENCE.json').read_text(encoding='utf-8'))['status']=='PASS'
print(json.dumps({'status':'PASS','files':len(files),'claim_version':7,'rolling_status_lines':2,'full_FEI':'OPEN'}))
