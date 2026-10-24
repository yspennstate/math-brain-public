import datetime as dt,hashlib,json
from pathlib import Path

R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11')
BASE=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT=Path(r'~\brain_workers\FEI100_20261011\context')
OLD=R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions'
def readj(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
now=dt.datetime.now(dt.timezone.utc).isoformat()
cert=readj(R/'out/CERTIFICATE.json');one=readj(R/'out/ONE_BIASED_CERTIFICATE.json');direct=readj(R/'out/DIRECT_CERTIFICATE.json');lean=readj(R/'out/LEAN_RESULT.json')
assert all(c['status']=='PASS' for c in (cert,one,direct))
assert cert['structured_cases']==7 and cert['all_two_bit_ordered_child_pairs']==256 and one['cases']==8 and direct['full_activation_cases']==12
files=[PROTO/f for f in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
files += [BASE/f for f in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
files += list((BASE/'sources').glob('*.md'))+list(CONTEXT.glob('*.txt'))
files += [Path(r'~\AGENTS.md'),HOME.parents[1]/'BOARD.md',HOME.parents[1]/'claude/B04/STREAM_NOTES.md',OLD/'REPORT.md',OLD/'CLAIMS.json',OLD/'PROGRESS.json',OLD/'code/check_exposure.py']
# Resolve the campaign root from the explicitly supplied path, independent of nesting depth.
files=[p for p in files if p.exists()]
receipts=[]
for p in files:
 b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'read_scope':'full byte provenance read; mathematical excerpts and theorem locators specified in REPORT.md'})
dump(R/'out/SOURCE_RECEIPTS.json',receipts)
statements=[
('A019-FORCED-BIASED-EMPTY-ROW-DEBT',
 'For every integer k>=2 let epsilon=2^-k, E=1[v=0] on k uniform bits, and hplus=(1-E)u+E, hminus=(1-E)u-E. Supply Qb=(Pb+delta_empty)/2 and the actual conditional queried-frequency lift of their average as incoming Qh. Activate with the fixed nonlinear two-bit mask s of mean1/2 and exact flat reference Qs. Both children are nonconstant, have means +/-epsilon and identical squared spectra, and disagree with probability epsilon. The exact net reference surcharge Lambda=average Dchild-Dparent-Dcore/2 equals D_(1/4)(epsilon^2,(1+epsilon^2)/2), lies strictly between1/32 and1/8, and tends to (1/2)log2(9/8). For h0=u,h1=(1-E)u+E, disagreement epsilon/2 and one child balanced, the same prescribed reference surcharge tends to (1/2)log2(18/17)>0, with Dcore=(epsilon^2/2)log2((2+epsilon^2)/(1+epsilon^2)). Thus no finite K universally bounds Lambda by K times disagreement even with one balanced child and both children nonconstant.',
 ['Uniform Boolean physical cubes; entropy and KL in bits','Fixed specified incoming core conditional lift; supplied contaminated child references','Fixed exact nonlinear two-bit mask reference; no support substitution','Integer k>=2; limits are k->infinity'],[]),
('A019-OWNED-EMPTY-REFERENCE-PAYMENT',
 'For arbitrary Boolean core children with supplied finite complete references Qb satisfying Pb(empty)<=Qb(empty), the same exact nonlinear two-bit mask reference, and the prescribed incoming parent conditional lift, put A0=average Qb(empty), cb=CE(Pb,Qb), and sbar=average(K I(hb)-cb). The exact signed activation-reference surcharge obeys Lambda<=1/2 log2(1+A0/4). Given already-booked U>=0, if sbar>=2U+log2(1+A0/4), its positive part is paid from the same remaining original half-core bank sbar/2-U, retaining both complete activation child terminals and the core entropy decrement. In the explicit opposite-mean family of the preceding claim at K=4, after any old booking 0<=U<=1/8, more than1/4 remains after paying Lambda; in the one-balanced-child family more than3/4 remains for k>=2. No new core or mask reference is substituted.',
 ['Both supplied references normalized with finite complete cost','Empty core true mass dominated by empty supplied reference mass in each child','Qs=Ps for the nonlinear two-bit mask, so Qs(empty)=(E s)^2=1/4','Incoming parent core reference is the specified conditional lift before querying','Any existing bookings are explicitly deducted from the same original bank'],[])
]
protocol=readj(PROTO/'EXECUTION_PROTOCOL.json')
claims=[]
for cid,statement,hyp,deps in statements:
 claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A019 account03'],'proof_source':{'path':str(R/'REPORT.md'),'derivation':str(R/'out/DERIVATION.md'),'certificates':['out/CERTIFICATE.json','out/ONE_BIASED_CERTIFICATE.json','out/DIRECT_CERTIFICATE.json']},'proof_dependencies':deps,'review_records':[],'status':'ANALYTIC_PROOF_AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Universal Lambda<=K*d for the specified inherited core-reference hierarchy'] if cid.endswith('DEBT') else [],'first_unproved_line':None,'next_consumers':['A018','A020','A092','A094']}
 assert set(claim)==set(protocol['required_per_run']['claim_fields']);claims.append(claim)
dump(R/'CLAIMS.json',{'claims':claims})
oldp=readj(OLD/'PROGRESS.json')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B04','packet_id':'A019','gap_id':oldp['gap_id'],'attempt_id':'A019-stage17-forced-biased-empty-row','method':'Exact incoming-reference calculation, explicit Boolean sparse families, one owned terminal-bank payment, direct Walsh reproduction','mathematical_delta':'Removes one balanced-child assumption in explicit unbounded family; forced positive limiting Lambda with exact source-bank payment; conditional arbitrary-core empty-row domination payment. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_CHECKED_PROOF_AT_STATED_SCOPE; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':[{'source':str(OLD/'REPORT.md'),'scope':'exact CE insertion and carried-reference conventions reconstructed explicitly'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1} for c in claims],'source_artifacts':['REPORT.md','CLAIMS.json','out/DERIVATION.md','out/FROZEN_SPEC.json','out/ONE_BIASED_SPEC.json','out/DIRECT_SPEC.json','out/CERTIFICATE.json','out/ONE_BIASED_CERTIFICATE.json','out/DIRECT_CERTIFICATE.json','out/LEAN_RESULT.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A018','A020','A092','A094'],'next_action':'Expose one v-coordinate in the one-balanced-child construction with the ORIGINAL references, booked U<=1/8 and paid Lambda retained; certify the actual inherited child references against the SAME remaining >3/4 bank, retaining the opposite terminal.','stagnant_substantive_attempts':0,'blockers':['No arbitrary-core bank-eligibility invariant through subsequent data queries','Independent review and supervisor copying pending','Full entropy theorem not Lean-formalized; see exact core side-check disposition'],'packet_ids':['A019']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
derivation=(R/'out/DERIVATION.md').read_text(encoding='utf-8')
report=f'''# A019 stage17: forced biased empty-row debt, paid from one original bank

Full FEI remains OPEN. The saved balanced-child reference repair does not extend continuously to unequal means: a genuinely essential sparse query has fixed positive net reference surcharge. Its specified rate4 terminal references contain enough original unused slack to pay that debt once, including an old debit. This closes the requested explicit structured low-disagreement case. Independent review is pending; there is no priority or literature-novelty claim.

## exact target, quantifiers, hypotheses and units

Uniform finite physical cubes, Boolean signs, entropy/KL/complete reference costs in bits. All k are quantified as integers>=2 unless the finite k1 boundary check is explicitly named. The hypotheses and exact statements are in CLAIMS.json. Q denotes an actual normalized complete reference, not a spectral conditioning surrogate. Both activation child terminals are retained. No result here constructs references for arbitrary Boolean cores.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision {protocol['revision']} was read in full. Current user deadline 2026-10-23 14:49UTC takes precedence over the historical Oct21 endpoint in the static protocol. BOARD snapshot2026-10-22 22:17UTC, B04 STREAM_NOTES v2 and its appended private-query empty-row repair, STATUS/LEARNED, and own stage5 REPORT sections1-6 supply the precise frontier. The latest saved STATUS still points to stage5; no superseding own proof was consumed. Static campaign README, status, registries, packet and next-action files, campaign plan and supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING are navigation sources; only their B04/C019/C024 and reference-ownership interfaces are used. Hash/byte receipts distinguish provenance reads from inspected mathematical excerpts.

Threshold38pp Proposition8.6 equations75-79 and Corollaries8.7-8.8 were inspected: the shared-data identity and max(2/c,C) closure are baseline, not this result. Threshold theorem statements, earlier threshold version, percolation30pp Theorems1.1-1.6 and earlier extension version were inspected for scope; no percolation theorem is a proof dependency. Supplemental ISOSPECTRAL_SPLICING_CURATED section2 fixes the physical restriction convention. The bent-splice falsifier is imported from OBSTRUCTION_REGISTRY O-BENT-SPLICE and the actual sparse-bent construction in COUNTEREXAMPLES X003: arbitrary magnitude-changing branches do not acquire a selector-only price. This stage concerns prescribed complete reference costs, not a purported repair of that false universal local entropy price. Math recall gave the same local-induction warning and no bank-eligibility theorem; its cards are leads, not proof inputs. No external novelty claim is made.

The prior byte-pinned exposure helper supplies only exact arithmetic and the established full activation reference implementation. Its normalized-text hash in the checker output and raw source-byte hash in SOURCE_RECEIPTS are different provenance conventions, not interchangeable source pins. The direct reproduction does not call its fast Walsh transform or gate helper.

## complete derivation or exact first unsupported line

For completeness, define eta(z)=-z log2(z), eta(0)=0, and
Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+1-mu^2-eta(mu^2)/2.
For F=1 at x0 and h*s at x1, the data mixture is (P_h tensor P_s+delta_empty)/2. Its complete reference is (Q_h tensor Q_s+delta_empty)/2 lifted by the actual conditional selector-frequency law. Directly the nonempty data coefficients are hhat(T)shat(U)/2 in each selector frequency; the empty coefficients are (1+mu)/2,(1-mu)/2. Entropy chain rule and binary log-sum therefore give
CE_F=(c_h+2)/2+Psi(beta/2)-D_(1/4)(beta^2,Q_h(empty)).
The exact posterior-label refund is the scalar D in the derivation below, including continuous zero cases. For a core query the supplied parent lift gives c_parent=average c_child+Delta H_core-D_core, D_core>=0 by log-sum. Substitution gives the FULL insertion
Delta CE_F=Delta H_core/2+profile_curvature+Lambda,
Lambda=average D_child-D_parent-D_core/2.
Neither the average child refunds nor the full child terminal costs can be dropped. The prior sharp profile curvature bound is retained as a separate term, not paid again from the terminal bank.

{derivation}

The first unsupported universal line is preservation/eligibility of this SAME unused source bank and these SAME references after a further physical data query. Empty-reference domination and the required original slack are hypotheses with explicit owners, not general theorems about all Boolean functions. A fixed known family remains a proper-class result; finite data do not establish full FEI.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede each job. All commands run inside A019 with python -X utf8; no GPU, automatic dimension growth, detached work or >300MB search was used. Estimated memory was60-100MB, not measured peak RSS. Each mathematical checker has a60second internal cap. Shell startup delays on the shared machine are excluded from checker timings.

code/check_biased.py --pilot: PASS,1 case,{readj(R/'out/PILOT.json')['checks']} assertions. Full code/check_biased.py: PASS,7 all-k-family instances k2..8 plus ALL256 ordered two-bit child pairs, {cert['checks']} exact assertions, {cert['seconds']:.6f}seconds. Supplementary pairs include equal children, constants, opposite signs, zero means and nonzero means; there is no symmetry quotient. Integer comparisons 145^4<2*128^4 and72^65>2^7*65^65 certify the uniform logarithmic bounds. Walsh coefficients, normalization, support, KL conservation, full reference insertion, entropy/influence identities and the prior-debit bank deductions are exact.

code/check_one_biased.py: PASS,{one['cases']} cases k1..8,{one['checks']} assertions,{one['seconds']:.6f}seconds. k1 is explicitly a finite boundary check, not used in the k>=2 bank proof. code/check_direct.py: PASS,{direct['full_activation_cases']} full activation spectra by literal character summation,{direct['checks']} assertions,{direct['seconds']:.6f}seconds. This separately checks the complete reference atoms and scalar refund, rather than just repeating a fast transform.

Exact log expressions use rational prime coefficients. Log signs use range-reduced36-term rational atanh sums and rigorous geometric tails, with symbolic cancellation of exact zero forms. The all-k statements follow the analytic derivation and inequalities above, not the finite range. Lean core side-certificate attempt: {json.dumps(lean,ensure_ascii=False)[:1800]}. Full entropy/reference mathematics is author-checked analytic proof, not Lean-checked. No compiler failure or admission hold is treated as a mathematical counterexample.

## proof dependencies and changed downstream conclusions

Both claims are source-complete at stated scope with no dependency on a proposed universal FEI lemma. Elementary Fourier expansion, entropy chain rule, binary log-sum and concavity are reconstructed above. The earlier profile bound is retained unchanged and is not needed for the separate Lambda payment. Source-bound prior A018/A020 acceptance is historical, not independent review of this stage. This stage gives A018/A020/A092 a forced-support guard that survives the old absent-query convention, plus the exact named source of payment. It does not lower a universal FEI constant or reclassify max(2/c,C) as progress.

## one next mathematical action and independent reviewer

{progress['next_action']} A018 and A020 should independently reconstruct the full reference atoms and the one-balanced-child limit; A092/A094 should challenge original-bank ownership and the retained child costs. No remote message or shared registry mutation has been performed.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA are saved locally with code, frozen specs, certificates and source receipts. Rolling STATUS remains two lines; dated WORKLOG and LEARNED receive this mathematical delta. The finalizer validates all protocol field sets, claim digests, complete file size limits and local SHA256 receipts. Supervisor copying, remote mirror verification, downstream use and independent review are pending; local saves do not imply them.

## Universal bridge

This stage moves C024 inherited-reference transfer and B04's C019 stopping-tree payment interface by removing one balanced-child assumption in an explicit unbounded family: the FORCED true-row contrast has limiting net debt (1/2)log2(18/17), and the SAME original half-core terminal bank pays it once after an old debit<=1/8 while retaining>3/4. A conditional arbitrary-core bound prices positive Lambda by original empty reference mass when domination and source-slack eligibility hold. No universal constant improves. What remains is preservation of that eligibility and unused owner through an actual further data exposure; NEXT is the shortest route because it exercises the surviving original source rather than inserting a fresh reference or proving another already-covered class bound.
'''
(R/'REPORT.md').write_bytes(report.encode('utf-8'))
marker=f'A019 stage17 {R.name}'
entries={
 'WORKLOG.md':f'\n## {now} — {marker}\nRead B04 frontier and protocol. Derived forced positive empty-row surcharge with opposite means and one balanced child; proved explicit original-bank payment with old U<=1/8 retained. Main {cert["checks"]}, one-biased {one["checks"]}, direct {direct["checks"]} exact assertions PASS. Full FEI OPEN, independent review pending. Lean disposition saved separately. NEXT: one v-query with unchanged references and remaining original bank.\n',
 'LEARNED.md':f'\n## {now} — {marker}\nA true positive folded empty row removes zero-row reference freedom. For hplus/minus=(1-E)u +/-E with epsilon=2^-k, supplied Qb=(Pb+delta_empty)/2 forces Qparent(empty)=0 and Dcore0; Lambda tends to half log2(9/8) and is in(1/32,1/8) for all k>=2. With h0=u,h1=(1-E)u+E, only one child is biased, Qparent(empty)=(2+epsilon^2)/8, Dcore=(epsilon^2/2)log2((2+epsilon^2)/(1+epsilon^2)), and Lambda tends to half log2(18/17). These rule out a local K*d reference price, not FEI. For exact nonlinear mask and Pb(empty)<=Qb(empty), Lambda<=half log2(1+average Qb(empty)/4). Explicit K4 original half-core banks pay Lambda_+ once after old U<=1/8, retaining>1/4 (opposite) or>3/4 (one balanced). General bank eligibility after another query remains unpaid.\n'}
for name,entry in entries.items():
 p=HOME/name;b=p.read_bytes() if p.exists() else b''
 if marker.encode() not in b:p.write_bytes(b+entry.encode('utf-8'))
(HOME/'STATUS.md').write_bytes(('STATE: A019 stage17 author proof: forced biased empty-row debt paid from SAME original K4 core bank, old U<=1/8 retained; main/one-biased/direct exact checks PASS; independent review pending; FEI OPEN.\nNEXT: A018/A020/A092/A094 review; expose one v-coordinate with ORIGINAL references, paid Lambda and old U retained, both full terminals, SAME remaining >3/4 bank.\n').encode())
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(len(p.read_bytes())<20_000_000 for p in R.rglob('*') if p.is_file())
for f in protocol['required_per_run']['report_fields']:assert '## '+f in report
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C024')
manifest=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_utc':now,'files':manifest,'protocol_fields':'PASS','claim_digests':'PASS','delta_identical':True,'remote_mirror':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps({'status':'PASS','claims':len(claims),'main_checks':cert['checks'],'one_biased_checks':one['checks'],'direct_checks':direct['checks'],'run':str(R),'full_fei':'OPEN'}))
