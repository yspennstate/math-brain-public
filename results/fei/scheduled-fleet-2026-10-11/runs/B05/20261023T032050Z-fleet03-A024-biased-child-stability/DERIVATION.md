# Hereditary physical-query repair, A024 v4

All logarithms in entropy are base two; influence is the uniform physical-cube
influence. These are author proofs, pending independent reconstruction.

## 1. The hereditary class and a dimension-free pivot

Let q be an arbitrary polynomial of degree at most two over F_2 on D physical
bits. Let f(x)=(-1)^q(x), with optionally its value flipped at one specified
vertex. Fair coordinate restrictions preserve this class: substitute the fixed
bit in q; the edited vertex either disappears or projects to one vertex.
No conditioning on an inner output is being performed.

If the quadratic part is nonzero, select a coordinate incident to a quadratic
monomial. Its derivative in the unedited phase is a nonconstant affine phase,
so its influence is exactly 1/2. A single edited vertex changes the pivotal
status of just its incident edge in this direction, and hence changes influence
by at most 2^(1-D). For D>=3 the selected influence d is at least 1/4.
For any Boolean function B_i=H(S_i|S_{-i})<=h_2(d)<=1. Consequently B_i<=4d.
For D<=2 every positive influence is at least 1/2, so B_i<=2d;
if d=0 the spectral coordinate is deterministic and B_i=0.

If q is affine, multiplication by its character translates the squared Fourier
law on subsets. Translation preserves B_i, but it does NOT preserve influence:
it either preserves d or replaces d by 1-d. For a single point defect set
u=2^(1-D). Its empty Fourier coefficient is 1-u and every other coefficient has
magnitude u. Pairing subsets with and without i gives exactly

    B_i = 2u(1-u) + L(1-u,u),
    L(a,b)=e(a^2)+e(b^2)-e(a^2+b^2), e(s)=-s log_2 s.

The previously proved scalar estimate L(a,b)<=2|ab|/ln 2 follows by
ln(1+s^2)<=s: the derivative of s-ln(1+s^2) is (s-1)^2/(1+s^2).
Since ln 2>2/3 (its positive atanh series starts with 2/3),

    B_i <= (2+2/ln 2)u(1-u) <= 5d(1-d) <= 5d.

This includes D=1, character-cancelled constants and both deterministic limits.
D=0 is constant. With no edit an affine phase has B_i=0.
Thus every restriction of this class has a complete physical continuation tree
whose selected nodes satisfy B_i<=5d_i, independently of D. If its quadratic
part survives use an incident coordinate; otherwise use any remaining coordinate.

## 2. Products, actual activation, and biased outputs

Allow each of w and h to be any product of such phases on disjoint physical
blocks, with unbounded block widths and any finite number of factors. Tensor
product of squared Fourier laws preserves the coordinate conditional entropy
and coordinate influence in its factor. After ANY fair physical adaptive history
the two residual functions still have this product structure (constant factors
are harmless). Choose a coordinate using the policy above in either residual
block. This is an actual uniform remaining-cube query.

For F=1-(1-w)(1-h)/2 and a w coordinate let r=Pr(h=-1),
a=Ew and beta=(Ew_0-Ew_1)/2. The v3 exact transport is

    d_F=r d_w, B_i(F)=r B_i(w)+R_r(a,beta),
    R_r=L(1-r+ra,r beta)+r(1-r)L(1-a,beta)-r L(a,beta).

Dropping only the last, nonpositive term and applying the scalar L estimate,
|1-r+ra|<=1, |1-a|<=2 and |beta|<=d_w gives
R_r<= (6/ln 2)r|beta|<=9r d_w. Therefore every selected actual
continuation query obeys B_i(F)<=14d_i(F). The h-coordinate case is symmetric.
When r=0 the function is constant on that block; when r=1 it is w.
No division by variance or mean is used, so near-dictator and deterministic
limits need no unpaid log(1/r). Changes in output means induce biased outer
inputs; physical coordinates remaining after the history stay uniform.

The corrected FEI+ quantity is sum over nonempty S of
p_mu(S) log_2(product_{i in S}(1-mu_i^2)/p_mu(S)); no output-variance
numerator is present. Deterministic inner outputs are contracted before a
biased orthonormal basis is used. This proof uses the physical uniform
identities instead of introducing that basis.

There is also no binary-fan-in restriction on this corollary. For any finite
number of disjoint inner functions w_j of this product class, form their OR
(+1 is the absorbing value). At a query in w_j, group ALL other inner functions
as h=OR_{k!=j} w_k. The v3 transport needs no structural hypothesis on h:
only its mean enters R. Hence the same B_i<=14d_i holds, with
r=product_{k!=j} Pr(w_k=-1). Arbitrary fan-in costs no additional factor.
For zero other functions h=-1 and r=1. Deterministic absorbing inputs give a
constant leaf. Input/output sign flips also give the analogous AND statement.

## 3. Exact scope of the history transfer and credit

Fix ANY already executed physical stopping prefix, with its original leaf
reaches p_l. At every nonconstant leaf run the new continuation policy. At
threshold K=14 its additional bad-node odd-face bill is identically zero.
The completed bad-node bill is EXACTLY the bill already booked in the prefix.
No old credit is renewed, no prefix debit is erased, and no old fixed-tree
potential identity is asserted for the reordered continuation.

The localized B05 reduction (constant leaves, c_JS=2/ln 2) gives

    H(F_l) <= (14+2/ln 2) I(F_l) <= 17 I(F_l).

For a single product the corresponding bound is H(w)<=8I(w). The numerical
relaxations to 17 and 8 are strict when the corresponding influence is positive;
constants have equality zero throughout.
Both actual terminal functions at every binary split are retained until this
continuation resolves their FULL entropies. Precisely, prefix telescoping is

    H(F)=sum_prefix p_v [H(F_v)-(H(F_v0)+H(F_v1))/2]
         + sum_leaves p_l H(F_l),
    I(F)=sum_prefix p_v d_v + sum_leaves p_l I(F_l).

These are equalities; no leaf entropy is discarded. The continuation entropy
bound spends only the remaining influence. Any pre-existing valid bank R with
booked debit U keeps the SAME R and U because the extra bad bill is zero.
This does not prove a bound on a nonzero prefix debit U, or convert an old Phi
into a new-tree Phi. In particular the v3 raw root-Phi obstruction survives.

## 4. First unsupported line for the universal bridge

The hereditary pivot lemma does not apply to an arbitrary Boolean residual.
For a general edit event E, changing a quadratic phase changes a coordinate
influence by at most Pr[E(x) differs from E(x^i)]<=2 Pr(E).
This supplies a large pivot when the density is small, but density can grow
under restrictions. More decisively, once the quadratic part vanishes, the
point-defect formula has no justification for a general edit set. Taking the
base phase constant would include EVERY Boolean function. An assertion that
this residual always admits a uniformly good continuation is the first
unsupported universal step. There is no FEI proof or disproof here.
