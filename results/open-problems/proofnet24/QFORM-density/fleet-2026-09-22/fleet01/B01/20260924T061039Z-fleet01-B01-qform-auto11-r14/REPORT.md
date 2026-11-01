SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-24T06:10:39Z.
attacking: remove the explicit tiny outer-pivot loss on the exact diagonal-plus-star/arrowhead branch, and combine the newest fleet02/B01 generic-edge quarter-Riesz estimate with two literal square completions.

# fleet01/B01 — full arrowhead closure and a two-square generic-edge compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T061039Z-fleet01-B01-qform-auto11-r14`  
Role: Oscillatory replacement  
Status: **NEW TARGET-LEVEL SUBCLASS THEOREM + NEW SUPPORTING COMPILER / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The owner target is unchanged: independent ORIGINAL real coordinates with densities at most one; arbitrary real symmetric `A`; at least three singular/eigenvalue magnitudes at least one; prove a universal essentially bounded density for `Q=X^T A X`, or give a valid counterexample. The full conjecture and the requested full-target continuity conclusion remain OPEN.


The phase-aligned fragmented-support counterexample remains binding. No claim of the form

`|E exp(i t X^2)| <= C |t|^{-alpha}`

with `alpha>0` is used. The only oscillatory input below is a joint physical-edge Plancherel estimate already proved by the designated partner, and the only other smoothing mechanisms are exact distribution-function/fractional-potential identities in ORIGINAL coordinates.

Source-pinned premises actually used:

1. **Previous B01 star aggregation / outer-pivot theorem.**  
   `yspennstate/math-open-problems@6c6b0d78a725b7a1cfa941b0497d17cc6a2223ba`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260924T051102Z-fleet01-B01-qform-auto11-r13/REPORT.md`.  
   It proves `QFORM-STAR-DISPERSION-HALFRIESZ-v1`:

   `H_(1/2)(R) <= 8 (C^4-c_*^4)^(-1/8)`

   for a literal diagonal-plus-star quadratic polynomial, and the exact rank-one singular-value reduction `s_3(A)<=s_2(S)` after one scalar completion.

2. **Any-sign two-literal-pivot receiver.**  
   `yspennstate/math-open-problems@5a750c5b1188ea297a92c01b9692de5d87ab7f4c`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260924T041020Z-fleet01-B01-qform-auto11-r12/REPORT.md`.  
   If `s_3(A)>=1`, a first literal pivot is `a!=0`, and a second literal LDL pivot is `d!=0`, then

   `||p_Q||_infinity <= C_2 |a|^(-1/2)|d|^(-2/5)`,

   `C_2=27.2653244653667...`.

3. **Orientation-free rank-two affine half-Riesz theorem, including its sharper in-range constant.**  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,  
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.  
   In the physical two-coordinate case, after conditioning all other ORIGINAL coordinates, the induced affine vector lies in the physical coordinate plane, so the sharper source bound applies:

   `H_(1/2)(Z^T Lambda Z + ell^T Z + c)
      <=16 sqrt(30) |det Lambda|^(-1/4)`.

4. **Newest completed designated partner fleet02/B01.**  
   `yspennstate/math-open-problems@6efd5124aa67510aa22fb5aff7acd57463050ba8`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T050513Z-fleet02-B01-qform-auto11/REPORT.md`.  
   Its `QFORM-PHYSICAL-EDGE-QUARTER-RIESZ-v1` proves for an arbitrary ambient quadratic polynomial containing one literal physical edge `mu!=0`:

   `H_(1/4)(R) <= C_edge |mu|^(-1/4)`,
   `C_edge=3.179662567631707...`.

   The proof is a two-coordinate conditional Plancherel estimate and therefore respects the pointwise-decay correction.

5. **Exact square-fractional upgrade.**  
   `yspennstate/math-open-problems@9c7d5029a308cb0f4903065baab48638203c4206`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T230734Z-fleet01-B01-qform-auto11/REPORT.md`.  
   For `0<beta<1/2`, adding a source-disjoint literal square upgrades `H_beta` to `H_(beta+1/2)` with factor `|b|^(-1/2)J_beta`, where

   `J_beta=max{B(1/2,beta), B(1/2,1/2-beta)+B(1/2-beta,beta)}`.

All dependencies are used only in these stated scopes.

## 2. First essential implication: improve the diagonal-plus-star outer-pivot compiler to a clean constant 91

Suppose a literal ORIGINAL coordinate has nonzero pivot `a` and exact completion gives

`Q=a(X_0+h(Z))^2+R(Z)`,

with Schur matrix

`S=[[d,c^T],[c,D]]`, `D=diag(d_1,...,d_m)`,                    (2.1)

and suppose the FULL matrix satisfies

`s_3(A)>=1`.                                                     (2.2)

As in the previous B01 report,

`A=(1/a)[a;r][a;r]^T + diag(0,S)`,                              (2.3)

so the rank-one singular-value inequality gives

`s_2(S)>=s_3(A)>=1`.                                            (2.4)

### Theorem 2.1 — `QFORM-OUTER-PIVOT-DIAGONALSTAR-SCALEFREE-v2`

Under (2.1)-(2.2), for every admissible product law,

`boxed: ||p_Q||_infinity <=91 |a|^(-1/2).`                      (2.5)

This improves the preceding constant `194.518...` while keeping exactly the same hypotheses.

### Proof

Use the fixed diagonal threshold

`tau=1/20`.                                                      (2.6)

**Case A: a residual diagonal has magnitude at least `1/20`.**

Choose a residual ORIGINAL coordinate `k` with `|S_kk|>=1/20`. The full physical pair `{0,k}` has first LDL pivot `a` and second LDL pivot exactly `S_kk`. Premise 2 gives

`||p_Q||_infinity
 <=C_2 |a|^(-1/2)|S_kk|^(-2/5)
 <=C_2 20^(2/5)|a|^(-1/2)
 =90.3696642083... |a|^(-1/2)
 <91 |a|^(-1/2).`                                               (2.7)

**Case B: every residual diagonal has magnitude `<1/20`.**

Write

`S=B+E`,
`B=[[0,c^T],[c,0]]`,
`E=diag(d,d_1,...,d_m)`.                                        (2.8)

Put `C=||c||_2`, `c_*=max_i |c_i|`, and

`E_star=C^4-c_*^4`.                                             (2.9)

The pure star `B` has exactly two nonzero singular values, both equal to `C`. By (2.4), Weyl and `||E||<1/20`,

`C>19/20`.                                                       (2.10)

Split again at the fixed aggregate threshold

`eta=2^(-24)`.                                                   (2.11)

If `E_star>=eta`, premise 1 gives

`H_(1/2)(R)
 <=8 eta^(-1/8)
 =8*2^3
 =64`.                                                          (2.12)

The outer literal square peel therefore gives

`||p_Q||_infinity<=64 |a|^(-1/2)`.                              (2.13)

If instead `E_star<eta`, then by (2.10)

`c_*^4=C^4-E_star
 >(19/20)^4-2^(-24)
 >(9/10)^2`,                                                     (2.14)

hence

`c_*^2>9/10`.                                                    (2.15)

Take a leaf `j` attaining `c_*`. Its physical residual hub-leaf pair is

`Lambda=[[d,c_j],[c_j,d_j]]`.                                   (2.16)

Since `|d|,|d_j|<1/20`,

`|det Lambda|
 =|d d_j-c_j^2|
 >9/10-1/400
 =359/400`.                                                      (2.17)

Conditioning all other ORIGINAL residual coordinates turns their couplings into an affine term on this physical pair. That affine term lies in the physical pair plane, so the sharper in-range version of premise 3 yields

`H_(1/2)(R)
 <=16 sqrt(30) (400/359)^(1/4)
 =90.0372031028... .`                                           (2.18)

The outer square peel gives

`||p_Q||_infinity
 <90.038 |a|^(-1/2)
 <91 |a|^(-1/2).`                                               (2.19)

The cases are exhaustive, proving (2.5). QED.

### Why this is still an oscillatory-replacement theorem

The only frequency-space input in the difficult diffuse-star branch is the previous joint grouped-star estimate, which first aggregated two independent physical leaf groups to obtain a critical `|t|^-1` envelope and only then integrated against the half-Riesz weight. The proof never assigns a law-uniform pointwise Fresnel factor to a scalar arbitrary-density square.

## 3. Target-level closure: every exact physical arrowhead is uniformly paid

Call a symmetric matrix an ORIGINAL-coordinate arrowhead if, after a permutation of the original coordinates,

`A=[[d_0,c^T],[c,D]]`, `D=diag(d_1,...,d_m)`.                   (3.1)

No assumption is made on the signs or sizes of the coefficients.

### Theorem 3.1 — `QFORM-FULL-ARROWHEAD-UNIVERSAL-LINF-v1`

If an ORIGINAL-coordinate arrowhead `A` satisfies

`s_3(A)>=1`,                                                     (3.2)

then for every independent cap-one input law the quadratic form `Q=X^T A X` has an essentially bounded density and

`boxed: ||p_Q||_infinity <=91.`                                 (3.3)

Continuity is not claimed.

### Proof

Separate the leaf diagonal from the rank-two arrowhead skeleton:

`A=L+E`,

`L=[[d_0,c^T],[c,0]]`,
`E=diag(0,d_1,...,d_m)`.                                        (3.4)

Every leaf row of `L` is a multiple of the hub coordinate row, so

`rank L<=2`.                                                     (3.5)

The rank-two singular-value inequality therefore gives the exact structural estimate

`boxed: s_3(A)<=||E||_op=max_i |d_i|.`                          (3.6)

Under (3.2), choose a literal leaf `j` with

`|d_j|>=1`.                                                      (3.7)

This is an ORIGINAL physical scalar pivot `a=d_j`; the star skeleton has zero leaf diagonal, so there is no cancellation in (3.7). Complete this leaf exactly. Since leaf `j` couples only to the hub, the Schur complement on the remaining original coordinates is again a diagonal-plus-one-star matrix:

`S=[[d_0-c_j^2/d_j, c_{-j}^T],
    [c_{-j},D_{-j}]]`.                                          (3.8)

Theorem 2.1 applies to the full target matrix `A` with this pivot and gives

`||p_Q||_infinity
 <=91 |d_j|^(-1/2)
 <=91`.                                                         (3.9)

QED.

### Structural meaning

This removes the apparent tiny-outer-pivot debt completely on the exact arrowhead branch. A pure hub-plus-star skeleton can contribute at most two singular directions. Therefore the third target singular direction MUST already be carried by a literal leaf diagonal of target size, and completing that leaf preserves the diagonal-plus-star geometry exactly.

A strict target control is obtained from three leaves,

`d_0=0`, `D=I_3`, `c=(1,1,1)/sqrt(3)`.                          (3.10)

Its exact spectrum is

`{(1-sqrt(5))/2, 1, 1, (1+sqrt(5))/2}`,                         (3.11)

so exactly three eigenvalues have modulus at least one. The theorem gives `||p_Q||_infinity<=91` for every admissible product law.

## 4. Newest designated partner applied: two literal squares upgrade ANY generic physical edge to an endpoint density bound

The fleet02/B01 theorem in premise 4 is deliberately subcritical: a generic edge supplies `H_(1/4)`, while `H_(1/2)` can fail because of parabolic same-bank curvature. The exact square-fractional composition in premise 5 supplies the missing exponent if two literal scalar squares are available.

### Theorem 4.1 — `QFORM-TWOSQUARE-GENERICEDGE-LINF-v1`

Let `X_0,Z` be two distinct ORIGINAL coordinates. Suppose successive literal LDL completions give

`Q=a(X_0+h_0)^2+b(Z+h_1)^2+R`,                                 (4.1)

with `a,b!=0`; the shifts may depend arbitrarily on all later original coordinates. Suppose the residual quadratic polynomial `R` contains a literal physical edge

`2 mu YW`, `mu!=0`,                                             (4.2)

between two remaining ORIGINAL coordinates. Every other residual quadratic and affine coefficient is arbitrary.

Then

`boxed:
 ||p_Q||_infinity
 <= C_GE |a|^(-1/2)|b|^(-1/3)|mu|^(-1/6),`                    (4.3)

where

`C_GE=(J_(1/4) C_edge)^(2/3)
    =11.7458907464...`.                                         (4.4)

Only essential boundedness is asserted.

### Proof

The newest completed designated partner gives directly, in the full arbitrary residual environment,

`H_(1/4)(R)<=C_edge |mu|^(-1/4)`.                               (4.5)

Apply the exact square-fractional upgrade with `beta=1/4` to the literal inner square `b(Z+h_1)^2`. Since

`J_(1/4)=12.660413817789728...`,                                (4.6)

we obtain

`H_(3/4)(b(Z+h_1)^2+R)
 <=J_(1/4) C_edge |b|^(-1/2)|mu|^(-1/4)`.                      (4.7)

For every center, Lyapunov/Jensen gives

`H_(1/2)<=H_(3/4)^(2/3)`.                                      (4.8)

Thus

`H_(1/2)(b(Z+h_1)^2+R)
 <=C_GE |b|^(-1/3)|mu|^(-1/6)`.                                (4.9)

Finally apply the literal outer-square density kernel to `a(X_0+h_0)^2`; this gives (4.3). Every conditioning/completion is in ORIGINAL coordinates. QED.

This is an actual equation-level use of the newest fleet02/B01 result, not a comparison citation.

### Scale-cancelling target family

For `0<epsilon<=1`, take independent cap-one variables and

`Q_epsilon
 =epsilon X_0^2+epsilon Z^2
  +epsilon^(-5)(Y+W)^2
  -epsilon^(-5)V^2
  +T^2`.                                                        (4.10)

The coefficient spectrum is

`{epsilon, epsilon, 0, 2epsilon^(-5), -epsilon^(-5), 1}`,       (4.11)

so every member is in the owner target. The residual `(Y,W)` physical pair is parabolic, with nonzero diagonals and edge `mu=epsilon^(-5)`, so the partner's stronger zero-diagonal-edge theorem does not apply to that pair. Theorem 4.1 gives the exact scale cancellation

`||p_(Q_epsilon)||_infinity
 <=C_GE epsilon^(-1/2)epsilon^(-1/3)(epsilon^(-5))^(-1/6)
 =C_GE
 <11.746`,                                                      (4.12)

uniformly as `epsilon` tends to zero.

The purpose of this family is to verify the homogeneity of the compiler in a target-valid regime with two vanishing scalar pivots and a compensating large generic edge; it is not claimed extremal.

## 5. What is and is not closed

The exact full physical-arrowhead branch is now quantitatively closed with the universal constant 91. This is a genuine target-level implication, not merely a local subclass estimate after assuming a target-scale pivot: the target spectrum itself forces the required leaf pivot by the rank-two skeleton identity (3.6).

The generic-edge compiler also removes the critical-parabolic obstacle whenever two literal scalar pivots can be exposed before the edge. It keeps all signs and arbitrary residual curvature.

The unrestricted conjecture is still OPEN. The first unpaid B01 implication is now

`QFORM-FINITELEAK-NONARROWHEAD-TINY-PIVOT-AGGREGATION-v1`:

> In a general finite-leak / diagonal-plus-low-rank survivor, where the full matrix is not an exact physical arrowhead, use `s_3(A)>=1` to force either (i) an exact arrowhead/diagonal-star branch covered by Theorem 3.1, (ii) two literal scalar pivots followed by any nonzero physical edge covered by Theorem 4.1, or (iii) a target-scale aggregate two-bank / grouped-star / physical-pair currency before any vanishing scalar pivot is inverted. The genuinely nonzero low-rank collar must be retained; it cannot be discarded under rough laws.

Continuity for the full target and for the new square-kernel compilers remains unproved.

## 6. Deterministic checks and review status

The accompanying `CHECKS.txt` records:

- `C_2 20^(2/5)=90.3696642083129<91`;
- diffuse-star threshold `8(2^-24)^(-1/8)=64`;
- concentrated-pair bound `16 sqrt(30)(400/359)^(1/4)=90.03720310276094<91`;
- `(19/20)^4-2^-24-(9/10)^2=0.004506190395...>0`;
- `J_(1/4)=12.660413817789728...` and `C_GE=11.745890746379832...`;
- the arrowhead stress spectrum in (3.11).

These are deterministic arithmetic diagnostics only, not independent proof reviews. The new theorems remain pending independent mathematical review. Full QFORM remains OPEN.
