# LO05 companion [48]: Sections 1-3 of the pointwise 2-converse read line by line (12 Nov 2026)

Source: lit/conv2/paper_c.txt, lines 51-938, a text extraction of "A pointwise 2-converse for elliptic curves
with rational two-torsion" (OpenAI, 7 Oct 2026), the companion that LO05 cites as [48]. The extraction loses
the symbols for "not equal", "in", "at most" and most subscripts; each was restored from the surrounding
argument, and the restored forms are the ones checked. Each step below was re-derived by hand. Kato [29],
Nekovar [37], the open image theorem [42] and the CM input [6] were checked against the forms the paper
quotes, not against the sources.

Theorem 1.1 of [48]: if E(Q)[2] is nonzero and s2(E) is 0 or 1, then the analytic rank and the rank both
equal s2(E) and Sha(E/Q) is finite. Sections 1-3 give the corank-0 case (Theorems 3.1 and 3.2); the corank-1
case runs through Sections 4-9.

| Part | Content | Check | Result |
|---|---|---|---|
| 1 | plan: integral cyclotomic interpolation over a binary cube of quadratic twists, the missing vertex recovered from valuation bounds at the nonzero addresses | matches the statements of Sections 3-9 | holds |
| Lemma 2.1 | s2 = rank + corank Sha[2^inf]; Gross-Zagier-Kolyvagin for analytic order at most 1 | Kummer sequences | holds |
| Lemma 2.2 | Monsky 2-parity, isogeny invariance, s2(A/K) = s2(A) + s2(A^(k)) | restriction-corestriction, rational coefficients | holds |
| 2, conventions | t_p in {1, 2}; s(h) finite when s2 = 0 | a rational 2-torsion point is fixed by Frobenius | holds |
| Lemma 3.3 | O cap Lambda[1/2] = Lambda | an element of Lambda[1/2] integral at (2) has no power of 2 in its denominator | holds |
| Lemma 3.4 | b > r(2^M - 1) gives x != 0 with (z_j)_x = (z_j)_0 mod 2^M | z(x) = a + sum 2^|I| a_I x^I; digit j is the coefficient of Y^(2^j) in (1+Y)^z, and (1+Y)^(2^k a) = (1+Y^(2^k))^a over F2, so digit j has degree at most 2^j in x; M digits give 2^M - 1, r families r(2^M - 1) < b; Chevalley-Warning parity, and 0 is a common zero | holds |
| Lemma 3.5 | the positive complex is perfect and commutes with base change; the real-place class a | acyclic disks cancelled over Artin quotients and lifted; H^0(G_S, V) = 0 makes the connecting map from the real invariant line injective rationally; H^1(R, T) is killed by 2 | holds |
| Lemma 3.6 | the positive complex over O[G] is O[G]^2[-1] | for the trivial residual piece over the layer K_n of degree d_n = 2^n: H^0 injects, H^1 has dimension d_n - 1 + s_n + c_n = d_n + O(1) (signatures surjective since the norm of zeta + zeta^-1 is -1, and a vector of odd augmentation is a unit of the local group algebra), H^2 is bounded, higher degrees vanish; over F2[[t]] modulo t^(2^n) a free rank r term gives r 2^n + O(1), so rank one in degree one only; E[2] has two trivial factors; a minimal complex over the local ring has zero residual differentials | holds |
| 3.3, (3.2) | fixed-form Kato classes and the coefficient map | (3.2) is a ring homomorphism on integral coefficients, with no division by the order of G | holds |
| 3.3, (3.3) | unsmoothing | c = 1 mod 3 N_odd m and c = 1 + 2^e mod 2^(e+1) give v2(gamma(c)) = e - 2, so 1 - (1+t)^gamma(c) is nonzero in F2((t)) and the factor is a unit of O[G]; its central value c(c - 1) has valuation exactly e | holds |
| (3.4) | central reciprocity | at a good unused prime the omitted Euler factor times q is #E^(h)(F_q) | holds |
| 3.4, (3.5)-(3.7) | local cones and their determinants | D_q nonzero, so H^1(Q_q) = 0 and length H^2(Q_q)_p = v_p(D_q); at a good active prime inertia acts by -1 and W_q = 0; at a bad prime the correct module is H^1(I_q, V_h) (split multiplicative: Q_2(-1), determinant 1 - phi/q, nonzero central value); D_q(0) != 0 in general since H^2(Q_q, V_h) = H^0(Q_q, V_h)^* = 0 | holds |
| (3.8) | comparison with the Kato zeta line | the difference of the two Lambda-elements vanishes at infinitely many finite-order characters, so it is zero by Weierstrass preparation; c_h need not be uniformly bounded, but it is a unit of A | holds |
| (3.9), (3.10) | divisibility at height-one primes; Euler conventions | enlarging S adds at most sum v_p(D_q) to H^2 and multiplying by prod D_q adds exactly that to the index; the local factor at 2 has no factor t since H^2(Q_2, V_h) = 0; P_q(Z) - Z^2 P_q(1/Z) = ((q-1)/q)(1 - Z^2), so the ratio r_q is 1 mod 2 and U_q = 1 + ((r_q - 1)/2)(1 + g_q) is a unit of O[G], equal to 1 at active characters and r_q at unused ones, with unused central value 1 | holds |
| (3.11), (3.12) | u_x in Lambda[1/2], and 2^C_int u in Lambda[G] with C_int independent of S, h0, G, b | Lambda is normal, so no pole away from (2) puts u_x in Lambda[1/2]; Fourier inversion over Lambda[1/2][G] divides only by powers of 2; Lemma 3.6 and the integral trace give 2^C_int u in O[G]; Lemma 3.3 coefficientwise | holds |
| Prop 3.7 | v2(u_x(0)) - D(h_x) bounded by C_loc when s2 = 0 and L(E(h_x), 1) != 0; u_x(0) = 0 when the central value is 0 | (3.14) from Poitou-Tate with Kummer conditions; the index i of the global image in L_2 appears twice and cancels; unused prime terms v2(#E(F_q)) cancel those of (3.4); active primes give 2w(h_x); zero central value puts the class in the finite Selmer group, which is 0 rationally | holds |
| Thm 3.1 | v2(L(h)) >= 2w(h) + s(h) - C_E | (3.12) gives v2(u_h(0)) >= -C_int, then Prop 3.7 | holds |
| Thm 3.2 | D(h_x) <= B for x != 0 gives L(E(h0), 1) != 0 and D(h0) <= B + C_E | take M - C_int > B + C_loc; Lemma 3.4 on the constant coefficient of 2^C_int u in Z2[G] gives x != 0 with v2(u_x(0) - u_0(0)) >= M - C_int; if u_0(0) were 0 or of valuation above B + C_loc, then v2(u_x(0)) > B + C_loc, against Prop 3.7 at x | holds |

Remarks. The sign convention for torsion in the inverse determinant (degree-two torsion subtracts its length)
was checked on the paper's own example [Z2 -> Z2, multiplication by 2^a] only; it is the direction that makes
Theorem 3.1 the expected lower bound (Sha and Tamagawa factors divide the central value), and the opposite sign
would make it vacuous. No constant in Sections 1-3 grows with b, with the number of auxiliary primes or with the
prime count of h0: every constant comes from the fixed form, the fixed real period line or the finite set of
local twists at 2N.

What this changes: LO05's Lemma 3.4 applies Theorem 1.1 of [48] with Selmer corank at most one, so it needs
both halves (corank 1 when r = 1; corank 0 when r = 0 and dim Sha[2] = 1). The corank-0 half shows no gap on a
first independent read. Sections 4-9 (ring-class interpolation, the corank-1 case) and the second companion [49]
are still unread, so LO05 stays REPORTED_SOLVED.
