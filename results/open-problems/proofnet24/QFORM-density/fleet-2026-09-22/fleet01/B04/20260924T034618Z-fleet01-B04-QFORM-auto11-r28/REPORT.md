SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-24T03:46:18Z.
attacking: replace the exact-collision case split by a global determinant-entropy row-cap dual, extending two-carrier balancing to arbitrarily many heavy physical rows while preserving original-coordinate product structure.

# fleet01/B04 r28 — global row-cap partition dual and entropy cancellation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / GLOBAL MULTICARRIER OPTIMIZATION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Continuity: the paid Fourier branch below has a `C_0(R)` density; full-target continuity remains open.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. All random variables remain original product coordinates. No post-rotation independence, moment/support/log-concavity hypothesis, arbitrary-joint coarea inequality, fiber-supremum estimate, or law-uniform pointwise quadratic-phase decay is used.

## 1. Fresh source boundary and mechanism change


This run deliberately changes mechanism after the preceding collision runs. The analytic receiver is Theorem D from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For a literal original-coordinate cross block `M=A[I,J]`, any probability weight `w_ST` on supported physical `3x3` minors whose I-side row marginals are at most `1/2` gives

`||p_Q||_infinity <= 6 sqrt(e) G(w)^(-1/6)`,                    (1.1)

where

`G(w)=exp( sum_ST w_ST log(det(M_ST)^2/w_ST) ).`                 (1.2)

The same proof gives an `L^1` characteristic function, hence a `C_0` density. The D' extension allows a common row cap `h<3/4`, with coefficient

`6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1)`.                             (1.3)

The freshest designated partner fleet02/B04 r18 is

`yspennstate/math-open-problems@0999bcddc0ce4780efe4c4b6cd3792cbe34b3eb3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260924T031958Z-fleet02-B04-QFORM-auto11-r18/REPORT.md`.

It proves the exact two-carrier balancing formula used in Section 5 below.

## 2. Collapse columns first: the row-triple Gibbs currency

Let `M` have physical row set `[m]`. For a physical row triple `S`, define

`z_S = sum_(|T|=3) det(M[S,T])^2 = det(M[S,:] M[S,:]^T)`,        (2.1)

with `z_S=0` for unsupported triples. Let `p=(p_S)` be any probability law on supported row triples and put

`alpha_i = sum_(S contains i) p_S`.                               (2.2)

For fixed `p`, optimize (1.2) over the conditional column law. The finite Gibbs/log-sum identity gives the unique optimum

`w(T|S)=det(M[S,T])^2/z_S`,                                      (2.3)

and reduces the determinant-entropy currency exactly to

`G_row(p)=exp( H(p)+sum_S p_S log z_S ).`                         (2.4)

Thus the whole row-marginal obstruction is a finite entropy-constrained partition function; no individual minor needs to be selected or inverted.

## 3. Exact global row-cap dual

For `0<h<1`, define

`G_h^*(M)=sup { G_row(p): p is a supported row-triple law, alpha_i<=h for every i }`, (3.1)

with value zero if the feasible set is empty.

### Theorem `QFORM-GLOBAL-ROWCAP-PARTITION-DUAL-v1`

Whenever the feasible set is nonempty,

`boxed:
 log G_h^*(M)
 = inf_(lambda_i>=0)
   { log[sum_S z_S exp(-sum_(i in S)lambda_i)] + h sum_i lambda_i }.` (3.2)

Equivalently, with `x_i=exp(-lambda_i)`,

`boxed:
 G_h^*(M)
 = inf_(0<x_i<=1)
   e_3(M^T D_x M) prod_i x_i^(-h),
 D_x=diag(x_1,...,x_m).}`                                       (3.3)

At an optimizer, every penalized row `x_i<1` has marginal exactly `alpha_i=h`; every row with `alpha_i<h` has `x_i=1`.

Consequently Theorem D gives the full ambient estimate

`boxed:
 ||p_Q||_infinity <= 6 sqrt(e) [G_(1/2)^*(M)]^(-1/6),
 p_Q in C_0(R),}`                                                (3.4)

and, for every `1/2<=h<3/4`, D' gives

`boxed:
 ||p_Q||_infinity
 <= 6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)[G_h^*(M)]^(-1/6).}`         (3.5)

#### Proof

For multipliers `lambda_i>=0`, the Lagrangian of the concave problem (3.1) is

`H(p)+sum_S p_S log z_S + sum_i lambda_i(h-alpha_i)`.

Taking the supremum over the probability simplex gives

`h sum_i lambda_i + log sum_S z_S exp(-sum_(i in S)lambda_i)`     (3.6)

by the Gibbs variational identity. Finite-dimensional concave duality (or a limiting argument if the feasible face has empty relative interior) gives equality of primal and dual. Substituting `x_i=e^-lambda_i` gives the weighted Cauchy-Binet identity

`sum_S z_S prod_(i in S)x_i = e_3(M^T D_x M)`,                   (3.7)

which proves (3.3). Complementary slackness gives the marginal statement. Substitution into Theorem D/D' proves (3.4)-(3.5). QED.

This is the arbitrary-multicarrier extension of fleet02/B04 r18's exact two-carrier formula.

## 4. Exact entropy cancellation in the grouped projected-crossing theorem

The earlier B04 theorem `QFORM-GROUPED-CROSSING-EXACT-SUBSET-ENTROPY-v1` uses, for an `ell`-subset law `w`,

`G_C(w)=exp(sum_S w_S log(d_S/w_S))`,
`F_C(w)=exp((H(w)+sum_i alpha_i log alpha_i)/2)`.                 (4.1)

Its density factor is `G_C(w)^(-1/(2d))F_C(w)^(1/d)`, where `d=k+ell`.
The Shannon entropy cancels **exactly**:

`boxed:
 G_C(w)^(-1/(2d))F_C(w)^(1/d)
 = K_C(w)^(-1/(2d)),}`                                          (4.2)

where

`boxed:
 K_C(w)=exp(sum_S w_S log d_S - sum_i alpha_i log alpha_i).}`    (4.3)

Hence the grouped theorem can be written without an entropy term as

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)] 2^((k+3ell)/(2d))
 M_H^(1/d) S^(-1/d) K_C(w)^(-1/(2d)),}`                          (4.4)

with the same `C_0` conclusion and all the same allowances for arbitrary same-bank curvature, hub functions and affine terms. This is `QFORM-GROUPED-ENTROPY-CANCELLATION-v1`.

Equation (4.2) is algebraic: insert (4.1), use `log G_C=sum w log d+H(w)`, and cancel `H(w)`. It shows that for this grouped receiver the useful currency is geometric determinant mass penalized by inclusion marginals, not Shannon entropy separately.

## 5. Explicit three-heavy-row stress family

Let `H_8` be the Sylvester Hadamard matrix and

`U=H_8[:,0:4]/sqrt(8)`,                                         (5.1)

so `U^T U=I_4`. Let

`V=(1/15)[[14,-2,-3,-4],[-2,11,-6,-8],[-3,-6,6,-12],[-4,-8,-12,-1]]`, (5.2)

an exact orthogonal matrix. For `L>=1`, put

`R_L=[L e_1; L e_2; L e_3; U]`                                  (5.3)

and

`M_L=R_L V^T`.                                                    (5.4)

All physical entries of `M_L` are nonzero. Also

`R_L^T R_L=diag(L^2+1,L^2+1,L^2+1,1)`,                           (5.5)

so the singular values are `sqrt(L^2+1)` three times and `1` once.

To make every coefficient of the ambient symmetric matrix nonzero, set

`A_L=[[0,M_L],[M_L^T,0]] + 10^(-3)(J_11 direct_sum J_4)`.        (5.6)

The same-bank perturbation has operator norm at most `0.011`; for `L>=1` the six eigenvalues inherited from the three `sqrt(L^2+1)` crossing singular values retain modulus at least `sqrt(2)-0.011>1`. Thus (5.6) is fully dense, genuinely rotated, indefinite, and satisfies the exact owner target.

Relative to the three heavy rows, the row-triple squared-volume face masses are, exactly,

`W_empty=4`,                                                     (5.7)
`W_{a}=3L^2` for each one-heavy face,                            (5.8)
`W_{ab}=2L^4` for each two-heavy face,                           (5.9)
`W_{123}=L^6`.                                                   (5.10)

These follow from Cauchy-Binet on the light Parseval frame after fixing the heavy coordinate axes.

At the Theorem-D cap `h=1/2`, symmetry and (3.3) reduce the exact global optimization to one fugacity. Put

`Z(y)=4+9y+6y^2+y^3`.                                            (5.11)

The heavy marginal condition is `y Z'(y)/Z(y)=3/2`, equivalently

`y^3+2y^2-3y-4=0`,                                               (5.12)

whose positive root is

`r=(sqrt(17)-1)/2`.                                               (5.13)

Therefore

`boxed:
 G_(1/2)^*(M_L)=C_3 L^3,}`                                      (5.14)

where

`C_3=Z(r)r^(-3/2)=4(r+1)(r+2)r^(-3/2)
   =18.7011226692076... .`                                      (5.15)

Every heavy row has marginal exactly `1/2`. The eight light rows have equal marginal `3/16`, hence their constraints are inactive, verifying the global KKT conditions over **all eleven physical rows**.

The new theorem gives

`boxed:
 ||p_(X^T A_L X)||_infinity
 <=6 sqrt(e) C_3^(-1/6)L^(-1/2),
 p_(X^T A_L X) in C_0(R).}`                                    (5.16)

For `L=1` this is `6.071843159192598...`; for `L=2` it is

`boxed: 4.293441472166236... .}`                                 (5.17)

The purpose is the exact global multicarrer optimization: no one or two heavy rows are privileged and no tiny physical minor is inverted.

## 6. Designated fleet02/B04 result applied on the same family

Apply fleet02/B04 r18's completed `QFORM-TWO-CARRIER-GEOMETRIC-BALANCE-v1` to `M_1`, taking the first two heavy rows as its distinguished carriers. The four aggregate face masses are

`W_00=7`, `W_10=W_01=5`, `W_11=3`.                              (6.1)

Hence the partner theorem gives the exact two-carrier currency

`G_12=2(sqrt(21)+5)=19.1651513899117...`.                        (6.2)

Its optimal face probabilities are

`q_00=q_11=sqrt(21)/[2(sqrt(21)+5)]`,
`q_10=q_01=5/[2(sqrt(21)+5)]`.                                  (6.3)

The third heavy row then has actual marginal

`alpha_3
 =q_00(3/7+1/3)+2q_10(2/5)
 =0.390891054882004... <1/2`,                                   (6.4)

and each light row has marginal

`(2-alpha_3)/8=0.201138618139749... <1/2`.                       (6.5)

So the designated partner theorem applies at its exact hypotheses, and Theorem D yields the actual full-law inequality

`boxed:
 ||p_(X^T A_1 X)||_infinity
 <=6 sqrt(e)[2(sqrt(21)+5)]^(-1/6)
 =6.047090231517419... .}`                                      (6.6)

This is slightly sharper than the symmetric three-carrier cap on `L=1`, because the third carrier is not yet heavy enough to require saturation. At `L=2`, however, the same two-carrier optimizer gives the third carrier marginal above `1/2`, while the global three-carrier dual (5.14)-(5.17) remains feasible and exact. Thus r28 genuinely extends the partner's two-carrier balancing mechanism rather than merely renaming it.

## 7. What remains

The new dual solves the **optimization** problem once a useful literal cross block is supplied; it does not prove that the bare three-large-eigenvalue hypothesis forces `G_(1/2)^*(M)` to a universal target scale for some physical cut. The full conjecture remains open.

The sharpened next implication for this mechanism is

`QFORM-GLOBAL-ROWCAP-CURRENCY-OR-OVERLAP-ROUTING-v1`:

> Starting from the target spectral hypothesis and the current overlap-one/two/disjoint-E3 structural funnel, either produce a literal physical cross block with `G_(1/2)^*(M)>=c` by the exact dual (3.3), or show that the minimizing fugacity collapses onto a low-dimensional heavy face that is paid by the completed pair, grouped-hub, ridge, projected-crossing, square-bank, or zero-diagonal overlap-two receivers.

This is a structural bridge, not a proved claim.

Independent review of the new dual and its application is still pending. Full-target essential boundedness and full-target continuity are not claimed.
