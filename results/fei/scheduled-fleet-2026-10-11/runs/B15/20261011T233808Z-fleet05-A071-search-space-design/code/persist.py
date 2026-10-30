import hashlib,json
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def save(name,data):(ROOT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
sp=json.loads((ROOT/'out/search.json').read_text());full=json.loads((ROOT/'out/full_census.json').read_text());final=json.loads((ROOT/'out/final_certificate.json').read_text());pilot=json.loads((ROOT/'out/pilot.json').read_text());fp=json.loads((ROOT/'out/full_pilot.json').read_text())
assert final['full_E5_certificate_complete'] and final['all_candidates_certified'] and not final['strict_above_seed']
assert full['counts']['entropy_evaluated']==5778648 and full['counts']['candidates']==1
statement='On the uniform five-bit cube, E*(5)=max_{f nonconstant} min_{i:Inf_i(f)>0} H(S_i|S_-i)/Inf_i(f) equals K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89). Equality holds exactly for the 640 truth tables whose minority class is {t,t xor e_i,t xor e_j}, with t in F2^5 and distinct coordinates i,j, allowing output complement. The associated spectral law is P(S)=fhat(S)^2 and entropy is in bits.'
hyp=['Actual Boolean sign functions on the uniform cube F2^5','Only relevant physical coordinates participate in the minimum','Base-two Shannon entropy of the squared normalized Walsh spectrum']
claim={'claim_id':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['fleet05/A071'],'proof_source':['REPORT.md','SEARCH_DOMAIN.json','FULL_DOMAIN.json','code/sparse_search.py','code/full_census.py','code/check_final.py','out/search.json','out/full_census.json','out/final_certificate.json','out/candidate_certificates.json'],'proof_dependencies':[],'review_records':[],'status':'EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A075','A074','A073','A085','A092','A026','A028','A082','B15','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A071','gap_id':'G-R-SELECT','attempt_id':'A071-G-R-SELECT-001','method':'Exact minority truth-table census with covering cube symmetries; integer Walsh/direct-edge checks; rigorous rational packet entropy upper bounds; exact prime-log ties','mathematical_delta':'Decided the full E*(5), not only minority<=6: K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89), approximately 2.695887520153101. All 2^31 anchored masks scanned, 5778648 representatives evaluated, 5778647 strict passes and one exact equality. Exactly 640 extremizing truth tables. Universal FEI and dimension-uniform selection remain open.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'FULL_FIVEBIT_CONSTANT_CERTIFIED_PENDING_REVIEW; UNIVERSAL_FEI_OPEN','claim_versions_used':['B15-STREAM-NOTES-v2@2026-10-11T23:25Z (dispatch direction)','B15-LKSTAR-FAILS-N5-N6@1 (witness intake, no dependency of the five-bit upper certificate)','B15-SELECTION-EQUIVALENCE-COMPOSITION-INVARIANCE@1 (bridge context)','C005 (only the conditional universal-bridge implication)'],'claims_created_or_changed':['A071-EXACT-FIVEBIT-ERASURE-SELECTION@1'],'source_artifacts':['REPORT.md','SEARCH_DOMAIN.json','FULL_DOMAIN.json','FINAL_CERT_SPEC.json','SEARCH_BUDGET.md','code/sparse_search.py','code/full_census.py','code/check_final.py','out/pilot.json','out/search.json','out/full_pilot.json','out/full_census.json','out/final_certificate.json','out/candidate_certificates.json','out/source_receipts.json'],'next_consumers':['A075','A074','A073','A085','A092','A026','A028','A082','B15','B20'],'next_action':'A074/A085 independently reconstruct the all-function covering filters and packet upper bounds; A075 use the completely classified five-bit extremizer and the existing six-bit matching witness to isolate a dimension-growing erasure obstruction. A071 next freezes a bounded test of the first proposed structural payment in that derivation, rather than launching an n=6 census.','stagnant_substantive_attempts':0,'blockers':['Independent end-to-end reproduction of full census pending','Supervisor repository copy/mirror not observed','Dimension-independent sup_n E*(n) remains unpaid; E*(6)>368/125 already rules out universal use of K5'],'packet_ids':['A071']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(ROOT/'SEARCH_BUDGET.md').write_text(f'''Both domains were frozen before their own searches: SEARCH_DOMAIN.json (minority<=6) and FULL_DOMAIN.json (all five-bit functions). The full run used NumPy 2.4.3 observed locally; no compiler or package installation was used.
One serial Python process, no GPU, no workers. Sparse job cap 600 s, full job cap 1200 s (<30 minutes), equality/orbit job cap 55 s. Estimated RAM: sparse <=80 MB, full <=150 MB, final <=50 MB; resident memory was not measured. No job was expected to exceed 300 MB, so no memok gate was required. One substantial search ran at a time.
Sparse pilot: {pilot['cases']} cases, {pilot['runtime_seconds']:.6f} s. Full-domain prefix pilot: {fp['counts']['raw']} raw masks, {fp['runtime_seconds']:.6f} s. Both pilots under 60 s.
Sparse full: {sp['cases']} cases, {sp['runtime_seconds']:.6f} s. Full census: {full['counts']['raw']} raw masks, {full['runtime_seconds']:.6f} s. Final exact equality/orbit check: {final['runtime_seconds']:.6f} s.
Full chunks: 131072 raw masks. Signed int32 FWHT max magnitude 32, squared half-coefficients <=256; int64 packet upper bound totals stay far below 2^63. Deadline checked per chunk; checkpoint each 16777216 raw masks. A chunk can finish after the nominal cap, but the observed full job finished well within it. Candidate cap 100000; actual 1. No automatic dimension escalation. All final artifacts below 20 MB.
''',encoding='utf-8')
report=r'''# A071 / B15 stage 2: exact five-bit erasure selection constant

## exact target, quantifiers, hypotheses and units

Following B15 STREAM_NOTES v2, decide E*(5)=max over all nonconstant Boolean signs f on the uniform five-bit cube of min over relevant physical coordinates i of B_i/Inf_i, where B_i=H(S_i|S_-i), P(S)=fhat(S)^2, and entropy is in bits. This is an actual-Boolean optimization, not a relaxation of spectral phases. The answer is

    K5 = 16/3 - (3/8)log2(3) - (169/24)log2(13) + (89/24)log2(89)
       = 2.695887520153101... .

Exactly 640 truth tables attain the maximum: their minority output class is {t, t xor e_i, t xor e_j} for distinct i,j, with either output sign. The representative negative mask is 7, i.e. {-1 points}= {0,1,2}, assignment order little-endian. This is the same cube-isometry orbit as the lead's f_5 mask 4194372. This stage decides the FULL five-bit domain, including minority sizes 7..16; it does not infer that result from the preliminary sparse census.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-11 23:39 UTC, B15 STREAM_NOTES.md v2 (2026-10-11 23:25 UTC), own STATUS/LEARNED files, and reread EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Read the B15 lead run's CLAIMS.json, specifically B15-LKSTAR-FAILS-N5-N6@1 and B15-SELECTION-EQUIVALENCE-COMPOSITION-INVARIANCE@1, and code/certify_witnesses.py to pin sign/table conventions. Consulted A075/A085 current status to avoid duplicating their assigned asymptotic and review work. Board records show the prior A071 B09 grid has scoped review support; we did not repeat it.

The lead's direction replaces our old sharper-biased-tax next action. The <=6 sparse domain by itself could not prove the requested full E*(5). We first stated that gap explicitly, then froze and executed an all-function census using covering cube symmetries. Local source byte hashes are saved in out/source_receipts.json. The new upper certificate does not assume either lead claim. C005 is used only to explain the conditional universal bridge, not to compute E*(5).

## complete derivation or exact first unsupported line

1. Write f=-1 exactly on A and +1 elsewhere, with N=32 assignments. Output complement permits 1<=|A|<=16. Translation x->x xor t multiplies each Fourier coefficient by a sign, leaving every squared coefficient, B_i and Inf_i unchanged; translating any point of A to zero anchors the mask at assignment 0. Coordinate permutations permute the five ratios, leaving their minimum unchanged. Therefore every nonconstant truth table has a representative with an odd negative mask, popcount <=16, influences sorted nondecreasingly, and mask minimal among all its translations that contain zero. These are COVERING filters, not unique orbit labels. Sorted influences stay sorted under translation. General affine coordinate mixing is not used because it changes physical influences.

2. All 2^31 odd masks from 1 to 2^32-1 were scanned. Exactly sum_{k=1}^{16} C(31,k-1)=2^30 are anchored minority masks. Of these, 80198472 have sorted physical influences and 5778648 survive anchored-translation minimality. Every surviving table is explicitly built as +/-1 and transformed by an integer batched FWHT. Let c_s=W_s/2; then p_s=c_s^2/256, and the code checks sum_s c_s^2=256. For a spectral pair s,s+i let a=c_s^2, b=c_{s+i}^2. Set

    G(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b),
    L_i=sum_{s not containing i} c_{s+i}^2.

Then B_i=sum_pairs G(a,b)/256 and Inf_i=L_i/256, so B_i/Inf_i=sum_pairs G(a,b)/L_i. Zero masses use 0 log 0=0; G(a,0)=G(0,b)=0. Independently, the number e_i of undirected physical edges on which f changes gives Inf_i=e_i/16. The full census checks L_i=16 e_i for every evaluated table and coordinate. Irrelevant coordinates have L_i=0 and are omitted.

3. Packet entropy bounds are rigorous. For integer z, range-reduce z=2^k t with 1<=t<2, put y=(t-1)/(t+1) in [0,1/3], and use

    ln t = 2 sum_{j=0}^{47} y^(2j+1)/(2j+1) + R,
    0<=R<=2 y^97/[97(1-y^2)].

Each term is floored at natural-log scale 2^128; adding 48 rounding units and the rounded-up tail gives the upper enclosure. The separately enclosed positive ln2 converts to log2; all integer logarithms here are nonnegative, so division uses lower numerator/upper denominator and upper numerator/lower denominator, with outward rounding to 96 bits. Powers of two are exact. In G, the positive coefficient uses its upper logarithm and the negative coefficients use lower logarithms for an upper bound. The already rigorous G interval is then outward rounded to 40 bits for the NumPy lookup table. Integer quotient ceiling gives a rigorous upper bound on each relevant ratio, and its minimum is an upper bound on E(f).

4. The sparse search first constructed a rigorous 96-bit interval and prime-log expression for the seed's exact minimum. The full census fixed a 40-bit lower integer bound on that value, seed_lower_scaled=2964159675584 at scale 2^40. For 5778647 representatives a relevant coordinate's computed upper ratio is <= that lower bound, which proves E(f)<=K5. Only one representative, mask 7, remained. A separate Python integer FWHT reconstructs that table, checks Parseval, its sign-valued inverse at all 32 physical assignments, and influence by direct edges. Exact prime factorization of G's logarithm arguments gives its minimizing ratio vector {2:16/3, 3:-3/8, 13:-169/24, 89:89/24}. The remaining relevant ratios are rigorously at least this value. Thus the seed attains K5, and the all-function covering proves E*(5)=K5.

5. Every other surviving representative is strictly below the seed, since the 40-bit seed lower bound is below the exact seed value. Hence any extremizer must map to mask 7 under output complement, translation and coordinate permutation. Exhaustive generation of that cube-isometry orbit has 320 negative support sets; their 320 complements are distinct, giving exactly 640 extremizing truth tables. Equivalently, choose t in 32 ways and the two distinct coordinate directions in C(5,2)=10 ways; the degree-two vertex of the three-point path identifies t uniquely. Both output signs give 640.

The proof is complete within dimension five, pending independent execution/review. The first unsupported extension would be replacing E*(5) by a bound on sup_n E*(n). In fact the lead's existing six-bit witness has E>368/125>K5, so K5 itself is already excluded as a universal selection constant. No finite census resolves the existence of some larger dimension-independent constant.

## executed validation with domain, arithmetic, commands and outputs

Commands run from A071, always with UTF-8 Python:

    python -X utf8 runs/20261011T233808Z-fleet05-A071-search-space-design/code/sparse_search.py --pilot
    python -X utf8 runs/20261011T233808Z-fleet05-A071-search-space-design/code/sparse_search.py
    python -X utf8 runs/20261011T233808Z-fleet05-A071-search-space-design/code/full_census.py --pilot
    python -X utf8 runs/20261011T233808Z-fleet05-A071-search-space-design/code/full_census.py
    python -X utf8 runs/20261011T233808Z-fleet05-A071-search-space-design/code/check_final.py

The preliminary sparse domain exhausted every anchored A of size 1..6: counts 1,31,465,4495,31465,169911, total 206368, covering 1149016 negative support sets before translation. Exact per-size maximum values, ties and prime expressions are saved in out/search.json. It found no improvement over the three-point seed; this alone would leave sizes 7..16 unpaid.

The separate full prefix pilot scanned 524288 odd masks and evaluated 60541 representatives in FULL_PILOT_SECONDS s. Full census scanned 2147483648 odd masks, evaluated 5778648 representatives, certified 5778647 strict upper passes and retained one equality, in FULL_SECONDS s. Final equality and orbit checks completed in FINAL_SECONDS s, with no unresolved sign. All decisions use integer or rational arithmetic; output decimals are display only.

Outputs saved: out/pilot.json, out/search.json, out/full_pilot.json, out/full_census.json, out/candidate_certificates.json, out/final_certificate.json. Checkpoints and changed incumbents were saved during computation. Enumeration hash for retained full-domain representatives (ordered little-endian uint32 masks): ac010403c1e2e329262b930668c4d34bf548c862cad687ebd9210579dd0c233b. Frozen domain/spec files and SEARCH_BUDGET.md document the case counts, coverage, resource caps and exact arithmetic. The full job used one serial NumPy process with <=150 MB estimated RAM and a 1200-second cap; RAM was not measured. No >300 MB job, GPU, automatic dimension increase, compiler installation or external write occurred.

## proof dependencies and changed downstream conclusions

One bundled finite claim created: A071-EXACT-FIVEBIT-ERASURE-SELECTION@1. Its upper proof depends on elementary cube symmetries, integer transforms, the explicit packet identity, and the proved logarithm remainder; it does not use any assumed FEI theorem or the lead's five-bit lower certificate. It replaces the lead's five-bit lower bound by an exact maximum and completely classifies the equality orbit. All hereditary classes whose actual coordinate restrictions remain five-bit juntas may use this as a sharp finite leaf selection constant after review. It must not be promoted to dimension six or to general affine dimension five without a separate physical-coordinate argument.

The universal endpoint remains sup_n E*(n)<infinity. If one uniform K paid selection on every Boolean descendant, C005 and I(f)=Inf_i+average I(children) would telescope H<= (K+2/ln2)I. Conversely, B=sum_i B_i<=H by the entropy chain rule and conditioning reduces entropy; H<=CI forces a relevant i with B_i<=C Inf_i by weighted averaging. Likewise C018's aggregate B<=KI yields that coordinate. Thus the selection endpoint is genuinely tied to universal FEI, but this stage supplies only its exact five-dimensional obstruction/leaf value.

## one next mathematical action and independent reviewer

A074/A085/A092 should independently reconstruct the covering filters and rigorous upper lookup, then reproduce the full census with a different mask/orbit enumeration or direct conditional law. A075 should use the completely classified five-bit extremizer together with the existing six-bit matching witness to identify the dimension-dependent term in erasure payment, as directed by the lead. A071's next search freezes the first precise structural or nonreusing payment proposed by that derivation; it will not attempt a blind 2^64 dimension-six census. The shortest mathematical step is to separate bounded sparse-defect contributions from an arbitrary-core remainder and prove that the remainder is paid once, rather than treating the solved five-bit leaf value as the universal bound.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json saved locally, with all protocol fields; SEARCH_DOMAIN.json, FULL_DOMAIN.json, FINAL_CERT_SPEC.json, SEARCH_BUDGET.md, code and outputs are inside this stage's A071 directory. Rolling STATUS.md, WORKLOG.md and LEARNED.md updated. Source hashes and artifact SHA256/size manifest saved in out/. A separate validation script checks schema fields, statement hashes and manifest readback. No shared index or another agent's folder was modified. Independent full-census review, supervisor repository adoption and mirror verification are pending and are not inferred from local persistence.

## Universal bridge

This stage moves the lead's universal erasure-selection bridge, equivalent to full FEI up to C005's additive 2/ln2 payment and linked to C018 by B<=H and weighted averaging: E*(5) advances from the lower bound 2.695887520... to the exact value K5 above, with all 640 extremizers classified and the entire five-bit upper gap closed. It does not improve an all-dimensional bound; the six-bit value already exceeds K5, and the unpaid obligation remains a finite uniform bound on sup_n E*(n), or a terminal-inclusive nonreusing C019 payment replacing it. NEXT targets the dimension-growing erasure mechanism using these exact extremizers and the lead's six-bit witness, so the next frozen search can test a specific universal structural-payment lemma rather than produce another isolated finite census or silently discard an arbitrary core's entropy.
'''
report=report.replace('FULL_PILOT_SECONDS',f"{fp['runtime_seconds']:.6f}").replace('FULL_SECONDS',f"{full['runtime_seconds']:.6f}").replace('FINAL_SECONDS',f"{final['runtime_seconds']:.6f}")
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A071 stage 2 complete locally: full E*(5)=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89); 2^31 masks scanned, 5778648 exact representatives, 640 extremizers; review pending; FEI OPEN.\nNEXT: A074/A085/A092 independently reconstruct full census; A075 isolate dimension-growing erasure term using five-bit extremizers and six-bit matching seed; A071 freeze that structural payment, not an n=6 census.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f"\n{datetime.now(timezone.utc).isoformat()}: Full n=5 census completed in {full['runtime_seconds']:.6f}s: 2^31 raw odd masks, 2^30 minority masks, 80198472 sorted-influence masks, 5778648 translation-minimal representatives. 5778647 strict passes, one exact equality (mask7). Independent Python FWHT/inverse/edge checks and cube-orbit reconstruction establish exact K5 and 640 extremizers. Saved all protocol artifacts and universal-bridge handoff; independent end-to-end review pending.\n")
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
## Stage 2: full uniform five-bit erasure census

- Exact local result pending independent review: E*(5)=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89)=2.695887520153101... . Exactly 640 truth tables attain it; the minority class is a three-point two-edge cube path. The whole domain, not only minority<=6, was covered.
- A complete five-bit census is practical with serial chunked NumPy: 2^31 odd masks scanned in 132.765480 s; sorted physical influences plus minimal anchored translations leave 5778648 entropy evaluations. These are covering filters, not unique NPN representatives. Input-coordinate mixing by a general affine map would invalidate physical influence invariance.
- Rational packet upper bounds rounded outward to 40 bits settle all but one representative; exact prime-log form settles the equality. No float tolerance and no precision escalation are needed. Direct physical edge counts matched spectral influence for every evaluated coordinate.
- The sparse <=6 census alone leaves sizes 7..16 unsupported. A second explicitly frozen full domain closed that gap. Do not confuse a structured census with the global optimum.
- E*(6)>368/125 from the B15 lead already excludes K5 as a universal constant. Full FEI still asks for a dimension-independent bound or a nonreusing terminal-inclusive payment. Next work should target the structural reason for ratio growth, not a raw dimension-six census.
''')
print(json.dumps({'persisted':True,'claim_id':claim['claim_id'],'E5_exact':True,'extremizers':640,'full_fei':'OPEN'},indent=2))
