# Independent checks and attempted failures

## 1. Capacity input

The independent recheck of round 5 is in LOG.md: random shifted sampling
replaces cell averaging for the upper sandwich, and the Fourier symbol
of the tent interpolant replaces its cube-wise Jensen calculation for
the lower sandwich. The mass multiplier (2+cos theta)/3 lies in [1/3,1].
The lattice and continuum energies both carry the SRW factor 1/6.
The half-cell enlargement is still required for the sampling proof:
every possible x+z with x in B_R must lie in the region where F=1.

The six-face decrement was recomputed using one fixed amplitude. The
total variation energy is 16 and its negative cross term is at least
216 pi C/(24+16 pi)^2. Dividing the optimized decrement by 6 gives
216^2/(16*6)=486, exactly the earlier coefficient. No numerical
evaluation is involved.

## 2. Boundary covariance by matrix algebra

The proof uses last exit. A second check, once G_K e_K=1 is known,
is direct matrix algebra. For S>=R, the cross matrix G_(B_R,B_S)
satisfies G_(B_R,B_S)e_S=1_(B_R). Therefore

    Cov(M_R,M_S)=e_R^T G_(B_R,B_S)e_S=e_R^T1=a_R.

Also Var(M_R)=e_R^T G_(B_R)e_R=a_R. Thus an increment has variance
a_S-a_R, not 1/a_R-1/a_S. The normalized harmonic averages H_R=M_R/a_R
instead have covariance

    Cov(H_R,H_S)=1/a_S, S>=R.

They are not a forward martingale for F_R. Confusing M_R with H_R
would reverse the time direction. The constant-shift Gaussian mode in
a fixed box is H_R, while the forward boundary score is M_R.

Each covariance of M_S-M_R with a field coordinate in B_R is zero.
Joint Gaussianity makes this independence of the whole finite vector,
not merely orthogonality to M_R. This validates the filtration used
for independent increments in the artificial construction.

## 3. Signs, second derivatives, and the root in the endpoint bound

For one Gaussian coordinate X of variance sigma^2 and event {X>=h},
the score is X/sigma^2. The exact ratio is
Q((h+t)/sigma)/Q(h/sigma), which decreases as t increases. Equation
(13) has the negative sign -t M_R and recovers this ratio exactly.
The opposite sign would fail this one-coordinate test.

A second derivation of (3) expands (13) at t=0. Its log is

    -a_R t^2/2 + log E[exp(-t M_R)|A_R(h)].

The first two derivatives are -E[M_R|A_R(h)] and
Var(M_R|A_R(h))-a_R. Thus m_R'=a_R-Var, in agreement with the direct
density differentiation in PROOF.md. Only an upper bound on m_R'
follows; taking an absolute value here would be unjustified.

Integrating m_R'(h)<=a_R gives the endpoint upper bound on the nearby
score. Integrating it a second time reproduces (16), independently of
Jensen. This checks both the coefficient 1/2 of the quadratic loss and
the fact that an endpoint bound suffices.

For the constant in (5), write y=sqrt(kappa c). The threshold equation
is y^2+2My-2 log 2=0. Completing the square gives
y=sqrt(M^2+2 log 2)-M. Rationalizing gives the independent expression

    c = (2 log 2)^2 /
        [kappa (sqrt(M^2+2 log 2)+M)^2].

This is positive for every finite M>=0. At M=0 it is 2 log 2/kappa;
for large M it is asymptotic to (log 2)^2/(kappa M^2). Both checks
agree with the linear-plus-quadratic loss. This is a conditional bound,
not a value for the actual arm radius.

## 4. Residual path threshold

The residual covariance g(x,y)-1/a_R is positive semidefinite because
it is the covariance of phi-H_R, not because subtracting a positive
matrix preserves positive semidefiniteness in general. Its deterministic
charge constraint explains its degeneracy.

Only a fixed-R decomposition is asserted. The residual fields psi_R
at different R are not asserted to be mutually independent. No such
independence is used in either the path formula or the sparse-radius
construction.

Every path can be reduced to a simple path and stopped at the first
boundary vertex. The collection is finite, so its maximum bottleneck
is an ordinary finite random variable. The common additive H_R can be
pulled through every minimum and the outer maximum. This gives the
event identity before any differentiation. Conditioning on psi_R and
integrating one Gaussian tail checks both formulas (18).

## 5. Probability lower bound without positive association

The proof uses association, derived there from independent increments.
There is a separate lower-bound argument using only independent
increment probabilities. Let a_j=a_(R_j), and r_j=a_(R_(j-1))/a_j.
By (1) and the spacing of R_j, r_j tends to zero. Choose j0 large
enough that r_j<1/2 for all j>=j0.

There is a fixed positive-probability event E0 on B_(R_(j0-1)) on
which all its field coordinates exceed a sufficiently large constant.
Since all equilibrium weights are nonnegative, this ensures every
earlier threshold in (23), and M_(R_(j0-1))>0. Its probability is
positive by finite Gaussian nondegeneracy. It is independent of all
later increments W_j.

For j>=j0 require the stronger independent conditions

    W_j >= b_j sqrt(a_j).

All these increments are positive. Induction gives M_(R_j)>=W_j,
so E0 and these conditions imply D_(R_n). Therefore

    P(D_(R_n)) >= P(E0)
        product_(j=j0)^n Q(b_j/sqrt(1-r_j)).

By (25) the negative log of the jth factor is at most

    2 ell_j/(1-r_j)
       +log(1+b_j/sqrt(1-r_j))+log(1/c0).

Since r_j tends to zero, its leading coefficient is 2+o(1).
For any eta>0 the leading sum is bounded, after a fixed starting
index, by (2+eta)sum ell_j. The logarithmic remainder is
O(n+n log ell_n)=o(ell_n); earlier fixed terms are negligible.
Equation (22), followed by eta decreasing to zero, gives exactly
log(1/P(D_(R_n)))<=(2+o(1))ell_n again.

This check does not assume independence of the M_(R_j) themselves;
those variables are correlated. Only their increments are independent.

## 6. Half-ratio upper bound through a Gaussian bridge

There is a second route to (27), independent of applying the
multidimensional likelihood directly. Fix n and put

    Z=M_(R_n)/sqrt(a_n),
    Y_j=M_(R_j)-(a_j/a_n)M_(R_n), j<=n.

By (2), all Y_j are independent of Z, and Y_n=0. Given the bridge
vector Y, every inequality in D_(R_n) is a lower bound on Z. Their
intersection is

    Z>=C(Y),
    C(Y)=max_(j<=n) [(b_j sqrt(a_j)-Y_j)sqrt(a_n)/a_j].

The last term is b_n, so C(Y)>=b_n. Translation of phi by -t shifts
M_(R_j) by -a_j t. Thus it leaves every Y_j invariant and shifts Z
by -t sqrt(a_n). Conditional probabilities are consequently Q(C(Y))
and Q(C(Y)+s), where s=t sqrt(a_n).

For any real c and s>=0,

    Q(c+s)=integral_c^infinity exp(-sz-s^2/2)varphi(z)dz
           <=exp(-sc-s^2/2)Q(c).

Use c=C(Y)>=b_n and average over Y. This recovers precisely (27).
The construction therefore supplies an upper bound on an actual
probability ratio, not just a large derivative at one point.

## 7. The coefficient 8 and the liminf quantifier

Here is a scale calculation separate from the proof's substitution.
If a Gaussian half-space threshold has b^2=2 rho log R and its
translation displacement is s=t sqrt(kappa R), then the tail loss
is approximately b s. A half-ratio has b s=delta=log 2, giving

    t^2 R = delta^2/(2 rho kappa log R).

Also log(1/t) is asymptotic to (1/2)log R. Hence

    t^2 log(1/t) R tends to delta^2/(4 rho kappa).

Taking rho=2 gives delta^2/(8 kappa). In the construction,
b_n^2=4 log R_n exactly, so this matches (28).

The universal lower bound applies to every R, including the long gaps
between selected radii: P(D_R)=P(D_(R_n)) there, and log R>=log R_n.
The upper bound for L_D is only along t_n. That is enough to match
the universal liminf. No limit or asymptotic equivalence for L_D(t)
at every t is claimed. Nor does P(D_R) have to have a logarithmic
exponent: its probabilities are constant through long intervals.
At the selected radii their logarithmic exponent is 2, because
P(D_(R_n))<=Q(b_n)<=R_n^(-2), complementing (26).

Finiteness of L_D for every t>0 follows from (27) as n grows, without
any subcritical theorem. Finitely many small radii, including those
with D_R equal to the whole space, cause no issue for the lower bound:
their translated ratios tend to one, and for whole-space events are
identically one. Floors have vanishing scaled error.

## 8. Limits of the obstruction

The D_R are not events of paths exceeding a common height. They are
tests of equilibrium-weighted boundary averages, with deterministic
radius-dependent thresholds. They meet the precise broad structural
assumptions tested in the proof, but no extra geometric assumptions.
The construction therefore obstructs an inference from those broad
assumptions; it does not obstruct a stronger result for lattice arms.

The endpoint mean bound (4), or equivalently a uniform bound on the
ratio in (18), remains an actual missing geometric estimate. No claim
of novelty of the Gaussian martingale, the score identity or the
sparse construction is established. No numerical workload was used.
