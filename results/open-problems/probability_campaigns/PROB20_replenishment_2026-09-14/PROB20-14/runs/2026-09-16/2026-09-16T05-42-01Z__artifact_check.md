# PROB20-14 — correlation-budget checker execution certificate

**Status:** finite-support algebra/indexing consistency check only; not proof evidence for the infinite-variance theorem.

Checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/correlation_budget_check_20260916.py`

Creation commit: `493b0088a037de8e671b0a37150c96cdf321e3c4`  
SHA-specific readback blob: `77486657c6aa5fdb1167170f06ed19bf77f45b87`

The checker was actually executed after the substantive Markdown report had already been delivered. It uses exact `Fraction` convolutions for the critical finite-support test law
\[
\pi_0=1/2,\qquad \pi_1=1/4,\qquad \pi_3=1/4.
\]
It checks:

1. the numerical chain-rule identity
   \[
   D(Q_n\|\mu_n^{\otimes n})=\lambda_n-nD(\mu_n\|\pi);
   \]
2. the data-processing lower bound
   \[
   D(Q_n\|\mu_n^{\otimes n})\ge -\log \mu_n^{*n}(n-1);
   \]
3. the bounded `sqrt(n) * max atom` concentration diagnostic for the product marginal;
4. for the hard mark `g=1_{xi=3}`, the tilted Bernoulli data-processing inequality
   \[
   nD(\operatorname{Ber}(\alpha)\|\operatorname{Ber}(\rho_\theta))
   \le nD(\mu_n\|\pi)-\theta+n\Lambda(\theta)
   \]
   at \(\theta=0.1,0.3,0.7\).

Execution output:

```text
critical test law: pi(0)=1/2, pi(1)=1/4, pi(3)=1/4
n= 8 a_n=0.116455078125 lambda=2.150249676 nDmu=0.046061605 corr=2.104188070 -log(mu^n center)=2.100196178 sqrt(n)*maxatom=0.346291142
  theta=0.1: n KL(Ber(alpha)||Ber(rho_theta))=0.002242582 <= nD(mu||pi)-theta+nLambda=0.003996498
  theta=0.3: n KL(Ber(alpha)||Ber(rho_theta))=0.213947166 <= nD(mu||pi)-theta+nLambda=0.228289633
  theta=0.7: n KL(Ber(alpha)||Ber(rho_theta))=1.374379545 <= nD(mu||pi)-theta+nLambda=1.558174714
n=10 a_n=0.0979804992676 lambda=2.322986807 nDmu=0.051530576 corr=2.271456231 -log(mu^n center)=2.254917713 sqrt(n)*maxatom=0.343034896
  theta=0.1: n KL(Ber(alpha)||Ber(rho_theta))=0.000818648 <= nD(mu||pi)-theta+nLambda=0.023949192
  theta=0.3: n KL(Ber(alpha)||Ber(rho_theta))=0.241511243 <= nD(mu||pi)-theta+nLambda=0.354315610
  theta=0.7: n KL(Ber(alpha)||Ber(rho_theta))=1.643163404 <= nD(mu||pi)-theta+nLambda=2.116671963
n=12 a_n=0.0930933952332 lambda=2.374152040 nDmu=0.030140161 corr=2.344011879 -log(mu^n center)=2.342178618 sqrt(n)*maxatom=0.332962538
  theta=0.1: n KL(Ber(alpha)||Ber(rho_theta))=0.010136442 <= nD(mu||pi)-theta+nLambda=0.017042500
  theta=0.3: n KL(Ber(alpha)||Ber(rho_theta))=0.373994481 <= nD(mu||pi)-theta+nLambda=0.453482201
  theta=0.7: n KL(Ber(alpha)||Ber(rho_theta))=2.209202869 <= nD(mu||pi)-theta+nLambda=2.648309824
n=14 a_n=0.0850813239813 lambda=2.464147727 nDmu=0.028149288 corr=2.435998439 -log(mu^n center)=2.431784659 sqrt(n)*maxatom=0.331814083
  theta=0.1: n KL(Ber(alpha)||Ber(rho_theta))=0.016386626 <= nD(mu||pi)-theta+nLambda=0.029535351
  theta=0.3: n KL(Ber(alpha)||Ber(rho_theta))=0.463587611 <= nD(mu||pi)-theta+nLambda=0.572048335
  theta=0.7: n KL(Ber(alpha)||Ber(rho_theta))=2.651023643 <= nD(mu||pi)-theta+nLambda=3.199347229
n=20 a_n=0.0719007141379 lambda=2.632469082 nDmu=0.019235254 corr=2.613233827 -log(mu^n center)=2.610831471 sqrt(n)*maxatom=0.329210102
  theta=0.1: n KL(Ber(alpha)||Ber(rho_theta))=0.046774907 <= nD(mu||pi)-theta+nLambda=0.064072487
  theta=0.3: n KL(Ber(alpha)||Ber(rho_theta))=0.775294842 <= nD(mu||pi)-theta+nLambda=0.924805322
  theta=0.7: n KL(Ber(alpha)||Ber(rho_theta))=4.083316883 <= nD(mu||pi)-theta+nLambda=4.849518027
ALL ASSERTIONS PASSED
```

The computation is a reproducibility check only. It does not test the infinite-variance quantifiers, uniform integrability, or the asymptotic shell-localization theorem.
