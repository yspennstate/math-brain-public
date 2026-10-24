# PROB20-14 artifact execution certificate

**Execution timestamp:** 2026-09-16T06:40:38Z  
**Status:** PASSED (numerical/algebra consistency only; not proof evidence)

Executed artifact source:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/variance_sensitive_correlation_exactrun_20260916.py`

- creation commit: `9c21cb3218a5c200560c49cbc0e7587e1c94087f`
- SHA-specific readback blob before execution: `44558edc4566b579e6fd1b9478e94b588bd1af33`

The script uses the genuine infinite-support critical law with `q=3/2`,

`P(xi=2^j)=c/(j^2 2^(qj))`, `c=1/4`, `j>=1`,

and chooses masses at 0 and 1 so total mass and mean both equal one. Its q-moment is finite because the tail q-moment is proportional to `sum 1/j^2`, while its second moment is infinite because it is proportional to `sum 2^((2-q)j)/j^2`.

Observed initialization:

```text
A tail mean 0.2254149446279583
B tail prob 0.09774626159946606
p0 0.12766868302849224
p1 0.7745850553720417
sum 1.0
```

For each tested admissible `n`, the exact central conditioning marginal was computed from finite polynomial convolutions (offspring values above `n-1` cannot occur on `S_n=n-1`). The script checked the conditioned marginal sums to one, has exact mean `1-1/n` to floating tolerance, and satisfies the data-processing inequality

`lambda_n - n D(mu_n||pi) >= -log mu_n^{*n}(n-1)`.

Outputs:

```text
n=32
lambda=2.048661456695926
x=nKL=0.09219799440785517
TC exact=1.9564634622880708
target atom=0.14625660355931855
-log target=1.9223926413471675
R=1.9650324234536374
V=0.7745850553720417
max atom=0.14625660355931855
max*sqrt(nV)=0.7281570014784736
0.5log(nV)=1.6051540486816753

n=64
lambda=2.442386887605707
x=nKL=0.06770284312479707
TC exact=2.37468404448091
target atom=0.09568282149392582
-log target=2.346716500356683
R=2.267492790846883
V=1.1281384459653154
max atom=0.09568282149392582
max*sqrt(nV)=0.8130273590665249
0.5log(nV)=2.139725982344486

n=128
lambda=2.837169097248752
x=nKL=0.056441005827878934
TC exact=2.780728091420873
target atom=0.06343753865049295
-log target=2.757699500477362
R=2.6101949429525284
V=1.1281384459653154
max atom=0.06367891677945879
max*sqrt(nV)=0.7652121408184264
0.5log(nV)=2.4862995726244588

n=256
lambda=3.2279373859896476
x=nKL=0.050032025042298145
TC exact=3.1779053609473493
target atom=0.042560247408085325
-log target=3.156834620805745
R=3.001977854134725
V=1.1281384459653154
max atom=0.04281328618831293
max*sqrt(nV)=0.7275783146685971
0.5log(nV)=2.8328731629044315
```

All programmed assertions passed. The finite numerical values are only a consistency/reproducibility check for the exact formulas and inequalities in the report; they are not an independent verification of the asymptotic theorem and do not settle PROB20-14.
