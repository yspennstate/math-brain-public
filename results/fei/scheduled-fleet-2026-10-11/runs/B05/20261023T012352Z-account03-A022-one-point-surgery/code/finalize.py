"""Persist the verified stage; no mathematical search or shared-index mutation."""
from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,o): p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=read(protocol_path)
results={n:read(root/'out'/f'{n}.json') for n in ['pilot','main','targeted','scalar','replay']}
assert all(o['status']=='PASS' for o in results.values())
total=sum(o['assertions'] for o in results.values()); assert total==53684
assert results['main']['cases']==768 and results['targeted']['cases']==12 and results['replay']['cases']==8
prior=agent/'runs/20261021T213608Z-account03-A022-one-point-surgery'
a021=Path('~/brain_workers/FEI100_20261011/agents/A021/runs/20261023T001013Z-account03-A021-rare-core-asymptotics')
old=read(prior/'CLAIMS.json')[0]; dep=read(a021/'CLAIMS.json')[0]
board=Path('~/brain_workers/FEI100_20261011/BOARD.md')
notes=Path('~/brain_workers/FEI100_20261011/claude/B05/STREAM_NOTES.md')
sources=[]
for p in [protocol_path,board,notes,prior/'REPORT.md',prior/'CLAIMS.json',a021/'REPORT.md',a021/'PROOF.md',a021/'CLAIMS.json',a021/'code/check.py',a021/'out/LEAN.json']:
    txt=p.read_text(encoding='utf-8-sig')
    sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'lines':len(txt.splitlines()),
                    'scope':'Mathematical use and acceptance restricted as stated in REPORT/PROOF'})
save(root/'out/SOURCE_RECEIPTS.json',sources)
save(root/'out/FINAL_WITNESS.json',{
 't':2,'delta':'1/64','v':0,'controller':'A(z)=z on one bit','a':'one Fourier character','old_U':0,
 'L':0,'original_R':['63/64','1/64'],'terminal_H':0,
 'final_CE':'h2(1/64)=6-(63/32)log2(3)-(63/64)log2(7)',
 'final_B':'-6+(63/32)log2(3)+(63/64)log2(7)',
 'rigorous_sign':'B_final < -3/32, because phi(1/64)=3/32 and phi(63/64)>0',
 'scope':'Refutes universal nonnegative final CE-only bank with unchanged R; does not refute FEI',
 'verification':'direct terminal identity in main and separate replay; proof Section7'})
report='''# A022 stage8: the second query and long original-reference histories

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. For every t>=2, every vertex v of b=g tensor t (g is the three-bit point defect), and every arbitrary independent control indicator A, preserve original Q=P_b, original controller spectral reference R, L=8^-t H(1-2A), old U in[0,t/64], original reaches and both full terminal KLs. Entropies are in bits. Along any fixed block-first order, at every uniform-depth prefix d<=3floor(t/2)+2, with the explicitly prescribed positive local references of PROOF Section2, the ACTUAL remaining bank satisfies

    B_d=4 I_data,remaining+L-C_d-U >=13t/576.

This includes the second query in an ALREADY converted block, completion of that block, and continued entry into later blocks. It covers arbitrary t and control dimension/bias, but not unequal-depth adaptive stopping cuts or control queries. It refines the existing A022 ledger rather than opening another broad universal candidate.

## sources actually read, revisions and theorem locators

Entry BOARD.md, B05 STREAM_NOTES.md v2, and own STATUS were read. The board identifies A021's first-query conversion as already complete, so that step is consumed rather than repeated. A021 run20261023T001013Z REPORT, PROOF Sections2--4, CLAIMS and checker were read; the exact signed source, complete first-child reference formula and old-reserve scope were reconstructed. A022 run20261021T213608Z REPORT Sections2--6 and CLAIMS supply the original signed reference interface. Dependency SHA256s and exact source paths are in out/SOURCE_RECEIPTS.json. Protocol revision2026-10-11-execution-v2 supplies the unchanged schema and compute rules. No new paper or web premise and no novelty claim is used. Older campaign endpoint text is superseded by the current2026-10-23 14:49UTC deadline; no schedule is altered.

The current brain wake reports degraded personal-context notes: personal-context model87.8h old, state-of-mind72.4h old. That warning was stated in the session; those notes were not relied upon for mathematics or authority. Current source files govern.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete all-parameter proof. The original R is passed unchanged to ALL children. Untouched blocks retain original q; completed blocks have reference1. First-bit references are A021's uniform4/positive(13,1,1,1)/16. After the second bit, the reference is15/16 at the unedited one-bit seed's character/constant label and1/16 at the other label. Zero R rows retain zero actual mass and no zero data reference is used.

Write p=log2(13), q15=log2(15), and sigma the second physical edge's seed sign. The exact second-query reference-capacity loss is

    ell2=2+p/2-q15+delta alpha[8sigma-w1+2q15],
    w1=0 if the first queried vertex bit is0, otherwise3p.

It is<1/4 for all t>=2 and negative for t>=3. A021's11t/64 first-query reserve therefore gives3t/64 after the second query. These are REFERENCE losses, not bounds on every entropy decrement.

For the longer history, every active cylinder's ORIGINAL physical reach times its conditional point density is still delta. Exact complete CE and remaining physical influence are PROOF(3)--(5). For n=t-r remaining blocks, the intact-block lower bank is(314n-117t-54)/576. At partial-block prefixes it is(314n-117t-32)/576. Since n>=t/2, both are>=13t/576. The inequalities use the SAME original signed seed costs, beta>3/4, X<=118/9, partial banks>5/6, partial signed costs<=16, and the original controller overhead<=delta alpha(12t+6). Integer-power comparisons certify all logarithmic bounds; finite testing does not supply the all-t passage.

The reserve13t/576 is smaller than the prior11t/64 because it applies after as many as3floor(t/2)+2 queries, rather than one. It still retains the original t/64 plus t/144. No bank, R, L or U is reset at a block boundary. The complete signed identity is B_d+D_d+E_d=B_0+D_0, with every terminal KL in D_d and the accumulated actual signed query account in E_d.

Final CE-only obstruction: after ALL data bits are exposed, C_final=H(R), H_final=L, and B_final=L-H(R)-U. For t=2,A(z)=z,U=0, this is-h2(1/64)<-3/32. The actual terminal entropy is0. Its terminal KL equals+h2(1/64) and cancels the negative reference balance. out/FINAL_WITNESS.json is an exact Boolean certificate. This refutes only a universal nonnegative FINAL CE-bank extension with unchanged R, not FEI or the signed history account.

First unsupported universal line: an actual controller query after the paid data history admits its prescribed complete child references at a fixed rate using SAME inherited R, remaining original reserve, old U, full controller terminals and both child KLs. Arbitrary nonflat source admission and arbitrary unequal-depth stopping cuts also remain open.

## executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json precedes the pilot and searches. Pilot24 cases/1440 exact assertions PASS in1.774709s. Its linear projection left little margin for shared-machine contention; BEFORE main, only the main runtime cap was raised from60 to120s, without changing any family or dimension. Main768 cases/46080 exact assertions PASS in49.425779s: t=2, all64 vertices, six declared two-bit controllers, two fixed block-first coordinate orders, all depths0..6. Depth6 checks the final CE-bank obstruction; the paid theorem ends at depth5.

Targeted t=3:12 cases/624 exact assertions PASS in2.435747s, vertices0 and511, the six controls, depths0..5. Scalar replay:3261 declared parameter cases/2260 exact assertions PASS in0.125459s over t=2..64,r=0..floor(t/2),j=0,1,2, plus all local signed costs and six integer logarithm certificates. Both partial j values share the same rational lower-bound check. These finite domains do not assert all-dimensional exhaustiveness.

REPLAY_SPEC.json freezes a separate implementation importing NO production helper. It reconstructs eight roots by direct character sums and physical edge enumeration, forms every COMPLETE joint reference independently, and checks all depths, both terminal KLs, original R, old U, influence telescoping and final-collapse identities. It passes3280 exact assertions in0.331243s. Main code uses integer FWHT, Fraction-valued prime-log identities, multiplicity compression and40-term atanh intervals with proved geometric tails. Supporting intervals and integer signs are exact, not floating decisions. Total including pilot:53,684 exact assertions. This is author verification by two implementations, not independent-person acceptance.

Commands: python -X utf8 code/check.py pilot; code/check.py main; code/check.py targeted; code/scalar.py; code/replay.py. All are small jobs, frozen estimate60--100MB, peak unmeasured; no automatic dimension escalation, GPU, remote compute or detached process. The current resource gate exits1 at physical free1.3GB (need4GB), commit free15GB (need8GB). Formal admission is HELD and no compiler starts. code/Bank.lean records scalar targets only; it is uncompiled, with no formal theorem, compiler/source/axiom certification or extrapolation to entropy. Mathematical rung: analytic proof with exact author checks, independent review pending.

Failure checks explicitly varied: zero/full activation, all local vertex types, inherited R zero-row support, original physical reaches, already changed references, old U, all terminal debts, sign of actual data edges, distinguishing actual entropy decrement from reference loss, and the false final nonnegative CE-only extension. The all-t proof has no canceled alpha denominator, limit exchange or omitted terminal.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v6 to v7, retaining inherited scopes. A021's source first-query theorem is consumed at its stated scope; formulas and the sharper original source estimate are checked, not attributed as new A022 source credit. No new review acceptance of the whole inherited bundle is asserted. A021/A025/A028/A029 may consume the long-history formulas and final KL obstruction. A087/A094 should review the active-path reach cancellation, partial-block costs, both-terminal signed account and the exact scope of the fixed-order/uniform-depth theorem.

The unpaid target has moved from one already converted data query to a mixed DATA/CONTROL conversion. Completing more identical data blocks beyond the proven range without retaining the final KL would target a false CE-only statement. The full source controller entropy L remains explicit throughout and is not proved to satisfy FEI for arbitrary A.

## one next mathematical action and independent reviewer

Expose ONE actual controller coordinate after a paid nonflat data prefix. Carry original R, remaining13t/576, old U and the complete signed data-query account. Price explicitly supplied positive child controller/data references while keeping both full source-controller terminal entropies and all child KLs. A021/A025 reconstruct the new continuation; A087/A094 independently audit source ownership and the final-collapse refund. No messages or observed review acceptance are claimed.

## actual persistence receipts or precise save blocker

REPORT, PROOF, CLAIMS, PROGRESS and identical PACKET_DELTA, frozen specs, code and exact outputs are local to the assigned A022 run. Rolling STATUS, WORKLOG and LEARNED are current. out/ARTIFACT_CHECK.json validates exact field sets, statement digest, packet compatibility, file hashes and20MB limits. No campaign registry, other agent folder, research brain content, git state or external service is mutated. Required wake/checklist bookkeeping is the administrative exception. Supervisor copying, remote mirrors and independent review remain unverified.

Universal bridge: This advances C024 history transfer toward C019 by consuming A021's paid first conversion and proving an ORIGINAL-reference reserve through3floor(t/2)+2 physical data queries, including completion of already converted blocks. The remaining bank is>=13t/576 after old U, with original R, full L and every terminal KL intact. A Boolean final-collapse witness proves the CE-only extension is false and identifies its exact compensating KL. What remains is the actual mixed controller-reference conversion or arbitrary nonflat source admission. NEXT attacks that conversion with the same remaining account, the shortest universal step because longer identical data-only histories cannot remove controller hardness or justify a reference reset.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8',newline='')
statement='Refinement of A022 ledger v6, inherited assertions retaining original scope: for all t>=2, g=-1 only at000 on3bits, b=g tensor t, arbitrary controlled vertex surgery by independent indicator A, original Q=P_b and controller spectral reference R, L=8^-t H(1-2A), and old0<=U<=t/64, every uniform-depth prefix d<=3floor(t/2)+2 of every fixed block-first coordinate order admits the prescribed complete positive local references in PROOF Section2 and has ACTUAL remaining B_d=4I_data,remaining+L-C_d-U>=13t/576. Second already-converted query loss is exactly PROOF(6), <1/4 for all t>=2 and negative for t>=3. Original R, original physical reaches, both full terminal KLs, old U and full L remain; B_d+D_d+E_d=B_0+D_0 with E signed actual query account. After all data exposures, B_final=L-H(R)-U. The actual Boolean t2,literal-controller,U0 instance gives B_final=-h2(1/64)<-3/32 while H_final=0 and D_final=h2(1/64). Thus nonnegative final CE-only extension with original R is false; full FEI, arbitrary mixed queries and unequal-depth adaptive cuts remain OPEN.'
claim={k:old.get(k) for k in protocol['required_per_run']['claim_fields']}
claim.update(version=7,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),
 hypotheses=['Uniform data/control cubes; bits','t>=2; g tensor t; one controlled vertex flip; arbitrary independent A','Fixed block-first coordinate order and uniform-depth physical cuts d<=3floor(t/2)+2','Original R and untouched q retained; partial references prescribed;0<=U<=t/64; full L and terminal KL retained'],
 contributors=['A022 account03 stage8','A021 original first-query source; A022 prior ledger at original scope'],
 proof_source={'current':'PROOF.md','inherited':str(prior/'REPORT.md'),'validation':['out/main.json','out/targeted.json','out/scalar.json','out/replay.json','out/FINAL_WITNESS.json']},
 proof_dependencies=[{'claim_id':old['claim_id'],'version':6,'statement_sha256':old['statement_sha256'],'scope':'inherited source/reference interface only'},
                     {'claim_id':dep['claim_id'],'version':dep['version'],'statement_sha256':dep['statement_sha256'],'scope':'original signed source and specified first-query conversion; reconstructed at that scope'}],
 review_records=old.get('review_records',[]),status='ANALYTIC_PROOF_EXACT_AUTHOR_CHECKED; INDEPENDENT_REVIEW_PENDING; UNIVERSAL_FEI_OPEN',
 supersedes=[{'claim_id':old['claim_id'],'version':6,'scope':'long-history refinement; inherited conclusions unchanged'}],
 refutes=['Unconditional nonnegative final CE-only bank with SAME R,full L and U>=0 after all physical data exposures'],
 first_unproved_line='Actual controller-query prescribed reference conversion after paid data prefix is paid from SAME inherited reserve with full source-controller terminals and old signed query/KL account.',
 next_consumers=['A021','A025','A028','A029','A087','A094','B05'])
save(root/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':root.name,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH',
 'attempt_id':'A022-stage8-converted-block-long-history','method':'consume A021 paid first query; exact complete-reference block-prefix invariant and final CE-only obstruction',
 'mathematical_delta':'Pays second query and block completion, extends through3floor(t/2)+2 physical data queries with SAME original R,Qrest,U and terminal KLs; reserve13t/576. Exact literal-controller final CE-only obstruction isolated.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_AUTHOR_CHECKED; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':7}],
 'source_artifacts':['REPORT.md','PROOF.md','SEARCH_SPEC.json','REPLAY_SPEC.json','code/check.py','code/exact.py','code/scalar.py','code/replay.py','code/Bank.lean','out/pilot.json','out/main.json','out/targeted.json','out/scalar.json','out/replay.json','out/FORMAL_ADMISSION.json','out/FINAL_WITNESS.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':'Expose one actual controller bit after a paid nonflat data prefix; price original-R conversion with SAME remaining13t/576, old U, full source-controller terminals, signed data account and BOTH terminal KLs; A087/A094 review.',
 'stagnant_substantive_attempts':0,'blockers':['Controller-reference conversion and arbitrary nonflat source admission unproved.','Unequal-depth adaptive-cut extension not asserted.','Formal admission held; independent review and supervisor mirrors pending.'],'packet_ids':['A022']}
save(root/'PROGRESS.json',progress); save(root/'PACKET_DELTA.json',progress)
(agent/'STATUS.md').write_text('STATE: A022 stage8 saved: second query/full-block/long original-reference histories paid through3floor(t/2)+2 at rate4; reserve13t/576 after old U; final CE-only negative witness/full KL retained;53684 exact assertions PASS; review pending; FEI OPEN.\nNEXT: A021/A025/A087/A094 review v7; expose one actual controller bit after paid nonflat data prefix, pricing ORIGINAL R conversion from SAME remaining13t/576 with old U, full controller terminals and BOTH KLs.\n',encoding='utf-8',newline='')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
entry=now+' stage8: consumed A021 paid first-query source instead of repeating it. Exact second-query loss<1/4, negative t>=3; completion and long block-first data prefix through3floor(t/2)+2 retain13t/576 after old U with original R and full L/KL. Literal-controller final CE bank=-h2(delta)-U, exact terminal KL cancels; not FEI counterexample. Pilot1440+main46080+target624+scalar2260+replay3280=53684 exact assertions PASS. Main49.426s, separate direct-character replay0.331s. Formal admission held memok exit1, no compiler. Independent review/universal mixed-query bridge OPEN.\n'
with (agent/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f: f.write('\n'+entry)
with (agent/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\nStage8: g tensor t point activation keeps physical reach times active point density equal to ORIGINAL delta under data exposures. Original R survives all data prefixes in expectation; it must not be replaced by a child marginal. At block-first depth3r+j, positive first references uniform4/(13,1,1,1)/16 and second references15/16 at unedited one-bit seed label give exact complete CE formulas in PROOF(3),(4). Signed intact costX<118/9, partialY<=16, partial base banks>5/6 yield B>=13t/576 for r<=floor(t/2),j0..2, with oldU<=t/64, full L and full terminal KL. Smaller bound than11t/64 applies to LONGER history. All-data final B=L-H(R)-U can be negative: literal A gives-h2(delta)-U while actual terminal H=0, and terminal KL=h2(delta) cancels. No universal CE-only nonnegativity or R reset follows. Next must price actual controller conversion with original inherited account.\n')
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
assert sha(root/'PROGRESS.json')==sha(root/'PACKET_DELTA.json')
for field in protocol['required_per_run']['report_fields']: assert field in report
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
receipt={'status':'PASS','statement_sha256':claim['statement_sha256'],'protocol_field_sets':'PASS','packet_delta_identical':True,
 'exact_assertions':total,'independent_person_review':'PENDING','formal_status':'ADMISSION_HELD','remote_mirror':'UNVERIFIED','files':[]}
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_CHECK.json':
  assert p.stat().st_size<20*1024*1024
  receipt['files'].append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(root/'out/ARTIFACT_CHECK.json',receipt)
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
