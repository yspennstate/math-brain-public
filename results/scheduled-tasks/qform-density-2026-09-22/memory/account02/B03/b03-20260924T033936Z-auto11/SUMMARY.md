SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T03:39:36Z.
attacking: exact-rank-two aligned anchored collar: convert spread same-bank curvature into a literal three-volume crossing by an internal balanced physical cut, while preserving original-coordinate product provenance and whole-copy dependence.

# Memory snapshot

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: full QFORM OPEN; unrestricted continuity OPEN; this run proves a new target-valid family theorem and a localization obstruction.
Canonical report: `math-open-problems` commit `c9a27b38fff24b31ff9a53fc96abbf1770d5b42a`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/b03-20260924T033936Z-auto11/REPORT.md`.
Early calculation: `5dcc9adfba7d180451fd15a809f1c2c9faa7c36c`.

Main retained result: for m divisible by 4, m>=8, the aligned curved family

`Q_m=2h(<u1,U>+<v1,V>)+<u1,U>^2+<v1,V>^2+2<u1,U><v1,V>+2<u2,U><v2,V>`

has nonzero spectrum `{1+sqrt(3),1-sqrt(3),1,-1}` and is target-valid. A balanced original-coordinate repartition has physical cross `Z3=1/8`; three-volume row marginals are `1/2` at h and `5/(2m)` on bank rows. Pinned e5f71d79 Theorem D yields

`||p_Q||_infinity <= 6 sqrt(2e)`,

`int |t|^(-1/2)|phi_Q(t)|^2 dt <= (24/5)sqrt(2*pi)e^(1/4)2^(1/4)`,

`E|Q-Q'|^(-1/2) <= (24/5)e^(1/4)2^(1/4)`.

This is a positive witness that spread same-bank curvature in the aligned rank-two endpoint can become the missing third crossing direction after an internal physical cut.

Latest account03/B03 r47 was applied to the curvature-deleted companion. A literal zero pair has `mu=2/m`, Schur hub diagonal `d=-1`, principal-triple determinant `4/m^2`; r47 gives `||p||_infinity <=(144m^2)^(1/3)` and weighted time `<=4 sqrt(pi)12^(1/3)m^(1/3)`. These valid bounds diverge, furnishing a source-valid obstruction to an exhaustive localized-triple determinant scale.

Next implication: prove a universal aligned-collar structural alternative: quantitative internal E3 repartition versus cut-poor/concentrated curvature entering an already-paid aggregate/low-rank receiver. Do not infer a universal rank-three physical cut; that correction remains active. Do not use conditional conjugate-variable cap or post-rotation independence. Preserve `|phi_Q|^2=E exp(it(Q-Q'))` only for the whole scalar output.

Control refreshed through brain main `5f1e6da728bf518ab3dd2a42ab20a7a35fab9fed`; no later invalidating correction/stop observed. Brain status: `WITHOUT_VERIFIED_BRAIN`.
