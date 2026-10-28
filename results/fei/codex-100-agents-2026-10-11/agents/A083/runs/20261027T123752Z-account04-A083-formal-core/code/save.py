from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def write(n,d):(R/n).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
root=Path('~/brain_workers/FEI100_20261011')
peer=root/'agents/A097/runs/20261027T092641Z-account04-A097-cross-route-transfer'
claim_source=json.loads((peer/'CLAIMS.json').read_text(encoding='utf-8-sig'))[1]
assert hashlib.sha256(claim_source['exact_statement'].encode()).hexdigest()==claim_source['statement_sha256']
paths=[root/'BOARD.md',root/'claude/B17/STREAM_NOTES.md',peer/'PROOF.md',peer/'CLAIMS.json',root/'agents/A012/runs/20261027T062634Z-account04-A012-sparse-activation-accounting/DERIVATION.md',root/'agents/A033/runs/20261027T105244Z-account04-A033-derivative-hierarchy/PROOF.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),A/'runs/20261026T201649Z-account04-A083-formal-core/REPORT.md',A/'runs/20261026T201649Z-account04-A083-formal-core/out/SOURCE_RECEIPTS.json']
write('out/SOURCE_RECEIPTS.json',[{'path':str(p),'raw_sha256':digest(p),'bytes':p.stat().st_size} for p in paths])
result=json.loads((R/'out/CHECK_RESULT.json').read_text(encoding='utf-8'))
formal=json.loads((R/'out/LEAN_RESULT.json').read_text(encoding='utf-8'))
assert result['status']=='PASS'
stmt='For every even n>=4, the actual Boolean product of n/2 disjoint two-bit signs negative only on pair(+,+), with A097 parity-face reference Q and epsilon=2^(-4n), has uniform squared spectrum P, H=n,I=n/2,Inf_i=1/2,CE(P,Q)<4I, exact vacuum calibration and every marginal through order n-2 matched. For all i<n, projection loss L_i=D=n-(1/4)log2(2-epsilon). For i=n, L_n=D-(1/2)log2(4/((3-epsilon)(1+epsilon))), and this is the strict minimum over all coordinates: n-1/2<min_i L_i<n and 2n-1<min_i L_i/Inf_i<2n. Both physical children have CE=n-1+d_i, d_i=0 except the positive displayed tail divergence. No dimension-independent existential first-coordinate L_i<=K Inf_i follows from these matching and source hypotheses; FEI is not refuted since H/I=2.'
c={
 'claim_id':'A083-ALL-COORDINATE-HIGH-MOMENT-QUERY-LOSS','version':1,'exact_statement':stmt,
 'hypotheses':['Every even n>=4; finite uniform Boolean cube; bits','Explicit strictly positive normalized A097 face reference, tail coordinate n, epsilon=2^(-4n)','Loss is KL contraction under spectral deletion, not unspecified inheritance or a fresh child source','All physical outcomes, remaining terminal mismatch, old bills and original capacity retained'],
 'statement_sha256':hashlib.sha256(stmt.encode()).hexdigest(),'contributors':['A083'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':digest(R/'PROOF.md'),'formal_status':formal['status'],'formal_scope':'Finite n4 rational face/projection formulas and16/9<2 only; no all-n or entropy kernel claim'},
 'proof_dependencies':[],
 'review_records':[{'source_claim':'A097-HIGH-MOMENT-MATCHED-QUERY-LOSS','source_version':1,'source_statement_sha256':claim_source['statement_sha256'],'reviewer':'A083','verdict':'HOLDS unchanged at original i<n scope','basis':'Independent direct character sums, all proper marginals and rational likelihood certificates; analytic rederivation, no peer helper imports','extension_scope':'Tail-coordinate strengthening is new here and pending separate independent review; no claim to novelty of the parity construction'}],
 'status':'ANALYTIC_PROOF_EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':[{'statement':'There exists an absolute K such that every normalized covering reference with CE<=4I, matched vacuum and all marginals through order n-2 has some coordinate i with L_i<=K Inf_i','witness':'Explicit f_n,Q_n for every even n>=4: all ratios>2n-1','scope':'Supplied-reference local-payment interface only; neither FEI nor the globally paid projection-history theorem is refuted'}],
 'first_unproved_line':'Construct a useful noncircular O(I) original source for arbitrary Boolean cores or pay required productive-interface full query losses from SAME unused original capacity after all old bills and both full terminals.',
 'next_consumers':['A097','A012','A033','A096','A094','A011','A050','B20']}
write('CLAIMS.json',[c])
p={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083','gap_id':'C024-ORIGINAL-SOURCE-QUERY-KL-PAYMENT','attempt_id':'A083-stage22-all-coordinate-tail-certificate',
 'method':'Independent A097 review plus exact tail erasure formula, all-coordinate analytic obstruction and finite direct-Walsh/rational likelihood certificates',
 'mathematical_delta':'Extends A097 i<n obstruction to EVERY coordinate: exact tail loss min_i L_i>n-1/2, so min_i L_i/Inf_i>2n-1. Complete both-child CE and actual influence account retained; no universal constant improves.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A097-HIGH-MOMENT-MATCHED-QUERY-LOSS@1'],'claims_created_or_changed':[c['claim_id']+'@1'],'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','code/check.py','out/CHECK_RESULT.json','code/Face.lean','out/LEAN_RESULT.json','out/SOURCE_RECEIPTS.json'],'next_consumers':c['next_consumers'],
 'next_action':'A097/A033/A094 review the tail formula and both-child accounting. Replace high-moment local selection by an ORIGINAL complete arbitrary-core O(I) source or a productive selected interface paid globally, preserving full query KL and terminal mismatch.',
 'stagnant_substantive_attempts':0,'blockers':['Universal original-source supplier and required productive interface unpaid','Formal checking subject to saved admission result; finite draft does not certify analytic theorem','External review, supervisor mirror and downstream adoption unverified'],'packet_ids':['A083']}
write('PROGRESS.json',p);write('PACKET_DELTA.json',p)
count=result['exact_assertions'];sec=result['seconds']
report=f'''# exact target, quantifiers, hypotheses and units

Independently review A097-HIGH-MOMENT-MATCHED-QUERY-LOSS@1 and close its omitted tail coordinate. For EVERY even n>=4, the same actual Boolean function and strictly positive supplied reference satisfy n-1/2<min_i L_i<n, hence min_i L_i/Inf_i>2n-1. Bits; full spectral projection convention, matched vacuum/all marginals through n-2, original CE<4I, BOTH physical children and remaining terminal divergence. This rules out existential first-coordinate local payment under those hypotheses; it does not refute FEI.

# sources actually read, revisions and theorem locators

Current BOARD, unchanged B17 notes v2, own stage21 STATUS/report, protocol-v2, A097 stage22 PROOF sections3-4 and named CLAIMS, A033 stage22 PROOF section5 and A012 stage22 DERIVATION sections1-6 read. Actual bytes are pinned in out/SOURCE_RECEIPTS.json. Earlier baseline campaign, registries and four manuscript texts retain stage21 byte provenance; they are not new proof premises or re-audited literature. A097 explicitly consumes our derivative-t erratum; no old source was rewritten. The high-moment source is already independently reconstructed by A033 at its original scope; this stage adds the still-omitted tail calculation, not another copy of that scope. No external literature priority or new parity construction is claimed.

# complete derivation or exact first unsupported line

PROOF.md gives the complete all-n finite-law argument. Root D=n-(1/4)log2(2-e), e=2^(-4n). For i<n, erased reference is uniform and L_i=D. For the tail, projected masses are(3-e)/2^n and(1+e)/2^n, so d=(1/2)log2(4/((3-e)(1+e))) lies strictly between0 and1/4. Exact16/9<2 supplies the bound, so L_n=D-d is the strict minimum and exceeds n-1/2. EVERY possible first physical coordinate has large loss. This extends rather than changes A097's original n-1/4 lower bound, which applies to the first n-1 coordinates only. Actual child entropy is n-2; influences are n/2 and(n-2)/2, with mean(n-1)/2. Their full CE is n-1+d_i, so the CE change is exactly -1-L_i. First unsupported universal line: noncircular useful original arbitrary-core CE<=C I source or a required productive globally paid interface retaining all query losses, old bills and full terminals.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes execution: n4,6,8 only,3 roots,18 queries,36 actual children and315 marginal masks. No symmetry reduction or dimension escalation. python -B -X utf8 code/check.py: PASS {count} exact assertions in{sec:.6f}s. Direct Walsh character sums and Fraction/integer likelihood powers certify all matched marginals, exact projected laws, strict loss bounds, BOTH child CE and physical influence conservation, with no floating logarithm signs. The analytic proof supplies all even n, not extrapolation from these cases. out/DRAFT_CORRECTION.json records the pre-execution distinction between individual child influence and its mean. Formal finite n4 face/fiber source uses core rational arithmetic; its admission/checker receipt is {formal['status']}. No kernel success, transitive axiom result or all-n formalization is inferred from an unverified draft or a refused run. out/FORMAL_MEMOK.json records fresh admission; no guard was overridden.

# proof dependencies and changed downstream conclusions

A097's high-moment claim independently HOLDS unchanged. Our strengthened all-coordinate claim has a standalone proof and awaits A097/A033/A094 review. It closes a selection escape: even the tail cannot be charged at a dimension-independent local influence rate. It leaves the complete A012/A097 projection-history theorem intact because initial divergence D pays the first large loss globally. The remaining positive tail divergence d and both child CEs are retained, not set to zero. No arbitrary reference is replaced by a true-kernel reference for free, no old charge is removed and no new original capacity appears.

# one next mathematical action and independent reviewer

A097/A033/A094 independently review the tail likelihood factor and full child account. A011/A050/A096 must supply a useful ORIGINAL arbitrary-core source or productive globally paid stopping interface. High-moment calibration releases zero on this reference and ALL-coordinate selection fails; further tuning of moment order cannot replace that unpaid source. The source or policy must preserve actual full query KL, old U and terminal mismatch from the SAME unused original account.

# actual persistence receipts or precise save blocker

All four exact-schema protocol files, PROOF, independent code, frozen domain, exact output, formal source/admission result and raw source receipts saved inside A083. out/PERSISTENCE.json verifies schema keysets, compatibility equality and file hashes/sizes. Rolling STATUS/WORKLOG/LEARNED updated. Shared trees and brain remain read-only; no git, external message or other-agent mutation performed. Supervisor mirror, independent acceptance and downstream use remain unverified. No stage research job is left running. Brain self-care remains degraded/unverified: stale personal model/state/dream records affect context freshness and consolidation reliability and supply no proof premise.

Universal bridge: C024 history transfer and C019 stopping-tree payment gain an all-coordinate obstruction to replacing original query-KL payment by local influence after high-order moment calibration. The prior source excluded n-1 choices; the new exact tail formula excludes the last one, with min_i L_i/Inf_i>2n-1 while CE<4I and H/I=2. No universal FEI constant improves. What remains is the useful original O(I) arbitrary-core source or a productive globally paid interface retaining the full history and terminals. NEXT attacks that source/payment boundary because coordinate selection and even order-n-2 matching can no longer be invoked to bypass it.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A083 stage22 saved: A097 high-moment theorem HOLDS; NEW ALL-coordinate loss minL>n-1/2, minL/Inf>2n-1;{count} exact checks PASS;formal {formal["status"]};FEI OPEN.\nNEXT: A097/A033/A094 review tail/full-child formula;A011/A050/A096 supply ORIGINAL arbitrary-core O(I) source or productive globally paid interface with full queryKL/old U/BOTH terminals.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for filename,entry in [('WORKLOG.md',f'stage22: independently reconstructed A097 high-moment control and closed tail coordinate. Exact tail projected masses3-e and1+e give0<d<1/4; ALL first-coordinate losses>n-1/2. {count} exact assertions PASS on n4/6/8,315 marginals,36 children. Child influence individual/mean distinction corrected before execution. Formal {formal["status"]}; universal source/FEI OPEN.'),('LEARNED.md','Durable stage22: In A097 parity-face reference, tail deletion does NOT remove all mismatch: d=.5log2[4/((3-e)(1+e))] in(0,1/4). It is the unique cheapest coordinate, with Ltail=D-d>n-1/2. Thus EVERY coordinate has L/Inf>2n-1 despite original CE<4I and vacuum/all order<=n-2 marginals matched. Both actual children have H=n-2 and CE=n-1+d_i; influences n/2 and(n-2)/2, mean(n-1)/2. Full CE change=-1-L. Root mismatch pays globally once; local selection and moment matching alone cannot supply the universal source.')]:
 with (A/filename).open('a',encoding='utf-8') as f:f.write('\n'+stamp+' '+entry+'\n')
protocol=json.loads(paths[6].read_text(encoding='utf-8-sig'))
assert set(c)==set(protocol['required_per_run']['claim_fields'])
keys=set(protocol['required_per_run']['progress_fields']);keys.remove('packet_ids (one primary ID, for compatibility)');keys.add('packet_ids');assert set(p)==keys
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert all('# '+s in report for s in protocol['required_per_run']['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for x in R.rglob('*'):
 if x.is_file() and x.name!='PERSISTENCE.json':
  assert x.stat().st_size<20*1024*1024
  files.append({'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':digest(x)})
write('out/PERSISTENCE.json',{'status':'PASS','verified_at_utc':stamp,'schema':'exact','compatibility':'identical','source_statement_hash':'matched','local_only':True,'artifacts':files})
print(json.dumps({'status':'PASS','files':len(files),'checks':count,'formal':formal['status']}))
