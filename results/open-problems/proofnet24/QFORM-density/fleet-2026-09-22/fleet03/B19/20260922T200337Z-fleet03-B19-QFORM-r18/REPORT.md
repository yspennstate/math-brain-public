SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), fleet03, slot B19, 2026-09-22T20:03:37Z.
attacking: the first unpaid nonzero-pivot O0 near-coloop implication, by replacing reciprocal pair selection with a hybrid mixed-exponent regularized-determinant / exact-two-row dichotomy.

# fleet03/B19 — hybrid heavy-row closure of the nonzero-pivot transverse O0 branch

**Run:** `20260922T200337Z-fleet03-B19-QFORM-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Start control:** `yspennstate/math-research-brain@36c473d75525e102cafb6436d918b798cab5e002`, owner revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NONZERO-PIVOT TRANSVERSE NEAR-COLOOP DEBT REMOVED / FULL QFORM OPEN`.

## 1. Target and correction discipline

The full target remains the unrestricted statement: for every dimension, independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential-density bound for `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately.

This run does **not** use post-rotation independence, law-uniform scalar quadratic-phase decay, unrestricted fiber suprema, a worst conditional projection-density cap, the refuted arbitrary-joint rank-three coarea inequality, or reciprocal inversion of a single tiny physical minor. The only Fourier pointwise estimate used below is the already completed **product-bank regularized determinant inequality**, whose proof decouples an original-coordinate product law before applying geometric Brascamp--Lieb.

The run changes mechanism relative to the preceding B19 passes. Instead of further local Schur/minor selection, it derives a mixed Fourier-power graph inequality and spends a near-coloop row by Cauchy--Schwarz. If a second physical row is even moderately large, the two **whole rows** form an exact-rank-two bank and are paid without selecting any column pair.

## 2. Completed inputs actually used

### 2.1 B08 fine-scale transverse state

Source observed on current repository history:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T194215Z-fleet03-B08-qform-diffuse-r19/REPORT.md`.

After completing a genuine nonzero original-coordinate scalar pivot `a0`, the relevant O0 transverse branch supplies an actual residual original-coordinate cross block `H` and a scale `gamma>0`. At

`g=gamma/16`,                                                        (2.1)

its ridge kernel

`K=H H^T(g^2 I+H H^T)^(-1)`                                        (2.2)

has effective dimension

`theta=tr K >=256/129`.                                             (2.3)

The B08 result already pays:

* `theta>=201/100`, with density `<1543/sqrt(|a0| gamma)`;
* `theta<201/100` and `max_i K_ii<=99/100`, with density `<3349/sqrt(|a0| gamma)`.

Thus its only nonzero-pivot fine-scale survivor had `theta<201/100` and a physical row `j` with `K_jj>99/100`. B08 additionally derived large one- and two-sided exterior-volume currencies, but those will no longer be needed for this branch after the theorem below.

### 2.2 Exact two-row cross-bank half-Riesz endpoint

The completed fleet01/B19 theorem

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T191359Z-b19-qform-r11/REPORT.md`

proves that if an arbitrary quadratic-affine residual has an original-coordinate cross block `C` with exactly two active physical rows and `rank C=2`, then

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <=4 sqrt(2) e^(1/4) Pi_2(C)^(-1/4)`,                           (2.4)

where `Pi_2(C)=s_1(C)s_2(C)=sqrt(det(CC^T))`. Arbitrary self blocks and outside couplings are retained.

The same source records the physical-square transducer

`Q=a0(Z+h)^2+R  =>  ||p_Q||_infinity<=|a0|^(-1/2) H_(1/2)(R)`. (2.5)

### 2.3 Bank regularized determinant machinery

The completed regularized-determinant proof is at

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its scalar norm estimates and geometric Brascamp--Lieb step are used in Section 3 below. I rederive the needed mixed-exponent extension rather than assuming it.

## 3. New mixed-exponent regularized graph inequality

Let `D_1,...,D_m` be independent differences of independent cap-one variables, hence their densities are difference densities. Let `R` be an `m x N` real matrix with columns `r_i`. Let `f_i` be arbitrary probability densities with `0<=f_i<=1`. Fix `xi in R`, `alpha>0`, and exponents

`1<=q_i<=2`.                                                       (3.1)

Put

`M=alpha I_m+xi^2 R R^T`,
`c_l=alpha e_l^T M^(-1)e_l`,
`d_i=xi^2 r_i^T M^(-1)r_i`,
`Theta=sum_i d_i=sum_l(1-c_l)`.                                  (3.2)

Assume

`d_i<=q_i/2` for every i.                                         (3.3)

### Lemma 3.1 — `QFORM-MIXED-Q-GRAPH-BL-v1`

Under (3.1)--(3.3),

`E prod_i |hat f_i(xi r_i dot D)|^(q_i)
 <=det(I+xi^2 R R^T/alpha)^(-1/2)
   (L_1/sqrt(alpha))^Theta
   prod_i q_i^(-d_i/2)`,                                        (3.4)

where

`L_1=pi e sqrt(2)`.                                               (3.5)

In particular the final product is at most one.

#### Proof

The completed graph proof uses the normalized vectors

`v_l=sqrt(alpha)M^(-1/2)e_l`,
`w_i=xi M^(-1/2)r_i`,                                            (3.6)

whose outer products sum to the identity. Their squared norms are `c_l,d_i`. Geometric rank-one Brascamp--Lieb gives, after the same linear change of variables as in the source theorem,

`det(M)^(-1/2)
 prod_l [alpha^(c_l/2)c_l^(-c_l/2)||g_l||_(1/c_l)]
 prod_i [d_i^(-d_i/2)|| |hat f_i|^(q_i)||_(1/d_i)]`,            (3.7)

where `g_l` is the difference density of `D_l`.

The sharp scalar estimates already proved in the regularized-determinant report are

`||g_l||_(1/c)
 <=2^c c^(c/2)(1+c)^(-(1+c)/2)`,                                (3.8)

and, for `d<=q/2`,

`|| |hat f|^q ||_(1/d)
 <=(2pi)^d q^(q/2-d)(q-d)^(-(q-d)/2)d^(d/2)`.                    (3.9)

The powers of `c_l,d_i` cancel in (3.7). Write

`G(c)=2^c(1+c)^(-(1+c)/2)`,
`H_q(d)=q^(q/2-d)(q-d)^(-(q-d)/2)`.                             (3.10)

The same concavity calculation as in the source gives

`log G(c)<=(1-log 2)(1-c)/2`,
`log H_q(d)<=(1-log q)d/2`.                                    (3.11)

Since `sum_l(1-c_l)=sum_i d_i=Theta`, substitution into (3.7), followed by factoring `alpha^m` from `det M`, gives exactly

`det(I+xi^2RR^T/alpha)^(-1/2)
 [pi e sqrt(2)/sqrt(alpha)]^Theta
 prod_i q_i^(-d_i/2)`.                                         (3.12)

This is (3.4). No common `q` was required. QED.

For all `q_i=2`, retaining `prod 2^(-d_i/2)` turns `L_1` into

`L_2=pi e`.                                                     (3.13)

## 4. New heavy-row dichotomy

Consider the B08 residual quadratic-affine form `R` and orient its original-coordinate cross cut as

`R(X,Y)=F(X)+2X^T H Y+G(Y)+c`.                                 (4.1)

All `X_i,Y_j` remain original independent coordinates with density cap one. Let `h_i` denote row `i` of `H`. For `t real`, one Cauchy--Schwarz step removes `F`, and expansion against an independent copy `Y'` gives the standard source-valid inequality

`|phi_R(t)|^2
 <= E_D prod_i a_i(D,t)`,                                      (4.2)

where

`D=Y-Y'`,
`a_i(D,t)=|hat f_i(2t h_i dot D)| in [0,1]`.                   (4.3)

Assume throughout this section

`256/129<=theta<201/100`,
`ell:=K_jj>99/100`.                                            (4.4)

There are two exhaustive cases.

### Case A: another physical row has ridge leverage above one half

Suppose some `k!=j` has

`K_kk>1/2`.                                                     (4.5)

Because `0<=K<=I`, the two-by-two principal block obeys the contraction determinant inequality

`det K[{j,k}] >=K_jj+K_kk-1>49/100`.                           (4.6)

Also

`K<=g^(-2) H H^T`.                                             (4.7)

Taking the `{j,k}` principal block and using determinant monotonicity for positive definite two-by-two matrices gives

`det(H_{jk}H_{jk}^T)> (49/100) g^4`.                           (4.8)

Thus the **whole two-row cross bank** `C=H_{jk}` has exact rank two and

`Pi_2(C)> (7/10)g^2`.                                          (4.9)

Apply the completed exact-two-row theorem (2.4), then (2.5):

`||p_Q||_infinity
 <4sqrt(2)e^(1/4)(7/10)^(-1/4)
   |a0|^(-1/2)g^(-1/2)`.                                      (4.10)

With `g=gamma/16`,

`boxed(||p_Q||_infinity<31.764/sqrt(|a0| gamma).)`             (4.11)

No column pair is selected; all columns in the two physical rows remain in the exact-rank-two bank.

### Case B: the near-coloop row is the only row above one half

Assume instead

`K_ii<=1/2` for every `i!=j`.                                  (4.12)

Set

`P=prod_(i!=j) a_i`,
`A_1=E[a_j^2 P]`,
`B_1=E[P]`.                                                     (4.13)

Cauchy--Schwarz gives

`E[a_j P] <=A_1^(1/2)B_1^(1/2)`.                              (4.14)

For `A_1`, apply Lemma 3.1 with `xi=2t`, `alpha=(2g t)^2`, `q_j=2`, and `q_i=1` for `i!=j`. Then `d_i=K_ii`; (4.12) verifies the `q_i=1` constraints and `d_j<=1` is automatic. If

`D_0=det(I+HH^T/g^2)`,                                        (4.15)

then

`A_1
 <=D_0^(-1/2)(L_1/(2g|t|))^theta`.                         (4.16)

For `B_1`, Cauchy--Schwarz once more gives

`B_1^2<=E[P^2]`.                                               (4.17)

Let `H_-j` be `H` with row `j` removed, and define

`K_-j=H_-j H_-j^T(g^2I+H_-j H_-j^T)^(-1)`,
`theta_-=tr K_-j`,
`D_-=det(I+H_-j H_-j^T/g^2)`.                                 (4.18)

The all-`q_i=2` instance of Lemma 3.1 has no leverage restriction and gives

`E[P^2]
 <=D_-^(-1/2)(L_2/(2g|t|))^theta_-`.                          (4.19)

Combining (4.2), (4.14), (4.17), (4.16), and (4.19),

`|phi_R(t)|
 <=D_0^(-1/8)D_-^(-1/16)
   (L_1/(2g|t|))^(theta/4)
   (L_2/(2g|t|))^(theta_-/8).`                                (4.20)

It remains to lower-bound `theta_-` without any dimension assumption. Put

`M_-=g^2I+H_-j^T H_-j`, `tau=h_j M_-^(-1)h_j^T`.              (4.21)

Sherman--Morrison gives

`ell=tau/(1+tau)`.                                             (4.22)

Moreover

`theta-theta_-
 =g^2 h_j M_-^(-2)h_j^T/(1+tau)
 <=tau/(1+tau)=ell<=1`,                                       (4.23)

because `M_->=g^2I` implies `g^2M_-^(-2)<=M_-^(-1)`. Hence

`theta_->=theta-1`.                                            (4.24)

Define

`beta=theta/4+theta_-/8`.

From (2.3) and (4.24),

`beta>=(3theta-1)/8
 >=(3*(256/129)-1)/8
 =213/344`.                                                     (4.25)

Thus

`beta-1/2>=41/344`.                                            (4.26)

Since `D_0,D_->=1` and `L_2<=L_1`, (4.20), together with `|phi_R|<=1`, yields the clean universal envelope

`|phi_R(t)|
 <=min{1,(T/|t|)^(213/344)},
 T=L_1/(2g)=pi e/(sqrt(2)g).`                                 (4.27)

The completed half-Riesz Fourier identity says

`H_(1/2)(R)
 <=sqrt(2/pi) int_0^infinity t^(-1/2)|phi_R(t)|dt`.            (4.28)

Using (4.27),

`int_0^infinity t^(-1/2)|phi_R(t)|dt
 <=sqrt(T)[2+1/(213/344-1/2)]
 =sqrt(T)*(426/41)`.                                           (4.29)

Since `T=pi e/(sqrt(2)g)`,

`boxed(
 H_(1/2)(R)
 <=(426/41) 2^(1/4) sqrt(e) g^(-1/2)
 <20.372 g^(-1/2).
)`                                                              (4.30)

Applying the genuine outer physical square (2.5) and `g=gamma/16` gives

`boxed(
 ||p_Q||_infinity
 <81.488/sqrt(|a0| gamma).
)`                                                              (4.31)

This is the new analytic payment. The exponent gain is not a scalar van-der-Corput decay: it comes from one product-bank mixed-power Brascamp--Lieb estimate plus an independent-copy `q=2` payment after deleting the heavy row.

## 5. Target-level consequence for the B08 nonzero-pivot transverse branch

Combine the completed B08 alternatives with Section 4.

### Theorem 5.1 — `QFORM-NONZERO-PIVOT-TRANSVERSE-FULL-LEVERAGE-CLOSURE-v1`

Under the exact B08 O0 transverse hypotheses, with genuine nonzero original-coordinate pivot `a0`, scale `gamma>0`, and residual cross block satisfying the inherited exterior-two-volume reserve, **no ridge-leverage exception remains**. More precisely,

`boxed(
 ||p_Q||_infinity
 <3349/sqrt(|a0| gamma).
)`                                                              (5.1)

Indeed:

1. if `theta>=201/100`, B08 r19 gives `<1543/sqrt(|a0|gamma)`;
2. if `theta<201/100` and `max diag K<=99/100`, B08 r17/r19 gives `<3349/sqrt(|a0|gamma)`;
3. if `max diag K>99/100`, Section 4 gives `<82/sqrt(|a0|gamma)`.

Therefore the previous two-sided `99%` near-coloop intersection bank is no longer an analytic obstruction in the **nonzero-pivot transverse** branch. The aggregate minor currency remains mathematically valid, but it need not be inverted or grouped to pay this branch.

The theorem proves absolute continuity and an essential `L^infinity` bound. The mixed half-Riesz/square splice does **not** by itself prove a continuous representative.

## 6. Actual application of designated partner fleet04/B19

The completed designated-partner result remains `QFORM-FINITE-UNION-CORE-v1`, canonical source

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T122030Z-fleet04-B19-QFORM-r1/REPORT.md`.

Apply it to the concrete interval inequality produced by Theorem 5.1. On bounded finite-union product-indicator cores the proof above gives

`P{Q in I}<=[3349/sqrt(|a0|gamma)] |I|`.                       (6.1)

The partner theorem transfers (6.1), with **no constant loss**, through the monotone finite-union approximation to every independent coordinate law with density cap one. Thus the same inequality (5.1) holds for the full arbitrary cap-one class. This is an actual application to the new inequality, not only attribution.

The direct Fourier proof above already covers the cap-one class; the partner application supplies an independent product-law closure route and checks that no hidden support regularity entered.

## 7. Compact conditional full-proof assembly after this run

A correction-safe proof tree now reads:

1. previously completed low-off-diagonal branches are paid by universal constants;
2. high-off-diagonal matrices are reduced by the source-valid third-compound overlap machinery to O0/O1/O2/O3, without asserting that one physical cross minor controls the law;
3. O0 diffuse/effective-dimension branches are paid by the completed ridge estimates;
4. O0 with three heavy physical rows is paid by B19 r17 through an exact three-row-by-many-column cross bank;
5. every O0 **nonzero-pivot transverse** branch carrying the B08 exterior reserve is now paid by Theorem 5.1, including the formerly unpaid `>99%` near-coloop case;
6. the exact-zero Schur diagonal endpoint is separately paid by the completed zero-diagonal affine half-Riesz theorem;
7. what is not yet globally paid is the structural transition through genuinely zero/near-zero physical pivots where a universal lower bound on `|a0|gamma` is unavailable, plus the independent O1/O2/O3 overlap splices.

Thus the first O0 analytic debt has changed. It is no longer `near-coloop aggregate -> fixed/grouped rank-two payment`.

## 8. First unpaid implication after the new closure

The next implication is

### `QFORM-O0-ZERO-NEARZERO-PIVOT-DISCRIMINANT-SCALE-BRIDGE-v1`

Starting from the remaining O0 one/two-heavy structural state, prove an exhaustive alternative:

* either produce a genuine original-coordinate pivot and transverse scale with `|a0|gamma>=c_*>0`, in which case Theorem 5.1 closes it immediately;
* or, in the genuinely zero/near-zero pivot state, retain the physical discriminant/remainder coupling and obtain a translation-uniform fractional/small-ball estimate from a second grouped smoother.

The exact-zero endpoint is already paid, but the live rank-one counterexample to a naive “small diagonal is almost zero” half-Riesz continuity argument remains binding. Therefore the near-zero branch must be attacked by discriminant/grouped smoothing, not by continuity of the exact-zero lemma.

The separate O1/O2/O3 aggregate overlap branches remain full-target debts.

## 9. Status

* `QFORM-MIXED-Q-GRAPH-BL-v1`: **PROVED**.
* `QFORM-NONZERO-PIVOT-TRANSVERSE-FULL-LEVERAGE-CLOSURE-v1`: **PROVED at the stated B08 structural scope**.
* Former `99%` near-coloop analytic debt in that branch: **REMOVED**.
* Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Continuous representative for the unrestricted target: **OPEN**. The new half-Riesz branch proves essential boundedness, not continuity.

No Monte Carlo, post-rotation independence, unsupported conditioning, single-minor reciprocal payment, paid API/model call, external workflow, or public release is used here.
