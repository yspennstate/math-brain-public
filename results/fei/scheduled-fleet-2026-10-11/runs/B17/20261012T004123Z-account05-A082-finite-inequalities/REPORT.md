# A082 stage 2: independent exact five-bit certificate and affine-five application

## exact target, quantifiers, hypotheses and units

Independently reconstruct A071-EXACT-FIVEBIT-ERASURE-SELECTION v1: for every nonconstant Boolean sign on the uniform five-bit cube, the minimum over relevant physical coordinates of B_i/I_i is at most

K5 = 16/3 - (3/8)log2(3) - (169/24)log2(13) + (89/24)log2(89).

This upper bound is attained exactly by the 640 tables whose minority class is {t,t xor e_i,t xor e_j}, with distinct physical coordinates i,j and either output sign. Entropy is in bits, P(S)=fhat(S)^2 and I_i is physical influence. Independently certify 107/40<K5<27/10. The separate all-dimensional application concerns affine Fourier support dimension at most five per disjoint factor, hereditarily under physical restrictions. No assertion of aggregate B<=K5 I or a universal selectable constant is made. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the updated BOARD.md, snapshot 2026-10-12 00:39 UTC; B17 STREAM_NOTES.md v2, dated 2026-10-11 23:40 UTC; own STATUS.md and LEARNED.md; B15 STREAM_NOTES.md v2; A075 LEARNED.md; A085 STATUS.md. Read A071 stage 2 REPORT.md and CLAIMS.json at runs/20261011T233808Z-account05-A071-search-space-design, and code/full_census.py and code/sparse_search.py in full. Read B17 lead's exact CLAIMS.json statements. Reread EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, for field contracts and resource rules. The earlier A082 EXHAUSTIVENESS_LEMMA.tex is the source of the parameterized physical projection argument, initially learned from A026; its affine-four proof is reused rather than enumerated again. Source SHA256 pins are recorded in out/source_receipts.json.

The lead requested an exact K_B(5) census. The newer A071 result already supplies that census, so this stage consumes and independently reviews it rather than pretending the target is still an unexplored search. The implementation reconstructs the crucial coefficient and log computations by different methods. Prior n<=4 censuses, B09 margin and affine-four enumeration were not repeated. The board records external scoped reviews of the earlier A082 finite/bridge claims; this stage does not overwrite those sources or shared review records.

## complete derivation or exact first unsupported line

The complete covering proof and separate application are in EXHAUSTIVENESS_LEMMA.tex. Output complement reduces to a nonempty minority class A of size<=16. Translation puts zero in A, physical coordinate permutation sorts influences, and a subsequent minimal anchored translation preserves that sorted vector. Thus all filters can hold simultaneously and cover all Boolean tables. These are covering filters, not unique orbit representatives. General affine coordinate mixing is excluded.

For each retained mask the independent engine directly computes c_s=W_s/2=16*1_{s=0}-|A|+2 popcount(A intersect odd-character-mask_s). It uses no butterfly transform and imports no A071 helper. Squared probabilities are c_s^2/256. For adjacent squared coefficients a,b, conditional entropy is G(a,b)/256, where G=(a+b)log2(a+b)-a log2(a)-b log2(b). Physical boundary counts independently check D_i=sum_{s containing i}c_s^2=16*e_i and thus I_i=D_i/256. Parseval is checked at each retained table.

Fresh exact Fraction arithmetic encloses each logarithm using a 50-term rational atanh sum and its proved positive remainder. For r in [1,2], z=(r-1)/(r+1), the remainder after the sum through exponent 99 is at most 2*z^101/[101*(1-z^2)]. Positive numerator intervals are divided by opposite positive ln2 endpoints, an exact dyadic exponent is added, and endpoints round outward at denominator 2^110. Packet G upper endpoints combine positive and negative coefficients correctly and round upward at denominator 2^40. There is no floating-point screening decision. The target lower bound is 2964159675584/2^40, rigorously below K5. Every upper pass uses numerator<=2964159675584*D_i with D_i>0. Fixed int64 bounds are checked: each numerator sum is at most 16*512*2^40+256<2^63, and each target product is at most 256*2964159675584<2^63. All conversions occur within these bounds.

The only surviving equality representative is mask 7, A={0,1,2}. Exact prime-log vectors verify its minimum equals K5; all five coordinate comparisons to the target are checked by clearing rational denominators and comparing integer products. Every other representative has a strict upper pass below K5, proving the upper theorem and equality orbit. The orbit generation has 320 negative masks and 320 distinct output complements. Its unique degree-two vertex distinguishes the center, yielding exactly 32*C(5,2)*2=640 tables. Separate integer comparisons certify 2^319*89^445>3^45*13^845 and 2^316*89^445<3^45*13^845, equivalent to 107/40<K5<27/10.

For the physical application, support in c+V with dim(V)<=5 admits either a relevant e_i outside V, giving B_i=JS_i=0, or at most five relevant physical unit vectors in V. The latter case is a genuine five-junta, exhausted by the finite theorem. Restriction projects c+V without increasing dimension. Disjoint independent spectra preserve coordinate erasure and influence. Exact decrement B_i+JS_i and influence conservation yield H<=(K5+2/ln2)I by induction, including every terminal entropy. This is a parameter-five instantiation of the prior structural mechanism, with a newly certified finite premise, not a new universal mechanism. The class expansion from affine dimension four to five requires a larger selectable constant; it is not a reduction of the previous constant.

The first unsupported universal line is a uniformly influence-paid proper stopping transport from unrestricted residuals into these hereditary affine-five leaves. Neither covering symmetry nor projection bounds the affine dimension of arbitrary supports. The known B15 six-bit matching seed already has every ratio>368/125>K5; thus extending this constant to all dimensions is false. Zero erasure without the hereditary support hypothesis does not certify a terminal, and overlapping factor products are not admitted. No unreviewed upper statement is assumed in the finite review.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the searches. All Python commands use -X utf8. From A082, executed:

```
python -X utf8 runs/20261012T004123Z-account05-A082-finite-inequalities/code/reconstruct.py --pilot
python -X utf8 ~\brain_workers\FEI100_20261011\tools\memok.py
python -X utf8 ~\brain_workers\FEI100_20261011\tools\memok.py
python -X utf8 runs/20261012T004123Z-account05-A082-finite-inequalities/code/reconstruct.py
python -X utf8 runs/20261012T004123Z-account05-A082-finite-inequalities/code/finalize.py
```

Pilot: 524288 odd masks, 60541 retained representatives, 60540 strict passes and one equality candidate, mask 7; elapsed 0.387738 seconds, below the 55-second cap. The pilot retained-mask SHA256 is 58fb4a26062848c331cc65d85d40cc992064ef1095791bc9a171f977102f0a70.

Full reconstruction: all 2147483648 odd uint32 masks scanned; 1073741824 anchored minority masks; 80198472 with ordered influences; 5778648 canonical-translation representatives; 5778647 strict passes; one exact equality, mask 7. Elapsed 197.502076 seconds, under the 1200-second cap. The little-endian representative stream SHA256 is ac010403c1e2e329262b930668c4d34bf548c862cad687ebd9210579dd0c233b, agreeing with A071's independently generated stream. The proof uses exact upper lookup values freshly reconstructed by Fraction arithmetic, not equality of this hash alone. Candidate and partial-count checkpoints were saved during the computation. Seed and rational-bound certificates are in out/seed_certificate.json and FINITE_INEQUALITY_CERTIFICATE.json.

One serial NumPy process, batch size 131072, estimated memory<=80 MB, no GPU or automatic dimension escalation. RAM usage was not measured. The requested preflight guard returned 1 twice: free physical 3.1 then 2.9 GB, free commit 8.1 then 3.5 GB, below its 4/8 GB thresholds. No job expected over 300 MB was started. The full replay remained within the frozen 80 MB estimate, below the user's threshold requiring a successful guard; B17's instruction to run the guard first was followed. No other heavy job was launched by this agent.

## proof dependencies and changed downstream conclusions

A071-EXACT-FIVEBIT-ERASURE-SELECTION v1 receives a local HOLDS_AT_STATED_SCOPE independent review record. Its original contributor list and statement hash remain unchanged; no repair was needed, and A082 is not a contributor to that original theorem. This reconstruction checks its exact constant, full-domain upper bound and all 640 extremizers. Shared source adoption remains a supervisor action, not an inferred mutation.

A082-AFFINE5-ERASURE-BRIDGE v1 uses the independently reconstructed finite theorem, the existing exact C005/B17 JS interface, and the parameterized physical projection proof. A026/A027/A028/A061 can use the expanded certified terminal class; A081 can replace the five-bit lower-only scope node with the exact reviewed finite node. A074/A085/A092 can consume the source-bound independent review. C018's universal aggregate inequality, C019's unrestricted stopping payment and full FEI remain OPEN. The affine-five application is author-proved and still awaits an uninvolved reviewer.

## one next mathematical action and independent reviewer

Next consume a concrete A027/A028 or A097/A064 proper-stopping candidate and certify its unpaid cumulative path-to-leaf residual using the affine-five terminal constant. Do not open a blind dimension-six census: the six-bit obstruction is already known and the missing argument is transport, not more finite coverage. A090 is primary reviewer of the new affine-five application; A094 is alternate. A082's A071 review is independent in its critical spectrum and logarithm methods and supplies no substantive repair.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, FINITE_INEQUALITY_CERTIFICATE.json, EXHAUSTIVENESS_LEMMA.tex, FROZEN_SPEC.json, code and outputs are saved in the requested stage directory. STATUS.md remains exactly two lines; dated WORKLOG.md is appended and LEARNED.md records the durable finite/structural facts. The finalizer checks protocol claim/progress fields (normalizing the explanatory parenthesis on packet_ids), statement preservation, packet-delta byte equality, all required report fields, and artifact sizes under 20 MB. out/persistence_receipts.json pins artifact hashes and regeneration commands; source receipts pin inputs. Final artifact hashes are verified after all writes. Supervisor repository copying, brain ingestion, downstream adoption and independent review of the new application are not claimed. No git, external message, shared-tree write or modification of another agent folder was performed.

**Universal bridge:** This stage advances the finite terminal obligation adjacent to C018 and the certified-leaf part of C019: the full five-bit optimum K5 and its 640 extremizers now have a second source-level implementation, and the hereditary affine-support application expands from dimension four to five with payment K5+2/ln2. It adds one certified physical dimension, not an all-dimensional universal bound or an improvement in the old constant. What remains is a nonreusing influence-paid path into those leaves for unrestricted Boolean residuals. NEXT targets a concrete live stopping residual using the reviewed finite premise, because certifying that unpaid path cost is the shortest route from this packet to full FEI; another finite census would leave the same universal line unsupported.
