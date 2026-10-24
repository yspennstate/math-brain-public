# exact target, quantifiers, hypotheses and units

Extend the existing A056 two-branch controller transport candidate to coherent shared data and arbitrary controller output bias. All costs are bits. Let F=c(W)G(S,X)+(1-c(W))H(S,Y) for Boolean branches and indicator c, with W,S,X,Y disjoint uniform physical blocks. Set a=1-2c, p=Ec, V=4p(1-p), d=P(G!=H). Empty blocks, constant branches and endpoint biases are included. Terminal reference bounds and strong controller certificates are explicit hypotheses, never conclusions about arbitrary cores. Full FEI remains OPEN.

The local all-dimensional residual is

    H(F)-pH(G)-(1-p)H(H)
       <=d Hplus(a)+V[A(vG+vH+sigma)+B d],
    A=1/(e ln2), B=3/ln2+2,

where vG,vH are private Fourier masses and sigma is the sum of absolute squared-coefficient differences at every shared-only atom. When both conditional-mean Fourier profiles have l1 norm at most Lambda, the correction is at most [4A(1+Lambda)+B]Vd. In particular it is <11Vd for one shared physical bit and <13Vd for two. These coefficients are not competitive with the already-reviewed fair-selector constants; the new scope is arbitrary controller bias with the vanishing variance factor and exact terminal debt.

# sources actually read, revisions and theorem locators

Read complete EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2, BOARD supervisor snapshot 2026-10-14 01:30 UTC, own STATUS and prior stage claim/code, and B12 STREAM_NOTES v2 (still dated 2026-10-11 23:30). Its original biased-erasure assignment was completed in earlier stages; this stage resumes the saved shared-data gap. Required campaign/paper readings retain their recorded earlier-stage scope; no new external literature theorem is used here.

Consume A097 run 20261013T222610Z DERIVATION sections 1-4: calibration at all shared atoms, compatible fair reference, and the unrestricted overlap boundary. BOARD records A094's full-chain acceptance. Read A091 run 20261013T220323Z REPORT, especially independent cap acceptance, ownership corrections and the honest shared-control gap. This discharges our old NEXT request for an independent A057 cap review without pretending A056's earlier upstream-linked reconstruction was independent. Read A057 run 20261012T003930Z code/save.py line 28 and CLAIMS for its actual hash convention. Read A095 run 20261013T213857Z REPORT: biased activation with retained core debt and common-spine restrictions, distinct from coherent two-branch shared data. A077/A078/A013/A018 reports were inspected for nonduplication: one-bit fair DATA pricing, actual multishared rare-query failure, fair complete reference, and the shared-bit product identity respectively. None is an unpaid premise of the scalar proof. Byte receipts for principal consumed sources are in out/SOURCE_RECEIPTS.json.

# complete derivation or exact first unsupported line

DERIVATION.md proves the exact spectrum, entropy and physical influence identities, including nonempty shared collisions. Its scalar lemma is valid for all real x,y and p in [0,1]:

    K_p(x,y)<=4p(1-p)[A|x^2-y^2|+B(x-y)^2/4].

Homogeneity permits normalization max(|x|,|y|)=1. The function phi(z^2)+3z^2/ln2 is convex on [-1,1], including zero. The remaining entropy packet is bounded using its elementary one-variable maximum for equal signs and q>=1/4 for opposite signs. Summing gives the displayed named residual; the conditional-mean inequality |mG-mH|<=1-mG*mH bounds every shared Fourier difference by 2d. Rational series certify constants <11/<13. This analytic argument supplies the continuum bridge beyond the finite grid.

All shared-only atoms are calibrated individually. The root reference uses the actual biased controller Fourier kernel, including every nonempty controller subset. Its normalization follows from alpha_T^2+Vq_T=p x_T^2+(1-p)y_T^2. Off-support reference mass is retained. Direct KL expansion yields

    D(PF||Q)=pD(PG||RGcal)+(1-p)D(PH||RHcal),
    CE(PF,Q)=p CE(PG,RGcal)+(1-p)CE(PH,RHcal)+Pi.

Thus both complete terminal bills survive with their actual probabilities. If Hplus(a)<=T[I(a)-V] is independently supplied, I(a)>=V gives controller charge max(T,C_Lambda)dI(a). Supplied terminal CE<=K_j I(j) then gives the corresponding max-constant conditional root bound.

Physical coordinate restrictions preserve independent uniform remaining blocks; output means, profiles and kernel must be recomputed. Nonlinear event conditioning is not automatically a subcube restriction. Private restrictions can create shared-only coefficients that were not calibrated above. First unsupported C024 line: pay the actual transition from an inherited complete reference to the newly calibrated reference with one exclusive reserve. First unsupported unrestricted C020 line: pay V A sigma from retained terminal slack when no bounded-profile admission is available. Bent/point-flip boundaries already refute universal selector-only payment; this stage does not reopen that route.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json was saved before search. Pilot domain: 51 scalar triples and 32 roots. Full domain: p=j/16, j=0..16, x,y=k/8, k=-8..8 (4913 scalar triples); all 16 two-bit sign controllers paired with all 16^2 branch pairs in each of two domains: (i) two shared bits, no private bits; (ii) one shared bit and one private bit per branch (8192 Boolean roots). No symmetry quotient, random sampling or automatic dimension increase. Each root checks uniform and index-weighted complete seed references (16384 reference checks). Actual cube size is at most five physical bits.

Commands from A056:

    python -X utf8 runs/20261014T012909Z-account05-A056-balanced-composition/code/check.py --pilot
    python -X utf8 runs/20261014T012909Z-account05-A056-balanced-composition/code/check.py
    python -X utf8 runs/20261014T012909Z-account05-A056-balanced-composition/code/finalize.py

The initial integer-product-only full attempt was stopped after approximately 260 seconds, below its 300-second frozen limit, without a completed validation or reported counterexample. Its pilot had underestimated interior scalar sign costs. out/SPEC_AMENDMENT.json freezes the replacement before execution: identical domain and arithmetic identities, sign decisions from cached rational natural-log intervals, with integer products only as an ambiguity fallback. Range reduction to [1,2] uses 24 positive atanh terms and explicit remainder 2z^49/[49(1-z^2)], then outward rounding to denominator 2^64. No floating entropy or sign is used. Copied arithmetic.py preserves the prior transparent integer Walsh/Fraction/prime-log helper; check.py adds a distinct coherent embedding and reference implementation.

Final result: ALL PASS on 4913 scalar triples, 8192 Boolean roots and 16384 calibrated-reference checks, in 273.841 seconds (below the frozen 300-second limit). The pilot passed in 0.151 seconds. Outcomes are recorded verbatim in out/checks.json; finalizer required ALL PASS before saving claims and rolling completion. Identities compare exact prime-log coefficient vectors; all nonnegative signs are rigorous. The 120 MB estimated memory is below the memok threshold; one observed process sample had peak working set 24,494,080 bytes. No >300 MB job, GPU, background helper or external write was used. The finite checks validate the stated domain, while DERIVATION independently proves all-dimensional formulas and continuous bias statements.

# proof dependencies and changed downstream conclusions

The scalar lemma and exact reference identities are proved directly, with an acyclic elementary chain. Earlier disjoint/priority claims remain intact at their original stronger constants. This is v2 of A056-TWO-BRANCH-COMMON-CONTROL-TRANSPORT, extending one existing review slot, rather than opening a third broad universal candidate under the stream cap. Independent review of this extension is pending; locally proved is not independently accepted or adopted.

A091's acceptance closes the old A057 cap-review dependency at its exact fresh-activation scope. A057's statement digest is valid: its author hashes canonical sorted compact JSON containing statement and hypotheses. Our stage3 plain-UTF8 comparison incorrectly diagnosed a provenance inconsistency. out/HASH_CORRECTION.json verifies the source recipe and retracts that warning; immutable earlier files and author sources were not edited. The correction is bookkeeping, not mathematical progress.

Downstream users may replace the fair-controller assumption in the calibrated shared-row interface by the present variance-scaled residual, preserving current terminal costs. They may not infer an inherited-reference reset telescope or unlimited shared dimension. No universal FEI constant improves.

# one next mathematical action and independent reviewer

Next: after one private physical restriction of the coherent branches, compute the inherited-reference recalibration bill together with V A sigma, and compare the signed total with a single certified terminal-slack reserve on the known bent/point-flip obstruction. Keep both weighted seed CE bills. This directly tests the missing payment, rather than exhaust another fixed overlap width. Independent reviewers: A091, alternate A090; compatible-reference consumer A097/A094. These are saved handoffs only; no message was sent and no reviewer response is assumed.

# actual persistence receipts or precise save blocker

The run stores REPORT, CLAIMS, PROGRESS and its byte-identical PACKET_DELTA compatibility copy, DERIVATION, frozen specs, code, pilot/full results, source receipts, hash correction and local persistence manifest. STATUS has exactly STATE/NEXT lines; WORKLOG and LEARNED are appended only within A056. Finalization validates full checks and the metadata correction, keeps every file below 20 MB, and records hashes in out/PERSISTENCE.json. Local saving is the only claimed receipt: supervisor copying, remote mirrors and downstream mathematical adoption are unobserved.

# Universal bridge

This stage moves C020 whole-set witness cost and the local C024 restriction interface by closing arbitrary controller bias in a single normalized coherent shared-row reference: terminal KL is preserved exactly and bounded one/two-bit profiles incur <11Vd/<13Vd beyond controller entropy. The all-dimensional unpaid residual is now explicitly V A sigma, and physical restriction exposes a separate inherited-reference reset bill rather than hiding it. Universal payment and full FEI remain open. NEXT targets those two terms with one certified terminal reserve on the already-known obstruction, the shortest identified route to full FEI because it attacks the failed dimension-independent ownership step instead of producing another isolated bounded-overlap theorem.
