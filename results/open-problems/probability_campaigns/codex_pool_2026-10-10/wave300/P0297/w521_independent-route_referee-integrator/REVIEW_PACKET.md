# P0297 referee packet, 2026-10-10

## Scope and source

Primary statement: Gwynne--Miller, *Existence and uniqueness of the Liouville quantum gravity metric for gamma in (0,2)*, Invent. Math. (2020), Problem 7.1. Compute d_gamma = dim_H(C,D_h) for gamma in (0,2), with xi_gamma=gamma/d_gamma. The metric is a length metric for a whole-plane GFF plus a continuous function. The known gamma=sqrt(8/3) dimension 4 is a proper special case. A 2026 ICM invited lecture still calls general d_gamma unknown. Primary URLs: https://link.springer.com/article/10.1007/s00222-020-00991-6 and https://epubs.siam.org/doi/10.1137/25M181012X .

The 2020 paper's Problem 7.1 explicitly says the Watabiki prediction is false for small gamma, citing Ding--Goswami. Therefore a derivation reproducing that formula cannot be accepted without explaining the rigorous contradiction.

## w519 W519-L1: KEEP, independently rederived

1. Read the two hypotheses as separate finite logarithmic limits; positivity ensures the logarithms exist.
2. Set b=aL. For each epsilon, log b/log epsilon = log a/log epsilon + log L/log epsilon.
3. Pass to the limits. The result is alpha+0=alpha.
4. Scope: this proves invariance of an exponent under a subpower factor. It gives no value for the unknown LFPP normalization exponent and therefore no value of d_gamma. No theorem-level parent claim is certified.

Evidence: `~/brain_workers/w519/CLAIMS.jsonl` W519-L1 and `ATTEMPT.md`, read 2026-10-10.

## w520 snowflake lemma in ATTEMPT.md: KEEP WITH SCOPE

1. For 0<a<1, (u+v)^a <= u^a+v^a, so D^a obeys the triangle inequality. Monotonic continuity of t^a preserves the topology.
2. For a cover by sets U_i, diam_{D^a}(U_i)^s = diam_D(U_i)^{as}; the mesh restriction transforms from delta to delta^(1/a). Thus H^s_{D^a,delta}=H^{as}_{D,delta^(1/a)} under the same diameter normalization, yielding dim_H(X,D^a)=dim_H(X,D)/a.
3. If D_{h+c}=exp(xi c)D_h, then (D_{h+c})^a=exp(a xi c)D_h^a. Hence (a xi)(d/a)=xi d=gamma. The reduced scalar identities alone do not determine d.
4. Crucial boundary: for D(s,t)=|s-t| on [0,1], **every** continuous path from 0 to 1 has infinite D^a-length. For any n, use first hitting times of levels k/n in order. The partition sum is n*(1/n)^a=n^(1-a), unbounded as n grows. Thus the snowflake is not a length metric and is not a competing canonical LQG metric. This does not refute metric uniqueness.

Evidence: `~/brain_workers/w520/ATTEMPT.md`, read 2026-10-10. The formal claim in `CLAIMS.jsonl` is only a correct scope guard and awaits the worker's primary-source citation update.

## Independent conditional route and requested cross-check

My `ATTEMPT.md` records the all-center ball-mass covering route before peer arguments were read. The compact-space covering lemma is in `CLAIMS.jsonl` as a sketch pending w524's audit. It is a standard conditional reduction. The all-center explicit exponent is the single hardest open piece; typical-point scaling or a self-referential d_gamma exponent cannot close it.

Requested w524 decision: KEEP/FIX/DROP the exact hypotheses and two inequalities in `w521.P0297.conditional-covering.001`. Please check the finite maximal separated set argument and the lower mass-distribution step; report whether any hidden full-support or ball convention assumption is needed. A KEEP certifies only this conditional lemma.

## Continuation audit of new claims

`VERDICTS.jsonl` records nine further claim-level verdicts: W519-L2/L3/L4/L5/C2, w520 .002/.003, and w518 C1/C2. The hardest source transfer was W519-L5: Falconer--Jin Corollary 2.3 applies to the disk's Lebesgue measure (dimension 2, gamma<2, disk satisfies A0); the log-potential conclusion then follows from W519-L2. Its scope is Euclidean balls. The w520 profile identity is exact algebra with positive denominator; Gwynne--Pfeffer Theorem 1.5 applies for each fixed alpha almost surely. It supplies no value of xi. The D0049-A001 historical row's wrong `d_gamma=2Q/xi` was directly read and corrected by the 10-versus-4 Brownian-map case.

No full proof of the parent problem has appeared in these claims. The source correction should land through w519's two-field patch after patch-level audit; this packet verifies the mathematical correction and the two source-row occurrences, not every field of that historical attempt.

## Parent verdict

P0297 remains OPEN/UNKNOWN after latest checked 2026 ICM statement; no current triad artifact computes d_gamma for general gamma. Hardest unresolved claim: a rigorous independent metric-geometric estimate fixing the exact exponent for every gamma in (0,2). Recheck all newer peer claims before any stronger verdict.
