SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T02:04:35Z.
attacking: QFORM-O3-TWO-INTERNAL-RANK2-BANKS-ROUTING-v1 — extract a product-preserving payable grouped packet from two rank-two source banks.

# fleet03/B19 r22 — one-rank-one / two-rank-two O3 routing theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Fresh owner control:** revision `2026-09-22.15`  
**Control main observed at startup:** `yspennstate/math-research-brain@01cd2bed706607ca647497ead5b4f28ee81a9ef0`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED TARGET-LEVEL SUBBRANCH AND STRUCTURAL DICHOTOMY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Exact target and correction boundary

The unrestricted target remains OPEN: for every dimension, every independent real coordinate family with marginal densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. A continuous representative is a separate desired conclusion and remains open globally.

This run uses no post-rotation independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea estimate, positive moment of a conditional projection density, worst-fiber supremum, or selection of one universally good physical `3x3` minor. In particular, it respects the live `QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1`: a bounded two-dimensional projection density by itself is not enough for a nonlinear indefinite quadratic pushforward. Whenever a two-dimensional projected receiver is used below, its original-product provenance is retained through a completed product-projection theorem.

The immediate predecessor is fleet03/B19 r21,

`yspennstate/math-open-problems@207a77337f6b3587233055160a27b317b2491342`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T010143Z-fleet03-B19-QFORM-r21/REPORT.md`.

That run closes the exactly-one-internal-rank-two O3 chamber by a robust `1+2` grouped packet. Its first remaining exact-rank-three O3 chamber is the state with at least two resource banks of internal spectral rank at least two. The present run attacks the first nontrivial case of that debt: exactly one bank is spectral-rank one and the other two are spectral-rank two.

## 2. Source-valid analytic inputs

I use the following completed results only at their stated scopes.

1. **Rank-one-bank Schur pivot, fleet03/B19 r19.** If a disjoint original-coordinate bank has spectral frame `lambda vv^T`, `t=v^T Mv`, and `a=lambda t !=0`, then

   `||p_Q||_infinity <=16 sqrt(60) [lambda |a| |det M|]^(-1/4)`.

   Since `a=lambda t`, its controlling currency is

   `theta=lambda^2 |t| |det M|`.

   Source: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T223200Z-fleet03-B19-QFORM-r19/REPORT.md`.

2. **Robust grouped near-null payment, fleet03/B19 r21.** For one genuinely independent cap-one scalar and one two-dimensional original-product orthogonal projection of density cap at most `e`, an active `3x3` symmetric matrix `K=[[a,b^T],[b,C]]` with `s_min(K)>=s`, `D=|det K|`, and `|a|<=s/2` has the cross-transverse resource `P>=D/2`; the completed fleet01/B16 projection-product theorem then yields

   `||p_Q||_infinity <=103680^(1/3) e^(2/3) (D P)^(-1/6)`.

   Arbitrary affine terms from conditioning outside the active source banks are allowed. Source dependency: fleet01/B16 canonical report `yspennstate/math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T003846Z/REPORT.md`.

3. **Weighted affine-fiber product projection.** A two-dimensional orthogonal projection of independent cap-one physical coordinates has joint density cap at most `e`; a normalized one-dimensional linear form has density cap at most `sqrt(2)`. Canonical source: fleet02/B06 `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

4. **Designated partner fleet04/B19.** `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` gives, in its residual-diffuse exact-null-coloop scope and `0<D_res<=1`,

   `||p_Q||_infinity <34 sqrt(log(e/D_res))`,

   with continuous density. Canonical source: `yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

No source is enlarged beyond those scopes.

## 3. Exact one-rank-one / two-rank-two frame geometry

Work in the exact-rank-three core

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`.                    (3.1)

Partition the original-coordinate spectral rows into three disjoint source banks

`H`, `G_1`, `G_2`.                                                   (3.2)

Assume

`S_H=sum_(h in H) u_h u_h^T=lambda vv^T`,                            (3.3)

with `0<lambda<=1`, `|v|=1`, while

`S_j=sum_(i in G_j) u_i u_i^T`, `rank(S_j)=2`, `j=1,2`.              (3.4)

Parseval gives

`lambda vv^T+S_1+S_2=I_3`.                                         (3.5)

Let `P=I-vv^T`, identify `v^perp` with `R^2`, and define the transverse compressions

`A_j=(P S_j P)|_(v^perp)`, `d_j=det A_j`.                           (3.6)

Then

`A_1+A_2=I_2`.                                                       (3.7)

Because each `A_j` is positive semidefinite, `0<=d_j<=1`.

### Lemma 3.1 — exact mixed-volume conservation

Define the mixed source triple energy

`tau=sum_(h in H, i in G_1, k in G_2) det(u_h,u_i,u_k)^2`.           (3.8)

Then

`tau=lambda(1-d_1-d_2)`.                                            (3.9)

#### Proof

Write `u_h=c_h v`, so `sum_h c_h^2=lambda`. Only the transverse projections of `u_i,u_k` enter the determinant with `v`. Hence

`tau=lambda sum_(i,k) det(Pu_i,Pu_k)^2`.                             (3.10)

For two positive semidefinite `2x2` frame sums `A_1,A_2`, Cauchy--Binet gives

`sum_(i,k) det(Pu_i,Pu_k)^2`
` =det(A_1+A_2)-det A_1-det A_2`.                                  (3.11)

Using (3.7), the right side is `1-d_1-d_2`. QED.

Now choose any full-column-rank `3x2` matrices `W_j` with

`W_j W_j^T=S_j`,                                                    (3.12)

and define the grouped spectral maps

`L_j=[sqrt(lambda)v, W_j]`.                                         (3.13)

Since `rank(S_j)=2`, the rank-one determinant update in a basis beginning with `v` gives

`det(L_j)^2=det(lambda vv^T+S_j)=lambda d_j`.                       (3.14)

Let

`K_j=L_j^T M L_j`, `D_j=|det K_j|`.                                (3.15)

Therefore

`D_j=|det M| lambda d_j`.                                           (3.16)

Finally, for every physical triple `I={h,i,k}` with one index in each bank,

`|det A[I,I]|=|det M| det(R_I)^2`.                                 (3.17)

Thus the complete mixed principal-triple packet is

`mu=sum_(h,i,k)|det A[{h,i,k},{h,i,k}]|`
`  =|det M| tau`
`  =|det M| lambda(1-d_1-d_2)`.                                    (3.18)

Combining (3.16)-(3.18) yields the exact conservation law

`boxed: D_1+D_2+mu=|det M| lambda.`                                (3.19)

This is an aggregate identity. No single physical minor is selected.

## 4. Failure of both grouped determinant exits forces a near-complementary two-plane skeleton

Put

`m=1-d_1-d_2`, so `mu=|det M|lambda m`.                             (4.1)

Assume `mu>0`. If both grouped determinant currencies are small relative to the mixed packet,

`D_1<mu/4`, `D_2<mu/4`,                                           (4.2)

then by (3.16) and (4.1)

`d_1<m/4`, `d_2<m/4`.                                             (4.3)

Because `d_1+d_2+m=1`, (4.3) implies

`boxed: m>2/3.`                                                     (4.4)

There is a sharper geometric statement. Since `A_2=I_2-A_1`, diagonalize them simultaneously. Let the eigenvalues of `A_1` be `r,s in [0,1]`; then those of `A_2` are `1-r,1-s`, and

`d_1=rs`, `d_2=(1-r)(1-s)`,
`m=r(1-s)+s(1-r)`.                                                  (4.5)

A direct identity gives

`boxed: m^2-4d_1d_2=(r-s)^2.`                                      (4.6)

From (4.3), `d_1d_2<m^2/16`, hence

`|r-s|>(sqrt(3)/2)m>1/sqrt(3)`.                                   (4.7)

Therefore failure of both determinant exits is not an amorphous low-determinant state. It forces the two independent rank-two source banks into a quantitatively near-complementary transverse skeleton: one transverse direction is strongly carried by `G_1`, while the complementary direction is strongly carried by `G_2`.

This is the structural half of the new routing theorem.

## 5. A grouped determinant exit is payable except for a sharply isolated small-rank-one-mass corner

The live O3 packet supplied by the preceding B10/B19 decomposition has

`mu>=1/512`.                                                        (5.1)

Suppose for some `j in {1,2}`

`D_j>=mu/4`.                                                        (5.2)

Then

`D_j>=1/2048`.                                                      (5.3)

Put

`t=v^T Mv`.                                                         (5.4)

We split according to the same scalar Rayleigh quantity used by the rank-one-bank Schur theorem.

### 5.1 Small Rayleigh relative to grouped transverse determinant

Assume

`|t|<=d_j/2`.                                                       (5.5)

Define the normalized rank-one-bank aggregate

`Z=lambda^(-1/2) sum_(h in H)c_h X_h`;                              (5.6)

its density is at most `sqrt(2)`. Because `S_j` has exact rank two, the entire `G_j` contribution can be represented as

`W_j Y`, `Y=U_j^T X_(G_j)`, `U_j^T U_j=I_2`,                       (5.7)

where `Y` is a genuine two-dimensional orthogonal projection of the original product source. Its joint density cap is at most `e`. Since `H` and `G_j` are disjoint original-coordinate banks, `Z` and the full pair `Y` are genuinely independent.

Condition on every coordinate in the third bank `G_(3-j)`. This creates arbitrary affine and constant terms in `(Z,Y)` but does not alter their quadratic core or independence.

Normalize the scalar by

`X_0=sqrt(2)Z`,                                                     (5.8)

so `X_0` has density cap one. The active spectral map is

`L_0=[sqrt(lambda/2)v,W_j]`.                                       (5.9)

From (3.5),

`L_0L_0^T=(lambda/2)vv^T+S_j <= I_3`;                             (5.10)

therefore every singular value of `L_0` is at most one. Also

`det(L_0)^2=lambda d_j/2`.                                         (5.11)

For three singular values at most one, their product is at most the smallest squared singular value, so

`s_min(L_0)^2>=lambda d_j/2`.                                      (5.12)

Let

`K_0=L_0^T M L_0`, `s_0=s_min(K_0)`, `D_0=|det K_0|`.              (5.13)

Since `s_min(M)>=1`,

`s_0>=s_min(L_0)^2>=lambda d_j/2`.                                (5.14)

The scalar entry is

`a_0=(lambda/2)t`,                                                  (5.15)

so (5.5) gives

`|a_0|<=lambda d_j/4<=s_0/2`.                                     (5.16)

Moreover

`D_0=D_j/2>=1/4096`.                                               (5.17)

The scaled near-null cross-resource lemma from r21 therefore gives a transverse currency

`P>=D_0/2`.                                                         (5.18)

Applying the completed projection-product cross-transverse theorem with receiver cap `e`,

`||p_Q||_infinity`
` <=103680^(1/3)e^(2/3)(D_0P)^(-1/6)`
` <=103680^(1/3)e^(2/3)2^(1/6)4096^(1/3)`
` =1643.310509...`
` <1644`.                                                           (5.19)

This payment does **not** use only the pair density cap: the source theorem retains the pair's original-product projection structure, exactly as required by the live B16 correction.

### 5.2 Non-small Rayleigh: rank-one-bank Schur pivot

Assume instead

`|t|>d_j/2`.                                                        (5.20)

The rank-one-bank pivot currency is

`theta=lambda^2 |t| |det M|`.                                      (5.21)

Using (5.20) and (3.16),

`theta>(lambda/2)D_j`.                                             (5.22)

Hence, whenever additionally

`lambda>=1/64`,                                                     (5.23)

(5.3) gives

`theta>1/262144=2^(-18)`.                                          (5.24)

The r19 rank-one-bank Schur theorem now yields

`||p_Q||_infinity`
` <=16sqrt(60) theta^(-1/4)`
` <16sqrt(60)2^(18/4)`
` =2804.339494...`
` <2805`.                                                           (5.25)

No sign of `t` or `M` is assumed.

## 6. Main new routing theorem

### Theorem 6.1 — `QFORM-O3-ONE-RANK1-TWO-RANK2-ROUTING-v1`

Consider an exact-rank-three O3 packet with disjoint source banks `H,G_1,G_2` satisfying (3.3)-(3.5), where `H` has spectral rank one and both `G_1,G_2` have exact spectral rank two, and assume the live mixed principal-triple packet obeys `mu>=1/512`.

Then every state satisfying

`lambda>=1/64`                                                     (6.1)

and

`max(D_1,D_2)>=mu/4`                                               (6.2)

has an essentially bounded output density with the explicit universal estimate

`boxed: ||p_Q||_infinity<2805.`                                   (6.3)

More precisely, if the grouped determinant exit (6.2) occurs, its small-Rayleigh side is paid by `<1644` **without any lower bound on `lambda`**; only the non-small-Rayleigh side uses (6.1).

If instead both grouped determinant exits fail, then the exact frame geometry forces

`boxed: m>2/3, |r-s|>1/sqrt(3).`                                  (6.4)

Consequently every unpaid state in this one-rank-one/two-rank-two chamber lies in one of only two residual mechanisms:

1. **small rank-one mass / non-small Rayleigh:** `lambda<1/64` together with `|t|>d_j/2` for each large grouped-determinant exit that occurs; or
2. **near-complementary rank-two skeleton:** both `D_j<mu/4`, hence (6.4).

This is a strict narrowing of r21's `QFORM-O3-TWO-INTERNAL-RANK2-BANKS-ROUTING-v1`. It retains complete original-product source provenance throughout and never pays a reciprocal single physical minor.

Continuity is **not claimed** for Theorem 6.1; the branch proves essential boundedness.

## 7. Designated partner fleet04/B19 applied to an actual inequality

The designated partner's completed adaptive Hausdorff--Young theorem gives, in its exact residual-diffuse null-coloop scope,

`||p_Q||_infinity<34 sqrt(log(e/D_res))`, `0<D_res<=1`.             (7.1)

Apply it on the concrete interval

`e^(-8)<=D_res<=1`.                                                 (7.2)

Then `log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity<102.`                                     (7.3)

This is an actual target-level inequality for arbitrary cap-one product laws inside the partner theorem's proved scope. I do not transfer (7.3) to the new O3 frame solely by analogy.

## 8. Compact correction-safe proof map after r22

The current B19 assembly is now:

1. Prior low-offdiagonal, diagonal, physical-pivot, ridge/diffuse, exact-cross-rank, null-coloop and grouped O0/O1/O2/O3 branches remain paid at their exact hypotheses.
2. r21 removes the O3 chamber with exactly one rank-two resource bank and two rank-one companions.
3. Theorem 6.1 now removes a dimension-free, sign-free portion of the next chamber: one rank-one resource bank plus two rank-two banks. A large grouped `1+2` determinant is paid either by the product-preserving near-null mechanism or by the aggregate rank-one-bank Schur pivot.
4. Failure of both grouped determinant exits is converted into the explicit transverse spectral gap (6.4), giving a concrete object for the next product-bank transducer rather than a vague aggregate packet.
5. The exact-rank-three states in which all three resource banks have spectral rank at least two, and any bank of spectral rank three, remain separate; arbitrary additional spectrum remains a separate global descent debt.

The **first unpaid implication** produced by this run is now

`QFORM-O3-NEARCOMPLEMENTARY-TWORANK2-TRANSDUCER-v1`:

> Starting from two disjoint original-product exact-rank-two banks whose transverse compressions sum to `I_2` and have eigenvalue separation `>1/sqrt(3)`, use the complementary strong directions jointly, before conditioning or reciprocal-minor selection, to force one already-paid product-preserving ridge/cross/grouped packet. The theorem must allow arbitrary within-bank self quadratic phases and arbitrary fragmented cap-one input laws.

The small-`lambda` / non-small-Rayleigh corner in Theorem 6.1 is a second explicit residual branch. A proof may merge it with the same two-bank transducer, because small `lambda` means the two rank-two banks carry almost all spectral frame mass.

The unrestricted QFORM conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity is still **OPEN**.

## 9. Arithmetic regression

The accompanying `CHECK.py` / `CHECK_OUTPUT.txt` verify the exact scalar identity (4.6) on a deterministic grid, the implications `(4.2)=>(4.4),(4.7)` away from equality, and the displayed numerical constants. They are regression checks only; the proof is Sections 3-6.
