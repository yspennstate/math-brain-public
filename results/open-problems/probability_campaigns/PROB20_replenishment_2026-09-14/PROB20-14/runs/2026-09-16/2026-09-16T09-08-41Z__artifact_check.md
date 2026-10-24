# PROB20-14 artifact execution certificate

**Status:** consistency check only; not proof evidence for the infinite-variance theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/kesten_entropy_budget_check_20260916.py`

The checker was executed after the substantive Markdown report was delivered. It uses exact rational arithmetic for all Galton–Watson and Dwass probabilities for the critical finite-support law

\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4,
\]

at fixed level \(k=2\), and floating-point logarithms only for the entropy identity itself. It checks:

1. the ordinary \((N_2,Z_2)\) prefix law sums to one;
2. \(b p_2(a,b)\) is a probability law (critical Kesten size-bias);
3. the conditioned prefix law obtained from the branching/forest decomposition sums exactly to one;
4. for every positive-mass prefix, the exact likelihood-ratio identity
   \[
   \frac{q_{n,2}(a,b)}{b p_2(a,b)}
   =\frac n{n-a}\frac{\Pr(S_{n-a}=n-a-b)}{\Pr(S_n=n-1)};
   \]
5. the entropy/local-cost identity
   \[
   D(\widetilde q_{n,2}\|\widehat p_2)
   +\mathbb E I_{n-A}(B)
   =\lambda_n-\log c_{n,2}
    +\mathbb E\log\frac n{n-A};
   \]
6. for \(r=1/2\), the weighted-density identity
   \[
   \mathbb E_{q_{n,2}} B^r
   =\mathbb E_{\widehat p_2}[B^rR_{n,2}].
   \]

Execution output:

```text
critical law PI={0:1/2,1:1/4,3:1/4}; k=2; r=1/2
n=8 a_n=0.116455078125 c=1 KL=0.44860568030776 E_local=2.28513709024262 rhs=2.73374277055038 gap=0 EBr=1.60698550375731 KestenWeighted=1.60698550375731 L1=0.638839753668763
n=10 a_n=0.0979804992675781 c=1 KL=0.24060046986887 E_local=2.50534488463388 rhs=2.74594535450275 gap=4.44e-16 EBr=1.66098876282262 KestenWeighted=1.66098876282262 L1=0.465861945201479
n=12 a_n=0.0930933952331543 c=1 KL=0.136985072482109 E_local=2.5800852230671 rhs=2.71707029554921 gap=0 EBr=1.72836322277986 KestenWeighted=1.72836322277986 L1=0.38645818126988
n=20 a_n=0.0719007141378825 c=1 KL=0.040752399604637 E_local=2.78306159375081 rhs=2.82381399335544 gap=-4.44e-16 EBr=1.81880094193365 KestenWeighted=1.81880094193365 L1=0.212177988162795
n=30 a_n=0.0589570392613316 c=1 KL=0.0166514468600036 E_local=2.93790800828718 rhs=2.95455945514718 gap=0 EBr=1.86102644887242 KestenWeighted=1.86102644887242 L1=0.135885121845102
ALL_ASSERTIONS_PASSED
```

The finite-support law does **not** satisfy the target infinite-variance hypothesis, so these checks certify only the algebra/indexing of the new identities and implementation. They are not independent verification of the universal statement.