SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T09:58:03Z.
attacking: the surviving diffuse exact-rank-two non-ultracollapse packet; force two literal large physical diagonals to become a uniformly conditioned original-coordinate indefinite pair, while retaining the designated partner's physical-star alternative.

# fleet03/B13 r48 — ultracollapse or a uniformly conditioned physical indefinite pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T095803Z-fleet03-B13-qform-r48`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING STRUCTURAL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

All random coordinates below are the original independent physical coordinates. The only rotation is within the latent two-dimensional coefficient space of an exact rank-two carrier. No Gaussianity, log-concavity, moment, compact-support, connected-support, interval-extremality, centered-uniform, bounded-fragment-count, post-rotation independence, law-uniform pointwise van-der-Corput estimate, unrestricted fiber supremum, or deletion of a coefficient-small quadratic random term is used. Full-target continuity is not asserted.

## 1. Extremal-product reduction at the correct scope

I first record the optimizer-free reduction because it is the assignment-level interface to the geometric sublevel problem.

### Proposition 1.1 — cap-one product laws reduce to arbitrary unit product indicators in supremal form

Let `K:R^n->[0,1]` be measurable. Then

\[
\sup_{\substack{0\le f_i\le1\\\int f_i=1}}
\int_{\mathbb R^n}K(x)\prod_{i=1}^n f_i(x_i)\,dx
=
\sup_{|E_1|=\cdots=|E_n|=1}
\int_{\prod_iE_i}K(x)\,dx.                                      \tag{1.1}
\]

The right-hand supremum may, with arbitrarily small loss, be restricted to bounded finite unions of intervals of total measure one in each coordinate. There is no assertion that an optimizer exists, that any `E_i` is one interval, that it is centered, that the product has bounded diameter, or that the number of components is uniformly bounded.

#### Proof

For one nonnegative measurable section `g` and one density `0<=f<=1`, `int f=1`, layer cake gives

\[
\int gf
=\int_0^\infty\int_{\{g>t\}}f(x)\,dx\,dt
\le\int_0^\infty\min\{1,|\{g>t\}|\}\,dt.                       \tag{1.2}
\]

The right side is exactly the supremum of `int_E g` over measurable `E` of measure one (equivalently, the integral of the decreasing rearrangement of `g` over `[0,1]`). No threshold set need attain that supremum. Therefore

\[
\int gf\le\sup_{|E|=1}\int_Eg.                                  \tag{1.3}
\]

Apply (1.3) successively to the coordinate sections of `K prod_i f_i`, each time choosing only an arbitrarily close near-maximizing unit-measure set. This gives the `<=` direction of (1.1); the reverse direction follows because indicator densities `1_E`, `|E|=1`, are admissible. Lebesgue regularity approximates each finite-measure `E_i` in symmetric difference by bounded finite unions of intervals; because `0<=K<=1` and the other product factors have mass one, the resulting change in the integral is at most the symmetric-difference error. Adjusting a terminal interval restores exact measure one. QED.

For the slab kernel

\[
K(x)={\bf1}_{\{x^TAx\in J\}},                                   \tag{1.4}
\]

(1.1) says that a uniform small-ball/density bound is equivalently a geometric estimate

\[
\left|\left\{x\in\prod_iE_i:x^TAx\in J\right\}\right|
\le C|J|                                                        \tag{1.5}
\]

for all arbitrary measurable `|E_i|=1`. This is the reduction used below; no interval extremality is smuggled in.

The designated partner fleet04/B13 independently proves the same optimizer-free transfer and is source-pinned below; I include the proof here so the present B13 deliverable is self-contained at the assignment interface.

## 2. Fresh source-pinned inputs


The mathematical inputs actually used are:

1. Own r45, source-pinned at
   `yspennstate/math-open-problems@a1ccc98be0cd4752de1b2b29e4c46f8193854757`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260924T063322Z-fleet03-B13-qform-r45/REPORT.md`.
   In the surviving diffuse exact-rank-two chamber
   \[
   A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad
   c_i:=\|u_i\|_2^2\le\frac13,\qquad s_3(A)\ge1,               \tag{2.1}
   \]
   every sufficiently high slab-ratio witness satisfies
   \[
   D_\Lambda:=|\det\Lambda|\le H\rho^{-2},\qquad
   H:=\sqrt{1536e^2}=106.534455308869\ldots .                  \tag{2.2}
   \]
   If `|lambda_1|>=|lambda_2|` are the latent eigenvalues, then
   \[
   |\lambda_2|\le\sqrt{D_\Lambda}\le\sqrt H\,\rho^{-1},
   \qquad \sqrt H=10.321552950446\ldots .                      \tag{2.3}
   \]
   R45 also records the rank inequality
   \[
   s_2(D)\ge1-|\lambda_2|.                                     \tag{2.4}
   \]

2. The scalar-Schur receiver of fleet01/B13,
   `QFORM-DIAG-RANK2-DIFFUSE-SCHUR-SEPARABLE-v1`, source-pinned at
   `yspennstate/math-open-problems@7e23bcf74fa1862bfe9054591c946bfd8f3276cb` (the theorem is also present in the later indexed snapshot `461ca4597face7955d318d0540729ca6b809fce2`). For any original physical `h` with `d_h!=0` and actual scalar pivot `a_h=A_hh!=0`,
   \[
   (1-c_h)|a_h d_h\det\Lambda|\le1024e^2\rho^{-4}.             \tag{2.5}
   \]
   Crucially this receiver retains the entire diagonal residual and arbitrary affine terms.

3. The designated partner fleet04/B13 newest completed theorem,
   `yspennstate/math-open-problems@8b90908a934588442491cf1a41c7db12ece290bf`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260924T061740Z-fleet04-B13-nearnull-star-r3/REPORT.md`. If `k` maximizes `|d_i|`, then every witness satisfies
   \[
   \boxed{
   D_\Lambda<3072e^2\rho^{-4}
   \quad\text{or}\quad
   \|A_{-k,k}\|_2\ge2^{-1/2}.}
                                                                    \tag{2.6}
   \]
   If `C` is the four-coordinate set of largest `|d_i|`, containing `k`, its star alternative further splits as
   \[
   \|A_{C\setminus\{k\},k}\|_2\ge\frac12
   \quad\text{or}\quad
   \|A_{C^c,k}\|_2\ge\frac12.                                  \tag{2.7}
   \]

The live corrections are obeyed: no post-rotation independence, no arbitrary-joint coarea lemma, no pointwise law-uniform quadratic phase decay, no positive moment of worst conditional projection-density caps, and no inference that coefficient-small quadratic tails are probabilistically negligible.

## 3. First essential implication: force a uniformly conditioned physical pair

The previous normal form still left a conceptual gap: a fixed physical star need not by itself provide a uniformly conditioned physical `2x2` quadratic pair. The aim here is to show that in the non-ultracollapse branch it actually does, using the two literal large diagonal entries forced by `s_3(A)>=1`.

### Theorem 3.1 — `QFORM-ULTRACOLLAPSE-OR-UNIFORM-INDEFINITE-PAIR-v1`

Assume (2.1) and let a slab witness have ratio `rho`. Suppose (2.2) holds. Put

\[
\rho_0:=8\sqrt H=82.572423603571\ldots .                         \tag{3.1}
\]

For every `rho>=rho_0`, one of the following alternatives holds.

**A. Ultra-collapse:**
\[
\boxed{D_\Lambda<6144e^2\rho^{-4}.}                              \tag{3.2}
\]
In particular
\[
\boxed{|\lambda_2|<32\sqrt6\,e\,\rho^{-2}
      =213.068910617739\ldots\rho^{-2}.}                         \tag{3.3}
\]

**B. Uniform original-coordinate indefinite pair plus partner star:** there are distinct original physical coordinates `k,j`, with `k` chosen to maximize `|d_i|`, such that
\[
|d_k|,|d_j|\ge\frac78,                                           \tag{3.4}
\]
`d_k,d_j` have the same sign, opposite to the sign of the dominant latent eigenvalue `lambda_1`, and
\[
|A_{kk}|,|A_{jj}|\le\frac27,                                    \tag{3.5}
\]
\[
|A_{kj}|\ge\frac{45}{112}.                                      \tag{3.6}
\]
Consequently the original-coordinate principal block
\[
B:=A[\{k,j\},\{k,j\}]
 =\begin{pmatrix}A_{kk}&A_{kj}\\A_{kj}&A_{jj}\end{pmatrix}      \tag{3.7}
\]
is uniformly invertible and indefinite, quantitatively
\[
\boxed{|\det B|\ge\frac{1001}{12544}=0.079799107142857\ldots,} \tag{3.8}
\]
\[
\boxed{\sigma_{\min}(B)\ge\frac{13}{112}
      =0.116071428571429\ldots .}                                \tag{3.9}
\]
At the same physical `k`, the designated partner gives
\[
\boxed{\|A_{-k,k}\|_2\ge2^{-1/2}}                              \tag{3.10}
\]
and, for the four-diagonal core `C`,
\[
\boxed{
\|A_{C\setminus\{k\},k}\|_2\ge\frac12
\quad\text{or}\quad
\|A_{C^c,k}\|_2\ge\frac12.}                                   \tag{3.11}
\]

#### Proof

Rotate only the latent two-dimensional coefficient basis so that
\[
U\Lambda U^T=\lambda_1vv^T+\lambda_2ww^T,
\qquad |\lambda_1|\ge|\lambda_2|,                               \tag{3.12}
\]
with `v,w` orthonormal in `R^n`. This does not rotate any random coordinate.

From (2.3) and `rho>=8 sqrt(H)`,
\[
|\lambda_2|\le\frac18.                                          \tag{3.13}
\]
Then (2.4) gives
\[
s_2(D)\ge1-|\lambda_2|\ge\frac78.                              \tag{3.14}
\]
Because `D` is diagonal, at least two distinct original coordinates have diagonal magnitude at least `7/8`. Let `k` maximize `|d_i|` and let `j` be another such coordinate. Thus (3.4) holds.

Assume Alternative A fails, so
\[
D_\Lambda\ge6144e^2\rho^{-4}.                                   \tag{3.15}
\]
For `h` equal to `k` or `j`, if `A_hh=0` then (3.5) is immediate. Otherwise apply the scalar-Schur inequality (2.5). Since
\[
1-c_h\ge\frac23,\qquad |d_h|\ge\frac78,                         \tag{3.16}
\]
we obtain
\[
|A_{hh}|
\le
\frac{1024e^2\rho^{-4}}
     {(2/3)(7/8)(6144e^2\rho^{-4})}
=\frac27.                                                         \tag{3.17}
\]
So (3.5) always holds.

Now fix `h in {k,j}`. If `d_h` had the same sign as `lambda_1`, then the two terms `d_h` and `lambda_1 v_h^2` reinforce, and the secondary mode can cancel by at most `|lambda_2| w_h^2<=|lambda_2|`. Hence
\[
|A_{hh}|
=|d_h+\lambda_1v_h^2+\lambda_2w_h^2|
\ge |d_h|-|\lambda_2|
\ge\frac78-\frac18=\frac34,                                     \tag{3.18}
\]
contradicting (3.5). Therefore both `d_k` and `d_j` have sign opposite to `lambda_1`, proving the sign assertion.

Define the dominant cancellation masses
\[
m_h:=|\lambda_1|v_h^2\qquad(h=k,j).                              \tag{3.19}
\]
Because `d_h` and `lambda_1` have opposite signs,
\[
m_h\ge |d_h|-|A_{hh}|-|\lambda_2|w_h^2
\ge\frac78-\frac27-\frac18
=\frac{13}{28}.                                                   \tag{3.20}
\]
Therefore the dominant mode contributes
\[
|\lambda_1v_kv_j|=\sqrt{m_km_j}\ge\frac{13}{28}.               \tag{3.21}
\]
For the secondary mode, orthonormality gives
\[
|w_kw_j|\le\frac{w_k^2+w_j^2}{2}\le\frac12,                    \tag{3.22}
\]
so by (3.13)
\[
|\lambda_2w_kw_j|\le\frac1{16}.                                 \tag{3.23}
\]
Since `A_kj=lambda_1 v_kv_j+lambda_2 w_kw_j`, the triangle inequality yields
\[
|A_{kj}|
\ge\frac{13}{28}-\frac1{16}
=\frac{45}{112},                                                  \tag{3.24}
\]
which is (3.6).

Write `a=A_kk`, `b=A_kj`, `c=A_jj`. From (3.5)-(3.6),
\[
ac-b^2\le |a||c|-b^2
\le\left(\frac27\right)^2-\left(\frac{45}{112}\right)^2
=-\frac{1001}{12544}.                                             \tag{3.25}
\]
Thus `B` is indefinite and (3.8) holds. Its two eigenvalues are
\[
\frac{a+c}{2}\pm\sqrt{\left(\frac{a-c}{2}\right)^2+b^2}.       \tag{3.26}
\]
The smaller absolute eigenvalue is bounded below by
\[
|b|-\left|\frac{a+c}{2}\right|
\ge\frac{45}{112}-\frac27
=\frac{13}{112},                                                   \tag{3.27}
\]
proving (3.9).

Finally (3.15) is stronger than the designated partner's threshold `3072 e^2 rho^-4`, so (2.6) forces (3.10), and (2.7) gives (3.11). This is the requested application of a completed fleet04/B13 result to an actual inequality. QED.

## 4. Geometric meaning after extremal-product purification

By Proposition 1.1, any cap-one slab witness can be purified, with arbitrarily small ratio loss, to a product indicator
\[
X\sim\prod_i{\bf1}_{E_i}(x_i)\,dx_i,\qquad |E_i|=1,              \tag{4.1}
\]
where the `E_i` may be arbitrarily fragmented and arbitrarily far apart. Theorem 3.1 is a statement about the coefficient matrix forced by the slab ratio, so it survives this purification unchanged after replacing `rho` by `rho-epsilon` and letting `epsilon downarrow0`.

Thus a hypothetical large-ratio geometric sublevel set
\[
\left|\left\{x\in\prod_iE_i:x^TAx\in J\right\}\right|
=\rho|J|                                                         \tag{4.2}
\]
inside the diffuse exact-rank-two chamber has an exhaustive source-valid fork:

- either the second latent mode is already `O(rho^-2)` via (3.2)-(3.3); or
- two literal original independent coordinates form an indefinite quadratic pair with determinant and smallest singular value bounded below by fixed numerical constants, while one of those same coordinates carries the partner's fixed physical star.

No inverse tiny physical minor is paid. This is exactly the type of geometry needed by the existing indefinite-pair / pair-log / quarter-Riesz receivers.

## 5. Why this advances the remaining receiver problem

Before this run, the non-ultracollapse branch supplied a fixed physical star, but the available indefinite-pair receivers require a genuinely invertible original-coordinate pair. A star alone could in principle coexist with every candidate physical pair becoming nearly singular. Theorem 3.1 rules that out in the present hard exact-rank-two survivor: once the latent determinant is not already `O(rho^-4)`, the spectral requirement forces two large literal diagonals; the scalar-Schur estimate makes both actual pivots small; this forces same-sign dominant-mode cancellation on both coordinates; and that same cancellation automatically creates a uniformly large physical off-diagonal entry between them.

The numerical constants are intentionally conservative and dimension-free. The mechanism uses no support geometry at all, so arbitrary fragmentation and translations remain admissible.

The immediate next obligation is

`QFORM-UNIFORM-INDEFINITE-PAIR-PLUS-PHYSICAL-STAR-RECEIVER-v1`:

> Schur-complete the pair `B` from Theorem 3.1 and prove a dimension-free density payment from the simultaneously retained star (3.10)-(3.11), while retaining the full diagonal `O(rho^-1)` tail and the secondary entangled mode rather than deleting either as a small random perturbation.

There is a promising source-matching analytic interface: fleet01/B06's completed indefinite-pair-plus-rank-one-crossing quarter-Riesz receiver controls precisely an invertible indefinite original pair followed by a genuine rank-one crossing. The remaining work is to prove that the star surviving after the present pair completion contains the needed disjoint rank-one crossing, or else route the failure into the finite four-coordinate core. That implication is not claimed here.

## 6. Exact arithmetic check

The finite checker stored beside this report verifies the constants symbolically/rationally:

- `(2/3)(7/8)(6144)=3584`, hence `1024/3584=2/7`;
- `7/8-2/7-1/8=13/28`;
- `13/28-1/16=45/112`;
- `(45/112)^2-(2/7)^2=1001/12544`;
- `45/112-2/7=13/112`.

These computations only validate arithmetic; the theorem is the exact argument above.

## 7. Status

**Full QFORM remains OPEN / not proved / not disproved.**  
**Full-target continuity remains OPEN.**

This report proves a supporting structural theorem in the exact diffuse diagonal-plus-rank-two survivor and applies the designated fleet04/B13 star theorem at a concrete determinant threshold. Essential boundedness/continuity in the full target is not inferred from this coefficient geometry alone.
