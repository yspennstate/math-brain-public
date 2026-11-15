# Piecewise certified three-state regular-tree cutoff: d >= 156

Claim T067-PIECEWISE-D0-001, version 3. Status: proof (unaudited).
No novelty or priority assertion. All previously submitted versions are unchanged.

For every integer d>=156 and every 0<lambda<=1/sqrt(d), the uniform-root
ferromagnetic symmetric three-state Potts broadcast on the regular d-ary tree
is nonreconstructible, including equality in the Kesten--Stigum bound.
The known strict-KS reconstruction direction is literature, not a new claim.
This leaves regular degrees 5..155 and all unaddressed q=4/GW cases open.

The hardest new pieces are (A) extending the signed replacement constants
beyond L=1/16, and (B) a global Gaussian curvature estimate permitting a
piecewise finite comparison. Part C is an exact finite certificate; Part D
proves canonical entry and composes the result. No particle simulation,
sampled gap, or fitted moment ceiling is used.

Dependencies, all version 1: SOFTMAX-DERIVATIVES, CUBIC-FUSION,
TERNARY-MOMENTS (F2), UNIFORM-LOCAL, RESCALE identity (R) only, FIXEDPOINT and GAUSSIAN-QUAD.
Their full claim ids have prefix T067- and suffix -001. Audit receipts must be
consulted individually: separate w683 receipts under the exact RESCALE and
GAUSSIAN-QUAD claim ids were not located. The lead analytic audit rederives
those two elementary arguments. No blanket two-audit assertion is made.
Part A restates the detailed proof of SHARP-LINDEBERG v1 parametrically;
every occurrence of L is retained, rather than importing its L=1/16 conclusion.
The pending GAUSSIAN-SMALL-GAP theorem is NOT a premise: only its saved
s=1/10 raw enclosure is independently checked with the quadrature lemma.
Exact proof/source/data hashes are in checks/piecewise156_submission.json.

## Part A. General-L one-sided comparison

Let mu be an S3-invariant probability law on the three-state simplex, with
uniform root and calibrated posterior p. Put a=3p-1, A=||a||^2, J=sum_i a_i^3,
M=EA=9x, U=EA^2, and T=EJ. Suppose T>=0. For integer d>=1 and
0<lambda<=L<=1/10, let x_next be the squared-posterior deviation after d
Potts branches, independent conditional on the root, with edge eigenvalue
lambda. In Sly's normalization s=d lambda^2 x,

    x_next-g_3(s) <= d lambda^4 (C_U U+C_M M^2),          (1)

with explicit positive constants C_U(L), C_M(L) defined in Section A.6.
The inequalities C_U<1/4 and C_M<31/180 apply only to L=1/16;
they are NOT used at larger L.
This is one-sided and requires T>=0. It asserts no Galton--Watson result.

The hardest new steps are the full-simplex softmax derivative bounds
T067-SOFTMAX-DERIVATIVES-001 v1 and the q=3-specific moment estimates below.
The Bayesian replacement construction and favorable cubic sign also occur in
the reviewed T067-SIGNED-LINDEBERG-001 v1; they are written out again here to
make the new estimates checkable. Source context: Sly, Reconstruction for the
Potts model, (4.7) and Lemma 4.3; Mossel--Sly--Sohn, Appendix A. Primary source
files and locators are in SOURCES.jsonl. The new constants are an own-work draft.

A.1. Exact Bayesian hybrid and retained cubic sign.

Write P=I-11^t/3, v=(1/3,-1/6,-1/6), and h=(0,1,-1). Conditional on root 1
the input law has density 1+lambda a_1 relative to mu. Define

    Lbranch=P log(1+lambda a),
    C=(lambda^2 M/2)P,    m=C e_1=lambda^2 M v,
    G conditional on root i ~ N(C e_i,C).

The M=0 case is immediate. Otherwise work on the zero-sum plane. The Gaussian
means have equal squared inverse-covariance norm, so their density ratio is
exp(g_i-g_j). Thus Lbranch and G are exact symmetric Bayesian experiments
with posterior softmax of the displayed vector. Any sum W of unreplaced and
replaced branches is also such an experiment, conditional independence being
with respect to the root. Its root-1 conditional posterior law has density
3p_1 relative to its unconditional symmetric posterior law nu_W.

For any permutation-invariant integrable radial function f(a),
E_1 f=E f: E[a_1 f]=(1/3)E[(sum_i a_i)f]=0. In particular E_1 A^k=EA^k.
We have A<=6 and M<=6.

For F(z)=softmax(z)_1, Bayes calibration gives
E_1 F(sum Lbranch)-1/3=x_next. The d-fold Gaussian sum has mean
(3s,-3s/2,-3s/2) and covariance (9s/2)P, hence
E_1 F(sum G)-1/3=g_3(s). Telescope over the d branches. In a single replacement
W is independent of its replaced branch conditional on root 1.

Symmetry gives Eaa^t=(M/2)P and the third moments
Ea_i^3=T/3, Ea_i^2a_j=-T/6 for i!=j, Ea_1a_2a_3=T/3.
With b=-P a^2/2, the leading raw moment differences are

    E_1 Lbranch-E_1 G = -lambda^3 T v/2 + higher terms,
    E_1 Lbranch Lbranch^t-E_1 GG^t = -lambda^3 T hh^t/2 + higher terms.

The leading third raw tensor is lambda^3 E a^tensor3. Contracting these
three terms with the first three derivatives in Taylor's formula yields
lambda^3 T ell_1(p), where

    ell_i(p)=-(1/2)p_i(p_j-p_k)^2+(3/2)e3(1-3p_i),
    e2=p_1p_2+p_1p_3+p_2p_3,   e3=p_1p_2p_3.

These identities follow by differentiating softmax: grad F dot v=p_1(1-p_1)/2,
D_h^2F=p_1[2(p_2-p_3)^2-(1-p_1)], and
sum_i partial_i^3 F=6e3(1-3p_1). The symmetric third tensor contraction is
(3T/2)sum_i partial_i^3 F before the Taylor factor 1/6.

Calibration and permutation symmetry imply

    E_1 ell_1 = E_nu sum_i p_i ell_i = -E_nu[e2(e2-9e3)] <= 0,        (2)

because e2-9e3=sum_cyclic p_k(p_i-p_j)^2>=0. For the middle equality, expand
sum_i p_i^2(p_j-p_k)^2=2e2^2-6e3 and use sum p_i=1. Thus all retained cubic
terms have nonpositive total expectation when T>=0. Nothing asserts their
pointwise sign or their vanishing. The remaining sections bound every term
discarded from this cubic expansion uniformly in the actual hybrid W.

A.2. Three-state identities and logarithm estimates.

For a zero-sum vector a in R^3, elementary polynomial identities give

    sum_i a_i^4=A^2/2,     ||P a^2||^2=A^2/6,
    P a^3=(A/2)a,         P a^4=(A/2)P a^2+(J/3)a,
    ||P a^4||^2=A^4/24+4AJ^2/9 <= 25A^4/216.          (3)

Here A^3/6-J^2=product_(i<j)(a_i-a_j)^2/3>=0. All equalities can also be
verified by a_3=-a_1-a_2; the exact generic symbolic check is
checks/q3_quartic_geometry.py. Consequently for c=P a^3/3,
||b||=A/(2sqrt(6)) and c=(A/6)a. The same generic orbit computation gives

    E[a_1 c]=Uv/6,
    E[a_1(ab^t+ba^t)]=(U/36)*[[-2,1,1],[1,1,-2],[1,-2,1]].         (4)

The matrix in (4) has eigenvalues 0,-3,3, hence nuclear norm U/6 after scaling.
One way to derive (4) is the fourth-moment list
Ea_i^4=U/6, Ea_i^3a_j=-U/12, Ea_i^2a_j^2=U/12, and Ea_i^2a_ja_k=0 for distinct
i,j,k. Symmetrizing a generic zero-sum orbit proves these identities for every
invariant law by integration.

For an equivariant zero-sum vector V(a), a further useful exact identity is

    E[a_1 V(a)]=v E[a dot V(a)].                       (5)

Indeed its diagonal coordinate is (1/3)E[a dot V], and the two other coordinates
are equal and sum to its negative. This proof applies also to log vectors.

Write Lbranch=lambda a+lambda^2 b+lambda^3 c+r4. The scalar integral remainder
for log, after degree four, is bounded by |lambda a_i|^5/[5(1-lambda)], since
a_i>=-1. Combining this with (3), A<=6, sqrt(6)<=49/20 and
1/sqrt(6)<=5/12, define

    B4=25/288+(49/100)L/(1-L),
    B3=1/6+(49/20)L B4,
    B1=5/24+(49/20)L B3.                              (6)

The resulting pointwise bounds are

    ||r4|| <= lambda^4 A^2 B4,
    ||Lbranch-lambda a-lambda^2 b|| <= lambda^3 A^(3/2) B3,
    ||Lbranch-lambda a|| <= lambda^2 A B1,
    ||Lbranch|| <= lambda sqrt(A)/(1-lambda),
    ||lambda a+lambda^2 b|| <= lambda sqrt(A)(1+lambda/2).            (7)

For the first one, ||P a^4||/4 <=25A^2/288, and the fifth-order remainder
is at most lambda^5 A^(5/2)/[5(1-lambda)]. The next two follow from the exact
norms of b,c. Projection is a Euclidean contraction. These estimates do not
require a power series outside its convergence disk: the log identity follows
by integrating polynomial division of 1/(1+t), for t>-1.

A.3. Mean remainder.

Permutation symmetry implies E Lbranch=0. Applying (5) directly gives

    E_1 Lbranch = lambda v E[a dot Lbranch]
      = m-lambda^3 T v/2+lambda^4 U v/6+lambda v E[a dot r4].        (8)

This removes the unnecessary fourth-order bound on E_1 r4 used in the earlier
proof. At every W, 0<=grad F(W) dot v=p_1(1-p_1)/2<=1/8. Also
|E a dot r4|<=lambda^4 sqrt(6)U B4 by (7) and A<=6. The mean contribution
after its retained cubic part is therefore at most

    lambda^4 U [1/48+(49/160)L B4].                   (9)

A.4. Second and third raw moment remainders.

Let B=lambda a+lambda^2 b. For arbitrary vectors z,w,
||zz^t-ww^t||_*<=||z-w||(||z||+||w||). Using (7), the nuclear norm of
Lbranch Lbranch^t-lambda^2 aa^t-lambda^3(ab^t+ba^t) is at most

    lambda^4 A^2 [1/24+B3(1/(1-L)+1+L/2)].

The first term is ||b||^2=A^2/24; the other terms are the difference from BB^t.
Changing the root-conditional density on the degree-three term adds the exact
matrix (4), with norm lambda^4 U/6. Gaussian raw second moment C+mm^t adds a
remainder of norm lambda^4 M^2/6. Radial bounds average exactly under E_1.
The global Hessian bound 1/5 from SOFTMAX-DERIVATIVES v1 and Taylor factor
1/2 therefore give the contribution

    lambda^4 { (U/10)[1/24+B3(1/(1-L)+1+L/2)+1/6]+M^2/60 }.         (10)

Fix W and put Q(z)=D^3F(W)[z,z,z]. The mixed derivative bound 1/2 from that
same claim and (7) show

    |Q(Lbranch)-Q(lambda a)|
      <=(3/2)||Lbranch-lambda a|| max(||Lbranch||,lambda sqrt(A))^2
      <=(3/2)lambda^4 A^2 B1/(1-L)^2.

After division by 6 this costs lambda^4 U B1/[4(1-L)^2]. The density correction
on the leading cubic costs at most lambda^4 U/15, since
|Q(a)|<=(2/5)A^(3/2) and |a_1|<=sqrt(A).

For G=H+m with H centered, E Q(G)=Q(m)+3E D^3F(W)[m,H,H]. Since
||m||=lambda^2 M/sqrt(6) and E||H||^2=lambda^2 M, the two absolute terms,
after division by 6, are at most lambda^4 M^2*L^2/36 and
lambda^4 M^2*5/48, respectively. The first uses M<=6 and the diagonal bound
2/5; the second uses the mixed bound 1/2 and 1/sqrt(6)<=5/12. Thus all third
raw remainder terms together cost

    lambda^4 {U[B1/(4(1-L)^2)+1/15]+M^2[5/48+L^2/36]}.             (11)

A.5. Fourth-order Taylor remainders.

The global fourth derivative bound 3/5 makes the remainder after cubic order
at most ||z||^4/40. The Lbranch part is bounded by lambda^4 U/[40(1-L)^4].

For the Gaussian use its exact fourth moment, without a triangle inequality.
On the rank-two plane H has covariance (lambda^2 M/2)I. Odd centered Gaussian
moments vanish, E||H||^4=2lambda^4 M^2, and
E(H dot m)^2=(lambda^2 M/2)||m||^2. Expansion gives

    E||H+m||^4
      =2lambda^4 M^2+(2/3)lambda^6 M^3+lambda^8 M^4/36
      <=lambda^4 M^2(2+4L^2+L^4),                   (12)

using M<=6. The separate exact polynomial/Gaussian moment computation in
checks/q3_sharp_constants.py verifies the expansion. Thus the Gaussian
Taylor contribution is at most lambda^4 M^2(2+4L^2+L^4)/40.

A.6. Constants, replacement sum, and verification scope.

Summing (9)--(12), the constants in (1) are

    C_U=1/48+(49/160)L B4
      +(1/10)[1/24+B3(1/(1-L)+1+L/2)+1/6]
      +B1/[4(1-L)^2]+1/15+1/[40(1-L)^4],

    C_M=1/60+5/48+L^2/36+(2+4L^2+L^4)/40.

At L=1/16, B4=4301/36000, B3=2130749/11520000,
B1=872406701/3686400000. Exact rational arithmetic gives
C_U=68871759703/276480000000<1/4 and C_M<31/180.
Every contribution was bounded in absolute value except the retained cubic
term, whose expected sign is (2). All constants are independent of W,d,mu.
The d conditional-root replacements telescope to (1).

The exact source checks/q3_quartic_geometry.py verifies generic zero-sum
polynomial, fourth-moment orbit, equivariant-mean and averaged-cubic identities.
checks/q3_sharp_constants.py checks the Gaussian fourth moment and rational
constants. The derivative claim has a complete rational Bernstein certificate
and independent replay. These finite verifications do not replace independent
review of calibration, integrability, or the analytic remainder bounds above.

For clarity, in A.6 the specialization to L=1/16 is an old consistency check.
Every step A.1--A.5 is valid for arbitrary 0<lambda<=L<=1/10: the only
denominators are positive 1-L, the log remainder is an integral remainder
valid for lambda a_i>-1, and the bounds A<=6 and sqrt(6)<=49/20 are uniform.
No estimate uses C_U<1/4 in obtaining (1). At a Gaussian hybrid the messages
are unbounded, but the derivatives are globally bounded and its displayed
fourth moment is finite, so the integral Taylor remainders are integrable.

## Part B. Gaussian normalization, curvature and endpoint enclosures

B.1. Let w=P e_1, so ||w||^2=2/3. For s>0,

  g_3(s)+1/3 = E F((9s/2)w + sqrt(9s/2) Z_P),

where Z_P is a standard Gaussian on the two-dimensional zero-sum plane.
The drifted heat generator is H=(9/2)D_w+(9/4)Delta_P. The reviewed global
softmax bounds, for plane vectors, are

  |D^2 F[h,h]| <= ||h||^2/5,
  |D^3 F[r,h,h]| <= ||r|| ||h||^2/2,
  |D^4 F[h,h,h,h]| <= 3||h||^4/5.

Bounded derivatives and Gaussian integration by parts (or the constant-
coefficient heat semigroup, twice) give g_3''(s)=E H^2 F(L_s). To bound it,
take orthonormal plane vectors u,v. Polarization gives

  12 D^4F[u,u,v,v] = D^4F[(u+v)^4]+D^4F[(u-v)^4]
                    -2D^4F[u^4]-2D^4F[v^4].

The right side has absolute value at most (3/5)(4+4+2+2), so the mixed
derivative is at most 3/5. Therefore |Delta_P^2 F|<=12/5. Also
|D_w Delta_P F|<=||w||<=5/6 and |D_w^2 F|<=2/15. Expanding H^2 yields

  |g_3''(s)| <= 27/10 + 135/8 + 243/20 = 1269/40 < 32.       (B1)

Consequently for a<=s<=b, if U_a>=g_3(a), U_b>=g_3(b),

  g_3(s) <= ((b-s)U_a+(s-a)U_b)/(b-a) +16(s-a)(b-s).          (B2)

To check the direction, subtract the exact-endpoint chord and the positive
parabola from g_3. Its second derivative is g_3''+32>=0 and its endpoint
values are zero; convexity places it below zero. Raising endpoints preserves
the upper bound. All endpoints here are positive, avoiding s=0 issues.

B.2. Orthogonal standard Gaussian coordinates z_1,z_2 give exactly

  f_s(z)=[1+2 exp(-9s/2-(3sqrt(3s)/2)z_1)
                    cosh((3sqrt(s)/2)z_2)]^(-1),
  g_3(s)=E f_s(Z)-1/3.                                    (B3)

Indeed the logit contrasts L_2-L_1 and L_3-L_1 have common component
-9s/2-(3sqrt(3s)/2)z_1 and opposite components +/-3sqrt(s)z_2/2.
The corresponding zero-sum logit noise matrix has orthogonal columns of
squared norm 9s/2. Applying the reviewed softmax Hessian bound 1/5 gives
the global coordinate Hessian operator bound ||D_z^2 f_s||<=9s/10.

Partition [-6,6] into bins of width h (h=1/8 originally and h=1/16 at the
13 refined endpoints). Put w_i=Pr(Z in I_i), t_i=E[Z | Z in I_i],
v_i=E[(Z-t_i)^2 1_{I_i}], P_0=sum_i w_i and D_0=sum_i v_i.
All bins have positive mass. The product-bin Taylor linear term at (t_i,t_j)
integrates to zero and the quadratic remainder is bounded by
(9s/20)(w_j v_i+w_i v_j). Thus, with
Q_s=sum_ij w_i w_j f_s(t_i,t_j),

  |E[f_s(Z)1_{[-6,6]^2}]-Q_s| <= (9s/10)P_0 D_0.

Since 0<=f_s<=1, the omitted region contributes between zero and 1-P_0^2.
If outward enclosures give Q_s<=Q_U, P_L<=P_0<=P_U and D_0<=D_U, then

  g_3(s) <= Q_U+(9s/10)P_U D_U+1-P_L^2-1/3.                (B4)

This accounts for the entire Gaussian tail; there is no unbounded truncation.
The bin weights, means, variances and Q are computed with 160-bit outward
Arb balls and independently with directed dyadic integers/Fractions. The
dyadic exp, sinh/cosh, normal primitive and pi constructions, their series
truncation bounds, and round-down/round-up arithmetic are in the pinned
dyadic_interval.py and gaussian_gap_dyadic.py sources; no binary floating
point decides any bound. The changed producers only use h=1/16, the named
13 signal points and B4 in place of the older looser Hessian constant.

## Part C. Exact finite piecewise certificate

Set D=156 and L=16013/200000. Exactly,

  D*16013^2-200000^2 = 922364 >0,

so for every d>=D, eta=d^(-1/2)<L<=1/10. Define C_U,C_M by A.6 at this
fixed rational L, without rounding them to the old L=1/16 bounds. Their
exact rational values are printed in piecewise_cutoff_independent.json
(approximately 0.2599399973 and 0.1716534679; displays are not premises).

The 86 endpoints are s_i=1/(10-i/10), i=0,...,85. They cover [1/10,2/3].
At each endpoint use B4. For the original h=1/8 enclosures, endpoint indices
0..84 in gaussian_gap_{v1,dyadic_v1} give s_1..s_85, and endpoint 233 in
gaussian_small_gap_{v1,dyadic_v1} gives s_0=1/10. For each engine pair use
the LARGER endpoint upper bound, so either engine independently suffices.
At the following points also compute h=1/16 enclosures and use the smaller
of the valid old upper bound and this valid refined paired upper bound:

  5/43, 2/17, 5/42, 10/83, 5/41, 10/81, 1/8,
  10/79, 5/39, 10/77, 5/38, 2/15, 5/37.

verify_piecewise_refiners.py rebuilds all 13 refined endpoints and checks
301 enclosure overlaps (96 bins times three quantities plus 13 Q values).
verify_piecewise_endpoints_from_raw.py independently rebuilds all 86 final
upper bounds from raw Q/bin enclosures, verifies generating-source hashes,
and matches the final endpoint map. Stored 'passed' fields and stored gap
margins are not trusted. The endpoint formulas and all inputs are hash-pinned.

For every adjacent pair [a,b] form the exact function

  H_ab(s)=s-[(b-s)U_a+(s-a)U_b]/(b-a)-16(s-a)(b-s)
          -(81/156){C_U min(5s^2,2s/3)+C_M s^2}.          (C1)

It is a rational quadratic on either side of 2/15. The independent checker
verify_piecewise_cutoff_independent.py imports no gate polynomial or constant
function: it computes C_U,C_M afresh, evaluates C1 directly at each segment's
ends and midpoint, and obtains degree-two Bernstein coefficients

  b_0=H(l), b_2=H(r), b_1=2H((l+r)/2)-(b_0+b_2)/2.

It bisects only where necessary and verifies exact full coverage. Its saved
87 leaves cover all 85 original intervals, with every Bernstein coefficient
strictly greater than 3/10^7. Since the Bernstein basis is nonnegative and
sums to one, H_ab(s)>0 everywhere, including all boundaries. Missing-endpoint
and raised-upper-bound controls are rejected by this same checker.

These computations use only exact Fraction arithmetic on saved outward
enclosures, so combining B2 and C1 gives, for every s in [1/10,2/3],

  s-g_3(s) > (81/156){C_U min(5s^2,2s/3)+C_M s^2}.        (C2)

Regenerate the 13 refinements with refine_piecewise_arb_v1.py and
refine_piecewise_dyadic_v1.py, --count 13 --seconds 240 each (resume saved
checkpoints if needed). Then run verify_piecewise_refiners.py,
piecewise_curvature_gate.py, verify_piecewise_endpoints_from_raw.py, and
verify_piecewise_cutoff_independent.py, in that order. Original h=1/8 endpoint
producers and their exact configurations are included in the submission.
The old planning gate's optional derivative bound is NOT a premise here.

## Part D. Fixed point, canonical entry, and smaller eigenvalues

D.1. Fix d>=156 and eta=1/sqrt(d). Let p_n be the root posterior given all
spins at levels n and later. By the tree Markov property this equals the
posterior given generation n alone. These future sigma-fields decrease;
bounded reverse-martingale convergence gives p_n -> p_infinity almost surely
and in every finite L^r. The laws mu_n and mu_infinity are calibrated and
S3-invariant. Write M=9x, U and T as in A for the limiting law.

For this fixed finite d, the BP mapping is continuous on laws on the compact
simplex: every branch likelihood 1+eta a_i is at least 1-eta>0, so the posterior
and bounded Bayesian product weight are continuous. Thus mu_infinity is a BP
fixed point. The Blackwell decrease of the future observations gives
x_n decreasing to x_infinity, with 0<=x_infinity<=2/3.

D.2. The initial pure-state experiment has T_0=6. An eta-edge multiplies
the centered vector by eta and its cubic moment by eta^3. The reviewed
CUBIC-FUSION inequality is

  T_fuse >= (1-M_R/6)T_L+(1-M_L/6)T_R.

Every posterior has M<=6, so induction over depth and branches gives T_n>=0,
then bounded convergence gives T>=0. At the critical fixed point an individual
edge experiment has second moment M/d and fourth moment U/d^2. Any prefix of
branches has M_j<=M because forgetting the remaining observations is a
Blackwell degradation. The reviewed F2 applies to every fusion: the right
branch coordinates are at least (1-eta)/3 and eta<L<2887/5000. It yields

  U_(j+1) <= U_j+U/d^2+5 M_j M/d.

Summing from U_1=U/d^2 gives U<=U/d+5(d-1)M^2/d and hence U<=5M^2.
Pointwise A<=6 also gives U=EA^2<=6EA=6M. Therefore, if x>0,

  U <= 81 min(5x^2,2x/3),     M^2=81x^2.                 (D1)

All independence used is conditional on the root, as required for fusion;
unconditional branch independence is never assumed.

D.3. If x>=1/10, apply A with lambda=eta<L and T>=0. Sly's map variable is
s=d eta^2 x=x exactly, not 3x/2 or another normalization. Since x_next=x,

  x-g_3(x) <= (C_U U+C_M M^2)/d
            <= (81/156){C_U min(5x^2,2x/3)+C_M x^2},

contradicting C2. Therefore x_infinity<1/10. Convergence of x_n proves the
canonical BP sequence from the point-mass leaf experiment enters x<1/10 at
some finite depth; no numerical depth or convergence rate is asserted.

The reviewed UNIFORM-LOCAL v1 excludes a nonzero symmetric critical fixed
point with x<=1/10 when d>=100. Since d>=156, it gives x_infinity=0. For the
leaf law L_i^n conditional on root i and its unconditional law L^n,

  TV(L_i^n,L^n)=(3/2)E|p_n(i)-1/3| <= (3/2)sqrt(x_n) ->0.

This is critical nonreconstruction. It also proves the entry demanded above
without substituting a simulation for the canonical limiting argument.

D.4. For 0<lambda<=eta let c=lambda/eta and S_c(p)=u+c(p-u), u=(1/3,1/3,1/3).
The experiment obtained by retaining the observation with probability c and
otherwise replacing it with an independent unconditional observation, without
revealing that choice, has posterior S_c(p). It is a root-independent garbling.
Exactly 1-eta+3eta S_c(p)_i=1-lambda+3lambda p_i, so
B_lambda(mu)=B_eta((S_c)_*mu). Applying these independent garblings branchwise
preserves Blackwell order. Induction from the same pure-state experiment gives
mu_n^lambda <=_B mu_n^eta, hence x_n^lambda<=x_n^eta ->0 by convexity. This
proves the stated full interval of positive eigenvalues.

Audit scope: all four analytic/finite pieces A--D require independent review
on this exact version. The finite PASS receipts alone do not confer an
independently checked theorem. The previous d>=256 proof remains untouched.

NEXT: Both auditors check this immutable version; only then pursue a proved
fixed-point U/M^2 improvement toward the remaining degrees 5..155.

## Version 2 metadata-only amendment

The mathematical statement, analytic inequalities and finite certificate are
unchanged from v1 (SHA256 9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226). The lead review by codex-term-362ebe34
passed the v1 mathematics while flagging the blanket two-review assertion.
This version corrects that assertion; it does not inherit an exact-version
external PASS. No v1 proof, endpoint, certificate or review receipt is edited.

## Version3 dependency-scope clarification

Only RESCALE identity(R) is imported in D.4. Its false unrestricted F1
corollary is not used. D.3 instead uses TERNARY-MOMENTS F2 with actual
critical right branches supported on p_i>=(1-eta_ref)/3, eta_ref=2887/5000,
since lambda<=16013/200000<eta_ref. All mathematical inequalities, the
cutoff156 statement and frozen finite inputs are unchanged. The separate
review-status qualification in v2 remains in force. Versions1 and2 survive
unchanged; no exact-version PASS is inherited automatically by this v3.
