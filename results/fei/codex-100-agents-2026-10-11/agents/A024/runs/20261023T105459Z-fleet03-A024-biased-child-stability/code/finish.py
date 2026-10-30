from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1];home=run.parents[1]
old=run.parent/'20261023T032050Z-fleet03-A024-biased-child-stability'
helper=run.parent/'20261022T221625Z-fleet03-A024-biased-child-stability/code/check.py'
root=home.parents[1]
proto=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):
 with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def js(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(read(proto));required=protocol['required_per_run']
outs={name:json.loads(read(run/'out'/name)) for name in ['PILOT.json','VALIDATION.json','ACTIVATION_PILOT.json','ACTIVATION.json','WITNESS.json','OBSTRUCTION.json']}
assert all(v['status']=='PASS' for v in outs.values())
val,act,wit,obs=[outs[n] for n in ['VALIDATION.json','ACTIVATION.json','WITNESS.json','OBSTRUCTION.json']]
assert val['descriptions']==318826 and val['physical_restrictions']==2543504
assert act['ordered_pairs']==64 and act['one_query_prefixes']==272
assert wit['functions']==278 and wit['coordinate_queries']==804 and wit['distinguished_fibers']==3140
assert val['checker_sha256']==sha(run/'code/check_flat.py')
assert val['helper_sha256']==sha(helper)
assert wit['checker_sha256']==sha(run/'code/witness.py')
assert obs['checker_sha256']==sha(run/'code/obstruction.py')
for row in obs['rows']:
 d=Q(row['selector_d']);K=row['K']
 assert Q(row['erasure_lower'])>K*d
 assert Q(row['minimum_fiber_W'])>Q((K-2)**2,4)*d*d
total=sum(x['exact_assertions'] for x in [val,act,wit,obs])
consumers=['A021','A022','A023','A025','A028','A029','A087','A094','B05','B20']
statement=('Retains v3/v4 with their original scopes and extends them: for all real a,b, L(a,b)<=2|ab|, hence the exact scalar binary-activation erasure remainder satisfies R_r<=6r|beta|<=6r Inf_i(w) for every disjoint Boolean pair, including deterministic means. Every quadratic phase edited on an arbitrary affine subspace, its disjoint products, and every fair physical residual thereof admits a complete K4-good physical continuation. OR/AND of any finite number of disjoint such products admits a K10-good continuation after every physical stopping prefix, adding zero K10-bad odd-face debit; earlier debit and both full terminal entropies remain. For every Boolean f, coordinate i and T not containing i, let a=fhat(T), b=fhat(T+i), d=Inf_i(f), W=(1-d-a^2)(d-b^2). Then B_i<=L(a,b)+2sqrt(W)<=2d+2sqrt(W); this gives the exact localized tree liability in DERIVATION(7), whose universal O(I) price remains unproved. No paid reference is reset. Entropy corollaries H<=7I for products and H<=13I for the stated OR/AND class use inherited B05 localization. Arbitrary general-edit residuals, old-prefix payment, general outer gates and full FEI remain open.')
claim={'claim_id':'A024-MIXED-FACE-ORDER-OBSTRUCTION','version':5,'exact_statement':statement,
 'hypotheses':['Entropy in bits; Boolean outputs; disjoint finite physical blocks with uniform untouched coordinates',
 'Scalar L and distinguished-fiber inequalities are universal as quantified; composition remainder is for the specified binary activation, not an arbitrary outer gate',
 'Hereditary K4 class is a degree-at-most-two F2 phase with an empty or arbitrary affine-flat edit, then products on disjoint blocks',
 'Physical adaptive prefix fixes only revealed input bits; selected continuation, not every coordinate order',
 'Old bank, prefix debits, both full actual terminal functions and all prior reference liabilities retained; no changed-tree Phi transfer',
 'H<=7I and H<=13I use B05 localized entropy reduction with c_JS=2/ln2'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A024'],
 'proof_source':str(run/'DERIVATION.md'),
 'proof_dependencies':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3 (exact scalar transport identity, reconstructed here)',
 'A024-MIXED-FACE-ORDER-OBSTRUCTION@4 (hereditary point-edit baseline and no changed-tree potential transfer)',
 'B05-ODDFACE-LOCALIZED-REDUCTION@1 (entropy/tree corollaries only; inherited acceptance status)'],
 'review_records':[{'kind':'author exact exhaustive descriptions','status':'PASS','source':'out/VALIDATION.json','scope':f"318826 descriptions;2543504 physical restrictions;{val['exact_assertions']} exact assertions; finite D<=4"},
 {'kind':'author direct physical activation replay','status':'PASS','source':'out/ACTIVATION.json','scope':f"64 pairs;272 prefixes;{act['exact_assertions']} assertions"},
 {'kind':'author independent character-sum fiber lane','status':'PASS','source':'out/WITNESS.json','scope':f"All278 Boolean functions D<=3;3140 distinguished fibers;{wit['exact_assertions']} assertions; no square-root approximation"},
 {'kind':'author fixed rare-selector attempted break','status':'PASS','source':'out/OBSTRUCTION.json','scope':'Actual K4/K10 bad selectors retained; excludes an every-query reading'},
 {'kind':'formal certification','status':'NOT_CLAIMED','scope':'No compiler run; written all-dimensional author proof with exact finite verification'},
 {'kind':'independent review','status':'PENDING','reviewers':['A087','A094']}],
 'status':'AUTHOR_PROOF_REVIEW_PENDING','supersedes':['A024-MIXED-FACE-ORDER-OBSTRUCTION@4'],
 'refutes':[],
 'first_unproved_line':'No universal choice of physical tree and distinguished fibers has been shown to price the localized overlap liability in DERIVATION(7) by O(I), with old-prefix debits and both stopping terminals retained.',
 'next_consumers':consumers}
assert set(claim)==set(required['claim_fields']);js(run/'CLAIMS.json',[claim])
next_action='Price one genuinely mixed DATA query for a non-flat union of two affine edits using the exact distinguished-fiber overlap liability in (7), from the SAME unused original credit with old debit and both full terminals; test cross-term interference before any union-of-flats induction. A087/A094 reconstruct v5.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B05','packet_id':'A024',
 'gap_id':'G-R-SELECT','attempt_id':'A024-stage19-affine-flat-and-universal-fiber-credit',
 'method':'Exact calculus scalar bound; codimension-two absorption; annihilator spectrum and sparse quadratic pivot; universal distinguished-fiber Cauchy credit; literal physical Walsh replay',
 'mathematical_delta':'Scalar remainder9->6; hereditary product continuation5->4; actual OR/AND any-fan-in continuation14->10; all affine-flat edits including arbitrary two-point edits. Universal erasure witness certificate and explicit localized unpaid tree bill; prior debits and both terminals unchanged.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3','A024-MIXED-FACE-ORDER-OBSTRUCTION@4','B05-ODDFACE-LOCALIZED-REDUCTION@1'],
 'claims_created_or_changed':['A024-MIXED-FACE-ORDER-OBSTRUCTION@5'],
 'source_artifacts':['DERIVATION.md','AUDIT.md','FROZEN_SPEC.md','WITNESS_SPEC.md','OBSTRUCTION_SPEC.md','out/VALIDATION.json','out/ACTIVATION.json','out/WITNESS.json','out/OBSTRUCTION.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal localized overlap price and old-prefix payment remain open','Independent A087/A094 reconstruction pending; no formal certificate','Supervisor remote persistence/adoption unverified','Brain self-care degraded: owner-model/state-of-mind/latest-dream freshness unverified'],
 'packet_ids':['A024']}
assert set(progress)=={s.split(' (')[0] for s in required['progress_fields']}
js(run/'PROGRESS.json',progress);js(run/'PACKET_DELTA.json',progress)
source_paths=[proto,root/'BOARD.md',root/'claude/B05/STREAM_NOTES.md',old/'DERIVATION.md',old/'REPORT.md',old/'CLAIMS.json',old/'PROGRESS.json',old/'out/SOURCE_RECEIPTS.json',helper]
js(run/'out/SOURCE_RECEIPTS.json',{'fresh_scope':'Current BOARD B05/referee lines, full B05 notes, own STATUS, prior v4 proof, current protocol schema/review; source papers and broader registry intake inherited explicitly from previous runs',
 'prior_intake':str(old/'out/SOURCE_RECEIPTS.json'),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in source_paths]})
js(run/'out/EXECUTION_NOTES.json',{'brain_selfcare':'DEGRADED_UNVERIFIED: wake reported stale owner model97.3h, state-of-mind81.9h, latest dream32.6h; alerted in conversation',
 'compute_observation':{'available_memory_mb':23170,'commit_available_mb':39066,'disk_free_gb':67.1,'cpu_pct':87.6},
 'memory':'All jobs estimated below200MB; no job expected above300MB; no compiler/GPU/detached job',
 'mathematical_assertion_failures':0,'formal_certificate':False,'stopped':[],'left_running':[],
 'remote_save_verified':False,'research_writes':'A024 only; no git or messages',
 'lifecycle':'Required wake/checklist bookkeeping executed separately from research writes'})
pilot=outs['PILOT.json'];ap=outs['ACTIVATION_PILOT.json']
head=required['report_fields']
parts=[
 'Universal scalar erasure/transport and distinguished-fiber credit, plus hereditary affine-flat physical repair. For every Boolean f and Fourier fiber T disjoint from query i, W=(1-d-a^2)(d-b^2) supplies B<=L(a,b)+2sqrt(W)<=2d+2sqrt(W). For arbitrary quadratic phases edited on one affine flat, every physical residual admits K4 queries; actual OR/AND of any finite number of disjoint products admits K10 continuation. Bits, actual remaining uniform physical inputs, all dimensions and flat orientations; no general outer gate or full FEI assertion.',
 'Fresh source orientation: BOARD current B05/A087/A094 lines; B05 lead STREAM_NOTES v2; own STATUS; full v4 DERIVATION; execution protocol2026-10-11-execution-v2 schema/review fields. Exact transport is reconstructed from v3; corrected FEI+ normalization from the inherited source-paper intake. Earlier full campaign/registry/paper reads are inherited, not represented as fresh audits. Source paths and hashes: out/SOURCE_RECEIPTS.json. Proof locators: DERIVATION sections1-4, unsupported line section5; B05 localization supplies only the entropy/tree corollaries.',
 'DERIVATION.md contains the all-dimensional author proof. The scale-free derivative calculation gives L<=2|ab|, improving the universal signed binary-activation remainder to6rd. Dense flat edits of CODIMENSION<=2 are absorbed into the quadratic phase. Higher-codimension edits leave a robust quadratic pivot, or have an exact annihilator-fiber spectrum in the affine fallback. This closes ALL two-point and affine-flat residuals, not just coordinate-aligned edits. Independently, Fourier pairing and Cauchy give the distinguished-fiber bound for EVERY Boolean function and the localized tree liability(7). No reference reset occurs. First unsupported universal line: choosing an actual tree/fibers whose localized overlap cost is O(I) while retaining prior debit and both full terminal functions.',
 f'FROZEN_SPEC.md, WITNESS_SPEC.md and OBSTRUCTION_SPEC.md preceded their jobs. Main command: python -X utf8 code/check_flat.py --pilot, then code/check_flat.py; activation pilot/full and witness ran sequentially through Python runpy with the corresponding flags; final fixed stress command code/obstruction.py. Pilot3434 descriptions/{pilot["exact_assertions"]} assertions/{pilot["runtime_seconds"]:.3f}s; full318826 descriptions,2543504 physical restrictions,{val["exact_assertions"]} assertions/{val["runtime_seconds"]:.3f}s. Activation pilot16 pairs/{ap["exact_assertions"]} assertions; full64 pairs/272 prefixes/{act["exact_assertions"]} assertions/{act["runtime_seconds"]:.3f}s. Universal fiber verification278 functions/804 queries/3140 fibers/{wit["exact_assertions"]} assertions/{wit["runtime_seconds"]:.3f}s. Two fixed rare selectors/{obs["exact_assertions"]} assertions/{obs["runtime_seconds"]:.3f}s. Total{total} assertions excluding pilots. All PASS. Fraction/prime-log vectors and rational interval sign certificates; integer full spectra and independent direct character sums; squared nonnegative rational Cauchy checks, no approximate square roots. Runtime only uses floating point. No formal certificate or independent acceptance is claimed.',
 'v5 extends the existing pending v4 candidate. Universal remainder9->6; product continuation5->4; composition continuation14->10; entropy relaxations8->7 and17->13 using inherited B05 localization. The mean-rarity logarithm is fully bounded in the stated activation transport. Corrected FEI+ retains the product input-variance numerator, not output variance. Deterministic outputs are contracted. After any original prefix, new continuation adds ZERO K10-bad debit; it renews no bank and forgives no prior expense. Actual rare selectors in this same class can still be K4/K10 bad: out/OBSTRUCTION.json gives exact q/I and interval certificates. Hence no every-order interpretation survives. The new universal witness is algebraic, not a free reference reset or a proof of its required tree price.',
 next_action+' This is the first interference case outside one-flat spectral support and directly tests the new universal liability, rather than increasing width in a closed class. Independent review remains with existing reviewers; no new workers or messages created.',
 'Four protocol artifacts, complete proof/audit, frozen specs, code and outputs saved locally. code/finish.py validates exact field sets, count/hash receipts, witness/obstruction signs and statement digest; out/FINAL_RECEIPT.json records artifact and rolling-file readback hashes. STATUS is two lines; WORKLOG and LEARNED have dated append-only stage records. Supervisor remote mirror/adoption remains unverified. No research process stopped or left running; no source/other-agent edits or git/mail. Brain self-care degraded/unverified: owner-model, state-of-mind and latest-dream freshness remain affected; current task/source instructions govern.'
]
report='# A024 stage19: affine-flat repair and universal overlap credit\n\n'+'\n\n'.join('## '+h+'\n\n'+b for h,b in zip(head,parts))
report+='\n\n**Universal bridge**: This moves C018/C020 by a universal distinguished-fiber erasure bound and identifies the exact remaining localized overlap liability in (7); it moves C019/C024 by zero further K10-bad debit after ANY physical prefix for all quadratic affine-flat edited product blocks and arbitrary OR fan-in. Quantitatively R9->6, inner K5->4 and outer K14->10, with SAME original credit, old debit and both FULL stopping terminals. General non-flat interference and a universal O(I) price for (7) remain unproved; FEI stays OPEN. NEXT attacks a mixed query for two nonparallel flat edits using that actual liability because the cross term is the first obstruction to turning the closed one-flat mechanism into a universal witness-payment theorem.\n'
write(run/'REPORT.md',report)
write(home/'STATUS.md',f'STATE: A024 v5 saved: universal L<=2|ab|, R<=6rd and fiber-overlap credit; all affine-flat edits K4, actual OR/AND K10; {total} exact assertions PASS; review pending, FEI OPEN.\nNEXT: Pay actual mixed-query overlap liability for two nonparallel flat edits from SAME unused original credit, retaining old debit and BOTH full terminals; A087/A094 reconstruct v5.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (home/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write(f'\n{stamp} | Stage19 {run.name}: scalar L<=2|ab| gives R6rd; affine-flat edits absorbed at codim<=2, otherwise robust quadratic pivot or exact annihilator fallback; K4 inner/K10 actual composition. Universal distinguished-fiber W=(1-d-a^2)(d-b^2) gives exact remaining localized tree bill. {total} main assertions PASS; full318826 descriptions in457.402s;804 queries3140 fibers;64 activation pairs272 prefixes; m4/m10 bad-selector stress preserves old charges. No changed-tree Phi transfer; review and universal price open. No jobs left running.\n')
with (home/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write(f'\n{stamp} | L(a,b)<=2|ab| in bits (scale-free F(x) maximum2 ln2); signed activation remainder <=6r|beta|<=6rd. Quadratic phase plus ANY affine-flat edit is hereditary K4: codim<=2 absorbs into quadratic; codim>=3 preserves a half-influence quadratic pivot to>=1/4; affine fallback has Fourier support on the annihilator, erasure0 when e_i outside it and B=2u(1-u)+L(1-u,u)<=4d(1-d) inside. Products tensorize; OR/AND fan-in has K10 continuation after any physical prefix. Universal existing-query fiber credit: for T excluding i, a=fhat(T),b=fhat(T+i), W=(1-d-a^2)(d-b^2), B<=L(a,b)+2sqrt(W)<=2d+2sqrt(W), since |b|<=d from derivative. A localized tree price for sum_bad p[2sqrt(W)-(K-2)d] is still unpaid. This is an algebraic witness, not a reference reset; old debit/KL and both terminals persist. Fixed selectors m4/m10 show not every order is good; they are not FEI counterexamples.\n')
assert json.loads(read(run/'PROGRESS.json'))==json.loads(read(run/'PACKET_DELTA.json'))
assert len(read(home/'STATUS.md').splitlines())==2
assert all('## '+h in read(run/'REPORT.md') for h in head)
assert hashlib.sha256(json.loads(read(run/'CLAIMS.json'))[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='FINAL_RECEIPT.json')
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS_LOCAL_READBACK','time_utc':stamp,'files':[{'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'rolling_files':[{'path':str(home/n),'sha256':sha(home/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],
 'main_exact_assertions':total,'independent_review':'PENDING','full_fei':'OPEN','stopped':[],'left_running':[]}
js(run/'out/FINAL_RECEIPT.json',receipt)
print(json.dumps({'status':receipt['status'],'run_files':len(files),'main_exact_assertions':total,'independent_review':'PENDING','full_fei':'OPEN','left_running':[]}))
