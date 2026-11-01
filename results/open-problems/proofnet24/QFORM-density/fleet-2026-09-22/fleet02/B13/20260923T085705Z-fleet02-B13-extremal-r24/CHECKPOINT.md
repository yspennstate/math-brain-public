SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T08:57:05Z.
attacking: simultaneous finite-family purification and a cut-free fifth-volume sublevel inequality, then scalar-Schur descent to a bordered sixth-volume obstruction.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture OPEN. Execution WITHOUT_VERIFIED_BRAIN.

Sources actually used so far:

- fleet03/B13 partner `dd467574f6ba35d976c5ace6124aabb9575aa3f6`, which proves the random-cut identity `E e_m(S[L,R]^T S[L,R])=4^{-m}D_m^perp(S)` at the fair cut and the bordered identity `B_{m+1,k}^perp(A)=A_kk^2 D_m^perp(S)` after an original scalar Schur complement;
- Claude/Fourier pinned source `e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, Theorem D5: for every original-coordinate cross block M, `||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)` with no marginal condition and arbitrary self blocks/outside couplings/affine terms;
- fleet04/B13 `e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, which proves single-kernel no-attainment product purification by finite mixtures.

## 1. New finite-family purification lemma

Let `K_1,...,K_m` be bounded measurable kernels on `R^n`. For arbitrary cap-one probability densities `f_i` and every `eps>0`, there exist bounded finite unions of intervals `E_i` with `|E_i|=1` such that simultaneously for all `ell<=m`,

`| int K_ell prod_i f_i - int_{prod_i E_i} K_ell | < eps`.

Proof mechanism. First compactify each marginal in L1 while preserving the cap and mass. For compactly supported marginals, purify coordinates one at a time. At coordinate i define the finite vector measure on the compact support

`nu_i(E)=int_E (1,h_1(x),...,h_m(x)) dx`,

where each `h_ell` is the partial expectation of `K_ell` against the other current marginals. By Lyapunov convexity, the range of `nu_i` is compact and convex. Since

`int g_i(x)(1,h_1,...,h_m)dx = int_0^1 nu_i({g_i>=t})dt`,

that vector lies in the range, so one measurable set of measure one replaces `g_i` while preserving all m kernel integrals exactly. Iterate over i. Finally approximate each bounded measurable unit set in symmetric difference by a bounded finite union of intervals of exact measure one. The product L1 error controls all kernels simultaneously.

This strictly strengthens one-kernel equality-of-suprema: a single product indicator can preserve any finite battery of bounded tests to arbitrary accuracy. It does NOT give one indicator for a countably infinite family or an attained optimizer.

## 2. New cut-free D5 theorem

For a finite symmetric matrix A define the complete disjoint fifth exterior energy

`D_5^perp(A)=sum_{R,C: |R|=|C|=5, R cap C=empty} det A[R,C]^2`.

The partner random-cut theorem gives a physical partition `V=L disjoint_union Rside` with

`e_5(A[L,Rside]^T A[L,Rside]) >= 4^{-5} D_5^perp(A)`.

Apply the pinned D5 theorem to this actual original-coordinate cross block. Therefore

`||p_Q||_infinity <= 10 sqrt(2e) D_5^perp(A)^(-1/10)`.

Numerically the constant is `23.316439815971...`. Equivalently, every unit-measure finite-union product set satisfies the geometric slab estimate

`|{x in prod E_i: x^T A x in J}| <= 10 sqrt(2e) D_5^perp(A)^(-1/10) |J|`.

By the finite-family purification lemma (or directly by D5's arbitrary-law scope), the same constant holds for arbitrary independent cap-one laws. Thus a slab witness of ratio R forces

`D_5^perp(A) <= (10 sqrt(2e)/R)^10`.

This is a cut-free matrix-only obstruction: a diverging counterexample sequence must drive the complete disjoint fifth exterior energy to zero.

## 3. Scalar-Schur bordered-six consequence

For a physical pivot `a=A_kk!=0`, write the scalar Schur complement `S=B-a^{-1}cc^T`, so

`Q=a(X_k+a^{-1}c^T Z)^2 + R(Z)`, `R(Z)=Z^T S Z`.

The partner bordered identity at m=5 is

`B_{6,k}^perp(A)=a^2 D_5^perp(S)`.

The cut-free D5 theorem gives

`||p_R||_infinity <= 10 sqrt(2e) D_5^perp(S)^(-1/10)`.

For any probability density p with `||p||_infinity<=M`, layer cake gives the sharp cap-only half-Riesz estimate

`sup_s int |x-s|^{-1/2}p(x)dx <= int_0^infinity min(1,2M/u^2)du = 2 sqrt(2M)`.

The one-coordinate square peel therefore yields

`||p_Q||_infinity <= 4 sqrt(5 sqrt(2e)) (|A_kk|^8 B_{6,k}^perp(A))^(-1/20)`.

The constant is `13.657654210287...`.

Hence every slab witness of ratio R and every nonzero physical pivot k satisfy

`|A_kk|^8 B_{6,k}^perp(A) <= (13.657654210287/R)^20`.

This is the first new obstruction intended for the partner's trihub survivor: substantial bordered three-volume can coexist with high output density only while every bordered sixth-volume escape around the same pivot is quantitatively absent. The remaining closure must therefore combine the partner's cut-free two/trihub packet with this forced low fifth-exterior-complexity regime, rather than assuming a single large minor or bounded support.
