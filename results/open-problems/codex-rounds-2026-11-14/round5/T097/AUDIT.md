# Checks and attempted failures

## 1. Interpolation constant by a second method

The proof uses Jensen's inequality. An independent local matrix
calculation gives the same factor. The two linear basis functions on
[0,1] have Gram matrix

    M = [[1/3,1/6],[1/6,1/3]].

Its eigenvalues are 1/2 and 1/6, on the constant and alternating vectors.
For a derivative in one coordinate, the four edge increments form a
vector d on a square. The integral of its squared bilinear interpolant
over that square is

    d^T (M tensor M) d <= (1/4) d^T d.

This reproduces (7). Each oriented edge occurs in four unit cubes,
giving net factor one. A derivative is independent of its own coordinate,
whose integration contributes length one. There is no extra factor two
from unoriented edges: each edge is already counted exactly once in
sum_x sum_i (f(x+e_i)-f(x))^2.

As a separate normalization test, take f to be one at the origin and
zero elsewhere. Its lattice energy is 6/6=1. Its trilinear interpolant
is beta(y_1)beta(y_2)beta(y_3), where beta(v)=(1-|v|)_+.
Its continuum gradient energy is 3*2*(2/3)^2=8/3, so the normalized
energy is 4/9<=1, consistent with the direction of the transfer.

## 2. Taking the two infima

A lattice trial function f=1 on B_R need not be monotone or nonnegative.
The interpolation argument does not use either property. It equals one
throughout Q_R because all eight vertices of every interior unit cube
belong to B_R. Continuity handles the boundary. Its support may grow by
one cell; it is still compact, so no decay approximation is needed.

For the reverse direction, the union of all closed cells centered at
B_R is precisely Q_{R+1/2}. Thus the enlargement is geometric, not a
discretization error estimated after a limit. Omitting the half-cell
would fail at boundary vertices. Averaging a compactly supported
continuum trial function gives a finitely supported lattice trial
function.

The proof establishes equality, not just one inequality, in the lattice
Dirichlet variational formula. Finite-box minimizers supply admissible
functions with energies tending to cap(K). Without this step, infimizing
the reverse transfer would not identify the lower bound on capacity.

The same continuum class is used in both directions. It is the class of
compactly supported Lipschitz functions exactly one on the cube. There
is no appeal to an equilibrium potential in another function space.
Scaling gives exactly a*kappa because the volume factor is a^3 and
the squared gradient factor is a^(-2).

These observations give independently the interval

    1 <= cap(B_R)/(kappa R) <= 1+1/(2R),

which is valid for every integer R>=1. The error is nonnegative and
bounded, not merely o(R). It is not asserted to tend to a constant.

## 3. Face perturbation and the coefficient 486

The six open supports are disjoint: a point in one has one coordinate
of magnitude greater than one and both other coordinates of magnitude
less than one. It cannot lie in a second open support. Their boundary
intersections have zero three-dimensional measure. No cross term in
the gradient norm has been discarded on a set of positive measure.

An independent rescaling check of the tent integrals uses
alpha(s)=beta(2s-1). Thus

    integral alpha=(1/2) integral beta=1/2,
    ||alpha||_2^2=(1/2)||beta||_2^2=1/3,
    ||alpha'||_2^2=2||beta'||_2^2=4.

Direct integration on the two halves of [-1,1] gives
||beta||_2^2=2/3 and ||beta'||_2^2=2. Therefore the normal derivative
contributes 16/9 on each face and the two tangential derivatives together
contribute 8/9. The face total is 8/3; six faces give H=16.

The sign of the cross term can be checked without a three-dimensional
integration by parts. On a face the distance profile is u(s) and has
no tangential derivative. Its cross term is integral u'(s)alpha'(s) ds.
The endpoint values of alpha vanish, leaving
-integral u''(s)alpha(s) ds<0. The kink in alpha does not change this:
alpha is absolutely continuous and u' is smooth on [0,1].

On that interval S'(s)>=12 pi and S(s)<=D=24+16 pi. With J^(-1)=6C,
the six-face bound is

    I >= 36 pi/(J D^2) = 216 pi C/D^2.

To check the final numerical factor independently of optimization, use
the fixed limiting perturbation amplitude

    b = 27 pi C/(2D^2).

The limiting normalized energy is bounded above by

    C - b*(216 pi C/D^2)/3 + 16 b^2/6
      = C - 972 pi^2 C^2/D^4 + 486 pi^2 C^2/D^4
      = C - 486 pi^2 C^2/D^4.

For each finite T the same fixed b is admissible; its energy converges
to the displayed expression. This recovers C_1 without choosing the
T-dependent minimizing amplitude in PROOF.md.

The normalized decrement mu=486 pi^2 C^2/D^4 has the correct scaling:
at cube half-side a the base energy, cross term and perturbation energy
all scale by a. Its sign is positive. For a magnitude check, C<3,
D>16 pi and pi>3 give

    mu/C < 1458/(65536*pi^2) < 1/400.

The last comparison is the integer inequality
1458*400=583200<589824=65536*9. Thus the explicit improvement is small
and cannot plausibly change a power law. No decimal value is asserted.

## 4. Admissibility at the two boundaries and at infinity

The perturbation vanishes at s=0, hence on the cube boundary, as well
as at s=1 and on its tangential boundaries. Adding it creates no jump.
The trial functions remain globally Lipschitz, including across edges
and corners. Their values may exceed one outside the cube; this is
allowed by the variational definition. Clipping to [0,1] would preserve
the condition and decrease energy.

The infinite distance profile is used only to calculate a limit. For
every T>1 the actual trial function is compactly supported and its
energy is computed first. Its derivative on the perturbation support
is exactly -1/(J_T S(s)), so the cross term converges with no tail error.
The base energy 1/J_T also converges. No existence of a continuum
minimizer or density theorem for Sobolev functions is needed.

The lower magnitude bound kappa>=2 pi/3 can be checked against the
continuum unit ball: its exterior profile 1/r has gradient energy
4 pi. Every cube trial function is also a unit-ball trial function,
so the lower bound has the right normalization and sign.

## 5. Percolation coefficient by a second method

The proof uses optimized Holder. Gaussian likelihood-ratio rearrangement
instead gives p_R(h+t)>=Q(z+s), where Q(z)=p_R(h) and
s=t sqrt(cap(B_R)). For p_R(h_*)<1/2 one has z>=0. Jensen and the
normal Mills bounds give

    Q(z+s)/Q(z) >= exp[-s^2/2-s(z+2)],
    z <= sqrt(2 log(1/p_R(h_*))).

At R<=c/(t^2 log(1/t)), put H=log(1/t). The uniform leading bounds are

    s^2 <= kappa c/H+O(t^2),
    log(1/p_R(h_*)) <= (4+2epsilon)H.

Hence the leading loss is sqrt(4 kappa c(2+epsilon)). Its limit as
epsilon decreases to zero is sqrt(8 kappa c). The half-ratio threshold
therefore gives exactly (log 2)^2/(8 kappa), as in the Holder proof.

Finitely many small radii, the integer floor and finiteness of the first
half-ratio radius are handled separately in PROOF.md. No monotonicity
of that ratio in R or critical nonpercolation is used. Only q>4 from
the density theorem is used.

## 6. Conclusions the estimates do not support

The actual coefficient kappa in capacity is identified, but the bound
for L_rel is not proved optimal. The Gaussian sensitivity estimate still
has sqrt(log(1/p_R)) in it. Substitution of R=c*t^(-2) leaves a growing
loss, so this argument still does not give L_rel>=c*t^(-2).

No comparison with an ordinary crossing or two-point correlation length
has been supplied. No value or existence of a lattice critical exponent
follows from the capacity limit. The interpolation statement may be a
standard fact; novelty of it or of the explicit face variation has not
been established. No numerical workload or mathematical script was run.
