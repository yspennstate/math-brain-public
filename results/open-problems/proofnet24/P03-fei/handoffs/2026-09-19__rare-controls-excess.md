# FEI continuation: rare-control excess contraction and corrected scheduled instructions

19 September 2026. **Full FEI remains OPEN.** This is an owner-requested mathematical continuation with executed self-checks, not an independent audit or a claim that a later scheduled worker has consumed it.

## Read and reproduce

Read [the complete proof report](../continuations/2026-09-19-rare-controls/REPORT.md), [executed verifier](../continuations/2026-09-19-rare-controls/verify_rare_controls.py), [unchanged dependency](../continuations/2026-09-19-rare-controls/prior_exact_entropy.py), [actual output](../continuations/2026-09-19-rare-controls/verification.json), and [pre-experiment idea](../continuations/2026-09-19-rare-controls/IDEA.md).

Run `python verify_rare_controls.py --part all --output verification.json`. The final code was replayed and every non-timing field matched. Archived JSON was compact-formatted without changing its parsed values. No Lean or independent review was performed.

## Mathematical delta

Write M for minimum affine influence, M_0 for minimum influence over invertible input changes WITHOUT an output character, and Phi_C=H-C M. For c fresh independent bits set Gamma_c f(z,y)=1-1{z=0}(1-f(y)). For every Boolean input f, c>=4 and arbitrary quadratic Q on all old and new variables,

    Phi_C((-1)^Q Gamma_c f) <= 2^(-c) Phi_C(f),
    C >= C_* =17/4+1/(2 ln2) <5.

This is unconditional as an excess comparison, not an assertion that an arbitrary unknown seed has nonpositive excess. The operation ADDS fresh bits. It is NOT a transition in the fixed-domain multiplicative-derivative chain and cannot simply be inserted in that chain's entropy telescoping.

Starting with any proved H<=C_*M seed family, the SAME constant is retained under arbitrarily many such controlled-quadratic stages, disjoint products, and extended-affine/surjective transformations. The previous constant-four quadratic-coupled-clause/cubic-core family supplies seeds. High-degree terms may share the entire new control block, with unbounded depth and arbitrary quadratic interactions at every controlled stage. This is an extension beyond the previous displayed independent-clause parameterization, not a theorem for arbitrary overlapping clauses. Fresh controls and certified seeds remain essential.

Exact supporting identities, with p=2^(-c), d=1-Ef:

    M(Gamma_c f)=p[M_0(f)+cd], c>=2,
    H(Gamma_c f)=pH(f)+2c(2pd-p^2d^2)+R(p,d),
    R(p,d)<=(1+2/ln2)pd.

M_0 cannot be replaced by M: a one-bit character has M=0, M_0=1 and M(Gamma_4 f)=5/16, not 4/16.

The separate rare-base theorem applies to EVERY Boolean g with delta=Pr(g=-1)<=1/8, regardless of degree or internal dependencies. If Q has polar rank rho,

    M(g(-1)^Q)>=M(g)+(1/2-4delta)rho,
    |H(g(-1)^Q)-H(g)|<=rho.

The rank coefficient is attained on one-point bases. For delta<=1/16 and C>=4, quadratic twisting cannot increase H-CM. This extends the old clause-specific rank argument to arbitrary rare sets, not just disjoint products.

A corollary treats an arbitrary error set of density delta around any quadratic phase:

    H(g(-1)^Q) <= [2+2n/log_2(1/delta)]M(g(-1)^Q), 0<delta<=1/16.

At delta<=2^(-n/2) this is constant six; at delta<=2^(-3n/4) it is 14/3 and supplies additional seeds below C_*. The biased entropy/isoperimetry input is established background; its new use here is the arbitrary quadratic rank comparison.

## What is NOT proved

The global allocation bound T<=C J and unrestricted FEI are still unproved. A fixed rare gate applied to tensor powers of an arbitrary affine-minimized seed preserves that seed's H/M ratio asymptotically. Therefore gates around unrestricted unknown seeds are still FEI-hard. Do not turn the excess contraction into a circular full proof, and do not drop freshness or identify arbitrary shared old inputs.

The new class has constant below five; it cannot contain every Boolean function, since published H/I examples exceed 6.454784. Basic conjunction composition, archived S05 conjunction closures, prior affine tensorization, and standard quadratic/coset facts are credited in REPORT.md. No exhaustive reread or novelty clearance is claimed.

## Executed verification

834 gated truth tables, 59,416 exact control-direction identities; 1,143 rare-base/quadratic pairs with 20,234 directional inequalities and 76 sharp one-point cases; 460 scalar rational pairs; 10 nested stages and 11 affine checks; five shared-control high-degree examples; 12 exact tensor/gate reduction examples; 11 unstructured quadratic error sets. All acceptance checks are rational or outward rational logarithm intervals. The universal statements depend on the written proofs, not finite extrapolation.

Report blob: `98ba87f8804ad42bc16695472606e45b6aac8bdb`.
Verifier blob: `9645c37e7c1d310304be9e87b8daa22cf06d76b1`; SHA256 `854933ec5a344b94574125d83016834999857ad84fd4747d843bb96306ec357e`.
Dependency blob: `e867ba6b12e1a3e7588fd812eba6841319cd97b9`; SHA256 `9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab`.
Output blob: `e3f7edaf4c66770512f665d22662da35fe85aa6b`.
All these remote object hashes match the local files. A created object is not branch delivery until a commit and ref update succeed.

## Scheduled behavior actually corrected

Existing task `FEI proof continuation`, id `6aaec3d268808191814212175ff425aa`, was successfully updated at 2026-09-19T20:01:49Z, preserving its enabled hourly cadence. No new task or unrelated worker was changed. Its stale instruction to attempt the already-refuted full-resolvent bound was removed. The current prompt requires fresh-master reads, actual blob hashes, `superseded_targets_checked`, exact hypotheses, and substantive new mathematics rather than repeated unchanged certificates.

Retired targets remain: D_cross<=K(R+Q_log) and D_cross<=K(C+Q_log), for all fixed K; M<=a v+b delta_M, for every finite nonnegative pair; D_cross<=4(v+delta_M), for the stated coefficient four; the false pointwise erasure shortcut and universal zero-boundary-debt decomposition. Do not generalize the coefficient-four counterexample to all possible entropy-drift constants. Preserve the valid D_cross<=6M and earlier payments.

At the latest inspected run-directory listing, only the older 18:46:55Z report was present. Configuration and file availability are verified; subsequent consumption of this new report is not yet verified. Each next substantive report must document consumed paths/SHAs, retired claims removed from the plan, reused hypotheses, new mathematical delta, actual tests, and remaining full-scope gap.

## Next mathematical work

Reconstruct the contraction and rare-base rank proof, then attack the missing dependency bound: either control general dependent branch recombination, establish a truly global accumulated-allocation/hereditary-erasure bound, or extend the arbitrary-rare-base interference argument beyond character-valued quadratic derivatives. Do not spend a run merely renaming the remaining bound or tuning a refuted constant. Preserve the source status OPEN and the native P03 metric; do not change peer ownership, permissions, visibility, workflows, or unrelated files.
