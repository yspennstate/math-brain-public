# PD08: non-uniqueness of Leray-Hopf solutions of the unforced 3D Navier-Stokes equations

Row PD08 of the top-200 general list (DESERVE.tsv line 525). Checked 12 Nov 2026 by an agent.

## Status

Claimed solved, twice, by groups around the same senior author, and not confirmed by anyone else.

1. T. Y. Hou, Y. Wang, C. Yang, arXiv 2509.25116 (29 Sep 2025; v2 19 Mar 2026; 74 pages). Computer-assisted.
   Theorem 1: there are infinitely many distinct suitable Leray-Hopf solutions on R^3 x [0,1] with the same
   compactly supported divergence-free initial datum, smooth away from the origin and in L^q for every q < 3.
   The solutions lie in L^s_t L^q_x for 2/s + 3/q > 1, so they miss the Prodi-Serrin class only at the endpoint.
2. T. Y. Hou, Qin, Song, Zhang, arXiv 2611.06117 (4 Nov 2026; 113 pages). Stated to be entirely analytic: a
   cascade through geometrically separated Gaussian swirls gives a continuum of distinct suitable Leray-Hopf
   solutions from one axisymmetric datum in L^q (1 <= q < 3), not in L^3, with solutions in L^inf_t L^{3,inf}_x.
   Abstract read only.

Three dated arXiv searches (31, 4 and 2 entries; lit/search) show no independent confirmation and no dispute of
either paper. Related work that uses the same mechanism or bears on the program: Dahne-Sverak 2609.08985
(computer-assisted non-uniqueness for complex Ginzburg-Landau through an unstable eigenvalue of a self-similar
profile), Binz-Coiculescu 2607.12159 (a Liouville theorem for homothetic self-similar solutions), Guillod-Sverak
1704.00560 (the numerical evidence the program started from), Albritton-Brue-Colombo (the forced case).

Proposal for the list: keep PD08 as REPORTED_SOLVED, off the attack list, not marked solved.

## The argument of 2509.25116

The route is the Jia-Sverak program. Theorem 2 gives an exact self-similar profile U (even in z) and an exact
unstable eigenpair (v, lambda) of the linearization around it (v odd in z, so the instability breaks the
symmetry). Both are obtained from a numerical approximation by a fixed-point argument whose hypotheses
(Assumption 1, Propositions 1 and 2) are verified with interval arithmetic: residuals 6.5e-7 for U and 1.9e-5
for v, approximate eigenvalue -0.11314 in their sign convention, coercivity about 0.051 (U) and 0.164 (v).
The linearized operator is split into a coercive part and a compact part approximated at rank 25, on a
spectral basis of N = 1257 (U) and N = 1260 (v) Stokes eigenfunctions of the ball of radius 32.
Section 2.2 then localizes: Bogovskii decomposition of the self-similar datum, a cutoff correction, and a
Duhamel fixed point in which the coordinate along the unstable direction is free, which gives infinitely
many solutions. The exponent range 2/s + 3/q > 1 is what the scaling t^{-1/2} U(x / sqrt t) gives.

The authors' code is public: github.com/HouGroup2026/3d-navier-stokes-nonuniqueness (head commit
615ee6f3eca3abad7b5814fe9334bcd80bea0328, last push 23 Mar 2026; Julia sources, six notebooks, data files;
listing in lit/repo_listing). We did not run it.

## What was checked here (pd08_check.py, pd08_check.out)

A. Section 4.5, the closing chain of inequalities. From the constants (4.44)-(4.63) we recomputed the 20
printed steps (M1, M2U, M3U, M4U, x0U, x1U, y0U, y1U, lambda_con, eps5, M5, M2v, M0, M3v, M4v, x0v, x1v,
lambda_lin and the total eigenvalue shift). 19 reproduce. Two remarks:

- x0U is printed as <= 1.44e-5. With the bound M2U <= 0.0061 stated just above it the value is 1.4506e-5;
  the printed figure is what 0.005 in place of 0.0061 gives. A slip in the third digit.
- (4.29), (4.30) and the values y0U <= 1.3e-7, y1U <= 4.8e-7 use the first power of the Frobenius norm 0.025
  of the Gram matrix G_{Q^2} of (4.18). For a Gram matrix G of vectors w_j the inequality is
  sum_j <U1, w_j>^2 <= lambda_max(G) |U1|^2, which gives the square root of that norm, as the paper itself
  uses in M3U and M3v. With the square root: y0U <= 8.24e-7, y1U <= 3.05e-6.

Neither changes the conclusion. With both read conservatively the chain still closes: M4U = 0.0020155 > 0,
1 - M1 = 0.06995 > 0, M5 = 0.1551, M3v = 8.789, M4v = 0.0209 > 0, and the eigenvalue moves by at most
0.0045 against |lambda| = 0.113, so it stays on the unstable side.

B. Section 6.2, the size of the spectral basis. We counted the roots of the two eigenvalue equations of
Lemma 4, (6.3) and (6.4), for the ball of radius 32 (sign changes on a grid of step 0.004, the same count at
step 0.002, each root then located by bisection). Below the scaled value 10 there are 1291 eigenvalues in the
parity class of U and 1287 in the class of v (1286 plus the zero mode); the paper takes N = 1257 and 1260.
At the paper's N our (N+1)-th eigenvalue is 9.769 (U) and 9.778 (v), not above 10, so the sentence
"we need lambda_{N+1} > 10 ... thus N = 1257 for U and N = 1260 for v" does not match our count. The bound
the proof actually uses does hold there: K5 = 4.5 / (0.005 + lambda_{N+1}) is 0.4604 (U) and 0.4600 (v),
below the 0.47 used in Section 4.5 (0.47 needs lambda_{N+1} >= 9.57, which our count places at N >= 1233
and 1240). So Section 4.5's K5 <= 0.47 is consistent with N = 1257 and 1260, and the "0.45" and "> 10" of
Section 6.2 read as loose wording. This rests on our own root count and our reading of the parity rule of
Remark 9 (U: even l for the Y family, odd l for the Z family; v the other way); part C compares it
with the authors' own root file and settles the count.

C. The authors' root file (pd08_mat_dump.py, pd08_zeros_cmp.py, pd08_zeros_cmp.out). data/bessel_zeros.mat at
commit 615ee6f3 (48,392 bytes, sha256 731f0c56ece56e736d5e16dd00c8503755cc22a1e86d47bb9ca59f038fb84a54) holds 2,516 roots: every root
of (6.3) and (6.4) below 100, for l = 1 to 96 in the Y family and 1 to 95 in the Z family. The notebook that
wrote it, notebooks/get_bessel_zeros.ipynb, asks for all roots below 100. Our own roots below 100 are the same
2,516, family by family and l by l; the largest difference between a root of theirs and ours is 7e-13. Under
the parity rule of Remark 9 they split into 1257 in the class of U and 1259 in the class of v, 1260 with the
zero mode. These are the paper's N exactly, so the parity reading above is right, and N is "every
eigenfunction whose root is below 100", that is, scaled eigenvalue below (100/32)^2 = 9.7656. The next
eigenvalue is 9.769 (U) and 9.778 (v). The sentence of Section 6.2 that asks for lambda_{N+1} > 10 does not
describe what was computed; the proof needs K5 <= 0.47 only, and that holds with room (0.4604 and 0.4600).
The basis the paper says it used is the basis in the authors' repository.

## The second paper (arXiv 2611.06117), first reading

Hou, Qin, Song, Zhang, "A viscous cascade construction of nonunique Leray-Hopf solutions to the unforced 3D
Navier-Stokes equations", v1 of 4 Nov 2026, 113 pages (lit/2611.06117). Read: the abstract, Theorem 1.1,
Remark 1.2 and Section 1.3, from the text extraction, which drops the symbols; the pages were not looked at.

It is not an analytic version of the first paper. The first paper perturbs a self-similar profile (the
Jia-Sverak route) and needs interval arithmetic. This one has a different datum and a different mechanism,
and computes nothing numerically.

Statement (Theorem 1.1). An axisymmetric divergence-free datum, smooth away from the origin, in L^p for
1 <= p < 3 and in weak L^3, not in L^3; a reference solution and a one-parameter family of pairwise distinct
solutions on a common time interval. All are suitable Leray-Hopf solutions with strong L^2 initial trace,
global and local energy equality, smooth for t > 0, in L^r_t L^q_x whenever 2/r + 3/q > 1, and bounded in
time with values in weak L^3.

Mechanism. The datum is a sum of Gaussian swirls, velocity of order A/l at radial scale l, placed at
l = 1, 1/Lambda, 1/Lambda^2, ..., and corrected to an exact solution. A perturbation at a small scale grows on
the swirl there; its quadratic stress, integrated over the growth time, drives the next larger scale; and so
on up to scale one. At each finite depth a shooting argument fixes a terminal coordinate, the L^2 size of the
initial perturbation tends to zero with the depth, and compactness gives the limit solutions.

Checked here.

- Against the uniqueness theorems. The family lies strictly outside the Ladyzhenskaya-Prodi-Serrin class
  2/r + 3/q <= 1. The datum is not in L^3, where Leray-Hopf solutions are unique. It is in weak L^3 only,
  and the paper itself proves (Proposition A.1, Remark 1.2) that a bound in L^infty_t L^(3,q) with q finite
  would force uniqueness, so the endpoint it reaches is the only one left open. The scaling is consistent:
  velocity A/l at scale l is the critical scaling; |u_0| of order 1/|x| near the origin is in L^p locally
  exactly for p < 3 and in weak L^3; a perturbation comparable to the swirl at scale l has L^2 norm of order
  A l^(1/2), which tends to zero; the time spent at scale l is of order l^2, summable. Nothing in the
  statement contradicts a known theorem.
- The step that stands where the first paper has a computed eigenvalue. For the swirl u_theta = r exp(-r^2/4)
  the circulation is Gamma = r^2 exp(-r^2/4) and the Rayleigh discriminant is
  r^-3 d(Gamma^2)/dr = (4 - r^2) exp(-r^2/2). Its negative, (r^2 - 4) exp(-r^2/2), is positive outside r = 2
  and has maximum 2 e^-3 at r = sqrt 6. These are the potential, the neutral radius and the maximum stated in
  Section 1.3. So the instability is the classical centrifugal one of a swirl whose circulation decays
  outward, with inviscid growth rate up to (2 e^-3)^(1/2) A = 0.316 A at high axial frequency. Recomputed by
  hand.

Not read: Sections 2 to 9 and the appendices, in particular Lemma 4.2 (the radial variational problem),
Lemmas 4.4 to 4.6 (growth with viscosity and a moving eigenspace), Lemma 4.9 (the sign of the complete
quadratic stress, on which the transfer to the next scale depends), Proposition 7.7 (the transfer),
Proposition 8.1 (one nonlinear transition), the selection of a finite cascade in Section 8.4 and the
compactness of Section 9. The paper is a first version, eight days old. This reading does not change the
row's status.

## Not checked

The interval-arithmetic code and its outputs (the numerical constants entering Section 4.5 are taken as
printed); Sections 2, 3, 5 and 7 beyond the statements and outline; Appendices; 2611.06117 beyond the first reading above.

## What would upgrade the row

An independent rerun of the authors' notebooks, or a referee'd publication of either paper, or a third
group's proof. The second paper, if it stands, makes the computer-assisted one unnecessary for the row.

## Second paper (arXiv 2611.06117): Lemmas 4.7 to 4.9 from the pages (12 Nov, 07:15)

Read on PDF pages 43 and 45 to 51 (the text extraction drops every Greek letter, so nothing here is taken from
it). Notation: W_tau(r) = r tau^-2 exp(-r^2/(4 tau)), zeta = r^2/(4 tau), U_d = A W_{1+t} e_theta,
B_tau = W' + W/r, Omega_tau = W/r, C_tau = W' - W/r, chi0 = e - 2,
mG(zeta) = int_0^1 (e^{1-y} - 1) e^{y zeta} dy, F_v(t, r) = int v_r v_theta dz.

Lemma 4.7 (exact stress and mean identities). Each step redone by hand:
- angular integration of v (x) v gives s_h - s_z = pi (E - 3Z); the two mixed tensors give
  2 pi A int W_{1+t} mu_theta[w] r dr on each horizontal entry and nothing on the vertical one;
- the azimuthal component of (v . grad) v is d_r(v_r v_theta) + d_z(v_z v_theta) + 2 v_r v_theta / r for a
  solenoidal axisymmetric v, so the axial mean of w_theta solves the radial heat equation with source
  -(d_r + 2/r) F_v; the linear term -A B w_r has zero axial mean because int w_r dz = 0;
- int W (-d_r - 2/r) F r dr = int C F r dr, and C_tau = -(r^2/(2 tau^3)) exp(-zeta);
- -2 int_0^inf C_{tau+2h} dh = (8/r^2)(1 - (1 + zeta) exp(-zeta)) = K_hist(tau, r), and K_hist <= 2/tau;
- exchanging the order of integration in (4.44) gives the two kernels K_hist(1+s, r) and K_hist(1+2te-s, r) of
  (4.46) with the stated signs, and |R| <= pi A/(1+te) int E because int |F| r dr <= E/2;
- int_{te}^inf W_{1+2t-te} dt = (2/r)(1 - exp(-r^2/(4(1+te)))), which gives (4.47).

Lemma 4.8 (sign of the high-frequency history). Each step redone by hand:
- the integral for mG equals ((e^zeta - 1 - zeta)/zeta - chi0)/(zeta - 1), so (zeta - 1) mG is the expression
  of (4.53); mG is a difference quotient of a convex function, hence increasing, with mG(0) = chi0;
- K_hist(tau, r) = -B_tau tau mG + 2 chi0 tau Omega_tau: both sides are (2/(tau zeta))(1 - (1 + zeta) exp(-zeta));
- the linearised azimuthal equation is (d_t - Delta_1) v_theta = -A B v_r and the meridional energy identity is
  E_mer'/2 + D_mer = 2A int Omega F r dr (the two transport terms were recomputed in cylindrical coordinates);
- (d_t + d_r^2 + d_r/r)(tau mG(zeta)) = mG + (1 - zeta) mG' + zeta mG'';
- with D >= 4E on axial frequencies |k| >= 2 and tau >= 1 the four terms after Q'/2 are at least 3Q, and
  Q >= chi0 E >= E/2; inserting into (4.46) gives (4.52) with the coefficient pi (1/2 - A/(1+te)).

Numerical check (pd08_weight_check.py, pd08_weight_check.out; 40 digits, a grid of tau and r, zeta from 0 to
80): the formula for C, the kernel identity (4.49), the weight identity (4.53) and the time integral behind
(4.47) hold to 1e-32 or better; 0 <= K_hist <= 2/tau; chi0 <= mG <= chi0 e^zeta with mG increasing;
(1 - zeta) mG' + zeta mG'' <= mG everywhere on the grid, the left side being at most 0.31 mG, so the inequality
(d_t + Delta_h) m_G <= 2 m_G / tau of the proof holds with room.

Lemma 4.9 (the complete signed history). The proof is an assembly: the first variation is split at axial
frequency two, Parseval removes the cross terms, the low part is bounded through Lemma 4.6, the high part gets
its sign from Lemma 4.8 (for te = tp + L with L >= 4A the coefficient 1/2 - A/(1+te) is at least 1/4), and the
lower bound (4.56) on the energy of a fixed frequency band absorbs the two error terms because
G > c_* - eta_low. The assembly is correct as written. It rests on Lemma 4.2 (the growth rates sigma_k),
Lemma 4.4 (the lower bound on a band), Lemma 4.5 (the size of the prepared seed), Lemma 4.6 (the low-frequency
deficit) and the energy bound (4.4), none of which has been read here yet. The value c_* = sqrt 2 e^{-3/2} of
(5.1) is the square root of the maximum 2 e^{-3} of the centrifugal potential recomputed earlier.

No error found in Lemmas 4.7 to 4.9. The mechanism that turns the linear instability into a signed stress is
an exact identity plus one weighted energy estimate, and both check.

## Second paper (arXiv 2611.06117): Lemmas 4.1 to 4.6 from the pages (12 Nov, 07:18)

Read on PDF pages 30 to 44. Notation as in the previous section; Phi(r) = (4 - r^2) exp(-r^2/2) = 2 Omega_1 B_1.

Lemma 4.1 (sharp energy estimate (4.4), coupling bound (4.5)). Redone by hand:
- with the azimuthal weight F = 1/(1 - zeta) for zeta <= 1/2 and 2 beyond, 2 Omega - F B vanishes inside and
  |2 Omega - 2B|/(2 sqrt 2) = tau^-2 (2 zeta - 1) e^-zeta / sqrt 2 outside, largest at zeta = 3/2 with value
  sqrt 2 e^{-3/2} tau^-2 = c_* tau^-2;
- (d_t + d_r^2 + d_r/r) F(zeta) = (zeta F'' + (1 - zeta) F')/tau = F (1 + 2 zeta/(1 - zeta)^2)/tau <= 5F/tau on
  zeta <= 1/2; the corner at zeta = 1/2 has the helpful sign;
- the Hilbert-Schmidt integral is 2 tau^-3, the norm of B_tau in L^2(r dr) is sqrt 2 tau^{-3/2}, |v_r(r)| <=
  |k| ||v_z|| / sqrt 2, and the time integral of sqrt 2 A |k| tau^{-3/2} is 2 sqrt 2 A |k|.

Lemma 4.2 (the radial variational problem, sigma_k < c_*, increasing, limit c_*). Redone by hand:
- sigma^2 L_k f = -k^2 Phi f with Rayleigh quotient int(-Phi)|h|^2 r dr / (||h||^2 + k^-2 ||D_r h||^2); the
  maximum of -Phi is 2 e^-3 = c_*^2 at r^2 = 6, so sigma_k < c_*, and the quotient of a fixed h increases with k;
- the trial function (1 - (r^2 - 6)^2/delta^2)_+ has squared norm 8 delta/15 and derivative energy 32/delta;
  -Phi(sqrt(6 + x))/c_*^2 = (1 + x/2) e^{-x/2} >= 1 - x^2/4 on |x| <= 1; with delta = 4/sqrt k and k >= 16 this
  gives sigma_k^2/c_*^2 >= (1 - 4/k)/(1 + 15/(4k) + 1/(5k^2)). (The mean of x^2 over the trial function is
  delta^2/7, so the numerator is in fact at least 1 - 4/(7k); the paper's bound is the weaker one and is right.)
- the scaling (4.12): Omega_tau and B_tau are tau^-2 times their tau = 1 profiles in r/sqrt tau and L_k scales by
  1/tau, so the frozen rate at heat age tau is tau^-2 sigma_{k sqrt tau}.

Lemma 4.3 (a metric on the complement). Read at the level of the argument. The Lyapunov identity
C* S + S C = 2 b S - 2 b I for S = 2b int_0^inf e^{-2bu} e^{uC*} e^{uC} du, the lower bound
<Sq, q> >= b/(b + ||C||) ||q||^2 and (4.18) were redone; the compactness and finite-rank steps are standard and
were not checked line by line.

Lemma 4.4 (the growing coordinate of the point response). Redone: the radial Green identity
int K_1(kr) L_k h r dr = 2 h'(0)/k (boundary term at the axis), the derivative at the axis of the order-one
radial heat flow, (e^{-tL_k} h)'(0) = e^{-k^2 t}/(8 t^2) int e^{-r^2/(4t)} h r^2 dr, and the barrier argument for
the ratio r_q (the right side is negative at r_q = g_0 A/(4C)). The Duhamel bounds were read, not redone.

Lemma 4.5 (the prepared response). Read; the kernel e^{-|x|}/(8 pi) of (1 - Delta)^-2 and the moment condition
mu < 5/2 from a |x|^-4 tail are right; the weighted commutator estimate (4.31) was not checked line by line.

Lemma 4.6 (low-frequency lifetime). Redone: with k_0 = c_*/(16 sqrt 2) the small frequencies give
A e^{4 sqrt 2 A k_0} = A e^{c_* A/4}; on k_0 <= |k| <= 2 and t <= 1 the rescaled frequency is at most 2 sqrt 2,
the squared propagator is at most C e^{sigma_* A} with sigma_* = sigma_{2 sqrt 2}; for t >= 1 the estimate (4.4)
gives the factor (1+t)^5 e^{c_* A - 2 k_0^2 (t-1)}; and c_* + sigma_* = 2(c_* - eta_low) for
eta_low = (c_* - sigma_*)/2.

With these, the inputs of Lemma 4.9 are in place: G_k(t) >= sigma_k t/(1+t) can be brought above any G_0 < c_*
by a high band J and a late fixed time t_d, and the two requirements G > c_* - eta_low and 2(c_* - G) < c_*/256
of (5.1) are compatible. The observation window of (4.56) has length 1/A at the fixed time t_d, inside
[t_p, t_p + 4A] for large A.

No error found in Section 4. What has not been checked line by line there: the compactness and finite-rank
steps of Lemma 4.3, the Duhamel and regularisation bounds in Lemma 4.4, the weighted commutator estimates of
Lemma 4.5. Sections 5 to 9 (the transfer to the finite-energy solution, the cascade and the iteration) are
unread beyond the statements.

## Second paper (arXiv 2611.06117): Section 5 from the pages (12 Nov, 07:28)

Read on PDF pages 51 to 63. Constants (5.1), (5.2): c_* = sqrt 2 e^{-3/2}, rho = c_*/8, G = c_* - omega with
0 < 2 omega < rho/32, R = e^{rho A}, b = e^{beta A}, t_p = (2 + Theta log A)/A, t_f = t_p + 16 A^2, s_* = 19/8,
alpha = 7/4, rho_c = 3 rho/8, gamma = rho/4. Numerical and exact checks: pd08_sec5_check.py, .out (30 lines, all
pass).

Proposition 5.2 (weighted energy estimate with the sharp rate, (5.8) to (5.11)). Redone by hand:
- the pure-swirl column Q_1 = Omega x_h^perp with Omega = A eta_1 T^-2 e^-zeta acts on an axisymmetric field by the
  pointwise couplings (2 Omega v_theta, -2 Omega (1 - zeta) v_r); in the metric energy v_r^2 + kappa v_theta^2 +
  v_z^2 one half of the derivative is 2 Omega (1 - kappa (1 - zeta)) v_r v_theta. With kappa = 1/(1 - zeta) on
  zeta <= 1/2 it vanishes; with kappa = 2 beyond, |v_r v_theta| <= (v_r^2 + 2 v_theta^2)/(2 sqrt 2) gives the
  coefficient A eta_1 (2 zeta - 1) e^-zeta/(sqrt 2 T^2), largest at zeta = 3/2 with value c_* A eta_1/T^2, and
  eta_1 <= 1. So the rate is 2 Gamma_src' with Gamma_src' = c_* A/(1+t)^2, as in (5.8), (5.9);
- the reduced weight w = 1 + A^-2mu <x>^2mu: |grad w|/w <= C/A and |Laplace w|/w <= C/A^2 need mu >= 1;
  |grad w|/sqrt w <= 2 mu A^-mu <x>^(mu-1); A^-2mu <x>^(2mu-2) <= A^-2 w on both sides of <x> = A. These give the
  pressure bound through the moment mu - 1 < 3/2 (Lemma 5.1), with no derivative of the tensor source;
- the heat and metric term: 2 int w Kv . Laplace v = -2 D + int v . Laplace(wK) v, which is the displayed formula;
  the bounds |grad K| <= C T^-1/2, d_t K + Laplace K <= C T^-1 use kappa' <= 4, r <= sqrt(2T) on the support of
  kappa', (kappa - 1)/r^2 = 1/(4T(1 - zeta)) <= 1/(2T), and the downward jump of kappa' at zeta = 1/2;
- the column sums (5.13) and the list of terms of a_mu; their integrals over [t_p, t_f]: log((1+t_f)/(1+t_p)),
  16, C A R^-2 (1/t_p + 16 A^2), C A/b, C, C R^-2 t_p^-1/2, 16 A^2/R, and for the correction
  Sigma_1 log(t_f/t_p) + C Sigma_0 (1 + log A). All are O(1 + log A) once beta is large, so the integrating factor
  costs a power of A only;
- (5.14): the integrating factor gives N^2 <= C A^P B^2 e^{2 Gamma(t)} int e^{2(m-1) Gamma(u)} du, at most
  16 A^2 times e^{2m Gamma(t)} because Gamma_src increases and m >= 1;
- the short-interval smoothing: int_{t-h}^t (t-u)^-1/2 du = 2 sqrt h, used with the monotonicity of Gamma_src only.
The H^4 energy inequalities with D_coeff(A) were read, not redone.

Proposition 5.3 (comparison of the complete histories, (5.15) to (5.19)). Redone by hand:
- |1 - eta_1| <= C(t/b^2 + |z|/b) from 1 - (1 + 2t/b^2)^-1/2 <= t/b^2 and 1 - e^-x <= min(1, x);
- the three sources of the first-variation difference have G_1 at most C A^P e^{n Gamma} times b^-1, R^-2 and
  e^{K A} b^-1/2, which is xi_A = R^-2 + e^{K_* A} b^-1/2;
- (5.22): with x = D y the squared weighted norm of a far column is C A^2 D^(1-2mu) int |y|^-2mu |y_h|^2
  e^{-c|y_h|^2} dy; the axial integral is C r^(1-2mu) (needs mu > 1/2), the radial one int r^(4-2mu) e^{-c r^2} dr
  (needs mu < 5/2). At mu = s_* the outer sum is O(A R^-15/8); at mu = s_* - alpha = 5/8 it is C A sum R^-j/8;
- (5.21): the horizontal Gaussian norm of Q_l is C A l^2/(l^2 + t); the inner sum is C A R^-2/t;
- ||h||_{L^1_z L^2_h} <= sqrt(pi A) N_1(h) from int (1 + z^2/A^2)^-1 dz = pi A;
  ||(1 - eta_1)(1 + z^2)^-1/2||_{L^2_z} <= C(b^-1/2 + t/b^2) by splitting at |z| = b;
- (5.18): the relative error is C A^P (R^-15/8 + e^{K_* A} b^-1/2) e^{2 omega A}; it tends to zero because
  (15/8) rho > 2 omega and beta/2 > K_* + 2 omega.

Lemma 5.4 (the retained mean and the low-frequency fibers). Redone by hand:
- chi_l = K_l/r = (1/4) int_l^inf W_tau dtau and its truncation (e^{-r^2/(4L)} - e^{-r^2/(4l)})/r;
  (d_r - 1/r) chi_l = -(1/4) K_hist(l, r); the adjoint of -(d_r + 2/r) in L^2(r dr) is d_r - 1/r; with
  l = 1 + t_f the kernel in (5.27) is K_hist(1 + 2 t_f - u, r);
- 0 <= K_hist(l, r) <= 2/l (the function (1 - (1 + zeta) e^-zeta)/zeta is at most 0.2985), and
  int |F| r dr <= ||v_d||^2/(4 pi), so the right side of (5.27) is at most C A M_d/(1 + t_f) <= C M_d/A;
- (5.28): int K_l^2/(r sqrt(1 + r^2)) dr <= C l^-1/2 by splitting at r^2 = l; (5.29): |cos y - 1| <= 2|y|^(3/2),
  int |z|^3 (a + z^2)^-9/4 dz = B(2, 1/4) a^-1/4 = (16/5) a^-1/4, and int K_l^2/(r (1 + r^2)^1/4) dr <= C l^-1/4;
- the fiber estimate: the pointwise coupling matrix has norm 2 Omega max(1, |1 - zeta|) <= 2A/(1+t)^2; testing
  against -Laplace v_d gives the displayed bound with 4 A^2; the Hilbert-Schmidt norm of phi_0 is
  sqrt 2 (1+t)^-3/2, |v_r| <= |nu| ||v_z||/sqrt 2, and the time integral of sqrt 2 A |nu| (1+t)^-3/2 is
  2 sqrt 2 A |nu|, so (5.31).
The dominated-convergence step for L to infinity and the continuity of the axial Fourier representative were read
and look right; they were not redone.

Proposition 5.5 (inputs near the prepared shape, (5.33) to (5.41)). Redone by hand:
- rho_c - gamma - 2 omega > rho/8 - rho/32 = 3 rho/32, so (5.44) tends to zero;
- Hoelder with theta = alpha/(2 s_*): M_{alpha/2}(d)^2 <= M_{s_*}(d)^{alpha/s_*} ||d||^{2 - alpha/s_*},
  alpha/s_* = 14/19, and the exponent -(24/19)(3 rho/8) + (14/19)(rho/4) = -11 rho/38;
- the scalings (5.36), (5.37): ||F_{f,R}|| = R^5/2 ||w_f||/M_f and ||y_3 F_{f,R}|| = R^3/2 ||z w_f||/M_f, and
  9/4 < s_* gives the bound on the ratio W_f by C A^P e^{2 omega A};
- the leading symbol: the accumulated zero-frequency stress is c I + m_f diag(1,1,0) with m_f = -M_f; the Leray
  projection removes the scalar part and -i P(xi) diag(1,1,0) xi = i xi_z P(xi) e_z, so the sign is +m_f, and the
  rescaling F_R(y) = R^4 w_f(Ry)/m_f leaves the degree-one symbol unchanged;
- the remainder: |S^(u, xi) - S^(u, 0)| <= C |xi|^alpha int |x|^alpha |S| for an even integrable tensor and
  |e^{-h|xi|^2} - 1| <= h^{alpha/2} |xi|^alpha give R^-alpha |xi|^{1+alpha} after rescaling; the H^-17/4 integral
  int <xi_h>^{-8-1/2} (1 + |xi_h|)^{2+2 alpha} d xi_h converges because alpha < 2 + 1/4, and 1 + alpha = 11/4,
  R^-alpha = R^-7/4, as in (5.39);
- (5.41) from (5.29) with |nu| <= K_0 A/R; the sine part vanishes because w_{f,theta} is even in z;
- the axial heat tail: e^{-k^2/A} <= e^{-K_0^2 A} beyond |k| = K_0 A, and ||F_{f,R}|| <= R^5/2 W_f.

No error found in Section 5. What it rests on from earlier sections and was taken as stated: the correction
bound (5.6) with K_m independent of beta (Proposition 3.4), the Riesz moment bound (3.5) and its capped version
(Lemma 3.1), and the seed estimate (5.4) (Lemma 4.9, checked before). Not redone: the H^4 parts of
Propositions 5.2, 5.3 and 5.5, the limit L to infinity in Lemma 5.4. Sections 6 to 9 are unread beyond the
statements.

## Second paper (arXiv 2611.06117): Section 6 from the pages (12 Nov, 07:32)

Read on PDF pages 63 to 72: Lemma 6.1 (the moment M_s at the final time costs only e^{lambda A}, any lambda > 0,
for 0 <= s < 5/2), Lemma 6.2 (frequency derivatives of the extended column operator), Lemma 6.3 (the H^4 bound
at the final time). Checks by script: pd08_sec6_check.py, .out (15 lines, all pass).

Section 6.1 and Lemma 6.2. Redone by hand:
- the difference-quotient identity for F(k) = f^z(k) and the remark that differentiating div_h F_h + ik F_z = 0
  in k gives -i F_z on the right, so the differentiated fiber is not solenoidal and a fixed space is needed;
- the operators (6.2): d_r Phi_{l,t} g = 2 Omega_l g with Omega_l = A l^2 T_l^-2 e^{-r^2/(4 T_l)}, so
  (grad_h Phi, 0) is the radial coupling 2 Omega v_theta e_r and P_k(grad_h Phi, 0) = -ik P_k(e_z Phi); and
  K_{l,t} is 2 Omega_l (1 - zeta) composed with (1/r) int_0^r u h, which with v_r = -(ik/r) int_0^r u F_z is the
  azimuthal coupling -2 Omega (1 - zeta) v_r of Section 5. The extension agrees with the physical operator;
- (6.8): (R_*(k) + ik e_z Phi_*) g = ik (I - P_k)(e_z Phi_* g), whose squared norm is
  |k|^4 int |Phi_*g^|^2/(|xi_h|^2 + k^2); the unit-disk integral of 1/(|xi_h|^2 + k^2) is pi log((1 + k^2)/k^2),
  and |Phi_*g^| <= ||Phi_* g||_1 <= C ||g||;
- on the sector |Im k| < |Re k|/8 the denominator has modulus at least 0.99 (|xi_h|^2 + |k|^2), so Cauchy's
  formula on discs of radius proportional to |k| gives the bounds on R_*'' and R_*''';
- the translation bound C |h| (1 + |log |h||) from the three regions, and the integrability of
  h^{-2 theta} (1 + |log h|) exactly for theta < 1/2, which is where 2 + theta < 5/2 comes from;
- the scaling: Phi_{l,t} = A l^2 T^-3/2 D Phi_* D^-1 for the unitary horizontal dilation D by sqrt T, and
  P_k = D P_{k sqrt T} D^-1, so the meridional block is A l^2 T^-2 D R_*(k sqrt T) D^-1; two k-derivatives give
  T, the L^2_k norm T^-1/4, the fractional seminorm T^{theta/2}: the powers -5/4 and -5/4 + theta/2 of (6.5),
  and -7/4, -7/4 + theta/2 for one derivative, -3/2 for the supremum of one derivative as in (6.4);
- the time integrals: for l = 1 the power -5/4 + theta/2 is integrable at infinity because theta < 1/2; for
  l >= R the bound A t_f l^{-1/2 + theta} sums geometrically.

Section 6.2, proof of Lemma 6.1. Redone by hand:
- -L k^2 + C A |k| = -L (|k| - C A/(2L))^2 + C^2 A^2/(4L), bounded when L is of order A^2;
- W(t) = e^{(t_f - t) d_z^2} v_Q(t) has W(t_p) = e^{16 A^2 d_z^2} f, W(t_f) = v_Q(t_f) and solves (6.12) with
  the commutator P[e^{(t_f - t) d_z^2}, M_Q] v_Q;
- (6.9): the time integrals of m_0 and d_1 over the retained radii (inner radii l^2/t_p, l = 1 at most 1,
  outer radii 16 A^2/l^2); the cutoff derivative bounds C/(b l) and C (b l)^-1 (b^2 l^2 + 2t)^-1/2;
- the commutator bound with h^1/2 + h^{(s+1)/2} from the first moment of the Gaussian kernel and the weight
  translation, and (6.13);
- (6.15): for Q_l = eta_l(z) U_l the radial part commutes with eta_l (it acts in x_h), the azimuthal part of
  B_l^ext applied to eta_l F contains d_z(eta_l F_z), and removing eta_l' K F_z and the shear eta_l' U_theta F_z
  gives the physical operator;
- (6.16) from k (G * F) = G * (kF) + (nu G) * F with mass of G at most 1 and first moment at most C/(b l);
- the triangular integration x_0, x_1, x_2 with the coefficients 1, B_0, B_0^2/2 (also by a numerical
  integration of the equality case), and the reason for keeping the levels apart: the diagonal integral is
  O(kappa_cut A) + O(A/b), the off-diagonal ones are O(A) but enter polynomially;
- the omitted translations: int_{|h| > kappa} 4 |h|^{-1-2 theta} dh = (4/theta) kappa^{-2 theta};
- the high-frequency part e^{-16 A^2 k^2} <= e^{-16 kappa^2 A^2} beyond |k| = kappa; the order of choices
  kappa_cut with C_s kappa_cut < lambda/2, then beta > 2 K + 2, then A;
- the weighted interpolation between s = 0 and s' in (2, 5/2) is the Stein-Weiss statement and is used correctly.

Lemma 6.3. Redone: the maximum of -(16 A^2 - O(1)) k^2 + C A |k| is O(1), so (6.27);
|1 - eta_l| <= C (b l)^-1 (sqrt t + |z|) from 1 - (1 + x)^-1/2 <= sqrt(x/2) and 1 - e^{-y^2/2} <= |y|/sqrt 2;
the three terms of the cutoff difference (matrix A l^2 T^-2 times (b l)^-1 (sqrt t + |z|), shear
(b l)^-1 A l^2 T^-3/2); (6.29).

No error found in Section 6. (One line of my own first check script had the exponent count of (6.5) wrong; the
paper's -5/4 is right, as the dilation identity in the script shows.) Read only, not redone: the operator-valued
fractional product estimates (6.19), the Dini-derivative inequalities for n_0, n_1, n_2, q_theta, the recovery of
the horizontal moment (6.22), (6.23), the density and limiting arguments at the end of the proof of Lemma 6.1,
and the H^3 and H^4 bounds in Lemma 6.3. Taken as stated from Section 3: Lemma 3.1 (odd-field projection in
weighted spaces), Proposition 3.4 (the correction e^{I,J}).

## Second paper (arXiv 2611.06117): Sections 7.1 and 7.2 from the pages (12 Nov, 07:44)

Read on PDF pages 72 to 81: the end of Lemma 6.3, the set-up (7.1), Section 7.1 (physical fibers, the point
response, Lemma 7.1) and Section 7.2 (Lemma 7.2, entrance through the invariant array, with its proof). Checks by
script: pd08_sec7a_check.py, .out (31 lines, all pass).

Set-up. With t_p = (2 + Theta log A)/A and t_f = t_p + 16 A^2 from (5.2): d = t_f/R^2, s_* = t_p - d give
t_f + R^2 s_* = R^2 t_p exactly; d < t_p/2, s_* > 3/A, t_* < R^2 and the hypotheses A <= t_f, R >= A^2,
t_f + 1 <= R^2/(2A) of Lemma 7.2 hold for large A (R = e^{rho A} with rho = c_*/8 = 0.039 passes A^2 only near
A = 300, so "sufficiently large" is large in numbers).

Section 7.1. Redone by hand:
- (7.2) is the operator of Sections 5 and 6: B_T = (2 - r^2/(2T)) Omega_T = 2 Omega_T (1 - zeta); before
  projection the matrix is A l^2 (-2 Omega_T J_h + (Omega_T/(2T)) x_h^perp (x) x_h), smooth, of norm
  A l^2 max(2 Omega_T, |B_T|) <= 2 A l^2 T^-2;
- (7.3): the Hilbert-Schmidt norm of Phi_v is sqrt 2 T^-3/2 (as in Lemma 5.4), |v_r| <= (|k|/sqrt 2) ||v_z||
  by Cauchy-Schwarz with int_0^r u du = r^2/2, int B_T^2 r dr = 8 T^-3 int (1 - z)^2 e^{-2z} dz = 2 T^-3, and
  the two outputs are orthogonal (one in the (r, z) plane, one along e_theta); the bound sqrt 2 A l^2 |k| T^-3/2
  follows;
- the fiber of the point distribution, (2 pi)^-1/2 i k P_k(e_z delta_{0,h}); (7.4): the two-dimensional heat
  kernel has L^2 norm (8 pi s)^-1/2, and int k^2 s^-1 e^{-2 k^2 s} dk is of order s^-5/2;
- Lemma 7.1: the axis value -2 A (T_par + s)^-2 J_h; P J_h P is skew-adjoint and commutes with heat, so the point
  response of the axis matrix has the norm of e^{s Delta} applied to the point distribution, c s^-5/4 by
  homogeneity (symbol of degree 1 in three dimensions), and two xi-derivatives give s^-1/4; the true matrix
  differs by C A |x_h|^2; C A int_0^{1/A} s^-1/4 ds = (4/3) C A^1/4, against c A^5/4.

Section 7.2. Redone by hand:
- the three lines for T_l(phi): e^{u Delta^(1)} W_{L+u} = W_{L+2u}, int_0^inf W_{L+2u} du =
  (2/r)(1 - e^{-r^2/(4L)});
- (7.7): R u(R y, t_f + R^2 s) for a column of radius l is A rho^2 (tau + s)^-2 e^{-|y_h|^2/(4(tau + s))} y_h^perp
  with rho = l/R, tau = (t_f + l^2)/R^2; for the outer radii R^{j+1} this is the second sum, j = 0 the parent
  column with T_par = 1 + d;
- (7.8): the point distribution is homogeneous of degree -4, hence R^4/m; the axial transform gives R^3 and k/R;
- the constant of (7.10): the leading pairing is 8 pi A conj(c_r(0)) m^-1 int K_in phi_theta^ dr, the pairing of
  the point fiber with the test is 2 conj(c_r(0))/sqrt(2 pi) (from 2 c_r = -i k Psi_z(0)), and the quotient is
  4 pi A sqrt(2 pi)/m: (7.19) holds with the stated c_mean;
- B_*: int_0^inf (tau + s)^-3/2 ds = 2 tau^-1/2 and rho^2 tau^-1/2 = l^2/(R sqrt(t_f + l^2));
- the axis gain: ||r e^{-r^2/(cT)}|| = (sqrt pi c/2) T in L^2(R^2), so one old interaction against a test
  vanishing linearly at the axis costs A^2 rho^2 T^-1, and int_0^{t_1/2} ds/(d + s) = log(1 + t_1/(2d));
- (7.13) and the remark A^{(j+3)/2} (tau + s)^{(j-1)/2} <= A^2 (tau_n + s <= 1/A on the early half-interval, by
  t_f + 1 <= R^2/(2A)); Q_psi; B_* <= C_K A^3/2/R; (7.14) from sum_{n >= 2} B_*^{n-1}/(n-1)! = e^{B_*} - 1;
- (7.15); the three norms of E_psi (int s (d+s)^-3 ds <= 1/(2d), int s (d+s)^-7/2 ds = (4/15) d^-3/2, d = t_f/R^2)
  and the interpolation exponent -1 - delta/2 with R^delta; (7.16);
- the dual radial weight (1 + r^2)^{zeta - 7/4}; (7.17) (both norms stay bounded after multiplication by the
  stated power of T, numerically for T up to 1000);
- (7.18): r^2 W_T = 4 T^2 d_T W_T + 8 T W_T and r^2 T^-2 e^{-r^2/(4T)} = 4 T d_T P_T + 4 P_T, hence the three
  lines; also checked that the right sides solve the two radial heat equations;
- the moment exponents: norm T^-15/8 of the Gaussian test at p_0 = 7/4, the tail (4/7)(L + 2H)^-7/8, the two
  integrals of order H^1/8, and R^-7/4 from H = R^2/(2A) both ways;
- the fourth error: r B_T = d_r(r^2 Omega_T), d_r(r w_r) = -i nu r w_z, the integration by parts, and
  int_0^H (L + 2u)^-1 du = (1/2) log(1 + 2H/L);
- the sum of the four errors is at most C_K A^4 W (R^-7/4 + R^-3/2 log(2 + R)) (the powers of A are 27/8, 4,
  23/8 and 7/2);
- c_mean(k) - c_mean(0): int |z|^3 (1 + r^2 + z^2)^-9/4 dz = (16/5)(1 + r^2)^-1/4, and
  int (1 - e^{-r^2/(4L)})^2 (1 + r^2)^-1/4 dr/r <= C L^-1/4 (numerically 1.38 to 1.41 times L^-1/4);
- |k| > K A: 2 A sum l_j^2/(t_f + l_j^2) + 2 A t_1 sum R^-2j <= C, e^{-k^2 t_1} <= e^{-K^2 A}, and
  ||F_R||_2 = R^5/2 ||phi||_2/|m|;
- the last Duhamel comparison, A^3/2 R^-2.
Every term of (7.11) is accounted for by (7.14), (7.15), (7.16), the four errors and the three closing estimates.

No error found. Read only, not redone: the derivative bounds (7.5) and (7.12) for the adjoint test (including
|c_r'(s)| <= C_K A^3), the dual-smoothing step for F_k - J_k, the global Taylor bound for the adjoint expansion,
the positivity of the radial kernels (standard Bessel form), and the density and limiting argument at the end of
the proof of Lemma 7.2.

## Second paper (arXiv 2611.06117): Sections 7.3 and 7.4 from the pages (12 Nov, 07:48)

Read on PDF pages 81 to 85: Section 7.3 (the actual incoming field, (7.21) to (7.25), Lemma 7.3, comparison
with the localized reference) and Section 7.4 (Lemma 7.4, late propagation and tensor sources, (7.37), (7.38)).
Checks by script: pd08_sec7b_check.py, .out (14 lines, all pass).

Section 7.3. Redone by hand:
- the leading term of phi = -int e^{(t_f - t) Delta} P div S dt for an even stress with accumulated integral
  m diag(1,1,0) + c_0 I_3: P annihilates the isotropic part, diag(1,1,0) = I - e_z (x) e_z, and what remains is
  m times the symbol i xi_3 P e_z of the point distribution; the remainder is at most
  C |xi|^{1+alpha} M_alpha from |1 - cos y| <= C |y|^alpha and 1 - e^{-u} <= u^{alpha/2} (1 < alpha < 2);
- the normalization (7.8) turns it into C R^-alpha |xi|^{1+alpha} M_alpha/|m| (the point symbol is homogeneous
  of degree 1, so (R/m) phi^(xi/R) has leading term exactly the point symbol);
- (7.22): |xi_h|^2 + k^2 <= (1 + |xi_h|^2)(1 + k^2) and int_{R^2} (1 + |xi_h|^2)^{-3 + alpha - delta} d xi_h =
  pi/(2 - alpha + delta);
- the additional old radii: by Cauchy-Schwarz against the weight (1 + r^2 + z^2), int dz/(a + z^2) = pi/sqrt a,
  the squared dual integral is pi int (1 - e^{-r^2/(4L)})^2 dr/(r sqrt(1 + r^2)) <= C L^-1/2 (numerically 1.2
  to 3.2 times L^-1/2 for L from 1 to 10^6); with sum_{j >= 1} l_j^2 <= C R^-2 and L_j >= t_f their
  contribution to c_mean(0) is at most C A R^-2 t_f^-1/4 W_f, which by (7.23) is A^{P+1} e^{(2 omega - 2 rho) A},
  small because 2 omega < rho/32; hence (7.25);
- the parent-coordinate ages R^{2j-2} + d + s agree with (7.7);
- (7.28), (7.29): int_0^inf rho^2 (rho^2 + d + s)^-2 ds = l^2/(l^2 + t_f); sup_r r e^{-r^2/(4T)} = sqrt(2T/e)
  and int_0^inf rho^2 (rho^2 + d + s)^-3/2 ds = 2 l^2/(R sqrt(l^2 + t_f)); the parent column gives C A s_* <=
  C A t_p = C (2 + Theta log A);
- the correction: sigma_1 log(1 + s_*/d) <= C sigma_1 rho A, bounded once beta > 2 C_*;
- (7.30): on axisymmetric fields the linearization is P applied to a pointwise matrix, so y_3 commutes with
  the matrix and y_3 P M V = P M (y_3 V) + [y_3, P] M V with M V = -div(U (x) V + V (x) U) on solenoidal V; the
  heat commutator is -2 d_{y_3} V; the symbol of [y_3, P] div has degree 0;
- (7.31) is the cutoff difference of Lemma 6.3 with l replaced by rho = R^{j-1} (width b rho); its two time
  integrals are 2 l/sqrt(l^2 + t_f) and R l/(l^2 + t_f);
- the scaling ||F_R||_2 <= R^5/2 W, ||y_3 F_R||_2 <= R^3/2 W, and the two terms of (7.26).

Section 7.4. Redone by hand:
- (7.32), (7.33): Gamma_tr' = 2 A R^2/(R^2 + t)^2 is the matrix bound 2 A l^2 T^-2 of (7.2) for the parent column
  (l = R, T = R^2 + t); on [t_f, t_*] one has R^2 + t <= 2 R^2, so Gamma_tr' >= A/(2 R^2), and
  Gamma_tr(t_*) <= 2 A t_*/R^2 = 2 A t_p;
- b_rem and its integral (A/t_f, A R^-2 t_p, A t_p/b, sigma_1 log(t_*/t_f));
- (7.35): the integrating factor gives C B_0^2 e^{2n Gamma(t)} int e^{-2(n-1)(Gamma(t) - Gamma(u))} du, and
  Gamma(t) - Gamma(u) >= A (t - u)/(2 R^2) gives R^2/((n-1) A); the constant does not depend on n;
- (7.38): the interval has length at most R^2 t_p <= R^2.

No error found. Read only, not redone: (7.23), (7.24) (they quote Propositions 5.3 and 5.5 and (5.24), (5.36),
(5.40)), the energy and axial-moment estimates behind (7.27), the L^2-to-H^j smoothing in the proof of (7.34)
and (7.36), and (7.37) (it quotes Lemma 6.3). Taken as stated: Proposition 3.4.

## Second paper (arXiv 2611.06117): Sections 7.5 to 7.7 and 8.1 from the pages (12 Nov, 08:01)

Read on PDF pages 85 to 92: Section 7.5 (Lemma 7.5, smoothing in parent coordinates; Lemma 7.6, alignment of
the heat ages), Section 7.6 (Proposition 7.7, transfer of the complete quadratic response), Lemma 7.8
(smoothing of a nonlinear perturbation), Section 8.1 (parameters, shape class, (8.1) to (8.7)), the statement of
Proposition 8.1 and the first step of its proof (the series on the source interval).
Checks by script: pd08_sec7c_check.py, .out (26 lines, all pass).

Section 7.5. Redone by hand:
- H(y) = R h(R y) in three dimensions: ||H||_2 = R^-1/2 ||h||_2 and ||d^4 H||_2 = R^7/2 ||d^4 h||_2;
- the Duhamel formula on an interval of length 1/A, its signs, and int (s - u)^-1/2 du = 2 sqrt h;
- Lemma 7.5: in parent coordinates the parent column has radius 1 and age 1 + d + s, about 1, so its matrix and
  derivatives are at most C_j A; the old columns give C_j A R^-2 s^(-2-j/2) (radii l/R, ages at least s, sum of
  l^2 bounded), the farther ones C_j A R^-2; on (s_* - 2/A, s_*) one has s >= t_p/2 once Theta log A >= 2, so
  both are below C_j A; the rescaling of an interval of length 1/A by the spatial factor A^-1/2 makes the
  matrix and the drift (sigma_0 (d + s)^-1/2 times A^-1/2) bounded;
- the point distribution has a symbol of degree 1, so it is in H^-s for s > 5/2 (H^-3 as stated); y_3 times it
  has a symbol of degree 0 and is in H^-s for s > 3/2, so the stated H^-4 holds with room;
- e^{C A t_p} = e^{2C} A^{C Theta}, a power of A;
- (7.41): R^-2 from the old and farther columns, 1/b from the parent cutoff, e^{C_* A} b^-1/2 from the
  correction (7.42);
- Lemma 7.6: (7.43) is the scaling u -> R u(R^2 t, R y) at t_* = R^2 t_p; in (7.44) the identity
  U(t_p, d) J - U(t_p, 0) J = - int_0^d U(t_p, s) L(s) J ds has the right sign (the derivative of U(t, s) in s
  is -U(t, s) L(s)), s <= d leaves an evolution time of at least t_p/2, and d = t_f/R^2 <= 17 A^2 R^-2.

Section 7.6 and Lemma 7.8. Redone by hand:
- alpha = 7/4, delta = 1/4: alpha < s_* - 1/2 = 15/8;
- the rates (7.48): R^-(alpha - delta) e^{2 omega A}, R^-3/2 log(2 + R) e^{2 omega A} give (3/2) rho - 2 omega,
  above rho because 2 omega < rho/32; R^-1 log(2 + R) gives rho; the tail gives K^2 - (5/2) rho - 2 omega;
- after time 1/A the integrated matrix norm of the old columns is A R^-2 (A - 1/s_*) <= A^2 R^-2;
- (7.49) from the two terms of (7.26); (7.50): the factor R^4 R^-3/2 = R^5/2 times the response C A^P R^2, and
  the mass lower bound of (8.5), rate 2G - (9/2) rho > rho since 2G = 16 rho - 2 omega;
- the coefficient R^6 R^-1 R^-2/m_f = R^3/m_f of the tensor source, the difference equation for
  Z = W - a_f V_{1+d} (signs), and (7.51): R^3 R R^7/2 = R^15/2, rate 2G - (15/2) rho > rho;
- (7.53) for Z = H + zeta V_{1+d} (signs), the product bound R^9/2 a^4 e^{4 c_* A}, and (7.54):
  (15/2) rho - 2 x_0 + 4 c_* - 2G <= -(1/2) rho + 2 omega < -(15/32) rho for x_0 >= 12 rho; the condition on
  kappa is slightly stronger than needed.

Section 8.1 and page 92. Redone by hand:
- the margins: s_* + 1/16 = 39/16 < 5/2, s_* - alpha = 5/8 > 1/2, rho/8 + 2 omega < 5 rho/32 < gamma = 8 rho/32,
  rho_c = 12 rho/32 < 13 rho/32; (7.46) uses delta_A = e^{-3 rho A/8};
- (8.4): the integrating factor gives a factor t_f - t_p = 16 A^2, the same for every m;
- (8.7) is (7.47) times |m_f| R^-3 (sign of m_f checked);
- (8.10) from (8.9): 2 c_* - 3 rho = 13 rho, so A(a_-, f) <= A^P e^{-rho A/32} a_- < a_-/2, and
  2G - 3 rho - 12 rho = rho - 2 omega > 0, so A(a_+, f) > 2 a_+, for large A;
- (8.12): with h = sum (-a)^m V_m the signs agree at every order and V_2 = w_f;
- the recurrence d_1 = L, d_m = L sum d_j d_{m-j} has d_m = Catalan(m-1) L^(2m-1) <= 4^(m-1) L^(2m-1) and the
  generating function (1 - sqrt(1 - 4 L^2 z))/(2L); at z = a e^{Gamma_src} <= e^{(-12 rho + c_*) A} = e^{-4 rho A}
  the series converges for large A.

No error found. Read only, not redone: the heat-energy argument for (7.39), the negative-order estimates
behind (7.40), the last step of Proposition 7.7 (applying Lemma 7.5 on the final interval), and the statements
quoted from Sections 5 and 6 in (8.4) to (8.6). Taken as stated: Proposition 3.4, Lemma 4.9 (G and Theta).

## Second paper (arXiv 2611.06117): proof of Proposition 8.1 and Section 8.3 from the pages (12 Nov, 08:09)

Read on PDF pages 93 to 98: the proof of Proposition 8.1 from the convergence of the series on the source
interval to its end, (8.13) to (8.26), and Section 8.3 (Proposition 8.2, initial preparation, (8.27) to (8.37)).

Checks by script: pd08_sec8a_check.py, .out (25 lines, all pass).

Pages 93 to 95. Redone by hand:
- (8.13): h + a v_f - a^2 w_f is the sum of the terms of degree at least three, at most C A^P a^3 e^{3 c_* A};
  a <= a^2 e^{2 c_* A} because x <= 13 rho + rho/32 < 2 c_* = 16 rho, so ||h(t_f)||_{H^4} <= C A^P a^2 e^{2 c_* A};
- the second series: convergence parameter C A^P (R/sqrt A) a^2 e^{2 c_* A}, exponent rho - 2x + 2 c_* <= -7 rho;
- (8.15): the three terms are the decayed first variation (a), the terms of degree at least three
  (a^3 e^{3 c_* A}) and the later response to a tensor of size (a^2 e^{2 c_* A})^2 with the factor R/sqrt A of
  Lemma 7.4;
- (8.16): A_lead = a_f a^2 M_f R^-3 n_A is a^2 times the leading term of (8.7), S_A = n_A g;
- the normalised rates (8.17): R^-1/2 a/(a^2 e^{2GA} R^-3) gives x + (5/2) rho - 2G; likewise
  -x + 3 c_* + (5/2) rho - 2G and -2x + 4 c_* + (7/2) rho - 2G; on 12 rho <= x <= 13 rho + rho/32 they are at
  most -(15/32) rho + 2 omega (at the upper end), -(3/2) rho + 2 omega and -(9/2) rho + 2 omega (at the lower
  end); the first is below -(13/32) rho because 2 omega < rho/32;
- the hypotheses of Lemma 7.8 with zeta_tr = A_lead/n_A, kappa = 13 rho/32: the lower bound on zeta by (8.5),
  the tensor exponent (15/2) rho - 2x + 4 c_* - 2G <= -(1/2) rho + 2 omega, and kappa < (15/32) rho - 2 omega;
- kappa = 13 rho/32 > rho_c = 12 rho/32;
- (8.18): from h_out = -A_lead g + r_out and ||g||_2 = 1, A = A_lead - <r_out, g>, F - g = (<r_out, g> g - r_out)/A;
  if ||r_out||_2 <= A_lead/2 then A >= A_lead/2 and ||F - g||_{H^4} <= 2 (1 + ||g||_{H^4}) ||r_out||_{H^4}/A_lead;
- the two integrals after (8.20): int ||dh||^2 <= C A^P a^2 delta_A^2 e^{2 c_* A} (interval of length 16 A^2),
  which is o(1) since -24 rho + 16 rho < 0; the second is a^4 delta_A^2 e^{2 c_* A} up to powers of A;
- (8.22): the three products, with the weight on one factor, add up to a^2 e^{2 Gamma_src} (1 + delta_A B_mom);
- (8.23) from (8.6) for the linear part and (8.4) with m = 2 for the rest;
- on [t_f, t_*] the integrated heat matrix: A/t_f from the radii at most 1, A t_p = 2 + Theta log A from the
  radius R, A t_p/R^2 from the farther ones;
- (8.24): the exponent of R^2 a^2 e^{2 c_* A} is at most 2 rho - 24 rho + 16 rho = -6 rho;
- (8.25): h_out(y) = R h(t_*, R y) has ||h_out||_2 = R^-1/2 ||h||_2 and || |y|^s h_out ||_2 = R^(-s-1/2) || |x|^s h ||_2;
- the quadratic part: R^(-s_*-1/2) a^2 e^{2 c_* A}/(a^2 e^{2GA} R^-3) = e^{((5/2 - s_*) rho + 2 omega) A} =
  e^{(rho/8 + 2 omega) A}; the linear part has exponent xi_lin = (5/2 - s_*) rho + x - 2G + 2 rho;
- at x = 13 rho + rho/32: gamma_0 = rho/8 + 2 omega < 5 rho/32 < gamma, delta_A B_mom <= e^{-rho A/8}, and
  xi_lin + gamma = -(19/32) rho + 2 omega < 0.

Pages 96 to 98 (end of the proof of Proposition 8.1; Section 8.3, Proposition 8.2, initial preparation).
Redone by hand:
- (8.10) from (8.9): A^P e^{-rho A/32} at a_-, A^-P e^{(rho - 2 omega) A} at a_+;
- the regularised impulse: the point distribution is homogeneous of degree -4, so e^{eta Delta} J =
  eta^-2 J_1(x/sqrt eta); its j-th derivative has L^2 size eta^(-5/4 - j/2), so H^4 costs eta^-13/4;
- with eta = e^{-rho A} and |eps| <= 2 a_+: |eps| eta^-13/4 <= 2 e^{-35 rho A/4} and |eps| eta^-13/2 <=
  2 e^{-11 rho A/2};
- the energy inequality for the correction: the source A^2 b^-1/2 squared is A^4 b^-1, and Gronwall over
  [0, t_p] costs e^{C(A+1) t_p}, a power of A, which gives (8.30);
- ||J_eta - J||_{H^-6} <= C eta from the derivative of the heat semigroup;
- the Bessel-smoothed distribution has a tail |x|^-4, so its moment of order mu is finite exactly for
  mu < 5/2, and it is locally square integrable (symbol of degree -3 at high frequency);
- (8.33): || |x|^mu D^j J_eta ||_2 = eta^(-5/4 - j/2 + mu/2) times a constant, at most eta^(-5/4 - j/2) for eta <= 1;
- (8.35): int_0^inf e^{-lambda s} ds = 1/lambda and int_0^inf s^-1/2 e^{-lambda s} ds = sqrt(pi/lambda) with
  lambda = K(A + 1); removing the weight costs e^{K(A+1) t_p}, a power of A;
- s_* + chi_seed = 39/16 < 5/2; five derivatives in (8.34) cost eta^-15/4 <= eta^-4;
- the rates of (8.27): eta^-4 b^-chi = e^{(4 rho - chi beta) A} <= e^{-2 rho A} because chi_seed beta > 6 rho,
  and b^-1/2 <= b^-chi; the nonlinear remainder eps^2 eta^-13/2 divided by eps;
- B_J(lambda) = lambda (1 + <d, g>) and F_J - g = (d - <d, g> g)/(1 + <d, g>) from the definition and ||g||_2 = 1;
  (8.28) follows; every error rate is at least rho > rho_c = 3 rho/8.

No error found. Read only, not redone: the telescoping argument for (8.19), the weighted energy inequality
(8.20) and its Gronwall step (they quote Proposition 5.2), the weighted mild inequality behind (8.24)
(it quotes Lemma 3.1 and (3.22)), the pressure bounds after (8.29) (they quote (3.25)), (8.31), (8.32) and
(8.34) (weighted graph argument of Lemma 4.5), and the cutoff bounds before (8.36).

## Second paper (arXiv 2611.06117): Section 8.4, Section 9 and Appendix A from the pages (12 Nov, 08:18)

Read on PDF pages 99 to 110: Section 8.4 (Lemma 8.3, finite shooting) and the whole of Section 9: 9.1 (physical
solutions at finite depth, (9.1) to (9.8)), 9.2 (Proposition 9.1, compactness and the initial energy
inequality), 9.3 (mixed norms, Proposition 9.2, (9.15) to (9.22)), 9.4 (fixed observations, (9.23) to (9.27)),
9.5 (proof of Theorem 1.1, Corollary 9.3); on pages 107 to 110 Appendix A. The references start on page 110.
Checks by script: pd08_sec8c_check.py, .out.

Pages 99 to 101. Redone by hand:
- Lemma 8.3: by (8.10) the unclipped output at a_- is below a_- and at a_+ above a_+, for every shape of the
  class, so a boundary amplitude stays at the same boundary under the clipped recursion; by (8.28) the clipped
  initial amplitude is a_- at lambda = a_-/2 and a_+ at lambda = 2 a_+; the terminal amplitude is continuous in
  lambda and takes the values a_- and a_+ at the two ends, so some lambda_N strictly inside gives a_*; an
  earlier boundary amplitude would force a boundary terminal value, so no clipping acted and the orbit is a
  genuine one with every amplitude in the open interval;
- ||Q_l(0)||_q = C_q A b^(1/q) l^(3/q - 1): substitute x_h = l y, z = b l zeta; the series over l_n = R^-n
  converges exactly for q < 3; each summand is x_h-perp times a function of |x_h| and z, so divergence free;
- the weak-L^3 bound: the exponent is at least rho^2/(4 l^2) with rho^2 = |x_h|^2 + z^2/b^2;
  e^{-s^2/4} <= C s^-4 (the maximum of s^4 e^{-s^2/4} is 64 e^-2); both sums are geometric and give
  C_R rho^-2; |u_0| <= C_R A |x_h| rho^-2 <= C_R A/rho; the ellipsoid rho < a has semi-axes a, a, b a and
  volume 4 pi b a^3/3; hence (9.6);
- (9.7): sum over n > N of C A sqrt(b) l_n^1/2 = C A sqrt(b) l_{N+1}^1/2/(1 - R^-1/2); the regularised input
  has L^2 norm (lambda_N/n_A) l_N^(-1 + 3/2) ||J_eta||_2 and ||J_eta||_2 = C eta^-5/4;
- u_0 is not in L^3: on D_n the n-th summand is at least (A/l_n^2) l_n e^{-1 - 1/(2 b^2)} >= A e^-3/2/l_n for
  b >= 1; |D_n| = pi (4 - 1) l_n^2 times 2 l_n = 6 pi l_n^3; the cylinders are disjoint once R > 2; each
  contributes 6 pi e^-9/2 A^3;
- (9.8): for lambda in J_n, lambda mu_0(lambda)^(1/3) >= (c_0 A/(2 l_n)) (6 pi)^(1/3) l_n; the intervals J_n
  are disjoint once R > 2 and each has logarithmic length log 2, so the integral diverges for every finite
  second exponent;
- Proposition 9.1, first step: ||v||_4^2 <= C ||v||_2^1/2 ||grad v||_2^3/2 in three dimensions, the power 3/2
  integrated to the power 4/3 gives the energy, so the time derivative is in L^4/3(H^-1); Holder in time gives
  the exponent 1 - 3/4 = 1/4.

Pages 102 to 104 (end of Proposition 9.1; Section 9.3, (9.15) to (9.17); Proposition 9.2). Redone by hand:
- (9.11): the cutoff terms C E_A T_0/K^2 (from the Laplacian of the cutoff and the energy bound) and the flux
  terms with 1/K;
- (9.12): ||v||_3^3 <= C ||v||_2^3/2 ||grad v||_2^3/2 and Holder in time with exponents 4/3 and 4;
- the interpolation L^3 between L^2 and L^10/3 in space-time: 1/3 = (1/6)/2 + (5/6)(3/10);
- (9.15): T_n <= t <= T_{n-1} = R^2 T_n with T_n = l_n^2 t_p gives l_n^1/2 <= t_p^-1/4 t^1/4 and
  l_n^-1 <= R sqrt(t_p) t^-1/2;
- (9.16): ||h||_q <= ||h||_2^(2/q) ||h||_inf^(1 - 2/q) has the exponent (1/4)(2/q) - (1/2)(1 - 2/q) = (3/q - 1)/2;
- the norm of the heat evolution of one column: the horizontal factor is (l^2/(l^2 + t))^2 x_h-perp
  exp(-|x_h|^2/(4 (l^2 + t))), the vertical one (b^2 l^2/(b^2 l^2 + 2t))^1/2 exp(-z^2/(2 (b^2 l^2 + 2t))), so
  ||Q_l(t)||_q = C_q A b l^3 (l^2 + t)^(-3/2 + 1/q) (b^2 l^2 + 2t)^(-1/2 + 1/(2q)); since b >= 1 and the last
  exponent is not positive this is at most C_q A b l^3 (l^2 + t)^(-2 + 3/(2q));
- the split at l = sqrt t: the smaller radii give t^(3/2) t^(-2 + 3/(2q)) = t^((3/q - 1)/2), the larger ones the
  sum of l^(3/q - 1): bounded for q < 3, 1 + |log t| at q = 3, t^((3/q - 1)/2) for q > 3; hence (9.17);
- (9.18): for q > 3 the power t^(-(1 - 3/q) p/2) is integrable exactly when 2/p + 3/q > 1;
- (9.20): the integral of min(|E|, M^3 lambda^-3) over lambda is (3/2) M |E|^(2/3) (split at lambda =
  M |E|^(-1/3)); with E the set where |Q(t)| > lambda this gives lambda |E|^(1/3) <= (3/2) M;
- (9.21): ||e||_3 <= ||e||_2^(2/3) ||e||_inf^(1/3) and the powers of t cancel, 1/6 - 1/6;
- the gradient inequality: the nonlinear term is at most ||v||_inf ||grad v||_2 ||Laplace v||_2, absorbed by
  Young; the coefficient ||v||_inf^2 <= C/t is integrable on a positive-time interval.

Pages 105 to 107 (Section 9.4, fixed observations and the family of branches; Section 9.5, proof of Theorem 1.1;
Corollary 9.3). Redone by hand:
- psi_n = -l_n^-3/2 g(x/l_n) has norm 1, and with (9.4) and <f, g> = 1 the pairing is
  l_n^-1 l_n^-3/2 l_n^3 a = l_n^1/2 a, which is (9.23); at n = 0 it is (9.24);
- the compactly supported test: ||U - u-bar||_2 <= 2 sqrt(E_A) by (9.9), so the error of replacing psi_1 by
  phi_1 is at most a_- l_1^1/2/2 and the pairing stays at least a_- l_1^1/2/2;
- (9.26): the difference equation, the identity -int (w . grad) v . w = int (w . grad) w . v for a
  divergence-free w, and Young; the coefficient ||v||_inf^2 <= C/t is integrable on [eps, T_0] by (9.17), so two
  members that agree at one positive time agree up to T_0; (9.24) gives different terminal coordinates, and
  a_* >= a_- > 0 separates every branch from the reference; hence (9.27);
- the order of the parameters in the proof of Theorem 1.1 agrees with the conditions used earlier
  (chi_seed beta > 6 rho with chi_seed = 1/16 is beta/16 > 6 rho; lambda = 2 rho at s = s_* in Lemma 6.1);
- Corollary 9.3: the mollified equation, the triangle inequality for the mollified velocities, the join at T_0
  through strong continuity and the energy equality (9.22).

Pages 107 to 110 (Appendix A, uniqueness in Lorentz spaces of finite second index: Proposition A.1, Lemmas A.2
and A.3). Redone by hand:
- (A.5): the Lorentz product inequality with 1/2 = 1/3 + 1/6 and second indices infinity and 2, and the
  Sobolev embedding of H^1 into L^{6,2}; (A.7) follows, the time derivative is in L^2(H^-1) and (A.8) is the
  usual cancellation;
- the heat estimates: from weak L^3 to L^4 the power is -(3/2)(1/3 - 1/4) = -1/8, to L^inf it is -1/2, and
  ||f||_4 <= C ||f||_{3,inf}^(3/4) ||f||_inf^(1/4) gives the same -1/8;
- (A.10) needs the density of smooth compactly supported fields, which holds exactly for a finite second
  index: ||e^{t Laplace} a|| <= C ||a - b||_{3,inf} + tau^(1/8) ||b||_4;
- (A.11): the kernel of e^{(t-s) Laplace} P div from L^2 to L^4 has the power -1/2 - 3/8 = -7/8, to L^3 the
  power -1/2 - 1/4 = -3/4; the integral of (t - s)^(-7/8) s^(-1/4) is t^(-1/8) B(1/8, 3/4) and with 3/4 in place
  of 7/8 it is the constant B(1/4, 3/4); hence (A.12);
- the contraction on the ball of radius 2 ||e^{t Laplace} a||, the sign in (A.13), and the L^4 contraction used
  for the regularised data a_j;
- (A.16): the small weak-L^3 part costs C eps ||grad h||_2^2 by (A.5), the bounded part
  ||grad h||_2^2/4 + C ||b||_inf^2 ||h||_2^2; with C eps <= 1/4 Gronwall gives h = 0;
- (A.19): the energy inequality of v from 0 minus the energy equality of u on [0, tau_*].

Section 9 and Appendix A are read through. No error found. Taken as stated: the covariance (3.23), (3.24), (3.21), (5.5), (5.6),
the convergence of the reference solutions at the end of Proposition 3.4 (used on page 105 so that every
branch has the same reference limit), the Lorentz convention (A.1), (A.2), weak-strong uniqueness and the
standard compactness steps of Proposition 9.1 and Corollary 9.3.

## Second paper (arXiv 2611.06117): Section 3 from the pages (12 Nov, 08:37)

Read on PDF pages 20 to 29: Section 3 (a finite-energy reference solution): 3.1 weighted operators and
symmetries (Lemma 3.1), 3.2 the heat array and its linear evolution (Lemmas 3.2, 3.3), 3.3 construction of the
exact reference solution (Proposition 3.4).
Checks by script: pd08_sec3_check.py, .out.

Pages 20 to 22 (Section 3.1, Lemma 3.1 and its proof; start of Section 3.2 to (3.7)). Redone by hand:
- the two thresholds: a kernel of order |x|^-4 has weighted square integral int_1^inf r^(2 mu - 8) r^2 dr, finite
  exactly for mu < 5/2; a kernel of order |x|^-3 gives int r^(2 lambda - 4) dr, finite exactly for lambda < 3/2;
- a centrally odd axisymmetric field: -x is (r, theta + pi, -z) and e_r, e_theta change sign there, so v_r and
  v_theta are even in z and v_z is odd;
- the outward shell bound with cancellation: |K(x - y) - K(x)| <= C 2^k 2^-4j for x in D_j, y in D_k, j >= k + 3;
  with |D_j|^(1/2) = C 2^(3j/2) the exponent is 3j/2 + k - 4j + 3k/2 = -5 (j - k)/2;
- without cancellation the kernel has order -3 and the exponent is 3j/2 - 3j + 3k/2 = -3 (j - k)/2;
- the inward bound (k >= j + 3): 3j/2 - 3k + 3k/2 = -3 (k - j)/2;
- with the weight ratio 2^(mu (j - k)) the coefficients are 2^(-(5/2 - mu)(j - k)) outward and
  2^(-(3/2 + mu)(k - j)) inward, summable exactly for mu < 5/2 (with cancellation), and for lambda < 3/2 without it,
  which is (3.5);
- horizontal axisymmetric fields: the angular integral of e_r and e_theta at fixed (r, z) vanishes, so
  K(x - (0, 0, z)) can be subtracted;
- the heat kernel: sup over h of h^-3/2 e^{-|x|^2/(4h)} is C |x|^-3 (s^(3/2) e^-s bounded), and the gradient
  C |x|^-4 (s^(5/2) e^-s bounded);
- (3.4): the kernel of e^{h Laplace} P div is at most C (|x| + sqrt h)^-4, L^2 norm C h^-1/2 (the symbol
  |xi| e^{-h |xi|^2}); outward coefficient 3j/2 - 4j + 3k/2 = -5 (j - k)/2 - k, inward 3j/2 - 4k + 3k/2 =
  -3 (k - j)/2 - k;
- the capped weight: outward ratios decrease, inward ratios are at most one;
- (3.6): B_T = (1/r) d(r W_T)/dr = 2 Omega + r Omega' = 2 (1 - r^2/(4T)) Omega_T, the axial vorticity of the swirl;
- Q_l is the heat evolution of Q_l(0): x_j T^-2 e^{-r^2/(4T)} is a derivative of the two-dimensional heat kernel
  at age T = l^2 + t; the vertical Gaussian of variance b^2 l^2 becomes sqrt(b^2 l^2/D) e^{-z^2/(2D)} with
  D = b^2 l^2 + 2t; at t = 0 it is (A/l^2) x_h-perp e^{-r^2/(4 l^2)} e^{-z^2/(2 b^2 l^2)}, the datum used in
  Section 9;
- ||grad^j Q_A(t)||_inf <= C_j A t^(-(j+1)/2): one column is at most C A l^2 T^-3/2, the radii below sqrt t sum to
  A t^-1/2 and the larger ones (A/l) also; each derivative costs T^-1/2 because D_l >= T_l for b >= 1;
- ||eta'||_inf <= b l e^-1/2/D <= C/(b l) and ||eta''||_inf <= C b l/D^(3/2) <= C/(b l sqrt D) since D >= b^2 l^2;
  the axial shear is at most C A l^2 T^-3/2 D^-1/2 <= C A l^2 T^-2.

Pages 23 to 25 (Lemma 3.2 and its proof; Lemma 3.3 and its proof; start of Section 3.3). Redone by hand:
- b_0 <= 16A/(3t): l^2/(l^2 + t)^2 <= min(l^2/t^2, 1/l^2); each side of sqrt t is a geometric sum with ratio
  R^-2 <= 1/4, so 2 (2A/t)(4/3);
- (3.9): for V = A l^2 W_T e_theta and axisymmetric v, (V . grad) v + (v . grad) V =
  A l^2 (-2 Omega v_theta e_r + B_T v_r e_theta), since V_theta/r = A l^2 Omega and V_theta' + V_theta/r = A l^2 B_T;
  sup 2 Omega_T = 2 T^-2 and sup |B_T| = 2 T^-2 (the factor (1 - s) e^-s is at most 1), which is c_coup;
- the pressure primitive: d p_v/dr = 2 Omega v_theta, and (grad_h p, 0) = grad(p e^{ikz}) - ik p e_z;
  Hilbert-Schmidt norm squared int int 1_{rho > r} (4 Omega(rho)^2/rho^2) rho d rho r dr = 2 int rho Omega^2 d rho
  = 2 T^-3;
- (3.10): r v_r = -ik int_0^r rho v_z d rho from the divergence at frequency k; Cauchy-Schwarz with
  int_0^r rho d rho = r^2/2; ||B_T||^2 in L^2(r dr) is 4 T^-3 int_0^inf (1 - u/2)^2 e^-u du = 2 T^-3;
- the integral bound in (3.8): int_0^h 2 A l^2 (l^2 + t)^-2 dt = 2Ah/(l^2 + h); int_0^h sqrt2 A l^2 |k|
  (l^2 + t)^-3/2 dt <= 2 sqrt2 A l |k|; the three ranges give 2 sqrt2 A/(1 - R^-1), 2A (1 + log(|k| sqrt h)/log R),
  2A/(1 - R^-2); with R >= 2 the constants add to (4 sqrt2 + 2 + 8/3) A = 10.33 A < 12 A; for |k| sqrt h < 1,
  (4 sqrt2 + 8/3) A = 8.33 A;
- (3.14): the active set is an interval because b_0 decreases in t; Phi <= 24A + 4 zeta log_+ x - x^2/2 with
  x = |k| sqrt h, maximal at x^2 = 4 zeta with value 2 zeta log(4 zeta/e), so Phi <= 2 log K_Q;
- the active set lies in u < 64A/(3 k^2) because 16A/(3u) > k^2/4 there;
- 0 <= k d_k b_0 <= b_0 termwise; k d_k Phi = Phi - k^2 |active|/2 at most, and at least -k^2 |active| >= -64A/3
  >= -d_Q since d_Q >= 24 A;
- (3.15): comparable frequencies of one sign, B_l <= 2 L_l min(|k|, |k'|) and |m(k) - m(k')| <=
  K d |k - k'|/(2 min); otherwise max(|k|, |k'|) <= 2 |k - k'| and |m(k)/m(k') - 1| <= K; both below
  K (d + 2) L_l |k - k'|;
- the kernel G_l: (2 pi)^-1/2 times the transform of eta_l, b l (2 pi)^-1/2 e^{-D q^2/2}; its integral is
  b l/sqrt D <= 1 and int |q| G = sqrt(2/pi) b l/D;
- the shear multiplier: sup A l^2 W_T = sqrt2 A l^2 T^-3/2 e^-1/2 = L_l/sqrt e;
- (3.16): the constant 1 + K (d + 2) + K/sqrt e <= K (d + 4);
- (3.17): L_l mu_l = (2A/sqrt pi) b l^3/(T^3/2 D) <= (2A/(sqrt pi b)) l (l^2 + t)^-3/2, and the sum over the radii
  is at most (2 + 4/3)/t;
- (3.18): b_0 - (2 b_0 - k^2/2)_+/2 <= k^2/4 in both cases, which leaves 3/4 of the dissipation; the constant
  is epsilon_Q;
- (3.19): (v . grad) Q = (v . grad Omega_Q) x_h-perp + Omega_Q v_h-perp and (Q . grad) v = Omega_Q v_h-perp for
  an axisymmetric v;
- h_0 = min((t - s)/2, t/(8 (1 + A))) >= (t - s)/(8 (1 + A)); ||v||_inf <= C ||v||_2^1/4 ||grad^2 v||_2^3/4 is
  scale invariant (3/8 - 3/8);
- (3.20): (E^1/2)' <= (epsilon/t) E^1/2 + K M t^-3/4 integrates to K M t^1/4/kappa with kappa = 1/4 - epsilon;
  then (3/4) int D <= 2 K^2 M^2 sqrt t (epsilon + kappa)/kappa^2 = K^2 M^2 sqrt t/(2 kappa^2);
- the Beta integrals: int_0^t (t/s)^epsilon (t - s)^-1/2 s^-3/4 ds = t^-1/4 B(kappa, 1/2) and with -3/4 in place
  of -1/2 it is t^-1/2 B(kappa, 1/4), the weights of (3.13).

Pages 26 to 29 (Proposition 3.4 and its proof; the first lines of Section 4). Redone by hand:
- (3.25): d_r P_{l,l~} = A^2 l^2 l~^2 eta eta~ r T^-2 T~^-2 e^{-r^2/(4T) - r^2/(4T~)} = Q_{l,theta} Q_{l~,theta}/r;
  with (Q . grad) Q = -(Q_theta^2/r) e_r the array obeys Q_t - Laplace Q + (Q . grad) Q + grad P_Q = (d_z P_Q) e_z;
- the axial residual: for l <= l~ the axial variance D D~/(D + D~) is at least D/2 >= b^2 l^2/2; the
  differentiated Gaussian has L^2 norm (sqrt(pi)/2)^(1/2) sigma^-1/2 <= C (b l)^-1/2; the horizontal Gaussian
  has norm (2 pi T T~/(T + T~))^(1/2); together C A^2 b^-1/2 l^3/2 l~^2/(sqrt(T T~) (T + T~)^3/2);
- with l = sqrt(t) u, l~ = sqrt(t) v the last factor is t^-3/4 f(u, v),
  f = u^3/2 v^2/(sqrt((1 + u^2)(1 + v^2)) (2 + u^2 + v^2)^3/2), and the three bounds hold with C = 1;
- (3.26): v <= 1: the inner sum leaves v^7/2; u <= 1 <= v: the sums separate; 1 <= u <= v: the inner sum
  leaves v^-3/2;
- (3.27): -P((Q . grad) Q) = -P((d_z P_Q) e_z) = F_Q since the gradient is annihilated;
- (3.28): t^-1/2 t^-1/4 = t^-3/4;
- the contraction: with ||F_Q||_2 <= M_A t^-3/4 the map sends the ball of radius 2 L_ref M_A into itself when
  4 L_ref^2 M_A <= 1 and has Lipschitz constant 4 L_ref^2 M_A, which 8 L_ref^2 M_A <= 1 makes at most 1/2;
- K_Q for R = e^{rho A}: zeta_Q = A/log R = 1/rho, so K_Q = e^{12A + c_Q(rho)}; epsilon_Q <= 1/8 and
  8 L_ref^2 M_A <= 1 both hold for b >= e^{B A} with B large (b enters as 1/b and b^-1/2 against A^P e^{C A});
  (3.21) is 2 L_ref M_A;
- (3.23): R Q_l(R^2 t, R x) = Q_{l/R}(t, x) (l^2 R^2/(l^2 + R^2 t)^2 = l'^2/(l'^2 + t)^2 with l' = l/R, and
  eta_l(R^2 t, R z) = eta_{l'}(t, z)), so the radii R^j, -I <= j <= J, become -(I + 1) <= j <= J - 1; the
  lifespan l_max^2 scales with it; the scaled correction is in the same ball because the homogeneous term is at
  most K_Q t^epsilon delta^(1/4 - epsilon) ||e||;
- (3.24): ||Q_l(0)||_p = C_p A b^(1/p) l^(3/p - 1), summable over l_n = R^-n exactly for p < 3;
- Q e, e Q and e^2 have L^2 norms O(t^-1/2 t^1/4) = O(t^-1/4), integrable at zero;
- (3.29): ||u||_3^3 <= C ||u||_2^3/2 ||grad u||_2^3/2 and Holder in time with 4/3 and 4;
- the inner cutoff limit: the Picard majorant t^epsilon s^(-3/4 - epsilon) is integrable since epsilon < 1/4;
  the heat parts converge in L^2 uniformly in time by the contraction; the corrections differ by at most
  2 Sigma_0 t^1/4 near zero;
- page 29: d_tau W_tau = (d_r^2 + d_r/r - 1/r^2) W_tau and d_r p_d = A^2 W^2/r; the linearised system is (3.9)
  with A l^2 replaced by A.

Section 3 is read through. No error found. Read only, not redone: the smoothing step for (3.12) (rescaled
derivative energies on the last interval), the derivative estimates (3.22), the energy equalities through zero
and the convergence of the linearised propagators as the inner cutoff is removed; these are standard parabolic
arguments and their inputs ((3.11), (3.18), (3.21), (3.26), (3.29)) are the ones checked above.

## Second paper (arXiv 2611.06117): Sections 1 and 2 from the pages (12 Nov, 08:56)

Read on PDF pages 1 to 19: the abstract, Section 1 (the solution class, Theorem 1.1, the mechanism, earlier
work, conventions) and Section 2 (overview). Checks by script: pd08_sec12_check.py, .out (17 checks, all pass).

## PDF pages 1-4 (read 12 Nov 08:5x)
Contents: Sections 3 (p. 20), 4 (29), 5 (51), 6 (63), 7 (73), 8 (89), 9 (99), Appendix A (107), references (110).
Solution class (1.2)-(1.4): Leray-Hopf with strong L^2 attainment of the datum, energy inequality from s = 0 and
a.e. s; suitable = pressure in L^{3/2}_loc and local energy inequality including the initial time.
Theorem 1.1 as printed (page 4). There exist T > 0, a nonzero real divergence-free u_0 in L^2, a solution ubar and
solutions u^theta, 0 < theta < 1, with:
 (i) u_0 axisymmetric, in C^infty(R^3 minus 0), in L^{3,infty}, in every L^q with 1 <= q < 3, not in L^3;
 (ii) every listed solution in C([0,T]; L^2_sigma), L^2 H^1, C^infty((0,T) x R^3); initial value strongly in L^2;
      pressure in L^{5/3}((0,T) x R^3); global energy EQUALITY for 0 <= s <= t <= T; local energy equality through
      time zero; hence suitable and Leray-Hopf;
 (iii) every L^p(0,T; L^q) with 1 <= p <= infty, 2 <= q <= infty, 2/p + 3/q > 1 (1.6); and L^infty(0,T; L^{3,infty}) (1.7);
 (iv) pairwise distinct: for u != v listed and every 0 < eps <= T, int_0^eps ||u - v||_2^2 dt > 0; one time t_w and
      one real test phi with <u^theta(t_w) - ubar(t_w), phi> > 0 for all theta.
Text after the theorem: proof completed in Section 9.5; datum specified in (3.24); theta assigned by prescribing a
terminal L^2 coordinate of the limiting solution. Remark 1.2: by Proposition A.1 no listed solution is in
L^infty(0,T; L^{3,r}), r < infty; (9.8) shows the datum is in no L^{3,r}, r finite.
To compare with Sections 3-9: (a) where u_0 not in L^3 and u_0 in L^{3,infty} are proved ((9.8), Section 9.3);
(b) where pairwise distinctness for ALL pairs theta != theta' is proved, not only theta against ubar (the displayed
observable separates u^theta from ubar only; distinctness of u^theta from u^theta' needs the terminal coordinate
to be injective in theta) - Section 9.4; (c) pressure exponent 5/3; (d) the range (1.6) includes p = infty, q = 2
and q = infty with p < 2: check Section 9.3 covers q = infty.

## PDF pages 5-8 (read 12 Nov 08:5x)
Section 1.3. Difference identity (1/2) d/dt ||h||^2 + ||grad h||^2 = - int (h.grad) ubar . h: standard.
(1.8) Q_l(0,x) = (A/l^2) exp(-r^2/(4 l^2) - z^2/(2 b^2 l^2)) x_h^perp; stated ||Q_l(0)||_2^2 = 4 pi^{3/2} A^2 b l.
  By hand: (A^2/l^4) * 2 pi * int_0^inf r^3 e^{-r^2/(2 l^2)} dr * int e^{-z^2/(b^2 l^2)} dz
  = (A^2/l^4) * 2 pi * 2 l^4 * sqrt(pi) b l = 4 pi^{3/2} A^2 b l. Agrees. Radii 1, R^-1, R^-2, ...: sum of norms
  is a geometric series in R^{-n/2}, finite.
U_d(t,r) = A r (1+t)^-2 e^{-r^2/(4(1+t))} e_theta: its vorticity is -2 A d/dtau of tau^-1 e^{-r^2/(4 tau)},
  tau = 1+t, a 2D heat solution. Agrees with "solves the viscous equations with a radial pressure".
Rayleigh discriminant of U_theta = r e^{-r^2/4}: (1/r^3) d/dr (r U)^2 = (4 - r^2) e^{-r^2/2}; zero at r = 2,
  minimum -2 e^-3 at r = sqrt 6 (derivative r (r^2 - 6) e^{-r^2/2}). So the potential (r^2 - 4) e^{-r^2/2} has
  maximum 2 e^-3 and c_* = sqrt(2 e^-3) = sqrt2 e^{-3/2}: same constant as Lemma 4.2 and Section 8.
  Stated: 0 < sigma_k < c_*, sigma_k -> c_* as k -> infinity (Lemma 4.2; read earlier in Section 4).
Complete quadratic stress S = v(x)v + U(x)w + w(x)U, (d_t - Lap) w = -P div S; int S dx = diag(s_h, s_h, s_z);
(1.9) M = - int_{t_p}^{t_f} (s_h - s_z) dt, claim M > 0 (Section 4.7 / 5: the positive stress mass; read earlier).
Shape transferred: J = P d_z(e_z delta_0). (1.10) a_out ~ K_A(f) a^2, K_A > 0; Proposition 8.1 gives the exact
transition map with H^4 and weighted L^2 control of the output.
Finite cascade: N+1 radii, N transitions, ONE initial amplitude at the smallest radius chosen by continuous
shooting so that the difference has a prescribed nonzero observation at a fixed later time. Initial perturbation
a multiple of J_{eta_reg} = e^{eta_reg Lap} J; scaling ||l_N^-1 J(./l_N)||_2 = l_N^{1/2} ||J||_2 (by hand:
l^-1 * l^{3/2}); amplitudes bounded independently of N, so initial differences -> 0 in L^2.
Propositions 9.1, 9.2: strong trace, positive-time regularity, both energy identities.
Section 1.4: builds on the authors' 2D Euler papers [HQSZ26a, b]; centrifugal instability [HG62].
Nothing on these pages contradicts Sections 3-9 as read. Point (b) of the first block stays open until page 9-19
and Section 9.4 are compared: the shooting prescribes ONE observation value per solution; a continuum needs the
map theta -> prescribed value injective.

## PDF pages 9-12 (read 12 Nov 08:5x)
Pages 9-10: related work (Jia-Sverak, Guillod-Sverak, Vishik, Albritton-Brue-Colombo, Hou-Wang-Yang [HWY25] = the
first paper of this row, Ionescu-Jia-Palasek, Buckmaster-Vicol, Cheskidov-Luo, Tao, Palasek, Coiculescu-Palasek,
Cheskidov-Dai-Palasek, Yudovich, Brue-Colombo-Kumar, [HQSZ26a,b], Choi). No mathematical claim of this paper there.
Conventions (1.5): Fourier transform unnormalised in full space, unitary in z ((3.2)), horizontal transform
unnormalised with ||q||_2 = (2 pi)^-1 ||q^h||_2 (2D Plancherel: correct); CA^P = polynomial in A before the final
choice of A, C(A) after.
Section 2.1 scales: l_n = R^-n, R = e^{rho A}, b = e^{beta A}, rho = c_*/8;
 t_p = (2 + Theta log A)/A, t_f = t_p + 16 A^2, t_* = R^2 t_p; T_n = l_n^2 t_p, l_n^2 t_* = T_{n-1}
 (by hand: l_n^2 R^2 t_p = l_{n-1}^2 t_p. Agrees). G = c_* - omega. Order of choice: frequency band and Theta,
 then beta, then A; restrictions in (8.1); depth varies only afterwards.
(2.1) Q_t - Lap Q + (Q.grad)Q + grad P_Q = (d_z P_Q) e_z, ||d_z P_Q(t)||_2 <= C A^2 b^{-1/2} t^{-3/4}.
(2.2) L_V h = Lap h - P div(V(x)h + h(x)V); correction e: (d_t - L_Q) e = F_Q - P div(e(x)e), e(0) = 0,
 F_Q = -P((d_z P_Q) e_z).
 X norm: sup_{0<t<=l_max^2} (t^{-1/4}||e||_2 + t^{1/4}||grad e||_2 + t^{1/2}||e||_inf);
 Proposition 3.4: ||e||_X <= C_rho A^P e^{C_rho A} b^{-1/2}. Stated consequence ||e||_inf ||grad e||_2 <=
 t^{-3/4}||e||_X^2: t^{-1/2} * t^{-1/4}. Agrees.
 Propagator: ||U_Q(t,s)|| on axisymmetric L^2_sigma <= K_Q (t/s)^{eps_Q}, 0 < eps_Q < 1/4 (Lemma 3.3); with the
 residual t^{-3/4} this leaves an integrable singularity: int_0^t (t/s)^{eps} s^{-3/4} ds finite iff eps < 1/4.
 That is exactly why eps_Q < 1/4 is needed. Agrees with Section 3 as read.

## PDF pages 13-16 (read 12 Nov 08:5x)
p. 13: int_0^t (t/s)^{eps} s^{-3/4} ds = t^{1/4}/(1/4 - eps). By hand: t^eps * t^{1/4 - eps}/(1/4 - eps). Agrees.
 W_T(r) = r T^-2 e^{-r^2/(4T)}, T = 1 + t (the same U_d as page 5).
 Fiber v^z(r,k) = (k f_r, f_theta, i D_r f_r), D_r f = f' + f/r; L_k = -d_r^2 - r^-1 d_r + r^-2 + k^2;
 C_k(0) = [[0, 2k L_k^-1 Omega_1], [-k B_1, 0]], Omega_1 = e^{-r^2/4} (angular velocity U/r of r e^{-r^2/4}),
 B_1 = (2 - r^2/2) e^{-r^2/4} (its axial vorticity (1/r)(r U)': 2 e^{-r^2/4} - (r^2/2) e^{-r^2/4}. Agrees).
 (2.4): sigma f_theta = -k B_1 h and sigma h = 2k L_k^-1 Omega_1 f_theta give
 sigma^2 L_k h = -2 k^2 Omega_1 B_1 h = -k^2 (4 - r^2) e^{-r^2/2} h. Agrees with Phi = (4 - r^2) e^{-r^2/2}.
 Rayleigh quotient: pairing (2.4) with h r dr and dividing by k^2: numerator int (r^2 - 4) e^{-r^2/2} |h|^2 r dr,
 denominator int (|h|^2 + k^-2 |h'|^2 + k^-2 r^-2 |h|^2) r dr. Agrees.
p. 14: sigma_k^2 < 2 e^-3 (the penalty terms are positive), sigma_k increasing to c_*: argument as stated is sound
 (fixed test function near r = sqrt 6, k -> infinity, then shrink the support).
 (1/r^3) d_r (r U_d)^2 = A^2 T^-4 (4 - r^2/T) e^{-r^2/(2T)}: from r U = A r^2 T^-2 e^{-r^2/(4T)}. Agrees; sign
 change at r = 2 sqrt T.
 lambda_k(t) = (1+t)^-2 sigma_{k sqrt(1+t)} ((4.12)); A int_{t_p}^t lambda_k <= c_* A (1/(1+t_p) - 1/(1+t)) =
 Gamma_src(t) ((8.3)). By hand: sigma < c_* and int (1+s)^-2 ds. Agrees. Dilation: at time t the swirl is the
 unit swirl at radius sqrt T with angular velocity amplitude A T^-2, frequency k sqrt T. Consistent.
 (2.5) J = P d_z(e_z delta_0), S_A = U_d(t_p, 0) J, n_A = ||S_A||_2, g = S_A/n_A;
 J^z(k) = (i k/sqrt(2 pi)) P_k(e_z delta_{0,h}): unitary transform of the 3D Dirac mass is (2 pi)^-1/2 delta_{0,h}.
p. 15: w has no factorial: (d_t - L_U) w = -P div(v(x)v), w(t_p) = 0. S as on page 6.
 Sign identity: int S = s_h I + (s_z - s_h) e_z(x)e_z; P div(s_h I delta_0) = P grad(...) = 0;
 - int_{t_p}^{t_f} P div((int S) delta_0) dt = - int (s_z - s_h) dt J = -M J with M = - int (s_h - s_z) dt. Agrees.
p. 16: (8.6): M_{s*}(v_f(t_f)) <= C A^P e^{2 rho A} M_{s*}(f); ||v_f(t_f)||_{H^4} <= C A^P ||f||_2 +
 C A^P e^{K_{s*} A} b^-1/2 M_{s*}(f), s_* = 19/8. A^-P e^{2GA} <~ M <~ A^P e^{2 c_* A}.
 Symbol identity -i P(xi) diag(1,1,0) xi = i xi_z P(xi) e_z: diag(1,1,0) xi = xi - xi_z e_z and P(xi) xi = 0. Agrees.
 (5.39): ||F_{f,k} - J_k||_{H^{-17/4}_{y_h}} <= C A^P (1+|k|)^{11/4} R^{-7/4} e^{2 omega A}, F_{f,R}(y) =
 R^4 w_f(t_f, R y)/m_f, m_f = -M_f. Decay: R^{-7/4} e^{2 omega A} = e^{(-7 rho/4 + 2 omega) A}, 2 omega < rho/32.
 R^4: delta(R y) = R^-3 delta(y) and one derivative gives R^-1. Agrees.

## PDF pages 17-19 (read 12 Nov 08:5x)
p. 17: (2.6) = (8.7) rescaled: ||R (U_ubar(t_*, t_f) w_f(t_f))(R .) + a_f M_f R^-3 S_A||_{H^4} <= C A^P M_f R^-3
 e^{-kappa_r A}, 0 < kappa_r < rho, a_f = 1 + O(A^-1) > 0. Sign and power: R^4 w(t_f, R .)/m ~ J with m = -M
 (page 16), the velocity rescaling carries one factor R, so R w(R .) ~ -M R^-3 J and after the parent evolution
 -a_f M R^-3 S_A. Agrees. Amplitude law R(u - ubar)(t_*, R .) ~ -a_f ||S_A||_2 M_f R^-3 a^2 g: the second-order
 term is a^2 w_f and S_A = n_A g. Agrees with (1.10) and with A ~ a_f n_A M_f R^-3 a^2 on page 18.
 (2.7) = (8.2): C_A = {g + zeta: <zeta, g> = 0, ||zeta||_{H^4} <= e^{-3 rho A/8}, M_{19/8}(zeta) <= e^{rho A/4}}.
p. 18: series h = sum_{m>=1} (-a)^m V_m, V_1 = v_f, V_2 = w_f, (d_t - L_ubar) V_m = -P div sum_{j=1}^{m-1}
 V_j (x) V_{m-j} ((8.12)). By hand: h solves (d_t - L_ubar) h = -P div(h (x) h), h(t_p) = -a f; the coefficient
 of (-a)^m is the stated sum; m = 2 gives the equation of w on page 15. Agrees.
 Crossings: a_- = e^{-(13 rho + rho/32) A}, a_+ = e^{-12 rho A};
 A^-P e^{(2G - 3 rho) A} a^2 <= A(a, f) <= A^P e^{(2 c_* - 3 rho) A} a^2. With 2 c_* = 16 rho:
 A(a_-)/a_- <= A^P e^{(13 rho - 13 rho - rho/32) A} = A^P e^{-rho A/32};
 A(a_+)/a_+ >= A^-P e^{(16 rho - 2 omega - 3 rho - 12 rho) A} = A^-P e^{(rho - 2 omega) A}, positive rate since
 2 omega < rho/32. Both as printed. eta_reg = e^{-rho A}.
p. 19: orbit a_0 = B_N(lambda_N), f_0 = F_N(lambda_N), a_-/2 < lambda_N < 2 a_+, N transitions, a_N = a_*.
 U_N(0) - ubar_N(0) = -(lambda_N/n_A) l_N^-1 J_{eta_reg}(x/l_N), L^2 norm (|lambda_N|/n_A) l_N^{1/2}
 ||J_{eta_reg}||_2 -> 0. <U_N(T_0) - ubar_N(T_0), -g> = a_*: at the outermost radius the difference is -a_N f_N
 with <f_N, g> = 1. Agrees. Convergences listed: uniform energy, tightness, strong L^2((0,T_0) x R^3), C_w L^2.
 ||U - ubar||_2 <= C_A t^{1/4}, ||U - ubar||_inf <= C_A t^{-1/2}: scaling of l^-1 f(x/l) at t ~ l^2
 (L^2 norm l^{1/2}, sup norm l^-1). Consistent.

## Comparison with Sections 3 to 9 (PDF pages 106-107 looked at again for the proof of Theorem 1.1)
(a) u_0: smooth away from the origin, in L^q for 1 <= q < 3 (the sum of l^{3/q - 1} over the radii), in
 L^{3,infty} ((9.6), (9.20)), not in L^3 and in no L^{3,r} with r finite ((9.8)). As stated in (i).
(b) Pairwise distinct for ALL pairs: (9.26) with ||v||_inf^2 <= C/t integrable on [eps, T_0] shows that two
 members equal at one positive time are equal up to T_0; (9.24) gives each branch its own terminal coordinate
 a_* at T_0, and a_* >= a_- > 0 separates every branch from the reference. So (9.27) holds for every pair,
 which is the first half of (iv).
(c) The observation of (iv): the proof of Theorem 1.1 cites (9.24) to (9.27) for "the fixed compact observation".
 The compactly supported test is phi_1, an approximation of psi_1 = -l_1^{-3/2} g(x/l_1), at the level n = 1,
 so t_w = T_1 = l_1^2 t_p lies in (0, T_0) and T = T_0; the pairing is at least a_- l_1^{1/2}/2 > 0 for every
 branch. As stated.
(d) (ii): C([0,T]; L^2), both energy equalities through zero and smoothness at positive times are Propositions
 9.1 and 9.2 ((9.22)); the pressure in L^{5/3} comes from the velocity in L^{10/3} of space-time.
(e) (iii): (9.15) to (9.18) give the range 2/p + 3/q > 1, including q = infinity with p < 2; (9.20), (9.21)
 give L^infty L^{3,infty}.
(f) Parameters: Section 2.1 and (2.6), (2.7), the crossings a_-, a_+ and eta_reg = e^{-rho A} are the ones used
 in Sections 5, 7 and 8 as read (rho = c_*/8, 2 omega < rho/32, s_* = 19/8, t_f = t_p + 16 A^2, t_* = R^2 t_p).
(g) Corollary 9.3 continues each branch to a global suitable Leray-Hopf solution by the mollified construction
 from the value at T_0.
The paper carries a "Disclosure of AI assistance" paragraph (page 107).
No disagreement found between the statement, the overview and the proofs.
