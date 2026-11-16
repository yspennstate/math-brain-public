# NT01 (Riemann hypothesis row): the October 2026 zero-free-region preprints, what has been checked

Status: provisional. The row is the Riemann hypothesis itself, which neither preprint claims; the row keeps its
place. This file records what was read and what was tested in the 49-page preprint of 5 Oct 2026 (openai/math,
commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, tree b46286acfa00dca1008962a0276b3fa1c3679404), whose Theorem
1.1 states that Hecke L-functions over Q(sqrt(-3)) have no zeros in Re s > 11/12. The reading notes, the section
map and the list of follow-up papers are in STATE.md.

## Read

Sections 1 to 7 and Appendices A and B (lines 1 to 2067 of lit/openai_oct5/paper_c.txt, with pages 6, 11 to 14
and 18 to 45 of the PDF by eye). Of the sources it cites: Dunn and Radziwill, arXiv 2109.07463, pages 16 to 19 and
78 by eye; Goldmakher and Louvel, arXiv 1112.1642v2, pages 1 to 3. Not read: Patterson's 1977 paper itself, and
the 199-page preprint of 30 Sep 2026.

## Tested by computer: Lemma 4.1

Lemma 4.1 is the arithmetic the whole dual mean-square estimate rests on: it converts Moebius coefficients into
normalised cubic Gauss sums and back. `nt01_check.py` computes, for every squarefree primary n in Z[w]
(w = exp(2 pi i/3), n = 1 mod 3, prime to 6) of norm at most 1500 built from primes of norm at most 200, the
sextic residue symbol chi_n and the normalised Gauss sums gamma_j(n) for j = 1, 2, 3, -1 by direct summation over
the residues mod n, and tests each identity of the lemma to 1e-8.

With the definitions as printed on page 13 (alpha(n) = n/|n|, G(n) = conj(chi_n(4)) gamma_3(n)), over 227 values
of n and 168 coprime pairs (a, b), output `nt01_check.out`:

| identity | holds |
|---|---|
| \|gamma_j(n)\| = 1 for j = 1, 2, 3, -1 | 227 of 227 |
| (4.2) gamma_2(n)^3 = mu(n) alpha(n) | 227 of 227 |
| (4.2) gamma_1(n) gamma_2(n) = mu(n) alpha(n) G(n) | 227 of 227 |
| (4.3) gamma_1(n) gamma_-1(n) = chi_n(-1) | 227 of 227 |
| (4.4) conj(alpha(n)) gamma_2(n) gamma_1(n) = mu(n) G(n) | 227 of 227 |
| (4.5) mu(n) gamma_-1(n) = chi_n(-1) G(n)^-1 conj(alpha(n)) gamma_2(n) | 227 of 227 |
| \|G(n)\| = 1 | 227 of 227 |
| (4.1) chi_b(a)/chi_a(b) is +1 or -1 | 168 of 168 |
| (4.1) G(ab) = G(a) G(b) R(a, b) | 168 of 168 |
| (4.6) a(ab) = a(a) a(b) chi_b(a)^4 with a = conj(alpha) gamma_2 | 168 of 168 |

Controls that must fail, and do: gamma_2^3 = alpha without the Moebius sign (0 of 51 with mu = -1); G(ab) =
G(a)G(b) without R (0 of 88 pairs with R = -1; R = -1 on 88 of the 168 pairs, so the sign is exercised); (4.6)
with chi_b(a)^2 in place of chi_b(a)^4 (0 of 118). The wrong conjugate of alpha in (4.2), (4.4), (4.5) holds
only on the 9 values of n that are real.

### Identity (4.7)

In (4.7) the quotient b a^-1 is taken in a ray class group of a modulus the paper fixes only as "sufficiently
large". Given (4.1), identity (4.7) is equivalent to R(a, a) = chi_a(-1), where R(a, a) means
chi_a'(a)/chi_a(a') for a prime a' in the ray class of a. `nt01_check47.py` tests this for the 44 primary primes
a of norm at most 200 against every primary prime a' of norm at most 2500 congruent to a modulo M, for nine
moduli M (output `nt01_check47.out`):

| modulus M | pairs (a, a') | R(a, a') = chi_a(-1) | a for which R(a, a') does not depend on a' |
|---|---|---|---|
| 1 | 15928 | 9656 | 9 of 44 |
| 2 | 5272 | 3182 | 9 of 44 |
| 3 | 15928 | 9656 | 9 of 44 |
| 6 | 5272 | 3182 | 9 of 44 |
| 9 | 1720 | 1024 | 9 of 44 |
| 4 | 1283 | 1283 | 44 of 44 |
| 12 | 1283 | 1283 | 44 of 44 |
| 24 | 275 | 275 | 44 of 44 |
| 36 | 114 | 114 | 42 of 42 |

So (4.7) holds in every case once the modulus is divisible by 4, and fails for moduli prime to 2 or divisible
by 2 only; chi_a(-1) = -1 for 24 of the 44 primes, so the sign is exercised. This is what quadratic reciprocity
in Z[w] predicts: for primary a and b the cubic parts of chi_b(a) and chi_a(b) agree, the ratio of the quadratic
parts is the Hilbert symbol of (a, b) at the prime 2, which depends on a and b modulo 4 only, and
(a, a) = (a, -1). "Sufficiently large" therefore means: divisible by 4 (the condition n = 1 mod 3 is already in
"primary"). The statement that G itself factors through the ray class group is not tested.

A by-hand cross-check: the duplication formula for Gauss sums, g(chi) g(chi psi) = conj(chi(4)) g(chi^2) g(psi)
with psi quadratic, applied to chi = chi_n, gives gamma_1 conj(gamma_2) = conj(chi_n(4)) gamma_2 gamma_3, hence
gamma_1 gamma_2 = gamma_2^3 conj(chi_n(4)) gamma_3 = mu alpha G. So (4.2) to (4.5) are the standard identities
with the paper's normalisation, as the lemma says.

## Sections 4.2 to 4.4, checked by hand

Read against pages 14 to 18 of the PDF (page 14 by eye; the text file drops the square root and the bar in
(4.8) as well).

**Lemma 4.2** (Poisson summation twisted by a primitive character, with excluded primes). Derived
independently: Poisson summation on the class a mod m gives
sum_{l = a (m)} f(l) = N(m)^-1 sum_h e(ah/m) fhat(h/m); summing against chi(a) gives
sum_l chi(l) f(l) = gamma(chi) N(m)^-1/2 sum_h conj(chi(h)) fhat(h/m); and for f(u) = Phi(|u|^2/H') one has
fhat(w) = H' Phihat(H'|w|^2). With H' = H/N(d) after the inclusion-exclusion k = dl this is (4.8) exactly as
printed: prefactor H gamma(chi)/sqrt(N(m)), weights mu(d) chi(d)/N(d), conj(chi(h)), argument
H N(h)/(N(d)N(m)).

Tested numerically as well (`nt01_check42.py`, output `nt01_check42.out`) with Phi(t) = exp(-pi t), for which
Phihat(t) = (2/sqrt 3) exp(-4 pi t/3): chi = chi_n^j for the eight primary primes n of norm 13, 19, 37, 73 and
j = 1 to 5, r with no, one and two excluded primes, H = 7 and 23.5; both sides summed until the tail is below
1e-13. (4.8) holds in 240 of 240 cases, largest difference 4.9e-14. The left side is a sum over elements, so it
vanishes unless chi^j is trivial on the six units; it is nonzero in 156 of the cases, and on those two wrong
forms fail every time: 1/N(m) in place of 1/sqrt(N(m)) (0 of 156) and chi(h) without the bar (0 of 120 with
chi^j not real).

**Lemma 4.4** (removing an exclusion). With n = dm and (4.6), a(dm) = a(d)a(m)chi_m(d)^4, the column sum with
(n, r) = 1 becomes sum_{d | r0} mu(d) a(d) chi_d(k) chi_d(f)^4 C_1(X/N(d); k, df); the factor chi_m(d)^4 joins
chi_m(f)^4 and enforces (m, d) = 1; Cauchy-Schwarz over the tau(r0) divisors and the injection f -> df into
[F N(d), 2F N(d)) give (4.10), and (X/N(d))(F N(d)) = XF keeps the normalisation. Correct.

**Proposition 4.5**, the algebra down to (4.16) and the count (4.17). Checked line by line:
- the Gauss sum of chi_z1 conj(chi_z2) splits by the Chinese remainder theorem into
  chi_z1(z2) conj(chi_z2(z1)) gamma_1(z1) gamma_-1(z2); (4.4) and (4.5) turn the two factors into
  mu(z1) G(z1) conj(a(z1)) and mu(z2) chi_z2(-1) G(z2)^-1 a(z2); the leftover
  chi_z2(-1) conj(G(z2)) G(z1) R(z2, z1) is G(z1 z2^-1) by (4.7). So the coefficient is a function of the ray
  class of z1 z2^-1 times conj(a(z1)) a(z2), which is (4.15). This is where (4.7), hence a modulus divisible
  by 4, is used;
- the weights: D^-1 times H/(N(e) sqrt(N(z1)N(z2))) times W W = H N(g)/(D^2 N(e)) W0 W0, as displayed;
- the Moebius removal of (z1, z2) = 1 with zj = v mj: the v-part has modulus 1_(v,h)=1, the m-part carries
  chi_m(h e^5 v^4), and the argument of Phihat gets N(v)^2;
- the change of variables b = g/e, f = ev, k = eh is a bijection onto coprime squarefree b, f and nonzero k
  (e = (f, k) because (v, h) = 1), with gv = bf, h e^5 v^4 = k f^4, mu(e)mu(v) = mu(f), N(g)/N(e) = N(b), and
  H N(h)/(N(e)N(v)^2 ...) = H N(k)/(N(f)^2 ...): this is (4.16);
- the count: (H/D^2) times sum over b of N(b) times (XF)^2, with O(B) ideals b and XF = D/B, is H: (4.17).
The last step uses Lemma B.2, checked next.

**Lemma B.2** (Appendix B: a bound for every test function gives the bound for a smooth kernel). As printed on
page 45, (B.4) bounds sum_r c_r sum a_{1,r}(n1) conj(a_{2,r}(n2)) K_r(x1, x2) by
sqrt(M1 M2) sup_r ||K_r||_{C^(2m+4)(I^2)}. The proof holds: Mellin inversion on the box writes
K_r(x, y) = int int b_r(s, t) U_s(x) conj(U_t(y)) ds dt with U_t(x) = V(x) x^(it) and
|b_r(s, t)| << (1+|s|+|t|)^-q sup_r ||K_r||_(C^q); Cauchy-Schwarz over r and the hypothesis give
sqrt(M1 M2) ||U_s||_(C^m) ||U_t||_(C^m) with ||U_t||_(C^m) << (1+|t|)^m; and the integral of
(1+|s|)^m (1+|t|)^m (1+|s|+|t|)^-q converges once q > 2m+2, so q = 2m+4 is enough. The hypothesis is applied to
the complex functions U_t; (4.12) is stated for smooth W, and a complex W splits into real and imaginary parts
at the cost of a constant. In Proposition 4.5 it is used with rows (f, k), weight 1, coefficients
mu(f) 1_((f,b)=1), both families equal to S_U(b, f, k), and M1 = M2 = D^(eps/2) (XF)^2, which is what (4.17)
takes. The weight Phi there has supp Phihat in [0, C_Phi], so the kernel vanishes for N(k) above the stated
range. Lemmas B.1 (Mellin separation with the coefficient bound) and B.3 (weighted Cauchy-Schwarz) are standard
and correct as read.

So Section 4 reduces the mean square of Proposition 3.1 to the dual estimate (4.12) correctly. The dual estimate
itself is the content of Sections 5 to 7.

## Section 5, checked by hand

Read on pages 18 to 22. Section 5 derives the dual estimate (Proposition 5.1: E(H, X, F) << D^eps XF whenever
H <= XF D^-kappa, where H is the dual length) from two inputs proved later: Proposition 5.2 (the completed
mean square, Section 6) and Proposition 5.4 (the transfer estimate, Section 7). What Section 5 itself does was
checked line by line.

**The completed sum (5.3).** With V(y) = sqrt(y) W(y), the term of T(X; Psi) with indices n, b equals
X^-1/2 a(n) Psi(n) conj(alpha(b))^3 Psi(b)^3 sqrt(N(b)) W(N(n)N(b)^3/X), and b = 1 gives the column sum of
(4.9).

**Lemma 5.3** (cube inversion).
- (5.8): the term of mu(h) conj(alpha(h))^3 Psi(h)^3 N(h)^-1 T(X/N(h)^3) with indices n, c is the term of
  T(X) with cube index b = hc times mu(h), because N(h)^(3/2)/N(h) = sqrt(N(h)) and alpha, Psi are completely
  multiplicative; summing mu(h) over h | b leaves b = 1. The sum over h is finite.
- The short part (5.9): weighted Cauchy-Schwarz, then Proposition 5.2 at column length X/N(h)^3 >= 1, gives
  after the average over f the bound H + H^2 F N(h)^3/X; the sum of N(h)^2 over N(h) <= H_c is << H_c^3, and
  H^2 F H_c^3/X <= H^2 F (X^2/H^2)/X = XF.
- The long part: with b = hc, sqrt(N(b)/X) = N(b)^-1 L_b^-1/2 and Psi_k(b)^3 = xi(b)^3 chi_b(k)^3 1_((b,f)=1)
  (chi is sextic), so P_long is a combination of column sums at length L_b = X/N(b)^3 with coefficients bounded
  by tau(b)/N(b), and sum tau(b)/N(b) <= (sum 1/N(c))^2 << log^2.
- L_b <= 1: the support forces L_b >= 1/v, the column has O(1) terms, and the mean square is << H/L_b << H.
- H^2 <= X: then H_c = X^(1/3) and N(b) > H_c gives L_b < 1, so the supremum is empty.
So (5.7) is correct as printed.

**The induction of Section 5.5.** The statement proved by induction on j is the proposition under the extra
condition H <= D^(j kappa). Base: H <= 1 and counting give E << H X, which is at most XF. Step: for
H <= D^((j+1) kappa), Lemma 5.3 leaves the supremum over b with N(b)^3 > H_c^3 = X^2/H^2; Proposition 5.4 at
column length L_b and target XF is applicable (L_b <= X, max(H, L_b F) <= XF), and every mean square in its
supremum has
H' <= H L_b/(XF . F) = H/(N(b)^3 F^2) < H (H/XF)^2 <= D^(-2 kappa) H <= D^(j kappa),
H'/Sigma' <= H/XF <= D^-kappa, Sigma' <= L_b <= XF,
so the induction hypothesis covers it, with the test function of C^m norm at most one on the enlarged interval
[u/16, 4v] and the derivative order m independent of the interval. The losses are D^(eps/3) three times. The
depth is the fixed number ceil(C0/kappa), so the constants and derivative orders stay bounded. Correct.

**Section 5.6.** With H = D^(1+theta) the ranges (4.11) give dual length at most C D^(1-theta)/B^2 and
XF = D/B, so the ratio is at most C D^-theta, and Proposition 5.1 applies with kappa = theta/2 and C0 = 2; the
cases X < 1 and dual length below 1 are counting. So (4.12) holds given Propositions 5.2 and 5.4.

So the whole chain from Theorem 1.1's mean square down to two statements is checked: Proposition 5.2 (theta
transformation and the quadratic large sieve, Section 6) and Proposition 5.4 (Section 7).

## Section 6, checked by hand

Read on pages 22 to 29, with page 6 for (2.10). Section 6 proves Proposition 5.2, the mean square of the
completed sums T(X; k, f) over rows 0 < N(k) <= H: the bound D^eps ||W||^2 (H + H^2 N(f)/X) of (5.5).

**Lemma 6.1 (the completed sum as a twisted theta function).** On the page, (2.10) reads c_theta(n b^3) =
3^(5/2) |b| conj(chi_n(lambda)^2) gamma_2(n), with c_theta the Fourier coefficient of the conjugate of Kubota's
theta function; the text file drops both bars. With that, (6.3) follows term by term from the coefficient
formula (the general term matches (5.3); sqrt(N(b)) = |b|; chi_b(lambda)^6 = 1), and (6.4) from finite Fourier
inversion on O/q with e(w) = exp(2 pi i Tr(w/lambda)) and sum of phi-hat equal to phi_k(0) = 0. Correct as
printed, given (2.10). Formula (2.10) is Patterson's evaluation of the cubic theta coefficients; it agrees with
the statement of that theorem as I know it (coefficient at lambda^(3n-3) c d^3 equal to conj(g(1, c)) |d/c|
3^((n+5)/2), constant term 3^(5/2)/2), and with the source as recorded by Dunn and Radziwill (see the section on the cited results below).

**Section 6.2 (statements only).** Proposition 6.2 (T(X; Psi) is a sum of O(2^|P|) terms (6.9) with local
factors B_{p,j} of (6.5), the transformed weight (6.6) and the coefficients d_sigma of the conjugate theta
function at three cusps (6.7), (6.8)), Lemma 6.3 (uniformity in the twist k0) and Lemma 6.4 (support (6.10), the
bound |d(u lambda^m n b^3)| <= 27 3^(m/6) |b| of (6.11), the decay (6.12) of the transformed weight) are proved
in Appendix A.2, not read here. Lemma 6.5 is the quadratic large sieve over K, cited from Goldmakher and Louvel
(Theorem 1.1 of reference [13]); the hypotheses are stated in the proof, the source was not opened.

**Lemma 6.6 (squarefree rows), pages 26 to 29, checked line by line given the statements above.**
- (6.17): for k = u0 t k0 the exponent at p is j_p = v_p(k) + 4 v_p(g) mod 6, from chi_n(k) chi_n(g)^4.
- (6.18): every prime of k0 has j_p = 1, the local factor is chi_p(x)^(-3) = chi_p(x)^3, and chi_p(b)^9 =
  chi_p(b)^3, so the k0-dependence of a transformed term is the quadratic character chi_k0(n b)^3 times a
  bounded scalar.
- The normalisation: with l = u lambda^m n b^3, N(l) = 3^m N(n) N(b)^3, so d alpha psi / sqrt(N(l)) equals
  A_{u,m}(n, b) / (3^(m/3) sqrt(N(n)) N(b)) with |A_{u,m}| <= 27 by (6.11); the weight argument is
  3^m N(n) N(b)^3 X / (N(c_*)^2 N(k0)^2). Both match the displayed term and (6.15) with Y = N(c_*)^2 H0^2 / X.
- The local identity at j_p = 4: B_{p,4}(x) = -q^(-1/2) + q^(1/2) 1_{p|n} + q^(1/2) 1_{p not | n, p | b}, and
  the three-term reindexing identity (n = p n' and b = p b') were recomputed: the second term gives
  chi_k0(p)^3 S_m[A^(p,n), qY] and the third q^(-1/2) chi_k0(p)^3 S_m[A^(p,b), Y/q], as printed.
- The update table for (a^2, Y) follows: (a^2, q^2 Y) for j_p not in {0, 4}; (a^2/q, q^2 Y) for j_p = 0; the
  three options (a^2/q, q^2 Y), (a^2, qY), (a^2/q, Y/q) for j_p = 4. So a^2 never increases and a^2 Y grows by
  at most q^2 at a prime of t (there j_p is odd), by q when j_p is 0 or 4, by q^2 when j_p = 2, which needs
  v_p(g) >= 2. This gives (6.16): a^2 Y << H0^2 N(t)^2 N(g) / X.
- The large sieve step: R >= z_* = 3^m U B^3 / Y because N(b) >= B and N(k0) <= H0; Lemma 6.5 applies to
  G_{b,s} with coefficients of square sum << a^2; the two weighted Cauchy-Schwarz steps give (6.20); U <= 81 Y z_*
  because m >= -4 and B >= 1; with A = 3 and sigma <= 1 the exponent left on (1 + z_*) is at most -2.
- The dyadic sums (log^2(2 + Z) and sqrt(Z)) and the geometric sum over m >= -4 converge as stated, giving
  a D^eps (sqrt(H0) log^2(2 + Y) + sqrt(Y)) and then, with (6.16) and H0 N(t) = H, the bound H + H^2 N(g)/X.

**Proof of Proposition 5.2 (page 29).** k = u0 s v^2; chi_n(v)^2 = chi_n(v)^8 gives T(X; u0 s v^2, f) =
T(X; u0 s, f v^2); Lemma 6.6 with row bound H/N(v)^2 and g = f v^2 (N(g) <= H N(f) <= D^(2 C0)) gives
(H + H^2 N(f)/X) / N(v)^2, and the sum over v converges. Correct.

So Section 6 is correct as printed, given three things it does not prove in place: Patterson's formula (2.10),
the theta transformation with its coefficient bounds (Proposition 6.2, Lemmas 6.3 and 6.4, Appendix A.2), and
the Goldmakher-Louvel large sieve.

## Section 7, checked by hand

Read on pages 29 to 34. Section 7 proves Proposition 5.4, the transfer estimate (5.11): the mean square A(W) of
(5.10) is bounded by D^eps Sigma (1 + S_m), with S_m the supremum of E(H', X', F')/Sigma' over the parameters
allowed by (5.12). Two Poisson summations and one regrouping.

**Lemma 7.1 (first Poisson summation), pages 29 to 31.** With n_i = C u_i the row character is
chi_u1 conj(chi_u2), of modulus norm L^2 z1 z2 / N(C)^2 (z_i = N(n_i)/L), and the exclusion (k, C) = 1 gives
d | C. Lemma 4.2 with length H/N(d) gives the prefactor (1/(LF)) (H/N(d)) N(C)/(L sqrt(z1 z2)), which is
w_{C,d} (z1 z2)^(-1/2), and the argument H N(h) N(C)^2/(L^2 N(d) z1 z2) of the transform; both as printed, and
the frequency range follows from the support of the transform. The zero frequency needs u1 = u2 = 1 and is
<< H ||W||^2. The column coefficient p_y with y = h f^2 carries both the dual character and the twist by f,
since conj(chi_x(h f^2)) = conj(chi_x(h)) chi_x(f)^4. The bound N(y) <= Y_{C,d} uses LF <= Sigma and
c_I >= 4 C_Phi v^2, so the (f, h) sum is dominated by the nonnegative form Q of (7.2) up to a divisor-bounded
multiplicity, and Lemma B.2 finishes. Correct.

**The paired identities.** (7.3) and its converse in the proof of Lemma 7.2 follow from Lemma 4.1 by a short
computation, done here: with A = a_xi/xi one has A gamma_1 = mu G by (4.4) and mu gamma_{-1} = chi_n(-1) G^(-1) A
by (4.3); the Chinese remainder theorem gives gamma(chi_u1 conj(chi_u2)) = chi_u1(u2) conj(chi_u2(u1))
gamma_1(u1) gamma_{-1}(u2), the two cross characters make R(u1, u2) by (4.1), and (4.7) turns
chi_u2(-1) G(u1) conj(G(u2)) R(u1, u2) into G(u1 u2^(-1)). The converse is the same computation with the roles of
gamma_1 and gamma_{-1} exchanged. So both rest on Lemma 4.1 only, which was tested numerically above.

**Lemma 7.2 (second Poisson summation), pages 31 and 32.** With n_i = g z_i the y-character is
conj(chi_z1) chi_z2 with exclusion (y, g) = 1, handled by e | g. Recomputed: the prefactor
Y mu(e) N(g)/(N(e) l) (using U U/sqrt(N(z1) N(z2)) = (N(g)/l) U0 U0), the identity
chi_z(dh) conj(chi_z(e)) chi_z(C)^4 = chi_z(deh) chi_z(Ce)^4, the zero-frequency term Z with its Euler factor, the
removal of (z1, z2) = 1 by w with (4.6) (the w-factors pair to 1_{(w,h)=1}, the surviving coprimality is
(n, tg/e) = 1), and the kernel argument Y N(h) N(g)^2/(N(e) l^2 x1 x2) at scale X' = l/N(gw). All as printed.

**Lemma 7.3 (the regrouping), pages 32 to 34.** With r = tg/e, f' = Cew, k' = deh:
- X0' = L/(N(r) N(f')), the prefactor c_I Sigma N(r)/L^2 and the Fourier parameter
  c_I Sigma F N(k') N(r)^2/(HL) were recomputed from w_{C,d}, Y_{C,d} and l; they depend on (r, f', k') only.
- The preimages of (r, f', k') are t | r, the ordered coprime factorisation f' = Cew with e | k', (w, k') = 1,
  d | (C, k'); every constraint of Lemma 7.2 and of (7.2) holds for each of them when the kernel is not zero
  (N(C) N(t) <= N(r) N(f') <= 2vL). Summing mu(e) mu(w) over them gives, at each prime p of f',
  (1 + 1_{p|k'}) - 1_{p|k'} - 1_{p not | k'} = 1_{p|k'}, so the regrouped sum runs over f' | k' with weight
  N(r) tau(r). This cancellation is what returns the sum to the family (4.9).
- Dyadic block R, F': X' = L/(RF'), Sigma' = L/R, H' = HL/(Sigma F R^2). From f' | k': F' <= H', so H' >= 1;
  (7.7) X'/N(j) >= F Sigma/H >= 1 for j | r; H'/Sigma' = H/(Sigma F R) <= H/Sigma, Sigma' <= L,
  H' <= HL/(Sigma F). These are exactly the conditions (5.12), also after the exclusion removal of Lemma 4.4.
- Lemma B.2 over rows (r, f', k') with weight << D^delta Sigma R/L^2 and O(R) values of r gives
  D^(2 delta) (Sigma R/L^2) R (L/R)^2 S_m = D^(2 delta) Sigma S_m. The zero-frequency total is
  << Sigma sum_C tau(C)/N(C)^2 sum_t 1/N(t) << D^delta Sigma.
Correct. Proposition 5.4 then follows from Lemmas 7.1 and 7.3 with j = 2m + 4 (derivative order 4m + 12).

## Appendix A.1 (proof of Lemma 4.1), checked by hand

Read on pages 35 to 37. With this the lemma no longer rests on the numerical table alone.

**(4.2).** The count #{x : 4x(1 - x) = y} = 1 + chi_p^3(1 - y) (u = 2x - 1) gives
chi_p(4) J(chi_p, chi_p) = J(chi_p, chi_p^3). The Gauss-Jacobi identity J(A, B) = sqrt(q) gamma(A) gamma(B)/gamma(AB)
turns this into gamma_3/gamma_4 = chi_p(4) gamma_1/gamma_2, and gamma_2 gamma_4 = chi_p^2(-1) = 1 gives
gamma_1 gamma_2 = conj(chi_p(4)) gamma_3 gamma_2^3, as printed (the bar is on the page). For gamma_2^3 =
J(chi_p^2, chi_p^2)/sqrt(q): J is in O of norm q; it vanishes mod p because the power sums of exponent
(q-1)/3 + l, 0 <= l <= (q-1)/3, vanish in the field O/(p); so J is a unit times p. The unit: the product of
x(1 - x) over x != 0, 1 is (-1)(-1) = 1 by Wilson, so the exponents j_x sum to 0 mod 3, and
w^j = 1 + j(w - 1) mod (w - 1)^2 gives J = q - 2 = -1 mod 3; with p = 1 mod 3 the unit is -1. So
gamma_2^3 = -alpha(p), and the Chinese remainder theorem carries both identities to squarefree n (the cross terms
chi_a(b)^3 chi_b(a)^3 are the same on both sides of the second one). `nt01_checkA1.py` confirms J = -p, and
never -conj(p), for the 118 split primary primes of norm at most 700.

**(4.6).** gamma_2(ab) = gamma_2(a) gamma_2(b) chi_a(b)^2 chi_b(a)^2 and cubic reciprocity
chi_a(b)^2 = chi_b(a)^2 for primary a, b. Correct.

**(4.1), the quadratic Gauss sum.** Formula (A.1), |c|^-1 sum_{x mod c} e(x^2/c) = (1/2) sum_{y mod 2O}
e(-c y^2/4), is proved in the paper by Poisson summation with a Gaussian regulariser; that limiting argument was
not reworked. Instead (A.1) was tested directly: `nt01_checkA1.py` computes both sides for every c = a + bw
coprime to 2 with |a|, |b| <= 14 and norm at most 330, 564 values, and they agree in all 564 (the conjugate
formula fails on all 290 values where the sum is +-i). From (A.1) the closed form
(1 + i^-b + i^a + i^(b-a))/2 follows by evaluating e at y = 1, w, w^2 (done by hand, and 564 of 564 by
computer). The rest was checked by hand: dependence on c mod 4 only; invariance under squares (the squares in
(O/4O)^x are 1, w, w^2, and y -> w^2 y permutes O/2O); the four classes 1, -1, lambda, -lambda are the
2-torsion of (O/4O)^x and the table 1, 1, i, -i is right; with Gquad = i^f (-1)^(ef) on the class
(-1)^e lambda^f and lambda^2 = -3 = 1 mod 4, the quotient is (-1)^(eh + fg + fh), a symmetric bicharacter.
Gquad(p) = gamma_3(p) by grouping x^2 = y, and to squarefree n because both sides pick up the same quadratic
symbols. chi_b(a)/chi_a(b) is the product of the two quadratic symbols because chi = chi^3 (chi^2)^-1 and the
cubic parts cancel by reciprocity; it extends from primes to all coprime primary a, b by multiplicativity on both
sides. chi_c(4) = (-2/c)_3 = (c/(-2))_3 is a character of c mod 2 (-2 is a primary prime). R(c, c) = chi_c(-1):
on the classes with f = 1 the norm is 3 mod 4. Correct.

**(4.7), (4.3) to (4.5).** G(1) = 1 = G(a) G(a^-1) R(a, a^-1) gives G(a^-1) = chi_a(-1) conj(G(a)) (bar on the
page), then (4.7) by bimultiplicativity. (4.4) is (4.2) times conj(alpha); (4.5) is (4.4) with
gamma_-1 = chi_n(-1)/gamma_1 and mu^2 = 1. Correct.

## Appendix A.2 (the theta transformation), checked by hand

Read on pages 37 to 44. A.2 proves Proposition 6.2 and Lemmas 6.3 and 6.4: the twisted sum T(X; Psi) of (5.3) is
O(2^|P|) dual sums (6.9) with scalars |C| <= 1/81, arithmetic factors B_(p,j), cusp coefficients d_sigma, an
additive character psi and the weight V-sharp of (6.6).

**Finite Fourier expansion, page 38.** (A.5) recomputed in its four rows (y = h_p^-1 u for h_p != 0; orthogonality
for h_p = 0, j != 0; the direct sum for j = 0). The shift z_h and the coefficient c_F(h) of (A.4) follow by
multiplying (A.3) over P, and the constant terms of the translates cancel because sum_h c_F(h) is the value of
the twist at 0, which is 0. Correct.

**Reduced denominators and the matrices, page 39.** c_F(h) != 0 forces every prime with j_p != 0 to be active, so
only primes with j_p = 0 can be inactive. At an active prime v_p(lambda^2 h_p/p) = -1 and the rest of z_h is
p-integral, so the reduced denominator is c = c_0 r, also when (h_0, L) != 1. With h_p = 0 mod M^2 the residue
of a mod M c_0 is fixed. delta' exists by the Chinese remainder theorem ((a, c) = 1, (r, M) = 1), b_g is
integral with the stated residues, g is in SL_2(O). In each of the three cases for H the matrix g_1 = g H^-1 was
multiplied out and is = I mod 3. Correct.

**(A.8), (A.9), page 40.** (A.9) recomputed in quaternions: with u = z + vj, g^-1(u + a/c) =
-delta'/c - (1/c) u^-1 (1/c), and (1/c)(conj(z) - vj)(1/c) = conj(z)/c^2 - vj/N(c). As printed.

**(A.10), pages 40 and 41.** All three cases follow from the determinant equation and cubic reciprocity. For
3 | c: c_1 = c, a_1 = a, and (c/a)_3 = (c_0/a)_3 (r/a)_3 = (c_0/a)_3 (a/r)_3. For v_lambda(c) = 1 the two
congruences printed are what the determinant gives, and for (c, lambda) = 1 the congruence -b_g c = 1 mod 9
removes the supplementary factors, so (delta'/(-b_g c))_3 = 1. Then kappa(g_1) = kappa_0 prod_(p|r) chi_p(a)^2
with kappa_0 fixed by h_0, the active set and r mod M^2. Correct.

**(A.11), (A.12), page 41.** a = sigma_p h_p mod p from the expression for a; (A.11) by the additive form of the
Chinese remainder theorem with eps_p = -((lambda^3 c/p) sigma_p)^-1. (A.12) recomputed in each case from (A.5):
for j != 0, 4 the sum over y = h_p^-1 of chi_p(y)^(j+2) e(eps_p y x/p) is a Gauss sum and gives
B_(p,j)(x) = N(p)^-1/2 chi_p(x)^(-j-2) with omega as printed; for j = 4 the character is trivial and the sum is
N(p)^-1/2 gamma_4 (-1 + N(p) 1_(p|x)); for j = 0 active the coefficient -1/N(p) and the cubic Gauss sum give
N(p)^-1/2 chi_p(x)^-2 with omega = -gamma_2(p) chi_p(eps_p)^-2; an inactive prime gives the scalar 1 - 1/N(p).
These are the B_(p,j) of (6.5), and B_(p,1)(x) = chi_p(x)^3 up to N(p)^-1/2 is the quadratic factor of (6.18).

**The archimedean transform, pages 42 and 43.** (A.14) and (A.15) (the Mellin transform of K_(1/3), from
int t^(mu-1) K_nu(t) dt = 2^(mu-2) Gamma((mu-nu)/2) Gamma((mu+nu)/2) with mu = 2s + 1). The phase
i conj(alpha(l)) |l|^-2s = 27^s conj(alpha(n)) conj(alpha(b))^3 N(n)^-s N(b)^-3s for l = lambda^-3 n b^3
(alpha(lambda^-3) = i). The constant 3^(5/2)/4 in (A.16): each mode contributes its coefficient times
i conj(alpha(l)) Gamma Gamma |l|^-2s/(4 (2 pi)^2s), and the coefficient at l = lambda^-3 n b^3 carries 3^(5/2),
consistent with the bound 3^(5/2)|b| printed for m = -3. The derivatives of (A.9) at z = 0 are as printed, so
the derivative in cusp coordinates is -(cv)^-2 d/dz' with no height term; (A.18) follows with
N(c)/c^2 = conj(alpha(c))^2, and (A.19) from (A.14), (A.15) with d/dz in place of d/dconj(z) (hence alpha(l),
not its conjugate; the constant 1/(4 (2 pi)^2s) recomputed). Inserting (A.19) at 1 - s into (A.18), dividing by
the gamma factors of (A.16) and putting t = 1/2 - s gives the quotient
Gamma(5/6 + t) Gamma(7/6 + t)/(Gamma(5/6 - t) Gamma(7/6 - t)), the factor ((2 pi)^4 x/27)^-t at
x = N(l) X/N(c)^2, the factor N(l)^-1/2, and the scalar 3^(-5/2) 3^(-3/2) = 1/81, so |C| <= 1/81. All of this
agrees with (6.5), (6.6) and (6.9) as printed on pages 23 and 24. The first pole of the numerator is at
t = -5/6, so the contour moves from Re t > 1/2 to Re t = 0 and, for (A.20), to Re t = -1/4 (factor x^(1/4)) or
Re t = A (factor x^-A) without crossing a pole. T(s, Psi) is entire because J(s) is: the constant modes are
removed by the horizontal derivative and the other modes decay exponentially at both ends. The polynomial bound
in the strip is by Phragmen-Lindelof, a standard step, read and not reworked.

**Lemma 6.3, page 43.** Every prime of k_0 has j_p = 1 and is active, so r = k_0 times a fixed product; fixing
k_0 mod M^2 fixes r mod M^2, hence H, c_0 and the residues in (A.11). The dependence of (d, psi, c_0) on k_0 is
as stated.

**What A.2 takes from elsewhere.** Kubota's cubic character and the automorphy law theta(g_1 w) =
kappa(g_1) theta(w) for g_1 = I mod 3 ([7, (5.4), (5.6)]); Patterson's cusp expansions (A.6) with the coefficient
bounds that give (6.10) and (6.11) of Lemma 6.4 ([38, Theorem 8.1, Table III]); formula (2.10); the
supplementary law that makes phi periodic mod L; the identification of the three cusp representatives with
[7, Section 5.1]. None of these was compared with its source here.

**Lemma B.1, page 44.** Fourier inversion in logarithmic coordinates and (1 - Laplacian)^(q/2) under the
integral; integrable against (1 + |t|)^J when q > J + d. Correct.

## Section 3 and the cited results

**Section 3 (Proposition 3.1 implies Theorem 1.1), pages 11 and 12.** Reworked by hand. chi_n(p^6) = 1 when p
does not divide n, so |A_1(D) - A_(p^6)(D)| << D/Y for N(p) in (Y/2, Y]; there are J of order Y/log Y such
primes and their sixth powers are distinct rows of norm at most Y^6 = H. Averaging,
|A_1|^2 <= (2/J) sum |A_(p^6)|^2 + O(D^2/Y^2) << D^(2+theta+eps)/Y + D^2/Y^2, and with Y = D^((1+theta)/6) the two
terms are D^(11/6 + 5 theta/6 + eps) and D^(5/3 - theta/3), so A_1(D) << D^(11/12 + 5 theta/12 + eps). The Mellin
step: with W(y) = y^-rho phi(y) the transform at rho is the integral of phi(y)/y, positive; M_W(s), the Mellin
transform of A_1(D) in D, equals W-hat(s)/L^S(s, nu) for Re s > 1 (substitute y = N(n)/D termwise) and is
holomorphic on Re s > 11/12 by (3.3), since A_1(D) = 0 for D < 1/2; the identity L^S M_W = W-hat continues, and
at a zero rho it reads 0 = W-hat(rho) > 0. The Dirichlet case is base change with L(1, chi_-3) != 0. Correct as
printed. Proposition 3.1 carries the whole content of the theorem; its proof is Sections 4 to 7. Section 2 is an
outline and proves nothing that is used.

**Patterson's formula (2.10) against Dunn-Radziwill (5.6), (5.7).** Their additive character is
e-breve(z) = exp(2 pi i (z + conj z)) and their normalised cubic Gauss sum is
g~(c) = |c|^-1 sum_(x mod c) (x/c)_3 e-breve(x/c) ((1.7) there). The theta function has constant term
3^(5/2)/2 v^(2/3) and coefficient tau(mu) = conj(g(1, c)) |d/c| 3^(n/2+5/2) at mu = +-lambda^(3n-3) c d^3
(n >= 0; c, d = 1 mod 3, c squarefree), with tau even. The preprint's character e(z) = exp(4 pi i Im z/sqrt 3)
is e-breve(z/lambda) (lambda = i sqrt 3), so the substitution x = lambda y gives
gamma_2(n) = chi_n(lambda)^2 g~(n), and the coefficient of the conjugate theta function at lambda^-3 n b^3 is
conj(tau) = 3^(5/2) |b| g~(n) = 3^(5/2) |b| conj(chi_n(lambda)^2) gamma_2(n). This is (2.10) as it reads on
page 6. The bounds for t_0 on page 40 (3^(k/2+2)|b| at m = 3k - 4, 3^(k/2+5/2)|b| at m = 3k - 3) are the sizes
in (5.7). Agrees.

**Kubota's character and the cusp expansions against Dunn-Radziwill Section 5.1 and Appendix A.** Their (5.4):
chi(gamma) = (c/a)_3 for gamma = I mod 3 with c != 0, theta automorphic on Gamma_2 = <SL_2(Z), Gamma_1(3)> with
multiplier chi, chi trivial on SL_2(Z). This is the law (A.8) uses, with kappa(g_1) = (c_1/a_1)_3, and the two
invariances the preprint states. Their coset representatives gamma_10 = (1 0; omega 1) and
gamma_19 = (1 0; omega^2 1), and the table on their page 78: d_10(mu) = omega tau_2(omega mu) e-breve(mu),
d_19(mu) = omega^2 tau_1(omega^2 mu) e-breve(mu). These are t_+ and t_- of (A.6). The coset of (1 0; x 1)
depends on x modulo Z + 3O only, three classes, so the matrices H of Appendix A.2 land on gamma_1, gamma_10 or
gamma_19 as the preprint says (lambda = -omega and -lambda = omega modulo Z + 3O; H = (u_0 -1; 1 0) is the
inversion followed by translation by u_0). tau_1 and tau_2 ((5.13), (5.14) there) are supported on units times
lambda^-4 c d^3 and have size 9|d|, which is the support (6.10) and the "at most 9|b|" of page 40. Agrees.

**The quadratic large sieve (Lemma 6.5) against Goldmakher-Louvel, Theorem 1.1.** Their theorem: for a
quadratic Hecke family {chi_a} with respect to an ideal c (primitive Hecke characters of trivial infinite type
indexed by squarefree ideals prime to c, with a reciprocity law chi_a(b) = chi_b(a) C([a], [b]) through a finite
group of classes, and chi_a chi_b primitive modulo ab for coprime a, b in one class), the mean square over
squarefree a of norm at most M of sums over squarefree b of norm at most N is << (MN)^eps (M + N) sum |lambda_b|^2.
The family of the preprint: x -> (x/k)_2 kappa_lambda(x)^(e_k), e_k = 1 when N(k) = 3 mod 4. Checked: (omega/k)_2 = 1
(omega is a square) and (-1/k)_2 = (-1)^((N(k)-1)/2), so the twist by the character modulo lambda, which is -1
at -1 and 1 at omega, makes it trivial on units; it is primitive of conductor k lambda^(e_k) for squarefree k
prime to 6; for k_1, k_2 in one class modulo 24 the exponents agree, the twists cancel and the product is
primitive modulo k_1 k_2; the reciprocity factor is a Hilbert symbol at 2 and depends on classes modulo 8. The
finitely many values of the S-part of n are handled by fixing it and splitting k into classes. The hypotheses
match and (6.13) follows.

## A caution about the text extraction

`pdftotext` drops every overline on this page. Read from paper_c.txt, the lemma has G(n) = chi_n(4) gamma_3(n)
and no conjugate on alpha in (4.4) and (4.5); in that form (4.2b), (4.4) and (4.5) hold for 81 of the 227 values
only (`nt01_check_asextracted.out`). The printed page has the bars, and with them every case passes. Any
identity in this paper that is checked from the text file has to be compared with the page first. The same
holds for square roots and hats: the text file has 1/N(m) for 1/sqrt(N(m)) in (4.8), M1 M2 for sqrt(M1 M2) in
(B.4), and "supp Phi" for the support of the transform in Proposition 4.5. In Section 6 it drops the bars in
(2.10), (6.2), (6.4) and (6.8) and the square roots in (6.9), (6.15) and (6.19).

The same holds on pages 30 to 37: the bars in (7.1), (7.3), (7.4) and in Appendix A.1 (G(n) = conj(chi_n(4))
gamma_3(n), gamma_1 gamma_2 = conj(chi_p(4)) gamma_3 gamma_2^3, G(a^-1) = chi_a(-1) conj(G(a))), the hats on Phi and
the square roots under N(p) are on the pages and missing from the text file.

In Appendix A.2 (pages 37 to 44) the bars over theta and its translates, over kappa(g_1) in (A.8), over z in
(A.9), over t_sigma(-l) in (A.7), over alpha in (A.16) and (A.18) and over kappa_0 in the scalar C, the hat on
phi, the breve on the additive character and the sharp on V are on the pages and missing from the text file.

## What this does and does not show

Every step the paper proves itself has now been read against the page and reworked: Section 3 (the mean-square
estimate implies the zero-free half-plane), Sections 4 to 7 (the mean-square estimate), Appendices A and B. No
error was found. The three results it takes from the literature were compared with their sources and are used
as stated there: Patterson's theta coefficients and cusp expansions in the form recorded by Dunn and Radziwill,
Kubota's automorphy law, and the Goldmakher-Louvel quadratic large sieve.

What this file does not do. Two steps inside the paper were tested or read instead of reworked: the Poisson
limit for (A.1) (tested on 564 moduli) and the Phragmen-Lindelof bound in Appendix A.2. Patterson's formulas
were compared with the transcription in Dunn and Radziwill, not with Patterson's 1977 paper. The proofs of the
cited results were not read. The 199-page preprint of 30 Sep 2026 was not read. And this is one reader's pass:
the places where a single pass is weakest are the uniformity claims (implied constants independent of the row,
the twist and the step of the recursion in Section 5, and the D^eps losses over the finitely many steps), which
were checked as printed but not stress-tested by an independent derivation.

A zero-free half-plane Re s > 11/12 for these L-functions is a result of the first rank, and a line-by-line
reading that finds no error is not a verification of it. The claim stays unconfirmed in this file until a
second, independent audit agrees.
