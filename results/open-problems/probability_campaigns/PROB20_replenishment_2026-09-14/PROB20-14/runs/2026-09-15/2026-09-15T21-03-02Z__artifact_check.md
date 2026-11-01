# PROB20-14 — adaptive tail-mean Palm checker execution

**Artifact:** `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/adaptive_tail_mean_palm_check.py`  
**Artifact commit:** `84780f733ff36a822b00bfa224a26a2ebedaf450`  
**Role:** reproducible finite-support consistency check only; **not proof evidence** for the infinite-variance universal theorem.

The script was executed with Python's exact `Fraction` arithmetic for all convolution probabilities. All assertions passed.

```text
case A
Y law: {0: '3/4', 1: '3/20', 4: '1/10'}
E Y = 11/20 = pi_0
d=5 T=4 M=0 V=1.75 exact_bad=0.347380661 chernoff=0.985229222
d=8 T=4 M=0 V=1.75 exact_bad=0.290986745 chernoff=0.962621258
d=10 T=4 M=0 V=1.75 exact_bad=0.236113193 chernoff=0.9422131
d=12 T=4 M=0 V=1.75 exact_bad=0.1854484 chernoff=0.917856438
d=15 T=4 M=0 V=1.75 exact_bad=0.106113653 chernoff=0.874652538
d=20 T=4 M=0 V=1.75 exact_bad=0.0493764336 chernoff=0.788127628

case B
Y law: {0: '799/1000', 1: '1/5', 19: '1/1000'}
E Y = 219/1000 = pi_0
d=8 T=1 M=0.019 V=0.2 exact_bad=0.243890372 chernoff=0.904837418
d=10 T=1 M=0.019 V=0.2 exact_bad=0.172814358 chernoff=0.855345327
d=15 T=1 M=0.019 V=0.2 exact_bad=0.0721342709 chernoff=0.703587874
d=20 T=1 M=0.019 V=0.2 exact_bad=0.0112397962 chernoff=0.535261429
d=30 T=1 M=0.019 V=0.2 exact_bad=6.92899039e-05 chernoff=0.245060539
d=40 T=1 M=0.019 V=0.2 exact_bad=4.67922153e-09 chernoff=0.0820849986
```

Case B illustrates the point of the new adaptive criterion: the threshold can stop at `T=1`, excluding the rare `Y=19` atom, because its omitted **tail mean** is already small enough for all tested `d`. This is precisely the flexibility absent from the preceding fixed-`T≈d` criterion.
