# A071 stage 3: exact six-bit-gate admission countersearch

## exact target, quantifiers, hypotheses and units

Let h be the six-bit Boolean sign negative exactly on {0,1,2,4,8,16,32,6,17,40}. For an actual Boolean core g on a uniform physical cube, form F=h(g_1,...,g_6) with six disjoint identical copies. Set B_i(g)=H(S_i|S without i), E(g)=min over relevant i of B_i(g)/Inf_i(g); all entropies are bits. Test the proposed admission helper that the signed empty-sector reserve is nonnegative, and its repairs by minority orientation or choosing either output sign. These are explicit A071 test hypotheses, not statements attributed to A075 or A056. The broader target is A075's arbitrary-core biased admission NEXT after its matching/path mechanism closure. No claim about universal FEI follows from a bounded erasure counterexample.

The result is an exact obstruction: for the six-bit one-point defect g, E(g)>9/4 but BOTH h(g^6) and h((-g)^6) have E<9/4. Thus an unguarded fixed-threshold admission theorem, even with a choice of output sign, is false. Separately the actual 36-bit h(h^6) has E between 323/100 and 324/100, excluding any universal selectable-erasure constant at most 323/100. The one-point obstruction has low E and does not refute an admission theorem restricted to E(g)>=K6 or to a larger hard-core threshold.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 21:55 UTC, B15 STREAM_NOTES.md (still v2, 2026-10-11 23:25 UTC), own STATUS.md, and EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Consumed A075's 20261013T212622Z REPORT/CLAIMS, specifically its matching-family hereditary closure and arbitrary-core biased admission NEXT. The lead's n=5 assignment is already finished: A082 independently reconstructed the full census and A085's 20261013T213517Z report accepts its coverage/lookup audit. This stage does not repeat it. Read A098's 20261012T024601Z reallocation report and A089's 20261012T044049Z repair report to avoid retired half-tax, matching-growth and raw-recursion work. Read A056's 20261011T233147Z REPORT in full, especially equations (3)-(6) and its already-known AND2 negative signed-correction example. That interface is reused, not renamed as a new result. Earlier campaign/paper source pins remain the prior A071 stages; no new manuscript audit is claimed. out/source_manifest.json records actual source hashes.

## complete derivation or exact first unsupported line

Write p=P(g=-1), m=1-2p, v=1-m^2, beta_i=ghat({i}), t=beta_i^2. Constants are handled by deletion. Expand h under independent biased inputs, in their normalized centered product basis, with coefficients b_T. For J excluding outer coordinate 1, put U_J=b_J^2 and V_J=b_(J union {1})^2. Define

    e(x,y)=(x+y)log2(x+y)-x log2 x-y log2 y,
    q(p)=2p(1-p)^3(2-p),
    M_p(t)=sum_J e(U_J, t V_J/v),
    R_p(t)=M_p(t)-q(p)e(m^2,t).

Zero terms use continuous endpoint values. Exact coefficient expansion, homogeneity of e and Parseval on the other occupied blocks give, for every physical coordinate in every copy,

    Inf_i(F)=q(p) Inf_i(g),
    B_i(F)=q(p) B_i(g)+R_p(beta_i^2).                 (1)

For the empty selected-child residual Fourier set the no-i amplitude is the recentered outer coefficient; its contribution is M_p. Nonempty selected-child residual sets contribute q times their child pairs. Removing precisely the child's empty pair produces (1). This is A056's recentered identity with an explicitly specialized gate, not an assumption that squared signed terms add incoherently. Independently, the gate minority probability is alpha(p)=(1-p)^4(1+4p-2p^2), and sum_J V_J=vq; both were verified exactly at every tested bias.

The core spectrum for g negative only at zero on six bits is ghat(empty)=31/32 and ghat(S)=-1/32 for every nonempty S. Every physical influence is 1/32. Hence all six core ratios equal

    E(g)=[62+962 log2(962)-961 log2(961)]/32
        =2.2922449382251937... >9/4.

Both g and -g are invariant under all six input permutations. The outer gate is transitive under swaps within its matched pairs and permutations of those pairs. Independent core permutations within each block and these outer automorphisms act transitively on all 36 physical coordinates, so a single computed ratio is the actual minimum, with no omitted cheap coordinate. Exact rational enclosing intervals and all 32 rational outer packets for each sign are in out/orientation_certificate.json. They certify:

    p=1/64: R=-0.0002579291303..., E(h(g^6))=2.1527061725... <9/4;
    p=63/64: R=-0.00000006946869..., E(h((-g)^6))=2.0008009627... <9/4.

All strict comparisons use rational interval endpoints, not these displayed decimals. The independent reconstruction directly sums the two signed conditional sections of h on its other five inputs, rather than reusing the centered-transform algorithm.

A smaller explicit physical-table control is g on three bits negative at all points except 7 (mask127): E(g)=2.6724889839... >8/3, while all 18 coordinates of h(g^6) have E=2.0761370119... <21/10. Its full actual truth table, integer Walsh transform, pair spectra and physical edge counts were reconstructed independently. This validates (1) against an explicit composition rather than only a compressed calculation.

The positive calibration h(h^6), with core p=5/32 and beta_i=-3/16, has q=5806485/16777216, every physical influence 17419455/268435456, reserve 0.01854441296..., and E=3.230266468892202... . Its rational lower endpoint is strictly greater than 323/100. The opposite orientation h((-h)^6) has E=2.63789894979... . Thus output complementation preserves the core's H,I,B,E but cannot be quotiented before applying a fixed biased outer gate.

The second family is complete in an important limited sense. For any six-bit Boolean core with M negative points and a chosen coordinate, let M0,M1 be negative counts in its two halves. Then p=M/64 and |beta|=|M0-M1|/32. Consequently d=|M0-M1| satisfies 0<=d<=min(M,64-M) and d congruent M modulo2. Conversely every such pair is realized by placing (M+d)/2 lex-first negatives in the coordinate-zero half and (M-d)/2 in the coordinate-one half. Since R depends only on (p,beta^2), the 559 signatures settle the reserve sign for every chosen coordinate of every six-bit Boolean core without enumerating 2^64 tables. They do not settle E minima or the admission implication for all cores. Among the 288 signatures with p<=1/2, 39 have negative reserve. Both output orientations are negative at exactly the four minority signatures (M,d)=(1,1),(2,2),(3,1),(3,3) in this six-bit projection.

The honest first unsupported line is now narrower: for an arbitrary core whose E already exceeds the campaign's hard-core threshold (at least K6), does some legitimate orientation/representation preserve that threshold after the signed reserves in (1), all physical coordinates, and actual terminal H(g) are retained? The low-E point defect does not answer this. Nor does E(h(h^6))>3.23 establish unbounded E or unbounded H/I. No recursion, asymptotic admission theorem, or terminal entropy payment is proved here.

For the logarithm certificates, write n=2^k r, 1<=r<2. For z=(r-1)/(r+1), 0<=z<1/3, use ln r=2 sum_(j>=0) z^(2j+1)/(2j+1). Floor each of 48 terms at scale 2^128; the upper error is 48 units plus the ceiling of the geometric tail 2 z^97/[97(1-z^2)]. Enclose ln2 by the same construction with z=1/3. Add k ln2 with positive k, divide positive interval endpoints outward, then round outward at 2^96. Powers of two are exact. Rational e(x,y) is evaluated after clearing a common denominator, with negative logarithmic coefficients rounded in the opposite direction. No floating value selects a sign, minimum, or threshold.

## executed validation with domain, arithmetic, commands and outputs

Each search/check has a spec saved before execution: out/FROZEN_SPEC.json, VERIFY_SPEC.json, SIGNATURE_SPEC.json, ORIENTATION_VERIFY_SPEC.json. All helpers and JSONL records are inside this run. No symmetry quotient of core output sign is used. For the first family, six identical blocks justify carrying only the chosen core's physical coordinates; every relevant coordinate in each block is included. Constants and zero singleton endpoints are explicit.

Commands, with this run as the script prefix: python -X utf8 code/search.py --pilot; python -X utf8 code/search.py; python -X utf8 code/verify.py; python -X utf8 code/signatures.py --pilot; python -X utf8 code/signatures.py; python -X utf8 code/orientation_verify.py. Outputs record measured computation times:

- First pilot: 23 actual cores, 32 relevant coordinate types, 0.0298 seconds.
- First full family: all 408 frozen cores, 1526 relevant coordinate types, 0.649 seconds; 946 positive, 166 exactly zero, 414 strictly negative reserves; 73 strict decreases of the minimum E; no unresolved reserve signs. out/cases.jsonl is flushed after each core.
- Independent physical/conditional check: the 18-bit table on all 18 coordinates plus both 36-bit seed orientations, 4.058 seconds. out/direct18_certificate.json is saved as soon as the direct reconstruction completes.
- Signature pilot: all25 planned signatures, 0.0831 seconds. Full: all559, 13.084 seconds, 440 positive/31 zero/88 negative reserves. Minority orientations: 233 positive/16 zero/39 negative. out/signatures.jsonl is flushed after every case.
- Independent orientation check: two one-point-defect orientations, 0.0881 seconds, common exact threshold K=9/4 rejected for both.

Execution bookkeeping: the first full search completed and saved its entire output, but piping console output to Select-Object -First caused a nonzero pipeline exit. Counts, file hashes and full results were inspected afterward; this is not presented as a clean console invocation. The initial verifier used an unjustified diagnostic threshold 5/2 for the complemented seed and failed there after saving the direct18 certificate. Reading the exact seed interval corrected that check to 8/3; the rerun passed. No mathematical witness or logarithm arithmetic changed. All other listed runs completed normally. These checks use under120MB estimated peak RAM, so no >300MB job or memok override was needed. No n escalation, GPU, background job, or full36-bit table was attempted.

## proof dependencies and changed downstream conclusions

The calculations use only exact Walsh/physical edge identities and the recentered split reconstructed from A056; neither A075's pending all-dimensional closure nor an unreviewed universal payment is assumed. A075's matching result is consumed as dispatch evidence, not a proof premise. A082/A085's n=5 reconstructions justify retiring the previous census task.

A075/A089/B15 can reject the unguarded statements R_p(t)>=0, minority orientation always makes R nonnegative, and for every K,g some sign preserves E(g)>K. They cannot reject a threshold-guarded admission theorem at K>=K6 on this evidence. The six-bit projection is exhaustive for reserve signs only. A036-style overlap/physical descendant arguments and C019 terminal entropy costs remain untouched. The 36-bit positive calibration raises this packet's exact erasure obstruction from K6=2.9444953... to >3.23, without converting it into an FEI lower bound of that size.

## one next mathematical action and independent reviewer

NEXT: A075 should state one threshold-guarded admission inequality at E(g)>=K6 using (1), and test whether the known negative-reserve signatures can occur at every coordinate of an actual hard core. Retain both orientation choices, physical influences and terminal H(g); use the 559-signature table to target the bad sectors instead of increasing the dimension or repeating matching searches. A085 (alternate A092/A082) should independently reconstruct the two conditional-section certificates and transitivity, and confirm the direct18 Fourier/edge hashes. All independent acceptance of this stage remains pending; no message was sent to another agent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, code helpers, frozen specs, per-case outputs and local receipts are saved in agents/A071/runs/20261013T215901Z-fleet05-A071-search-space-design. Rolling STATUS/WORKLOG/LEARNED are updated only inside A071. out/receipts.json supplies artifact hashes/sizes; schema validation is in out/schema_validation.json. Every file is below20MB. Independent review, supervisor copy, mirror verification and downstream mathematical use are pending, distinct from this completed local artifact. No shared index, other agent folder, brain or repository was modified.

## Universal bridge

This stage moves B15's lead-linked arbitrary-core biased admission bridge toward C018 erasure B<=KI: it rules out an unguarded fixed-threshold transfer even after choosing the core's output sign, with a common rational K=9/4 and actual36-bit Boolean witnesses, and raises the packet's exact necessary selectable-erasure constant from 2.9444953... to greater than3.23. It pays zero additional universal entropy or stopping-tree cost. The remaining line is a threshold-guarded admission or amortized signed-reserve argument for arbitrary high-E cores, including terminal H(g), not positivity of every reserve. NEXT attacks that exact universal reduction by checking realizability of the now-explicit bad signature sectors under the hard-core hypothesis; it avoids another isolated formula-class result or dimension-only search.
