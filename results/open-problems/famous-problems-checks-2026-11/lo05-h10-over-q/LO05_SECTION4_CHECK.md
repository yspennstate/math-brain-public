# LO05: Section 4 (the height bound, Theorem 2.4) read line by line (12 Nov 2026)

Source: lit/openai_oct6/paper_c.txt, lines 1101-1861 (text extraction of paper.pdf in openai/math tree
0a112e434f6bf7f316e2999a63813ce58447e432). Each step below was re-derived by hand; the arithmetic of 4.1 was
also run as a script (lo05_check.py and a one-line check). The cited inputs [48], [49] are in LO05_CITED_INPUTS.md.

| Part | Content | Check | Result |
|---|---|---|---|
| 4.1 | B of discriminant 210, X = Sh_{O^x} of genus 5, W = (Z/2)^4, X* = P^1 with five rational branch values | area (1/6)(1)(2)(4)(6) = 8 gives g = 5; Q(i), Q(sqrt -3) split at 5, 7, so no elliptic points; Riemann-Hurwitz r = 5 - 4 g*; -30, -42, -70 are nonsquares mod 7, 5, 3; 105, 210 ramify at 2 | holds |
| 4.2 | Siegel datum psi(x,y) = Trd(Delta x ybar), fine level, Y -> X unramified, fibers over a rational s geometrically isogenous to their conjugates, moduli map nonconstant | Delta pure makes psi alternating; countability argument for nonconstancy | holds |
| 4.3, Lemma 4.1 | fibre field of degree <= (deg pi)!, unramified outside S and the primes of odd contact; good reduction outside S | local equation t = z^2 by Hensel at odd q; even contact gives an unramified square root; valuative criterion on proper Y | holds |
| 4.4, Lemma 4.2 | h(pi(y)) <= C(1 + max(0, h_F(A_y))) | theta-group normalization (g_x^{k^2} = 1, 2k divides k^2 as k = r^2 is even); h^0 = r^4; nonconstancy of theta-null via constant Fourier coefficient; Pazuki's Cor. 1.3(2) with h_FD = h_F + log pi | holds |
| 4.5, Lemma 4.4 | one Galois field L of bounded degree, unramified outside T, for all Homs between conjugates | finite image on a bounded-rank lattice; Neron-Ogg-Shafarevich | holds |
| 4.6 | C_B = Q or imaginary quadratic; CM case bounded (ineffectively); generic case D = B; sign cocycle (4.8) | degree identity |c|^4 = deg mu_g deg mu_h / deg mu_gh re-derived; epsilon = c/|c| | holds |
| 4.6, Lemma 4.5 | Dirichlet chi of order <= CM, beta with beta^2 = chi and coboundary epsilon, trivial on inertia outside T | local square-root obstruction = value at -1; Hasse-Brauer-Noether; order <= 2 prod(q - 1) <= CM; conjugacy invariance on G_L; quadratic twist removes the finitely many offending inertia signs | holds |
| 4.7 | r_2 modular by [49]; r_3 matched by Chebotarev | read earlier (lines 1609-1700) against [49] | holds |
| 4.8, Lemma 4.7 | N <= C M^2 | tame exponent <= 2 at large q in T; uniform unit-group cut for beta (squaring onto U^b, U^{b+e} at 2); Grothendieck over F(A[p0]); Swan <= 2 u_q | holds |
| 4.9, Lemma 4.8 and (4.14)-(4.16) | J_1(N) ~ A x D0 over L'; h_F(J) <= C N^12; h_F(A) <= C M^C | invariants commute with scalar extension; deg j <= N^2, Javanpeykar gives N^2 N^10; dimension count 8 g0; Gaudron-Remond log-degree polynomial in M; Bost lower bound -(dim/2) log(2 pi^2) | holds |

Remarks. The CM case uses the finiteness of CM j-invariants of bounded degree, which is ineffective; the theorem
needs only the existence of the constants. The Zarhin step in 4.9 is not needed for (4.5), which asks for no
principal polarization, and does no harm. The statements of [5] (Carayol), [23] (Gaudron-Remond), [32]
(Javanpeykar) and [51] (Pazuki) were checked against the forms the paper quotes, not against the sources.

What this changes: Section 4 shows no gap on a first independent read. LO05 stays REPORTED_SOLVED: Section 3's
other lemmas, Section 5 (the elliptic inputs), Section 2's reduction, and the companions' proofs are unread, and
a solved mark needs a second independent audit.
