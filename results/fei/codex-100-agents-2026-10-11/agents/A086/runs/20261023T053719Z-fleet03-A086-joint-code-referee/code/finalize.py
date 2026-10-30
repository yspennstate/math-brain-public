from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(c):return hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
def source(agent,run):return B/'agents'/agent/'runs'/run
v2=source('A011','20261023T000841Z-fleet03-A011-representation-existence')
v3=source('A011','20261023T045622Z-fleet03-A011-representation-existence')
obs=source('A095','20261023T044042Z-fleet03-A095-restricted-result-extraction')
env=source('A011','20261014T074949Z-fleet05-A011-representation-existence')
pad=source('A011','20261021T182829Z-fleet03-A011-representation-existence')
third=source('A094','20261023T035625Z-fleet03-A094-proof-chain-challenger')
def finalize():
 results=[read(R/'out/PILOT.json')]+[read(R/f'out/BATCH_{j}.json') for j in range(4)]
 assert all(x['status']=='PASS' for x in results)
 histories=sum(x['histories'] for x in results);checks=sum(x['assertions'] for x in results)
 assert histories==6216
 two=read(R/'out/TWO_RESULTS.json');assert two['status']=='PASS' and len(two['fixtures'])==6
 # Independent affine-polynomial certificate, coefficients [constant, C0].
 K=(F(15),F(4));target=(F(15,8),F(1));old=(F(1),F(1))
 def sub(x,y):return tuple(a-b for a,b in zip(x,y))
 def mul(c,x):return tuple(c*a for a in x)
 coefficients={
 'root_and_final':sub(sub(K,(F(0),F(2))),mul(F(1,8),(F(30),F(4)))),
 'padding':sub(sub(mul(F(7,8),K),(F(0),F(3,2))),(F(41,4),F(0))),
 'intermediate_source':sub(sub(mul(F(7,8),K),(F(0),F(5,2))),(F(45,4),F(0)))}
 assert coefficients=={'root_and_final':(F(45,4),F(3,2)),'padding':(F(23,8),F(2)),'intermediate_source':target}
 assert all(all(v>=0 for v in sub(row,target)) for row in coefficients.values())
 assert sub(target,old)==(F(7,8),F(0))
 dump(R/'out/ALLOWANCE_CERTIFICATE.json',{'status':'PASS','arithmetic':'Exact Fraction affine coefficients, ordered [constant,C0]','coefficients':{k:list(map(str,v)) for k,v in coefficients.items()},'uniform_before_booking':list(map(str,target)),'booking':list(map(str,old)),'uniform_after_booking':['7/8','0'],'formal_proof':'Analytic with rational coefficient certificate; no Lean compiler invoked'})
 claims=[];hash_conventions=[]
 for src in (v2,v3,obs):
  cc=read(src/'CLAIMS.json')
  for c in cc:
   candidates={'compact_sorted_statement_and_hypotheses':canonical(c),'utf8_exact_statement_only':hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()}
   matches=[k for k,v in candidates.items() if v==c['statement_sha256']]
   assert len(matches)==1,(c['claim_id'],'unverified source statement hash')
   hash_conventions.append({'claim_id':c['claim_id'],'version':c['version'],'declared_sha256':c['statement_sha256'],'verified_convention':matches[0]})
   c['review_records'].append({'reviewer':'A086/fleet03','verdict':'HOLDS_AT_FULL_NAMED_SCOPE','source':str(R/'RECONSTRUCTION.md'),'validation':str(R/'out/VALIDATION_TOTALS.json'),'independence':'Independent analytic disintegration and leaf-liability proof; direct-character source census; integer butterfly two-edit stress fixtures. No author checker imported. Own previously audited rational-log helper hash pinned.','substantive_repair_supplied':False,'scope':'The exact statement only; finite census does not prove universal FEI. No acceptance of unrestricted iteration, free canonical conversion or incompatible history handoff.'})
   c['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE';claims.append(c)
 statement='For every nonconstant Boolean source g with finite source subprobability R and c=CE(P_g,R)<=C0 I_g,C0>=0, retain exactly the prescribed references, original K=4C0+15 and padding-then-source policy of A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@2, but assume b>=2 padding bits and r>=1 fresh controls. At the root, every nonempty padding frontier and every active source frontier including final collapse, the full signed history bill L obeys K I(F)-L>=(C0+15/8)I_g. Consequently ANY external previously booked U in[0,(C0+1)I_g] is retained at ALL these frontiers with remaining quota at least7I_g/8>0, without a renewed source bank. This nonvanishing allowance is not restricted by K(C+J). All original subprobability masses, physical reaches and full complementary terminal CE/KL remain. No compatibility between A095 narrow-first canonical history and this prescribed floor/padding-first history is asserted; positive-part histories and arbitrary iteration/full FEI remain unproved.'
 hyp=['Uniform finite Boolean cubes; ideal bits and physical influence; original source nonconstant','At least TWO padding bits and one fresh point control','Exactly A011 v2 source reference inheritance and prescribed models; original C0 and K retained','External booking retains full amount U; all signed old reset charges and complete terminals retained','Initial influence-paid source reference remains a supplied hypothesis; no arbitrary unrelated off-path reset or free normalization']
 c={'claim_id':'A086-NONVANISHING-ALL-FRONTIER-OLD-BOOKING-ALLOWANCE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':'','contributors':['A086/fleet03'],'proof_source':{'derivation':str(R/'NONVANISHING_ALLOWANCE.md'),'rational_coefficient_certificate':str(R/'out/ALLOWANCE_CERTIFICATE.json')},'proof_dependencies':[{'claim_id':'A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK','version':2,'statement_sha256':read(v2/'CLAIMS.json')[0]['statement_sha256'],'scope':'Quantitative source-prefix bill factor2(1+w), padding bound and root/final bills; independently reconstructed here without repair'}],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_COEFFICIENT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':'Within the stated bound none; actual reference/policy-compatible handoff of an inherited nonvanishing conversion and arbitrary fixed-rate iteration remain unproved.','next_consumers':['A011','A094','A095','A096','A097','B20']};c['statement_sha256']=canonical(c);claims.append(c)
 protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
 fields=protocol['required_per_run']['claim_fields'];assert all(set(c)==set(fields) for c in claims)
 dump(R/'CLAIMS.json',claims)
 dump(R/'out/HASH_CONVENTIONS.json',{'status':'PASS','claims':hash_conventions,'initial_finalizer_error':'Our first validator incorrectly required A095 compact statement+hypotheses convention for A011; A011 authors explicitly hash UTF8 exact_statement alone. Corrected without changing any source statement/hash. No mathematical failure.'})
 receipts=[]
 for folder,names in [(v2,['DERIVATION.md','CLAIMS.json']),(v3,['DERIVATION.md','CLAIMS.json']),(obs,['DERIVATION.md','CLAIMS.json']),(env,['GENERAL_ENVELOPE.md','CLAIMS.json']),(pad,['DERIVATION.md']),(third,['RECONSTRUCTION.md'])]:
  for name in names:
   p=folder/name;receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':'Proof text or claim metadata used as located in RECONSTRUCTION.md; source checker code NOT used'})
 dump(R/'out/SOURCE_RECEIPTS.json',receipts)
 dump(R/'out/VALIDATION_TOTALS.json',{'status':'PASS','completed_source_histories':histories,'source_assertions':checks,'two_edit_fixtures':len(two['fixtures']),'two_edit_assertions':two['assertions'],'completed_assertions':checks+two['assertions'],'pilot_counts_in_source_total':'included once; disjoint a1,2 vs a3 batches','two_edit_pilot_counts':'excluded from total','interrupted_counts':'excluded; original FAILURE.json retained','finite_to_universal':'Separate analytic reconstructions; no finite extrapolation','memory':'Estimated90-100MB; peak not measured; no >300MB job or formal compiler launched'})
 gap='C024-HISTORY-TRANSFER-SAME-ORIGINAL-SOURCE-BANK'
 progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B18','packet_id':'A086','gap_id':gap,'attempt_id':'A086-stage19-arbitrary-core-two-edit-independent-audit','method':'Independent complete-reference reconstruction; exact Fraction/direct character census, separate integer-transform two-edit stress reconstruction, affine rational certificate','mathematical_delta':'A011 source-prefix v2 and two-edit v3 independently HOLD at named scope; A095 nonvanishing-booking obstruction and A094 positive third-reset sign HOLD. NEW b>=2 all-frontier external allowance U<=(C0+1)Ig leaves>=7Ig/8 from SAME original quota.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_REVIEWS_HOLD_NEW_ALLOWANCE_PENDING_EXTERNAL_REVIEW_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':x['claim_id'],'version':x['version'],'statement_sha256':x['statement_sha256']} for x in claims[:-1]],'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':x['version'],'change':'independent scoped review added' if x is not c else 'new analytic allowance; external review pending'} for x in claims],'source_artifacts':receipts,'next_consumers':['A011','A094','A095','A096','A097','B20'],'next_action':'A011/A094 independently verify new nonvanishing allowance; prescribe ONE actual reference-and-policy-compatible handoff of a genuine inherited nonempty-profile conversion with full old debits and both terminals retained, or aggregate further interacting edits at FIXED original rate/padding.','stagnant_substantive_attempts':0,'blockers':['Universal influence-priced initial reference supplier and arbitrary fixed-rate iteration remain OPEN','A095 canonical/narrow-first model is not identified with A011 floor/padding-first model; larger numerical booking cap alone does not establish handoff','Owner-model and state-of-mind notes stale/unverified; excluded from mathematics','Local persistence only; supervisor mirror/adoption not verified'],'packet_ids':['A086']}
 pfields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']];assert set(progress)==set(pfields)
 dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
 report=f'''# A086: arbitrary-core same-bank two-edit audit and nonvanishing old-booking allowance

## exact target, quantifiers, hypotheses and units

Stage19, A086/B18 joint-code referee. Independently audit A011 source-prefix v2 and its new two-edit v3 for arbitrary nonconstant Boolean source, supplied finite-cost subprobability reference, original C0 and SAME K=4C0+15. v2 requires b,r>=1; v3 additionally b>=6 and retains first controls unqueried. Ideal base2 complete-reference costs; integer prefix rounding is separate. No literal new binary encoder/decoder is claimed. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD.md relevant A001-A015/B18-B20 statuses, B18 STREAM_NOTES v2 and own incoming STATUS consumed; execution protocol2026-10-11-execution-v2 read. A011 v2 DERIVATION sections1 through final/source collapse; v3 DERIVATION sections1-5; original GENERAL_ENVELOPE.md; original padding-prefix DERIVATION; A095 current DERIVATION sections1-5; A094 current RECONSTRUCTION section5 and full preceding chain read. Exact paths/hashes in out/SOURCE_RECEIPTS.json. Author checkers were not imported or used. Own prior rational-log helper pinned at48cd9de1ec443e89be969dd3eac40569c413ddbfafaa9df70e9db1ef238907bc.

## complete derivation or exact first unsupported line

RECONSTRUCTION.md gives independent complete derivations. Verdicts HOLDS at EXACT named scope for A011 v2/v3, A095 booking obstruction and A094 positive canonical-reset witness. Source inheritance retains mass s and factors Z/s, with positive Z0+Z1=2s and complete divergence contraction. Source histories include both terminal bills, true-zero reference mass and zero-dimensional -log(s). Two-edit proof uses distinct-leaf divergence partition and the actual F1 sign at the second point. Previous L1 remains charged through actual operation difference L2-L1; no renewed C0 or KL-only description of a changed target.

NEW NONVANISHING_ALLOWANCE.md proves that b>=2 admits external U<=(C0+1)Ig at ALL original frontiers, leaving>=7Ig/8. Before U, root/final residual >=(3C0/2+45/4)Ig, padding >=(2C0+23/8)Ig, source >=(C0+15/8)Ig, plus retained nonnegative creation terms. Keep factor2(1+w) until after w<=1/4; replacing it by3 too early hides this margin. New claim is author-proved with exact rational coefficient certificate; external independent review remains pending. This is an extension, not a repair of any reviewed version.

First unsupported universal line: an actual compatible handoff of arbitrary inherited nonempty-profile conversion, or arbitrary interacting edits at fixed source/rate/padding. A095 uses a different root and narrow-first policy; the larger numerical allowance does not identify those models. Supplied initial influence-paid source reference also remains a hypothesis. Canonical conversions can be positive; no free conversion or universal FEI follows.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs FROZEN_SPEC.json, BATCH_SPEC.json, TWO_EDIT_SPEC.json and ALLOWANCE_SPEC.json precede their computations. Source census: every nonconstant labelled Boolean table on a1,2,3; b1,r1; s1 or1/2, eta0 or1/4, EVERY source-coordinate permutation, fixed edited point0. Completed {histories} disjoint histories, {checks} exact assertions PASS. Pilot120 histories is included once; interrupted initial whole-census counts excluded. Four a3 batches use unchanged truth-table domain; each finishes under60seconds. Actual runtime receipts are in out/PILOT.json and BATCH_0 through3.json.

Commands: python -B -X utf8 code/check.py --pilot; code/check.py --batch j for j0..3; code/two_edit.py --pilot; code/two_edit.py. Source checker uses direct character sums, literal physical edges, Fraction references and rational atanh/outward96-bit log bounds. The separate two-edit checker uses an integer butterfly transform, literal edges, grouped rigorous logs and six fixed fixtures: a1 dictator or a2 AND, b6,r1=r2=1, second point zero/padding-off/source-off, specified normalized or missing-mass source references. All old frontiers checked: {two['assertions']} assertions PASS. Pilot checks excluded from final totals. Exact integer witness N>16D,N^2<512D^2 proves1/128<e3<9/1024; exact rational4039/32768>1/10>279/16384 verifies obstruction separation. New allowance has an affine-coefficient certificate valid for every real C0>=0, not sampled C0. No formal compiler or >300MB job launched; observed peak memory unmeasured.

Original monolithic source census hit its frozen58-second guard, exit1, without a mathematical assertion failure; FAILURE.json preserved as INCOMPLETE. Completed bounded batches replace no domain or arithmetic. No all-policy finite census is claimed for arbitrary sources; adaptive/all-dimensional conclusions rest on the analytic proof. No measurements from authors counted as our independent validation.

## proof dependencies and changed downstream conclusions

Exact version chain v3->v2->v1/general-envelope is acyclic. Source statements/hypotheses remain byte-identical in content; declared statement hashes verified under the source conventions recorded in out/HASH_CONVENTIONS.json. Our first finalizer incorrectly imposed the compact statement+hypotheses convention on A011, which explicitly hashes the UTF8 statement alone; this validator error was corrected without source changes. Our added reviews supply no substantive repair. New allowance depends on reconstructed v2 quantitative bill; A086 authored it and does not self-accept it as independently reviewed. A095 obstruction does not refute A011, and the new allowance does not establish a cross-policy handoff. Full FEI remains OPEN.

## one next mathematical action and independent reviewer

A011/A094: reconstruct NONVANISHING_ALLOWANCE.md, then price one genuine reference-and-policy-compatible inherited profile conversion using the SAME diminished original account and both full terminals. A095 supplies its actual canonical narrow-first fixture; require an explicit conversion rather than renaming its bank. For many-edit continuation retain fixed padding and original C0, not increasingly fresh source certificates.

## actual persistence receipts or precise save blocker

All four protocol files, reconstruction, new proof, frozen specs, code and exact outputs saved only inside A086. STATUS.md two-line state and NEXT, WORKLOG.md and LEARNED.md updated. Schema and per-file SHA256 reread checks in out/SCHEMA_VALIDATION.json and PERSISTENCE_RECEIPTS.json. No git, external publication, mail, shared registry update or research brain write performed. Supervisor mirror/adoption unverified. Wake reports owner-model92.1h/state-of-mind76.7h stale: brain self-care degraded/unverified; affected notes excluded. No source mathematical claim depends on those notes.

Universal bridge: C024 history transfer advances by independent arbitrary-core TWO-edit reconstruction at SAME original rate and a new nonvanishing all-frontier old-booking allowance for b>=2; finite evidence is {histories} exact source histories and six two-edit fixtures, not a universal proof. C019/C020 still need a universal initial paid reference and bounded conversion liabilities for arbitrarily many interacting edits. NEXT is an actual compatible profile-conversion handoff against this larger original reserve, because it tests the remaining universal interface rather than adding another isolated Boolean family. Full FEI remains OPEN.
'''
 (R/'REPORT.md').write_text(report,encoding='utf-8')
 (A/'STATUS.md').write_text('STATE: Stage19 COMPLETE_LOCAL: A011 arbitrary-core source-prefix v2/TWO-edit v3 scoped HOLDS; NEW b>=2 nonvanishing U<=(C0+1)Ig leaves7Ig/8; external review pending; FEI OPEN.\nNEXT: A011/A094 review allowance; price ONE actual compatible inherited nonempty-profile handoff with original C0, old debits/both full terminals; arbitrary fixed-rate edit aggregation remains open.\n',encoding='utf-8')
 date=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n[{date}] Stage19: independent A011 v2/v3 full-scope reconstructions; A095 rare-cap and A094 positive third-reset scope HOLD. NEW b>=2 all-frontier old-booking allowance U<=(C0+1)Ig leaves7Ig/8; pending independent review. Completed{histories} source histories/{checks} assertions, six two-edit fixtures/{two["assertions"]} assertions. Initial whole-census guard timeout preserved, excluded. Same finite domain completed in four bounded batches. All artifacts local; FEI OPEN.\n')
 with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage19 durable fact: In A011 v2 SAME prescribed history, b>=2 lets w<=1/4,E<=Ig/8. Keeping quantitative source coefficient2(1+w)<=5/2 yields before-old-booking source reserve>=(C0+15/8)Ig; root/final and padding bounds exceed it. Therefore external U<=(C0+1)Ig leaves>=7Ig/8 at EVERY old frontier, independent of rare edit mass. This does not identify canonical/narrow-first references with the floor/padding-first model. Two-edit v3 distinct exceptional leaves share ONE contracted D budget; construction debit changes target and is not a KL-only physical reset. Universal initial supplier/arbitrary fixed-rate iteration remain unpaid.\n')
 assert read(R/'PACKET_DELTA.json')==read(R/'PROGRESS.json')
 assert all(len(p.read_bytes())<20_000_000 for p in R.rglob('*') if p.is_file())
 dump(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claims':len(claims),'claim_fields_exact':True,'progress_fields_exact':True,'delta_identical':True,'full_fei':'OPEN'})
 files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[A/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
 records=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
 dump(R/'out/PERSISTENCE_RECEIPTS.json',{'files':records,'mirror_verified':False})
 assert all(sha(Path(x['path']))==x['sha256'] for x in records)
 print(json.dumps({'status':'COMPLETE_LOCAL','source_histories':histories,'source_checks':checks,'two_edit_checks':two['assertions'],'new_allowance':'7Ig/8 after U<=(C0+1)Ig, b>=2','claims':len(claims),'artifacts_verified':len(records),'full_fei':'OPEN'}))
if __name__=='__main__':finalize()
