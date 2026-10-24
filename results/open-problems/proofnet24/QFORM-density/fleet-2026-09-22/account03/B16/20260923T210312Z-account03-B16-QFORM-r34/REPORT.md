SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T21:03:12Z.
attacking: the epsilon-uniform two-bank endpoint by testing the fixed-P/Minkowski bridge inside an authentic, perfectly conditioned product projection and isolating the product-safe replacement.

# account03/B16 r34 — authentic fragmented mixed-slice obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SOURCE-VALID OBSTRUCTION TO A PRECISE EPSILON-INTERPOLATION MECHANISM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** no new full-target density theorem is claimed here; global continuity remains open.

## 1. Exact live debt

The immediately preceding B16 theorem is

`yspennstate/math-open-problems:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T202349Z-account03-B16-QFORM-r30/REPORT.md`.

In the canonical two-bank packet it proves, for nonzero `epsilon`,

`||p_Q||_infinity <= 3 [L_H K_2 K_3 / |alpha epsilon lambda|]^(1/3)`

for

`Q=2 alpha H L + beta L^2 +2 delta L V + lambda V^2+2 epsilon L P + affine`,

while retaining arbitrary dependence inside each three-dimensional bank. The remaining live implication is to remove the negative power of `epsilon` by marrying this punctured estimate to the exact-zero shared-hub operator. A tempting move is to freeze the `P` coordinate in each bank, apply the exact-zero `L^2` operator on every slice, and then integrate the slice norms by Minkowski. The theorem below shows that this move is impossible even for an **exact orthogonal image of three independent cap-one scalar laws**. Thus it is not merely an arbitrary-joint-density pathology.

The live corrections are respected: no post-rotation independence, no arbitrary-joint coarea bound, no conditional projection-density cap, and no pointwise law-uniform van der Corput decay is used.

## 2. The mixed norm that the fixed-P bridge would need

For a bank density `g(l,v,p)` define

`B(g):= integral_R [ integral_R2 g(l,v,p)^2 dl dv ]^(1/2) dp.`       (2.1)

If one freezes `p` in a two-bank zero-endpoint argument, applies the shared-hub/rank-one-crossing `L^2` operator on each fixed pair `(p_A,p_B)`, and then uses the triangle or Minkowski inequality in `(p_A,p_B)`, the resulting constant contains

`B(g_A) B(g_B)`.                                                     (2.2)

This is exact: the fixed-slice amplitudes enter through their `L^2(dl dv)` norms, and absolute integration over the two frozen `p` variables is precisely (2.2).

The question is therefore whether the actual bounded-density projection theorem, plus perfect conditioning of the projection, can bound `B(g)` universally. It cannot.

## 3. Theorem: a perfectly conditioned authentic product bank has unbounded `B(g)`

### `QFORM-ORTHOGONAL-FRAGMENTED-SLICE-L1L2-OBSTRUCTION-v1`

For every integer `N>=3` there exist three independent real random variables `X_1,X_2,X_3`, each with probability density bounded by one, and an **orthogonal** `3 x 3` matrix `U`, such that the density `g_N` of

`(L,V,P)=U(X_1,X_2,X_3)^T`

satisfies

`||g_N||_infinity=1`,                                               (3.1)

its coefficient Gram is exactly `I_3`, and nevertheless

`B(g_N)=2^(-1/4) * (4/3) * [ (N-1)/sqrt(N) + 1/N ]`.               (3.2)

In particular

`B(g_N) ~ (4/(3*2^(1/4))) sqrt(N) -> infinity`.                    (3.3)

Thus no dimension-free or fragmentation-free fixed-`P`/Minkowski bridge can follow from the bounded-density projection theorem, even in the best-conditioned three-source case.

### Proof

Let `ell=1/N`, fix the integer base `K=10`, and put

`a_j=K^j`, `j=0,...,N-1`,

`E_N= union_j [a_j,a_j+ell]`,

`f_N=1_(E_N)`.                                                       (3.4)

The intervals are disjoint and have total length one, so `f_N` is a probability density with `0<=f_N<=1`. Take `X_1,X_2` iid with density `f_N`, and take `X_3` uniform on `[0,1]`, independently. Define the orthogonal coordinates

`L=(X_1+X_2)/sqrt(2)`,
`V=X_3`,
`P=(X_1-X_2)/sqrt(2)`.                                               (3.5)

The transformation `(X_1,X_2,X_3)->(L,V,P)` has absolute determinant one. Hence

`g_N(l,v,p)=f_N((l+p)/sqrt(2)) f_N((l-p)/sqrt(2)) 1_[0,1](v)`,       (3.6)

so `g_N` itself is an indicator density and (3.1) holds. The coefficient matrix in (3.5) is orthogonal, so there is no small singular value, small determinant, or leverage defect hidden in the construction.

Because `g_N^2=g_N`, for each fixed `p`,

`||g_N(.,.,p)||_2^2 = integral g_N(l,v,p) dl dv = p_P(p)`,          (3.7)

where `p_P` is the density of `P`. Let

`h_N(d)=(f_N * tilde f_N)(d)`, `tilde f_N(x)=f_N(-x)`.               (3.8)

Since `P=(X_1-X_2)/sqrt(2)`,

`p_P(p)=sqrt(2) h_N(sqrt(2)p)`,                                    (3.9)

and therefore

`B(g_N)=2^(-1/4) integral_R sqrt(h_N(d)) dd`.                       (3.10)

It remains to evaluate the last integral exactly. Put

`T_ell(s)=(ell-|s|)_+`.                                             (3.11)

Then

`h_N(d)=sum_(i,j) T_ell(d-(a_i-a_j))`.                              (3.12)

All off-diagonal differences `a_i-a_j`, `i!=j`, are distinct. Indeed, if `K^j-K^i=K^l-K^k` with `j>i`, `l>k`, then the number of trailing base-`K` zeros forces `i=k`, and then `j=l`; negative differences are handled by sign. The distinct centers are nonzero integers, while every triangle in (3.12) has support width `2/N<1`. Hence all off-diagonal triangles are pairwise disjoint and are also disjoint from the diagonal packet at zero.

For one triangle,

`integral sqrt(T_ell(s)) ds = 4 ell^(3/2)/3.                         (3.13)`

There are `N(N-1)` off-diagonal ordered pairs. The `N` diagonal triangles coincide, giving `N T_ell(d)`. Consequently

`integral sqrt(h_N(d)) dd`
` = N(N-1) * 4/(3 N^(3/2)) + sqrt(N)*4/(3 N^(3/2))`
` = (4/3)[(N-1)/sqrt(N)+1/N].`                                     (3.14)

Combining (3.10) and (3.14) proves (3.2). QED.

## 4. Two-bank consequence for the live interpolation attempt

Take the two banks `A,B` to be independent copies of the bank above. Both are literal orthogonal projections of independent cap-one original coordinates, both have Gram `I_3`, and the standard two- and three-dimensional projection density theorems give universal caps (indeed the three-dimensional joint density here is exactly at most one). But a proof that first freezes `P_A,P_B`, applies the epsilon-zero two-dimensional operator, and then uses absolute Minkowski in the frozen variables necessarily pays

`B(g_N)^2 ~ [16/(9 sqrt(2))] N`.                                   (4.1)

Thus that proof constant diverges linearly in `N` despite perfect matrix conditioning. The obstruction is caused only by allowed fragmentation of the one-dimensional source densities.

This is stronger than the generic statement that an arbitrary bounded joint density can have bad fibers: the present `g_N` comes from an **actual linear image of an independent product law satisfying the owner hypotheses**.

It also explains why r30's common-`P`-frequency argument is structurally different. For the same `g_N`, three-dimensional Plancherel still gives

`||g_N||_2^2=1`,                                                     (4.2)

while its `(L,V)` marginal has the usual universal projection cap. Hence the frequency-side `L^2` energies used in r30 remain bounded even as the physical-slice norm (3.2) diverges. Any successful epsilon-uniform bridge must therefore keep a Hilbert-space pairing or cancellation in the `P` variable; it cannot reduce first to absolute fixed-`P` slices.

## 5. Companion cap-only pathology in the exact canonical quadratic geometry

For clarity about the role of product provenance, there is an even sharper **non-product-projection** warning. Let `L,H,U` be independent uniform variables on `[-1/2,1/2]` and let `V` be uniform on `[0,1]`. Define

`P=-V^2/(2L)+U` a.e. on `L!=0`.                                    (5.1)

The change `(L,V,U)->(L,V,P)` has Jacobian one, so `(L,V,P)` has a probability density bounded by one, and its `(L,V)` marginal is exactly the unit density on `[-1/2,1/2] x [0,1]`. Nevertheless, for the rank-three quadratic polynomial

`Q=2HL+V^2+2LP`                                                     (5.2)

one has the exact cancellation

`Q=2L(H+U)`.                                                        (5.3)

The matrix of (5.2) in `(H,L,V,P)` has nonzero eigenvalues `sqrt(2),-sqrt(2),1`. Since `W=H+U` has triangular density `1-|w|` on `[-1,1]`, the density of `Q` is, for `0<|q|<1`,

`p_Q(q)=log(1/|q|)-1+|q|`,                                         (5.4)

which diverges logarithmically at zero.

This is **not a counterexample to QFORM** because the curved triple (5.1) has not been represented as a linear projection of independent original coordinates. Its purpose is precise: even an independent cap-one hub together with bounded three- and two-dimensional joint projection-height caps would not close the canonical packet. The linear-product provenance of `P` is the missing resource.

## 6. Designated account04/B16 result applied at an actual inequality

The current completed designated-partner report is

`yspennstate/math-open-problems@a70c05e517e8a195a31ab4f4c301c672d1c8d4e6`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260923T192012Z-account04-B16-QFORM-r2/REPORT.md`.

Its `QFORM-PHYSICALPAIR-BANK-OVERLAP-v1` theorem gives

`||p_Q||_infinity <=9.2002740353 [D |det Lambda| tau det G_b]^(-1/5).`  (6.1)

On its live exact-rank-three packet, if

`det G_b >= W_b s^2/(64 D tau)`,                                   (6.2)

then `W_b>61/1728` and `|det Lambda|>=s^3`, so

`D |det Lambda| tau det G_b >61 s^5/(64*1728)`.                   (6.3)

Therefore

`||p_Q||_infinity`
` <9.2002740353 (64*1728/61)^(1/5) s^(-1)`
` =41.2552799658... s^(-1) <=41.256`,                              (6.4)

because `s>=1`. This is an actual target inequality, and the partner theorem gives continuity on that branch. The present obstruction concerns the complementary shared-bank/vanishing-leakage endpoint and does not reopen (6.4).

## 7. Exact successor lemma after this obstruction

The failed bridge can now be removed from the search tree. The source-valid remaining analytic obligation is not a bound on fixed-`P` slices. In a canonical two-bank packet with original-product banks, it is a **vector-valued shared-hub estimate** that preserves `P`-frequency pairing:

**`QFORM-EPSILON-UNIFORM-VECTOR-TTSTAR-v1` (OPEN).** Prove a characteristic-function or small-ball bound uniform in `epsilon` for

`2 alpha H(L_A+L_B) + lambda(V_A+V_B)^2`
` +2 epsilon(L_A+L_B)(P_A+P_B)`

with arbitrary within-bank quadratic phases and allowed compatible affine shifts, using only disjoint original-source independence and the product-projection structure. The proof must keep at least an `L^2` pairing in the `P` variable (or an equivalent cancellation) until after the two banks are combined; Sections 3-4 show that `L^1_P L^2_(L,V)` is unavailable even for an orthogonal product bank.

The newest diffuse-frame obstruction at `proofnet24/QFORM-density/interactive/20260923T205600Z-physical-pair-averaging-obstruction/REPORT.md` independently points in the same direction: physical-pair averaging or a disjoint matching loses the cross-pair mass in a diffuse frame. Together these two exact obstructions leave full-bank/vector-valued aggregation as the viable B16 mechanism rather than another physical-slice decomposition.

The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Arbitrary additional spectrum beyond exact-rank-three structural packets remains a separate interface. Global continuity remains OPEN.
