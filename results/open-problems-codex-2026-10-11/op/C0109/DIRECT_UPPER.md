# An explicit nonoptimal upper rate for C0109

2026-10-11, second attempt. This is a conventional written proof using
two specified published inputs. No optimality or full solution is claimed.

## Theorem

Let X be any fixed complex iid entry law with E X=0, E|X|^2=1 and
E|X|^(2+eps)<infinity, eps>0. Put e=min(eps,1) and

    beta=e/(12+4e).

For the empirical spectral measure mu_n of M_n/sqrt(n), its southwest-
rectangle distance to the unit-disk circular law satisfies, for every Q>0,

 P(d_K(mu_n,mu_circ)>C_Q n^-beta log n)<=C'_Q n^-Q

for all sufficiently large n. Constants and thresholds may depend on X,
eps,Q. In particular, under any coupling across matrix sizes, almost
surely d_K=O(n^-beta log n); every exponent delta<beta is admissible as
an almost-sure eventual polynomial upper bound. The same upper estimate
holds for E d_K. The theorem is NONOPTIMAL and does not determine the
exact dependence requested in C0109.

Definitions and the logarithmic-potential L2 bound are in SECOND_ATTEMPT.md.
In Sections A–F first put p=2+e, M=E|X|^p and gamma=e/(6+2e).
Section F proves the weaker exponent gamma/3. Section G improves it to
the theorem's stated beta=gamma/2 by localizing to derivative strips.
M>=1. The only external stochastic inputs are:

(I) Tao–Vu arXiv:0708.2895v5, Theorem 2.5, p.8, and Lemma 2.4,
p.7: arbitrarily high polynomial least-singular-value bounds under a
controlled second moment, after a fixed phase rotation, with a polynomial
deterministic shift. All uses here are for a fixed law X or its fixed
matching Gaussian law; uniformity in truncated laws is not needed here.

(II) Jalowy arXiv:2111.03595v3, Corollary 2, p.2: for a fixed all-moments
entry law with independent real/imaginary parts (or real entries),
E W_1(mu_n,mu_circ)<=C n^(-1/2+xi), for every xi>0. Only its FIXED
Gaussian-law case is used, with xi=1/4.

The linear-algebra, Gaussian count, replacement, and concentration steps
are proved explicitly below. No n-dependent high-moment theorem is used.

## A. Resolvent formulas and one-entry replacement

For A=M/sqrt(n), z complex, and 0<eta<=1 define

 F_eta(A,z)=(1/(2n))logdet((A-zI)(A-zI)*+eta^2 I),
 V_eta(A,z)=(1/n)sum_i eta^2/(s_i(A-zI)^2+eta^2).

Let H be the 2n-by-2n Hermitian dilation with off-diagonal blocks
A-zI and (A-zI)*, and R=(H-i eta I)^(-1). Then

 F_eta=(1/(2n))log|det(H-i eta I)|,
 V_eta=(eta/(2n)) Im tr R.

Indeed, H's eigenvalues are +/-s_i; these formulas follow by pairing them.
A change u in ONE raw complex entry changes H by a Hermitian matrix E
with rank<=2 and operator norm |u|/sqrt(n). It is affine along the real
line segment implementing that change. Since ||R||<=1/eta,

 |D^k F_eta[E,...,E]| <=(k-1)! |u|^k/(n^(1+k/2) eta^k),
 |D^k V_eta[E,...,E]| <=k! |u|^k/(n^(1+k/2) eta^k), k=1,2,3.

For F differentiate the real log determinant to obtain
(((-1)^(k-1)(k-1)!)/(2n))Re tr (R E)^k.
For V differentiate the inverse, yielding the trace of
(-1)^k k! (R E)^k R, multiplied by eta/(2n).
In both cases the traced product has rank<=2; its trace has absolute
value at most twice its operator norm, by the nuclear-norm bound.
These estimates hold for EVERY intervening matrix and every z, including
singular shifted matrices, because eta>0.

Taylor expansion in the two real coordinates of an entry through degree
two has remainder bounded by

    (C/n) min((|u|/(sqrt(n)eta))^3,
              (|u|/(sqrt(n)eta))^2)
      <=(C/n)(|u|/(sqrt(n)eta))^p.                         (A1)

The cubic bound is Taylor's integral third-derivative remainder along
the segment. The quadratic bound follows by writing that same remainder
as the integral of the difference between the second derivative along
the segment and its value at the base, and bounding both by the uniform
second-derivative bound. The minimum is <=t^p for 2<=p<=3, separately
for t<=1 and t>=1. Directional quadratic terms are homogeneous degree
two in Re u,Im u and thus are determined by their covariance matrix.

Let G be a centered complex Gaussian with the SAME real two-coordinate
covariance as X. Its absolute second moment is one and E|G|^p<=C_p M.
Replace entries one at a time. At each replacement the base matrix is
independent of the replaced variable; linear and quadratic Taylor terms
cancel exactly. Summing (A1) over n^2 entries gives, uniformly for ALL z,

 |E F_eta(A_X,z)-E F_eta(A_G,z)|
 +|E V_eta(A_X,z)-E V_eta(A_G,z)|
      <=C_p M n^(-e/2) eta^-p.                            (A2)

F_eta has finite expectation since its lower bound is log eta and its
upper bound grows only logarithmically with Frobenius energy. Thus all
conditional expansions and expectations are justified. V_eta is bounded.

## B. Uniform Gaussian singular-value count, including real Gaussians

For ANY deterministic complex shift D and iid G entries as above, put
A=D+G_n/sqrt(n). Then, for every u>0,

    E[(1/n)#{i:s_i(A)<=u}]<=C(u+1/n).                      (B1)

Here C is absolute because the real covariance of G has trace one.
Diagonalize this covariance by a plane rotation. One independent real
Gaussian component has variance v>=1/2; the other may be zero. Conditional
on the smaller component in one row, that row equals a deterministic
complex vector plus sqrt(v/n) times a standard REAL Gaussian vector,
up to a common phase. Multiplication by this phase does not change
distance to a complex linear subspace, and may be absorbed into its
deterministic vector.

Delete k rows, with 2<=k<n, leaving B with m=n-k rows. It has full
row rank almost surely: the determinant of any chosen square m-by-m
minor is a nonzero polynomial in the dominant real Gaussian entries
(the product of its diagonal variables has nonzero coefficient).
Conditional on its other m-1 rows, their complex orthogonal complement
has dimension d=k+1. Let P be the complex orthogonal projection onto it.
For a real Gaussian vector g, the squared norm of Pg has quadratic form
g^T(Re P)g. The real symmetric matrix Re P has eigenvalues in [0,1]
and trace d: for real x, x^T(Re P)x=x*Px lies between zero and ||x||^2,
and the real trace equals the complex trace of P.

For any deterministic translate a, a Gaussian integral by completing
the square gives

 E exp(-t||P(a+sqrt(v/n)g)||^2)
 <=det(I+(2tv/n)Re P)^(-1/2)
 <=(1+2tv/n)^(-d/2).                                      (B2)

To justify the first inequality, realify the target space and write
the norm as ||C g+b||. The Gaussian integral equals
det(I+2t C^T C)^(-1/2) exp[-t b^T(I+2t C C^T)^(-1)b];
the exponential is <=1. For the second inequality use
log(1+c lambda)>=lambda log(1+c) for 0<=lambda<=1 and sum lambda=d.

Tonelli and integral_0^infinity exp(-t a)dt=1/a give, for d>2,

 E dist(row_i,span(other rows))^-2
 <= integral_0^infinity (1+2tv/n)^(-d/2)dt
 =n/[v(d-2)]<=2n/(k-1).                                   (B3)

The negative-second-moment identity is
sum_i s_i(B)^-2=sum_i dist(row_i,span(other rows))^-2.
Proof: the diagonal entries of (BB*)^-1 are the reciprocal squared
distances, by the Schur complement of the other-row Gram matrix;
the trace of this inverse is the sum of inverse squared singular values.

Deleting k rows and singular-value interlacing imply
#{s_i(A)<=u}<=k+#{s_i(B)<=u}. Also
#{s_i(B)<=u}<=u^2 sum_i s_i(B)^-2. Therefore (B3) gives

 E[(1/n)#{s_i(A)<=u}]<=k/n+2n u^2/(k-1).

For n>=8 and u<=1/4 choose k=max(2,ceil(nu)). If nu>=2 the RHS is
<=5u+1/n; if nu<2 it is <=10/n. For u>1/4 use the trivial bound
one<=4u, and for n<8 use one<=8/n. This proves (B1).

Finally, since
eta^2/(s^2+eta^2)=integral_s^infinity 2eta^2 u/(u^2+eta^2)^2 du,
Tonelli and (B1) give

 E V_eta(A_G,z)<=C(eta+1/n)                                (B4)

uniformly in z. The integral of the kernel is one, and its first
moment is pi eta/2. Combining (A2),(B4) yields

 E V_eta(A_X,z)<=C[eta+1/n+M n^(-e/2)eta^-p].               (B5)

## C. Row concentration without higher moments

Keep Omega={|z|<=K} fixed. Replacing ONE row has rank-one effect on A,
so the singular-value interlacing proof in SECOND_ATTEMPT.md gives
|V_eta(A,z)-V_eta(A',z)|<=1/n, its scalar function being monotone with
total variation one. Thus T=integral_Omega V_eta(A,z)dz changes by at
most area(Omega)/n. The rows are independent. The bounded-differences
inequality gives

 P(T-E T>a)<=exp(-2n a^2/area(Omega)^2).                    (C1)

This inequality follows, for example, by exposing the independent rows:
the conditional Doob-martingale increments have range at most the stated
row difference; applying Hoeffding's lemma conditionally, multiplying
the exponential bounds, and optimizing the exponential parameter proves
(C1). It needs no bounded entries or entry moments.

For the potential, use upper clipping at L>=1:

 T_eta,L(A,z)=(1/n)sum_i min(.5 log(s_i^2+eta^2),
                            .5 log(L^2+eta^2)).

Its scalar range is w=.5 log((L^2+eta^2)/eta^2)<=log(2L/eta).
One-row change therefore costs at most w/n. The martingale variance
bound gives Var(T_eta,L(A,z))<=w^2/n. Equivalently, sum the squared
martingale-increment bounds; increments are orthogonal in L2.
Consequently

 E integral_Omega |T_eta,L-E T_eta,L|<=area(Omega)w/sqrt(n).

The integral of this absolute centered deviation itself changes by at
most area(Omega)w/n under one-row replacement. Applying (C1) to that
functional gives its concentration with the corresponding w factor.

For any Q, choose L=n^(Q+4). The Frobenius energy e_A has expectation
one, so P(e_A>n^(Q+2))<=n^(-Q-2). On the complementary event,
||A-zI||<=sqrt(n e_A)+K<L for all z in Omega, for large n; hence
F_eta=T_eta,L there. Deterministically, by concavity of log,

 0<=F_eta-T_eta,L<=(1/(2n L^2))sum_i s_i(A-zI)^2.

Its expected integral is <=C_K L^-2, since X is centered and
E||A-zI||_F^2/n=1+|z|^2. This also controls the difference of their
expectations. With eta=n^-gamma and any fixed gamma<1/2, the preceding
bounds imply

 ||F_eta(A_X,.)-E F_eta(A_X,.)||_L1(Omega)
      <=C_{K,Q} n^-gamma log n                            (C2)

with failure <=C_{K,Q}n^-Q, for all sufficiently large n. Specifically,
take deviation n^-gamma log n in the clipped-functional inequality;
its exponent is at least c_Q n^(1-2gamma), and its expectation is
O_Q(log n/sqrt(n)). Both are adequate for every fixed Q.

(C1) and (B5), at eta=n^-gamma with gamma=e/[2(p+1)], also give

    integral_Omega V_eta(A_X,z)dz<=C n^-gamma              (C3)

with failure smaller than every prescribed polynomial. Indeed
n^(-e/2) eta^-p=n^-gamma, and gamma<=1/8<1/2.

## D. Remove regularization using the actual least singular value

For any prescribed Q, input (I) supplies B,C so that

 P(s_min(A_X-zI)<n^-B)<=C n^(-Q-3)

uniformly in z in the fixed disk. Normalizing the raw matrix adds 1/2
to the inverse exponent and is included in B. Its deterministic shift
is sqrt(n)zI, with polynomial norm. Fubini and Markov imply that the
random set E_bad of such z has area <=n^-2 except with probability
<=C_K n^(-Q-1). No union over all z is taken.

For s>=n^-B and eta<=1, set x=eta^2/s^2<=n^(2B). The elementary bound

 .5 log(1+x)
 <=.5[1+log(1+n^(2B))] x/(1+x)
 <=C_B log n * eta^2/(s^2+eta^2)                           (D1)

follows from log(1+x)/x<=1. Therefore, on Omega minus E_bad,

 0<=F_eta-U_A<=C_B log n V_eta.

On E_bad use Cauchy–Schwarz. The NEGATIVE part of F_eta is bounded by
the negative part of U_A, because F_eta>=U_A. The positive part of
F_eta is at most .5 log(1+2e_A+2K^2+eta^2), by Jensen on its singular
values. The negative eigenvalue-log bound in SECOND_ATTEMPT.md is
sqrt(pi/2) in L2. Thus, on e_A<=n^(Q+2),

 ||F_eta||_L2(Omega)+||U_A||_L2(Omega)<=C_{K,Q}log n.

The exceptional-set integral of F_eta-U_A is at most
C_{K,Q}n^-1 log n. Combining (C3),(D1) proves

 ||F_eta(A_X,.)-U_{A_X}||_L1(Omega)
     <=C_{K,Q}n^-gamma log n                              (D2)

with failure <=C_{K,Q}n^-Q. These statements remain valid for discrete
laws: at eigenvalues the potential may be infinite, but those points have
zero planar area, and its negative logarithm is locally square integrable.

For the fixed Gaussian law, the same proof in EXPECTATION gives

 E||F_eta(A_G,.)-U_{A_G}||_L1(Omega)
     <=C_K log n (eta+1/n)+C_{K,D}n^-D.                    (D3)

Here use (B4) for the good set. On the bad set apply Cauchy–Schwarz
in probability times area, with E||F_eta||_L2^2+E||U||_L2^2<=C_K
as proved from the second moment in SECOND_ATTEMPT.md, and choose the
pointwise failure power arbitrarily large. This does not infer an
expectation bound from an event whose random constant is uncontrolled.

## E. Integrated comparison with the MEAN Gaussian potential

Denote V_G(z)=E U_{A_G}(z). It is defined as an L2(Omega) function,
by the expected L2 bound; Fubini is justified. With eta=n^-gamma,
(A2), (C2), (D2), (D3) and the triangle inequality give

 ||U_{A_X}-V_G||_L1(Omega)<=C_{K,Q}n^-gamma log n           (E1)

with failure <=C'_{K,Q}n^-Q. Explicitly the four terms are:
the X regularization error; fluctuation F_X-E F_X;
the deterministic difference E F_X-E F_G; and E F_G-E U_G.
The third is O(n^-gamma), because
e/2-p gamma=gamma. Each remaining term is O(n^-gamma log n).
This bound controls all compact smooth tests simultaneously via
Delta U=2pi mu, without a grid-dependent union bound.

## F. Compact smoothing to the source's UNIFORM rectangle metric

Choose K=8. Let chi be a fixed C_c^infinity function taking values in
[0,1], equal to one on [-4,4]^2 and supported in [-5,5]^2.
Let psi be smooth, nondecreasing, zero on (-infinity,0], one on [1,infinity).
For h in (0,1] and every real s,t set

 f^-_{s,t}(x,y)=chi(x,y)psi((s-x)/h)psi((t-y)/h),
 f^+_{s,t}(x,y)=chi(x,y)psi((s+h-x)/h)psi((t+h-y)/h).

All supports lie in Omega, their Laplacian sup norms are <=C h^-2,
and Lipschitz constants <=C h^-1, uniformly in s,t. They satisfy
f^-<=1_{Q(s,t)} everywhere and f^+>=1_{Q(s,t)} on [-4,4]^2.
For the circular law their integrals differ from mu_circ(Q(s,t)) by
at most C h, because its real/imaginary marginal densities are bounded
by 2/pi and only two strips of width h occur.

On event (E1), integration by parts gives, SIMULTANEOUSLY for every
compact C2 f supported in Omega,

 |mu_X(f)-E mu_G(f)|<= (||Delta f||_infinity/(2pi))
                         C_Q n^-gamma log n.

The two real coordinates of the matching Gaussian become independent
after a fixed common phase rotation, or the law is purely real after
rotation. Input (II) therefore applies to that rotated fixed law. W_1
and the disk circular law are rotation invariant, so

 |E mu_G(f)-mu_circ(f)|<=Lip(f) E W_1(mu_G,mu_circ)
                         <=C Lip(f)n^-1/4.

To control exterior mass, choose a second fixed cutoff chi_0 in [0,1],
equal to one on [-2,2]^2, supported in [-3,3]^2. Since mu_circ(chi_0)=1,

 mu_X(C\[-4,4]^2)<=1-mu_X(chi_0)
                 <=C_Q n^-gamma log n+C n^-1/4.

Apply the upper/lower test bounds to every rectangle and add this exterior
mass only on the upper side. Taking the supremum yields

 d_K<=C_Q[h+h^-2 n^-gamma log n+h^-1 n^-1/4
                +n^-gamma log n+n^-1/4].

Set h=n^(-gamma/3). Since gamma<=1/8, the Gaussian terms are smaller
than n^(-gamma/3). This proves d_K<=C_Q n^-beta log n, beta=gamma/3.
The probability bound is the same event (E1); no additional random
choice of s,t or uncountable union is involved.

Take Q=2 and use Borel–Cantelli to conclude the almost-sure eventual
bound for arbitrary cross-size coupling. Since d_K<=1, the high-probability
bound also implies E d_K<=C n^-beta log n by bounding it by one on the
bad event. Logs can be absorbed for every delta<beta. This completes
the nonoptimal-rate proof.

## G. Improved rectangle exponent by localizing the potential estimate

This section strengthens the exponent gamma/3 just proved to gamma/2.
Keep the same eta=n^-gamma and take the fixed disk radius K=20 so that
all cutoff supports and covering strips below lie inside Omega.

**Local version of (E1).** Fix rho>0. For any deterministic measurable
S subset Omega with area a>=n^-rho (and a<=area(Omega)), and any Q>0,

 P(||U_X-V_G||_L1(S)>C_{K,rho,Q} a n^-gamma log n)
      <=C'_{K,rho,Q}n^-Q,                                 (G1)

where constants are UNIFORM over these sets S, which may depend on n.
Here is the full modification of the proof, to track the factor a:

- (A2),(B4),(B5) are pointwise uniform in z, so their expectations
  integrated over S are multiplied by a.
- Both row bounds in Section C are pointwise. The change of the
  integrated V statistic is a/n, and the change of the clipped-potential
  absolute-deviation statistic is a w/n. Their expectation bounds are
  respectively C a n^-gamma and a w/sqrt(n). Use deviations a n^-gamma
  and a n^-gamma log n. The factor a cancels from the bounded-differences
  exponential inequalities; failure powers and constants stay uniform.
- Upper clipping's expected error is <=C_K a L^-2, and the one global
  energy event used in C2 implies equality to the unclipped potential
  over ALL of Omega, hence also over S.
- For regularization removal, take the pointwise least-singular failure
  exponent Q_0>Q+rho+2. Its bad-set expected area IN S is <=C a n^-Q_0.
  Markov gives bad area <=a^2 n^-2 except with probability
  <=C a^-1 n^(-Q_0+2)<=C n^(-Q_0+2+rho)<=C n^-Q.
  The global L2 potential bound on the energy event is O_{K,Q_0}(log n).
  Cauchy–Schwarz on this smaller bad set therefore gives
  O_{K,Q_0}(a n^-1 log n), preserving the factor a. On the good set
  (D1) and the concentrated integral of V give O(a n^-gamma log n).
- For the D3 Gaussian EXPECTATION step, use the global expected L2
  bound and bad-area expectation C a n^-Q_0. Cauchy–Schwarz gives
  C sqrt(a)n^(-Q_0/2). Because a>=n^-rho, this is <=C a n^-D when
  Q_0>=2D+rho. Choose D=1, or larger, and choose Q_0 to satisfy both
  requirements. The good Gaussian integral is C a log n(eta+1/n).

All shifts remain in the fixed disk. Constants in the inverse theorem
depend on Q_0 but not S or its area. Combining these statements proves
(G1) with exactly the same four-term decomposition as Section E.
This completes the local lemma, rather than assuming an L1 bound on
Omega automatically scales with the area of a subset.

**Finite covering of the derivative strips.** Set rho=gamma/2 and
h=n^-rho. The cutoffs chi,chi_0 and tests f^+,f^- are exactly those of
Section F. For all large n, h<=1/4. Include the vertical strips

 S_m=[m h,(m+3)h] x [-6,6]

for every integer m whose left endpoint lies in [-7,7], and also their
horizontal transposes. They lie in Omega when K=20 and have area 36h,
so meet a>=n^-rho. There are at most C/h=C n^rho such strips.
Apply (G1) to each with requested failure exponent Q+rho+2; union bound
and the global event (E1) give a single event with failure <=C_Q n^-Q
on which EVERY covering strip satisfies

    ||U_X-V_G||_L1(S_m)<=C_Q h n^-gamma log n,              (G2)

and the global L1 bound also holds. This is a deterministic grid with a
polynomial number of sets, not a union over random thresholds.

For any s,t, the nonconstant transition of each psi factor is on a
coordinate interval of length h. If it meets [-5,5], that interval is
contained in one of the width-3h covering strips, by taking the floor
of its left endpoint divided by h. Other transitions do not contribute
on the support of chi. Write g for the product of the two psi factors.
Product differentiation gives

    Delta(chi g)=(Delta chi)g+2 grad chi dot grad g+chi Delta g.

The first term is uniformly O(1) on Omega. Each derivative of g is
supported in the corresponding vertical or horizontal transition strip;
first derivatives are O(h^-1), second derivatives O(h^-2). There is no
mixed partial in the Laplacian. Since h<=1,

 |Delta f^+/-(z)|<=C[1+h^-2(1_{S_v}(z)+1_{S_h}(z))]

for covering strips S_v,S_h chosen from the finite family when a
transition is present. Consequently (E1),(G2) imply, SIMULTANEOUSLY
for all thresholds,

 |mu_X(f^+/−)-E mu_G(f^+/−)|
       <=C_Q h^-1 n^-gamma log n.                         (G3)

The fixed cutoff chi_0 uses only the global estimate. All deterministic
Gaussian test bounds and circular strip-mass errors are unchanged from F.
Repeating its upper/lower rectangle comparison now gives

 d_K<=C_Q[h+h^-1 n^-gamma log n+h^-1 n^-1/4
                 +n^-gamma log n+n^-1/4].

With h=n^-gamma/2 this is C_Q n^-gamma/2 log n. Since gamma<=1/8,
1/4-gamma/2>=3/16>gamma/2, so the Gaussian error is smaller.
Thus beta=gamma/2=e/(12+4e), as stated in the theorem. Summability and
expected-distance conclusions follow exactly as at the end of Section F.

## Remaining gap and referee-sensitive points

The proved upper exponent e/(12+4e) is far below the earlier necessary
bound 2eps/(2+eps), and neither is asserted sharp. The plateau at e=1
is a limitation of the second-order replacement argument, not a claim
about the optimal curve. The optimal dependence remains unresolved.

The most sensitive steps were checked explicitly: the Gaussian projection
can be COMPLEX while its dominant Gaussian component is REAL (B2 handles
this); high entry moments are not used for row concentration; all cutoff
and area exceptions have summable prescribed failure bounds; matrix
normalization is included in the least-singular-value exponent; no theorem
for a moving entry distribution is inserted; smooth tests are simultaneous
on one L1-potential event, including exterior tightness. Formal checks are
limited algebraic auxiliaries, not a Lean proof of this stochastic theorem.
