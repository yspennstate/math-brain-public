# I0071: exact scope and a weighted-polynomial estimate

Date: 2026-10-12. Verdict for the full source problem: PARTIAL.

## 1. Recovered question and conventions

Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity:
An Extended Survey*, NoDEA 32, article 123 (2025), DOI
10.1007/s00030-025-01090-2, Problem 7, printed p. 131, PDF p. 132 including
the Delft cover. The downloaded final publication is source.pdf.

The Itô system (8.14) is

    du_i = (nu_i Delta u_i + f_i(u)) dt
           + sum_n [b_(n,i) dot grad u_i + g_(n,i)(u)] dW^n.

The same independent Brownian motions can drive different species. The
domain is T^d or R^d, ell >= 2, and the transport fields belong to
C^gamma(O;ell^2(R^d)), gamma > 0. For a fixed h > 1 the six requirements are:

1. Initial data are componentwise nonnegative (understood pointwise for
   function-valued data in an admissible local existence space).
2. Each g_i:R^ell -> ell^2 is globally Lipschitz and vanishes on u_i=0 in
   the positive orthant.
3. f_i >= 0 on that boundary face (quasipositivity).
4. |f_i(y)-f_i(z)| <= C(1+|y|^(h-1)+|z|^(h-1))|y-z| on the orthant.
5. sum_i f_i(y) <= K_0+K_1 sum_i y_i.
6. There are r in R^ell and a nonnegative invertible lower triangular
   matrix R such that R f(y) <= (1+sum_i y_i) r componentwise.

The published condition (5) introduces K_1,K_2 but then displays K_0,K_1;
this is a naming inconsistency, not a new growth assumption. The r in
condition (6) is a vector multiplier, not a vector of exponents.

The question explicitly continues: "Does the global well-posedness hold
with g_i having superlinear growth? Is it possible to allow for optimal
growth of g, i.e. Assumption 8.4(3)?" The optimal local-Lipschitz exponent
for g in that assumption is (h-1)/2, corresponding to growth (h+1)/2.
These extensions are retained as part of the full target.

Throughout the positive PDE result below, strict stochastic parabolicity
is an explicit assumption inherited from the source's local framework:

    2 nu_i |xi|^2 - sum_n |b_(n,i)(x) dot xi|^2 >= mu |xi|^2,
    mu > 0, uniformly in i,x,xi.                         (SP)

No smallness beyond (SP) is imposed. The extracted printed Assumption
8.4(2) appears with the reversed inequality on sum_n b b; the intended
condition is (SP), consistent with the source's general parabolicity
condition (3.10), following the example (3.9). We do not use that apparent typographical error as a
counterexample. Dropping parabolicity changes even local well-posedness.

## 2. Precisely proved positive result

For the periodic domain, under (SP), conditions (1)--(4),(6), and the
source's admissible local existence parameters and initial data, the
maximal positive solution from Theorem 8.6 has infinite lifetime. This
holds in every dimension, for every finite ell and every polynomial h.
Condition (5) is unnecessary in the proof of this restricted result.
The reaction noise is globally Lipschitz. Existence, uniqueness,
instantaneous regularization, positivity, and the continuation criterion
are the source's local results; the new work here is the a priori energy
estimate giving continuation. No claim about new quantitative continuity
in initial data is made beyond the well-posedness furnished by that local
theory and continuation.

The proof first establishes the estimate for any positive regular local
solution. Section 8 explains how to justify its Itô formula at the
regularity of the source and use its continuation criterion.

## 3. Polynomial lemma, with complete proof

Fix an integer m >= 2. For a multi-index alpha in N^ell, let |alpha| be
the sum of its entries. Write

    c_alpha = product_i theta_i^(alpha_i^2), theta_i >= 1,
    P(y) = sum_(|alpha|=m) [m!/(product_i alpha_i!)] c_alpha y^alpha.

Set S=sum_i y_i. On the positive orthant all terms are nonnegative.
The multinomial theorem gives S^m <= P(y) <= C S^m, where C is the
largest of the finitely many coefficients c_alpha. Thus P is equivalent
to the mth power of any finite-dimensional norm on that orthant.

Writing P_i=partial_i P and H_ij=partial_i partial_j P, differentiation
and reindexing give

    P_i = m sum_(|beta|=m-1) binom(m-1,beta) c_(beta+e_i) y^beta,
    H_ij = m(m-1) sum_(|beta|=m-2)
                    binom(m-2,beta) c_(beta+e_i+e_j) y^beta.       (1)

The second formula also holds for i=j, with beta+2e_i.

For i<j and |beta|=m-1, the ratio of corresponding coefficients in
P_i and P_j is

    c_(beta+e_i)/c_(beta+e_j)
       = theta_i^(2 beta_i+1)/theta_j^(2 beta_j+1).

If theta_i >= D theta_j^(2m-1), D >= 1, this ratio is at least D.
Comparing each nonnegative monomial proves P_i >= D P_j everywhere.
Starting with a large theta_ell and choosing theta_(ell-1),...,theta_1
successively achieves this simultaneously for all i<j.

For |beta|=m-2 and i != j, direct subtraction of exponents gives

    c_(beta+e_i+e_j)
       = (theta_i theta_j)^(-1)
          sqrt(c_(beta+2e_i)c_(beta+2e_j)).                      (2)

All coefficients are positive real numbers. Apply Cauchy--Schwarz to
the finite sum (1), using its nonnegative weights
m(m-1)binom(m-2,beta)y^beta. This proves

    0 <= H_ij <= (theta_i theta_j)^(-1) sqrt(H_ii H_jj).          (3)

Consequently any prescribed epsilon>0 can be obtained in (3) by
requiring theta_i >= epsilon^(-1/2) for every i. This requirement is
compatible with all gradient-ordering requirements above.

For y != 0 in the orthant, every H_ii is positive: when some y_j>0,
the beta=(m-2)e_j term in (1) is positive, including when j=i.
For m=2 H_ii is a positive constant. On the compact simplex S=1,
all H_ii have positive minima. Continuity on that simplex and
homogeneity therefore imply, for a constant C_P,

    sum_i P_i^2/H_ii <= C_P P,                                 (4)
    sum_i H_ii y_i^2 <= m(m-1)P.                               (5)

For an explicit bound in (4), (1) and c_alpha>=1 give
H_ii>=m(m-1)S^(m-2), while P_i<=m C S^(m-1), with
C=max_(|alpha|=m)c_alpha. Thus the sum of ratios is at most
[ell*m*C^2/(m-1)]S^m <= [ell*m*C^2/(m-1)]P. At y=0 use the continuous value 0 for the
ratios if m>2. For (5), the coefficient of a given monomial in
sum_i H_ii y_i^2 is multiplied by sum_i alpha_i(alpha_i-1), which is
at most m(m-1). Euler's identity also gives sum_i P_i y_i=mP.
This proves all polynomial assertions, including at boundary faces.

## 4. Triangular reaction estimate

The diagonal entries R_ii are strictly positive: invertibility of a
triangular matrix makes them nonzero, and nonnegativity makes them
positive. Let

    D >= max(1, max_i sum_(j>i) R_ji/R_jj).

The preceding construction ensures

    P_i >= sum_(j>i) (R_ji/R_jj) P_j.                          (6)

For each y, solve R^T lambda=grad P by backward substitution. Its last
entry is lambda_ell=P_ell/R_ell,ell >=0. Suppose later entries satisfy
0<=lambda_j<=P_j/R_jj. Then

    lambda_i=(P_i-sum_(j>i)R_ji lambda_j)/R_ii

is nonnegative by (6) and is at most P_i/R_ii. Backward induction
proves these statements for every i. Hence

    grad P dot f = lambda dot (Rf)
        <= (1+S) sum_i lambda_i r_i
        <= (1+S) sum_i (|r_i|/R_ii) P_i
        <= C(1+S) S^(m-1) <= C'(1+P).                         (7)

The penultimate inequality follows from (1) and bounded coefficients;
the last follows by splitting into S<=1 and S>=1. Multiplying the
componentwise inequality by lambda is legitimate because lambda>=0.
No estimate of individual positive f_i by linear functions is assumed.

## 5. Absorption of species-dependent transport

Let v_i be arbitrary spatial gradient vectors, and let
B_i:R^d -> ell^2 be B_i v=(b_(n,i) dot v)_n at a fixed point x.
Uniform boundedness gives ||B_i||<=B. The diffusion and pure-transport
part of Itô's drift for P is

    Q = -sum_(i,j) H_ij nu_i v_i dot v_j
        + (1/2)sum_(i,j)H_ij <B_i v_i, B_j v_j>.

Because H is symmetric, the diagonal contribution is at most
-(mu/2)sum_i H_ii|v_i|^2 by (SP). The combined contribution of a pair
i<j has absolute value at most

    (nu_i+nu_j+B^2) H_ij |v_i||v_j|.

Set K=max_(i<j)(nu_i+nu_j+B^2). With z_i=sqrt(H_ii)|v_i|,
(3) bounds the mixed sum by

    K epsilon sum_(i<j) z_i z_j
       <= K epsilon (ell-1)/2 sum_i z_i^2.

Choose epsilon with K epsilon(ell-1)/2 <= mu/4. This proves

    Q <= -(mu/4) sum_i H_ii|v_i|^2.                           (8)

This pointwise estimate includes every cross-species covariance of the
common Brownian drivers. Neither equal diffusion coefficients nor equal
transport fields nor divergence-free fields have been assumed. No
derivative of b has been used.

## 6. Reaction-noise terms

If L is the maximum global Lipschitz constant of g_i, set y_i=0 while
leaving the other coordinates fixed. The boundary vanishing condition
and Lipschitz continuity imply

    norm_l2(g_i(y)) <= L y_i.                                 (9)

Here norm_l2 denotes the norm in the Brownian-index sequence space ell^2.
In subsequent formulas ||g_i||^2 means the square of that norm.

The Hessian normalized by diag(sqrt(H_ii)) has diagonal entries 1 and
mixed entries at most epsilon. Its operator norm is at most
1+(ell-1)epsilon, by the row-sum bound (or by summing 2|z_i z_j|).
Thus the transport/noise cross term has absolute value at most

    C [sum_i H_ii|v_i|^2]^(1/2)
       [sum_i H_ii||g_i(y)||^2]^(1/2).

Young's inequality bounds it by (mu/8)sum_i H_ii|v_i|^2 plus a
constant times sum_i H_ii||g_i||^2. The purely g quadratic term is
bounded by another constant times the latter sum. Equations (5),(9)
bound that sum by L^2 m(m-1) P. Combined with (7),(8), the complete
Itô drift is at most

    C(1+P) - c sum_i H_ii |grad u_i|^2, c=mu/8.              (10)

All constants may depend on m,R,nu,mu,B,L; none depends on the stopping
level. Large weights are allowed and need not be uniform as m grows.

## 7. Expected maximal energy estimate

For the torus with finite volume, write

    V(t)=integral P(u(t,x)) dx,
    E(t)=integral sum_i H_ii(u(t,x))|grad u_i(t,x)|^2 dx.

For an initially regular positive solution, stop where all local Itô
integrals are bounded. The inequality furnished by (10) is

    V(t)+c integral_0^t E(s) ds
        <= V(0)+C integral_0^t (1+V(s)) ds + M(t),            (11)

where M is a real continuous local martingale. For its transport
integrand, Cauchy--Schwarz, boundedness of B_i, and (4) give

    ||sum_i integral P_i B_i grad u_i dx||_ell^2
        <= C sqrt(V E).

For its g integrand, (9) and Euler's identity give

    ||sum_i integral P_i g_i dx||_ell^2
        <= L integral sum_i P_i u_i dx = Lm V.

Consequently

    d<M>_t <= C [V(t) E(t)+V(t)^2] dt.                     (12)

Use additional stopping to make M a genuine martingale, and denote the
resulting time by tau_N. Taking expectations in (11), with the usual
indicators t<tau_N in integrals, gives

    E V(t wedge tau_N) <= E V(0)
          +C integral_0^t (1+E V(s wedge tau_N)) ds.

Indeed 1_(s<tau_N)V(s) <= V(s wedge tau_N) since V>=0.
Gronwall gives an N-independent bound C_T(1+E V(0)) on terminal
expected energy for t<=T. Keeping the negative term in (11) then gives
the same bound on E integral_0^(T wedge tau_N) E(s) ds.

For the maximal estimate, Burkholder--Davis--Gundy with exponent 1 and
(12), followed by Young's inequality, give

    E sup_(t<=T) |M(t wedge tau_N)|
      <= delta E sup_(t<=T) V(t wedge tau_N)
          +C_delta E integral_0^(T wedge tau_N) [E(s)+V(s)] ds.

To see the use of Young explicitly, bound the square root of the
bracket by
C sqrt(sup V) sqrt(integral(E+V)); apply ab<=delta a^2+C_delta b^2,
then take expectations. Both integrals on the right already have
uniform expected bounds. Taking the supremum in (11) and choosing
delta<1/2 yields

    E sup_(t<=T) V(t wedge tau_N)
       + E integral_0^(T wedge tau_N) E(s) ds
         <= C_T (1+E V(0)).                                (13)

There is no circular attempt to absorb an arbitrarily large BDG constant
into c. The expected gradient integral is bounded before BDG is used.
Fatou's lemma removes the localizing sequence and proves almost sure
finiteness of sup V up to any finite lifetime endpoint, with the usual
bounded-initial-energy localization if V(0) lacks an integrable moment.

## 8. Itô justification and continuation

Theorem 8.6 gives u in L^r_loc((0,sigma);H^{1,r}) for all r>2 and
locally Hölder continuous in space-time, for the source's admissible
parameters. Positivity is furnished by its boundary conditions on f,g.
These imply that on a compact interval away from 0 and before sigma,
after stopping at bounds on ||u||_infinity and integral ||u||_(H^{1,2})^2,
u is bounded and its gradient square-integrable. The nonlinear reaction
and reaction-noise integrands are then bounded on the compact torus;
b grad u is square-integrable in space-time with values in ell^2.

Here is the regularization argument behind (11), rather than an
assumption of smooth transport fields. Convolve periodically in space
with a smooth nonnegative approximate identity J_epsilon. The process
J_epsilon u has smooth spatial trajectories and satisfies the convolved
Itô equation. Apply the finite-dimensional Itô formula pointwise to
P(J_epsilon u), integrate in x, and integrate the Laplacian by parts.
The convolution preserves nonnegativity and the stopped L-infinity
bound. J_epsilon u -> u uniformly on the stopped compact time-space
set and in L^2(H^{1,2}); J_epsilon(b grad u+g(u)) converges in
L^2(space-time;ell^2). All first and second polynomial derivatives
are bounded there. Therefore the quadratic Itô integrands converge in
L^1, the integrated diffusion terms converge in L^1, and the integrated
martingale integrands converge in L^2(time;ell^2). The drift reaction
terms converge in L^1 as well. Stochastic integral convergence follows
from the Itô isometry after stopping. Stochastic Fubini is justified
by these same finite-volume L^2 bounds. Passing to the limit proves the
Itô identity and hence (11). The convolved transport term is not
replaced by b grad(J_epsilon u); only its L^2 limit is used.

For general admissible initial data, begin at a deterministic s>0 on
the event {s<sigma, V(s)<=N}. This event belongs to F_s. Repeat the
stopped estimate conditionally or after multiplication by its indicator.
It gives a finite bound depending on N,s,T. Source regularization makes
V(s) finite on {s<sigma}, so the union over N covers that event.

Choose h_0>=h large enough that h_0>1+4/d. Choose delta_0>1 with
delta_0-1<gamma and sufficiently close to 1, q_0=d(h_0-1)/2, and an
admissible p_0; the parameter discussion following Assumption 8.4
ensures such choices. Increase m to an integer strictly larger than q_0.
The source's Theorem 8.9(1), printed p. 100, says for all 0<s<T that

    P{s<sigma<T, sup_(t in [s,sigma)) ||u(t)||_(L^m)<infinity}=0.

The estimate (13), P equivalent to S^m, and the preceding localization
make that supremum finite almost surely on {s<sigma<T}. Thus
P{s<sigma<T}=0. Taking rational s,T and using sigma>0 almost surely
proves sigma=infinity. This completes the periodic Lipschitz-noise
global-existence result. Uniqueness is inherited from the source's
compatible local solutions, not reconstructed from an energy estimate.

In that parameter calculation use d>=2, as explicitly required in
Assumption 8.4. For d=1, first use its separate local theory and the
source's positive-time regularization, then lift the problem at a time
s>0 to T^2 by setting the extra derivatives and extra components of b
to zero. Bounded regularized data are admissible in the two-dimensional
local framework. The lifted coefficients and initial data are invariant
under translation in the unused coordinate. Such translations preserve
the equation with the same Brownian motions, so uniqueness implies that
the global T^2 solution remains independent of that coordinate. It is
therefore a global extension of the original T^1 local solution, by
one-dimensional local uniqueness. Parabolicity of the lift follows from
(SP) in the first coordinate and 2nu_i in the second, with margin
min(mu,min_i 2nu_i)>0. This handles d=1 without applying an assumption
labelled d>=2 at d=1.

## 9. Hostile-referee checklist and remaining gaps

* Triangularity does not imply f_i has linear positive part individually.
  The backward substitution in Section 4 is essential; it explicitly
  avoids that false inference.
* The mixed Hessian must be small relative to both diagonals. Formula
  (2), rather than a heuristic diagonal-weight argument, proves this.
* Noise covariances between species are present in (8) and (10).
* No integration by parts in b is used. Hölder b is enough for the
  energy calculation once the source's local solution exists.
* At y=0 the ratios in (4) have continuous value 0; the Hessian may
  vanish for m>2, but all terms being estimated vanish there as well.
* The reaction bound is upper-only, which is exactly what energy needs.
* Arbitrarily large polynomial weights affect constants, not the
  stopping-level limit. Uniform-in-m estimates have not been proved.
* On R^d, integrating the constant in (10) over the whole domain is
  invalid. If f(0)=0 and the solution lies in a compatible global L^m
  framework, this defect can be removed: for S<=1, local Lipschitz
  continuity gives |f(y)|<=CS, so grad P dot f<=C S^m; for S>=1,
  (7) gives the same bound. Then (10) has CP in place of C(1+P).
  The weighted cutoff argument for the energy estimate is proved in
  Section 13. The whole-space local/continuation framework and all the
  data permitted by the source wording are not fully reconciled here.
* General superlinear g adds terms of size S^(m+h-1), which (13) cannot
  bound by V. Lipschitz boundary vanishing was used crucially in (9).
  No proof or counterexample for the optimal-growth extension is given.
* The paper arXiv:2604.06645 has no stochastic transport term in its
  model. It is a literature lead and does not certify this question
  solved in print.

The exact remaining gap for the full Problem 7 is global well-posedness
on its whole-space scope without silently adding integrability or
f(0)=0 assumptions, and an answer to its superlinear/optimal reaction-
noise questions. The periodic globally-Lipschitz reaction-noise result
above is only a proper part of the full source block.

## 10. Computational and formal checks

verify_polynomial.py checks the coefficient construction with exact
rational arithmetic in 66 small-dimensional cases, including boundary
faces and the origin, and verifies transport absorption in 198 cases.
All passed. polynomial_checks.json records the outcome. Such checks are
supplementary to the general proof, not evidence for SPDE existence.

PolynomialChecks.lean contains proposed formal versions of the exponent
identity, a two-species dual-cone reaction bound, and a scalar mixed-term
absorption inequality. Its first run failed for a missing real-number
import; the corrected run was interrupted without a completed record.
It is not labelled checked. CoefficientIdentity.lean isolates the central
natural-number exponent identity with just Mathlib.Tactic.Ring.
Only an exit-code-zero run in coefficient_lean_check.txt certifies that
identity. Neither file uses sorry or native_decide. The analytic proof
and the general polynomial lemma are not formalized in Lean.

## 11. Why a diagonal energy cannot replace the construction

This is a proved obstruction to a proof method, not a counterexample to
global existence. Take two species and

    f_1(x,y)=-x y^2, f_2(x,y)=x y^2,
    R=((1,0),(1,1)), r=(0,0), g=0.

Quasipositivity holds on x=0 and y=0, total reaction is zero, and
Rf=(-xy^2,0)<=0 on the orthant. The cubic local Lipschitz bound holds
with h=3: integrate the polynomial derivative along the segment between
two points, bounding its degree-two entries by C(|u|^2+|v|^2).
All six reaction/noise assumptions are thus met.

For any m>=2 and any fixed positive a,b, let F=a x^m+b y^m. At x=1,y=t,

    grad F dot f = m t^2[-a+b t^(m-1)],
    F(1,t)=a+b t^m.

Dividing by 1+F(1,t), the ratio tends to infinity linearly in t.
Therefore no such diagonal energy has a reaction estimate
grad F dot f<=C(1+F) for this fixed system. By contrast the constructed
P satisfies P_1>=P_2 and hence grad P dot f=xy^2(P_2-P_1)<=0.
This explains why one cannot obtain the result merely by choosing
different constant weights in the source's diagonal coercivity condition.

## 12. Homogeneous reduction: arbitrary locally Lipschitz noise growth

For spatially constant initial data on the torus, the ansatz u(t,x)=U(t)
sets both spatial operators to zero, even for x-dependent b. The problem
reduces to the finite-dimensional SDE

    dU_i=f_i(U)dt+sum_n g_(n,i)(U)dW^n.

Here assume f and g are locally Lipschitz, g_i maps into ell^2, f is
quasipositive, and g_i vanishes on the orthant's face U_i=0. Suppose
sum_i f_i<=K_0+K_1 sum_i U_i, with finite nonnegative K_0,K_1. There
is no global growth restriction on g. Local existence and pathwise
uniqueness follow by truncating locally Lipschitz finite-dimensional
drift and Hilbert--Schmidt noise coefficients on compact balls; in finite
dimension the norm of g as an ell^2-valued matrix is exactly the required
Hilbert--Schmidt norm. This yields a maximal solution up to its explosion
time and the standard compact-exit criterion.

For clarity, positivity can be checked without assuming it in the mass
argument. Extend f,g to all of R^ell by evaluation at U^+, coordinatewise
positive parts. These extensions are locally Lipschitz and agree with
the original coefficients in the orthant. Let

    Z(U)=sum_i (U_i^-)^2, U_i^-=max(-U_i,0).

The C^1 function s->(s^-)^2 has absolutely continuous first derivative
and second derivative 2*1_(s<0) almost everywhere, so the generalized
Itô formula follows from smooth approximation (no atom occurs in its
second derivative and hence no Tanaka local-time term occurs). At a
negative U_i the i-th noise is zero because (U^+)_i=0. Its drift is
nonnegative by quasipositivity at that face. Therefore the i-th drift
contribution -2 U_i^- f_i(U^+) is nonpositive, its quadratic correction
is zero, and its martingale contribution is zero. Stopped on compact
balls, Itô gives Z(U(t))<=Z(U(0))=0. Thus U remains nonnegative up to
the maximal lifetime. For a direct smooth-approximation justification
at U_i=0, local Lipschitz continuity and face vanishing imply
||g_i(U^+)||<=L_N |U_i| near that face on a stopped compact set; any
quadratic correction in an epsilon-neighborhood of the corner vanishes
as epsilon->0. The drift convergence follows from local boundedness.

Let S=sum_i U_i, and let tau_N be its first hitting time of N, for
N>S(0), within the maximal lifetime. In the orthant each U_i<=S.
Before tau_N the state lies in a compact set, so the stopped martingale
in the S equation has bounded quadratic-variation density and mean zero.
It follows that for t<=T,

    E S(t wedge tau_N)
       <= S(0)+K_0 t+K_1 integral_0^t E S(s wedge tau_N) ds
       <= (S(0)+K_0 T) exp(K_1 T).                          (14)

In the first inequality, the drift integral is restricted to s<tau_N;
nonnegativity lets us replace 1_(s<tau_N)S(s) by S(s wedge tau_N).
Continuity gives S(t wedge tau_N)=N on {tau_N<=t}. Hence

    P(tau_N<=T) <= (S(0)+K_0 T) exp(K_1 T)/N -> 0.

Compact-exit explosion forces S to cross every N, because all coordinates
are nonnegative. Thus the explosion time is infinite almost surely.
For random finite initial data, apply the argument on initial sigma-field
events bounding S(0), then take their increasing union. Substitution in
the SPDE shows the homogeneous SDE defines its spatially constant
solution; uniqueness holds wherever an appropriate local SPDE theory
is available. The triangular condition is not required for this reduction.

This proves nonexplosion even for the optimal-growth superlinear noise
in the homogeneous case. It does **not** assert finite higher moments or
finite expected supremum; such moments can fail for superlinear scalar
diffusions. It does **not** prove SPDE nonexplosion for spatially varying
data, because the integral of mass does not control spatial concentration.

## 13. Whole-space energy bound when f(0)=0

This section proves an a priori estimate, conditional on having a regular
positive local solution on R^d. Specify its regularity: away from initial
time and before its lifetime sigma, the solution is locally bounded in
time with values in L-infinity(R^d), is continuous in space-time, and
has gradient in L^2(time;L^r(R^d)) locally for some r>2. These conditions
are sufficient for the weighted Itô justification below; they are stated
explicitly rather than asserted to follow from the survey's periodic
theorem for every whole-space datum. Suppose u(s) is in L^m(R^d),
f(0)=0, and the other assumptions of Sections 3--6 hold globally.

First improve (7). If S<=1, the polynomial local Lipschitz bound and
f(0)=0 give |f(y)|<=C S, while |grad P(y)|<=C_P S^(m-1). Thus
grad P dot f<=C S^m. If S>=1, (7) gives the same upper bound since
(1+S)S^(m-1)<=2S^m. Therefore, throughout the orthant,

    grad P dot f <= C P.

There is no constant source term in the energy drift.

For R>=1 set

    chi_R(x)=exp(-sqrt(1+|x|^2)/R).

It is smooth, positive and integrable, chi_R increases pointwise to 1,
and |grad chi_R|<=chi_R/R. Write V_R=integral chi_R P(u) and
E_R=integral chi_R sum_i H_ii|grad u_i|^2. On an interval where u is
globally bounded, V_R is finite. The assumed L^r gradient bound and
Holder's inequality make E_R integrable in time because
chi_R belongs to L^(r/(r-2)); the polynomial Hessian is bounded on the
stopped range of u.

The integrated diffusion term now has one extra part,

    -sum_i nu_i integral (grad chi_R dot grad u_i) P_i.

Using |grad chi_R|<=chi_R/R, Young's inequality and (4), its absolute
value is at most

    (c/2) E_R + (C/R^2) V_R,

where c is the unweighted negative-gradient constant in (10). The
pointwise transport/noise corrections require no differentiation of
chi_R or b and are the same as in Section 6. Consequently

    V_R(t)+(c/2) integral_s^t E_R
        <= V_R(s)+(C+C/R^2) integral_s^t V_R + M_R(t).       (15)

The weighted Cauchy--Schwarz calculation is unchanged: its two factors
are integral chi_R sum_i P_i^2/H_ii and E_R. The first is at most C V_R.
The weighted g term is at most Lm V_R by Euler's identity. Thus

    d<M_R>_t <= C(V_R E_R+V_R^2)dt,

with constants independent of R>=1.

For completeness, justify integration by parts and Itô on this unbounded
domain by first using chi_R times a compactly supported smooth cutoff
eta_A^2, where eta_A=1 on the ball of radius A and |grad eta_A|<=C/A.
The extra derivative of that cutoff costs at most
(c/4) integral_(A<|x|<2A) chi_R eta_A^2 sum_i H_ii|grad u_i|^2 plus
(C/A^2) integral_(A<|x|<2A) chi_R P. Both extra terms tend to zero
as A increases, by the finite weighted energy
on stopped intervals. Smooth spatial convolution gives the same local
Itô formula as in Section 8. Its convergence over R^d is justified by
global boundedness, the exponentially integrable weight, and the
weighted square-integrable gradient. First remove convolution, then
send A to infinity. These arguments prove (15), with possibly a smaller
fixed negative-gradient constant, without imposing derivatives on b.

Take a common localizing sequence for the globally bounded norms and
the gradient time integral, and localize the martingales if necessary.
The expectation-first-then-BDG proof of Section 7 now has no constant
term. Since C+C/R^2 is uniformly bounded for R>=1 and
V_R(s)<=integral P(u(s)), it gives

    E sup_(s<=t<=T wedge tau_N) V_R(t)
       <= C_T E integral P(u(s)),                          (16)

uniformly in R and N. For each fixed R, any additional martingale
localization can be removed before taking R to infinity; the common
solution localization tau_N remains. Monotone convergence (or Fatou
for the suprema) as R increases then gives

    E sup_(s<=t<=T wedge tau_N) integral_R^d P(u(t))
       <= C_T E integral_R^d P(u(s)).                      (17)

Remove N by Fatou and use bounded-initial-energy events if the initial
moment is not integrable. This proves almost sure finiteness of the
whole-space L^m energy supremum up to any finite local lifetime endpoint
under the stated regularity and integrability assumptions. The same
argument bounds the weighted gradient integrals and their limits.

A compatible whole-space L^m continuation criterion would turn (17)
into nonexplosion, exactly as in Section 8. Verifying that criterion and
the regularity assumptions for the source's unspecified whole-space
initial-data conventions remains a reduction, not a completed answer
under the source's full quantifiers. Cases f(0)!=0 need a different
solution-space convention (for example, a nonintegrable background) and
are not covered by this estimate.

## 14. Exact obstruction to extending the polynomial drift bound

Fix q>1 and set h=2q-1. Take f=0, R=I, r=0, g_1(y)=(y_1^+)^q e_1,
and g_i=0 for i>1. These coefficients are quasipositive and face-vanishing,
with zero total reaction and zero triangular reaction vector. The power
function is locally Lipschitz, and the mean-value theorem gives

    |a_+^q-b_+^q| <= q(|a|^(q-1)+|b|^(q-1))|a-b|.

Therefore this g meets the source's optimal local-Lipschitz growth with
(h-1)/2=q-1. The zero reaction meets its polynomial bound for this h.
It is a valid example for the superlinear extension, not for the original
globally Lipschitz-noise condition.

On the ray y=(t,0,...,0), t>0, our polynomial satisfies

    P(y)=theta_1^(m^2)t^m,
    H_11(y)=m(m-1)theta_1^(m^2)t^(m-2).

For a spatially constant solution all transport and Laplacian terms
vanish. Its Itô drift for P is consequently

    (1/2)m(m-1)theta_1^(m^2)t^(m+2q-2).

The ratio of this expression to 1+P tends to infinity because q>1.
Thus the central linear-in-P drift estimate (10) cannot be valid for
this optimal-growth noise, for any of our choices of weights or m>=2.
The homogeneous solution nevertheless does not explode, by Section 12.
This is a precise counterexample to an extension of the energy method,
and emphatically not a counterexample to the source's global-existence
question. A successful proof of that extension must avoid this moment
estimate or impose an additional balancing dissipativity hypothesis.
