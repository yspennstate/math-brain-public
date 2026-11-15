# Independent referee log

Task: Be a hard, independent referee of `PAPER.tex`, requested 12 November 2026; first recorded local clock: 05:43:33 +04 (Asia/Tbilisi). Source locations below refer to the supplied, unchanged file.

Constraints: no browsing, no helpers, no outside writes, no git operations, no visible windows. All audit programs and outputs stay here. Computations use one Python worker, one numerical-library thread, inherited nice priority at least 10, a 240-second alarm and small scalar/short-grid problems. macOS rejected setting RLIMIT_DATA despite reporting unlimited inherited limits; actual peak resident memory is recorded for every successful run and is far below 1 GB. Shared checklist/mesh/brain writers are not invoked because this run expressly forbids outside writes. This log is the local task record. Prior memories are not treated as evidence for the paper.

## 1. Introduction and statement  reached first

- **CORRECT**, line 43: the atom-at-a-real-mode plus monotone density definition is the standard measure-theoretic definition of unimodality (equivalently convex/concave distribution function on the two sides). The value of the density at the mode is immaterial. Both proofs use this definition, including almost-everywhere representatives.
- **CORRECT**, quoted Conjecture 5.5 at lines 4749, **conditional on the quotation being faithful**: the theorem contradicts precisely this quotation. I remember the HasebeUeda paper as studying eventual unimodality for Brownian/free Brownian motion and other stable processes, with this moment conjecture near its end; confidence moderate in the subject and conjecture, lower in exact numbering and wording. I have not consulted the original and cannot authenticate the quotation.
- **CORRECT**, [eq:classical], lines 5356: exp(-t lambda^alpha) gives the drift-free stable subordinator. Laplace-transform multiplication proves the semigroup, and uniqueness gives S_t = D_(t^(1/alpha)) S_1. For positive a,b, a X_1+b X_2 has scale (a^alpha+b^alpha)^(1/alpha), with no centering. Strict stability is proved by this homogeneity; merely saying alpha<1 would not remove a separately added deterministic drift. The specified exponent has none.
- **CORRECT**, [eq:free], lines 5760: its analytic sign, growth, semigroup and strict dilation properties will be checked in step 5. No alpha=1 centering issue arises.
- **CORRECT**, [eq:mustar] and the moment claim of [thm:main], lines 6169: the weights are positive, their total is less than 1/4, and exp(lambda A_n-A_n^2) is eventually at most 1. Thus all absolute exponential moments, in particular the (2+alpha)-moment, are finite. Full estimates are recorded in step 4.
- **CORRECT**, line 71: with L_s(x)=s exp(-s^2/(2x))/(sqrt(2 pi) x^(3/2)), its Laplace transform is exp(-s sqrt(2 lambda)), so S_t^(1/2)=L_(t/sqrt(2)). Substitution gives t exp(-t^2/(4x))/(2 sqrt(pi) x^(3/2)), exactly line 109. This is the Brownian first-passage normalization. If instead L_s were normalized by exp(-s sqrt(lambda)), one would have S_t=L_t. An initial commentary sentence incorrectly questioned this equality; it was immediately corrected, before any numerical work.
- **WRONG if read as a characterization**, line 71: for this kernel the dividing line is the support of mu and not its tail. Unbounded support is not a necessary obstruction to eventual unimodality. For example, a positive exponential initial density convolved with the explicit positive 1/2-stable density is unimodal for every t (a direct proof is given in REPORT.md). The valid claim is that compact support suffices, while no prescribed positive upper bound on the left tail guarantees eventual unimodality. This wording does not enter the proof.
- **GAP (attribution only)**, lines 4551: the original propositions/theorems and the claim that the authors' particular construction necessarily has infinite 5/2-moment cannot be authenticated from memory. The opposite-direction mechanism itself will be checked, and novelty is deferred to step 9.

Provisional verdict on [thm:main]: pending the free audit; no defect in the statement's normalization or moment hypothesis.

## 2. [lem:classical], lines 7989

- **CORRECT**, hypotheses and statement, line 80. A nonnegative integrable function strictly decreasing on (b,infinity) is positive throughout that interval: a zero there would force negative values later. A kernel with b=0 and continuous g(0)=0 cannot satisfy these hypotheses, but that harmless empty subcase causes no counterexample.
- **CORRECT**, line 84, density display: the Weierstrass bound |p_j g(x+a_j)| <= p_j ||g||_infinity gives uniform convergence. The limit is continuous, Tonelli gives integral one, and convolution with a density has no atom.
- **CORRECT**, line 86, choice of N and I_n: growing gaps make these intervals nonempty. Terms j<n vanish identically because x+a_j<0. Terms j>=n lie entirely beyond b and are strictly decreasing. For any x<y in I_n all their differences are nonnegative and the n-th difference is strictly positive, so the infinite sum is strictly decreasing without differentiating the series.
- **CORRECT**, line 88: absolute continuity forces c=0. A full-measure equality set is dense in every nonempty open interval. Approximate any u<v<a by ordered pairs from this set, then use continuity of q. Hence q is nondecreasing to the left of a, contradicting an I_n contained there.
- **CORRECT**, finite-mode coverage: the definition requires a in R, so there is no missing mode at minus infinity case. A nonnegative globally nonincreasing integrable density on R must be zero almost everywhere (and likewise for globally nondecreasing). Thus allowing an infinite-mode convention would add no nonzero absolutely continuous probability here. Atoms at a finite mode are already excluded by absolute continuity.
- **CORRECT**, attempted counterexample audit: no kernel/weight counterexample satisfying the hypotheses can survive the explicit pairwise difference argument. Tiny positive weights do not affect its sign. A finite atom sequence falls outside the hypotheses; it may or may not be unimodal, as step 8 will illustrate.

Verdict: **CORRECT**.

## 3. [lem:kernel], lines 91113

Independent program: `python3 audit.py 3 > step3.txt`; output `step3.csv` and `step3.txt`. The first two launch attempts exposed inherited-priority/macOS-resource-limit restrictions and were corrected; they performed no mathematical calculation. Successful run: 3.582 seconds, peak RSS 38,633,472 bytes.

- **CORRECT**, line 96, scaling: Laplace uniqueness gives X_t =_d t^(1/alpha) X_1. Its characteristic function uses the branch (-iu)^alpha with argument -sign(u) pi alpha/2, so its modulus is exp(-cos(pi alpha/2)|u|^alpha). The latter is integrable. Fourier inversion yields a bounded continuous density; nonnegative support makes this density zero on the negative half-line, and continuity forces its value at 0 to be 0.
- **CORRECT**, [eq:series], lines 98101, including both signs. Independent derivation: deform the inverse-Laplace contour to the negative-real cut of exp(-s^alpha). For x>0 the jump integral is

  g_1(x) = (1/pi) integral_0^infinity exp(-rx) [-Im exp(-r^alpha exp(i pi alpha))] dr.

  Expanding the second exponential gives (-1)^(k+1) sin(k pi alpha) r^(k alpha)/k!. Integrating r^(k alpha) gives Gamma(k alpha+1) x^(-k alpha-1), exactly the displayed coefficients. Interchange is justified by exp(-rx+r^alpha), integrable for alpha<1, including the sum of absolute values. Equivalently the Hankel coefficient is (-1)^k/(k! Gamma(-k alpha)); reflection gives the same sign. This also handles the coefficients that vanish when k alpha is integral.
- **CORRECT**, line 102: Stirling gives the k-th root of Gamma(k alpha+1)/k! asymptotic to alpha^alpha exp(1-alpha) k^(alpha-1), which tends to 0. Thus E has infinite radius of convergence. This justifies termwise differentiation at every positive x.
- **CORRECT**, derivative display at lines 103105: chain rule with y=x^(-alpha) gives -x^(-2)(E(y)+alpha y E'(y)). Its first nonzero coefficient is (1+alpha) Gamma(1+alpha) sin(pi alpha)/pi > 0. Therefore the derivative is strictly negative for all sufficiently large x, uniformly over that tail for each fixed alpha. No uniform bound as alpha varies is needed.
- **CORRECT**, line 106: density scaling gives b_t=t^(1/alpha)b_1.
- **CORRECT**, lines 109113, explicit half-stable density and derivative: differentiating gives exactly the factor (t^2/4-3u/2) u^(-7/2). Its mode is t^2/6, so strict decrease holds beyond b_t=t^2/6. Independent quadrature at Laplace parameters 0.25, 1, 4 agrees with exp(-sqrt(lambda)); numerical differentiation agrees with the displayed derivative.
- **CORRECT**, independent series test: alpha=0.3,0.5,0.7, x=0.5,1,2,5, compared with de Hoog inversion of exp(-s^alpha), at 70 decimal digits. All 12 relative discrepancies are below 1.2e-70. The inversion uses the Laplace transform, not the series or an author's program. Full numbers will appear in REPORT.md.
- **GAP (citation authentication only)**, lines 98 and 113: exact Feller/Pollard locations and the claims about the unavailable author check script cannot be checked here. The mathematics does not depend on trusting that script.

Verdict: **CORRECT**.

## 4. Classical proof of [thm:main] and tail remark, lines 115125

- **CORRECT**, exponential-moment display at lines 116119: finitely many terms with A_n<lambda are finite; all remaining exponential factors are <=1, and the prefactors sum. This works for every fixed lambda>0 and supplies every polynomial absolute moment, including 2+alpha. In fact the weights even give a positive Gaussian exponential moment for any exponent below 1.
- **CORRECT**, line 120: W <= sum_(n>=1) 2^(-n-2) = 1/4, so 1-W>=3/4 and all masses are positive and sum to 1.
- **CORRECT**, line 120, growing-gap identity for n>=2: A_n=A_(n-1)^2, so A_n-A_(n-1)=A_(n-1)(A_(n-1)-1) tends to infinity. The first gap from a_0=0 to a_1=4 is separate. The sentence should explicitly attach n>=2 to the A-identity; the later remark's convention A_0=0 is incompatible with using that identity at n=1.
- **CORRECT**, application of the two lemmas: the same fixed mu_* works for every alpha,t, since the lemmas require only a finite tail-decrease threshold for each kernel. There is no interchange of quantifiers.
- **CORRECT**, tail remark, line 124: for x in [A_(n-1),A_n), strict s<-x includes exactly atoms -A_j with j>=n. At x=A_(n-1), the atom at that endpoint is excluded; at x=A_n one uses the next interval. Since psi is nonincreasing, psi(A_j)<=psi(A_n)<=psi(x) for j>=n. More explicitly,

  sum_(j>=n) p_j <= min(psi(A_n),1) sum_(j>=n) 2^(-j-1)
                    = 2^(-n) min(psi(A_n),1) <= psi(A_n) <= psi(x).

  Thus the suspected reversed inequality is actually right. The convention A_0=0 is valid for this interval partition only. The weights sum to <=1/2, so p_0 is positive; psi>0 ensures every p_n>0.
- **CORRECT**, conclusion of the remark in its stated uniform-guarantee sense: for every prescribed positive nonincreasing tail envelope one can choose a measure under it for which eventual unimodality fails. This is not an assertion that every measure of unbounded support fails.

Verdict: **CORRECT**, with the n>=2 indexing clarification above.

## 5. Free preliminaries, lines 129145

- **CORRECT**, line 130, admissibility of [eq:free]: if z=r exp(i theta), 0<theta<pi, then arg(-phi(z))=pi alpha+(1-alpha)theta lies strictly between 0 and pi. Thus Im phi<0, and |phi(iy)|/y=t y^(-alpha) tends to zero. The free LvyKhintchine characterization quoted here has the expected hypotheses; accepting that foundational theorem, it supplies a nondegenerate freely infinitely divisible law.
- **CORRECT**, line 130, dilation and semigroup: phi_(D_c nu)(z)=c phi_nu(z/c), giving c^alpha phi_1(z), and addition of phi gives time addition. Together these prove free strict stability without centering, not merely infinite divisibility.
- **CORRECT**, positivity/absolute continuity of this stable law, with an independent support check: write beta=1-alpha, so phi(z)=t(-z)^beta (arg(-z) in (-pi,0)). Its positive free Lvy measure has density t sin(pi alpha)/pi times s^(-1-alpha) on s>0, since on z=-r the compound-Poisson integral integral z s/(z-s) dLambda(s) is t r^beta. Positive compound-Poisson approximations give a nonnegative law. For mu=delta_0 the inverse boundary map at w=-r is -r+t r^beta; its maximum is

  ell = alpha t^(1/alpha) (1-alpha)^((1-alpha)/alpha) > 0.

  The support is [ell,infinity), consistent with concentrated on (0,infinity); the usual inverse-transform branch has a continuous density on its interior and a square-root edge, no atom. One can also exclude atoms directly: if F_nu(z) tends to 0 at a hypothetical atom x, z=F_nu(z)+phi(F_nu(z)) forces x=0, and at x=0 the power term prevents F_nu(iy)/(iy) from tending to a finite positive value. These checks agree with my high-confidence memory of the positive free stable family and its absolute continuity. Exact HK Corollary/BP attribution remains unverified.
- **CORRECT**, [eq:H] and Nevanlinna form, lines 132136: -phi_nu composed with F_mu is Pick, and F_mu(iy)/(iy)->1 implies phi_nu(F_mu(iy))/(iy)->0. Nevanlinna representation therefore gives H(z)=a+z+integral (1+sz)/(z-s) d sigma(s), with finite positive sigma. sigma=0 would make phi_nu constant real and nu a point mass; nondegeneracy excludes it. The representation is not claiming that H itself maps all of C+ to C+.
- **CORRECT**, threshold formula for f, line 136, derived directly. Put

  I(x,y)=integral (1+s^2)/((x-s)^2+y^2) d sigma(s).

  Then Im H(x+iy)=y(1-I(x,y)); I decreases strictly continuously with y>0, tends to 0 at infinity, and increases to I(x,0) as y decreases to 0. Thus f(x)=0 iff I(x,0)<=1, and otherwise I(x,f(x))=1. For f>0, implicit differentiation gives continuity; at a zero, every fixed y>0 has I(x,y)<1, which gives upper semicontinuity there and hence continuity. Lower semicontinuity follows by testing y<f(x). The upper domain Omega={x+iy:y>f(x)} is exactly where Im H>0.
- **CORRECT, with a definition needed**, (HW2), line 139. With finite real boundary value H(x), a finite nonnegative angular derivative is exactly 1-I(x,0) in [0,1], equivalent to x outside V. Finite I(x,0) gives the real boundary value and angular derivative by CauchySchwarz and dominated convergence in a nontangential cone. Conversely Im H(x+iy)/y=1-I(x,y) and the real-boundary angular expansion give the same criterion. No omitted upper bound on the positive derivative changes the criterion: it is automatically <=1. Infinity is not included in [0,+infinity).

  **GAP (wording/definition)**: angular derivative must include a finite *real* boundary value, as in the boundary JuliaCarathodory convention. If it only meant existence of an ordinary complex derivative at a real argument, the quoted equivalence would be false: H(z)=z-i has ordinary derivative 1 everywhere, but I(x,y)=1/y and f(x)=1. At analytic points where H is real on a real neighborhood, the angular derivative is exactly the ordinary derivative. The proof at line 182 explicitly verifies that extra realness, so this ambiguity causes no gap in its application.
- **CORRECT**, (HW1), direct derivation. In Omega,

  H(z_1)-H(z_2)=(z_1-z_2)[1-integral (1+s^2)/((z_1-s)(z_2-s)) d sigma(s)].

  CauchySchwarz bounds the integral modulus by sqrt(I(z_1)I(z_2))<1, proving univalence. The same identity extends to the boundary, where I<=1, and gives |H(z_1)-H(z_2)|<=2|z_1-z_2|. Thus H is continuous on the closed graph domain. Equality H(z_1)=H(z_2) for distinct boundary points would force equality in CauchySchwarz and I(z_1)=I(z_2)=1. If sigma has at least two support points, proportionality forces z_1=conjugate(z_2), impossible for distinct points in the closed upper half-plane. If sigma is a single atom, equality forces (z_1-s)(z_2-s)=M>0 with both |z_j-s|>=sqrt(M); again both points must be the same real endpoint. Hence the boundary map is injective.

  It is also proper: divide the integral part of H by z and split sigma into a compact part and its tail. The compact contribution tends to zero as |z| tends to infinity. CauchySchwarz bounds the tail by sqrt(I(z)) times sqrt(integral_tail |s+1/z|^2/(1+s^2) d sigma), which is at most 2 sqrt(sigma(tail)) for large |z|. Therefore H(z)/z->1 uniformly at infinity within the closed graph domain I<=1. In particular the real boundary map tends to -infinity and +infinity at its two ends. Combined with continuity and injectivity this proves that h is an increasing homeomorphism R onto R. It also proves H(Omega)=C+: the image is open by univalence and closed relative to C+ by boundary continuity and properness, so it is all of connected C+.

  On positive-height boundary arcs, I=1 implies Re H'=integral 2f^2(1+s^2)/((x-s)^2+f^2)^2 d sigma>0. Implicit differentiation gives f'=-Im H'/Re H', hence h'=|H'|^2/Re H'>0, a separate local check. This completes the boundary-map argument needed here without trusting the original HW1 citation.
- **CORRECT**, subordination and the positive-height part of (HW4), independently derived. Near infinity,

  F_(mu boxplus nu)^(-1)(z)=F_mu^(-1)(z)+phi_nu(z).

  Consequently F_(mu boxplus nu)(H(w))=F_mu(w) on Omega by inverse uniqueness and analytic continuation. Taking reciprocals and boundary imaginary parts gives

  p(h(x))=-Im G_mu(x+i f(x))/pi
         =f(x)/pi integral 1/((x-s)^2+f(x)^2) d mu(s),  x in V.

  Since f>0, these are actual analytic positive-density arcs, not arbitrary values of a representative. On an analytic real interval with F_mu real nonzero and H'>0, the inverse continues analytically with real G, proving zero density there directly.
- **CORRECT in the form used**, (HW3): atom exclusion from B,C follows from their stated containments. The full A/B/C classification, including existence assertions about arbitrary boundary limits, is accepted on trust as a quoted theorem, not reconstructed. There is a direct replacement for its only use here: at an isolated mu-atom of mass m, F_mu(x+iy)~iy/m, so for this stable phi

  Im H(x+iy)/y = 1-t m^(alpha-1) cos(pi alpha/2) y^(-alpha)(1+o(1)) -> -infinity.

  Thus I(x,0)=infinity, f(x)>0, without invoking (HW3).
- **CORRECT in the form used**, (HW4): absence of singular continuous mass, the atom classification and global density continuity away from h(A) are the nontrivial regularity results I take on trust. The local density/zero formulas used for this construction were derived above. At points of h(A), a density can be assigned value zero without specifying its limiting behavior, since values at atomic points do not determine the absolutely continuous measure; the display should clarify that convention. If s_nu does not exist, A should be declared empty, or the nonexistent-atom mass interpreted as zero.
- **GAP (source authentication only)**: I cannot verify the exact HuangWang proposition/theorem numbers, all boundary hypotheses in their original wording, or the HK/BP section citations under the no-browsing rule. Nothing in the specialized stable application contradicts the formulas derived here.

Verdict: **CORRECT in the application**, with the angular-derivative convention made explicit; general boundary and regularity theorems remain cited inputs.

## 6. Free proof of [thm:main], lines 148193

- **CORRECT**, Step 1, line 150: nu has no atoms, so the A inequality would demand a mu-atom of mass at least 1. Every mu-atom is strictly smaller than 1. Therefore A is empty and (HW4), as stated, supplies absolute continuity and a continuous density on all R. No moment restriction on nu is being tacitly used.
- **CORRECT**, Step 2, line 152: -Im G(x+iy)=integral y/((x-s)^2+y^2) d mu(s)>=w_k/y at x=-A_k. There is no cancellation of imaginary parts, so the limit cannot be finite real or zero. Thus x belongs to none of A,B,C, and x is in V. Since f(x)>0 and mu is a nonzero positive measure, every factor in the density formula is positive; its value is strictly positive. The direct stable-power calculation in step 5 independently proves f(x)>0 here.
- **CORRECT**, Step 3, [eq:nchoice]: A_n^alpha tends to infinity for every fixed alpha>0, so such n>=2 exists for every t. All later n also qualify; no uniform choice over alpha,t is asserted.
- **CORRECT**, line 158: A_(n-1)=sqrt(A_n)<=A_n/4 for n>=2, with equality at n=2 (A=16). Hence -A<c=-A/2<-A_(n-1).
- **CORRECT**, display at lines 159161: G(c) is the atomic Cauchy-transform sum. Differentiation gives G'(c)=-integral (c-s)^(-2) d mu(s), so I_2=-G'>0. Absolute convergence and local differentiated convergence follow because this gap is separated from the closed discrete support.
- **CORRECT**, line 162: for k<n, c+A_k<=-A/4<0 and its absolute value is >=A/4; for k>=n, c+A_k>=A/2>0. The 0-atom contributes -(2/A)(1-W), early atoms contribute negative numbers, and late atoms contribute at most 2W/A.
- **CORRECT**, G bound at lines 163165: dropping early negative terms and bounding the late mass by W gives G(c)<=-2(1-W)/A+2W/A=(-2+4W)/A<=-1/A.
- **CORRECT**, I_2 bound at lines 166169: the three displayed terms bound the 0, early and late contributions, respectively. Bounding each of the latter two masses by W is loose but valid. The sum is (4+16W)/A^2<=8/A^2<9/A^2. The paper correctly retains a strict <9 despite using non-strict W<=1/4.
- **CORRECT**, line 170: G is real analytic on the whole gap, and J_0={G<0} contains c. F=1/G is analytic and negative real on J_0. Also Im F(z)>0 for z in C+, since Im G(z)<0; in fact F'(x)=I_2/G(x)^2>0 on this real gap, explicitly verifying that F approaches the negative axis from above.
- **CORRECT**, lines 170173: the upper branch has w^(1-alpha)=|w|^(1-alpha) exp(i pi(1-alpha)) on negative w. It has a local analytic continuation across every strictly negative point (this is not the lower principal-branch boundary). Multiplication by -t exp(i pi alpha) gives +t |w|^(1-alpha). Thus H(x)=x+t a(x)^(alpha-1) is real, with a=-G>0.
- **CORRECT**, [eq:Hprime], lines 174177: a'=I_2, so H'=1-(1-alpha)t I_2 a^(alpha-2). The negative sign and exponent are both right.
- **CORRECT**, lines 178181: alpha-2<0 reverses the power inequality, so a(c)>=1/A implies a(c)^(alpha-2)<=A^(2-alpha). Therefore H'(c)>1-9(1-alpha)t A^(-alpha)>=1/2. In fact the loose bounds give a strict margin; no equality issue occurs.
- **CORRECT**, line 182, J outside V: shrink to an interval J around c with closure contained in J_0 and the original gap, and H'>0 throughout. At these analytic real points the angular derivative is the ordinary real derivative. The threshold calculation from step 5 gives I(x,0)=1-H'(x)<1, hence f(x)=0. This verifies the application of (HW2) directly and resolves the convention ambiguity there.
- **CORRECT**, line 182, zero density: on J, h=H, so (HW4) gives p=0 on h(J); equivalently the analytic inverse of H continues G_(mu boxplus nu) as a real function across h(J), proving there is no measure at all in this interval.
- **CORRECT with an implicit shrink**, ordering display at lines 183185: strict homeomorphism ordering plus closure(J) contained in (-A_n,-A_(n-1)) gives h(-A_n)<inf h(J)<sup h(J)<h(-A_(n-1)). Mere open inclusion without compact closure would not by itself imply the two outer strict inequalities. The continuity construction allows the needed shrink immediately; adding with closure contained in J_0 makes the argument explicit.
- **CORRECT**, Step 4, line 187: continuity and positive values at u and v give disjoint open neighborhoods of positive lower density, with a common eta>0 and delta>0 after shrinking. Pointwise positivity alone for an arbitrary density representative would be insufficient; the paper explicitly supplies the necessary neighborhoods.
- **CORRECT**, null-set and mode cases in line 187: if a>=sup K, choose a left-neighborhood point and an interior K point below a from the full-measure equality set. Their values are respectively >eta and 0, contradicting nondecrease. If a<sup K, the open set K intersect (a,infinity) is nonempty; choose there and then in the right positive neighborhood from the equality set, contradicting nonincrease. This covers a inside K, at either endpoint, and far outside it. Absolute continuity rules out a mode atom. No exceptional point or null set can undo an open-interval contradiction.
- **CORRECT**, line 189, quantifiers: n may depend on alpha and t, while mu_* is unchanged. Line 189 mentions dependence on t only because alpha was fixed at the start; it would be clearer to say alpha and t.
- **CORRECT**, final free remark, lines 191193: infinitely many disjoint input gaps qualify. Their ordered images contain zero-density intervals bracketed by positive-density neighborhoods, hence lie in distinct bounded complementary components of the support. They give infinitely many support gaps, not merely zeros at isolated points.
- **GAP (verification attribution only)**, line 189: unavailable claims about the author's checks F1F4 have not been used; our own experiment follows.

Verdict: **CORRECT**, modulo the immediately available shrink of J and explicit angular-derivative convention. Neither requires a new estimate or theorem.

## 7. Independent free experiment

Command: `python3 audit.py 7 > step7.txt`. This uses the expressly offered finite measure 0.9 delta_0+0.07 delta_-4+0.03 delta_-16, alpha=1/2,t=1, not the paper's tiny weights, for the full density grid. It writes `step7_grid.csv` (2,602 numerical rows) and `step7_paper.csv`; no author code is imported. Damped complex Newton solves H(w)=x+i eps in C+, with H(w)=w-i sqrt(1/G_mu(w)), independently differentiated. Continuation is used along each grid, with a high-imaginary seed fallback. All accepted iterates have Im w>0; since the final Im H=eps>0, each root is in Omega, where H is univalent.

- **CORRECT**, numerical support mechanism. Scanning real G<0,H'>0 and bisecting the two H'=0 endpoints gives:

  | original atom gap | real w interval with H'>0 | image zero interval |
  |---|---|---|
  | (-16,-4) | (-14.603198031408,-4.417483675880) | (-9.978446953609,-2.770859350532) |
  | (-4,0) | (-3.131888592060,-0.283558951103) | (-0.920020912522,0.279591324434) |

  At c=-8, G=-0.12625 and I_2=0.01890625 give H'=0.789269052197 and H(c)=-5.185609821079, within the first zero interval.
- **CORRECT**, positive atom images. Solving Im H(s+i f(s))=0 gives:

  | atom s | f(s) | h(s) | density there |
  |---|---:|---:|---:|
  | -16 | 0.957884509213 | -12.374920619595 | 0.0111845314445 |
  | -4 | 0.582724228753 | -2.150020277282 | 0.0484924711226 |
  | 0 | 0.561234159812 | 0.554621986590 | 0.511231911173 |

  These are positive interior density values and persist in neighborhoods, both analytically and on the numerical grid.
- **CORRECT**, resolution/error check: the x grid [-18,8], spacing 0.02, at eps=1e-4 and 1e-7 has maximum residual <3.0e-13, with at most 14 Newton iterations after a successful seed. At the first gap midpoint -6.374653152070, the computed densities for eps=1e-4,1e-7,1e-10 are 5.161755781e-7,5.161755783e-10,5.161755782e-13. At the second midpoint -0.320214794044 they are 1.774552081e-5,1.774552066e-8,1.774552106e-11. These nonzero values are the expected finite-eps Poisson smoothing, not evidence against an exact limiting gap. Exact vanishing follows from the analytic real inverse, not a floating-point zero claim.
- **CORRECT**, paper midpoint calculation with the actual mu_*: minimal n>=2 satisfying [eq:nchoice] gives the following values, including every atom through N=max(3,n+1), and treating the remainder by its explicit bound:

  | alpha | t | n | A_n | H'(c) |
  |---:|---:|---:|---:|---:|
  | 0.1 | 1 | 6 | 2^64 | 0.988577700676240438 |
  | 0.1 | 100 | 7 | 2^128 | 0.986474243505732121 |
  | 0.5 | 1 | 3 | 256 | 0.955805826165166861 |
  | 0.5 | 100 | 5 | 2^32 | 0.998921040678121113 |
  | 0.9 | 1 | 2 | 16 | 0.984610694421876993 |
  | 0.9 | 100 | 4 | 65536 | 0.999136832542495556 |

  A second calculation by symmetric differences of the real function H at relative step 1e-20 agrees with every displayed digit. Omitted mass <=2^(-N-2) exp(-A_(N+1)^2); the largest such bound in these six cases is below 10^(-1.8652806e9). The omitted terms and adjustment of p_0 are negligible at the displayed precision. Full G,I_2,c and logarithmic error bounds are saved.

Verdict: **CORRECT**, numerical corroboration of the free mechanism; computations do not substitute for the analytic proof.

## 8. Independent classical experiment

Command: `python3 audit.py 8 > step8.txt`; outputs `step8_table.csv` and `step8_grid.csv`. Use alpha=1/2,t=1 and weights (0.85,0.07,0.05,0.03) at (0,-4,-16,-256). The full grid [-256,5] has spacing 0.01; a separate decrease check has 5,001 points on [-250,-200]. Runtime 0.082 seconds, peak RSS 21,856,256 bytes.

- **CORRECT**, observed strict decrease: every adjacent grid difference on [-250,-200] is negative; they range from -1.339740870e-6 to -5.370328975e-9. The exact derivative on this entire interval is 0.03 g_1'(x+256)<0, since all other terms vanish and x+256>=6>1/6. Thus the sign is analytically certified between grid points as well.
- **CORRECT**, positive density further left: q(-255.9)=0.0219674738429. Sample decreasing values are q(-250)=0.000552323909443, q(-240)=0.000130181867531, q(-225)=0.0000486375182873, q(-210)=0.0000269785919246, q(-200)=0.0000201046014222.
- **CORRECT**, this finite example is itself non-unimodal: the ordered triple (-255.9,-20,-15.9) has densities (0.0219674738429,0.00000233178369161,0.0366147287583). The middle value is strictly smaller than both outer values. Continuity makes this an obstruction to every monotone-density representative, not a dependence on three exceptional point values.
- **CORRECT**, role of infinitely many atoms: for this fixed t a finite mixture already suffices. The infinite sequence in the lemma is what produces decreasing intervals arbitrarily far to the left, defeating every possible finite mode and every finite tail-decrease threshold b_t with one fixed measure. The lemma's proof does not apply to arbitrary finite sequences; one atom gives an immediate unimodal example for the half-stable kernel, and compactly supported initial laws are eventually unimodal for this kernel under the quoted HU theorem. The finite experiment does not establish failure for all t.

Verdict: **CORRECT**, numerical and analytic confirmation of the classical mechanism.

## 9. Attributions and novelty  memory only

- **CORRECT as a plausible attribution, not authenticated**, HasebeUeda, lines 4551, 71, 229: I remember the Brownian/free Brownian eventual-unimodality setting and a stable-process conjecture, with moderate confidence. I do not independently remember the exact wording of Conjecture 5.5 or the exact hypotheses, atom direction and estimates of Proposition 5.4; those remain unchecked source assertions. The paper's quoted conjecture is unambiguously contradicted by the construction.
- **CORRECT**, mechanism behind the plus-infinity weight discussion, line 51, with a scope qualification. For the explicit half-stable kernel, the old density tails have negative derivative asymptotic to -(3t/(4 sqrt(pi))) x^(-5/2). A new atom can create an increasing piece at a fixed scaled location only if its positive derivative, of order p_n t^(-4), overcomes those slopes. At distance a_n this demands p_n a_n^(5/2) of order t^5 or larger in that particular method. To cover arbitrarily large t through such tail-dominating bumps forces an infinite 5/2-moment. This explains the stated construction; it is not an independent proof that every possible construction with atoms to +infinity has the same necessity. Outweigh the decreasing tails should explicitly refer to derivatives/slopes. The exact necessity asserted for HU's construction is not independently authenticated.
- **CORRECT**, classical/free Cauchy identity mentioned at line 51: phi_C=-it is constant, so F_(mu boxplus C_t)(z)=F_mu(z+it). The classical Cauchy convolution has the same G_mu(z+it), hence the measures coincide. The finite-third-moment eventual-unimodality theorem number is not verified.
- **CORRECT as an expected attribution**, HasebeKuznetsov (line 227): I recognize this free-stable parametrization and the positive rho=1 endpoint with high confidence. I do not certify the exact corollary number.
- **CORRECT as an expected attribution**, BercoviciVoiculescu (line 223): additivity of phi, the free LvyKhintchine characterization and unbounded-support free convolution are standard foundations I associate with them with high confidence. Exact section matching remains unchecked.
- **CORRECT as an expected attribution**, BercoviciPata/Biane (line 221): the stable-law and absolute-continuity discussion is consistent with my memory of this reference and Biane's appendix. I would not substitute a Brownian smoothing theorem for the specific stable-law result; here the transform calculation already confirms the needed stable regularity. Exact attribution confidence moderate.
- **GAP (bibliographical authentication only)**, HuangWang (line 231): the stated framework agrees with the Nevanlinna/subordination calculations above. I cannot independently certify authorship, arXiv identifier, proposition numbering or verbatim theorem hypotheses from memory. HW1, HW2 with its boundary convention and the locally used part of HW4 have been derived; global singular-part regularity and the full HW3 classification remain trusted general results.
- **GAP (novelty cannot be certified)**: I do not recall a specific earlier paper already refuting this conjecture, but my memory is not a literature search. No claim that the present paper is the first such refutation has been verified. I have invented no reference or purported quotation.

Overall mathematical verdict reached: **SOUND**. The main theorem survives the audit. There are wording repairs and unauthenticated attributions, but no missing estimate or counterexample to its proof was found. REPORT.md will give the consolidated table, numerical evidence, repairs and limits of this verdict.

## Final cross-check: the specialized free regularity can also be derived

The general HW3 classification and HW4 regularity theorem remain unverified citations. However, neither needs to be trusted for this particular discrete mu and stable phi. The proper bijection H on the closed graph domain has a continuous inverse up to the real boundary. At a boundary point with f>0, G_mu is analytic and finite. At a point with f=0, I(x,0)<=1 forces H to have a finite real boundary value. Such a point cannot be a mu-atom, by the direct power asymptotic above; it cannot be a zero of G_mu either, because then F_mu and phi(F_mu) would diverge. Since the atom set is closed and discrete, G_mu is meromorphic near every real point. Thus at all zero-height boundary points G_mu is finite, nonzero and real (indeed negative, since positive G would make Im phi<0 on the boundary).

Consequently G_(mu boxplus nu)=G_mu composed with H^(-1) extends continuously with finite values to every real point. Local uniform boundary convergence and Stieltjes inversion give an everywhere continuous density and no singular part. This independently verifies the application of HW4 in Step 1. Alternatively, non-unimodality itself needs only the analytic positive-density neighborhoods and the zero-measure interval, already derived; any hypothetical unimodal density representative would contradict those local pieces even without a global regularity theorem. This final check strengthens the SOUND verdict and separates theorem validity from source authentication.

Completed 12 November 2026, 06:04 +04: REPORT.md contains the consolidated verdict table, derivations, all requested numerical tables and commands, wording corrections, memory-only attribution assessment and unchecked items. The independent program and all numerical outputs are saved in this folder. PAPER.tex is unchanged. No browsing, helper agents, outside writes or git push was used.
