SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T02:44:37Z.
attacking: prove a dependence-safe stability theorem that lets an arbitrary extra spectral block be absorbed after a protected original-coordinate certificate, and sharpen the scalar Schur recursion using exact threshold inheritance without assuming independence after rotation.

# account03/B12 r23 — exact one-sided scalar-Schur compiler and certificate-adapted extra-spectrum peeling

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_REDUCTION / PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source pins

The target is unchanged: independent real original-coordinate inputs with densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, log-concavity, Gaussian, diagonal-basis, or post-rotation independence assumption is introduced here.

This run consumes two completed results at their exact scopes.

1. **Threshold-preserving physical Schur inheritance**, account03/B12 r21:
   `yspennstate/math-open-problems@dd754a0bfed889fd29c931b7112c8c3285fc83e8`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T004313Z-qform-eigenvalue-r21/REPORT.md`.
   If an invertible `p`-coordinate ORIGINAL principal pivot is eliminated, then for every `L>0`

   `N_abs(S;L) >= N_abs(A;L)-p`,

   and likewise separately for positive and negative threshold counts. The surviving scale `L` is not degraded.

2. **Designated partner account04/B12 mixed-norm shear compiler**:
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.
   For a joint density `h(u,z)`, if

   `M(h)=int esssup_u h(u,z) dz <= C`,

   then for every measurable `psi`, with no independence between `U` and `Z`,

   `||p_(U+psi(Z))||_infinity <= C`.

The live corrections are respected: no law-uniform pointwise van-der-Corput estimate, arbitrary-joint rank-three coarea bound, positive conditional-density moment, worst normalized fiber cap, or independence after a spectral rotation is used.

The previous r22 scalar compiler used the valid but nonsharp estimate `4 sqrt(M/|a|)`. This run proves the exact one-sided rearrangement constant `2`, reducing the fixed point of an arbitrary scalar-pivot chain from `16/tau` to `4/tau`.

## 2. First essential implication: the sharp one-sided half-Riesz estimate

### Lemma 2.1 — one-sided `L^1 cap L^infinity` half-Riesz bound

Let `q:[0,infinity)->[0,infinity)` satisfy

`q(u)<=M` a.e.,     `int_0^infinity q(u)du <=1`.

Then

`boxed: int_0^infinity u^(-1/2) q(u)du <= 2 sqrt(M).`             (2.1)

The constant `2` is sharp for this information: equality is attained by

`q(u)=M 1_(0,1/M)(u)`.

#### Proof

Use the exact layer-cake identity

`u^(-1/2)=int_0^infinity 1_{s<u^(-1/2)} ds`.

Tonelli gives

`int_0^infinity u^(-1/2)q(u)du
 =int_0^infinity [int_0^(s^(-2)) q(u)du] ds
 <=int_0^infinity min(1,M s^(-2)) ds.`

Split at `s=sqrt(M)`:

`int_0^sqrt(M) 1 ds + int_sqrt(M)^infinity M s^(-2) ds
 =sqrt(M)+sqrt(M)=2sqrt(M)`.

QED.

This one-sided use is the point lost in the r22 symmetric truncation estimate. A completed square contributes only one half-line, so the symmetric `|R-t|^(-1/2)` majorant is unnecessarily expensive.

## 3. Exact original-coordinate scalar-Schur compiler

### Theorem 3.1 — `QFORM-ONE-SIDED-SCALAR-SCHUR-COMPILER-v2`

Let `X` be one ORIGINAL input coordinate, with density at most one, and let `Y` denote all remaining original coordinates. Suppose after completing this physical scalar pivot the form is

`Q = a (X+m(Y))^2 + R(Y)`,       `a!=0`,                           (3.1)

where `m` is arbitrary measurable and the law of `R` has density cap

`||p_R||_infinity <= M`.

Then

`boxed: ||p_Q||_infinity <= 2 sqrt(M/|a|).`                       (3.2)

No independence between the translated square `a(X+m(Y))^2` and `R(Y)` is asserted or needed.

#### Proof

Fix `Y=y`. If `a>0`, the two inverse branches of

`u=a(x+m(y))^2`

give, for `u>0`,

`p_(a(X+m(y))^2 | Y=y)(u)
 <= 1/(sqrt(a u)).`                                               (3.3)

Indeed each branch has Jacobian `1/(2 sqrt(a u))` and the original density is at most one. If `a<0`, the same bound holds after reflecting the output half-line. Write `eps=sign(a)`. Hence for almost every `t`, conditioning only on the untouched ORIGINAL coordinates,

`p_Q(t)
 <= |a|^(-1/2) E[ |t-R(Y)|^(-1/2) 1_{eps(t-R(Y))>0} ].`           (3.4)

For `u>0` define

`q_t(u)=p_R(t-eps u)`.

Then `0<=q_t<=M` and `int_0^infinity q_t(u)du<=1`. Lemma 2.1 gives

`p_Q(t)<=|a|^(-1/2) 2 sqrt(M)`.

Taking the essential supremum proves (3.2). QED.

### Matrix form

For a physical block decomposition

`A=[[a,b^T],[b,C]]`,    `a!=0`,

let

`S=C-bb^T/a`                                               (3.5)

be the Schur complement. Arbitrary affine terms are allowed. If the quadratic-plus-affine Schur remainder has density cap `M`, then the full form satisfies (3.2). All signs and all other eigenvalues/couplings are unrestricted.

## 4. Closed scalar-pivot chain with arbitrary pivot sizes

Normalize at a fixed spectral scale `L>0`. Suppose an outer-to-inner sequence of ORIGINAL scalar Schur pivots has

`|a_j| >= tau_j L`,       `tau_j>0`,     `j=1,...,k`,              (4.1)

and the terminal Schur form has density cap

`B/L`.                                                               (4.2)

Let `B_j/L` be the normalized density cap after the first `j` outer pivots have been removed, so `B_k=B`. Theorem 3.1 gives the exact recurrence

`B_(j-1) <= 2 sqrt(B_j/tau_j)`.                                    (4.3)

### Theorem 4.1 — `QFORM-CERTIFICATE-ADAPTED-PIVOT-CHAIN-v1`

The recurrence closes explicitly as

`boxed:
 B_0 <= 4^(1-2^(-k)) B^(2^(-k))
        prod_(j=1)^k tau_j^(-2^(-j)).`                              (4.4)

In particular, if every `tau_j>=tau`,

`boxed: B_0 <= (4/tau)^(1-2^(-k)) B^(2^(-k))
              <= max{B,4/tau}.`                                    (4.5)

Thus an arbitrarily long chain of extra large directions does not create a factor depending on chain length.

#### Proof

For `k=1`, (4.4) is exactly (4.3). Assume the formula for the inner `k-1` steps and apply `2 sqrt(. /tau_1)` once. Every inner exponent is halved, the new factor is `2=4^(1/2)`, and

`1/2 + (1/2)(1-2^(-(k-1))) = 1-2^(-k)`.

This yields (4.4). If all `tau_j>=tau`, the sum of the exponents on `tau` is

`sum_(j=1)^k 2^(-j)=1-2^(-k)`,

giving (4.5). QED.

### Corollary 4.2 — a terminal certificate sets its own safe pivot threshold

If the terminal certificate has normalized cap `B`, then it is enough that every preceding physical scalar pivot satisfy

`boxed: |a_j| >= (4/B)L`                                           (4.6)

to preserve the **same** final constant:

`boxed: ||p_Q||_infinity <= B/L`                                  (4.7)

through any number of such pivots.

Proof: if `B_j<=B` and `tau_j>=4/B`, then

`2 sqrt(B_j/tau_j)<=2 sqrt(B/(4/B))=B`.

Backward induction gives (4.7). QED.

This is strictly stronger than r22's safe threshold `16L/B` arising from its nonsharp symmetric half-Riesz bound.

## 5. Why this genuinely controls additional spectrum

The analytic chain above composes with the r21 threshold theorem. If the current quadratic matrix has at least four eigenvalues of modulus at least `L`, eliminating any scalar pivot satisfying (4.6) leaves at least three eigenvalues still of modulus at least **the same `L`**. Hence no spectral-scale loss accumulates while extra large directions are peeled.

All smaller eigenvalues are retained in the exact Schur complement; none are dropped as independent noise. Their signs, multiplicities and sizes may change under the Schur operation. The only independence used is the original product independence of the scalar pivot coordinate from the untouched original coordinates before conditioning.

Consequently, once a dependence-safe terminal certificate of size `B/L` is available, extra spectrum represented by any number of physical scalar pivots above `4L/B` costs zero in the final constant. This is a reduction/stability theorem, not a claim that the bare three-eigenvalue hypothesis always supplies such pivots.

## 6. Actual application of the assigned account04/B12 result

The partner theorem is now consumed in an actual inequality, not merely cited.

Suppose the terminal form has an ORIGINAL-coordinate statistic `Z` and scalar core output `U` with joint density `h(u,z)` satisfying

`M(h)=int esssup_u h(u,z)dz <= B/L`,                               (6.1)

and the entire remaining dependent quadratic block is any measurable scalar function `psi(Z)`. Account04/B12 gives

`||p_(U+psi(Z))||_infinity <= M(h) <= B/L`.                        (6.2)

No independence between `U` and `Z` occurs in (6.2). Combining (6.2) with Corollary 4.2 gives

`boxed:
 if |a_j| >= (4/B)L for every preceding scalar pivot, then
 ||p_Q||_infinity <= B/L,`                                        (6.3)

uniformly over the number, signs and magnitudes of the eigenvalues hidden in `psi` and over every cross coupling encoded by the original-coordinate Schur chain.

### Concrete partner calculation

The account04/B12 report applies its compiler to the completed Hadamard-cube joint estimate and obtains

`M(h)<=4 pi`.                                                       (6.4)

Set `L=1`, `B=4pi`. Then

`4/B = 1/pi = 0.3183098861837907...`.                              (6.5)

Therefore any number of preceding physical scalar Schur extensions with arbitrary cross couplings and either pivot sign, each satisfying

`|a_j| >= 1/pi`,                                                    (6.6)

preserves the exact terminal inequality

`boxed: ||p_Q||_infinity <= 4pi`                                  (6.7)

while the partner remainder may be **any measurable `psi(Z)`**, including quadratic remainders with arbitrary added eigenvalue signs and magnitudes within that certified interface.

This example is deliberately stated as a stability theorem around a verified mixed-norm certificate; it is not promoted to the unrestricted QFORM target.

## 7. Quantitative effect on the existing B12 exit constants

Several already-proved terminal bounds can now be propagated backward through a much weaker physical-pivot requirement.

### 7.1 Determinant-pair terminal

The r22 determinant-pair exit has

`B_pair=9.2+log(10000)=18.410340371976183...`.

The new no-loss scalar-pivot threshold is

`4/B_pair=0.21726920410926853...`.                                 (7.1)

Thus a chain of pivots only about `0.2173 L` in magnitude already preserves the pair-exit constant.

### 7.2 Collective-tail terminal

The volume/tail terminal used in r22 has

`B_tail=9 sqrt(3)e/2=21.186910062820317...`.

Now

`4/B_tail=0.18879581723525454...`.                                 (7.2)

Hence a chain with `|a_j|>=0.18880 L` preserves the full tail constant `B_tail/L`, independent of chain length.

### 7.3 Protected physical-triple terminal

For the earlier B12 protected-triple fixed-outside cap

`B_3=6 sqrt(pi)=10.634723105433096...`,

the no-loss threshold is

`4/B_3=0.37612638903183754...`.                                    (7.3)

These numbers are not numerical evidence for QFORM; they are evaluations of exact proved inequalities. `CHECK.py` verifies the closed recurrence and constants.

## 8. A sharpened high-rank reduction

Fix any proved terminal target constant `B>=B_pair`. While the current matrix has at least four eigenvalues of modulus at least `L`, repeatedly do the following:

1. if a paid terminal certificate with cap at most `B/L` is present, stop;
2. if some physical diagonal satisfies `|A_ii| >= 4L/B`, pivot that ORIGINAL coordinate and continue;
3. otherwise stop.

By threshold-preserving Schur inheritance, every pivot in step 2 leaves at least three eigenvalues of modulus at least `L`. By Corollary 4.2, if a paid terminal is eventually reached, the entire backward chain still has cap `B/L`.

Therefore the only high-rank matrices not disposed of by this compiler must reach a Schur terminal with

`boxed: |A_ii| < 4L/B for every physical coordinate i,`            (8.1)

in addition to failing whatever paid grouped/pair/volume certificate is being used. For the concrete collective-tail normalization `B=B_tail`, the residual diagonal window is

`|A_ii| < 0.188795818 L`.                                          (8.2)

This is a genuine narrowing of r22's `|A_ii|<L` no-pivot class. It still does not solve the dense mixed-sign residual class: matrices can have substantial spectrum spread across many tiny physical coefficients.

## 9. Continuity

The present scalar-square compiler proves an essential `L^infinity` bound. It does **not** by itself prove a continuous representative after backward scalar peeling. The partner account04/B12 theorem separately gives continuity when its mixed translation modulus tends to zero, but that modulus is not established here for every scalar-Schur extension. Therefore the full continuity objective remains open in this branch.

## 10. Remaining implication and full-target status

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** This run settles a narrower additional-eigenvalue issue: once a valid terminal product-preserving certificate exists, arbitrary dependent remainder spectrum handled by the partner shear compiler plus arbitrarily many sufficiently large ORIGINAL scalar Schur pivots can be restored with no accumulation of the density constant and no spectral-threshold degradation.

The unpaid structural implication is now sharper:

> In a three-large-eigenvalue instance that has no paid mixed-norm/grouped-volume terminal, can one aggregate the original product coordinates in the residual class where every physical diagonal is below the certificate-adapted threshold (for example `0.1888 L` at the current tail constant), without paying the reciprocal of a tiny local minor?

The singleton-plus-two-banks and Hadamard/diffuse correction families show why one should expect a grouped-bank or weighted-volume mechanism rather than a universal single-coordinate pivot.

## 11. Verification notes

`CHECK.py` verifies the exact closed form (4.4) against 450 iterated recurrences and evaluates the certificate-adapted thresholds. It is a finite algebra/constant check only; no Monte Carlo or histogram is used as proof.

Current prepublication control observed: `yspennstate/math-research-brain@3b461bee8c160d664091e53ce6f1b4cdf6697a9a`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`; QFORM remains the sole research target. The live correction inbox remained active and no newer correction invalidated the premises above.

Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
