SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T19:01:08Z.
attacking: convert the total third compound energy forced by s_3(A)>=1 into a target-scale physical cross cut whenever the row/column triples are disjoint, and spend that cut by an integrated-Fourier theorem; isolate the exact overlap strata that remain.

# account03/B02 r37 — disjoint third-compound energy gives a universal L1 Fourier exit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`, continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Run: `20260923T190108Z-account03-B02-qform-r37`  
Status: **NEW GLOBAL SUPPORTING THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full owner target is unchanged: arbitrary dimension, independent original-coordinate real variables with one-dimensional densities bounded by one, and arbitrary real symmetric A with at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concave, diagonal-basis or post-rotation independence assumption is used.

This run changed mechanism from the r36 grouped-Pluecker local receiver to a global compound-energy partition. The r36 aggregate identity remains valid, but no dimension-free grouped kernel-curvature Fourier inequality has yet been proved from it. The new route starts instead from the exact third Cauchy-Binet energy of A itself and pays the entire disjoint row/column stratum at target scale.

## 1. Source-valid inputs

### 1.1 Marginal-free physical three-volume Fourier theorem

I use the completed account02/B03 theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`,

canonical source

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`.

For any disjoint original-coordinate sets L,R and physical cross block M=A[L,R], put

`Z3=e_3(MM^T)=sum_{|I|=|J|=3, I subset L, J subset R} det(M[I,J])^2`.

If Z3>0, the source proves

`||p_Q||_infinity <= C3 Z3^(-1/6)`,

where

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.

Every source branch is a d=3 Fourier branch. Retracing the three explicit envelopes in that proof gives the single safe envelope

`|phi_Q(t)| <= min{1, K3 Z3^(-1/4)|t|^(-3/2)}`,                 (1.1)

with

`K3=4*pi^(3/2)*e^(1/2)=36.72248324244589... .`                  (1.2)

Here is the branch check, so (1.1) is not inferred from the density conclusion alone.

* Spread 3-volume branch: the pinned theorem used there has coefficient `(2*pi)^(3/2)e^(3/4)<K3`.
* First heavy-row promotion: its `(k,ell)=(1,2)` envelope coefficient is `2^(7/4) pi^(3/2)e^(1/2) alpha^(-1/4)`; `alpha>1/2` makes this strictly less than `K3`.
* A second promotion gives a `(2,1)` envelope with coefficient at most `2^(7/4)pi^(3/2)<K3` after both heavy-volume factors are inserted.
* The terminal exact-rank-three crossing has coefficient at most `2^(3/2)pi^(3/2)<K3` after its `P3^2>Z3/8` lower bound.

Thus (1.1) is a genuine whole-law pointwise envelope produced by the completed multi-coordinate Fourier proof. It does not use the refuted one-dimensional law-uniform quadratic van-der-Corput claim.

Integrating (1.1) reproduces the source density constant and gives the explicit L1 statement

`integral_R |phi_Q(t)| dt <= 2*pi*C3 Z3^(-1/6)`.                 (1.3)

### 1.2 Designated partner account04/B02

The designated completed partner is account04/B02

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

canonical source

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

On its exact overlap, a nonsingular physical principal 3x3 block H0 with a zero diagonal entry gives

`integral_R |phi_Q(t)|^2 dt <= L0 |det H0|^(-1/3)`,              (1.4)

where

`L0=6*pi*2^(2/3)=29.92180489898403... .`

I apply (1.4) at a new hybrid inequality in Section 4.

## 2. New global compound-energy decomposition

For a real symmetric n x n matrix A define, for r=0,1,2,3,

`V_r(A) = sum det(A[I,J])^2`,                                    (2.1)

where the sum is over all 3-subsets I,J of [n] satisfying `|I intersect J|=r`.

By Cauchy-Binet,

`sum_{r=0}^3 V_r(A)
 = sum_{|I|=|J|=3} det(A[I,J])^2
 = e_3(A^2).`                                                     (2.2)

If the singular values of A are `s_1>=s_2>=...`, then

`e_3(A^2)=sum_{i<j<k} s_i^2 s_j^2 s_k^2`.                        (2.3)

Therefore the exact owner hypothesis `s_3(A)>=1` implies

`boxed: sum_{r=0}^3 V_r(A) >=1.`                                 (2.4)

In particular at least one intersection stratum has

`V_r(A)>=1/4`.                                                    (2.5)

This four-way split is deterministic and contains no selection of an individual tiny minor.

## 3. Main theorem — the disjoint stratum is completely paid by integrated Fourier

### Theorem `QFORM-DISJOINT-COMPOUND-E3-L1-v1`

Let A be any real symmetric matrix and let

`D3:=V_0(A)
 = sum_{|I|=|J|=3, I intersect J=empty} det(A[I,J])^2`.           (3.1)

For every admissible independent cap-one product input, if `D3>0`, then the full ambient quadratic form Q=X^TAX satisfies

`boxed:
 ||p_Q||_infinity
 <= 2*C3*D3^(-1/6)
 =21.10033766232955... D3^(-1/6),`                                (3.2)

and

`boxed:
 integral_R |phi_Q(t)|dt
 <=4*pi*C3*D3^(-1/6)
 =132.5773315764771... D3^(-1/6).`                                (3.3)

Consequently this branch has a continuous density vanishing at infinity.

More explicitly the characteristic function obeys

`boxed:
 |phi_Q(t)|
 <= min{1, K_D D3^(-1/4)|t|^(-3/2)},`                            (3.4)

with

`K_D = 2^(3/2) K3
    = 103.86686769097139... .`                                   (3.5)

#### Proof

Choose a random physical cut `[n]=L disjoint-union R` by putting each original coordinate independently into L or R with probability 1/2. For a fixed cut put

`Z3(L,R)=e_3(A[L,R]A[L,R]^T)`.

Cauchy-Binet gives

`Z3(L,R)
 = sum_{I subset L, J subset R, |I|=|J|=3} det(A[I,J])^2`.        (3.6)

A term can occur only when I and J are disjoint. For each fixed disjoint ordered pair `(I,J)`, the probability that all three elements of I land in L and all three elements of J land in R is exactly `2^(-6)=1/64`. Therefore

`E_cut Z3(L,R)=D3/64`.                                           (3.7)

Hence at least one actual original-coordinate cut satisfies

`boxed: Z3(L,R)>=D3/64.`                                         (3.8)

Apply the source theorem (1.1)-(1.3) to this cut. Since

`(D3/64)^(-1/6)=2 D3^(-1/6)`

and

`(D3/64)^(-1/4)=2^(3/2)D3^(-1/4)`,

we obtain (3.2)-(3.5). QED.

### Universal target-scale corollary

If the disjoint stratum carries merely one quarter of the unit compound energy,

`D3>=1/4`,                                                        (3.9)

then

`boxed: ||p_Q||_infinity <=26.58475958065858...`,                 (3.10)

`boxed: integral |phi_Q| <=167.03697079209573... .`               (3.11)

Thus a full-target counterexample, if one exists, cannot have target-scale disjoint third-minor energy. Under the owner hypothesis, if (3.9) fails then (2.4) forces

`V_1+V_2+V_3>3/4`,                                                (3.12)

and hence at least one of

`V_1>1/4`, `V_2>1/4`, `V_3>1/4`                                  (3.13)

must hold. This is a concrete three-stratum remainder rather than a vague 'low cross-volume' state.

The overlap classes have direct structural interpretations which should guide the next payment:

* `V_1`: one shared physical coordinate — one-anchor plus residual 2x2-cross geometry;
* `V_2`: two shared physical coordinates — double-anchor plus residual one-crossing geometry;
* `V_3`: principal 3x3 compound energy.

No claim is made here that any one individual minor in these sums has universal scale.

## 4. Designated account04/B02 result applied at a new inequality

Assume in addition to `D3>0` that the partner's zero-diagonal physical triple H0 exists. Combine the partner L2 credit (1.4) with the disjoint-stratum tail (3.4).

For every T>0,

`integral |phi_Q|
 <= integral_{|t|<=T}|phi_Q| + integral_{|t|>T}|phi_Q|`

` <= sqrt(2T L0)|det H0|^(-1/6)
    +4 K_D D3^(-1/4) T^(-1/2).`                                  (4.1)

Optimizing the two terms gives

`integral |phi_Q|
 <=4 K_D^(1/2)(2L0)^(1/4)
      |det H0|^(-1/12) D3^(-1/8).`                               (4.2)

Fourier inversion therefore yields the genuinely new partner hybrid

`boxed:
 ||p_Q||_infinity
 <= C_hyb |det H0|^(-1/12) D3^(-1/8),`                           (4.3)

where

`C_hyb
 = (2/pi) K_D^(1/2)(2L0)^(1/4)
 = 2^(41/12) 3^(1/4)e^(1/4)
 =18.04567310883567... .`                                        (4.4)

At target-scale `D3>=1/4`,

`||p_Q||_infinity
 <=21.46004285604066...
   |det H0|^(-1/12).`                                             (4.5)

This is an equation-level application of the designated account04/B02 result, not a status citation. The disjoint-stratum theorem already gives continuity on the overlap because its characteristic function is in L1.

## 5. Exact-rank-three diffuse-frame corollary

The same mechanism gives a useful quantitative statement for exact-rank-three matrices and independently cross-checks the global decomposition.

Write

`A=U Lambda U^T`,                                                 (5.1)

where U has three orthonormal columns and Lambda is invertible symmetric 3x3. Put

`ell_* = max_i ||U_i||_2^2`.                                      (5.2)

For each physical triple I define

`p_I=det(U_I)^2`.

Cauchy-Binet gives `sum_I p_I=1`; this is the rank-three projection-determinantal base law, and its one-coordinate inclusion probabilities are

`sum_{I containing i} p_I = ||U_i||^2`.                           (5.3)

Let I,J be independent triples with law p. Conditional on I, the union bound gives

`P(J intersects I | I)
 <= sum_{i in I} P(i in J)
 <=3 ell_*`.                                                       (5.4)

Hence

`P(I intersects J = empty) >=1-3 ell_*`.                          (5.5)

Moreover

`det A[I,J]=det(Lambda) det(U_I)det(U_J)`,                         (5.6)

so

`D3
 = det(Lambda)^2 P(I intersects J=empty)
 >= det(Lambda)^2(1-3ell_*)`                                      (5.7)

whenever `ell_*<1/3`.

Combining (5.7) with (3.2)-(3.3) proves

`||p_Q||_infinity
 <=2C3 |det Lambda|^(-1/3)(1-3ell_*)^(-1/6),`                     (5.8)

`integral |phi_Q|
 <=4pi C3 |det Lambda|^(-1/3)(1-3ell_*)^(-1/6).`                  (5.9)

Under the exact rank-three owner scale `min_j |lambda_j|>=1` and the concrete diffuse threshold `ell_*<=1/6`,

`boxed: ||p_Q||_infinity <=23.68432823247784...`,                  (5.10)

`boxed: integral |phi_Q| <=148.8130231607234... .`                (5.11)

Thus the difficult exact-rank-three no-cross-three geometry is necessarily a heavy-physical-leverage regime; the diffuse spectral frame is fully paid by integrated Fourier without selecting a fixed triple.

## 6. Computational regression

A seeded symbolic/numerical checker was run on random exact-rank-three matrices with 7 physical coordinates. For each matrix it:

1. verified the basis-law identity (5.3);
2. computed the exact disjoint-basis probability and checked (5.5);
3. exhaustively averaged `Z3(L,R)` over all `2^7` physical cuts and compared it with `det(Lambda)^2 P(disjoint)/64`.

Across 30 dense trials the maximum relative identity error was

`1.49e-15`,

and the minimum numerical slack in (5.5) was positive (`0.74245...` in this deliberately diffuse random sample). The checker is corroborative only; the proof of (3.7) and (5.3)-(5.7) is exact Cauchy-Binet plus a union bound.

## 7. What is and is not solved

Proved in this run:

* a global integrated-Fourier theorem in terms of the disjoint third-compound energy `D3=V_0(A)`;
* a target-scale universal bound whenever `V_0>=1/4`;
* an exact four-stratum compound-energy decomposition with only `V_1,V_2,V_3` remaining after the new exit;
* a quantitative exact-rank-three diffuse-frame L1 theorem;
* the new account04/B02 L2/L1 hybrid (4.3).

Not proved:

* a universal payment of the overlap strata `V_1,V_2,V_3`;
* the full arbitrary-spectrum conjecture;
* full-target continuity;
* a valid counterexample to the target-wide unweighted L1 Fourier criterion.

The target-wide universal `integral |phi_Q|` statement therefore remains **OPEN / not refuted**. The present theorem shows it is true with an explicit constant on the entire target-scale disjoint-compound branch.

## 8. Next B02 implication

Next mechanism:

`QFORM-COMPOUND-OVERLAP-V1-V2-L1-v1`.

Start from the guaranteed target-scale alternative (3.13). For `V_1`, aggregate one-anchor / residual-two-crossing packets before any reciprocal local-minor selection. For `V_2`, aggregate double-anchor / one-crossing Schur packets. Use the canonical promotion theorem when the determinant-volume law develops a heavy physical anchor. Keep `V_3` (principal-triple compound energy) separate unless a source-valid principal-compound receiver is available.

All row/column sets above are original physical coordinates. No Monte Carlo density estimate is used as proof, no arbitrary-joint coarea estimate is invoked, and no nonzero quadratic term is deleted as a small random perturbation.
