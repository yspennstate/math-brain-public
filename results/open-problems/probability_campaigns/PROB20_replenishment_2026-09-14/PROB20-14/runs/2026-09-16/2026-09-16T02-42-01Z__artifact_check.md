# PROB20-14 — exact Laplace/Cramér duality checker execution

**Status:** finite-support consistency certificate only; **not** proof evidence for the universal infinite-variance theorem.

Artifact:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/exact_laplace_cramer_duality_check.py`

Artifact creation commit: `2f5391b739ee5cb0d0c14e6035510fd5323a3376`  
Artifact SHA-specific readback blob: `9f22d0bb2eea0e300f6ed4706fdf8b9061741127`

The script was executed locally with the Python standard library on the critical finite-support test law
\[
\Pr(\xi=0)=1/2,\quad \Pr(\xi=1)=1/4,\quad \Pr(\xi=3)=1/4,
\]
which has \(\mathbb E\xi=1\) and span \(h=1\). It checks numerically:

1. \(T(e^{-\Lambda(\theta)})=e^{-\theta}\);
2. \(K(\Lambda(\theta))=\theta-\Lambda(\theta)\) for \(h=1\);
3. the direct variational definition \(I_M(b)=\sup_t\{bK(t)-Mt\}\) against the formula \((M+b)H(b/(M+b))\).

Actual stdout:

```text
critical_mean 1.0
transform_checks
  theta=0.05 Lambda=0.00184320295427 T=0.951229424501 K=0.0481567970457
  theta=0.2 Lambda=0.0278888558307 T=0.818730753078 K=0.172111144169
  theta=0.7 Lambda=0.276514138622 T=0.496585303791 K=0.423485861378
  theta=1.5 Lambda=0.917606386925 T=0.223130160148 K=0.582393613075
cramer_checks
  M=20 b=2 direct=0.0619187412292 formula=0.0619187412292 t*=0.00287840621617 theta*=0.0626218404829
  M=20 b=8 direct=0.822897177668 formula=0.822897177668 t*=0.0321213432156 theta*=0.215286850397
  M=100 b=15 direct=0.673085692618 formula=0.673085692618 t*=0.00605375982869 theta*=0.0912845362827
ALL_ASSERTIONS_PASSED
```

The direct and formula values agree to floating precision on all tested pairs. This checks algebra/indexing only and does not validate any asymptotic universal claim.
