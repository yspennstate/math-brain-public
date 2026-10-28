SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T04:10:20.927846Z.
attacking: the bounded-coordinate survivor after single-edge exterior collapse; prove an any-sign two-physical-pivot distribution-function receiver and use it to close the curved rank-one arrowhead qualitatively without scalar pointwise Fresnel decay.

# Any-sign two-pivot Frostman receiver and curved rank-one-arrowhead compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T041020Z-account01-B01-qform-auto11-r12`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary


The phase-aligned fragmented-support construction is therefore preserved. Nothing below asserts `|E exp(itX^2)| <= C|t|^{-1/2}`. The new mechanism is instead: a quarter-power **distribution-function** estimate for a Schur remainder, upgraded through two literal original-coordinate square completions, plus a joint/conditional mixed-Fresnel estimate only in a spread rank-one-slope branch.

Source-pinned premises actually used:

1. `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`: for any nonzero symmetric residual matrix `S`, arbitrary affine terms and cap-one independent coordinates,

   `sup_w P(|Z^T S Z + ell^T Z + c - w| < rho) <= min(1,5(rho/||S||)^(1/4))`;

   and if a physical 2x2 block is completed, its Schur remainder has operator norm at least `s_3(A)`.

2. `yspennstate/math-open-problems@1297371d82e3b03f014dbbf0d5e22207a763382d`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260924T010808Z-account01-B01-qform-auto11/REPORT.md`: `QFORM-FROSTMAN-TWOSQUARE-LINF-v1`, upgrading any positive Frostman exponent through two source-disjoint adapted original squares.

3. `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`: `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, namely

   `H_(1/2)((U^T X)^T Lambda(U^T X)+b^T X) <=128 |det Lambda|^(-1/4)`

   for arbitrary affine `b` and every invertible symmetric 2x2 `Lambda`.

4. `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`: the proved one-hub mixed-Fresnel theorem and the Fourier-to-half-Riesz / literal square-peel interfaces.

The newest completed designated partner result available during this run is account02/B01 at `yspennstate/math-open-problems@47deae65829b8cae5282751e32d7aa0fb07c51c9`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T040416Z-account02-B01-qform-auto11-r43/REPORT.md`; it proves `QFORM-STAR-EDGE-TAIL-HALFRIESZ-v1` and leaves an almost-single-edge / rank-one-arrowhead endpoint.

## 2. First essential implication: any-sign physical pair via two adapted squares

### Theorem 2.1 — `QFORM-ANYSIGN-PAIR-TWOSQUARE-FROSTMAN-v1`

Let `A` be any real symmetric matrix with

` s_3(A) >= s > 0`.                                             (2.1)

Choose two ORIGINAL coordinates whose principal block is

`P=[[a,c],[c,b]]`,                                              (2.2)

with `a != 0` and `det P != 0`. Put

`d = b-c^2/a = det(P)/a`.                                      (2.3)

For independent cap-one input coordinates and arbitrary affine terms, the full quadratic polynomial has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_2 |a|^(-1/2)|d|^(-2/5)s^(-1/10),`                        (2.4)

where

`C_2 = [2 sqrt(5) J_(1/8)]^(4/5)
     = 27.2653244653667...`,                                   (2.5)

and

`J_beta=max{B(1/2,beta), B(1/2,1/2-beta)+B(1/2-beta,beta)}`.    (2.6)

Equivalently, using `d=det(P)/a`,

`boxed:
 ||p_Q||_infinity
 <= C_2 |a|^(-1/10)|det P|^(-2/5)s^(-1/10).`                   (2.7)

No sign assumption on `P` is imposed. Only essential boundedness is asserted.

### Proof

Reorder the chosen original coordinates first and write

`A=[[P,E],[E^T,C]]`.                                            (2.8)

Completing the first coordinate and then the second is an LDL completion in the ORIGINAL coordinates; it does not rotate the random vector. Including all affine terms, one obtains exactly

`Q=a(X_0+m_0(X_1,Z))^2+d(X_1+m_1(Z))^2+R(Z)`,                  (2.9)

where `Z` is the remaining original-coordinate bank and the quadratic matrix of `R` is the Schur complement

`S=C-E^T P^(-1)E`.                                              (2.10)

The rank-two matrix

`A_0=[[P,E],[E^T,E^T P^(-1)E]]`                                (2.11)

has rank at most two. Since

`A-A_0=diag(0,S)`,                                              (2.12)

the singular-value min-max principle gives

`s_3(A) <= ||S||_op`.                                           (2.13)

Thus `||S||>=s`. The source-pinned arbitrary-rank residual small-ball theorem gives, uniformly in the induced affine term and center `w`,

`P(|R-w|<rho) <= min{1,5 (rho/s)^(1/4)}.                        (2.14)

Apply `QFORM-FROSTMAN-TWOSQUARE-LINF-v1` with

`alpha=1/4`, `beta=1/8`, `K=5 s^(-1/4)`,                       (2.15)

and scalar density caps one. Since

`alpha/(alpha-beta)=2`,
`K^(beta/alpha)=sqrt(5) s^(-1/8)`,                              (2.16)

the source theorem yields

`||p_Q||_infinity
 <= |a|^(-1/2)
    [ |d|^(-1/2) J_(1/8) 2 sqrt(5) s^(-1/8) ]^(4/5),`          (2.17)

which is (2.4). Equation (2.7) is algebra. The coefficient powers in (2.7) sum to `-1`, so the common matrix-scaling homogeneity is exact. QED.

This theorem is a distribution-function replacement for trying to obtain two scalar pointwise Fresnel factors. It also complements the existing indefinite physical-pair density theorem: (2.4) works for definite, indefinite, or mixed-sign nonsingular pairs, at the price of requiring one nonzero literal first pivot.

## 3. A nonzero residual physical edge after one square is always quantitatively payable

Suppose now an ORIGINAL coordinate `X_0` has been completed:

`Q=a(X_0+h(Z))^2+R(Z)`, `a!=0`,                                (3.1)

and the Schur quadratic matrix `S` of `R` has some off-diagonal entry

`m=S_ij != 0`.                                                   (3.2)

Put

`u=S_ii`, `v=S_jj`, `Delta=uv-m^2`.                             (3.3)

### Theorem 3.1 — `QFORM-OUTER-SQUARE-RESIDUAL-EDGE-LINF-v1`

Under `s_3(A)>=s>0`,

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2)
    max{ 128*2^(1/4)|m|^(-1/2),
         C_2*2^(1/5)|m|^(-2/5)s^(-1/10) }.`                    (3.4)

Numerically the two leading constants are

`128*2^(1/4)=152.218510720348...`,
`C_2*2^(1/5)=31.3196333618271...`.                              (3.5)

### Proof

There are two exhaustive cases.

**Case 1: `|Delta| >= m^2/2`.** Condition on every residual original coordinate except `Z_i,Z_j`. The conditional quadratic matrix on this pair is

`Lambda=[[u,m],[m,v]]`,                                        (3.6)

and all couplings to conditioned variables become arbitrary affine terms. The orientation-free rank-two affine theorem therefore gives, uniformly in the conditioning,

`H_(1/2)(R) <=128 |Delta|^(-1/4)
             <=128*2^(1/4)|m|^(-1/2).`                         (3.7)

The literal outer square peel in (3.1) gives the first bound in (3.4).

**Case 2: `|Delta| < m^2/2`.** Then

`|uv|=|Delta+m^2| > m^2/2`,                                    (3.8)

so

`q=max(|u|,|v|) > |m|/sqrt(2).`                                (3.9)

Choose the corresponding original residual coordinate `Z_k`. Because `S` is precisely the Schur complement after eliminating `X_0`, the ORIGINAL physical 2x2 principal block of the full matrix on `{0,k}` has first LDL pivot `a` and second LDL pivot exactly `S_kk`; hence its determinant is `a S_kk`. Apply Theorem 2.1 to this actual physical pair. Using (3.9),

`||p_Q||_infinity
 <=C_2 |a|^(-1/2) q^(-2/5)s^(-1/10)
 <=C_2*2^(1/5)|a|^(-1/2)|m|^(-2/5)s^(-1/10).`                 (3.10)

This is the second bound in (3.4). QED.

This removes a qualitative singular-pair obstruction: even when the residual 2x2 pair is exactly parabolic (`Delta=0`), its large diagonal forced by the edge is converted into a second ORIGINAL scalar pivot, and the residual quarter-Frostman exponent supplies the remaining smoothing.

## 4. Curved rank-one two-hub arrowhead: exhaustive compiler

Let `H=(H_1,H_2)` be two original hub coordinates and `Y=(Y_1,...,Y_m)` a disjoint bank of original leaves. Consider the residual

`R=H^T C H + 2(b^T H)(z^T Y)
   +sum_l d_l Y_l^2 + affine`,                                  (4.1)

where `C` is an arbitrary symmetric 2x2 matrix, the leaf self-block is diagonal, and

`kappa=||b||_2 ||z||_2 >0`.                                    (4.2)

Together with an outer literal square as in (3.1), this is exactly the support-two isotropic arrowhead shape isolated by the designated partner after its latent zero-wedge reduction.

### Theorem 4.1 — `QFORM-TWOHUB-RANK1-SLOPE-COMPILER-v1`

If `s_3(A)>=s>0`, then

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2)
 max{ 128*2^(3/4) kappa^(-1/2),
      C_2*2^(3/5) kappa^(-2/5)s^(-1/10) }.`                    (4.3)

Numerically,

`128*2^(3/4)=215.269482304951...`,
`C_2*2^(3/5)=41.3265039834376...`.                              (4.4)

### Proof

Split according to the physical leaf leverage.

**Diffuse leaf slope.** If

`max_l z_l^2/||z||^2 <=1/2`,                                   (4.5)

choose a hub coordinate `r` with `|b_r|>=||b||/sqrt(2)` and condition on the other hub. The conditional residual is exactly a one-hub mixed-Fresnel packet with diagonal leaves. The source theorem gives

`|phi_R(t)|
 <=min{1, [2pi/(|b_r| ||z||)] |t|^(-1)}`.                      (4.6)

The source Fourier-to-half-Riesz lemma therefore yields

`H_(1/2)(R)
 <=8 (|b_r| ||z||)^(-1/2)
 <=8*2^(1/4) kappa^(-1/2).`                                    (4.7)

After the outer square this is already smaller than the first term of (4.3).

**Concentrated leaf slope.** Otherwise choose a leaf `l` with

`|z_l|>||z||/sqrt(2)`                                          (4.8)

and a hub `r` with `|b_r|>=||b||/sqrt(2)`. Their residual physical edge has magnitude

`|m|=|b_r z_l| >= kappa/2`.                                    (4.9)

Apply Theorem 3.1 to this literal residual edge. Its first branch gives

`128*2^(1/4)|a|^(-1/2)|m|^(-1/2)
 <=128*2^(3/4)|a|^(-1/2)kappa^(-1/2)`,                         (4.10)

while its second branch gives

`C_2*2^(1/5)|a|^(-1/2)|m|^(-2/5)s^(-1/10)
 <=C_2*2^(3/5)|a|^(-1/2)kappa^(-2/5)s^(-1/10).`                (4.11)

This proves (4.3). QED.

The point is that arbitrary same-hub curvature `C` is retained. The earlier critical-half-Riesz counterexample for a rank-one cross with adversarial same-bank curvature is not contradicted: in the concentrated branch we do not claim half-Riesz control of the singular parabolic residual pair; we switch mechanisms and spend the resulting literal second scalar pivot through a distribution-function estimate.

## 5. Actual application of the newest account02/B01 partner result

The newest completed designated partner theorem is `QFORM-STAR-EDGE-TAIL-HALFRIESZ-v1` in

`yspennstate/math-open-problems@47deae65829b8cae5282751e32d7aa0fb07c51c9`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T040416Z-account02-B01-qform-auto11-r43/REPORT.md`.

On its explicit full-target family

`Q_*=X_0^2+2H(U+V/2)`,                                         (5.1)

it has `a=1`, heavy edge `beta=1`, tail norm `C=1/2`, and spectrum

`{-sqrt(5)/2,0,1,sqrt(5)/2}`.                                  (5.2)

The partner theorem gives the actual law-uniform inequality

`boxed:
 ||p_(Q_*)||_infinity <=2^(23/8)=7.33603234563737... .`         (5.3)

The present run then attacks exactly the partner's remaining rank-one-arrowhead endpoint. In the partner finite-leak notation the support-two isotropic survivor has

`H[S,L]=beta w_S z_L^T`.                                       (5.4)

Set

`b=beta w_S`, `z=z_L`,
`kappa=|beta| ||w_S|| ||z_L||`.                                (5.5)

Whenever `kappa>0`, Theorem 4.1 supplies the explicit equation-level continuation

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2)
 max{215.269482305 kappa^(-1/2),
     41.326503984 kappa^(-2/5)s^(-1/10)}.`                     (5.6)

Thus genuine same-bank hub curvature is no longer a qualitative obstruction in this partner-produced arrowhead. What remains is quantitative routing when the available currencies `|a|` and `kappa` are allowed to become simultaneously tiny under the global spectral normalization.

Likewise the partner's `almost-singleedge` endpoint is now quantitatively controlled whenever its literal residual edge `m` is nonzero by (3.4), including the zero-tail case that its edge/tail theorem cannot use.

## 6. Strict target stress at the parabolic residual endpoint

Take four ORIGINAL independent cap-one coordinates `(X_0,H_1,H_2,Y)` and

`Q_par=X_0^2+H_2^2+(H_1+Y)^2`.                                 (6.1)

Its coefficient matrix is

`diag(1, [[1,0,1],[0,1,0],[1,0,1]])`                           (6.2)

in the order `(X_0,H_1,H_2,Y)`, and has spectrum

`{2,1,1,0}`.                                                     (6.3)

Hence `s_3(A)=1`: this is an owner-target form. After the outer square, the residual pair `(H_1,Y)` has

`u=v=m=1`, `Delta=uv-m^2=0`.                                   (6.4)

So the direct invertible-rank-two half-Riesz receiver is unavailable exactly. Theorem 3.1 switches to its second branch: `q=1`, and Theorem 2.1 gives

`boxed:
 ||p_(Q_par)||_infinity <= C_2
 =27.2653244653667... .`                                        (6.5)

This is a clean mechanism witness for why the any-sign two-pivot distribution-function receiver is genuinely needed rather than merely restating the rank-two affine theorem.

## 7. Deterministic checks and limitations

Finite deterministic checks associated with this report verify:

- `J_(1/8)=13.931514779840125...` and `C_2=27.2653244653667...`;
- the constants in (3.5) and (4.4);
- for 300 seeded random symmetric matrices with an invertible chosen physical pair, the rank-two completion matrix in (2.11) had third singular value at most `8.51e-15`, and `||S||/s_3(A)>=1.0228` in that sample;
- for 10,000 seeded concentrated-arrowhead samples satisfying the leverage condition opposite to (4.5), the deterministic inequalities `|m|>=kappa/2` and, on the small-determinant subbranch, `max(|u|,|v|)>=|m|/sqrt(2)` had zero violations;
- the stress matrix (6.2) has spectrum `{0,1,1,2}` and residual pair determinant zero.

These are diagnostics, not independent mathematical review.

The unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The estimates here deteriorate as the literal outer pivot `a`, residual edge `m`, or aggregate rank-one-slope currency `kappa` tends to zero. Therefore they do not by themselves prove that the bare three-large-eigenvalue condition forces one uniformly good receiver.

The first unpaid implication for this line is now

`QFORM-FINITELEAK-TINY-CURRENCY-AGGREGATION-v1`:

> In the remaining finite-leak geometry, prove that the spectral normalization forces at least one already-paid currency (outer scalar pivot, partner edge-tail product, literal residual edge, rank-one-slope aggregate, physical pair, or three-square/grouped receiver) to stay at target scale, or aggregate many individually tiny original-coordinate currencies before inversion. Do not discard a small random quadratic tail and do not invoke scalar pointwise Fresnel decay.

No counterexample to the full conjecture was found.
