# PROB20-14 — random-prefix forest identity checker execution

**Status:** consistency check passed; this is **not** proof evidence for the universal infinite-variance theorem.

**Artifact:** `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/random_prefix_forest_identity_check.py`  
**Artifact commit:** `e7d56374e7e3f321064128a9740e1f90eb88b822`  
**Artifact blob:** `924c90cf98e3ea6c90a03cc8debbf9ea54739320`

The script was executed on the critical finite-support law
\[
(\pi_0,\pi_1,\pi_3)=(1/2,1/4,1/4),
\qquad r=1/2,
\]
for the fixed level `k=2`. It enumerates the exact first-two-level prefix law with rational probabilities, computes total-progeny probabilities by Dwass with exact `Fraction` arithmetic, and compares the two sides of the new random-prefix identity
\[
\mathbb E[Z_2(T_n)^r]
=
m_{2,r}
\frac{\Pr(A_2+X_1+\cdots+X_{B_2}=n)}{\Pr(|T|=n)}.
\]

Observed values:

| n | conditioned `E[Z_2^r]` | random-prefix RHS |
|---:|---:|---:|
| 5 | 1.1722472488397357 | 1.1722472488397357 |
| 8 | 1.6069855037573110 | 1.6069855037573109 |
| 10 | 1.6609887628226203 | 1.6609887628226203 |
| 15 | 1.7752602754075450 | 1.7752602754075450 |
| 20 | 1.8188009419336530 | 1.8188009419336528 |

The asserted relative/absolute tolerance was `1e-13`; every test passed.

The same execution produced
\[
m_{2,r}=0.5588169965473758,
\qquad
\mathbb E A_2=3.3888762277166045,
\qquad
\mathbb E B_2=3.4667432356417502.
\]

These finite-support calculations check the algebra and indexing of the exact decomposition only. They do not test the infinite-variance endpoint, the asymptotic local-ratio theorem, or independence beyond what is encoded in the finite enumeration.
