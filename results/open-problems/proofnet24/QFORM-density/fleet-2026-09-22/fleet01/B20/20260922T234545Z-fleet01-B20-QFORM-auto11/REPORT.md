# QFORM fleet01/B20 auto11 — R-packet third-volume closure step

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`  
**Run:** `20260922T234545Z-fleet01-B20-QFORM-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / CONTINUITY_OPEN_OUTSIDE_PAID_BRANCHES`  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`

## Exact target

For arbitrary independent real coordinates `X_i` whose one-dimensional densities satisfy `0 <= f_i <= 1`, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. No Gaussian, moment, iid, compact-support, log-concavity, or rotated-independence assumption is introduced here.

## Fresh source dependencies actually read

4. Prior B20 candidate theorem used only in the diffuse subbranch: `QFORM-FRACTIONAL-VOLUME-BL-v1` from the immediately preceding B20 run. It is treated as a completed internal proof but **not** as independently reviewed programme closure.

Live corrections were respected: no uniform pointwise quadratic oscillatory decay, no post-rotation independence, no arbitrary-joint coarea shortcut, and no promotion of a single heavy edge to a well-conditioned physical pair.

## Input from fleet02/B20 r22

The r22 physical deshearing argument yields, after the O0 anchored-volume step, a source-realizable trichotomy. The branch attacked here is

`R: E_2(D) > 1/48 and E_5(D) < 1/1024`,

where `D` is an **actual physical residual cross block** (not a Schur-sheared random-coordinate block), and

`E_k(D) := e_k(D D^T)`.

The fifth-volume condition is retained but is not needed for the lemma below. The point is to execute r22's stated next split: substantial diffuse `E_3(D)` versus concentrated third-volume marginals versus small `E_3(D)`.

## New theorem: `QFORM-R22-E3-TAIL-TRICHOTOMY-v1`

Let the squared singular values of `D` be

`lambda_1 >= lambda_2 >= ... >= 0`.

Set

`E_2 = sum_{p<q} lambda_p lambda_q`,  
`E_3 = sum_{p<q<r} lambda_p lambda_q lambda_r`,  
`T_2 = sum_{r>=3} lambda_r = dist_F(D,{rank <= 2})^2`.

Then the exact identity

`3 E_3 = sum_{p<q} lambda_p lambda_q * sum_{r != p,q} lambda_r`

implies

`3 E_3 >= T_2 E_2`.

Indeed, for every pair `p<q`, because `lambda_1,lambda_2` are the two largest terms,

`sum_{r != p,q} lambda_r = sum_r lambda_r - lambda_p - lambda_q >= sum_r lambda_r - lambda_1 - lambda_2 = T_2`.

Therefore

`boxed: dist_F(D,{rank <= 2})^2 <= 3 E_3(D)/E_2(D).`

On the r22 R-packet, `E_2(D)>1/48`, so

`boxed: dist_F(D,{rank <= 2})^2 < 144 E_3(D),`

or equivalently

`boxed: dist_F(D,{rank <= 2}) < 12 sqrt(E_3(D)).`

This is dimension-free and uses only singular values algebraically; no random-coordinate rotation occurs.

### Fixed quantitative threshold

Take

`epsilon = 2^(-18)`.

Every r22 R-packet therefore falls into one of the following three source-valid states.

### A. Small third volume: an explicit rank-two tube

If `E_3(D)<epsilon`, then

`dist_F(D,{rank <= 2}) < 12*2^(-9) = 3/128 = 0.0234375.`

Thus the entire small-`E_3` R-branch is trapped in a universal Frobenius tube of radius `3/128` around rank at most two. This is the precise low-rank obstruction anticipated in the r22 handoff.

### B. Substantial third volume and diffuse physical volume marginals

Assume `E_3(D)>=epsilon`. Put the squared-minor probability law on physical triples

`w_{S,T} = det(D[S,T])^2 / E_3(D)`, `|S|=|T|=3`,

with row marginals `alpha_i=P_w(i in S)` and column marginals `beta_j=P_w(j in T)`.

If all row marginals satisfy `alpha_i<=2/3`, or after transposing all column marginals satisfy `beta_j<=2/3`, the prior B20 fractional-volume Brascamp--Lieb theorem with `theta=3/4` applies directly to the physical cross block `D`, preserving arbitrary same-side blocks and outside couplings. It yields

`||p_Q||_infty <= C_(3/4) E_3(D)^(-1/6)`,

where `C_(3/4)=21.59066859519...`. Hence at the chosen threshold

`boxed: ||p_Q||_infty < 21.59066859519 * 8 = 172.72534876152.`

This subbranch has a bounded continuous density by that Fourier argument. Because the fractional-volume theorem has not yet been independently reviewed in the programme, this payment is recorded as an internal completed implication, not as a reviewed global theorem.

### C. Substantial third volume and concentrated row/column marginals

Suppose instead that both orientations fail the `2/3` diffuse gate. Then there are an actual physical row `j` and physical column `p` of `D` with

`alpha_j>2/3`, `beta_p>2/3`.

Under the same genuine physical squared-minor law,

`P_w(j in S and p in T) >= alpha_j+beta_p-1 > 1/3`.

Therefore the third-minor mass of `D` simultaneously containing the two physical anchors satisfies

`boxed: sum_{S contains j, T contains p} det(D[S,T])^2 > E_3(D)/3 >= 1/786432.`

Now independently two-colour all residual rows other than `j` and columns other than `p`. For any anchored triple, the probability that its two non-anchor rows split across the two row colours and its two non-anchor columns split across the two column colours is `1/4`. Hence some deterministic four-bank colouring has anchored packet mass

`boxed: P_nested > E_3(D)/12 >= 1/3145728.`

Every object in this packet is an original-coordinate submatrix/minor of `D`. No rotated variables are asserted independent. This supplies the recursive physical anchor demanded by r22.

## Conditional end-to-end consequence for r22's R branch

The first r22 R-packet debt is therefore reduced to exactly two structural survivors:

1. a universal rank-two Frobenius tube
   `dist_F(D,{rank<=2}) < 3/128`, while retaining `E_2(D)>1/48` and `E_5(D)<1/1024`; or
2. a **nested two-anchor four-bank third-minor packet** with mass at least `1/3145728`.

The only third possibility, a substantial diffuse third-volume packet, is paid at density level `172.726` by the prior fractional-volume theorem.

This is a genuine first unpaid implication of the latest fleet02/B20 result. It does **not** close packets H or P from r22, it does **not** pay the rank-two tube or nested anchored packet, and it does **not** prove the full QFORM target.

## Why `E_5(D)<1/1024` is preserved rather than spent here

The tail inequality uses only `E_2,E_3`. The r22 fifth-volume restriction should remain attached to both surviving packets because it is useful downstream: a rank-two tube together with nontrivial `E_2` is a natural pair-log/fractional-potential regime, while a nested anchor can be combined with the fifth-volume cap to prevent unlimited diffuse five-direction escape. Dropping that information would make the handoff weaker.

## Exact arithmetic/check output

The numerical specialization was checked with:

```python
from fractions import Fraction
import math

eps = Fraction(1, 2**18)
C = 21.59066859519
print(float(eps))
print(12*math.sqrt(float(eps)))
print(Fraction(3,128))
print(C*float(eps)**(-1/6))
print(Fraction(1,3*2**18))
print(Fraction(1,12*2**18))
```

Output:

```text
3.814697265625e-06
0.0234375
3/128
172.72534876151997
1/786432
1/3145728
```

## Next unpaid implication

`QFORM-R22-RANK2-OR-NESTED-ANCHOR-PAYMENT-v1`:

- **rank-two tube:** exploit `E_2(D)>1/48` plus `dist_F(D,rank<=2)<3/128` without rotating the product source; seek two physical grouped slopes or a pair-log/fractional-potential estimate stable under arbitrary same-bank curvature;
- **nested anchor:** apply the same physical deshearing/volume mechanism one level lower, but track the original outer anchor and the new inner anchor simultaneously so the recursion cannot cycle without accumulating a paid grouped square/bilinear packet.

A useful monotone quantity for the nested route is the amount of third-volume mass attached simultaneously to all selected physical anchors; every recursive anchor here costs only an explicit fixed factor, while a diffuse stage is immediately paid.

## Keeper/result status

Fresh current-account inventory contained the same twenty B01--B20 QFORM tasks, enabled, hourly-valid and quiet. No verified missing authorized slot, duplicate, owner pause, or capacity defect was found; no scheduler mutation was required. The current-hour B20 login already existed and was preserved rather than duplicated. Missing peer login alone was not treated as an outage.

**Honest status:** `ESSENTIAL_STEP_APPLIED`. Full QFORM remains `OPEN`. Global continuity remains `OPEN`; continuity is available only in already-paid Fourier branches such as B above.
