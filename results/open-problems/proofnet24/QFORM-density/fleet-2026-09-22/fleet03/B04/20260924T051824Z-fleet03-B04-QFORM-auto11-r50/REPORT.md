SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T05:18:24Z.
attacking: pair-anchored third-volume product-Fourier promotion, then a quantitative bridge from the designated partner's fourth-volume double-anchor packet.

# fleet03/B04 r50 — pair-anchored E3 hub promotion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: **NEW SUPPORTING FOURIER THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner target is not proved or disproved here. The theorem below is a source-coordinate product-Fourier receiver. It retains arbitrary same-bank quadratic terms, affine leakage, extra spectrum, and all signs. It does not use law-uniform pointwise quadratic-phase decay, independence after a random-variable rotation, arbitrary-joint coarea, or a worst-fiber density supremum.


## 1. Pinned analytic inputs

The product-Fourier input is the completed grouped projected-crossing theorem at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

In its notation, with `k` literal hub directions, an `ell`-volume projected crossing remainder, `d=k+ell>2`, hub density cap `M_H`, hub-to-right singular product `S`, and residual compound `Z_ell`, it gives

`||p_Q||_infinity <= d/(d-2) 2^((k+3ell)/(2d)) exp(ell/(2d)) M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,

provided the canonical `ell`-volume row marginals are at most `1/2`; for `ell=1` the exponential factor is omitted. The theorem permits arbitrary internal hub functions, arbitrary same-bank light curvature, every diagonal and every linear term. Its characteristic-function envelope is integrable when `d>2`.

The exact-rank crossing theorem in the same source says that for a rank-`r>2` crossing with singular-value product `S_B` and projection-density caps `M_X,M_Y`,

`||p_Q||_infinity <= r/(r-2) (M_X M_Y/S_B)^(1/r)`.

The designated-partner input is fleet04/B04 r2,

`QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1`,

at `yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

At its live high-fourth-volume carrier gate, failure of the anchored entropy branch produces a literal physical row pair `{a,b}` whose canonical fourth-volume pair inclusion probability is `>2/75`.

## 2. Pair-anchored third-volume factorization

Let `I,J` be disjoint sets of ORIGINAL coordinates and let

`M=A[I,J]`.

Write its physical rows as `m_r`. Fix distinct `a,b in I`. Put

`D_2 = det Gram(m_a,m_b)`.

Let `P_2` be the orthogonal projection in coefficient space onto `span(m_a,m_b)`, and for `r in I\{a,b}` put

`c_r=m_r(I-P_2)`.

Define the pair-anchored third-volume currency

`K_ab := sum_{r in I\{a,b}} det Gram(m_a,m_b,m_r)`.             (2.1)

Whenever `K_ab>0`, necessarily `D_2>0`. The Gram-Schur identity gives, term by term,

`det Gram(m_a,m_b,m_r)=D_2 ||c_r||_2^2`,                        (2.2)

hence

`boxed: K_ab = D_2 Z_1,  Z_1:=sum_r ||c_r||_2^2.`              (2.3)

This is the key aggregate-before-reciprocal identity: the two-hub area and the entire residual one-volume recombine before any inverse power is paid.

## 3. Main theorem — `QFORM-PAIR-ANCHORED-E3-PROMOTION-v1`

Let the original coordinates be independent and have probability densities bounded by one. Let

`Q=X^T A X+b^T X+c`

with arbitrary real symmetric `A` and arbitrary affine terms. For a literal cross block `M=A[I,J]` and a physical row pair `{a,b} subset I`, if `K_ab>0`, then `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity <= 3*2^(5/6) K_ab^(-1/6).`                   (3.1)

Numerically the front coefficient is

`3*2^(5/6)=5.345392308842036...`.                               (3.2)

### Proof

Condition all original coordinates outside `I union J`. This only creates affine terms and preserves the density caps and independence of the surviving original coordinates. The estimates below are uniform in the conditioned values.

Let

`q_r=||c_r||_2^2/Z_1`.

**Diffuse residual.** Suppose every `q_r<=1/2`. Keep the literal variables `X_a,X_b` as two hubs. Their joint density is a product density bounded by one, so `M_H<=1`. The hub-to-right matrix is the two-row block with rows `m_a,m_b`, hence its singular-value product is

`S=sqrt(D_2)`.

The projected light crossing has `ell=1` currency `Z_1`. Apply the grouped theorem with `(k,ell,d)=(2,1,3)`. The `ell=1` entropy factor cancels exactly, giving

`||p_Q||_infinity
 <=3*2^(5/6) S^(-1/3) Z_1^(-1/6)
 =3*2^(5/6) D_2^(-1/6) Z_1^(-1/6)
 =3*2^(5/6) K_ab^(-1/6)`,                                      (3.3)

by (2.3).

**Heavy residual.** Suppose some `c_s` has `q_s>1/2`. Then the literal three-row cross block indexed by `{a,b,s}` has row-Gram determinant

`D_3=det Gram(m_a,m_b,m_s)=D_2||c_s||_2^2=q_s K_ab>K_ab/2`.     (3.4)

Condition all other left-bank variables. The three surviving original coordinates form the complete left side of an exact rank-three crossing to `J`; arbitrary internal terms on both sides remain allowed. The left three-dimensional density cap after the orthogonal SVD coordinate change is at most one (it is a full-dimensional unit-Jacobian image of the original three-variable product density). The right rank-three orthogonal projection has density cap at most `2^(3/2)`. The crossing singular-value product is `sqrt(D_3)`. Thus the exact-rank-three theorem gives

`||p_Q||_infinity
 <=3*(2^(3/2)/sqrt(D_3))^(1/3)
 =3*sqrt(2) D_3^(-1/6)
 <3*2^(2/3) K_ab^(-1/6)`,                                      (3.5)

which is strictly smaller than the coefficient in (3.1).

The two cases are exhaustive. In both cases the cited Fourier theorem supplies a common integrable characteristic-function envelope, uniform in every conditioned original coordinate. Averaging back preserves that envelope, so Fourier inversion gives a continuous `C_0` density. QED.

### Scope

The theorem is not a claim that the three-large-eigenvalue hypothesis forces `K_ab` to a universal scale. In particular, the live `Omega_2` third-compound overlap sector still needs an aggregation theorem before one can extract this literal cross-block currency without selecting a weak pair. The result removes the *analytic* row-marginal obstruction once pair-anchored third volume has actually been formed.

## 4. Designated fleet04/B04 result applied at an actual inequality

Use the partner's double-anchor branch on the same literal cross block `M`. It yields

`H_ab^(4) := sum_{|R|=4,{a,b} subset R} det Gram(M_R)
 > (2/75) E_4(M)`.                                              (4.1)

With the same pair projection as in Section 2,

`H_ab^(4)=D_2 e_2(CC^T)`,
`K_ab=D_2 e_1(CC^T)`.                                           (4.2)

For nonnegative eigenvalues, `e_1^2>=2e_2`. Therefore

`K_ab^2 >=2D_2 H_ab^(4) > (4/75)D_2 E_4(M)`,                   (4.3)

and the new theorem gives the explicit partner-spent inequality

`boxed:
 ||p_Q||_infinity
 < 3*2^(5/6)*(75/4)^(1/12)
    [D_2 E_4(M)]^(-1/12)`                                      (4.4)

with numerical front coefficient

`6.824377206888847...`.                                         (4.5)

This is a different payment from r48's area-free fourth-volume receiver: (4.4) uses the partner's pair packet to downshift one degree and becomes stronger when the physical pair area is correspondingly robust. It keeps the same full ambient form and has a continuous `C_0` density.

## 5. Fully dense genuinely rotated indefinite stress test

Let

`Q0 = (1/7) [[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`,

so `Q0^T Q0=I_3`. Define the `5 x 3` Parseval frame `R` by

`r_1=(sqrt(15)/4,0,0)`,
`r_2=(0,sqrt(15)/4,0)`,

and let its last three rows be the rows of

`Q0 diag(1/4,1/4,1)`.

Then `R^T R=I_3`. Let the `4 x 3` Parseval frame `V` have rows

`(1,1,1)/2`, `(1,-1,1)/2`, `(1,1,-1)/2`, `(1,-1,-1)/2`,

and put

`M=R V^T`.

Every one of the `20` physical entries of `M` is nonzero. Both `R` and `V` have orthonormal columns, so the three nonzero singular values of `M` are exactly `1,1,1`.

Now set

`A_* = [[J_5/100, 2M], [2M^T, -J_4/100]]`.                    (5.1)

Every entry of `A_*` is nonzero. The pure-cross part has nonzero spectrum `+2,+2,+2,-2,-2,-2`. The same-bank perturbation has operator norm at most `1/20`; Weyl therefore leaves at least six eigenvalues with absolute value at least `39/20>1`. Thus `A_*` is a genuinely rotated, fully dense, indefinite target matrix.

For the first two left physical rows of the cross block `2M`,

`D_2 = 16*(15/16)^2 =225/16`,                                  (5.2)

while the projected residual one-volume is `Z_1=4`. Hence

`boxed: K_12=D_2 Z_1=225/4.`                                   (5.3)

The new theorem gives, for every admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(5/6)*(225/4)^(-1/6)
 =2.730816364073070... .`                                      (5.4)

The density is continuous and vanishes at infinity.

For comparison on this identical matrix, the generic exact-rank-three crossing theorem sees singular-value product `8` and the two generic rank-three projection caps, giving `3`; the marginal-free `E_3` receiver has `E_3(2M)=64` and gives about `4.2266`. Thus the pair-anchored product-Fourier promotion is a strict quantitative improvement on this dense rotated indefinite form.

## 6. Remaining full-target implication

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN** separately.

The new theorem pays a literal pair-anchored `E_3` packet with no row-marginal loss. The first structural debt is now sharper:

`QFORM-OMEGA2-TO-PAIR-ANCHORED-E3-OR-SINGULAR-COLLAR-v1`:

> Starting from the global two-shared third-compound sector `Omega_2>=1/4`, aggregate the denominator-free pair Schur numerators across physical shared pairs before paying an inverse pair scale. Force either a target-scale literal pair-anchored third-volume currency `K_ab` (now paid by (3.1)), or route concentration on rank-one/near-rank-one pair bases into the already-proved singular-star, zero-pivot, square-bank, ridge, or grouped-hub receivers while retaining arbitrary same-bank curvature.

The exact fixed-pair Schur-numerator identities from fleet01/B09 show why this aggregation step cannot be replaced by choosing the largest local minor. No full-target counterexample was found in this run.
