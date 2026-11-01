from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8'));stamp=datetime.now(timezone.utc).isoformat()
def save(name,x):(R/name).write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def statement_hash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
src=ROOT/'agents/A038/runs/20261014T022516Z-fleet05-A038-occupancy-term-audit'
original=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert statement_hash(original)==original['statement_sha256']
reviewed=copy.deepcopy(original)
reviewed['review_records'].append({'reviewer':'A039','verdict':'ACCEPT_AT_STATED_SCOPE','reviewed_at':stamp,'source':str(R/'REVIEW_A038.md'),
'method':'Independent arbitrary-v analytic reconstruction; iterative Walsh and physical edges; source integer powers and canonical excluded-event bound rechecked; moment-only projection scalar validation; no author checker replay','source_statement_sha256':original['statement_sha256'],'substantive_source_repair':False})
reviewed['status']='INDEPENDENTLY_REVIEWED_LOCALLY_BY_A039'
statement=('At the actual A038 exposed priority fixture (u=(-1,-1,-1,+1), essential u0=0 exposure, v=(-1,+1,+1,+1), opposite shared-x events, next private a query), let M be the original completed canonical nonempty occupancy projection, A=D(P||M), E the queried-spectral-bit conditional KL released by erasure, O_occ the outcome KL under the same signed child kernel, and Q_y the inherited normalized Bayes child references. Then A=E+O_occ+average D(P_child||Q_y), E in [0.239583496125,0.239583496126], E-rho>1/40 for the original residual-product reset rho=2+(21/32)log2(7)-(25/16)log2(5), and A-O_occ-average TC(child)>1/25 for the actual occupancy-Bayes-to-child-product conversion. These are alternative one-use withdrawals; all sixteen adaptive depth-two stopping policies retain their original inherited reference KL and actual terminal spectral entropy/H-U-R. Conversely, replacing v by the actual n-bit point defect v_n=1-2*1_zero, with the same essential ancestor exposure and a query, gives for every n>=16, epsilon=2^-n: 0<E_n<=3 epsilon, rho_n>=((n-2)/2)epsilon, rho_n/E_n>=(n-2)/6, and A_n-O_occ,n-average TC(child)<=-((n-6)/2)epsilon. Thus no absolute multiplicative release-only reset price exists, and the actual canonical occupancy-to-child-product conversion needs a separate positive debit on this family. Both child spectra and terminal debts remain actual; this is not an FEI counterexample or an influence-priced impossibility.')
hyp=['Finite uniform independent physical Boolean signs; entropy and KL in bits; actual coherent children from signed Fourier amplitudes',
'Completed canonical occupancy M(empty)=P(empty), M(S)=P(nonempty)Q_occ(S); Q_occ maximizes entropy on nonempty subsets with the actual matched conditional marginals',
'Common physical child kernel applied identically to residual spectrum and inherited reference, with fair fallback on zero true fibers; only irrelevant coordinates dropped',
'The source priority selects u when x=0,a=1, v when x=1,b=1, otherwise +1; u0=0 is an essential original data exposure; the remaining u=-1 and true v core are retained',
'E=E_residual D_2(P(S_a|residual)||M(S_a|residual)); rho denotes original residual-product reset, sigma_occ actual conversion from inherited occupancy-Bayes child to child product; the two withdrawals are not summed',
'Fixture finite continuations query a then one actual remaining coordinate separately in each branch; rare all-n statement uses v_n exactly, not an arbitrary biased surrogate']
new={'claim_id':'A039-OWNED-OCCUPANCY-ERASURE-TRANSFER','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':'',
'contributors':['A039'],'proof_source':{'run_id':R.name,'files':['PROOF.md','RARE_OBSTRUCTION.md','REVIEW_A038.md','code/transport.py','code/scalar_check.py','code/rare_check.py','out/TRANSPORT.json','out/SCALAR_CERTIFICATE.json','out/RARE_PROJECTION_CERTIFICATE.json']},
'proof_dependencies':[{'claim_id':original['claim_id'],'version':1,'status':'INDEPENDENTLY_REVIEWED_LOCALLY_BY_A039','use':'Actual fixture, reset convention and canonical occupancy reference; independently reconstructed'},
{'claim_id':'A039-COHERENT-PROJECTION-TRANSFER','version':1,'status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW','use':'Compensated physical TC identity and occupancy Pythagorean identity; needed algebra re-derived in proofs'}],
'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
'refutes':[{'statement':'There exists finite C with rho<=C times the canonical occupancy KL released by erasing the physical queried spectral bit at every exposed priority controller query','version':'A039 release-payment continuation tested in this stage; not attributed to an upstream theorem','witness':'v_n point defect, n>=16, same essential u exposure and private a query, rho/E>=(n-2)/6'},
{'statement':'Original root occupancy KL always pays its Bayes outcome mismatch plus the mean actual child product KL with no extra debit','version':'A039 fixture conversion extended without scope','witness':'Same actual family; deficit >=((n-6)/2)2^-n'}],
'first_unproved_line':None,'next_consumers':['A038','A064','A088','A091','A092','A094','B20']}
new['statement_sha256']=statement_hash(new)
save('CLAIMS.json',[reviewed,new])
next_action='Price the actual positive conversion debit sigma_occ-E from one unused signed child/control slack at a selected mixed controller query, retaining inherited Bayes references until paid and both terminal H-U-R/core obligations; stress-test rare biased v_n and arbitrary remaining cores.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B08','packet_id':'A039','gap_id':'G-R-MISMATCH','attempt_id':'A039-occupancy-release-transfer-1',
'method':'Consume and independently review A038 source; exact canonical root/fiber transport; all sixteen two-level continuations; independent moment-only scalar certificate; analytic all-dimensional rare-family release and projection obstruction',
'mathematical_delta':{'review':original['claim_id']+'@1 ACCEPT_AT_STATED_SCOPE locally',
'fixture':'Released occupancy KL pays original product reset once with margin>1/40; actual occupancy-to-product conversion margin>1/25; alternatives, not simultaneous credits; all16 actual stopping continuations retained',
'all_n_obstruction':'For every n>=16 actual rare point-defect remaining core: E<=3*2^-n, rho>=((n-2)/2)*2^-n, rho/E>=(n-2)/6; A-O_occ-E TC_child<=-((n-6)/2)*2^-n',
'universal_FEI':'OPEN; no constant improvement; actual query influence1/2, no influence-priced impossibility claimed',
'first_unsupported_universal_line':'Pay extra actual reference-conversion debit plus mixed controller decrement and complete terminal/core entropy using one compatible unused physical slack'},
'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'SOURCE_REVIEW_ACCEPTED_LOCALLY; FIXTURE_PAYMENT_AND_ALL_N_RELEASE_OBSTRUCTION_PROVED; NEW_CLAIM_EXTERNAL_REVIEW_PENDING; FEI_OPEN',
'claim_versions_used':new['proof_dependencies'],'claims_created_or_changed':[{'claim_id':reviewed['claim_id'],'version':1,'change':'Source statement/contributors/hash unchanged; independent review record appended'},
{'claim_id':new['claim_id'],'version':1,'change':'Scoped existing reset interface closed at fixture, fixed-factor release continuation refuted by actual all-n Boolean family'}],
'source_artifacts':['PROOF.md','RARE_OBSTRUCTION.md','REVIEW_A038.md','out/FROZEN_SPEC.json','out/TRANSPORT_SPEC.json','out/SCALAR_CHECK_SPEC.json','out/RARE_SPEC.json','out/RARE_PROJECTION_SPEC.json','out/VALIDATION_REPAIR.json','out/TRANSPORT.json','out/SCALAR_CERTIFICATE.json','out/RARE_PROJECTION_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':['A038','A064','A088','A091','A092','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
'blockers':['Additional signed child/control slack and arbitrary terminal payment remain mathematical gaps','New claim independent external review, supervisor copies, index/mirror adoption and downstream use unobserved'],'packet_ids':['A039']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(R/'out/ENTRY_STATUS.md').write_bytes((A/'STATUS.md').read_bytes())
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B08/STREAM_NOTES.md',src/'REPORT.md',src/'PROOF.md',src/'CLAIMS.json',src/'code/fixture.py',
ROOT/'agents/A091/runs/20261014T013816Z-fleet05-A091-composition-referee/REPORT.md',
ROOT/'agents/A047/runs/20261014T015314Z-fleet05-A047-boundary-search/REPORT.md',
A/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/DERIVATION.md',
A/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/code/baseline_check.py',R/'out/ENTRY_STATUS.md']
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'scope':'Actual source read/use; A091 and A047 reports context only; earlier campaign/paper reading not represented as new reading'} for p in sources])
(A/'STATUS.md').write_text('STATE: A039 stage4 saved: A038 reset/occupancy claim independently HOLDS; source bank pays fixture once (>1/40 release margin, >1/25 actual conversion margin); all-n rare-core release-only and free projection conversion refuted; FEI OPEN, new review pending.\nNEXT: Price sigma_occ-E from one unused signed child/control slack at a selected mixed query; keep inherited Bayes references and both terminal/core debts; A038/A064/A091 consume, A088/A094 review.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | {R.name}: Read updated BOARD/B08/STATUS, consumed new A038 exposed-reset certificate instead of duplicating it. Independently ACCEPTED source at full stated scope, no repair. Actual canonical occupancy transport PASS140 checks/16 depth-two policies/0.36211s; independent scalar PASS6/0.00649s. Fixture E-rho>1/40 and actual projection conversion margin>1/25, alternative single-use withdrawals. Initial main stopped at exact-zero profile interval; fixed by formal-log cancellation, no domain change/count inflated. New actual v_n family proved alln>=16 E<=3eps, rho/E>=(n-2)/6 and actual conversion deficit>=((n-6)/2)eps. Final frozen n16,24,32,64 certificate PASS32/0.11634s. No universal FEI constant or terminal payment claimed. Four protocol/rolling files saved; external new-claim review and mirrors pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nSource-owned occupancy root bank A=D(P||M) transports exactly as A=E_erasure+O_outcome+mean inherited child KL under the same physical coherent kernel; retain normalized child references, do not create another root bank. A038 essential-exposure fixture releases0.239583496125bits, enough for product reset0.214314019339 with margin>1/40; its actual occupancy-Bayes-to-product reset is0.198062421435 and leaves margin>1/25. These are alternative withdrawals. Original terminal H-U-R/entropy remain unpaid. This continuation is not uniform: actual remaining v_n=point defect gives eps=2^-n, for alln>=16 E<=3eps and rho>=((n-2)/2)eps, so rho/E>=(n-2)/6. Actual root occupancy-to-child-product margin<=-((n-6)/2)eps by compensated TC, Delta>=0 and B_a>=m^2. Root credit, released credit and inherited child debt are distinct. Keep inherited Bayes references until conversion is paid by one unused physical/core slack. Exact-zero H-U-R must use formal cancellation before testing outward interval positivity. A038 source claim@1 independently accepted locally with original hash/contributors unchanged.\n')
claim_keys=set(protocol['required_per_run']['claim_fields']);progress_keys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
readclaims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in readclaims:
    assert set(c)==claim_keys and statement_hash(c)==c['statement_sha256']
assert readclaims[0]['exact_statement']==original['exact_statement'] and readclaims[0]['contributors']==original['contributors']
readprogress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'));assert set(readprogress)==progress_keys
assert readprogress==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((A/'STATUS.md').read_text().splitlines())==2
report=(R/'REPORT.md').read_text(encoding='utf-8');assert all('# '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
out=json.loads((R/'out/TRANSPORT.json').read_text());assert out['status']=='PASS' and len(out['two_level_stopping_trees'])==16
scalar=json.loads((R/'out/SCALAR_CERTIFICATE.json').read_text());rare=json.loads((R/'out/RARE_PROJECTION_CERTIFICATE.json').read_text())
assert scalar['status']==rare['status']=='PASS' and rare['domain']==[16,24,32,64]
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'];assert all(p.stat().st_size<20_000_000 for p in files)
save('out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_SAVED_CONTENT_CHECK_PASS','saved_at':stamp,'exact_protocol_key_sets':True,'claim_hashes_recomputed':[c['statement_sha256'] for c in readclaims],'reviewed_source_statement_contributors_unchanged':True,'progress_delta_equal':True,'report_fields_and_final_universal_bridge_checked':True,
'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
'rolling_files':[{'path':str(A/name),'bytes':(A/name).stat().st_size,'sha256':sha(A/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],
'unobserved':['External independent review of new A039 claim','supervisor copying','registry adoption','mirror verification','downstream use','public release']})
print(json.dumps({'status':'LOCAL_SAVED_CONTENT_CHECK_PASS','files':len(files),'max_file_bytes':max(p.stat().st_size for p in files),'source_review':'ACCEPT_AT_STATED_SCOPE','new_claim':new['claim_id']}))
