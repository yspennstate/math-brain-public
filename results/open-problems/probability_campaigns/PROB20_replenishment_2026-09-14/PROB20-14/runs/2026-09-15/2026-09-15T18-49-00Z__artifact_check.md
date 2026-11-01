# PROB20-14 artifact execution certificate — 2026-09-15T18:49:00Z

**Status:** consistency check passed; this is not proof of the universal theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/truncated_palm_boost_check.py`

Artifact commit: `ebeac77a277ee8ea02d914b71cfd0013931b4efd`  
Artifact blob: `e56514caf0649842110beceedc96f16cfe4ebe00`

The script was executed in the task runtime using exact `Fraction` arithmetic for the finite-support distribution and floating evaluation only for the displayed exponential/logarithmic quantities. It uses the critical law

\[
(\pi_0,\pi_1,\pi_2,\pi_5)
=(11/20,1/5,3/20,1/10),
\]
so \(\mathbb E\xi=1\), and verifies exactly that
\[
\mathbb E(\xi-1)_+=\pi_0=11/20.
\]

Run parameters were \(q=3/2\), \(N=200\), \(d=40\), \(\eta=0.2\), \(\kappa=0.2\). The exact dynamic program for \(\sum_{i=1}^N(\xi_i-1)_+\) and the truncated one-sided Chernoff calculation produced:

```text
E[Y]= 0.55 pi0= 0.55
lower_tail_exact= 0.3379804334085863
truncated_Chernoff_bound= 0.9126265014311828
bound_valid= True
log_falling_factor_product= 8.160600133892892
d^2/N= 8.0
boost_ratio= 1.0200750167366115
```

Thus the concrete finite-support instance satisfies the Lemma 4.1 upper bound, and the exact falling-factor product on the tested Palm-good state has positive logarithm of the predicted \(d^2/N\) order. These checks only guard the algebra/implementation; the report's universal claims rest on the written proofs, not on numerics.
