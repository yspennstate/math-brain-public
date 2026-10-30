from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json, hashlib, time

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
started=time.perf_counter()
def dump(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def fac(k):
    ans={}; p=2
    while p*p<=k:
        while k%p==0: ans[p]=ans.get(p,0)+1; k//=p
        p+=1
    if k>1: ans[k]=ans.get(k,0)+1
    return ans
def vec_add(*args):
    out=defaultdict(Q)
    for scale,v in args:
        for p,x in v.items(): out[p]+=scale*x
    return {p:x for p,x in out.items() if x}
def walsh(tt):
    # Independent direct character sums, not the JS butterfly or mux formulas.
    return [Q(sum(y*(-1 if (t&x).bit_count()%2 else 1) for x,y in enumerate(tt)),len(tt)) for t in range(len(tt))]
def entropy(tt):
    out=defaultdict(Q)
    for a in walsh(tt):
        p=a*a
        if not p: continue
        for prime,k in fac(p.denominator).items():out[prime]+=p*k
        for prime,k in fac(p.numerator).items():out[prime]-=p*k
    return {p:x for p,x in out.items() if x}
def influence(tt,n):
    return Q(sum(tt[x]!=tt[x^(1<<i)] for x in range(len(tt)) for i in range(n)),len(tt))
masks=[0,255,170,150,128,232]
tables=[[(-1 if mask>>x&1 else 1) for x in range(8)] for mask in masks]
fixtures=0
for g in tables:
    for h in tables:
        f=g+h
        hf,hg,hh=entropy(f),entropy(g),entropy(h)
        L=vec_add((Q(1),hf),(Q(-1,2),hg),(Q(-1,2),hh))
        expected=defaultdict(Q)
        for a,b in zip(walsh(g),walsh(h)):
            for scale,c in [(Q(1),(a+b)/2),(Q(1),(a-b)/2),(Q(-1,2),a),(Q(-1,2),b)]:
                p=c*c
                if p:
                    for prime,k in fac(p.denominator).items():expected[prime]+=scale*p*k
                    for prime,k in fac(p.numerator).items():expected[prime]-=scale*p*k
        assert L=={p:x for p,x in expected.items() if x}
        J=Q(sum(x!=y for x,y in zip(g,h)),8)
        assert influence(f,4)==(influence(g,3)+influence(h,3))/2+J
        fixtures+=1
        assert time.perf_counter()-started<60
quadratics=[]
for n in [2,4,6,8,10,12]:
    tt=[(-1 if ((x.bit_count()*(x.bit_count()-1)//2)&1) else 1) for x in range(1<<n)]
    assert influence(tt,n)==Q(n,2)
    # Check the actual first branch product and a reached descendant; algebra covers all reaches.
    for k in [n,max(1,n//2)]:
        child=tt[:1<<k]
        product=[child[x]*child[x|(1<<(k-1))] for x in range(1<<(k-1))]
        assert influence(product,k-1)==k-1
    total=n*(n-1)//2
    quadratics.append({'n':n,'I_root':str(influence(tt,n)),'ticket_sum':total,'ratio':n-1})
    assert time.perf_counter()-started<60
independent={'status':'PASS','method':'direct truth-table mux; Fraction character sums; prime-log maps; actual quadratic edge counts','mux_fixtures':fixtures,'quadratic_cases':quadratics,'elapsed_seconds':time.perf_counter()-started,'independent_agent_review':False}
dump(R/'out/INDEPENDENT_VALIDATION.json',independent)

protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
statement='For every finite uniform cube, arbitrary Boolean G,H on the same physical data bits, and a fresh fair selector z, let F=(G+H)/2+z(G-H)/2, J=Pr(G!=H), e=GH, and L=H(F)-(H(G)+H(H))/2. Then 0<=L<=h2(J)+4J<=I(e)+4J. For every adaptive physical stopping tree the signed coherent debit equals L_root minus the reached live-terminal L values and is at most the ONE original allowance 4J_root+I(e_root)<=4I(F_root), retaining every inherited-core decrement and full actual terminal. This supplies no ownership across nested muxes. Indeed for complete quadratic Boolean f_n=(-1)^(sum_{i<j}x_i*x_j), even n>=2, the sum of newly supplied disagreement-influence tickets at all mux levels is n(n-1)/2, while I(f_n)=n/2, for any complete adaptive coordinate-order tree.'
claim={
'claim_id':'A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER','version':7,'exact_statement':statement,
'hypotheses':['finite uniform cubes, real Walsh coefficients, base-2 entropy','fresh fair selector; arbitrary overlap between Boolean branches','one explicitly allocated original source allowance; signed expected-reach ledger','both inherited branches and every actual terminal retained; no renewed bank','scalar profile and bent edit are prior work; v6 remains available under its stronger hypotheses'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A058'],
'proof_source':['PROOF.md','code/exact_mux.js','code/finalize.py','out/EXACT_VALIDATION.json','out/NESTED_OBSTRUCTION.json','out/INDEPENDENT_VALIDATION.json'],
'proof_dependencies':['author reconstruction of exact coherent Fourier rows; elementary binary entropy series, concavity and input reveal chain','v6 for comparison only; not needed in new derivation','prior profile cards claim_76e621c18b4bc9fb5327f154b1f567e583b339d4cbcd041d2453291adf7cd257 and claim_7f5f22ff912203aa5274e2ba4e216316da9392bbfda1386c6f02803c17b8e759 credited, not assumed accepted'],
'review_records':[{'reviewer':'A091','status':'PENDING; primary; no message sent'},{'reviewer':'A090','status':'PENDING; alternate; no message sent'}],
'status':'AUTHOR_PROOF_WITH_EXACT_FINITE_CHECKS; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
'supersedes':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@6 (addendum; preserves sharper common-phase theorem)'],
'refutes':['Unclaimed naive universal nested budget sum_v w_v I(G_v H_v)<=K I(F_root) for a dimension-independent K'],
'first_unproved_line':'No proof that an already diminished ancestor bank contains this new source, or that arbitrary nested overlap costs can be allocated once to root physical edges. Summing fresh disagreement tickets is explicitly false.',
'next_consumers':['A091','A090','A057','A059','B12','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
progress={
'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B12','packet_id':'A058','gap_id':'A058-NONCOLLINEAR-SAME-SOURCE-OWNERSHIP','attempt_id':'substantive-stage7-disagreement-source',
'method':'exact coherent posterior + input-output entropy source + signed original-reserve telescope; actual Boolean nested obstruction',
'mathematical_delta':'Removed common-phase restriction for ONE explicitly supplied root-owned overhead reserve. Arbitrary overlap: L<=4J+I(GH); every adaptive stopping history retains full core and terminal bills. Complete quadratics refute renewed-ticket nesting with ratio n-1. Prior split profile and bent edit credited, no novelty claimed there.',
'deliverable_status':'COMPLETE_LOCAL; supervisor copy and independent review unverified',
'mathematical_status':'single-reserve composition lemma proved by author and exactly checked; inherited depleted-source/nested universal FEI gap OPEN',
'claim_versions_used':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@6 (comparison only)'],
'claims_created_or_changed':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@7'],
'source_artifacts':['PROOF.md','FROZEN_SPEC.json','NESTED_SPEC.json','INDEPENDENT_SPEC.json','out/EXACT_VALIDATION.json','out/NESTED_OBSTRUCTION.json','out/INDEPENDENT_VALIDATION.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':['A091','A090','A057','A059','B12','B20'],
'next_action':'Keep exact existing L reserve after one actual nested split; find physical-edge ownership of only the genuinely additional collision debit. Complete-quadratic ticket sums are forbidden; preserve prior booked debit and both full terminals.',
'stagnant_substantive_attempts':0,
'blockers':['independent review pending','no ancestor-reserve allocation across arbitrary nested muxes; fresh tickets provably overcount','brain self-care degraded: stale personal notes and earlier attached-document integrity unverified; these are not proof dependencies'],
'packet_ids':['A058']}
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)

report='''# A058 stage7: arbitrary overlap, one original collision reserve

## exact target, quantifiers, hypotheses and units

Finite uniform cubes, Boolean +/-1 branches with arbitrary shared physical inputs, a fresh fair selector, entropy in bits. PROOF.md proves 0<=L=H(F)-(H(G)+H(H))/2<=4J+I(GH), J=Pr(G!=H). The SAME explicitly allocated original allowance pays the signed coherent debit of every adaptive stopping tree; both complete inherited-core bills and every actual terminal stay. This is not a certificate that an already depleted v6 source has spare money. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2; the user's extended deadline governs. Read current BOARD.md B12 entries A056-A060, review entries and source-frontier rows; own STATUS.md; B12 STREAM_NOTES.md v2 dated 2026-10-11 23:30 UTC; previous run 20261022T211410Z-fleet03-A058-overlapping-compositions/PROOF.md, sections1-7. Campaign and paper orientation from the previous stage is inherited, not presented as a fresh paper audit. The machine AGENTS.md was read for applicable boundaries. Read-only math recall returned and then walked full cards claim_76e621c18b4bc9fb5327f154b1f567e583b339d4cbcd041d2453291adf7cd257 and claim_7f5f22ff912203aa5274e2ba4e216316da9392bbfda1386c6f02803c17b8e759: the stronger split profile and bent-edit sharpness are PRIOR WORK, no novelty claimed. The proofs here reconstruct a weaker rational profile independently and do not assume those draft cards accepted. No external papers or internet claims are needed.

## complete derivation or exact first unsupported line

PROOF.md gives the coherent Fourier-row posterior r[h(v)+1-h(w)], its nonnegativity, the bound by r h(v)+4d, entropy concavity, and an input-output reveal-chain proof h(Pr(e=-1))<=I(e). These pay one named original disagreement source. The signed adaptive identity is L_root minus the true-reach live-terminal reserves, not a new bank at every node. Existing booked debit D is permitted only if the remaining original allowance U after D is at least L_root; the argument never resets U or proves this admission automatically. The complete-quadratic Boolean family proves that a newly supplied I(GH) ticket at every nested level costs n(n-1)/2 against root influence n/2. Thus the suggested naive universal summation is false. The first unsupported step is allocating genuinely new nested collision costs from the already diminished ancestor source without double ownership of physical edges. All-dimensional FEI and arbitrary inherited core payment remain open.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the exact search. code/exact_mux.js was executed in the functions.exec V8 JavaScript runtime, with the identical saved source, frozen n=3: all65,536 ordered Boolean branch pairs, no symmetry;65,536 nonnegativity,65,536 posterior-upper,65,536 disagreement-source,65,536 mass/influence checks and196,608 data identities. Total458,752 assertions PASS. Exact integer Walsh transforms and prime-log vectors at denominator512; log signs use BigInt power-certified intervals at denominator4096. Zero exact fallbacks were needed; elapsed8.042s; estimated memory below100MB, not measured. Six grouped bent-edit integer certificates PASS. out/EXACT_VALIDATION.json records the domain and counts; a direct JS runtime can reproduce via code/exact_mux.js.

NESTED_SPEC.json froze six even n=2..12; integer degree certificates in out/NESTED_OBSTRUCTION.json agree with the all-n derivative-parity proof. INDEPENDENT_SPEC.json preceded Python validation: python -X utf8 code/finalize.py constructs36 full mux truth tables independently, uses direct character sums and Fraction prime-log maps instead of the JS butterfly/formula, and checks actual quadratic edge counts at n=2,4,6,8,10,12. out/INDEPENDENT_VALIDATION.json records the result. This is a second implementation by the SAME author, not an independent-agent review. No Lean claim, no float sign certificates, no GPU, no job above300MB, no automatic dimension increase.

## proof dependencies and changed downstream conclusions

The common-phase restriction is unnecessary for one explicitly supplied original-overhead reserve. The v6 sharper common-phase influence rates remain valid and are not overwritten. The scalar profile and bent obstruction were already known; the useful delta is the explicit disagreement-source accounting, the full stopped-tree formulation, and a source-specific nested overcount certificate. No branch FEI bound follows for arbitrary cores. The same physical influence must not finance both an old inherited allocation and an automatically restarted ticket. Only the existing umbrella claim is extended, respecting the review cap.

## one next mathematical action and independent reviewer

A091 primary, A090 alternate; neither has independently accepted this version. Next: retain the actual diminished L reserve through ONE nested mux split and price only its additional coherent debit using a physical-edge ownership rule, keeping original booked debit and both inherited terminal bills. Use the complete quadratic as an obligatory overcount control. This is an edge-ownership problem, not another Fourier-norm class census.

## actual persistence receipts or precise save blocker

The four protocol files, complete proof, three frozen specs, executable source and exact outputs are local to this immutable stage directory. out/MANIFEST.json binds their bytes; out/SOURCE_RECEIPTS.json records source hashes. CLAIMS exact_statement is SHA256-bound and schemas are checked against the actual protocol by code/finalize.py. PACKET_DELTA equals PROGRESS and has packet_ids=[A058]. Rolling STATUS has exactly two lines; WORKLOG and LEARNED receive dated entries. Local saves do not establish supervisor adoption, remote copies, independent review or universal mathematical completion. Brain wake reported stale owner-model/state-of-mind notes; earlier attached-document integrity remains unverified. Those notes were not proof premises.

Did: saved author proof, exact exhaustive checks and a nested-budget obstruction. Stopped: own finite checks completed normally. Left running: no owned research jobs.

## Universal bridge

C019 stopping-tree payment moves from common-phase spectra to arbitrary overlapping Boolean branches for ONE explicitly supplied original collision reserve: coherent cost<=4J+I(GH), uniformly over all adaptive stopping histories. The inherited-core and actual terminal bills remain fully present, and the complete-quadratic family proves the cost of renewing this source is unbounded relative to root influence. What remains is ownership of genuinely new nested collision debit from the SAME already diminished ancestor account, including previous charges. The shortest route toward full FEI is to resolve that precise ownership step under one actual nested split, since reusing the fresh source theorem at every level is now exactly ruled out.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
status='STATE: A058 stage7 saved: arbitrary-overlap original reserve L<=4J+I(GH); 458752 exact assertions PASS; complete quadratic refutes renewed-ticket nesting (ratio n-1); review pending, FEI OPEN.\nNEXT: A091/A090 review v7; retain SAME diminished reserve through one nested split, price only new coherent debit with original edge ownership; keep old debit and both full terminals.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
for name,entry in [
('WORKLOG.md','Proved one original collision-reserve allocation for arbitrary Boolean overlaps, preserving inherited terminals. Exhaustive65536 pairs/458752 checks PASS; independent implementation36 muxes and6 quadratic edge controls PASS. Prior split/bent results credited. Complete quadratic disproves renewed mismatch-ticket summation by ratio n-1. Nested same-depleted-source ownership remains OPEN.'),
('LEARNED.md','v7: arbitrary same-cube Boolean branches have coherent overhead L=sum r[h(d/r)+1-h(w)]>=0 and L<=4J+h(J)<=4J+I(GH). Exact stopped-tree signed coherent cost is L_root minus live-terminal L, with all inherited entropy bills retained. This is ONE supplied original allowance; no admission after prior debit is automatic. Complete quadratic f_n has I=n/2, while fresh nested disagreement tickets sum to n(n-1)/2. Never renew that source. Scalar profile and bent point edit are prior work (full card IDs in PROOF.md).')]:
    p=A/name; old=p.read_text(encoding='utf-8') if p.exists() else ''
    if R.name not in old:
        with p.open('a',encoding='utf-8') as f:f.write('\n2026-10-23 | '+R.name+' | '+entry+'\n')
sources=[protocol_path,Path(r'~\AGENTS.md'),Path(r'BOARD.md'),Path(r'claude\B12\STREAM_NOTES.md'),A/'runs/20261022T211410Z-fleet03-A058-overlapping-compositions/PROOF.md']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'current bytes; mutable board may change after observation'} for p in sources])
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert len((A/'STATUS.md').read_text().splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name not in ['MANIFEST.json','FINALIZE.json']:
        b=p.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(R/'out/MANIFEST.json',manifest)
result={'status':'PASS','manifest_files':len(manifest),'statement_sha256':claim['statement_sha256'],'protocol_fields_checked':True,'independent_validation':independent,'remote_copy':'UNVERIFIED','independent_review':'PENDING','full_fei':'OPEN'}
dump(R/'out/FINALIZE.json',result)
print(json.dumps(result,ensure_ascii=False))
