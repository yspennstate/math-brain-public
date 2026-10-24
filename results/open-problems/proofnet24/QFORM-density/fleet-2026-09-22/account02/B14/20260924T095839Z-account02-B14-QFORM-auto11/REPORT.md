SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T09:58:39Z.
attacking: environment-coupled deterministic extreme-set localization — reduce arbitrary cap-one active marginals to arbitrary unit-measure sets globally over the conditioning environment, then test whether Gaussian regularization can preserve the three-curvature scale.

# B14 report: environment-coupled extreme localization and a BV/dilation barrier

Status: `SUPPORTING_LOCALIZATION_THEOREM_PROVED / FULL_QFORM_OPEN`. Continuity of the unrestricted output law remains separate.

## First unpaid implication

`QFORM-EXTREME-SET-WHOLELAW-RECEIVER-BEFORE-REGULARIZE-v1`: after exact deterministic extreme-set reduction, expose a matrix-geometric whole-law receiver directly on arbitrary measurable unit-measure sets before imposing any BV, diameter, fragment-count, Gaussian-scale, moment, or connected-support regularity. The environment-coupled localization below is zero-loss; the remaining debt is structural/analytic on the rough extreme sets themselves.

## 1. One-coordinate bathtub lemma

Write

K = { f:R->[0,1] measurable : int_R f = 1 }.

For every measurable h:R->[0,1],

sup_{f in K} int h(x) f(x) dx
 = sup_{|E|=1} int_E h(x) dx.                         (1.1)

Indeed, if h* is the decreasing rearrangement then the bathtub principle gives

int h f <= int_0^1 h*(s) ds.

Conversely choose a superlevel set of h at the quantile giving mass one, completing inside a level set by nonatomicity of Lebesgue measure. If the relevant quantile is not attained, the same construction gives arbitrary epsilon approximation. This uses no support bound, moment, connectedness, finite fragment count, or regularity of E.

The no-environment extreme-set reduction itself is source-known; the new point needed for this B14 role is that the choices can be coupled across an arbitrary conditioning environment rather than made separately after conditioning.

## 2. Environment-coupled product bathtub theorem

Let (Omega,tau) be any finite positive measure space, tau(Omega)=m<infinity. Let

H: Omega x R^r -> [0,1]

be measurable and define

T_H(f_1,...,f_r)
 = int_Omega int_{R^r} H(omega,x) prod_{j=1}^r f_j(x_j) dx tau(domega).

Then

boxed{
 sup_{f_1,...,f_r in K} T_H(f_1,...,f_r)
 = sup_{|E_1|=...=|E_r|=1}
   T_H(1_{E_1},...,1_{E_r}).
}                                                        (2.1)

Proof. If m=0 there is nothing to prove. Otherwise fix f_2,...,f_r and set

h_1(x_1)
 = m^{-1} int_Omega int_{R^{r-1}}
     H(omega,x) prod_{j=2}^r f_j(x_j)
     dx_2...dx_r tau(domega).

Then 0<=h_1<=1. By (1.1), for any epsilon>0 one may replace f_1 by 1_{E_1}, |E_1|=1, losing at most epsilon/r after restoring the factor m. Repeat for coordinates 2,...,r, each time using the already replaced preceding coordinates and the still-unreplaced later ones. After r steps one obtains product indicators with value at least the original value minus epsilon. Let epsilon decrease to zero. The reverse inequality is immediate because each 1_E belongs to K.

The important provenance point is that E_j is chosen from the environment-averaged partial kernel. It is a single deterministic set, not a set E_j(omega) chosen after observing omega. Hence the reduction preserves the original product law and does not create post-conditioning independence that was not present.

The result is also exactly mass-homogeneous in the environment: replacing tau by a positive submeasure of mass m simply multiplies the functional by its true mass; no normalization tax occurs.

## 3. Quadratic-form localization corollary

Let Z be any independent environment, or more generally let tau be any finite positive environment submeasure. Let B be a fixed symmetric r x r matrix and let b(z),c(z) be arbitrary measurable affine data. For every bounded open interval I put

H_I(z,x)
 = 1{ x^T B x + b(z)^T x + c(z) in I }.

Applying (2.1) gives the exact concentration identity

boxed{
 sup_{f_j in K}
 int P_f{x^T Bx+b(z)^Tx+c(z) in I} tau(dz)
 =
 sup_{|E_j|=1}
 int P_E{x^T Bx+b(z)^Tx+c(z) in I} tau(dz).
}                                                        (3.1)

Therefore, if one proves for every product of arbitrary unit-measure sets E_1,...,E_r the interval estimate

P{x^T Bx+b^Tx+c in I} <= C |I|

uniformly in b,c, then exactly the same C holds for every independent cap-one active law. For an environment submeasure of mass m the estimate is m C |I|. This is a direct interval statement; no continuity argument is needed.

For an original-coordinate split

Q(X,Z)=X^T B X+2X^T C Z+Z^T D Z,

one has b(Z)=2CZ and c(Z)=Z^TDZ. Hence arbitrary conditioning-generated affine fields, arbitrary translations, arbitrarily fragmented or unbounded outside supports, and arbitrary positive outside localization are retained with zero tax. The active extreme sets themselves may also have arbitrarily many components or unbounded support.

This is the useful B14 localization principle: reduce cap-one laws to deterministic measure-one sets only **after averaging the entire environment**, not separately on each conditioning fibre.

## 4. Fixed-source completed theorem applied to a real exact-target inequality

Let

B_* = I_3-(2/3) 11^T,

so spec(B_*)={1,1,-1}. Let C be arbitrary and D arbitrary symmetric, and form

A = [[B_*, C], [C^T, D]].

By principal-submatrix interlacing, A has at least two eigenvalues >=1 and at least one eigenvalue <=-1. Thus it lies in the exact owner target regardless of C,D.

Condition on all outside original coordinates Z. The active variables X=(X_1,X_2,X_3) remain independent cap-one variables, and

Q|Z=z = X^T B_* X + (2Cz)^T X + z^T D z.

The completed fixed-source three-dimensional theorem (Theorem A in `COUNTEREXAMPLE_SEARCH.md` at commit e5f71d79eff325201dd0274053d20268ce65b837) permits arbitrary linear terms and, because every eigenvalue of B_* has modulus one, gives

boxed{ ||p_Q||_{infty,ess} <= 6 sqrt(pi). }               (4.1)

This is uniform over C,D, all outside laws, and every active cap-one product law. By (3.1), the same inequality could equivalently be checked only on arbitrary measure-one extreme sets in the three active coordinates. Thus a completed fixed-source theorem supplies an actual target-valid inequality on the rough extreme class, not merely on compact or connected laws.

## 5. Newest account03/B14 obstruction meets the exact extreme class

The newest compatible account03/B14 report proves that a Gaussian location-scale mixture

g(x)=int phi_t(x-m) dPi(m,t),

with

M=int t^{-1/2} dPi(m,t)

satisfies

Var_BV(g) <= sqrt(2/pi) M.

Hence the normalized Gaussian-mixture hypothesis M<=sqrt(2pi) imposes Var_BV(g)<=2, and this variation bound survives weak limits.

For

E_{N,L}
 = union_{k=0}^{N-1}
   [k(L+1/N), k(L+1/N)+1/N],

f_{N,L}=1_{E_{N,L}}

has total mass one and variation 2N. The partner therefore proves that any weakly convergent Gaussian-mixture approximation to f_{N,L} must satisfy

boxed{ liminf M_j >= N sqrt(2 pi). }                      (5.1)

It also proves the quantitative L1 separation from every normalized mixture class through its BV bound. Thus even finite two-or-more-fragment members of the exact extreme class (2.1) are excluded from the weak closure of the uniformly normalized Gaussian-mixture chamber.

For an unbounded-support endpoint,

E_infty = union_{k>=1} [k^2,k^2+2^{-k}]

has measure one and infinite variation. It is itself an admissible extreme law in (2.1), so no localization theorem compatible with the owner target may silently replace the extreme class by any uniformly BV-bounded family.

## 6. Dilation cannot hide the partner's BV cost

There is a further matrix-scale obstruction. Put the same N-fragment extreme law in all three active coordinates of the reflection example in section 4. The original rough law already obeys (4.1), uniformly in N and L.

Suppose nevertheless that each active marginal is weakly approximated by Gaussian mixtures with inverse-half-variance moments M_i. By (5.1), along any such approximation

M_i >= (N-o(1)) sqrt(2 pi).

Set

a_i=M_i/sqrt(2 pi),
D_a=diag(a_1,a_2,a_3),
Y=D_a X.

The Y_i-mixtures now satisfy the normalized inverse-half-variance hypothesis, but the active Hessian becomes

B_a = D_a^{-1} B_* D_a^{-1}.

Since ||B_*||_op=1 and min_i a_i >= N-o(1),

boxed{
 ||B_a||_op <= (N-o(1))^{-2}.
}                                                        (6.1)

Consequently every eigenvalue of B_a has modulus at most (N-o(1))^{-2}. Any scalar multiplication of the quadratic output that restores three eigenvalues of modulus at least one must have factor at least (N-o(1))^2. Pulling a density bound back through that scalar multiplication loses at least the same factor.

So the fragment cost from the partner's Gaussian inverse-scale moment cannot be removed by a diagonal rescaling trick: the regularization cost reappears as loss of quadratic curvature. The original rough extreme law has the uniform source-valid bound 6 sqrt(pi), while regularize-then-normalize necessarily destroys the universal spectral scale by at least N^2. This is a proof-interface obstruction, not a QFORM counterexample.

## 7. Consequence for proof architecture

The useful reduction is now sharper. Arbitrary cap-one active laws may be reduced exactly to arbitrary deterministic unit-measure sets **globally over the conditioning environment**, so conditioning-generated translations and outside fragmentation are no longer a localization debt. But those extreme sets are intrinsically rough: they include remote finite combs with arbitrarily large BV and unbounded-support sets with infinite BV. The newest partner theorem shows that a uniformly normalized Gaussian-mixture regularization cannot even approximate them weakly, and (6.1) shows that compensating by dilation pays the missing fragmentation through the Hessian scale.

Therefore the next receiver must work directly on arbitrary measure-one sets, or aggregate/cancel their fragments jointly with matrix geometry before any regularity parameter is paid. Bounded-diameter, fixed-fragment, bounded-BV, or fixed Gaussian-scale reductions are incompatible with the full target.

## Source discipline

Fixed source freshly consumed: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, all of `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Completed Theorem A was applied in (4.1). The source-known no-environment measure-one-set reduction is not relabeled as new; the scoped contribution here is its environment-coupled product form (2.1)-(3.1) and the dilation obstruction (6.1).

Newest compatible designated partner consumed: account03/B14 `20260924T093427Z-account03-B14-QFORM-auto11`, canonical math commit `80105e9cf5c3522438505be597f46b0605f41adf`; its BV/weak-closure theorem and fragmented family were applied in sections 5-6.

Execution label remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval/readback succeeded, but genuine native receiver retrieval of the exact prior QFORM checkpoint was not established in this invocation. Model self-report: GPT-5.6 Sol. Configured reasoning effort and provider reasoning telemetry: UNKNOWN/not exposed; provider reasoning-token and pure-thinking-time fields: null.
