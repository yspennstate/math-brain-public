PARTIAL

# F0129: compactly supported self-repelling Brownian polymers

Completed 2026-11-13. The full zero-speed conjecture is not proved here. The partial result is an explicit energy and speed bound from zero initial drift when the primitive of f is positive definite, including a nonsmooth truncated-sign kernel. No novelty is claimed for this energy estimate. It is weaker than subballisticity. Literature checks and computations are recorded separately.

## Statement and source correction

Let B be standard one-dimensional Brownian motion, X_0=0, and

\[
X_t=B_t+\int_0^t\!ds\int_0^s f(X_s-X_u)\,du.
\]

In the original setup f is Lipschitz. Assume it has compact support, is odd, and x f(x) >= 0. The conjecture is X_t/t -> 0 almost surely.

Pemantle, *A survey of random processes with reinforcement*, Probability Surveys 4 (2007), Section 6.1, p.57, states the conjecture as:

> if f is a compactly supported odd function with xf(x) ≥ 0, then X_t/t → 0 almost surely.

Mathematical notation in this quotation has been rendered inline; the words and hypotheses are unchanged. [Source](https://arxiv.org/abs/math/0610076), saved as `sources/pemantle_2007.txt`, PDF/printed p.57.

There is no additional t^(2/3) conjecture on that page. Pemantle discusses the Tóth–Werner limiting process in Section 6.3, pp.64–65. Mountford–Tarrès (2008), p.33, and Tarrès–Tóth–Valkó (2012), reprint p.2, attribute the proposed t^(2/3) scaling for the finite-range polymer to Tóth–Werner. This is distinct from zero speed and from the superballistic long-range conjecture of Durrett–Rogers.

Durrett–Rogers (1992), Theorem 1, p.338, proves the finite deterministic upper bound on limsup |X_t|/t for bounded finite-range f. Their Theorem 2 on the same page gives liminf X_t/t >= gamma > 0 for nonnegative f with f(0)>0. Their Conjecture 1 is the corresponding strong law. Pemantle's historical summary attributes that strong law to Durrett–Rogers; the original theorem is weaker. [Original paper](https://sites.math.duke.edu/~rtd/reprints/paper73.pdf), saved as text only.

## Literature outcome so far

No printed theorem resolving the complete zero-initial-profile conjecture was found in the sources inspected. In particular:

* Mountford–Tarrès, Theorem 1, printed p.34 (PDF p.6): f(x)=x/(1+|x|^(1+beta)), 0<beta<1, has X_t/t^(2/(1+beta)) -> c_0 with probability 1/2; reflection gives the negative limit with probability 1/2. The kernel is not integrable and has no compact support. This resolves Durrett–Rogers Conjecture 3, not Conjecture 2. [Paper](https://www.numdam.org/item/AIHPB_2008__44_1_29_0/).
* Tarrès–Tóth–Valkó, Theorem 1 (IMS reprint p.4) and Corollary 1 (p.5): if f=-b', with b smooth, integrable and positive definite, the environment viewed from the particle has a stationary ergodic centered Gaussian law of covariance b. Zero speed follows for almost every initial profile under that law. The identically zero initial profile is not covered by this almost-everywhere statement. [Paper](https://arxiv.org/abs/0911.2356).
* Giles–Gräfner (2025), Section 1.1, p.3, explicitly excludes the initial field identically zero. Theorems 1.3–1.4, p.4, construct singular polymers with initial laws absolutely continuous with respect to the Gaussian reference law and give superdiffusive bounds in stationarity. [Paper](https://arxiv.org/abs/2509.05286).

The theorem-by-theorem audit follows. Page numbers refer to the saved version: printed pages where available; otherwise the numbered PDF/reprint page is stated explicitly. TTV's 19-page IMS reprint warns that its pagination differs from the journal, so no unverified journal-page conversion is used.

| Source | Exact locator checked | What it proves and why it does not settle F0129 |
| --- | --- | --- |
| [Durrett–Rogers, PTRF 92 (1992), 337–349](https://sites.math.duke.edu/~rtd/reprints/paper73.pdf) | Theorems 1–2 and Conjectures 1–2, p.338; Theorem 3 and Conjecture 3, p.339; Theorem 4, p.340 | The finite-range upper speed bound is general. The positive lower speed bound and one-sided strong-law conjecture concern nonnegative f. Conjecture 2 is the odd repulsive finite-range zero-speed problem; the long-range exponent 2/(1+beta)>1 belongs to a separate problem. |
| [Cranston–Le Jan, Math. Ann. 303 (1995), 87–93](https://doi.org/10.1007/BF01460980) | Theorem 1, p.89; Theorem 2, p.90; saved archive OCR | Almost sure convergence in the attractive cases f(x)=-a x and f(x)=-a sgn(x), a>0. The force sign is opposite to the present problem. |
| [Cranston–Mountford, Ann. Probab. 24 (1996), 1300–1323](https://doi.org/10.1214/aop/1065725183) | Original theorem number/page **not verified**: publisher and JSTOR access interstitials. Later primary account: Mountford–Tarrès, Section 1.5, p.32 | The later account gives a positive-speed strong law for nonnegative nonzero f in the finite-range Lipschitz setup. Pemantle's asserted neighborhood-only weakening was not verified. These statements do not give the odd repulsive case. See `sources/cranston_mountford_1996_access_note.txt`; this is a real gap in the source audit. |
| [Mountford–Tarrès, AIHP 44 (2008), 29–46](https://www.numdam.org/item/AIHPB_2008__44_1_29_0/) | Conjecture, p.33; Theorem 1, p.34; proof begins p.34 | Proves the special nonintegrable-tail theorem described above. The proof fixes that explicit kernel thereafter, using its one-peak shape and quantitative power-law tail. The drift can grow during a persistent excursion; that tail mechanism is absent for finite-range kernels. |
| [Tarrès–Tóth–Valkó, Ann. Probab. 40 (2012), 695–713](https://arxiv.org/abs/0911.2356) | Assumptions, reprint p.3; Theorem 1, p.4; Corollary 1 and Theorem 2, p.5; Theorem 3 and Lemma 1, p.6; remarks, p.7 | Smooth positive-type b, f=-b'; Gaussian stationary initial drift. Zero speed is pi-almost everywhere. For nonzero compact repulsive f in this class, b-hat(0)>0 and the parameter alpha=0: the upper MSD bound is O(t^(3/2)); the t^(5/4) lower bound is only in the Laplace-transform sense. Neither bound is the sharp MSD t^(4/3) law. |
| [Horváth–Tóth–Vető, PTRF 153 (2012), 691–726](https://arxiv.org/abs/1009.0401) | Proposition 2, Corollary 2, Theorem 2, saved preprint p.9 | Stationary Gaussian environment, dimension d>=3. Gives zero speed and a Brownian CLT there. The low-frequency integrability and graded-sector estimates are dimension dependent. |
| [Horváth–Tóth–Vető, *Relaxed sector condition* (2012)](https://arxiv.org/abs/1202.5915) | Theorem 1, saved preprint p.7 | Abstract sufficient condition for martingale approximation and a CLT for stationary Markov additive functionals. It does not verify those hypotheses for the one-dimensional flat-profile polymer. |
| [Tóth–Werner, PTRF 111 (1998), 375–452](https://math.bme.hu/~balint/cikkek/tsrm_ptrf.pdf) | Introduction pp.377–378; Proposition 3.5, p.395 | Constructs TSRM with exact 2/3 self-similarity and a local-time description. The introduction proposes it as a scaling limit for other models, including the Durrett–Rogers polymer. It does not prove that finite-range Brownian-polymer convergence. TSRM is not a semimartingale. |
| [Benaïm–Ciotir–Gauthier (2015)](https://arxiv.org/abs/1408.6397) | Periodic assumptions, preprint pp.2–3; Proposition 1, p.4; Proposition 6, p.15 | Existence and Gaussian invariant measure for periodic interactions, using a Fourier-coordinate lift. A periodic force on the line is not a compactly supported force. |
| [Benaïm–Gauthier (2016/2017)](https://arxiv.org/abs/1505.05664) | Theorem 2, saved preprint p.4; compact-manifold assumptions in the introduction | In particular, a zero-speed theorem from zero initial coefficients for the single-cosine periodic potential. Ergodic results for finite-mode compact-manifold interactions underlie the further periodic results cited by Gauthier. They do not give estimates uniform in the period tending to infinity. |
| [Gauthier (2017)](https://arxiv.org/abs/1703.02963) | Model and existing LLN, preprint pp.1–2; Theorem 2, p.6 | A stationary CLT for a finite positive cosine expansion of a periodic potential. Different force class and geometry. |
| [Kleptsyn–Kurtzmann, EJP 17 (2012), article 50](https://arxiv.org/abs/1005.5632) | Theorem 1, preprint pp.3–4; Theorems 3–4, p.5 | Uniformly convex attractive potentials; drift contains an average divided by t. Convergence of empirical measures up to translation and of their centers. Both the force and its normalization differ. |
| [Chambeu–Kurtzmann, Bernoulli 17 (2011), 1248–1267](https://arxiv.org/abs/0707.2908) | Model, reprint pp.1–2; Theorems 2.6–2.7, p.5 | Drift -g(t) grad V(X_t-mean_t), attractive around an empirical mean, not a convolution with the unnormalized occupation measure of a finite-range repulsive force. |
| [Cannizzaro–Giles, 2024 preprint; published online 2025, PTRF 194 (2026), 411–483](https://arxiv.org/abs/2403.06730) | Related work, preprint pp.2–3; Theorem 1.2, p.6 | Weak-coupling invariance principle in dimension 2. Discusses the unresolved sharp one-dimensional SRBP scaling, rather than proving it. |
| [Giles–Gräfner (2025)](https://arxiv.org/abs/2509.05286) | Assumption 1.1 and exclusion of zero field, p.3; Theorems 1.3–1.4, p.4 | Positive-type possibly singular potential; annealed initial laws absolutely continuous with respect to the Gaussian law. Extends construction and stationary superdiffusive bounds. Does not cover zero deterministic initial drift. |
| [Kosygina–Peterson (2025 preprint)](https://arxiv.org/abs/2502.10960) | Theorem 1, p.2 | Functional convergence of the discrete true self-avoiding walk to TSRM. This proves a discrete scaling limit, not the continuum finite-range conjecture. |
| [Kosygina–Marêché–Mountford–Peterson (October 2026)](https://arxiv.org/abs/2610.28935) | Theorems 2.4–2.6, pp.8–9 | Inversion of augmented joint Ray–Knight limits for recurrent discrete walks; applications to polynomial and true self-repelling walks. No theorem for the finite-range Brownian-polymer SDE. |
| [Lörler, 2025 preprint, January 2026 revision](https://arxiv.org/abs/2511.23333) | Assumption 1, p.3; Theorems 5–7, pp.8–10 | Rates of convergence for the finite-dimensional environment of compact-manifold self-repelling diffusions. Again not an infinite-line finite-range zero-speed theorem. |
| [Yu, *The self-repelling burglar* (October 2026)](https://arxiv.org/abs/2611.00854) | Theorem 1.3, p.3; model distinction, pp.1–2 | Conditional endpoints of polynomial self-repelling motion and TSRM. Does not identify a scaling limit of the SDE in this question. |

The inspected literature therefore establishes neither the full zero-speed conjecture from a flat initial profile nor the sharp 2/3 scaling for that class. In particular, no zero-speed theorem for the **zero-initial-profile truncated-sign finite-range kernel** was found. Its triangular primitive has positive type, but it does not meet TTV's printed smoothness assumption; smoothing it still leaves the initial-field restriction. The statement here is a search outcome, not a proof of nonexistence of any later result. The remaining direct-source limitation is Cranston–Mountford.

The positive-type finite-range class is nonempty even with TTV's smoothness assumption. Take a nonnegative, even, smooth bump psi supported on [-1/2,1/2] that decreases on the positive axis, and put b=psi*psi. This is a nonnegative smooth autocorrelation, hence positive definite. The convolution of two even decreasing functions is decreasing on the positive axis: by the layer-cake representation, reduce to indicators of centered intervals, whose translated overlap decreases with separation. Therefore f=-b' is an odd repulsive smooth finite-range kernel. The published zero-speed conclusion for this class still assumes Gaussian initial drift. Conversely, for any nonzero repulsive finite-range f, b>=0 implies b-hat(0)=integral b>0; hence TTV's diffusive summability integral of p^(-2)b-hat(p) diverges at zero. Their separate diffusive Theorem 2 does not apply to these kernels.

## Occupation measure and the mechanism

Write mu_t(dy)=integral_0^t delta_(X_s)(dy) ds. Because the quadratic variation of X is t, its semimartingale local time is also its occupation density, mu_t(dy)=L_t(y)dy. Set

\[
a_t(x)=\int f(x-y)\mu_t(dy),\qquad a_t=a_t(X_t).
\]

For a bounded, compactly supported, odd repulsive kernel define

\[
b(x)=\int_{|x|}^{\infty}f(r)\,dr,\qquad
U_t(x)=\int b(x-y)\mu_t(dy).
\]

Then b is even, nonnegative and compactly supported, and b'=-f almost everywhere. For continuous f this equality holds everywhere. Consequently the force is

\[
a_t(x)=-(\partial_x U_t)(x).
\]

Thus it is the negative gradient of the *smoothed* local-time potential b*L_t. In the notation of this problem it is not -(f'*L_t); f'*L_t is the spatial derivative of the force. For discontinuous f the force equality is interpreted almost everywhere, which suffices along the trajectory by the finite-horizon absolute-continuity argument below.

For support in [-R,R], oddness gives

\[
a_t=\int_0^R f(r)\{L_t(X_t-r)-L_t(X_t+r)\}\,dr. \tag{1}
\]

This is an exact identity. The conjectured mechanism is that a long excursion builds occupation behind the particle; a backward Brownian fluctuation then puts that occupation ahead and reverses the bias. Proving that the time integral of the signed imbalance in (1) is o(t) is the missing step. Symmetry of the *law* does not show cancellation along each path, and does not imply equality of the front and back occupation profiles.

## Complete partial proofs

### 1. Reflection symmetry for every bounded odd kernel

On each finite interval [0,T], |a_t|<=Mt where M=||f||_infinity. Girsanov's exponential satisfies Novikov's condition because integral_0^T |a_s|^2 ds <= M^2 T^3/3 deterministically. Tilting Wiener measure by the exponential with drift functional a_s(w)=integral_0^s f(w_s-w_u)du constructs a weak solution. The reverse change of measure shows that every weak solution has this same law: the Brownian Radon–Nikodym density is determined by the coordinate path and this drift functional. In particular, its path law is equivalent to Wiener measure on each finite horizon. For Lipschitz f, one also has the usual pathwise strong solution.

If (X,B) solves the equation, oddness implies that (-X,-B) solves the same equation. Brownian symmetry and uniqueness in law therefore imply

\[
(X_s)_{s\ge0}\stackrel{d}=(-X_s)_{s\ge0}.
\]

The bound |X_t|<=|B_t|+Mt^2/2 gives finite first moments, so E[X_t]=0 for every t. If X_t/t has a deterministic almost sure limit, reflection forces that limit to be zero. This does **not** prove existence of a speed, nor rule out a nonzero random speed with symmetric sign. For example, the unrelated process X_t=S t+B_t with an independent uniform sign S has the same reflection symmetry and mean zero, but X_t/t -> S and E|X_t|/t -> 1. This example only disproves the proposed inference from symmetry; it is not a counterexample to the polymer conjecture.

### 2. A bound from zero initial drift for positive-definite primitives

**Proposition.** Let f be bounded, measurable, odd and compactly supported, with x f(x)>=0. Let b(x)=integral_(|x|)^infinity f(r)dr be positive definite. For the polymer started with zero initial drift define A_t=integral_0^t a_s^2 ds. Then

\[
\mathbb E A_t\le b(0)t,\qquad
\limsup_{t\to\infty}\frac{A_t}{t}\le b(0)\quad\hbox{almost surely}, \tag{2}
\]

and therefore

\[
\limsup_{t\to\infty}\frac{|X_t|}{t}\le\sqrt{b(0)}
=\left(\int_0^\infty f(r)\,dr\right)^{1/2}\quad\hbox{almost surely}. \tag{3}
\]

Also E|X_t| <= sqrt(t)+sqrt(b(0)) t. These are linear bounds, not the conjectured o(t) bounds.

**Proof for smooth b.** Define

\[
D_t=\int_0^t\!\int_0^t [-b''(X_s-X_u)]\,du\,ds,
\qquad M_t=\int_0^t a_s\,dB_s.
\]

The kernel -b'' is positive definite. Indeed, for any finite set of points and real coefficients, the quadratic form for 2b(z)-b(z+h)-b(z-h) is the b-quadratic form of the signed measure sum_i c_i(delta_(x_i+h)-delta_(x_i)), hence nonnegative. Divide by h^2 and let h tend to zero. The same positivity for an occupation measure follows by Riemann approximation of its time integrals. Thus D_t>=0.

The time-dependent Itô formula applied to U_t(X_t) gives

\[
d[U_t(X_t)]=b(0)\,dt-a_t\,dB_t-a_t^2\,dt
-\frac12\left(\int_0^t f'(X_t-X_u)\,du\right)dt.
\]

Here the term from adding occupation at time t is b(0)dt, with no extra factor t. Since f'=-b'' is even, integrating its triangular time domain gives D_t/2. Hence

\[
A_t+U_t(X_t)+\frac14D_t=b(0)t-M_t. \tag{4}
\]

Every term on the left is nonnegative. The martingale is square integrable on [0,T], since A_T<=M^2 T^3/3. Taking expectations proves the first bound in (2).

**Removal of smoothness.** Choose a nonnegative even Gaussian approximate identity rho_epsilon, and let b_epsilon=b*rho_epsilon, f_epsilon=f*rho_epsilon. These b_epsilon are smooth, nonnegative and positive definite, and converge uniformly to b. Apply the preceding Itô calculation to U^epsilon_t(x)=integral_0^t b_epsilon(x-X_s)ds along the *fixed solution with force f*, not along a solution with force f_epsilon. With a^epsilon_s=integral_0^s f_epsilon(X_s-X_u)du, the result is

\[
\int_0^t a^\epsilon_s a_s\,ds+U^\epsilon_t(X_t)
+\frac14D^\epsilon_t
=b_\epsilon(0)t-\int_0^t a^\epsilon_s\,dB_s,\qquad D^\epsilon_t\ge0. \tag{5}
\]

The Lebesgue differentiation theorem gives f_epsilon -> f off a Lebesgue-null set. Finite-horizon equivalence with Wiener measure implies that, for each fixed 0<=u<s, X_s-X_u has a density. Fubini and dominated convergence therefore give a^epsilon_s -> a_s for almost every (s,omega), and in L^2([0,T] times probability), since |a^epsilon_s|,|a_s|<=Ms. The integrals against a_s converge uniformly in t<=T almost surely. Doob's inequality gives uniform-in-time L^2 convergence of the stochastic integrals; choose a subsequence converging uniformly almost surely. The potential terms converge uniformly by the uniform convergence of b_epsilon. Dropping D^epsilon_t from (5) and passing to this subsequence yields, simultaneously on [0,T],

\[
A_t+U_t(X_t)\le b(0)t-M_t. \tag{6}
\]

Intersecting the probability-one events for integer T gives (6) for all t>=0. Expectations yield E A_t<=b(0)t also in the nonsmooth case.

For completeness, M_t/A_t -> 0 on {A_infinity=infinity}. The standard exponential-martingale inequality gives, for v,z>0,

\[
P(\sup_{s:A_s\le v}|M_s|\ge z)\le2\exp[-z^2/(2v)].
\]

Take v=2^(n+1), z=epsilon 2^n and sum over n. Borel–Cantelli, followed by a countable sequence epsilon down to zero, proves the assertion. From (6), eventually (1-epsilon)A_t<=b(0)t whenever A_t grows without bound. If A_infinity is finite, A_t/t -> 0 directly. Letting epsilon decrease to zero proves the second assertion of (2). Finally, Cauchy–Schwarz and the Brownian strong law give

\[
\frac{|X_t|}{t}\le\frac{|B_t|}{t}+\sqrt{\frac{A_t}{t}},
\]

which proves (3). The expectation bound follows from Cauchy–Schwarz and E|B_t|<=sqrt(t). This completes the proof.

**Truncated sign.** For f(x)=sgn(x) 1_(|x|<1), with f(0)=0 and any endpoint convention, b(x)=(1-|x|)_+. It is positive definite because b is the convolution of the indicator of [-1/2,1/2] with its reflection: its quadratic forms are integrals of squares. The proposition therefore proves E integral_0^t a_s^2 ds<=t and limsup |X_t|/t<=1. It does not prove zero speed or a t^(2/3) growth law for this f. Endpoint conventions do not affect the process law by the same finite-horizon absolute-continuity argument used above.

### 3. Why the extra hypothesis is a real restriction

Define, for x>0,

\[
f(x)=48(x-1/2)(1-x)1_{(1/2,1)}(x),
\]

and extend oddly, with f(0)=0. This is globally Lipschitz, bounded, compactly supported and repulsive. Its positive integral is 1, because integral_a^b (x-a)(b-x)dx=(b-a)^3/6. The primitive satisfies b(0)=b(1/2)=1 and b(1)=0. Its matrix at the three points 0,1/2,1 is

\[
K=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}.
\]

For c=(1,-1,1), c^T K c=-1. Thus b is not positive definite. This is a counterexample to an attempted extension of the Gaussian/positive-type method, **not** to the zero-speed conjecture. It already has only one nonnegative piece on the positive axis.

The suggested class “nonincreasing in |x|” needs a regularity qualification: if odd f is continuous at zero, f(0)=0, and f is nonnegative and nonincreasing on (0,R), then f is identically zero, by f(r)<=lim_(s down to 0) f(s)=0. Nonzero examples in that class, such as the truncated sign, necessarily have a jump at zero.

### 4. A finite-history extension of the stationary result

This proposition concerns a Gaussian initial field, not the original flat initial field. Assume the smooth positive-type hypotheses of Tarrès–Tóth–Valkó, and let omega have their stationary centered Gaussian law pi of covariance b. For any deterministic continuous path gamma:[0,T]->R, let

\[
h(x)=\int_0^T f(x-\gamma(s))\,ds.
\]

Then the polymer with initial drift omega+h has zero speed almost surely.

To recall the published zero-speed implication precisely, put eta_t(x)=xi(X_t+x)+integral_0^t f(X_t+x-X_s)ds and phi(eta)=eta(0). TTV Theorem 1 makes eta stationary and ergodic when xi has law pi. The ergodic theorem gives t^(-1) integral_0^t phi(eta_s)ds -> integral phi d pi=0, since phi is an integrable centered Gaussian observable. Together with B_t/t -> 0 this proves zero speed under the joint initial-field and Brownian law. Conditioning gives TTV Corollary 1 for pi-almost every initial field; it says nothing about exceptional fields.

**Proof.** The Gaussian variable Z=integral_0^T omega'(gamma(s))ds is well defined in L^2, with variance sigma^2<=T^2[-b''(0)]. Differentiating the covariance gives Cov(omega(x),Z)=integral_0^T [-b'(x-gamma(s))]ds=h(x). Tilt pi by the strictly positive density exp(Z-sigma^2/2). The joint Gaussian moment-generating formula shows that under this tilt each finite vector of evaluations of omega has mean h and unchanged covariance b. Thus the tilted law is precisely the law of omega+h. It is equivalent to pi. The probability-one set of good initial profiles in TTV Corollary 1 therefore also has probability one under the shifted law. Applying that corollary proves the claim. The same conclusion holds for an independent random finite path by conditioning. No claim is made for a path chosen dependently on omega. End of proof.

This transfer argument cannot create the deterministic zero field: if b(0)>0 then pi({omega identically zero})<=P(omega(0)=0)=0. Absolute continuity therefore cannot transfer a pi-almost-everywhere statement to that singleton.

### What remains unproved

No argument above establishes X_t/t -> 0, liminf |X_t|/t=0, or E|X_t|=o(t) for all kernels in the question. The energy identity allows A_t of linear order and a nonzero time-average of a_t. Positive definiteness alone also does not transfer stationarity to a flat initial field. Neither issue is removed by reflection symmetry. The new computations below are evidence only.

## Computation: scheme and kernels

All numerical jobs ran sequentially in a single-thread C++ program at nice 10. Numerical-library thread limits are set to one in the Python analysis. The grid has 262145 nodes; its occupation-mass and drift arrays together occupy 4,194,320 bytes. The simulator's resource audit measured approximately 16.3 MB peak resident memory for its self-test, well below 4 GB; this is not a measurement of every long job. No process was launched in a terminal window.

The Euler scheme stores unnormalized occupation **mass**, rather than a normalized empirical measure. At time n*dt, write x/h=j+theta. Split an occupation increment dt between grid nodes j and j+1 with weights 1-theta and theta. If m_k is accumulated mass, set F_j=sum_k m_k f(h(j-k)). The evaluated force is (1-theta)F_j+theta F_(j+1). Use

\[
x_{n+1}=x_n+\sqrt{dt}\,Z_n+dt\{(1-\theta)F_j+\theta F_{j+1}\}.
\]

The increment is evaluated before depositing the current dt of occupation. The cached drift array is then updated with the exact convolution of the two new deposits. This is equivalent to direct summation over the linearly interpolated past grid deposits. There is no cutoff in time or omission of older occupation; finite support makes each update local in space. The grid boundary causes an error exit rather than reflection or wrapping. No boundary exit occurred.

There are five repulsive kernels, each normalized by integral_0^infinity f=1; values below are on x>0 and extended oddly. All vanish outside [-1,1]. The sixth kernel is f=0, a Brownian control.

| Code name | Positive-axis force |
| --- | --- |
| `sign` | 1 on (0,1), with f(0)=0 |
| `spline` | 12x-18x^2 on (0,1/2); 6(1-x)^2 on [1/2,1) |
| `bump` | 2x(1-x^2)^(-2) exp(1-1/(1-x^2)) on (0,1) |
| `annular` | 48(x-1/2)(1-x) on (1/2,1) |
| `two_bump` | (g_(0.1,0.4)(x)+g_(0.65,1)(x))/2, where g_(a,b)(x)=6(x-a)(b-x)/(b-a)^3 on (a,b) and 0 elsewhere |

The spline primitive is b(x)=1-6r^2+6r^3 for r=|x|<=1/2, and 2(1-r)^3 for 1/2<=r<=1. It is a rescaled cubic B-spline, hence a fourth convolution power of a centered interval indicator with nonnegative Fourier transform. It satisfies the proposition's positive-type hypothesis. The annular kernel is exactly the obstruction proved above.

The force interpolant changes the effective positive integral slightly at finite h. In particular, for `sign` it is 0.95 at h=0.05 and 0.975 at h=0.025 under the stated endpoint convention. The target continuum integral remains 1. All grid and continuum integrals are recorded in `data/kernel_checks.csv`; this spatial bias is part of the discretization error.

## Numerical results and limits

The first run used 48 independent seeds per kernel, T=8192, dt=0.02 and h=0.05. A finer long run used 64 new independent seeds per kernel, T=8192, dt=0.005 and h=0.025. Three short refinement runs used the same 32 seeds and the same Brownian increments, aggregated from base step 0.005: (dt,h)=(0.02,0.05), (0.02,0.025), and (0.005,0.025), up to T=1024. The first path's final occupation grid is also saved for each kernel in the newer runs.

The truncated-sign, spline and two-bump long runs passed the recorded stiffness check: their largest dt times the negative local slope of the cached drift were respectively 0.121, 0.086 and 0.514 on the finer mesh. Largest drift increments were respectively 0.0258, 0.0291 and 0.0454 in spatial units. This is a numerical plausibility check, not a convergence theorem for an unbounded time interval.

The following table uses the 64-path finer long run. The exponent is the slope of log ensemble RMS displacement against log t over the six checkpoints 256,512,1024,2048,4096,8192. The interval is a percentile bootstrap interval, resampling whole independent paths 2000 times; it measures sampling variation for this finite-time fit only.

| Kernel | RMS(X_256)/256 | RMS(X_8192)/8192 | Sample mean absolute X_8192 / 8192 | RMS exponent, t=256–8192 | Bootstrap 95% interval |
| --- | ---: | ---: | ---: | ---: | ---: |
| truncated sign | 0.2410 | 0.0731 | 0.0628 | 0.638 | [0.586, 0.691] |
| spline | 0.1873 | 0.0772 | 0.0663 | 0.732 | [0.669, 0.793] |
| two bumps | 0.2580 | 0.0861 | 0.0694 | 0.676 | [0.618, 0.726] |
| Brownian control | 0.0534 | 0.0129 | 0.0102 | 0.581 | [0.518, 0.643] |

The table uses RMS, so it does not rely on cancellation of signed endpoints. These finite-time measurements are compatible with declining normalized displacement. They do not prove almost sure zero speed, exclude rare persistent excursions, or determine a limiting exponent. For example, moving the fit window to 1024–8192 changes the three polymer slopes to 0.608, 0.723 and 0.695. Even the exact Brownian control, whose true exponent is 1/2, gives a noticeable finite-sample slope error. The separate 48-path coarse Brownian control gives 0.503 over 256–8192. No seed or path was removed for its endpoint.

**Stiff kernels were excluded from this exponent table.** The long annular run at dt=0.02 had a drift step as large as 6.07, exceeding the interaction range. Reducing dt to 0.0005 at T=1024 still produced a maximum negative-slope product 2.55, above the deterministic Euler stability threshold 2 for a linear restoring drift. A shorter annular run with dt=0.00005, h=0.0125, T=256 and 32 paths reduced that product to 0.0215 and the largest drift step to 0.00502. Its endpoint RMS was 61.82, but this short horizon does not establish a growth exponent.

The smooth bump also became stiff in a few long finer-mesh paths: maximum negative-slope product 13.61, largest drift step 1.92, and sample drift energy A_T/T=135.7. A separate shorter run at dt=0.0005, h=0.025 and T=1024 had maximum negative-slope product 0.0401 and drift step 0.00695. Thus neither long smooth-bump nor long annular exponents should be used as continuum evidence. Their checkpointed trajectories and diagnostics are retained, with exclusion flags in the exponent CSV files. `data/growth_fine.png` displays only the three numerically better-controlled kernels and Brownian control; the earlier plot retains and labels the stiff runs.

The paired T=1024 refinement runs gave RMS ranges 143.48–153.03 for truncated sign, 123.75–130.83 for spline, and 144.29–159.70 for two bumps. These differences are comparable to the Monte Carlo uncertainty of 32 paths; they provide a resolution check, not certified mesh convergence. The coarse and fine long runs use different independent seeds, so differences between their exponents combine sampling and discretization error.

## Checks, artifacts and reproducibility

* `sources/` contains only plain text, with retrieval URLs, SHA-256 hashes and PDF page counts in `.metadata.txt` files. PDFs were held in RAM and converted using `pdftotext -layout - -`; none was saved. Cranston–Le Jan is archive OCR, with its formula-corruption warning preserved.
* `code/polymer.cpp` implements the Euler scheme; `code/reproduce.sh` lists the exact sequential simulation commands. `code/analyze.py` creates summaries, path-bootstrap intervals, stiffness flags and plots. `code/audit_math.py` independently checks parity, repulsion, normalization and the exact covariance obstruction.
* The simulator's short deterministic audit compares cached force against an O(N^2) summation over all past interpolated deposits, checks reflected noise/path symmetry, and checks deposited mass. Maximum errors were 5.33e-15, 1.78e-15 and 3.55e-15 respectively. With f=0, every recorded X equals its accumulated Brownian increments exactly.
* In the first long run the largest cached-force discrepancy was 4.26e-14 and occupation-mass discrepancy was 7.28e-11. These checks establish the implementation's convolution consistency, not the accuracy of a stiff Euler approximation.
* The annular normalization was rechecked with exact rational arithmetic and numerical quadrature; c^T K c=-1 was rechecked exactly and its negative eigenvalue is approximately -0.4142. The energy proof was audited by integrating Itô's formula first for b(X_t-X_u) at each fixed past time u; symmetry of the triangular time integral gives the factor 1/4 in (4).
* `data/main.csv`, `data/main_fine.csv`, the refinement CSV files and final occupation CSV files are raw numerical evidence. `data/summary.csv`, `data/main_fine_summary.csv`, exponent tables and `data/extra_checks.json` contain derived quantities. No empirical exponent is treated as a theorem.

The outstanding mathematical task is a sublinear bound for the time-integrated occupation imbalance from **zero initial drift**, uniform across the stated kernel class. Neither a proof nor a counterexample to that task was obtained here.

Task: “Open problem F0129” — received 2026-11-13 approximately 11:11 +04; exact message seconds were unavailable (first local clock reading 11:11:25).
