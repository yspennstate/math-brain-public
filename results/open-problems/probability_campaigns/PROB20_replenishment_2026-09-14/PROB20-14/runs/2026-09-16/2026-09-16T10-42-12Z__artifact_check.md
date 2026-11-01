# PROB20-14 canonical-tilt checker execution certificate

Mathematical status: **PARTIAL / OPEN**.

Checker artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/canonical_tilt_corridor_check_20260916.py`

- creation commit: `4365dbeb4869fbd9f5bf7a56736c5e4b15bd3990`
- exact-commit readback blob: `d7ac11b62b978a6c2ea813bf272308e9bcb3f1ea`
- readback status: **VERIFIED**

The checker logic was executed in this run on the critical finite-support test law
\[
(\pi_0,\pi_1,\pi_3)=(1/2,1/4,1/4),\qquad q=3/2.
\]
This law has finite variance, so the computation is only an algebra/indexing consistency certificate and is **not** evidence for the target infinite-variance theorem.

Execution output:

```text
ALL_ASSERTIONS_PASSED
tilt/entropy rows checked: 15
zero-surplus configurations checked: 1707
sample rows: m b theta central_exponent m*KL c/m^beta
8 1 0.0872850066003 2.10730819982 0.00312012948349 1.05365409991
8 2 0.184862536861 2.15082406641 0.0223103464507 1.07541203321
8 4 0.435663896111 1.85221623389 0.00141053413463 0.926108116947
10 1 0.0691292456403 2.28885361023 0.0173973794014 1.0623917359
10 2 0.144322761275 2.19999314723 0.00576310577333 1.02114636262
10 5 0.435663896111 1.98607846138 0.0164814526199 0.9218559609
12 1 0.0572359664039 2.34582601192 0.00181413268551 1.02463388884
12 3 0.184862536861 2.28641255523 0.0117452941954 0.998682671286
```

Assertions checked:

1. conditioning on `S_m=m-b` is invariant under the mean-matching exponential tilt;
2. both the tilted reference marginal and conditioned marginal have exact mean `1-b/m`;
3. `m D(mu_{m,b} || P_{m,b}) <= c_{m,b}` for every tested pair;
4. exact first-moment tail balance from equality of the means;
5. `q`-tail domination `P_theta <= pi/pi_0`;
6. the deterministic moving-tilt zero/excess identity
   `N_0=b+d-1+sum_i (xi_i-1)_+`;
7. its centered form
   `N_0-(m-1)P_theta(0)=d-1+b/m+sum_i(Y_i-E_theta Y)`.

No numerical assertion is promoted to a proof of the infinite-variance endpoint.