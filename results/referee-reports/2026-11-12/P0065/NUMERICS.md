Law key: 12 means p1=p2=1/2; 24 means p2=p4=1/2; 123 is uniform on {1,2,3}; geom means pk=2^(-k), k>=1.


## Numerical table 1: exact absorbing-chain check


| Tree | Interior vertices | lambda=0 | 1/3 | 1 | 3/2 | 3 | Agreement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1 | 99/119 | 5/9 | 32/77 | 1/5 | 5/5 exact |
| 2 | 3 | 1 | 135/163 | 7/13 | 68/173 | 13/73 | 5/5 exact |
| 3 | 4 | 1 | 1053/1193 | 23/35 | 344/659 | 23/83 | 5/5 exact |
| 4 | 9 | 1 | 43173/49204 | 137/228 | 1640/3889 | 85/596 | 5/5 exact |
| 5 | 12 | 1 | 645441291/784492043 | 8481/18167 | 2187712/8000077 | 2077/37165 | 5/5 exact |


Tree notation: `()` is a boundary vertex; a tuple lists its children. Each tree has mixed degrees.

`[(((),), ((), (), ())), (((),), ((), ())), (((), (), ()), ((),), ((), ())), ((((),), ((), ())), (((), (), ()),), (((), ()), ((),))), (((((),),), (((), ()), ((), (), ()))), ((((), (), ()), ((), ()), ((),)),))]`


Command: `python3 audit_exact.py`. Fraction Gaussian elimination solves the walk equations, independently of the escape recursion. All 25 results agree exactly.


## Numerical table 2: contraction and derivatives


| k | r/k | delta12 / bound | eta12 / bound | delta20 / bound | eta20 / bound |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.3 | 2.170e-08 / 5.314e-07 | 8.162e-07 / 1.153e-04 | 5.163e-15 / 3.487e-11 | 3.266e-13 / 1.295e-08 |
| 1 | 0.6 | 3.789e-05 / 2.177e-03 | 6.311e-04 / 3.065e+00 | 1.466e-09 / 3.656e-05 | 4.284e-08 / 8.880e-02 |
| 1 | 0.9 | 1.524e-03 / 2.824e-01 | 1.355e-02 / 9.355e+04 | 1.203e-06 / 1.216e-01 | 2.050e-05 / 6.956e+04 |
| 2 | 0.3 | 1.223e-08 / 5.314e-07 | 2.313e-07 / 5.767e-05 | 3.014e-14 / 3.487e-11 | 9.578e-13 / 6.475e-09 |
| 2 | 0.6 | 2.438e-05 / 2.177e-03 | 2.115e-04 / 1.532e+00 | 1.185e-08 / 3.656e-05 | 1.768e-07 / 4.440e-02 |
| 2 | 0.9 | 1.318e-03 / 2.824e-01 | 6.684e-03 / 4.678e+04 | 1.286e-05 / 1.216e-01 | 1.174e-04 / 3.478e+04 |
| 3 | 0.3 | 2.022e-08 / 5.314e-07 | 2.561e-07 / 3.845e-05 | 1.034e-13 / 3.487e-11 | 2.204e-12 / 4.317e-09 |
| 3 | 0.6 | 4.280e-05 / 2.177e-03 | 2.509e-04 / 1.022e+00 | 4.703e-08 / 3.656e-05 | 4.762e-07 / 2.960e-02 |
| 3 | 0.9 | 2.481e-03 / 2.824e-01 | 8.541e-03 / 3.118e+04 | 6.014e-05 / 1.216e-01 | 3.757e-04 / 2.319e+04 |


| k | r/k | max abs b20 derivative | M | max y FD error | max delta/bound (all j) | max eta/bound (all j) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.3 | 1.00000000 | 2.04081633 | 8.403e-11 | 0.874548 | 0.700000 |
| 1 | 0.6 | 1.00000000 | 6.25000000 | 1.060e-10 | 0.783339 | 0.400000 |
| 1 | 0.9 | 1.00000000 | 100.00000000 | 1.125e-10 | 0.713171 | 0.100000 |
| 2 | 0.3 | 0.50000000 | 1.02040816 | 2.224e-11 | 0.874548 | 0.700000 |
| 2 | 0.6 | 0.50000000 | 3.12500000 | 2.937e-11 | 0.783339 | 0.400000 |
| 2 | 0.9 | 0.50000000 | 50.00000000 | 3.822e-11 | 0.713171 | 0.100000 |
| 3 | 0.3 | 0.33333333 | 0.68027211 | 1.817e-11 | 0.874548 | 0.700000 |
| 3 | 0.6 | 0.33333333 | 2.08333333 | 2.305e-11 | 0.783339 | 0.400000 |
| 3 | 0.9 | 0.33333333 | 33.33333333 | 3.714e-11 | 0.713171 | 0.100000 |


Command: `python3 audit_contraction.py`. Each case: 384 roots, 17 lambda grid values, depths 1 through 20. Finite-depth trees use layered subtree sharing; unfolding is a valid tree, but samples are dependent. Supremum means the maximum of this test set, not the supremum over all trees. Centred differences use h=1e-5, including a rational continuation to negative h at zero. Every tested bound passed. Floating-point noise can dominate differences around 1e-16. The reported b20 derivative approximates beta; no finite test certifies an infinite-depth supremum.


## Numerical table 3: formula versus harmonic-ray entropy


| lambda | Formula, main pool | Formula, ray pool root sample | Ray n=120, root | Ray n=360, root | Ray n=360 after 20 levels |
| --- | --- | --- | --- | --- | --- |
| 0.3 | 0.3539020 ± 0.0000218 | 0.3557084 ± 0.0009514 | 0.3536291 ± 0.0002600 | 0.3541261 ± 0.0002252 | 0.3541918 ± 0.0002420 |
| 0.75 | 0.3706881 ± 0.0000571 | 0.3713079 ± 0.0005269 | 0.3701428 ± 0.0002321 | 0.3706156 ± 0.0002201 | 0.3708425 ± 0.0002147 |
| 1.2 | 0.3952165 ± 0.0000827 | 0.3952995 ± 0.0004747 | 0.3933556 ± 0.0001964 | 0.3948364 ± 0.0002010 | 0.3954323 ± 0.0002010 |


Commands: `python3 audit_ray.py 201` (and seeds 202–204), plus `python3 audit_pool.py 12 101` (and 102–104). The ray calculation uses 12,000 population nodes per level, 420 stored levels and 12,000 lazily unfolded rays per seed. Offspring and child indices are retained with their escape values. At each visited node choose child i with weight beta_i/sum beta and accumulate -log(weight). Thus the root column is literally -(1/n)log of prefix mass. The burn20 column estimates the same asymptotic rate after an initial segment. This uses harmonic-ray simulation, not a simulation of all backtracking steps of the original walk. Selected-child dependence is preserved.

The largest raw finite-n transient is at lambda=1.2; its reduction with n and after burn-in is visible. Main-pool formula and burn-in ray means agree within two combined standard errors at all three biases. The smaller ray pool has noisy one-root-sample formula estimates. Layer sharing, finite-pool bias and finite-depth effects are not included in the seed standard errors. This is an independent check of the entropy observable and stationary weighting, though it shares the escape recursion. It is not an independent proof of the source theorem.


## Numerical table 5: exact examples and constants


| Law | E 1/N | d0 | d0 prime |
| --- | --- | --- | --- |
| 12 | 0.75 | 0.34657359027997265470 | 0.02166084939249829091 |
| 24 | 0.375 | 1.03972077083991796412 | 0.02707606174062286364 |
| 123 | 0.61111111111111111111 | 0.59725315640935166693 | 0.04954268583459163943 |
| geom | 0.69314718055994530941 | 0.50783392286843839218 | 0.05495944237138239886 |


Binary 1/2 law: slope = log(2)/32. Binary 2/4 law: slope = 5 log(2)/128. Geometric slope rounds to 0.05496. Command: `python3 audit_exact.py`; mpmath precision 70 digits, geometric series through k=400. Tail contributions to the required logarithmic sums are below 1.6e-118, using log k<=k and sum_(k>400) k 2^-k=402*2^-400. The geometric a=log 2 also follows from -log(1-z)=sum z^k/k at z=1/2.


## Numerical table 6: slope reproduction


| Law | Exact d0 | Exact slope | Pool RHS [eq:quot] at 0 | Paired quotient at .02m |
| --- | --- | --- | --- | --- |
| 12 | 0.346573590 | 0.021660849 | 0.0215422 ± 0.0000800 | 0.0217605 ± 0.0000786 |
| 24 | 1.039720771 | 0.027076062 | 0.0270721 ± 0.0000246 | 0.0270596 ± 0.0000251 |
| 123 | 0.597253156 | 0.049542686 | 0.0495387 ± 0.0000636 | 0.0498311 ± 0.0000640 |
| geom | 0.507833923 | 0.054959442 | 0.0550698 ± 0.0000586 | 0.0561357 ± 0.0000602 |


Runs: `python3 audit_batch.py`, which serially executes `python3 audit_pool.py LAW SEED` for LAW in 12,24,123,geom and SEED in 101,102,103,104, then the four ray runs. Existing completed JSONs are skipped. A full fresh run is under five minutes here. Each numerical script and the driver have 280-second alarms. Pool settings: 40,000 entries, 180 synchronous sweeps, evaluations averaged over the last 40 sweeps, 14 coupled lambda values. All ± values are sample standard deviation of four seed means divided by 2.

The displayed dimensions use exact d0 as a control variate: d_est(lambda)=d_raw(lambda)-d_raw(0)+d0_exact. The quotient is consequently the paired empirical difference quotient, not a noisy quotient against an unrelated baseline. Raw values remain in each pool JSON. Averaging across sweeps reduces Monte Carlo error but does not remove finite-pool bias; the four-seed SE is not a bound on systematic error.


| Law | Paper vs ours pool z | Paper vs ours quotient z | Paper pool vs exact slope z | Paper quotient vs exact slope z | Our pool vs exact slope z |
| --- | --- | --- | --- | --- | --- |
| 12 | 1.239 | 1.244 | 0.974 | 1.510 | 1.483 |
| 24 | 0.668 | 0.628 | 0.652 | 0.547 | 0.163 |
| 123 | 1.376 | 1.452 | 1.463 | 0.014 | 0.062 |
| geom | 1.044 | 1.035 | 1.227 | 2.968 | 1.884 |


For paper-vs-ours comparisons z uses sqrt(SE_paper^2+SE_ours^2). For comparisons against the exact slope it uses the single stated SE. All published pool means and positive-bias quotients are within two combined SE of ours. Every published pool mean is within two of its own SE of the exact slope. The geometric positive-bias quotient is 2.97 SE above the exact slope; it estimates a different, curved-parameter quantity. Two-SE intervals with four seeds are descriptive, not a strong coverage guarantee.


### Curvature at zero


| Law | Expansion d2(0) | (dprime(.0025m)-dprime(0))/.0025m | same, .005m | same, .01m | 2(d(h)-d(0)-h*dprime(0))/h^2, h=.0025m | Richardson, 2*small-double |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.014158668 | 0.0141386 ± 0.0001754 | 0.0142335 ± 0.0001748 | 0.0144233 ± 0.0001737 | 0.0141069 ± 0.0001756 | 0.0140437 ± 0.0001759 |
| 24 | -0.000458229 | -0.0004368 ± 0.0000266 | -0.0004318 ± 0.0000265 | -0.0004223 ± 0.0000264 | -0.0004386 ± 0.0000266 | -0.0004419 ± 0.0000267 |
| 123 | 0.013913092 | 0.0140091 ± 0.0001881 | 0.0141528 ± 0.0001867 | 0.0144350 ± 0.0001841 | 0.0139608 ± 0.0001885 | 0.0138654 ± 0.0001894 |
| geom | 0.051763479 | 0.0521461 ± 0.0002884 | 0.0524117 ± 0.0002883 | 0.0529433 ± 0.0002881 | 0.0520576 ± 0.0002885 | 0.0518805 ± 0.0002886 |


Command: `python3 audit_curvature.py`; the pool estimates use the already saved near-zero runs. The independent symbolic expansion and the two different finite-difference calculations agree in scale and sign; first-order finite-difference errors are visible as h increases. The last column cancels that first-order error using paired h and 2h estimates. Geometric curvature shifts the .04 quotient by about .00103527, yielding .05599471 at quadratic order, with higher-order corrections remaining. The published .05677 ± .00061 is compatible with curvature plus sampling noise. No numerical error is identified.


### Dimension grid


| Law | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.346574 | 0.349992 | 0.353902 | 0.358505 | 0.364030 | 0.370688 | 0.378499 | 0.386997 | 0.395216 | 0.401995 |
| 24 | 1.039721 | 1.047825 | 1.055881 | 1.063806 | 1.071449 | 1.078602 | 1.085026 | 1.090486 | 1.094753 | 1.097573 |
| 123 | 0.597253 | 0.607504 | 0.618617 | 0.630655 | 0.643309 | 0.655843 | 0.667373 | 0.677280 | 0.685197 | 0.690716 |
| geom | 0.507834 | 0.520030 | 0.535207 | 0.554348 | 0.578034 | 0.605034 | 0.631816 | 0.655355 | 0.674242 | 0.687464 |


Standard errors over four seeds:


| Law | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.000000 | 0.000011 | 0.000022 | 0.000033 | 0.000045 | 0.000057 | 0.000067 | 0.000074 | 0.000083 | 0.000090 |
| 24 | 0.000000 | 0.000008 | 0.000018 | 0.000028 | 0.000040 | 0.000052 | 0.000065 | 0.000080 | 0.000097 | 0.000123 |
| 123 | 0.000000 | 0.000013 | 0.000027 | 0.000040 | 0.000049 | 0.000055 | 0.000059 | 0.000069 | 0.000089 | 0.000122 |
| geom | 0.000000 | 0.000014 | 0.000037 | 0.000071 | 0.000115 | 0.000162 | 0.000201 | 0.000231 | 0.000273 | 0.000362 |


| Law | log m | Every seed increasing | Every seed below log m | Mean gap at .9m |
| --- | --- | --- | --- | --- |
| 12 | 0.405465108 | True | True | 0.003470 |
| 24 | 1.098612289 | True | True | 0.001039 |
| 123 | 0.693147181 | True | True | 0.002432 |
| geom | 0.693147181 | True | True | 0.005683 |


The increase on this finite grid is numerical evidence only. It does not establish global monotonicity. These values reproduce the scale and trend of [tab:dim]; no attempt is made to reconstruct the authors' undisclosed seeds or raw outputs.
