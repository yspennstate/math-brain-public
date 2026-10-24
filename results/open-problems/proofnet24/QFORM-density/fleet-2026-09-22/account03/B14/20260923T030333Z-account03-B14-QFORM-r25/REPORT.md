# QFORM account03/B14 r25 — unnormalized overlap kernels and collective pure-bank leakage

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T03:03:33Z.

attacking: translations/localization: unnormalized overlap-kernel localization that retains full overlap mass through decoupling, plus collective pure-bank kernel-leakage smoothing.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T030333Z-account03-B14-QFORM-r25`  
Status: `SUPPORTING TARGET-LEVEL THEOREMS PROVED / FULL QFORM OPEN`  
Continuity: `OPEN for the full target; not claimed below for arbitrary rough laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and current correction boundary

The target remains: for arbitrary independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free bound on the density of `Q=X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, or post-rotation independence assumptions are used below.

The live corrections consumed before this report include: failure of law-uniform pointwise quadratic-phase decay; failure of conjugate-variable conditional density caps; divergence of positive conditional projection-density moments; failure of one-small-minor / one-coordinate reciprocal-scale proof compilers; and the preceding B14 `QFORM-CONDITIONAL-CAP-RENYI-OBSTRUCTION-v1` / overlap-mass threshold. The goal of this run is to retain the overlap mass before normalization rather than pay a random reciprocal conditional cap.

The completed designated partner actually applied in Section 4 is account04/B14 r6, canonical source

`yspennstate/math-open-problems@6442bbe9d4647a730b27b8e0786bc54b2546b7ec`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T011517Z-account04-B14-kernel-leakage-core-r6/REPORT.md`.

Its fixed four-coordinate affine-core theorem states that if an actual four-coordinate symmetric block has at least three eigenvalues of modulus at least `sigma`, then arbitrary cap-one product laws and arbitrary affine terms satisfy

`||p||_infinity <= C4/sigma`,

where

`C4 = 1000(8+log 4)`.

The theorem survives arbitrary outside original-coordinate conditioning and rough/unbounded input laws.

## 2. QFORM-UNNORMALIZED-OVERLAP-KERNEL-LP-v1

Let `f` be any probability density on `R` with `0<=f<=1`. For iid `X,X'~f`, put

`U=X-X'`, `V=X+X'`.

The joint density of `(U,V)` is

`r_f(u,v) = (1/2) f((v+u)/2) f((v-u)/2)`.

Define the overlap mass and its unnormalized Fourier kernel by

`m_f(u) = integral_R r_f(u,v) dv = integral_R f(x)f(x-u) dx`,

`K_f(u,xi) = integral_R exp(i xi v) r_f(u,v) dv`.

### Theorem 2.1 — exact mass-retaining kernel estimates

For every admissible `f`:

1. `m_f` is the probability density of `U`, `0<=m_f<=1`, and `integral m_f=1`.
2. `K_f(u,0)=m_f(u)` and `|K_f(u,xi)|<=m_f(u)`.
3. For every fixed `u`,

   `integral_R |K_f(u,xi)|^2 dxi
     = pi integral_R f(x)^2 f(x-u)^2 dx
     <= pi m_f(u)`.

4. Globally,

   `integral_R integral_R |K_f(u,xi)|^2 dxi du
     = pi (integral_R f(x)^2 dx)^2
     <= pi`.

5. More generally, for every `p>=2`,

   `integral_R |K_f(u,xi)|^p dxi <= pi m_f(u)^(p-1)`

   and therefore

   `boxed: integral_R integral_R |K_f(u,xi)|^p dxi du <= pi.`

6. If `f_c(x)=f(x-c)`, then

   `K_(f_c)(u,xi)=exp(2 i c xi)K_f(u,xi)`.

   Hence every absolute kernel inequality above is exactly invariant under arbitrary translations.

#### Proof

The change of variables `u=x-x'`, `v=x+x'` has `dx dx'=(1/2)du dv`, giving the displayed joint density. Integrating in `v`, then writing `v=2x-u`, proves the formula for `m_f`. Since `f<=1`,

`m_f(u)<=integral f(x)dx=1`,

and Fubini gives `integral m_f=1`.

The inequalities `K(u,0)=m(u)` and `|K|<=m` are immediate from `r>=0`. With Fourier convention `hat h(xi)=integral exp(i xi v)h(v)dv`, Plancherel gives

`integral |K(u,xi)|^2 dxi = 2pi integral r_f(u,v)^2 dv`.

Now `v=2x-u`, so

`integral r_f(u,v)^2 dv
 =(1/2) integral f(x)^2 f(x-u)^2 dx`.

This proves item 3. Integrating in `u` gives

`integral integral f(x)^2 f(x-u)^2 dx du
 =(integral f^2)^2`,

and `integral f^2<=integral f=1`, proving item 4. For `p>=2`, use `|K|^(p-2)<=m(u)^(p-2)` and item 3:

`integral |K|^p <= pi m(u)^(p-1)`.

Since `m<=1`, `m^(p-1)<=m` for `p>=2`; integration in `u` proves item 5. Finally translation by `c` followed by `x=y+c` yields the phase factor `exp(2icxi)`, proving item 6. QED.

### Corollary 2.2 — exact unnormalized quadratic decoupling

Let `X=(X_1,...,X_n)` have independent coordinates with densities `f_j<=1`, and let `X'` be an independent copy. For symmetric `A`, set `Q(X)=X^TAX` and `phi_Q(t)=E exp(itQ(X))`. Then

`Q(X)-Q(X')=(X-X')^T A(X+X')`.

Writing `u=X-X'`, the product structure of the original coordinate pairs gives the exact identity

`boxed:
 |phi_Q(t)|^2
 = integral_(R^n) product_(j=1)^n
      K_(f_j)(u_j, t(Au)_j) du.`

Consequently,

`|phi_Q(t)|^2
 <= integral_(R^n) product_j |K_(f_j)(u_j,t(Au)_j)| du.`

This identity retains each overlap mass `m_j(u_j)` inside the kernel. It never forms the normalized conditional density of `V_j|U_j=u_j`, whose cap is `1/[2m_j(u_j)]` on finite-fragment extremes and whose positive moments can diverge. Thus Theorem 2.1 is a genuine fragment-uniform repair of the previous normalize-then-average obstruction.

It does **not** by itself prove a uniform `integral |phi_Q|`: a remaining coupled Brascamp--Lieb/transversality step must exploit the map `u -> Au` while preserving these unnormalized kernels. The theorem is therefore supporting, not a declaration of full QFORM.

## 3. Linear-bank projection input

We use the standard sharp one-dimensional product-projection theorem of Ball--Rogozin / Rudelson--Vershynin: if `V_i` are independent with densities bounded by one and `a in R^m`, then for

`W=a^T V`, `L=||a||_2>0`,

`||p_W||_infinity <= sqrt(2)/L`.

Equivalently, for a unit coefficient vector the sharp density cap is `sqrt(2)`. This theorem has no moment or support hypothesis and is therefore compatible with arbitrary translations and distant fragments.

## 4. QFORM-COLLECTIVE-PURE-KERNEL-BANK-v1

The next theorem applies the completed account04/B14 affine-core result to a collective bank rather than one leakage coordinate.

### Theorem 4.1 — collective pure-bank leakage

Split the **original independent coordinates** into three banks

`X=(U,V,Z)`, with `U in R^3`, `V in R^m`.

Assume the symmetric coefficient matrix has block form

`A = [[B,       k a^T,  C],
      [a k^T,   0,      a b^T],
      [C^T,     b a^T,  D]]`,

where

- `B` is symmetric `3x3`;
- `k in R^3` is a unit vector satisfying `Bk=0`;
- `B` has at least one eigenvalue of modulus at least `nu>0`;
- `a in R^m` has `L=||a||_2>0`;
- the `V` self block is zero; and
- every `V`--outside coupling is along the same bank direction `a`.

Then, for arbitrary independent original-coordinate densities bounded by one,

`boxed:
 ||p_(X^TAX)||_infinity
 <= C4 / min(nu,L/sqrt(2))
 = C4 max(1/nu,sqrt(2)/L),`

where `C4=1000(8+log 4)`.

No moment, support-radius, fragment-count, fragment-separation, or centering assumption is imposed.

#### Proof

Condition on all outside coordinates `Z=z`. Since the coordinates are conditioned in the original product basis, `U` and `V` remain independent product banks. Put

`W=a^T V`.

By the assumed block structure, the conditional quadratic form depends on the entire bank `V` only through `W`:

`Q_z
 = U^TBU + 2(k^TU)W
   + 2U^T C z + 2(b^Tz)W + z^TDz`.

The projection theorem gives `||p_W||_infinity<=M0`, where

`M0=sqrt(2)/L`.

Set `Y=M0 W`. Then `Y` has density bounded by one and is independent of `U`. Since `W=Y/M0`, define

`r=1/M0=L/sqrt(2)`.

The conditional form becomes an affine perturbation of the four-variable quadratic form with active matrix

`H = [[B, r k],
      [r k^T, 0]].`

This reduction is exact; no random-variable rotation is used. To read the spectrum of `H`, one may choose a deterministic orthogonal basis only for the coefficient matrix in which `k` is a kernel basis vector and `B` is diagonal on `k^perp`. The `k,Y` block is

`[[0,r],[r,0]]`,

with eigenvalues `+r,-r`, while every nonzero eigenvalue of `B|_(k^perp)` is retained. Hence `H` has at least three eigenvalues of modulus at least

`sigma=min(nu,r)=min(nu,L/sqrt(2))`.

Now apply the completed account04/B14 r6 fixed four-coordinate affine theorem to the actual independent cap-one variables `(U_1,U_2,U_3,Y)`. The terms `2U^TCz`, `2(b^Tz)Y/M0`, and `z^TDz` are precisely arbitrary affine/scalar parameters, to which the partner theorem is uniform. Therefore

`||p_(Q|Z=z)||_infinity <= C4/sigma`

for every `z`. Averaging the conditional densities proves the same bound for `Q`. QED.

### Translation statement

Arbitrary physical-coordinate shifts cost nothing in Theorem 4.1. A shift of the `V` bank changes `W` only by the scalar `a^T h_V`; a shift of `U` or `Z` creates only affine/scalar terms in the four-variable conditional core. Since the partner theorem is affine-uniform, the displayed constant is unchanged. Thus the theorem explicitly handles arbitrary remote fragments and translations rather than recentering them with a moment bound.

## 5. Stress family: collective aggregation beats every single leakage coordinate

Fix `0<epsilon<1`, take

`B=diag(1,epsilon,0)`, `k=e_3`,

and for each `N` let

`a_N=(1/sqrt(N),...,1/sqrt(N)) in R^N`,

with no outside `Z` bank. Then the full matrix

`A_N=[[B,k a_N^T],[a_N k^T,0]]`

has nonzero eigenvalues

`{1, epsilon, +1, -1}`.

Thus it satisfies the exact target hypothesis with precisely three eigenvalues of modulus at least one. Every individual leakage coefficient is only `1/sqrt(N)`. A one-coordinate physical enlargement based on the rank-two block `B` therefore pays a reciprocal leakage factor growing like `sqrt(N)` (with the other block parameters fixed), while the collective bank has `||a_N||_2=1`.

Theorem 4.1 gives the dimension-free estimate

`||p_(X^T A_N X)||_infinity <= C4 sqrt(2)`

for all `N`, all independent cap-one input laws, and arbitrary translations/fragments. Numerically,

`C4 = 9386.294361119892`,

`C4 sqrt(2) = 13274.224785921857`.

The large numerical constant is not intended to be sharp. The important point is structural: the proof pays the `l2` norm of the entire leakage bank instead of `max_j |a_j|` or a selected reciprocal minor. This is a rigorous aggregate-before-inversion step on a valid target family.

## 6. What remains

The full conjecture is still open. The pure-bank gate in Theorem 4.1 is essential to the proof: the `V` self block is zero and the `V`--outside coupling has one-dimensional row space, so the form depends on `V` through the single linear statistic `W=a^TV`. If `V` carries an arbitrary quadratic self block or several independent coupling directions, collapsing `V` to `W` discards information and can create dependence that is not covered by the theorem.

Theorem 2.1 is designed for that unresolved regime: its unnormalized kernels retain a full overlap-mass power and are uniformly `L^p(du dxi)` for every `p>=2`, independently of support fragmentation. The next missing implication is a dimension-free coupled transversality / Brascamp--Lieb estimate that combines those kernels along `xi_j=t(Au)_j`, or an analogous grouped-bank theorem that allows nonzero self curvature, while still aggregating before reciprocal inversion.

Essential boundedness is proved only in the stated collective-bank branch. Continuity for arbitrary rough laws is not established here and remains separate.

## 7. Integrity and dependencies

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New theorem 1: `QFORM-UNNORMALIZED-OVERLAP-KERNEL-LP-v1`, proved above.
- New theorem 2: `QFORM-COLLECTIVE-PURE-KERNEL-BANK-v1`, proved above.
- Partner actually applied: account04/B14 r6 fixed four-coordinate affine theorem, source commit `6442bbe9d4647a730b27b8e0786bc54b2546b7ec`.
- External projection input: the sharp one-dimensional product-density projection bound `sqrt(2)` (Rogozin + Ball; also Theorem 1.2 of Rudelson--Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*).
- Repository transport is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
