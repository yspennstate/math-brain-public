# PROB20-14 — exact Palm switching artifact check

**Status:** finite-support exact-arithmetic consistency certificate; **not** a proof of the universal theorem.

**Artifact:** `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/palm_switching_self_normalization_check.py`

The checker was executed with Python `fractions.Fraction` arithmetic for the critical law
\[
\pi_0=11/20,\qquad \pi_1=1/5,\qquad \pi_2=3/20,\qquad \pi_5=1/10,
\]
which has total mass 1 and mean 1, with `n=18` and `d=5`.

It checks exactly:

1. the conditioned count-vector normalizer equals \(a_n=\Pr(S_n=n-1)\);
2. \(\mathbb E_QN_d=n\pi_dR_{n,d}\);
3. the summed renewal-switching identity
   \[
   \frac{1}{\pi_d}\mathbb E_Q[N_dH_{n,d}(N_0)]
   =\mathbb E_Q\mathcal O_{n,d};
   \]
4. the \(N_d\)-Palm law of \(N_0\) agrees pointwise with the direct law of the zero count among \(n-1\) iid offspring variables conditioned on \(S_{n-1}=n-1-d\);
5. the self-normalized identity
   \[
   R_{n,d}\,\mathbb E^*_{n,d}[nH_{n,d}(N_0)]
   =\mathbb E_Q\mathcal O_{n,d}.
   \]

## Exact execution output

```text
a_n = 1014718218066649829403/16384000000000000000000 0.06193348498941954
b_nd = 87526183002115186461/1638400000000000000000 0.05342174255500194
R = 914589164076438730/1060311617624503479 0.8625663897991255
E N_d = 548753498445863238/353437205874834493 1.5526195016384259
occupation = 382098377817242904773/368988442933327210692 1.0355293915974613
E[N_d H]/pi_d = 382098377817242904773/368988442933327210692 1.0355293915974613
Palm law equals direct residual conditional law: True
Palm nH = 22476375165720170869/18722178182270628120 1.2005213788107552
R * Palm nH = 382098377817242904773/368988442933327210692 1.0355293915974613
Palm self-normalization identity exact: True
```

All assertions passed. This validates the algebra implemented in the artifact on this finite example only; the analytic inequalities and universal quantifiers in the mathematical report remain author-side proofs, not numerically established facts.
