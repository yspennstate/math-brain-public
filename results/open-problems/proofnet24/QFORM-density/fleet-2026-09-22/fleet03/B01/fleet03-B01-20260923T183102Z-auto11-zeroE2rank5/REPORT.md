SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T18:31:02Z.
attacking: classify the exact projected-E2-degenerate near-null leakage endpoint; either a two-row physical split gives an averaged-frequency payment, or all residual nonseparable curvature is diagonal plus rank at most five.

# fleet03/B01 — zero projected E2 forces diagonal + rank-5 residual curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260923T183102Z-auto11-zeroE2rank5`  
Assignment: oscillatory replacement / quantitative inequalities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING ROUTING THEOREM / FULL QFORM OPEN**.

The target remains the unrestricted product-law problem: independent original real coordinates with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or independence-after-rotation assumption is introduced.

## 1. Sources actually used

Fresh control was read from `yspennstate/math-research-brain` on main under owner control revision `2026-09-22.15`; the current owner continuation remains `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the full theorem remains open.

The analytic positive-volume receiver is the completed arbitrary-rank projected-crossing theorem

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

together with the fleet03/B01 heavy-row promotion theorem

`yspennstate/math-open-problems@3e8c96175a9cb97e80365fc127ffd1c9b733588c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

The designated partner input is fleet04/B01

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T131003Z-fleet04-B01-singular-star-routing-r2/REPORT.md`.

I use its exact scalar-completion identity and valid leakage inequality

`L(ell)=sum_(k!=l) ell_k^2 ell_l^2 >= W2(S)/(4a^2)`                 (1.1)

in the leakage branch. I do **not** use that report's printed stronger individual-bank conclusion; the source-valid correction from the preceding B01 run is preserved.

I also use fleet04/B01's exact signed-Fejer equivalence

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`,

namely

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                         (1.2)

whenever the density is bounded.

Finally, the dependence-safe outer-square compiler from fleet03/B01 says: if `X` has density at most one, `X` is independent of `V`, `R(V)` has density bounded by `M0`, and `h(V)` is arbitrary measurable, then

`Q=a(X+h(V))^2+R(V)`

has an essentially bounded density with

`||p_Q||_infinity <= 2 sqrt(2) |a|^(-1/2) M0^(1/2)`.                (1.3)

No independence between `h(V)` and `R(V)` is needed.

## 2. The pointwise obstruction is preserved

Fix any frequency `s>0` and `eta>0`. The set

`E={x: dist(s x^2,2 pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite measurable subset of total measure one and let its indicator be the density of `X`. Then

`Re E exp(i s X^2) >= cos(eta)`.

Thus no positive law-uniform pointwise power decay for a scalar quadratic phase can hold. Nothing below uses such a bound. The payment branch is a signed-Fejer / density estimate; the zero-volume branch is algebraic.

## 3. Scalar-completed near-null residual and a global projected-E2 parameter

Use the partner scalar-completion notation for a physical pair `S={x,y}` with `a=A_xx!=0`:

`delta=A_yy-A_xy^2/a`,
`ell_k=A_yk-(A_xy/a)A_xk`,
`M_kl=A_kl-a^(-1)A_xk A_xl`,                                      (3.1)

where `k,l` range over the remaining original-coordinate set `K`.

After completing only the original coordinate `x`, the full form is exactly

`Q=a(X_x+h(Y,Z))^2+R(Y,Z)`,                                        (3.2)

with

`R(Y,Z)=delta Y^2+2Y(ell dot Z+beta)+Z^T M Z+affine terms`.         (3.3)

For each unordered pair `P={i,k}` in `K`, put

`J_P=K\P`.

If `ell_(J_P)=0`, define `gamma_P=0`. Otherwise let `P_ell` be the orthogonal projection in `R^(J_P)` onto `span(ell_(J_P))` and define

`C_P=M[P,J_P](I-P_ell)`,                                           (3.4)

`Z_P=e_2(C_P C_P^T)=det(C_P C_P^T)>=0`,                            (3.5)

(the last equality holds because `C_P` has two rows), and

`gamma_P=||ell_(J_P)||_2^2 Z_P`.                                   (3.6)

Set

`Gamma_2(ell,M)=max_P gamma_P`.                                    (3.7)

This parameter uses only literal original-coordinate splits. No random coordinate is rotated.

## 4. Positive projected two-volume is already an averaged-frequency payment

Let

`C_E2=3*2^(7/6)*exp(1/3)=9.39913188784886...`.                      (4.1)

The preceding B01 heavy-row-promotion theorem removes every row-marginal gate from the `k=1, ell=2` projected-crossing estimate. Therefore if `Gamma_2>0`, choose `P` attaining the maximum. The residual `R` in (3.3) has a continuous `C_0` density and

`||p_R||_infinity <= C_E2 Gamma_2^(-1/6)`.                         (4.2)

Applying the dependence-safe outer-square compiler (1.3) gives the full form an essentially bounded density satisfying

`boxed:
||p_Q||_infinity
 <= K_E2 |a|^(-1/2) Gamma_2^(-1/12),`                              (4.3)

where

`K_E2=2 sqrt(2 C_E2)=8.67139291595018...`.                         (4.4)

By fleet04/B01's signed-Fejer equivalence, the same number is the uniform signed-Fejer bound:

`boxed:
sup_(T>0,y) D_T law(Q)(y)
 <=8.671393 |a|^(-1/2) Gamma_2^(-1/12).`                           (4.5)

This is a genuine averaged-frequency replacement for the false pointwise Fresnel estimate.

The scaling is exact: under `A -> lambda A`, one has `a->lambda a`, `ell->lambda ell`, `M->lambda M`, hence `Gamma_2->|lambda|^6 Gamma_2`; the right side of (4.3) scales as `|lambda|^-1`.

## 5. New algebraic lemma: disjoint 2x2 minors imply diagonal + rank at most three

### Lemma 5.1 — `QFORM-DISJOINT2-DIAGRANK3-v1`

Let `N` be any real `m x m` matrix, not necessarily symmetric. Suppose

`det N[{r,s},{c,d}]=0`                                             (5.1)

whenever `r,s,c,d` are four distinct indices. Then there is a diagonal matrix `D` such that

`rank(N-D)<=3`.                                                     (5.2)

#### Proof

For `m<=3`, take `D=0`. If every off-diagonal entry of `N` vanishes, take `D=N`.

Otherwise choose `a!=b` with `N_ab!=0`. Define vectors `r,c` by

`r_a=N_ab`, `r_b=0`, `r_i=N_ib` for `i notin {a,b}`,                (5.3)

`c_b=1`, `c_a=0`, `c_j=N_aj/N_ab` for `j notin {a,b}`.             (5.4)

For distinct `i,j notin {a,b}`, apply (5.1) to rows `{a,i}` and columns `{b,j}`. Since these four indices are distinct,

`N_ab N_ij-N_aj N_ib=0`,                                          (5.5)

hence

`N_ij=r_i c_j`.                                                     (5.6)

By construction the same rank-one matrix `r c^T` also matches every off-diagonal entry in row `a`, every off-diagonal entry in column `b`, and the pivot `(a,b)`.

Thus `H=N-r c^T` has off-diagonal support only in row `b` or column `a`. Let `D=diag(H)` and `S=H-D`. Then

`S=e_b s^T+t e_a^T`                                                (5.7)

for suitable vectors `s,t` (take `t_b=0` to avoid double counting `(b,a)`). Therefore `rank S<=2`, and

`rank(N-D)<=rank(r c^T)+rank S<=1+2=3`.                            (5.8)

QED.

## 6. Main new theorem: exact projected-E2 degeneracy forces diagonal + rank five

### Theorem 6.1 — `QFORM-PROJECTED-E2-ZERO-DIAGRANK5-v1`

Let `M` be a real symmetric matrix indexed by `K`, and let `ell in R^K` be nonzero. Suppose

`Gamma_2(ell,M)=0`.                                                 (6.1)

Then there exists a diagonal matrix `D` such that

`boxed: M=D+L,  rank L<=5.`                                        (6.2)

Consequently the scalar-completed residual coefficient matrix on `(Y,Z)`,

`A_res=[[delta,ell^T],[ell,M]]`,                                   (6.3)

has the form

`boxed: A_res=diagonal + R_7,  rank R_7<=7.`                        (6.4)

#### Proof

If `|K|<=4`, take `D=0`; then `rank M<=4<=5`. Assume `|K|>=5`.

Choose one anchor `j0 in K` with `ell_j0!=0`. For distinct `i,k in K\{j0}`, let

`J=K\{i,k}`.

Then `j0 in J`, hence `ell_J!=0`. Since `Gamma_2=0`, equations (3.5)-(3.7) imply

`rank[M[{i,k},J](I-P_(ell_J))] <=1`.                               (6.5)

Define

`u_r=M_(r,j0)/ell_j0`,                                              (6.6)

and the generally nonsymmetric matrix

`N=M-u ell^T`.                                                      (6.7)

Its entire `j0`-th column vanishes:

`N_(r,j0)=0`.                                                       (6.8)

Moreover, subtracting `u_I ell_J^T` does not change the projected crossing because

`ell_J^T(I-P_(ell_J))=0`.                                          (6.9)

Hence (6.5) is equivalently

`rank[N[{i,k},J](I-P_(ell_J))] <=1`.                               (6.10)

Take four distinct indices `i,k,j,l` in `K\{j0}`. In (6.10), the two row vectors of `N[{i,k},J]` have collinear images in the quotient `R^J/span(ell_J)`. Therefore the three vectors

`N_i|J, N_k|J, ell_J`                                              (6.11)

span dimension at most two. Their `3x3` determinant on columns `{j0,j,l}` is zero. Using (6.8), that determinant is

`ell_j0 [N_ij N_kl-N_il N_kj]=0`.                                 (6.12)

Since `ell_j0!=0`, every disjoint `2x2` minor of the principal matrix

`N_OO`, `O=K\{j0}`,                                                (6.13)

vanishes. Lemma 5.1 therefore supplies a diagonal `D_O` and a matrix `R_O` with

`N_OO=D_O+R_O`, `rank R_O<=3`.                                    (6.14)

Extend the diagonal by setting

`D_j0j0=M_j0j0`.                                                    (6.15)

The difference `M-D` is the sum of the zero-extended matrix `R_O` and a matrix `T` with block form (ordering `j0,O`)

`T=[[0, ell_j0 u_O^T],
    [ell_j0 u_O, u_O ell_O^T]]`.                                   (6.16)

Although `T` need not be symmetric by itself, its columns lie in the two-dimensional span of

`v=(0,u_O)^T`, `w=(ell_j0,0_O)^T`:                                 (6.17)

column `j0` is `ell_j0 v`, while for `j in O`,

`column_j(T)=ell_j v+u_j w`.                                       (6.18)

Hence `rank T<=2`. Therefore

`rank(M-D)<=rank R_O+rank T<=3+2=5`,                               (6.19)

proving (6.2). Since `M-D` is symmetric, the resulting low-rank remainder is automatically symmetric even though the intermediate decomposition was not.

Finally,

`A_res=diag(delta,D)+[[0,ell^T],[ell,M-D]]`.                        (6.20)

The first off-diagonal star matrix has rank at most two and `M-D` has rank at most five, so the second term in (6.20) has rank at most seven. This proves (6.4). QED.

## 7. Partner theorem applied to the actual near-null leakage branch

The fleet04/B01 partner theorem gives, in its leakage branch,

`L(ell)=sum_(k!=l)ell_k^2 ell_l^2 >=W2(S)/(4a^2)`.                 (7.1)

In particular, whenever `W2(S)>0`,

`||ell||_2^4 >= L(ell) >=W2(S)/(4a^2)`,                            (7.2)

so

`||ell||_2 >= W2(S)^(1/4)/(sqrt(2)|a|^(1/2))>0`.                  (7.3)

Therefore Theorem 6.1 applies to the exact zero-volume endpoint of the partner's leakage branch. We obtain the following exhaustive routing statement:

### Corollary 7.1 — `QFORM-NEARNULL-LEAKAGE-E2-OR-DIAGRANK5-v1`

Assume the partner leakage branch (7.1) with `W2(S)>0`.

* If `Gamma_2(ell,M)>0`, then the full law has a bounded density and satisfies the signed-Fejer estimate (4.5).
* If `Gamma_2(ell,M)=0`, then the scalar-Schur residual curvature obeys

  `M=diagonal + rank<=5`,                                          (7.4)

  and the full `(Y,Z)` residual quadratic matrix is

  `diagonal + rank<=7`.                                            (7.5)

Thus the **exact** projected-E2-degenerate endpoint is no longer an arbitrary dense-curvature problem. All its nonseparable curvature lives in a fixed-rank carrier.

This is an actual use of the designated partner result at (7.1)-(7.3), not a source citation without application.

## 8. Deterministic checks

A seeded `n=9` stress family

`M=D+u ell^T+ell u^T`                                              (8.1)

was generated with dense random `D,u,ell`. For every two-row split `P`,

`M[P,J](I-P_(ell_J))`

has rank at most one analytically, because the `u_P ell_J^T` term is killed and the survivor is the rank-one matrix `ell_P u_J^T(I-P_(ell_J))`.

The finite numerical check gives

`max_P det(C_P C_P^T)=3.67e-14`,
`max_P second_singular_value(C_P)=1.48e-15`,
`rank(M-D)=2`                                                       (8.2)

at tolerance `1e-10`, consistent with Theorem 6.1.

Constant check:

`C_E2=9.39913188784886`,
`K_E2=8.67139291595018`.                                           (8.3)

Scaling check: `Gamma_2(lambda ell,lambda M)=|lambda|^6 Gamma_2(ell,M)`, so (4.3) is homogeneous of degree `-1` in the quadratic matrix.

These are diagnostics; the proof is the exact algebra in Sections 5-7.

## 9. What is and is not closed

This run removes the **exact** projected-E2-zero endpoint from the class of arbitrary dense Schur curvatures. The first unpaid implication is now

`QFORM-NEARNULL-SMALL-POSITIVE-GAMMA2-OR-DIAGRANK7-RECEIVER-v1`:

obtain a universal payment as `Gamma_2 ->0+`, or build a rough-law receiver for the diagonal-plus-rank-at-most-seven residual that is stable under this degeneration. A small operator-norm quadratic error may not be discarded because the input laws have no moment bound. No uniformly good single physical minor is assumed.

The positive-`Gamma_2` branch proves essential boundedness of the full `Q`; continuity of the residual `R` is `C_0`, but continuity of the full law after the correlated outer completed square is **not proved** by this argument. The exact `Gamma_2=0` branch is structural only; no density claim is made there. The unrestricted QFORM theorem and its global continuity conclusion remain open.

No source-matching published theorem was identified in the bounded literature check performed during this run; this statement is not a novelty claim.
