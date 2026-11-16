# LO05 companion [48]: Sections 4-5 (ring-class interpolation, switches, the missing vertex) read line by line (12 Nov 2026)

Source: lit/conv2/paper_c.txt, lines 939-2531 (text extraction of [48], "A pointwise 2-converse for elliptic curves
with rational two-torsion", OpenAI, 7 Oct 2026). Lost symbols and fraction bars were restored from the argument
and the restored forms are the ones checked. Kolyvagin [32], Howard [26], Nekovar [37], Milne [35], Cassels [9],
the open image theorem [42], Serre's CM image [41], Bogomolov [2] and Gross-Zagier in the split form [7] were
checked against the forms the paper quotes, not against the sources.

Outputs of these sections: Corollary 4.1, 2 j_h >= 4w(h) + s(h) + s(hk) - C(E, A) at every simple-zero ring
instance with omega(k) <= A; Theorem 4.2, for fixed K with corank Sel_2(E/K) = 1, binary families with simple
zeros and 2 j_hx - 4w(hx) - s(hx) - s(hxk) <= B at every nonzero address force ord_{s=1} L(E,s)L(E^(k),s) = 1.

| Part | Content | Check | Result |
|---|---|---|---|
| Lemma 4.3 | finite free models over an Artin local ring with a strong deformation retraction | flat = free (Nakayama with nilpotent m, Tor_1 vanishes); perturbation formulas with terminating geometric series | holds |
| Lemma 4.4 | ultrafilter limits of bounded diagrams | entries at precision j lie in the finite ring A_j, limits compatible in j, identities polynomial; inner rank bound from K(E[2]), S-units, Cl[2] and the Euler characteristic of a totally imaginary field | holds |
| Lemma 4.5 | integral Kummer local condition, self-orthogonal | derived reduction gives B(F)[2^n] and B(F)/2^n; Hom(M[-1] (x)^L M[-1], Z2[-2]) = Hom(M (x) M, Z2) because the Tor term sits in degree one; the quasi-isomorphism checked mod 2 by Tate duality, derived Nakayama | holds |
| Prop 4.6 | ring-class characters of 2-power order with prescribed values and the trace bound (4.8) | v_pj(alpha/alpha-bar) = m_j(a) since conjugate pairs are disjoint, so the prescriptions (4.9) respect every Kummer relation; split ring-class sequence with kernel F_r^*; the commutators of the Tate image over K(mu_2^inf) act trivially on the abelian radical extension, so each prescribed coset contains a translate of a fixed open subgroup; CM case through sigma with chi_cyc = 625 in 1 + 16 Z2 and the power 624; n_i >= 2i gives (1+t)^(2^n_i) = 1 in A_i | holds |
| Lemma 4.7 | local acyclicity at the height-one tests | r-inertia minus one is t times a unit; active odd primes give -2; at split prescribed primes det(zB - 1) is a nonzero polynomial in z = (1+t)^a, which is transcendental over F2 | holds |
| Lemma 4.8 | residual sizes bounded independently of the active support | active singular complexes acyclic after inverting t; semicontinuity from t = 0; Schreier bound for the index-two subgroup | holds |
| Lemma 4.9 | evaluation on every sequence; injectivity on H1 and H0 | one ultrafilter for all evaluation matrices, no diagonal selection; a detecting list of length at most dim H1 + 2; the cone starts in degree one after any base change; no H0 by absolute irreducibility | holds |
| Lemma 4.10 | restriction to the exact common kernel is injective | z = g^2 (tau g^2 tau^-1) is ring-class trivial by the dihedral action and acts by u^4; (u^4 - 1) b(g) = (g - 1) b(z); in characteristic two the r-inertia element acts by 1 + t | holds |
| Prop 4.11 | outer limit | the ultraproduct of the O_j modulo infinitesimals is a DVR with uniformizer 2 and characteristic-zero fraction field; integral degree-two matrices handle approximate cycles | holds |
| Lemma 4.12 | absolute irreducibility on the tests | Mackey with r-inertia separating chi and chi^-1; finitely many closed subgroups of index at most two in a compact 2-adic analytic group; (1+t)^n - 1 is a unit of O_j | holds |
| Lemma 4.13 | Chebotarev realization of exact-kernel evaluations | inert derivative primes with Frobenius tau u; b((tau u)^2) = (1 + tau) b(u) re-derived; a_l = 0, l = -1 in the limit | holds |
| Lemma 5.1 | split local model at a derivative prime | Fox resolution of <sigma, tau : sigma tau sigma^-1 = tau^q>: d1 = (0, 1 - q), pure-tame square coefficient binom(q, 2), both 0 mod 2^a when q = 1 mod 2^(a+1); (x, x) = (x, -1) with -1 a 2^a-th power; cross pairing (5.5) | holds |
| Lemma 5.2 | Kolyvagin derivative classes at 2 with one multiplier L | (sigma - 1)D = (l + 1) - sum sigma^i; uniform torsion bound from a central scalar; descent factor 2^(2e) once; f = (F^2 - 1)Q = (aF - (l+1))Q and s = (a - (l+1)F)Q; (F - a)(aF - (l+1)) = a - (l+1)F re-derived, so s = (F - a)f, which is Jf in the limit; the new finite coordinate vanishes since l(l+1)/2 is divisible by 2^a when v2(l + 1) >= a + 1 | holds |
| Lemma 5.3 | exact determinant switch over a DVR, v(u_F) = v(u_S) | the relaxed image is a Lagrangian containing (v0, 0) and (0, Jv0); the boundary is x -> <x, v0> B^*; the volume of v0 ^ x is a unit because the Weil form is unimodular | holds |
| Lemma 5.4 | a rank-two evaluation exists | Goursat with End_G(W) = F_O; polarization Q(sum a_i u_i) = sum a_i^2 Q(u_i) + sum a_i a_j B(u_i, u_j), valid in characteristic two, over an infinite field | holds |
| Prop 5.5 | coordinates in Lambda[1/2] | at each height-one p != (2): a rank-two switch lowers the fiber Selmer dimension by two (the relaxed image equals the finite plane); single-sign case by a rank-one switch first; at fiber dimension one the coordinate is integral; Lambda normal | holds |
| Lemma 5.6 | terminal minor estimate v(u) >= -a - b | u = (zeta lambda)/det A after triangular basis changes of determinant one (the extraction drops the fraction bar; the reading with the division is the one consistent with the paper's convention that degree-two torsion lowers the coordinate) | holds |
| Prop 5.7 | v_(2)(u) >= -C(E, A) | an unbounded loss gives an outer DVR on which rank reduction runs to rank one; a nonzero terminal minor has one finite valuation on an ultrafilter-large set; Lemma 5.6 contradicts | holds |
| Lemma 5.8 | derived specialization at constant rational rank | 0 -> H^i/t -> H^i(C0) -> H^(i+1)[t] -> 0; a nonunit pivot over Q2[[t]] would add central cohomology | holds |
| Lemma 5.9 | ramified good odd place | inertia acts by -1: H^1(I) = T/2T; H^1(F_v) = E[2]^Fr, H^2 = E[2]/(Fr - 1), equal dimensions | holds |
| Prop 5.10 | v(u_h(0)) = 2 j_h - s(h) - s(hk) - 4w(h) + O_{E,A}(1) | split distribution relation gives m = a_r - 2 chi_h(r) with v2(m) <= c_E; each active prime has two places of length t_p; the Cassels-Tate isogeny identity for Res_{K/Q} E^(h) and E^(h) x E^(hk): component factors agree at split primes and differ by 2^(t_p) at p dividing k (type I0*), giving (5.24) | holds |
| Cor 4.1 | the uniform lower bound | Props 5.5 and 5.7 give 2^C u_h in Lambda; constant coefficient and (5.22) | holds |
| Lemma 5.11 | removing unused primes in O[G] | (1 + a z + z^2)(1 + a z^-1 + z^-2) = (a + z + z^-1)^2 mod 2 re-derived, so l_q/e_q^2 = 1 mod 2 and the factor (5.27) is integral, equal to l_q/e_q^2 at unused characters and 1 at active ones | holds |
| Lemma 5.12 | Laurent expansion with poles below t^(-Mh) | O/2^M = (Z/2^M)((t)); B^-1 by the finite series (5.29) | holds |
| Lemma 5.13 | clearing a bounded complex, f u = d with v(f_0(0)) bounded | f = 2^a0 P^2, d = PQ; on a constituent where a pivot vanishes both sides are 0 | holds |
| Prop 5.14, 5.15 | the clearing factor independent of b and #Q | the new singular blocks are eliminated over O[G] (unit determinants, residual t-order at most four); central torsion bounded by the finite quotient of the fixed base Selmer group | holds |
| Lemma 5.16 | a nonzero address with prescribed coefficient bits | coefficient extraction commutes with character evaluation; Lemma 3.4 | holds |
| Lemma 5.17 | v(u_x(0) - u_0(0)) >= M - 2c | at the solution v_O(f_x) <= c, so u_x and u_0 have coefficients in 2^-c Z2; the constant term of d_x is the convolution, every term with a negative coefficient of f_x is 0 mod 2^(M-c); divide by f_0(0); L(M) + 2 tested coefficients | holds |
| Thm 4.2 | the missing vertex | if the base derivative vanished, Gross-Zagier makes the Heegner sum torsion and u_0(0) = 0; then v(u_x(0)) >= M - 2c > B1 at some x != 0, against Prop 5.10; the split Heegner sign is odd, so the order is exactly one | holds |

Remarks. Two readings depend on restored symbols: in Lemma 5.6 the coordinate is a quotient by det A, and in
Lemma 5.17 the inequality at the chosen address is v_O(f_x) <= c; both are forced by the steps that use them.
The proofs of Lemmas 5.13 and 5.14 describe the pivot cancellation over O[G] in words rather than in formulas;
the counting (at most r0 pivots, numerators of bounded degree, central valuation bounded by r0 and h1) is
consistent, and the identity f_x u_x = d_x was checked on the three kinds of constituent.

What this changes: with Sections 1-5 read, both outputs that [48]'s Theorem 1.1 draws from the cyclotomic and
ring-class arguments (Theorems 3.2 and 4.2, Corollary 4.1) show no gap on a first independent read. Sections 6-9
(auxiliary twists, coefficient systems, arithmetic graphs, assembly) build the families these theorems need and
are still unread, as is the second companion [49]. LO05 stays REPORTED_SOLVED.
