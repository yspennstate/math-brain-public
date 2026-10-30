from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
run=ROOT.name;now=datetime.now(timezone.utc).isoformat()
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source_paths=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),AGENT.parents[1]/'BOARD.md',AGENT.parents[1]/'claude/B01/STREAM_NOTES.md',AGENT/'STATUS.md',AGENT/'LEARNED.md']
others=AGENT.parent
for who,stage,files in [
 ('A002','20261013T220534Z-fleet05-A002-hardness-preserving-transformations',['REPORT.md']),
 ('A003','20261013T222630Z-fleet05-A003-minimal-target-formulation',['REPORT.md']),
 ('A072','20261013T222130Z-fleet05-A072-exact-walsh-engine',['REPORT.md']),
 ('A090','20261013T213537Z-fleet05-A090-independent-reconstruction',['REPORT.md']),
 ('A061','20261013T215821Z-fleet05-A061-entropy-process',['PADDING_EDIT_PROOF.md','CLAIMS.json'])]:
    source_paths.extend(others/who/'runs'/stage/file for file in files)
if not (ROOT/'out/SOURCE_MANIFEST.json').exists():
    write('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in source_paths])
statement=('Fix C>=0 and a nonconstant finite uniform Boolean seed f with H(f)-CI(f)>0. Pad with r dummy coordinates and flip physical vertex zero to get F_N, N=n+r. For every dummy j, average child slack sigma_j(F_N)=-(delta(f)+delta(F_(N-1)))/2 tends to -delta(f)<0. Every original coordinate slack converges to its seed slack. If all original average child slacks are strictly positive, then eventually the average-child-eligible coordinates are exactly the original coordinates and their minimum B_i/Inf_i tends to E(f), although the unrestricted minimum tends to min(E(f),2). For the three-bit point defect, N=12,C=8/3, F_N has full Fourier support, max influence<1/4 and positive delta; all original coordinates have nonnegative individual child slacks and B_i/Inf_i>5/2, while all nine dummy coordinates have both individual child slacks negative and B_j/Inf_j<5/2. Thus root selection B_i<=5Inf_i/2 does not imply selection with certified average children at C=8/3 on this class.')
hypotheses=['Finite uniform Boolean signs; entropy in bits; normalized Walsh coefficients', 'The fixed seed has only relevant inputs and I(f)>0; C fixed before r tends to infinity', 'B_i=H(S_i|S_-i), delta=H-CI, sigma_i=average_b(CI(child)-H(child))', 'Eligibility means sigma_i>=0; the limiting data-only minimum assertion requires strict positivity of every original seed average child slack', 'The finite example is the actual three-bit one-point defect padded by nine coordinates and flipped at physical zero; no minimal-violator hypothesis is asserted']
statement+=' Moreover, with Q_C(f)=min_i [B_i(f)+max(-sigma_i(f),0)]/Inf_i(f), Q_C(F_N) tends to Q_C(f) for every fixed violating seed, with no seed-child positivity assumption; every dummy corrected price is asymptotic to delta(f)*2^(N-1) and diverges.'
claim={'claim_id':'A005-POINT-EDIT-CHILD-ELIGIBILITY-OBSTRUCTION','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['fleet05/A005'],'proof_source':['DERIVATION.md Signed-child eligibility section','out/WITNESS_VALIDATION.json','out/DIRECT_VALIDATION.json'],
 'proof_dependencies':[{'claim_id':'A061-ARBITRARY-CORE-EDIT-ADMISSION','version':1,'scope':'Independent reconstruction of B-minimum limit and H/I continuity; original all-lambda/D statement not adopted as independently accepted here.'}],
 'review_records':[],'status':'SOURCE_COMPLETE_SCOPED_COROLLARY_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['For every full-Fourier-support Boolean function with max_i Inf_i<1/4 and H>(8/3)I, a coordinate with B_i/Inf_i<=5/2 and average child slack>=0 exists.'],
 'first_unproved_line':None,'next_consumers':['B01','A002','A003','A061','A064','A087','A094','B20']}
write('CLAIMS.json',[claim])
valid=[json.loads((ROOT/'out'/f'{m}_VALIDATION.json').read_text()) for m in ['PILOT','FULL','WITNESS','DIRECT']]
count=sum(v['assertions'] for v in valid)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B01','packet_id':'A005','gap_id':'C018-SAME-PARAMETER-LOCALIZATION','attempt_id':'A005-STAGE3-POINT-EDIT-CHILD-ELIGIBILITY','method':'Consume A061 source; reconstruct point-edit erasure ledger; derive signed physical-child eligibility and exact counterexample',
 'mathematical_delta':'All dummy cheap witnesses eventually have negative average child slack for any fixed violating seed; charging its negative part preserves the corrected minimum Q_C under full-support admission. Exact weak-influence counterexample separates cheap root and child-certified selection at C=8/3,K=5/2. A061 already owned the uncorrected price clamp; it is not claimed anew.',
 'deliverable_status':'COMPLETE','mathematical_status':'SCOPED_OBSTRUCTION_PROVED_FULL_FEI_OPEN','claim_versions_used':['A061-ARBITRARY-CORE-EDIT-ADMISSION@1','A005-CHILD-CERTIFICATION-ADMISSION-OBSTRUCTION@1 (context only)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['out/SOURCE_MANIFEST.json','DERIVATION.md','out/PILOT_VALIDATION.json','out/FULL_VALIDATION.json','out/WITNESS_VALIDATION.json','out/DIRECT_VALIDATION.json'],
 'next_consumers':claim['next_consumers'],'next_action':'Referee a noncircular bound paying the selected coordinate negative child slack or complete terminal deficit once; reject root-only cheap-witness admission as a substitute.',
 'stagnant_substantive_attempts':0,'blockers':['No universal signed-child or terminal payment is supplied. Same-constant universal localized implication remains open. Independent external review and supervisor mirrors pending.'], 'packet_ids':['A005']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# A005 stage 3: cheap root witnesses fail child eligibility

## exact target, quantifiers, hypotheses and units

Referee admission from arbitrary Boolean seeds into full Fourier support plus weak coordinate influences, retaining the witness needed for induction. Entropy is in bits; B_i=H(S_i|S_-i), sigma_i=average_b[CI(child)-H(child)]. The new scoped claim is {claim['claim_id']}@1: for any fixed violating seed at C, every added-coordinate witness from point surgery eventually has negative average child slack. The finite endpoint with max Inf_i<1/4, C=8/3 and price K=5/2 is false even under full Fourier support. This is not a disproof of FEI at an unrestricted absolute constant or of the lead's universal localization implication.

## sources actually read, revisions and theorem locators

Execution protocol revision 2026-10-11-execution-v2, fully reread; BOARD.md header 2026-10-13 23:59 UTC; B01 STREAM_NOTES v1, 2026-10-11 22:40Z; own stage-2 STATUS and LEARNED. Original stage-3 reports consumed: A002 correlated-tag admission obstruction, A003 sliced-majority prefix, A072 guarded six-bit admission, A090 aggregate tail completeness/zero selectable parity witness. A061 PADDING_EDIT_PROOF Sections 1--5 and CLAIMS.json, claim A061-ARBITRARY-CORE-EDIT-ADMISSION@1, are decisive. SOURCE_MANIFEST.json records exact bytes and SHA256. Preliminary scans of A002/A067/A080 reports are navigation only. No claim that the papers or old campaign plans were freshly reread this stage.

A061 already proves all-core local limits, minimum-price clipping, and retained terminal deficit. The preliminary derivation independently reconstructed the B ledger before finding that source; DERIVATION explicitly corrects priority. Those limits are not a new A005 claim. The new contribution is the signed-child eligibility corollary, its finite quantifier-level endpoint obstruction, and its linkage to the prior fixed-gap child-certified admission obstruction.

## complete derivation or exact first unsupported line

DERIVATION.md supplies exact coefficient and erasure formulas and then the signed-child proof. Along any added coordinate, one physical child is the clean padded seed and the other is its one-point surgery in one fewer dimension. Consequently sigma_j=-(delta(seed)+delta(F_(N-1)))/2 tends to -delta(seed). Old child slacks converge to their seed values. Strictly positive seed average slacks therefore force all eligible directions to be old ones for large padding, and the eligible minimum tends to E(seed), whereas the unrestricted minimum tends to min(E(seed),2).

The actual N=12 function has coefficients 1537/2048 once, -511/2048 seven times, and 1/2048 4088 times. Its influence is 771/1024, with three old influences 511/2048 and nine added influences 1/2048. Exact interval signs prove H-(8/3)I>0; every old average child slack is positive and its erasure ratio exceeds 5/2; every added slack is negative and its erasure ratio is below 5/2. Both added children violate C=8/3. Old children have signs zero and positive, so this finite example also separates individual-child eligibility. All 4096 Fourier coefficients are nonzero. More generally the corrected selectable price Q_C=min_i[B_i+max(-sigma_i,0)]/Inf_i IS preserved by this admission for every fixed violating seed: old prices converge, while every dummy corrected price is asymptotic to delta(seed)*2^(N-1) and diverges. This is a transport theorem for the explicit debt-corrected endpoint, not a bound on that endpoint.

The first unsupported universal line: pay the selected cheap witness's negative child slack (or the full retained terminal deficit), or admit into genuinely child-certified roots while retaining a fixed violating ratio. Neither full support nor strict weak influence supplies that payment. The example has uncertified added children and is not a minimal violator. The earlier all-child-certified dimension obstruction remains unchanged. A061's full multi-quantity theorem is author-proved; this stage reconstructs its B/H/I subset without asserting independent acceptance of every lambda/D dependency.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs are FROZEN_SPEC.json, FULL_RETRY_SPEC.json and INDEPENDENT_RECONSTRUCTION_SPEC.json. Commands, from A005: `python -X utf8 runs/{run}/code/check.py pilot`, followed by `.../code/check.py full`, `.../code/check.py witness`, and `.../code/direct.py`. Pilot covers 44 labelled seed/padding cases; full covers 556 cases (all 278 seeds in dimensions zero through three, each with two or three dummy bits). There is no symmetry quotient. These verify every Fourier coefficient, full support, Parseval, entropy grouping, physical influences and every coordinate erasure identity using integer Walsh and rational log-prime arithmetic. The initial full helper exceeded its frozen runtime and failed its final guard; no assertions from that attempt are counted. out/FULL_V1_OVERRUN.md preserves this compute-rule failure. A separately frozen retry memoized scalar expressions and added an in-loop deadline, then passed the unchanged domain in under two seconds.

The finite witness uses exact permutation classes and rational logarithm enclosures from a 40-term positive atanh series with a proved geometric tail, rounded outward to 2^-48. Direct reconstruction checks all 4096 physical values, all root coordinates and complete physical-child spectra for one representative of each coordinate class. This is an independent representation within A005, not external independent review. Total {count} passing assertions; all four output files report zero failures. Observed runtimes: {', '.join(v['mode']+': '+str(round(v['elapsed_seconds'],4))+'s' if 'mode' in v else 'direct: '+str(round(v['elapsed_seconds'],4))+'s' for v in valid)}. Jobs were fixed below 80 MB estimated memory, so the >300 MB memok trigger did not apply. No dimension escalation or heavy job.

## proof dependencies and changed downstream conclusions

A061 owns the already-proved price clamp and terminal ownership. Elementary physical restrictions plus that continuity yield the new eligibility limit; no universal FEI premise is used. The exact finite obstruction is checked from actual truth tables. A090's aggregate hardness with a zero parity witness explains why aggregate and selectable prices must stay separate; A002's correlated-tag no-go does not repair signed child slack. The new consequence is specific: the apparent cheap root admission cannot be upgraded to a certified-child selection at (C,K)=(8/3,5/2). Universal same-parameter localization and the C018 erasure bound remain open.

## one next mathematical action and independent reviewer

Next: audit a source-owned universal signed-child or terminal payment that explicitly retains the selected witness's descendant deficit once. At a root the exact identity delta+sigma_i=B_i+JS_i-C Inf_i exposes that charge; omitting sigma_i is invalid here. Ask A061/A087 to reconstruct the eligibility corollary and A094/A002 to check the endpoint quantifiers and the distinction from minimal violators. These are artifact handoffs only, with no messages or other-folder writes. This consumes a new source dependency rather than repeating the now-closed point-edit limit.

## actual persistence receipts or precise save blocker

All requested run files, code, three frozen specifications, proof, four exact outputs and manifests are saved inside this run. PROGRESS.json and PACKET_DELTA.json are identical with packet_ids=[A005]. STATUS.md is two lines; WORKLOG.md appended and LEARNED.md updated. All files are below 20 MB. out/PERSISTENCE_RECEIPT.json records paths, sizes and hashes after generation. Shared indices, external review, supervisor mirroring and downstream adoption were not performed or claimed. No save blocker.

**Universal bridge:** C018 localized erasure selection now has an exact signed-child admission obstruction: all new price-two directions in one-point full-support hardening fail child eligibility for any fixed violating seed, and a fully checked 12-bit weak-influence function refutes certified-child price-5/2 selection at C=8/3. Admission does preserve Q_C, the price corrected by negative child slack, identifying the universal endpoint whose bound is still unpaid. No universal FEI constant is improved. The precise unpaid term is the selected direction's negative descendant slack or the retained core's terminal deficit; NEXT is to referee its noncircular payment, because root-only full-support admission is already understood and cannot close that universal obligation.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A005 stage3 complete: source-owned A061 price clamp consumed; exact full-support weak-influence cheap witnesses fail child eligibility; '+str(count)+' assertions PASS; FEI OPEN.\nNEXT: A061/A087/A094 review signed-child eligibility; demand noncircular selected negative-slack or terminal payment; no repeat of root-only point-edit admission.\n',encoding='utf-8')
if run not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'):
    with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write('\n'+now+' stage3 '+run+': read new board and lead; preliminary clamp reconstruction superseded by A061 source ownership; pivoted to signed-child eligibility. Exact root/child certificate at N12,C8/3,K5/2 and exhaustive 556 cases passed; '+str(count)+' total assertions. New scoped source-derived corollary, external review pending; universal payment open.\n')
if 'Stage3 corrected-price transport' not in (AGENT/'LEARNED.md').read_text(encoding='utf-8'):
    with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write('\nStage3 corrected-price transport: for every fixed seed with H-CI>0, Q_C=min_i[B_i+max(-sigma_i,0)]/Inf_i is preserved in the point-edit full-support limit. Dummy corrected prices grow like delta(seed)*2^(N-1), while all old prices converge. No universal Q_C bound is proved.\n')
if 'stage3 corrected-price transport' not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'):
    with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write('\n'+now+' stage3 corrected-price transport: added arbitrary-violating-seed Q_C admission proof after the finite eligibility certificate; no seed-child strict positivity needed for Q_C. Preserved full-v1 overrun, successful memoized retry and pending external review.\n')
protocol=json.loads(source_paths[0].read_text(encoding='utf-8-sig'));pf=[p.split(' (')[0] for p in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pf);assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']+[AGENT/f for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
write('out/PERSISTENCE_RECEIPT.json',{'saved_at_utc':now,'schema_check':'PASS','packet_delta_identical':True,'external_review':'PENDING','mirrors':'NOT_PERFORMED_BY_A005','assertions':count,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files]})
print(json.dumps({'run':run,'assertions':count,'schema_check':'PASS','receipt_files':len(files)}))
