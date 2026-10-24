SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T21:03:58.325290Z.
attacking: robustify the rank-two Schur-DPP receiver against the retained Frobenius twist from the finite-hub normal form, without deleting the rough-law residual.

# account02/B13 r35 — robust Schur pair-volume, finite-center failure, and D5 transverse-bank obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws / complementary constructions. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED ROBUST SCHUR-DPP DICHOTOMY + NEW DIFFUSE RANK-ONE ROUGH NORMAL FORM + NEW PINNED-D5 TRANSVERSE-BANK OBSTRUCTION / FULL QFORM OPEN / CONTINUITY OPEN**.

The first unpaid implication after this run is

`QFORM-ONE-OR-TWO-TRANSVERSE-MODE-ROUGH-GLUE-v1`.

The retained Frobenius twist can now be absorbed whenever the normalized scalar-Schur rank-two carrier has a transverse singular value above its explicit twist scale. If that payment fails, the designated partner's pair-law stability forces either one physical coloop or three physical carrier coordinates; in the diffuse chamber it yields a diagonal + symmetric-rank-one + retained Frobenius remainder. Separately, the pinned unconditional D5 theorem proves that any shared-input transverse bank of dimension at least three is paid at a quantitative fifth-volume inequality. The remaining rough endpoint is therefore a one- or two-transverse-mode / near-null-pivot glue problem, not an arbitrary diffuse tail.

No moment, support, log-concavity, single-interval, bounded-diameter, fixed-fragment-count, diagonal-basis, post-rotation-independence, or coefficient-small-implies-random-small step is used.

## 1. Fresh sources and exact scope

Fresh owner control remained QFORM-only under OWNER CONTROL revision `2026-09-22.15`; the unrestricted conjecture remains OPEN and continuity remains separate. The latest completed designated partner is account03/B13 r34:

`math-open-problems@7ebaff80e4d6d1c5c45a561d1ff17a87cfd7a052`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T203053Z-account03-B13-qform-r34/REPORT.md`

with its zero-pivot clarification `ADDENDUM.md` at the same commit. Its quantitative pair-law theorem says that for a rank-two Parseval frame `W`, with pair law

`q_H=det(W_H)^2`, `sum_H q_H=1`,

and disjointness

`delta=P(H cap K=empty)`

for independent q-pairs, one has either a near physical coloop

`s_2(W_{-h}) <= sqrt(2) delta^(1/6)`,

or a three-coordinate concentration

`||W_{T^c}||_op <= 2 delta^(1/6)`.

If every row leverage is at most `q0<=2/3`, the same report proves

`delta >= (2-3q0)^3/64`; in particular max leverage `<=1/2` gives `delta>=1/512`.

The unconditional pair-volume half-Riesz theorem used below is the completed account01/B01 result

`math-open-problems@55255bcb25271145aa9f5a1a93a0cc84ad8e1c3d`:

for any full quadratic polynomial on independent cap-one ORIGINAL coordinates and any disjoint physical cross block `M` with

`Z_2=e_2(M^T M)>0`,

`H_{1/2}:=sup_s E|Q-s|^(-1/2) <= C_E2 Z_2^(-1/8)`,

where

`C_E2 <= 12*2^(5/6)*e^(5/24)=26.3340461807597...`.

No leverage gate is needed and arbitrary same-side curvature/outside couplings/affine terms are retained.

The required pinned source is

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. The completed result applied in Section 5 is D5:

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`

for every disjoint physical cross block `M=A[I,J]`, with no volume-marginal condition. The counterexample search reports no valid counterexample in the tested families; no numerical search is used as proof here.

Finally, the optimizer-free account04/B13 reduction retained by r34 gives equality of suprema between arbitrary cap-one product laws and unit-measure product indicators, followed by approximation by bounded finite unions with arbitrary small loss. It asserts neither attainment nor a uniform diameter/fragment count.

## 2. Exact Schur decomposition with the retained twist

Work on an original physical coordinate bank with

`A = D + U Lambda U^T + E`,                                      (2.1)

where

`U^T U=I_2`, `Lambda=Lambda^T` is invertible, `D` is diagonal,

and `E=E^T` has zero diagonal. Put

`epsilon=||E||_F`.

Fix an ORIGINAL coordinate `z`. Let its row of U be `u^T` and write

`c=||u||^2`, `d=D_zz`, `a=A_zz=d+u^T Lambda u`,

`r=U_- Lambda u`, `e=E[-z,z]`.                                  (2.2)

Assume

`a d !=0`, `c<1`.                                                  (2.3)

The genuine scalar Schur remainder is

`S=A[-z,-z]-a^(-1)A[-z,z]A[z,-z]=S_0+F`,                         (2.4)

with

`S_0=D_-+U_-[Lambda-a^(-1)Lambda u u^T Lambda]U_-^T`,            (2.5)

`F=E[-z,-z]-a^(-1)(r e^T+e r^T+e e^T)`.                          (2.6)

Hence

`||F||_F <= epsilon_z`,                                           (2.7)

where

`epsilon_z := epsilon(1+2||r||/|a|)+epsilon^2/|a|`.               (2.8)

This quantity is intentionally allowed to blow up near a null pivot. No assertion is made that a coefficient-small E produces a small random quadratic term.

Set

`G=U_-^T U_-=I_2-u u^T`,

`W=U_- G^(-1/2)`,

`N=G^(1/2)[Lambda-a^(-1)Lambda u u^T Lambda]G^(1/2)`.             (2.9)

Then

`W^T W=I_2`,

`S_0=D_-+W N W^T`,                                                (2.10)

and the determinant transport is exact:

`det N=(1-c)d det(Lambda)/a`.                                     (2.11)

Let

`q_H=det(W_H)^2`, `|H|=2`,                                       (2.12)

and let

`delta=P_q(H cap K=empty)`                                       (2.13)

for two independent q-pairs. By Cauchy-Binet q is a probability law.

## 3. Robust exterior payment of the actual Schur cross block

### Theorem 3.1 — `QFORM-ROBUST-SCHUR-DPP-FROB-TWIST-v1`

Under (2.1)-(2.13), at least one of the following holds.

**Paid branch.**

`boxed: s_2(N) >= 24 epsilon_z/sqrt(delta)`                        (3.1)

and the full original quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <= C_R delta^(-1/8)
    [(1-c)|a d det Lambda|]^(-1/4),
 C_R=2^(3/4) C_E2
    <=44.2884100650533.
}`                                                                  (3.2)

**Structural branch.**

`boxed: s_2(N) < 24 epsilon_z/sqrt(delta),}`                       (3.3)

and the designated partner's r34 stability theorem gives either a physical coordinate h with

`boxed:
 s_2(W_{-h})
 < sqrt(2)(24 epsilon_z/s_2(N))^(1/3),
}`                                                                  (3.4)

or a physical three-set T with

`boxed:
 ||W_{T^c}||_op
 < 2(24 epsilon_z/s_2(N))^(1/3).
}`                                                                  (3.5)

Thus failure of robust pair-volume payment is itself a quantitative finite-center statement about the exact normalized carrier.

### Proof

Color the rows of W independently red/blue and write `I,J` for the two physical banks. The cross block of the exact rank-two Schur carrier is

`B_0=W_I N W_J^T`.                                                (3.6)

For two physical pairs H,K,

`det B_0[H,K]=det(W_H) det(N) det(W_K)`.                           (3.7)

A fixed ordered disjoint pair `(H,K)` lands with `H subset I`, `K subset J` with probability `1/16`. Therefore

`E e_2(B_0^T B_0)=det(N)^2 delta/16`.                             (3.8)

Some physical cut satisfies

`||wedge^2 B_0||_HS
 =e_2(B_0^T B_0)^(1/2)
 >= |det N| sqrt(delta)/4`.                                       (3.9)

On this same cut the ACTUAL Schur cross block is

`B=S[I,J]=B_0+G_1`, `G_1=F[I,J]`, `||G_1||_F<=epsilon_z`.         (3.10)

Tensor expansion followed by antisymmetrization gives the deterministic inequality

`||wedge^2(B_0+G_1)-wedge^2 B_0||_HS
 <=2||B_0||_F||G_1||_F+||G_1||_F^2`.                              (3.11)

Because the bank restrictions of W are contractions and N has rank two,

`||B_0||_F<=||N||_F<=sqrt(2)s_1(N)`.                              (3.12)

If (3.1) holds, then `epsilon_z<=s_2(N)sqrt(delta)/24`. Dividing the right side of (3.11) by the lower bound (3.9) gives at most

`8 sqrt(2)/24 + 4/24^2 <1/2`.                                    (3.13)

Hence

`||wedge^2 B||_HS >= |det N|sqrt(delta)/8`,                       (3.14)

so

`boxed: e_2(B^T B)>=delta |det N|^2/64.}`                         (3.15)

Apply the unconditional pair-volume half-Riesz theorem to the genuine Schur remainder, using the actual physical block B:

`H_{1/2}(S-form)
 <=C_E2 64^(1/8) delta^(-1/8)|det N|^(-1/4)`.                    (3.16)

The pinned original-coordinate square peel gives

`||p_Q||_infinity <= |a|^(-1/2)H_{1/2}(S-form)`.                  (3.17)

Substituting (2.11) into (3.16)-(3.17) proves (3.2).

If (3.1) fails, then

`delta < (24 epsilon_z/s_2(N))^2`.                                (3.18)

Insert this in account03/B13 r34's near-coloop/near-triangle alternatives to obtain (3.4)-(3.5). QED.

### Scope note

Every random variable remains an ORIGINAL coordinate. The random red/blue coloring is only a deterministic existence proof for a physical partition. The perturbation E is never evaluated as `X^T E X`; it is retained inside the actual Schur cross block B.

## 4. Diffuse consequence: either density payment or diagonal + rank one + retained rough remainder

Assume in addition

`max_i ||u_i||^2 <=1/3`.                                          (4.1)

For every remaining row after deleting z,

`||w_i||^2
 =u_i^T(I-u u^T)^(-1)u_i
 <=||u_i||^2/(1-c)
 <=1/2`.                                                          (4.2)

The designated partner r34 therefore gives

`delta>=1/512`.                                                    (4.3)

### Corollary 4.1 — `QFORM-DIFFUSE-SCHUR-RANK1-ROUGH-NORMAL-FORM-v1`

Under (2.1)-(2.13) and (4.1), either

`boxed:
 ||p_Q||_infinity
 <=96.5937072867808
   [(1-c)|a d det Lambda|]^(-1/4),
}`                                                                  (4.4)

or

`boxed: s_2(N)<384 sqrt(2) epsilon_z
              =543.058007951269... epsilon_z.}`                   (4.5)

In the latter branch there are a diagonal matrix `D'`, a symmetric matrix `R_1` of rank at most one, and a symmetric zero-diagonal matrix `E'` such that the exact Schur matrix S satisfies

`boxed:
 S=D'+R_1+E',
 ||E'||_F
 <(384 sqrt(2)+1)epsilon_z
 =544.058007951269... epsilon_z.
}`                                                                  (4.6)

#### Proof

Equation (4.4) follows from (3.2), (4.3), and

`C_R 512^(1/8)=96.5937072867808...`.

If the paid branch fails, (3.3) and (4.3) give (4.5). Since N is symmetric two-by-two, keep the eigenvalue of larger absolute value and call the resulting rank-at-most-one matrix `N_1`. Then

`||N-N_1||_F=s_2(N)`.                                             (4.7)

Because W has orthonormal columns,

`||W(N-N_1)W^T||_F=||N-N_1||_F`.                                 (4.8)

Thus

`S=D_-+W N_1 W^T + H`,

`||H||_F <(384 sqrt(2)+1)epsilon_z`.                              (4.9)

Absorb `diag(H)` into the diagonal term and put `E'=H-diag(H)`. Removing a diagonal can only reduce Frobenius norm, proving (4.6). QED.

This is the stable version of the partner's exact pair-law geometry. In a hypothetical high-ratio finite-hub sequence with `||E||_F=O(rho^(-3/2))`, every non-near-null pivot for which `epsilon_z` remains comparable to `||E||_F` now yields either a paid density inequality or a Schur remainder that is diagonal plus rank one up to a retained `O(rho^(-3/2))` Frobenius term. The explicit factor `epsilon_z` records exactly why the zero/near-zero pivot transition is still unpaid.

## 5. Required pinned-source application: D5 kills a three-dimensional transverse shared-input bank

The first unpaid implication from the previous account02/B13 run was to pay a third smoothing resource that shares original inputs with a robust rank-two carrier. The pinned D5 theorem gives an unconditional answer as soon as that shared-input transverse bank has dimension at least three.

Let I be an original physical row bank and let J,T be disjoint original physical column banks, all mutually disjoint. Put

`M=A[I,J]`, `C=A[I,T]`, `N_5=A[I,J union T]=[M C]`.                (5.1)

Assume `s_2(M)>0`. Let `P` be the orthogonal projection onto the top two left singular vectors of M and put

`C_perp=(I-P)C`.                                                   (5.2)

Write

`t_1>=t_2>=t_3>=...`                                              (5.3)

for the singular values of `C_perp`.

### Theorem 5.1 — `QFORM-D5-TRANSVERSE-THREE-MODE-v1`

For every slab ratio

`rho=P(Q in J0)/|J0|`,                                            (5.4)

the pinned D5 theorem implies

`boxed:
 rho
 <=5 sqrt(2e)
   [s_1(M)s_2(M)t_1t_2t_3]^(-1/5).
}`                                                                  (5.5)

Equivalently,

`boxed:
 s_1(M)s_2(M)t_1t_2t_3
 <=(5 sqrt(2e)/rho)^5.
}`                                                                  (5.6)

In particular,

`boxed:
 t_3
 <=(5 sqrt(2e)/rho)^(5/3)
   [s_1(M)s_2(M)]^(-1/3).
}`                                                                  (5.7)

Thus once a physical cross cut already carries a robust rank-two area `s_1(M)s_2(M)`, every additional shared-input column bank has transverse numerical rank at most two at the explicit scale (5.7). There is no row-marginal or leverage hypothesis.

#### Proof

Choose top right singular vectors `v_1,v_2` of M and top right singular vectors `w_1,w_2,w_3` of `C_perp`. In the orthogonal direct sum of the J and T coordinate domains, the five vectors

`(v_1,0),(v_2,0),(0,w_1),(0,w_2),(0,w_3)`                         (5.8)

are orthonormal. Their images under `N_5=[M C]` are

`s_1(M)u_1`, `s_2(M)u_2`, `Cw_1`, `Cw_2`, `Cw_3`.                 (5.9)

When wedged with `u_1,u_2`, the components of `Cw_j` inside `range(P)` vanish. The perpendicular components are mutually orthogonal and have lengths `t_1,t_2,t_3`. Therefore

`||wedge^5 N_5||_op
 >=s_1(M)s_2(M)t_1t_2t_3`.                                       (5.10)

Since Hilbert-Schmidt norm dominates operator norm,

`e_5(N_5^T N_5)^(1/2)
 =||wedge^5 N_5||_HS
 >=s_1(M)s_2(M)t_1t_2t_3`.                                       (5.11)

The pinned unconditional D5 theorem gives

`rho<=5sqrt(2e)e_5(N_5^T N_5)^(-1/10)`,                          (5.12)

which proves (5.5)-(5.6). Since `t_1t_2t_3>=t_3^3`, (5.7) follows. QED.

The same statement holds with rows and columns interchanged by applying it to `A^T=A`.

### Meaning for the shared-input gap

Theorem 5.1 is a direct equation-level application of the owner-required pinned source, not a numerical heuristic. It rules out an arbitrary diffuse third bank in a high-density witness: after two strong cross directions have been identified, three further transverse physical column modes cannot all remain substantial. The only shared-input transverse configurations not paid by this D5 mechanism have effective transverse rank at most two, precisely the scale at which finite-center / mixed-Fresnel or rank-one-Schur methods must now operate.

## 6. Extremal-product consequence and remaining obstruction

The optimizer-free purification theorem remains at its valid scope. If the unrestricted conjecture is false, every strict bad slab may be transferred with arbitrarily small loss to a product of indicators of bounded finite unions of intervals of total measure one. Their diameters and fragment counts may diverge. Theorems 3.1, 4.1, and 5.1 use only cap-one product structure and physical coefficient geometry, so they survive this transfer without any support parameter.

Combining the current and designated-partner results, a hypothetical counterexample sequence with `rho->infinity` cannot escape through an arbitrary diffuse rank-two Schur carrier plus an arbitrary diffuse shared-input tail. At every usable nonzero physical pivot it faces the following alternatives:

1. the ACTUAL Schur cross-volume survives the retained Frobenius twist and is paid by (3.2);
2. the normalized carrier collapses toward one physical coloop or three physical carrier coordinates by (3.4)-(3.5);
3. in the diffuse leverage chamber, the Schur remainder is diagonal + rank one + a retained Frobenius residual controlled by (4.6);
4. any additional physical column bank with three transverse modes is paid by pinned D5 through (5.5).

The first unpaid implication is therefore

`QFORM-ONE-OR-TWO-TRANSVERSE-MODE-ROUGH-GLUE-v1`:

handle the remaining one- or two-dimensional transverse shared-input bank together with the diagonal + rank-one rough Schur normal form, uniformly through `a=0` / `a` near zero, without deleting the Frobenius remainder or rotating the product variables. A valid next step may use mixed Fresnel, a physical null-pivot pair receiver, or an exact rank-one exterior identity. Otherwise construct a genuine bounded-finite-union product-indicator counterexample satisfying all target hypotheses.

## 7. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No valid counterexample is produced. Global continuity remains **OPEN**. The pinned counterexample search's negative numerical result is not used as proof.