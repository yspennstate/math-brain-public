# PROB20-14 artifact execution certificate

**Status:** consistency check only; not proof evidence for the infinite-variance theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/entropy_categorical_prefix_check_20260916.py`

Artifact creation commit: `93060ef3d4c2b9f4b72b0cc1bb4e6aaaf2747774`  
Artifact readback blob: `ce307a0252d13846b57c22e189cff7a74dc4a927`

The script was executed after the substantive Markdown report was delivered. It uses the critical finite-support law
\[
\Pr(\xi=0)=0.4,\quad \Pr(\xi=1)=0.4,\quad
\Pr(\xi=2)=0.1,\quad \Pr(\xi=4)=0.1,
\]
whose mean is exactly one. It checks:

1. the one-sided entropy-retention inequality from Lemma 3.1;
2. the pre-optimization categorical tilted-entropy inequality underlying Theorem 6.1 for the simultaneous categories \(\{2\}\) and \(\{4\}\);
3. the exact \(k=1\) prefix/forest entropy decomposition using Dwass for the forest probability.

Execution output:

```text
PROB20-14 consistency checks: PASS
n=12 a_n=0.097370898432 x_n=0.0493493257954 retention=0.125568205911>=0.090705640008 cat_rhs=-1.22826402818 theta*=0.548 prefix+forest=4.81413454683 total=4.81413454683
n=20 a_n=0.0753733668144 x_n=0.0277082796313 retention=0.135480497667>=0.0934326698427 cat_rhs=-2.08702279209 theta*=0.555 prefix+forest=5.58103356519 total=5.58103356519
n=40 a_n=0.0533019317559 x_n=0.0133784347446 retention=0.142765003956>=0.0944836229557 cat_rhs=-4.21203917748 theta*=0.558 prefix+forest=6.62066215951 total=6.62066215951
```

All assertions passed. These calculations validate algebra/indexing on a finite-support test law only and are not an independent verification of the arbitrary infinite-variance result.
