VERDICT: PARTIAL conditional volume-tail exponent existence with crossing counts controlled in probability

The earlier finite-scale inequality and its exponent-existence transfer
were independently re-derived and hold. The new result extends that
work to the cluster-volume tail and weakens the crossing-count assumption
for the forward averaged two-point conclusion.

For the exact earlier free-boundary count K_n in B_{2n}, assume

    pi(n)=n^{-a+o(1)},  0<a<d/2,
    P(K_n>n^epsilon) -> 0 for every epsilon>0.         (P)

PROOF.md proves

    P(|C(0)|>=t)=t^{-a/(d-a)+o(1)},
    delta=(d-a)/a=d rho-1,
    X(n)=n^{d-2a+o(1)}.

The earlier subpolynomial E K_n assumption implies (P), as does tightness
of K_n. The proof does not infer an expectation bound from (P). Rare
large counts can still dominate expectation, exactly as the earlier
audit warned. It avoids that expectation through a buffered annulus and
selected scales at which arm-probability ratios are bounded. Logarithmic
one-arm decay supplies enough such scales to obtain the tail law at
every sufficiently large size. No regular variation is assumed.

The finite geometric lemma is

    J_m <= sum_{z in m*partial B_12} K_m(z),

where J_m counts crossing components in the induced annulus with radii
8m and 16m. Every small box lies between radii 10m and 14m. The inner
arm variables stop at radius 7m, so they are independent of J_m.
This proves a largest-cluster mass estimate at good scales and then the
volume-tail lower bound. The upper bound is a radius/volume split using
the independent-endpoint-arm estimate from the earlier work.

The relation delta=d rho-1 and the annular method are classical. The
deliverable is a self-contained conditional extension of the earlier
folder's result for its exact K_n and logarithmic limits. No priority
claim over classical conditional hyperscaling results is made.

## Verification and commands

Read the earlier REPORT.md, LOG.md, PROOF.md and AUDIT.md with `cat`.
`ls -la ~/codex_op_1114/briefs/T087` confirmed that
there were no earlier computation scripts. LOG.md records the independent
re-derivation, source openings, choice before proof, and audit.

This was a proof task: no simulation, numerical dataset, Python run,
subagent, git operation, or external posting was used. AUDIT.md checks
the covering, independence, tail directions, integer scales, parameter
limits, exponent arithmetic, and counterexamples to tempting stronger
claims. Its constants are exact arithmetic re-derived separately.

Final text check: `OMP_NUM_THREADS=1 nice -n 15 sed -n '1,380p' PROOF.md`
printed the entire proof. The sandbox denied the priority adjustment
(`nice: setpriority: Operation not permitted`); the brief text read
completed. No numerical workload was launched.

The status search finished in less than five minutes. No verified
complete solution of T087 was found. The September 2026 OpenAI continuity
manuscript's README was opened, but its claim was not independently
certified. Nothing here depends on it. Primary sources and exact URLs
are recorded in LOG.md; the relevant classical comparison is
C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness of
Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26,
especially Sections 2 and 5.

## What failed or remains uncertain

No bound on the actual critical K_n distribution in dimension three was
proved. Neither the one-arm exponent nor (P) is established here for
Z^3. The result gives no uniform pointwise two-point exponent, numerical
exponent value, or near-critical matching. The earlier reverse existence
transfer from X to pi is not extended to (P). Novelty beyond this local
continuation has not been established.

A direct replacement of E K_n by a typical count in the earlier
Cauchy–Schwarz inequality is invalid. A bound on every fixed-ratio arm
comparison also does not follow from a logarithmic exponent. The proof
uses independent buffered events and a telescoping selection of scales
to avoid these two failed shortcuts.

## Next step

The weaker concrete geometric target is now (P): for every epsilon>0,
prove P(K_n>n^epsilon)->0 at p_c on Z^3, with the exact induced-box
definition. An expectation estimate is sufficient but not required for
the new forward theorem. Separately, investigate whether the reverse
transfer from an existing X exponent to a one-arm exponent can be
recovered under (P), without assuming arm-ratio regularity. Keep that
question separate from the theorem proved here.

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 01:19 Asia/Tbilisi.
