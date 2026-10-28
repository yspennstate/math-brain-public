SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T03:20:39Z.
attacking: recycle the deletion-child third-spectral-loss branch into a fourth-large-eigenvalue spill at the parent scale, then pay its diffuse spectral window or extract a stronger physical localized witness.

# account03/B08 r49 — deletion loss forces rank-four spectral spill

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Run: `20260924T032039Z-account03-B08-qform-diffuse-r49`  
Status: **NEW SUPPORTING STRUCTURAL/ANALYTIC ROUTER / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. The new point is that, in a genuinely diffuse top-three eigenframe, failure of the designated account04/B08 deletion-child theorem by **loss of the child's third target-scale singular value** cannot simply be recorded as an unresolved branch. It forces the parent to have a fourth eigenvalue almost as large as the original target scale. That fourth-direction spill is either paid immediately by the reviewed spectral-window theorem or creates a quantitatively stronger ORIGINAL-coordinate localized witness.

No moment, support, Gaussian, log-concavity, connectedness, spectral-coordinate independence, arbitrary-joint coarea estimate, pointwise van-der-Corput decay, or small-random-perturbation deletion is used.

## 1. Source boundary and completed inputs


### 1.1 Designated partner account04/B08 r2

Canonical source:

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

Its theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` says: if an ORIGINAL-coordinate deletion child `C` has three eigenvalues of modulus at least `m>0`, and the physical spectral projection

`P_C(m/64)=1_{|C|>=m/64}`

satisfies

`max_k (P_C(m/64))_kk <= 1/32`,

then the full parent quadratic form has a continuous `C_0` density with

`||p_Q||_infinity <= C_R/m < 64/m`,                         (1.1)

where

`C_R=288 sqrt(3e)/13 = 63.26405187778285...`.               (1.2)

The parent coordinate is merely conditioned; all parent cross coefficients are retained as affine terms.

### 1.2 Global affine-uniform spectral-window theorem

The same reviewed ridge-window source is

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

At any scale `M>0`, if a symmetric matrix has at least three eigenvalues of modulus at least `M` and

`max_k (1_{|A|>=M/64})_kk <= 1/32`,                            (1.3)

then the full cap-one product quadratic form has a continuous `C_0` density with

`||p_Q||_infinity <= C_R/M < 64/M`.                           (1.4)

Only this exact stated scope is used below.

### 1.3 Immediate predecessor

Account03/B08 r48 is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T021854Z-account03-B08-qform-diffuse-r48/REPORT.md`.

Its unpaid route included a designated-partner failure in which the same physical deletion child `C_j` either had `s_3(C_j)<L/64` or a high-leverage child spectral-window coordinate. The present run removes the raw `s_3(C_j)<L/64` branch from the list of terminal obstructions whenever the selected top-three parent frame is diffuse at `j`.

## 2. A sharp deterministic deletion-spill inequality

Let `A=A^T in R^{n x n}`. Write its eigenvalues in nonincreasing absolute value, and let

`s_1(A)>=s_2(A)>=...`

denote the singular values. Fix `L>0` with

`s_3(A)>=L`.                                                     (2.1)

Choose three eigenvectors corresponding to the three largest absolute eigenvalues and assemble them as the columns of `U in R^{n x 3}`. Thus

`U^T U=I_3`,
`A U=U Lambda`,
`s_min(Lambda)=s_3(A)>=L`.                                      (2.2)

For an ORIGINAL coordinate `i`, put

`p_i=||U_{i,*}||_2^2`,                                         (2.3)

let `T={1,...,n}\{i}`, and define the literal principal child

`C=A[T,T]`.                                                     (2.4)

### Lemma 2.1 — `QFORM-DIFFUSE-DELETION-RANK4-SPILL-v1`

For every such `i`,

`boxed:
 s_3(C) >= (1-p_i)L - s_4(A).
`                                                                  (2.5)

Equivalently, for every `theta>=0`,

`s_3(C)<theta L`

forces

`boxed:
 s_4(A) > (1-p_i-theta)L.
`                                                                  (2.6)

This is useful only when the right side is positive; in the diffuse regime it is nearly the full target scale.

### Proof

Split the parent exactly into its top-three spectral packet plus the orthogonal spectral remainder:

`A=A_0+E`,
`A_0=U Lambda U^T`,
`||E||op=s_4(A)`.                                                (2.7)

Because `U_T` is obtained by deleting row `i`,

`G:=U_T^T U_T=I_3-u_i u_i^T`,                                  (2.8)

where `u_i=U_{i,*}^T`. Hence

`lambda_min(G)=1-p_i`.                                          (2.9)

If `p_i<1`, write the polar factorization

`U_T=V G^(1/2)`, `V^T V=I_3`.                                  (2.10)

Then

`(A_0)[T,T]=V [G^(1/2) Lambda G^(1/2)] V^T`.                   (2.11)

The three nonzero singular values of the left side are therefore exactly those of the central `3x3` matrix. Consequently

`s_3((A_0)[T,T])
 =s_min(G^(1/2) Lambda G^(1/2))`
`>=s_min(G^(1/2))^2 s_min(Lambda)`
`>=(1-p_i)L`.                                                   (2.12)

The principal compression satisfies

`||E[T,T]||op<=||E||op=s_4(A)`.                                (2.13)

Weyl's singular-value perturbation inequality applied to

`C=(A_0)[T,T]+E[T,T]`

gives

`s_3(C)>=s_3((A_0)[T,T])-||E[T,T]||op`
`>=(1-p_i)L-s_4(A)`,                                           (2.14)

which is (2.5). Rearranging gives (2.6). The case `p_i=1` is trivial because the right side of (2.5) is nonpositive. QED.

### Interpretation

For an exact-rank-three parent (`s_4(A)=0`), deleting a coordinate of leverage `p_i` leaves a **third** child singular value at least `(1-p_i)L`; the usual rank-loss estimate that guarantees only two child directions is unnecessarily weak in this exact-rank-three/diffuse situation. For a general parent, the only way a diffuse physical deletion can lose that third direction is for the complementary parent spectrum itself to carry a fourth direction of comparable size.

## 3. The rank-four spill is itself a diffuse/localized router

Assume now a diffuse selected-three gate

`p_i<=mu`,                                                        (3.1)

and choose `theta` with

`0<theta<1-mu`.

Put

`delta=1-mu-theta>0`.                                           (3.2)

If the child loses its third direction,

`s_3(C)<theta L`,                                                (3.3)

Lemma 2.1 gives

`s_4(A)>delta L`.                                                (3.4)

Thus the parent has not merely three but at least **four** eigenvalues of modulus greater than `delta L`.

Let

`P_delta=1_{|A|>=delta L/64}`.                                  (3.5)

There are two possibilities.

### (S-D) diffuse fourth-direction spill

If

`max_k (P_delta)_kk<=1/32`,                                     (3.6)

apply the completed spectral-window theorem at scale `M=delta L`. It gives

`boxed:
 ||p_Q||_infinity <= C_R/(delta L) < 64/(delta L),
 p_Q in C_0(R).
`                                                                  (3.7)

### (S-L) localized fourth-direction spill

If (3.6) fails, choose an ORIGINAL coordinate `k` with

`(P_delta)_kk>1/32`.                                            (3.8)

Spectral energy gives

`||A e_k||_2^2
 >= (delta L/64)^2 (P_delta)_kk
 > (delta L)^2/(64^2*32)`.                                     (3.9)

Therefore

`||A e_k||_2 > delta L/(256 sqrt(2))`.                          (3.10)

Since

`||A e_k||_2^2=|A_kk|^2+||A[k,-k]||_2^2`,                      (3.11)

one of those two pieces is at least `||Ae_k||/sqrt(2)`. Hence

`boxed:
 max{|A_kk|, ||A[k,-k]||_2} > delta L/512.
`                                                                  (3.12)

This is an actual original-coordinate localized witness at the **parent spill scale**. No spectral-coordinate conditioning occurs.

## 4. Designated account04/B08 partner applied at an actual inequality

Now combine the new spill lemma with `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` on the SAME deletion child `C`.

If

`s_3(C)>=theta L`                                                (4.1)

and

`max_k (1_{|C|>=theta L/64})_kk<=1/32`,                         (4.2)

then the designated partner theorem gives the actual parent inequality

`boxed:
 ||p_Q||_infinity <= C_R/(theta L) < 64/(theta L),
 p_Q in C_0(R).
`                                                                  (4.3)

If (4.1) holds but (4.2) fails, choose a physical child coordinate `k`. The same spectral-energy computation inside `C` gives

`max{|C_kk|, ||C[k,T\{k}]||_2} > theta L/512`.                  (4.4)

Because `C` is a literal principal block of `A`, the parent has the corresponding original-coordinate witness

`boxed:
 max{|A_kk|, ||A[k,-k]||_2} > theta L/512.
`                                                                  (4.5)

If (4.1) fails, Section 3 applies: either the parent is paid by (3.7), or it has the stronger spill-scale witness (3.12).

We have therefore proved the following four-way router.

### Theorem 4.1 — `QFORM-DIFFUSE-DELETION-PARTNER-SPILL-ROUTER-v1`

Under `s_3(A)>=L`, `p_i<=mu`, and `0<theta<1-mu`, at least one of the following holds:

1. **Child diffuse payment:**
   `||p_Q||infinity <= C_R/(theta L)` and `p_Q in C_0`.
2. **Child localized witness:** an original coordinate `k!=i` obeys
   `max{|A_kk|,||A[k,-k]||_2}>theta L/512`.
3. **Rank-four spill diffuse payment:**
   `||p_Q||infinity <= C_R/((1-mu-theta)L)` and `p_Q in C_0`.
4. **Rank-four spill localized witness:** an original coordinate `k` obeys
   `max{|A_kk|,||A[k,-k]||_2}>(1-mu-theta)L/512`.

The alternatives are obtained with no assumption on signs and no assumptions on any input moments or supports.

## 5. Numerical specialization at the live diffuse gates

Use the live B08 diffuse threshold

`mu=1/48`                                                       (5.1)

and the r48/account04 deletion threshold

`theta=1/64`.                                                   (5.2)

Then

`delta=1-1/48-1/64=185/192
      =0.9635416666666666...`.                                 (5.3)

The four alternatives become:

### 5.1 Designated-partner child payment

If `s_3(C)>=L/64` and its `L/4096` child window is diffuse,

`boxed: ||p_Q||infinity <4096/L, p_Q in C_0.`                  (5.4)

### 5.2 Child localized witness

If that child window is not diffuse,

`boxed:
 max{|A_kk|,||A[k,-k]||_2}>L/32768
 =3.0517578125e-5 L.
`                                                                  (5.5)

### 5.3 Child spectral loss becomes almost-full-scale fourth spectrum

If

`s_3(C)<L/64`,                                                  (5.6)

then

`boxed: s_4(A)>185L/192=0.9635416667...L.}`                    (5.7)

If the parent window at threshold

`(185/192)L/64=185L/12288`

is diffuse, the global spectral-window theorem pays

`boxed:
 ||p_Q||infinity
 <= [288sqrt(3e)/13]*(192/185) L^-1
 <65.658/L,
 p_Q in C_0.
`                                                                  (5.8)

If that window is localized, then some physical parent coordinate satisfies

`boxed:
 max{|A_kk|,||A[k,-k]||_2}
 >185L/98304
 =0.001881917317708333...L.
`                                                                  (5.9)

The witness (5.9) is about 61.67 times larger than the child-window witness (5.5). Thus the previous raw `s_3(C)<L/64` survivor has been replaced by a much stronger object.

## 6. Application to the r48 weak-carrier debt

The r48 aligned-carrier theorem ended with the following designated-partner failure at a chosen physical light coordinate `j`:

- weak rank-one/near-rank-one carrier currency; and
- either `s_3(C_j)<L/64`, or a high-leverage child `L/4096` window.

Whenever that same `j` lies in the diffuse top-three parent frame, `p_j<=1/48`, Theorem 4.1 removes the first item as a terminal spectral branch:

`boxed:
 s_3(C_j)<L/64
 =>
 [ ||p_Q||infinity<65.658/L, p_Q in C_0 ]
 or
 [ exists k: max(|A_kk|,||A[k,-k]||)>0.0018819L ].
`                                                                  (6.1)

If instead `s_3(C_j)>=L/64`, the actual account04/B08 theorem either pays `<4096/L` or returns the child localized witness (5.5).

Thus, in the diffuse-selected-three portion of r48, the remaining debt is no longer **weak carrier plus unexplained child spectral loss**. It is **weak carrier plus an explicit physical localized coordinate**, at either the child-window scale or the much stronger rank-four-spill scale. This is precisely complementary to localized-coordinate conditioning.

The result does not yet consume those localized witnesses in every sign/degeneracy configuration, so it is not a full proof.

## 7. Regression computation

A deterministic seeded checker was run for the new inequality (2.5).

- 9,900 dense random symmetric-matrix/deletion cases, dimensions 5 through 15: zero violations; minimum observed margin `s_3(C)-[(1-p_i)L-s_4(A)]` was `0.08232285743995005`.
- 9,600 exact-rank-three random-frame/deletion cases, dimensions 4 through 19: zero violations; minimum observed margin above `(1-p_i)L` was `8.19e-10`, consistent with near equality and floating-point error.
- Constants reproduced:
  `delta=185/192`, `C_R=63.26405187778285...`, `C_R/delta=65.65782681369896...`, child witness `1/32768`, spill witness `185/98304`.

These computations are regression evidence only. The proof of Lemma 2.1 and Theorem 4.1 is analytic.

## 8. What remains

The unrestricted QFORM conjecture remains OPEN. Global continuity remains OPEN; continuity is proved on the two payment branches (4.3) and (3.7).

The next B08 implication is

`QFORM-WEAK-CARRIER-PLUS-EXPLICIT-LOCALIZED-ROW-COMPILER-v3`:

> consume the r48 weak-carrier state after the present router has replaced child spectral loss by an actual physical scalar/star witness. The two witness scales are `theta L/512` from a localized deletion-child window and `(1-mu-theta)L/512` from the new rank-four spill. Preserve the weak aligned carrier, arbitrary diagonal twists, all signs, and all remaining spectrum; use a product-safe localized-coordinate theorem rather than assuming a good rotated pivot.

A second useful direction is to combine the new fourth-direction spill with a four-direction diffuse cross-block compiler, which may bypass the localized branch entirely when the added fourth eigenvector is itself delocalized.

No counterexample is claimed.
