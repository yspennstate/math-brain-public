from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def save(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
main=json.loads(read(RUN/'out/validation.json'));other=json.loads(read(RUN/'out/independent_validation.json'))
assert main['status']==other['status']=='PASS'
oldpath=ROOT/'runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget/CLAIMS.json'
old=json.loads(read(oldpath))[0]
newstatement=('For every even m>=4, every Boolean bent b on the uniform m-cube, every two distinct vertices v,w, and one independent balancing sign z, let g0=zb,g1=zb_v,g2=zb_w, where b_v,b_w are actual single-vertex flips. With independent fair controls A,B, put f=g0+A[g1+B(g2-g1)-g0], pi=(1/2,1/4,1/4), H_T=sum pi_j H(gj), I_T=sum pi_j I(gj), I_C=I(f)-I_T, R_star=2sum_{j<k}pi_j pi_k I(gj gk), eta=1 if v,w are adjacent and0 otherwise. Then I_C=2^(1-m), R_star=(3m/2-eta/2)2^-m<=2I_T, and (H(f)-H_T-R_star)/I_C < 9/(4 ln2)+eta/4 <4. The supremum in each adjacency class, over even m>=4, equals 9/(4 ln2)+eta/4. In particular H(f)<=4I(f). Query A then B only on A=1, stop at all three original cores, open the marked symmetric physical data reserve once at the root and never renew it at control descendants. All terminal entropies remain. No arbitrary-width, mixed-data local-payment, arbitrary-terminal, or universal FEI assertion is included.')
claim=dict(old);claim.update(version=5,exact_statement=old['exact_statement']+' ADDITIONAL ALL-DIMENSIONAL THREE-BENT-CORE SUBTHEOREM: '+newstatement,
 proof_source=str(RUN/'PROOF.md'),contributors=['A023'],review_records=[],status='AUTHOR_PROOF_WITH_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW; PRIOR_SCOPES_PRESERVED',
 supersedes=[{'claim_id':old['claim_id'],'version':4}],first_unproved_line=None,
 proof_dependencies=[{'claim_id':old['claim_id'],'version':4,'source':str(oldpath),'status':'Earlier statements preserved at their original review scope; new subtheorem reconstructed directly, not inferred from finite census.'}],next_consumers=['A025','A029','A028','A087','A094','B05','B20'])
claim['hypotheses']=old['hypotheses']+['New subtheorem requires arbitrary bent seed, two DISTINCT edits, shared balancing sign z, exactly two independent FAIR one-bit point controls, and all original terminal weights.']
claim['statement_sha256']=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
save(RUN/'CLAIMS.json',[claim])
leanp=RUN/'out/lean_validation.json'
lean=json.loads(read(leanp)) if leanp.exists() else {'status':'NOT_EXECUTED_RESOURCE_LIMIT','scope':'Scalar core formalization saved; no Lean-checked mathematical result claimed.'}
nextaction='Expose one original core-data coordinate in the three-bent-core family, retaining original pi/reference, spent two-control debit, BOTH full terminals, and SAME remaining R_star; price the signed nonflat residual using actual release plus unused original terminal surplus. Reviewers A029/A028/A087/A094.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B05','packet_id':'A023','gap_id':'G-R-MISMATCH-FIRST-REVELATION','attempt_id':'A023-17-three-bent-core-coherent-refund',
 'method':'Exact coherent spectrum compression, independent physical-edge falsification/correction, signed absolutely convergent Taylor series with coefficientwise negative combined remainder, original single reserve and complete terminal accounts',
 'mathematical_delta':'Extends prior finite three-core refund to ANY bent seed and two distinct edits in ALL even dimensions m>=4, at fair widths r=s=1. Sharp class control supremum9/(4ln2)+eta/4<4; H<=4I. Adjacent boundary factor corrected by exact direct edges. '+str(main['exact_assertions'])+' primary and '+str(other['exact_assertions'])+' independent exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'AUTHOR_PROOF; EXACT_FINITE_RECONSTRUCTION_PASS; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':5}],
 'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/independent.py','code/Tail.lean','code/finalize.py','out/FROZEN_SPEC.json','out/INDEPENDENT_SPEC.json','out/validation.json','out/independent_validation.json','out/PILOT_CORRECTION.json','out/sign_certificates.json','out/direct_rows.jsonl','out/scalar_rows.json','out/independent_rows.json','out/source_receipts.json'],
 'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['Actual mixed-data nonflat residual is unpaid by this root theorem.','General arbitrary-core terminal admission and full FEI remain open.','Independent mathematical review and supervisor copies unverified.','Lean status: '+lean['status']],
 'packet_ids':['A023']}
save(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',read(RUN/'PROGRESS.json'))
fields=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))['required_per_run']
assert set(progress)==set(x.split(' (')[0] for x in fields['progress_fields'])
assert set(claim)==set(fields['claim_fields'])
report=f'''# exact target, quantifiers, hypotheses and units

A023/B05 stage17, substantive continuation of stage5. Uniform Boolean signs, entropy bits. For every even m>=4 and EVERY bent seed b, take its two distinct point flips, multiply all three cores by the SAME independent sign z, and use fair nested point controls A,B. Original pi=(1/2,1/4,1/4), I_C=2delta, delta=2^-m, R_star=(3m/2-eta/2)delta, eta=1 for adjacent edits. The complete control entropy increment is paid by one original reserve:

    (H(f)-H_T-R_star)/I_C < 9/(4 ln2)+eta/4 <4.

The constant is the exact supremum for this family in each adjacency class (adjacent approximately3.4961, nonadjacent approximately3.2461). Both full terminal entropies remain, R_star<=2I_T, H_T<=2I_T, hence full H(f)<=4I(f). Arbitrary widths, mixed-data local payment and full FEI remain OPEN. Rung: author proof with exact reconstruction checks, pending independent review; not a Lean-checked all-dimensional theorem.

# sources actually read, revisions and theorem locators

Read current BOARD snapshot2026-10-22 20:55UTC, B05 STREAM_NOTES v2, own STATUS/LEARNED/WORKLOG, complete EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2, campaign README/CURRENT_STATUS and relevant registry/stream entries. Source trees are read-only. Prior A023 run20261014T051414Z supplies the exact finite refund frontier and requested bent/two-edit NEXT; its REPORT, CLAIMS, PROGRESS and checker were read. Own stage4 check_block.py is used ONLY as pinned exact arithmetic, not as an unproved theorem premise.

Read the latest substantive A028 REPORT (20261014T051435Z) and A029 REPORT (20261014T055200Z): bank conservation and actual signed entropy payment are separate. Their later marker-only folders do not substitute for a mathematical report. A029 finite-label variance conservation motivates NEXT but is not a premise of the new root proof. Earlier full source scope remains inherited; current paper inspection is contextual, not a re-audit of either manuscript. The initial UTF-8 decode of a paper extract failed; context_receipts.json records the actual encoding used where recovered. No external literature, novelty, publication, or full-paper review claim is made. Brain recall returned the older bent single-edit splice and its constant-2 warning; the full card was requested, and no recalled claim is a proof premise. Current explicit owner deadline supersedes older campaign metadata.

# complete derivation or exact first unsupported line

PROOF.md gives all formulas. Translation/sign normalization reduces one edited vertex to0 and b(0)=1. Bent Fourier inversion counts the signed rows on the half-space b(w)chi_T(w)=1. The three nonzero-control sectors each have M/2 atoms of mass delta^2. The control-zero spectrum has one unchanged half and two altered amplitude classes. This coherent spectrum yields H(f)=m+3m delta/2-J and H_T=m-D/2, with explicit scalar F(x)=(1+x)^2 ln((1+x)^2) formulas.

Combining the absolutely convergent expansions, rather than separately charging their tails, gives

    (D/2-J)ln2 =9delta/2-sum_{{l>=2}}[2(4^l-1)/u_l+(4^l-4)/v_l]delta^l,

where u_l=(2l)(2l-1)(2l-2), v_l=(2l-1)(2l-2)(2l-3) are positive. Every tail coefficient is negative. Physical point-product edges give R_star=(3m/2-eta/2)delta. Thus the exact signed bill is D/2-J+eta delta/2, proving the sharp control envelope. The O(delta^2) geometric tail proves its limiting sharpness. ln2>2/3 proves the strict rate<4 without floating arithmetic. The balancing z supplies the stated simple full-terminal H<=2I certificate.

Stopping rule: query A; stop at g0 on failure, otherwise query B and stop at actual g1 or g2. Original terminal weights, all terminal costs and one marked physical-data reserve are retained. No bank is renewed at the inner node. This is root stopping payment, not a sum of separately renewed local prices.

First unsupported universal line: after an actual core-data query, pay the signed nonflat entropy/reference residual using release of the SAME original reserve and genuinely unused ancestor terminal surplus, preserving both full terminal debts and old bookings. The coherent root calculation does not establish that drift inequality or universal terminal admission.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded each job. Main domain: canonical quadratic bent m=4, ALL240 ordered distinct vertex pairs; m=6, v=0,w=1..8; compressed scalar formulas m=4,6,...,40. No quotient or all-bent finite exhaustion claimed. Integer FWHT and direct physical edges independently compare to compressed spectrum and all original influences. Primary result: {main['direct_cases']} direct cases plus{main['scalar_cases']} scalar cases, {main['exact_assertions']} exact assertions PASS, {main['sign_certificates']} saved sign certificates, {main['elapsed_seconds']:.6f}sec. Rational prime-log signs use the pinned own helper's positive atanh tail and outward dyadic bounds.

One substantive first-run failure was caught at the R_star adjacency formula. I had subtracted8delta rather than4delta from the two-point product influence. Direct edges rejected that formula. out/PILOT_CORRECTION.json preserves the failing line and correction. The corrected frozen-domain run passed; no hypothesis or domain was weakened. The preliminary adjacent limiting figure3.7461 changes to3.4961 because the corrected reserve has half the adjacency deduction, not because of a precision change.

Independent checker imports no old helper. It reconstructs F through40-term exact rational natural-log atanh intervals, checks sharp scalar signs on the same19 dimensions, and independently checks coefficient identities and signs for l=2..20. Result: {other['exact_assertions']} exact assertions PASS in{other['elapsed_seconds']:.6f}sec. The all-dimensional extension is supplied by the explicit convergent-series proof, not these finite checks. Commands from A023: python -X utf8 runs\\{RUN.name}\\code\\check.py and same run code\\independent.py. Maximum runtime60seconds each; estimates60MB and30MB, no >300MB job, GPU, automatic dimension escalation or detached task. Lean status: {lean['status']}; no unavailable formal certificate is claimed.

# proof dependencies and changed downstream conclusions

Version5 extends the existing A023 candidate, preserving earlier subtheorems at their original scopes. The new result is reconstructed from definitions, Fourier inversion and a proved scalar series; no A028/A029 entropy theorem or unreviewed finite inference is needed. Their source reports prevent conflating conservation with payment. The earlier A021 remainder-sign error is not used. The exact new boundary factor and sharp scalar tail are recorded for A025/A029/A087/A094 to reconstruct independently.

The former two-bit finite refund now has a high-dimensional coherent class where multiplier1 of R_star suffices and the complete control rate is strictly below4. This does not delete A029's general grouping surcharge, and it does not prove arbitrary-core refund. The same original terminal bank funds the full root bill; no descendant entitlement is inferred. Independent review, remote copying and downstream use remain unverified.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

Saved REPORT, CLAIMS, PROGRESS, byte-identical PACKET_DELTA, complete PROOF, frozen specs, exact checkers and outputs, first-failure correction, and source/artifact receipts inside A023 only. Rolling STATUS is exactly two lines; WORKLOG and LEARNED append the new theorem and correction. finalize.py checks schema fields, statement digest, completion counts and file-size cap. Local save succeeded; independent acceptance and supervisor mirrors are unobserved.

**Universal bridge:** This stage moves C019 stopping-tree payment from a finite two-bit three-core census to every bent seed and two distinct edits in all even dimensions m>=4, using the SAME symmetric physical reserve once and retaining every original terminal. It proves a sharp control supremum9/(4ln2)+eta/4<4 and full H<=4I for that family. C024's next unpaid step is actual mixed-data entropy drift after the spectra become nonflat, with original weights, old debit and both full terminal/reference bills retained. NEXT attacks that precise conserved-bank-versus-payment gap; it is the shortest route beyond this refund because it tests whether the newly sharp coherent cancellation survives the operation required by universal restriction induction.
'''
write(RUN/'REPORT.md',report)
state='STATE: A023 stage17 author proof: arbitrary bent seed/two distinct edits, all even m>=4 at fair controls paid once from SAME R_star; sharp rate9/(4ln2)+eta/4<4, full H<=4I; exact checks PASS; review pending, FEI OPEN.\nNEXT: Pay one actual core-data query with original pi/reference, old debit, BOTH terminals and SAME unused R_star; A029/A028/A087/A094 review sharp signed-series refund.\n'
write(ROOT/'STATUS.md',state)
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{date} stage17 {RUN.name}: Resumed stage5 high-contrast NEXT. Derived arbitrary-bent/two-distinct-edit exact coherent spectrum, sharp combined negative Taylor tail, one R_star/full-terminal rate4 theorem for all even m>=4. First direct check rejected doubled adjacency deduction; corrected product boundary4delta and sharp adjacent rate9/(4ln2)+1/4. {main["exact_assertions"]} main plus {other["exact_assertions"]} independent exact assertions PASS. Full FEI/mixed-data drift OPEN; no shared writes, brain writes, git, messages or detached work.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-23: For arbitrary bent b, balanced cores zb,zb_v,zb_w and fair nested controls, ANY distinct v,w have the same coherent entropy. I_C=2delta, R_star=(3m/2-eta/2)delta. The exact signed bill is D/2-J+eta delta/2. Its natural-log combined series is9delta/2 minus strictly positive coefficients [2(4^l-1)/u_l+(4^l-4)/v_l]delta^l. Hence sharp class control supremum9/(4ln2)+eta/4<4 and full H<=4I for all even m>=4. Adjacent two-point product influence is4m delta-4delta, NOT4m delta-8delta (caught by independent direct edges). Reserve marked only once; mixed-data drift remains unpaid.\n')
sources=[Path(r'BOARD.md'),Path(r'claude\B05\STREAM_NOTES.md'),oldpath,RUN/'out/helper_receipt.json']
save(RUN/'out/source_receipts.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources])
for title in fields['report_fields']:assert '# '+title in report
assert report.rfind('Universal bridge')>report.rfind('# actual persistence')
assert (RUN/'PACKET_DELTA.json').read_bytes()==(RUN/'PROGRESS.json').read_bytes()
assert len(read(ROOT/'STATUS.md').splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],'rolling':[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ['STATUS.md','LEARNED.md','WORKLOG.md']],'mirror':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps({'status':'PASS','protocol_fields':'EXACT','run':str(RUN),'main_assertions':main['exact_assertions'],'independent_assertions':other['exact_assertions'],'files':len(files)}))
