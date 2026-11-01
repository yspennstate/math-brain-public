# PROB20-14 marked-factorial checker execution

**Status:** consistency check passed; this is not proof evidence for the universal infinite-variance theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/marked_factorial_replication_check.py`

Artifact creation commit: `a5daf45665e33d671a59bb43e12e1b3ea9913a92`  
SHA-specific readback blob: `1aff1875b6a1fda8a15bcacb4bd53f554cdc2611`

The script was executed after the mathematical report was delivered. It uses exact `Fraction` convolution arithmetic for the finite-support conditioned probabilities and floating evaluation only for exponential/logarithmic inequalities.

Test law:
\[
\Pr(\xi=0)=1/2,\qquad
\Pr(\xi=1)=1/4,\qquad
\Pr(\xi=3)=1/4,
\]
which is critical but finite-variance and is used only to check algebra/indexing.

Soft mark:
\[
g(0)=0,\qquad g(1)=1/5,\qquad g(3)=4/5.
\]

Actual execution output:

```text
a_n = 0.051167870005909145
lambda_n = 2.972643482868742
p_g = 0.25
q_g = 0.24312381349675596
n q_g = 9.724952539870237
m=1: factorial=9.72495253987 lower=4.86247626994
  marked inequality checks passed
m=2: factorial=88.0435786521 lower=23.6436754757
  marked inequality checks passed
m=3: factorial=738.943263535 lower=114.966810935
  marked inequality checks passed
m=4: factorial=5723.28076475 lower=559.023389999
  marked inequality checks passed
hard-set recovery gap = 0.0
winsorized mark identities passed; expected marks = 11.573456863459645
ALL CHECKS PASSED
```

Checks performed:

1. exact conditioned central atom \(a_n=\Pr(S_n=n-1)\);
2. exact soft-mark one-coordinate probability \(q_g\);
3. exact factorial marked moment identity and the Jensen lower bound for \(m=1,2,3,4\);
4. Theorem 3.1 at several positive tilt parameters for every tested \(m\);
5. recovery of the previous hard-set optimization from the soft-mark formula on the singleton set \(\{3\}\);
6. exact winsorized identities \(p_g=W_P/D^q\) and \(q_g=W_Q/D^q\).

No numerical result here is used to certify the infinite-variance quantifiers.