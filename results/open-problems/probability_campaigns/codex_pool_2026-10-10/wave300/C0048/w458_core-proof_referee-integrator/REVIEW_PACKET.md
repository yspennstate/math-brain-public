# C0048 referee packet — w458, 2026-10-10

## Scope and source

Primary target: Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice* (2017), Conjecture 2, printed p. 93, https://www.ihes.fr/~/duminil/publi/2017PIMS.pdf. Its definition (printed p. 5) says discontinuity means positive spontaneous magnetization at beta_c. In the delta-spin normalization used by peers, p=1-exp(-beta). The source's simplex convention rescales beta, leaving the property unchanged. The 2026-09-07 intake marks C0048 attempted_unsolved; it is not a current proof or status certificate. Current openness: UNKNOWN. No parent-problem solution is claimed.

Review scope: w456/ATTEMPT.md, STATEMENT.md, CLAIMS.jsonl and w457/ATTEMPT.md, CUBIC_OBSTRUCTION.md, CLAIMS.jsonl. I independently rederived the load-bearing algebra. Author and referee response-side served-model metadata are unavailable. Requested model settings are not evidence of served identity.

## Verdicts

| Claim | Verdict | Exact scope | Remaining gap |
|---|---|---|---|
| w456 L1 | KEEP | Exact cumulant identities through order four on a finite free-boundary zero-field Potts graph, integer q>=2 | No uniform critical control |
| w456 L2-L3 | KEEP | Positive cubic sign alone is insufficient; local Legendre coefficient and moment inequality are correct | No uniform lattice potential or remainder |
| w456 L4 | KEEP | Algebraic stationary-minimum exclusion under fixed C1 quartic bounds, including C=0 | Hypotheses are unproved for actual Potts |
| w456 L5 | KEEP, conditional | SP(q,d) implies positive M(beta_c), using wired right continuity | SP(q,d) remains the hardest missing input |
| w456 SP(q,d) | FIX status | Retain as an explicit unproved conjectural input; mean-field calculation is only a special case | Physical stationarity/minimum link and uniform cubic/remainder |
| w457 I1 | KEEP | Exact finite-FK edge conditional/path bounds and subcritical local-to-global counterexample | No critical uniform bound |
| w457 I2 | KEEP, conditional | Wired critical right continuity and uniform-gap reduction | Uniform gap unproved |
| w457 cubic obstruction | KEEP | Abstract S3-invariant continuous-onset example; no Potts realization asserted | Cannot infer Potts behavior |

## Reproduction

For w456 L1, condition on FK clusters of sizes n_C. Each cluster's centered color-1 indicator Y_C has cumulants a2=(q-1)/q^2, a3=(q-1)(q-2)/q^3, a4=(q-1)(q^2-6q+6)/q^4. Conditional independence gives E[X^2|FK]=a2 S2, E[X^3|FK]=a3 S3, and E[X^4|FK]=a4 S4+3a2^2 S2^2. Subtract 3(E X^2)^2 **after** averaging: the fourth cumulant includes 3a2^2 Var(S2). At q=3 on a two-vertex edge with exp(beta)=2, independent spin and FK enumerations both give unnormalized cumulants (5/9, 7/27, -8/27). Run `python -X utf8 verify_exact.py` in this folder.

For w456 L3, invert m=P'(h): h=m/A-Bm^2/(2A^3)+O(m^3), integrate I'(m)=h, obtaining I(m)=m^2/(2A)-Bm^3/(6A^3)+O(m^4). Configuration-wise S2^2<=N S3; Jensen yields B/(6A^3)>=q(q-2)/(6(q-1)A). This lower bound alone can vanish as A grows. For L4, F'=0 gives a=(3/2)b_t m-R'/(2m), hence F(m)>=b m^3/2-3C m^4. The exclusion is strict for m<b/(6C), and holds for every interior m when C=0. L5 is a valid implication because finite-box wired M_N decrease with N, are continuous in beta, and are increasing in beta; M=inf_N M_N is right continuous.

For w457 I1, the conditional FK edge ratio is p or a=p/[p+q(1-p)]. The tower property and sequential exposure, rather than independence, give a^n<=P(path open)<=p^n. At q=d=3,p=1/10, a=1/28 and the path union bound gives f_N<=0.6(0.5)^(N-1), so local positivity does not imply percolation. For the free four-cycle at p=1/2,q=3, direct FK enumeration gives Z=258, edge marginal 11/43, all-open 1/86, joint/product ratio 2.71521754. This specifically refutes an upper product bound from FKG. For I2, finite wired f_N decrease in N; the inner-boundary event sandwich identifies inf_N f_N with infinite-volume theta_w. An infimum of continuous f_N is upper semicontinuous, and monotonicity in p gives right continuity.

For w457's S3 example, write r=|z| and s=sqrt(r). Since 1-s+s^3>=c=1-2/(3sqrt(3))>0, F_t(z)>=-t r^2+c r^(5/2). For t<=0 the zero state is the unique minimizer. For t>0 sufficiently small r yields negative F_t, while any minimizer with F_t<=0 obeys r<=(t/c)^2. The ordered radius thus tends to zero. The r^(5/2) term is outside the required uniform quartic Taylor remainder.

## Single missing lemma and next step

SP(q,d), or equivalently a uniform positive lower bound on wired percolation just above p_c, is the load-bearing missing input. For q=d=3 no peer supplied a bound uniform in volume and p-p_c. w456's mean-field entropy remainder (q=3: b=1/3, C=8/9, threshold 1/16) checks algebraically but does not control spatial correlations. The ordinary thermodynamic Legendre potential can have a coexistence flat segment, so it cannot silently stand in for w456's physical branch potential. The next mathematical step is to prove or disprove a fixed-scale, volume-uniform branch potential/remainder estimate for actual nearest-neighbor q=3,d=3, with an explicit source of the stationarity and minimum comparison.

No Lean theorem or formal-check receipt is claimed. Source/hash validation and finite enumeration are not mathematical proofs of C0048.
