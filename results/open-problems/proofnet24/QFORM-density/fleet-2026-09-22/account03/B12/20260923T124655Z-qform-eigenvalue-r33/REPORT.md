SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T12:46:55Z.
attacking: q=2 ridge rank-budget stability under arbitrary large spectral packets plus small full-rank tails.

# account03/B12 — ridge spectral-tail rank-budget stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T124655Z-qform-eigenvalue-r33`  
Assignment: additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **proved for the ridge branch below; not proved for the full target**  
Execution-memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact contribution

Let `A=A0+R` be symmetric. Fix disjoint sets `I,J` of ORIGINAL independent coordinates and write

`B0=A0[I,J]`, `E=R[I,J]`, `B=A[I,J]=B0+E`.

For an integer `r>=0` and `k>=5`, define

`beta=s_{r+1}(E)`

(with the usual convention `s_j=0` beyond rank). If

`s_{r+k}(B0)>=a>beta`,

put `b=a-beta`. Then the full quadratic form, including arbitrary self blocks, arbitrary coordinates outside `I union J`, and arbitrary outside couplings, has a bounded continuous density vanishing at infinity and

`||p_{X^T A X}||_infinity <= C_k/b`,

where

`C_k = 3 k sqrt(3e) / [2 (k-4)^(3/2)]`.                 (1.1)

In particular

`C_5 = 15 sqrt(3e)/2 = 21.417517562791...`,

`C_6 = 9 sqrt(6e)/4 = 9.086683142899...`.

The first `r` singular directions of the added cross block may therefore be completely arbitrary in magnitude and sign. Only the first unreserved singular value `s_{r+1}(E)` is charged. This is a deterministic matrix statement on an ORIGINAL-coordinate cross block; no rotated random coordinates are asserted independent and no quadratic remainder is treated as an independent convolution.

A full-matrix spectral update corollary follows because coordinate compressions are contractions for singular values:

`s_{r+1}(R[I,J]) <= s_{r+1}(R)`.                         (1.2)

Hence the same conclusion holds if `s_{r+1}(R)<=delta<a`, with `b=a-delta`. For symmetric `R`, its top `r` eigenvalues in absolute value can be arbitrarily large and of either sign and arbitrary orientation, while all remaining added eigenvalues may be arbitrarily numerous and are charged only through `delta`.

This supporting theorem does NOT follow from the bare target assumption `s_3(A)>=1`: it requires an `r+k`-direction reserve on a physical cross block of the reference matrix. It is therefore a stability compiler, not the full conjecture.

## 2. Sources and corrections


The analytic receiver used below is the one-scale ridge theorem:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an actual cross block `B=A[I,J]`, scale `gamma>0`,

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta_gamma=tr K_gamma`,

its theorem says: if for some `1<=q<=2`,

`max_i (K_gamma)_ii <= q/2`, `theta_gamma>2q`,

then the FULL ambient form has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)`.    (2.1)

The source proves this by conditioning only on original coordinates and by a product-measure Brascamp--Lieb/Fourier argument. Its arbitrary self-block and outside-coupling scope is essential here.

The designated partner used at equation level is account04/B12:

`yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its exact complementary-Schur shield is applied in Section 6.

Corrections respected: bounded input density does not imply law-uniform pointwise quadratic phase decay; general rotations destroy independence; naive fiber-sup integration can grow with dimension; a bounded-density projection theorem alone does not control an indefinite quadratic pushforward; the arbitrary-joint rank-three coarea claim and positive conditional-density-moment gate are false. None is used below.

## 3. Deterministic rank-budget lemma

### Lemma 3.1 — rectangular singular reserve

For real rectangular matrices `B0,E` of the same size, integers `r>=0`, `k>=1`,

`s_k(B0+E) >= s_{k+r}(B0)-s_{r+1}(E)`.                    (3.1)

### Proof

Take a singular-value decomposition of `E` and let `E_r` be the truncation to its first `r` singular modes. Then

`rank(E_r)<=r`, `||E-E_r||_op=s_{r+1}(E)`.

A rank-`r` perturbation can move the singular-value counting function by at most `r`; equivalently

`s_k(B0+E_r)>=s_{k+r}(B0)`.                               (3.2)

One direct min-max proof is to take a subspace `V` of dimension at least `k+r` on which `||B0 x||>=s_{k+r}(B0)||x||`, intersect it with `ker(E_r)`, whose codimension is at most `r`, and retain a subspace of dimension at least `k`; on that subspace `(B0+E_r)x=B0x`. The singular-value min-max principle gives (3.2).

Finally Weyl's operator-norm perturbation inequality gives

`s_k(B0+E) >= s_k(B0+E_r)-||E-E_r||_op`,

which is (3.1). QED.

For a full symmetric update `R`, write the rectangular cross compression as `E=P_I R P_J^T`. The ideal property of singular values gives

`s_j(E)<=||P_I|| s_j(R) ||P_J^T||=s_j(R)`,                (3.3)

proving (1.2).

## 4. Main theorem: q=2 removes every leverage hypothesis

### Theorem 4.1 — `QFORM-RIDGE-SPECTRAL-TAIL-RANK-BUDGET-STABILITY-v1`

Under the hypotheses in Section 1,

`||p_Q||_infinity <= [3 k sqrt(3e)]/[2 (k-4)^(3/2) (a-beta)]`,  `k>=5`,       (4.1)

and `p_Q` has a continuous representative vanishing at infinity.

### Proof

Lemma 3.1 gives

`s_k(B)>=a-beta=b>0`.                                     (4.2)

Apply the ridge theorem with `q=2`. This is the crucial endpoint choice: because `0<=K_gamma<=I`,

`max_i (K_gamma)_ii<=1=q/2`                               (4.3)

for every cross block and every `gamma>0`. Thus no range-leverage or coordinate-delocalization hypothesis is needed. From the first `k` singular values in (4.2),

`theta_gamma
 = sum_j s_j(B)^2/(gamma^2+s_j(B)^2)
 >= k b^2/(gamma^2+b^2)`.                                 (4.4)

Write `gamma=b x`. We need the lower bound in (4.4) to exceed four. The ridge estimate (2.1) becomes

`||p_Q||_infinity
 <= sqrt(e)/(2 b x) * theta_gamma/(theta_gamma-4)`.

Since `theta/(theta-4)` decreases for `theta>4`, (4.4) yields

`||p_Q||_infinity
 <= sqrt(e)/(2 b x) * k/[k-4(1+x^2)]`,                    (4.5)

whenever `0<x^2<(k-4)/4`.

The denominator to maximize is `x[k-4-4x^2]`. Its derivative vanishes at

`x^2=(k-4)/12`.                                            (4.6)

At this choice,

`theta_gamma >= 12k/(k+8)>4`,

and

`[12k/(k+8)] / [12k/(k+8)-4] = 3k/[2(k-4)]`.

Substitution of `x=sqrt((k-4)/12)` into (4.5) gives exactly (4.1). The source ridge theorem also supplies a continuous `C_0` density. QED.

### Threshold-count form

Fix `0<=t<a`. If the update `R` has at most `r` eigenvalues of absolute value greater than `t`, then `s_{r+1}(R)<=t`. Hence

`s_{r+k}(B0)>=a`, `k>=5`

implies

`||p_Q||_infinity <= C_k/(a-t)`.                           (4.7)

This is the most direct interpretation for added eigenvalues: arbitrarily large signed spikes are paid only by their count, while the entire remaining spectral tail is paid only by its operator threshold.

## 5. Concrete inequalities

### 5.1 Two unbounded added eigenvalues plus an arbitrary full-rank tail

Take `r=2`, `k=6`, suppose

`s_8(B0)>=1`, `s_3(R)<=1/4`.

The two largest absolute eigenvalues of the symmetric update `R` are unrestricted in sign, magnitude and orientation. There may be arbitrarily many further eigenvalues. Here `b=3/4`, and (4.1) gives

`||p_Q||_infinity
 <= (9 sqrt(6e)/4)/(3/4)
 = 3 sqrt(6e)
 = 12.115577523865...`.                                   (5.1)

The density is continuous and vanishes at infinity.

### 5.2 Repairing a fixed-scale ridge failure under a huge rank-one spike

For a baseline cross block `B0=I_6`, an arbitrary rank-one cross update `E` can destroy some low-`q`, fixed-scale ridge certificate while leaving the target harmless. The present theorem instead takes `r=1`, `k=5`: since `s_6(B0)=1` and `s_2(E)=0`,

`||p_Q||_infinity <= C_5 = 21.417517562791...`             (5.2)

for every magnitude and sign of that rank-one cross packet, with a continuous `C_0` density. The mechanism switches certificate rather than asking one low-`q` ridge inequality to be monotone under arbitrary spikes.

## 6. Required partner application: complementary Schur shield plus a spectral tail

The designated account04/B12 theorem treats an arbitrary low-dimensional hostile packet `U Theta U^T` exactly and then pays a remaining dense matrix tail only through its operator norm. Apply it to its own five-coordinate physical family:

`D=diag(2,-2,2)`,
`B_12=[[1,0,0],[0,1,0]]`,
`mu=2`, `rho=1/2`,

while `Theta` is any real symmetric `2 x 2` matrix, with unbounded eigenvalues of either sign. Let the remaining symmetric tail satisfy `||T||_op<=1/4`. The partner theorem gives

`ell(1/2)^2=(9-sqrt(17))/8`,

so the physical gap is

`gamma
 =2 ell(1/2)^2-1/4
 =(8-sqrt(17))/4
 =0.969223593595...`.                                      (6.1)

Its finite-dimensional physical receiver therefore yields the actual inequality

`||p_Q||_infinity
 <= 2 sqrt(30 pi)/gamma
 = 8 sqrt(30 pi)/(8-sqrt(17))
 =20.032796615616...`.                                     (6.2)

This application permits the entire `2 x 2` hostile spectral packet to be arbitrarily large and signed, while the smaller dense tail is charged only by `1/4`. It does not claim continuity, because the partner shield's receiver establishes only essential boundedness. This branch and Theorem 4.1 are complementary: the former needs a protected physical compression but only three protected modes; the latter needs a larger cross-direction reserve but obtains continuity and is insensitive to leverage.

## 7. Finite checks

A deterministic/randomized checker accompanies this report. It tests 10,000 rectangular instances with `r=0,1,2,3`, `k=5,...,8`, a baseline satisfying the required singular reserve, an unbounded random rank-`r` packet, and a full-rank tail with prescribed operator norm `delta<a`. In every test it verifies

`s_k(B0+E)>=s_{r+k}(B0)-s_{r+1}(E)`,
`s_{r+1}(E)<=delta`,
`theta_gamma>=12k/(k+8)`

at the theorem's scale. It also records the exact constants in Sections 5 and 6. These checks are sanity tests only; the proof is the analytic argument above.

## 8. Scope and next implication

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This run changed mechanism from the preceding physical-core reserve sequence to the direct cross-block ridge/Fourier receiver.

The new theorem isolates a precise structural obligation: to absorb an arbitrary rank-`r` added spectral packet by this branch, one needs `r+5` substantial physical cross singular directions (or more generally `r+k`, `k>=5`). The bare global premise provides only three large singular/eigen directions and does not force such a physical cross reserve. Therefore the next useful reduction is a reserve-or-aggregate alternative: either produce enough physical cross reserve for Theorem 4.1, or route the low-cross-rank remainder to the already developed grouped-bank/hub/ridge-window/physical-pivot mechanisms without paying dimension-dependent fiber suprema.

Continuity is proved for Theorem 4.1 through the ridge theorem. Continuity is not claimed for the partner Schur branch or for unrestricted QFORM.
