# Scoped audit of w456's C0048 attempt

Auditor: w457. Date: 2026-10-10. Native independent derivations were saved before reading the paired proof. Exact paired snapshot and SHA-256 are in review/provenance.json. w458 independently issued concordant finite/conditional KEEP verdicts for the paired L1--L5 and kept w457's FK/S3 obstructions. Local receipts are in review/w458_verdict_snapshot.json; no different-model approval is attested.

**Verdict: KEEP the finite-volume identities, conditional reduction, and scalar mean-field special case. No parent-problem solution is established.**

The audited source is w456/ATTEMPT.md as snapshotted in review/w456_ATTEMPT_snapshot.md. The following checks are mathematical derivations, not source-hash checks.

| Paired claim | Audit and exact scope |
| --- | --- |
| L1: field cumulants | KEEP for finite graphs with free boundary, zero field and independent uniform FK cluster colors. Independent derivation is CUBIC_OBSTRUCTION.md. In particular the fourth-order term includes 3*a2^2*Var(S2). It does not apply without alteration to fixed-color wired clusters, whose conditional color mean is nonzero. |
| L2: bare cubic obstruction | KEEP. The positive finite-volume third cumulant also occurs at beta=0. No critical magnetization conclusion follows from its sign alone. |
| L3: Legendre expansion and incompatibility | KEEP with finite-volume/local scope. Cauchy-Schwarz gives S2^2<=N*S3; the ratio constant q(q-2)/(6(q-1)A) is correct. Positivity I>=0 at the stated test point gives A<=2C/b^2 when r0>=b/(2C). A uniform finite-volume analytic neighborhood is not proved. |
| L4: cubic exclusion | KEEP. Stationarity gives a=(3/2)b_t*m-R'(m)/(2m). Substitution gives F(m)>=b*m^3/2-3C*m^4. The exclusion uses strict m<b/(6C), interior stationarity and F(m)<=F(0). It also handles C=0 correctly. |
| L5: critical endpoint | KEEP as a conditional implication for each fixed q,d. The constants delta,r0,b,C must be identical across the whole right neighborhood of beta_c. Upper semicontinuity from decreasing continuous wired finite-volume magnetizations plus monotonicity proves right continuity. Independent detail establishing the infinite-volume identity is ATTEMPT.md I2. |
| Entropy constants | KEEP for the stated scalar mean-field special case. Differentiation gives J_q''''=2(q-1)/q*[(q-1)^3/(1+(q-1)m)^3+(1-m)^(-3)]. At q=3,r0=1/2, K=64/3, C=8/9 and b=1/3; the exclusion threshold is 1/16. |

The minimal missing premise is exactly SP(q,d): a differentiable scalar potential for the **actual** monochromatic Gibbs magnetization, an interior stationary/minimizing link, a cubic coefficient bounded below by the same positive b, and value/derivative quartic remainder bounds on the same interval, uniformly as beta decreases to beta_c. The physical-potential identification is part of the premise; it cannot be obtained merely by naming the finite-volume Legendre transform or by replacing spatial correlations with independent-color entropy.

w456 leaves this premise open, so there is no invalid completed proof to reject. Our independent S3-invariant example F_t(z)=-t|z|^2+|z|^(5/2)-Re(z^3)+|z|^4 shows concretely how continuous onset survives a fixed cubic polynomial term when the uniform remainder is absent. It is a toy potential, not a lattice model. The exact finite-FK one-arm example in ATTEMPT.md I1 similarly prevents a local-positivity shortcut from filling SP.

A separate source-scope caution: Biskup--Chayes, *Rigorous Analysis of Discontinuous Phase Transitions via Mean-Field Bounds*, Theorem 2.1, establishes a jump at J_t in sufficiently high dimension. Its following paragraph explicitly does not establish zero magnetization at every J<J_t. That theorem alone should therefore not be used to identify J_t with the critical onset or to supply SP(3,3). This does not contradict the theorem or settle what later results establish. [Primary paper, printed pp.63–64](https://www.math.ucla.edu/~lchayes/lchayes_website_folder/old_publications_folder/bc_mft.pdf).

NEXT: Attack SP(3,3)'s uniform cubic ratio and C1 remainder for the actual constrained lattice potential.
