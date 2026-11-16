# LO05 companion [48]: Sections 6-9 (auxiliary twists, coefficient systems, arithmetic graphs, assembly) read line by line (12 Nov 2026)

Source: lit/conv2/paper_c.txt, lines 2532-5566 (text extraction of [48], "A pointwise 2-converse for elliptic curves
with rational two-torsion", OpenAI, 7 Oct 2026). Lost symbols were restored from the argument; the restored forms
are the ones checked. Heath-Brown's quadratic large sieve, Soundararajan's Gauss-sum evaluation, Waldspurger,
Shimura, Gross's ternary lift, the linear sieve (Friedlander-Iwaniec Thm 11.13), the ray-class prime ideal theorem
and the explicit Gross-Zagier ratio of Cai-Shu-Tian [7] were checked against the forms the paper quotes, not
against the sources.

Outputs: Proposition 9.6/9.7 (corank 0, the even original base), Proposition 9.10 (the arithmetic premise of
Corollary 4.1 and Theorem 4.2), Proposition 9.14 (corank 1, the odd original base) and the proof of Theorem 1.1.

| Part | Content | Check | Result |
|---|---|---|---|
| 6 | auxiliary twists with nonzero central value and bounded prime count | approximate functional equation; Heath-Brown large sieve; Poisson identity (6.4) with its CRT factor; H_p and the even part (1 - x^2) L_p(sym^2); gamma_p = 1/(1 + p F_p^ev); the Gauss-sum table; the q-truncation range q >~ X^(1-eps)/(HJ); Waldspurger and the linear sieve step | holds |
| 7.1-7.3 | Shimura and Waldspurger relations; Lemma 7.2 (Kummer detection); Lemma 7.3 (Gross ternary lift) | chi = B chi_h, psi = B(|h|/.), chi/psi = (-1/.); eigenline count 1 + (-n/p); orbit count 2^omega(N) | holds |
| 7.4 | Lemma 7.6 and the trace and inertia identities (7.14), (7.15) | c_p(D) = (a_p - eps(-D/p) - 1)/2 = Delta_0/2; Delta_1 - Delta_0 = 0 mod 4 | holds |
| 7.5 | Prop 7.9, contraction | d_p A = A(D0); the item-4 residues are #E(F_q)/2 mod 2 | holds |
| 8 | Lemma 8.1 (realization), Lemma 8.4 (cycles vanish), (8.2) matrix-tree, Lemma 8.6, Thm 8.3 | ray-class prime ideal theorem; Cauchy-Binet; the F2 example recomputed (Q = [[0,0,0],[0,1,1],[0,1,0]], h = (0,0,1), c = (1,0,1), adj Q = E11); program 1 radical r = sum u_i with adj = r r^t; program 2 forces H = [[0,T],[T^t,B]] and the entry ((T_J^-1)_b1)^2; cost D = sum (d_x + e_x) | holds |
| Prop 9.1 | interfaces with Thm 3.2, Cor 4.1 (9.1) and Thm 4.2 | statements match the earlier sections | holds |
| Lemma 9.2, (9.6) | isogeny orientation; a good simple prime has #E(F_p) = 2 mod 4 | order-4 point and the isogeny image re-derived | holds |
| Lemmas 9.3-9.5 | stabilization of r(s); finite bookkeeping | a nonincreasing integer sequence stabilizes | holds |
| Props 9.6, 9.7 | the even estimate and the even original base | Thm 8.3 plus cyclotomic transfer (Thm 3.2) | holds |
| Lemma 9.8 | root-number flip | chi_k(-1) chi_k(N) = -1; Prop 6.2 completion with bounded R | holds |
| Lemma 9.9 | 2 j_h(k) - 2 j(P_h) = v(L(hk)) + O(1) | the Cai-Shu-Tian ratio as quoted | holds |
| Prop 9.10 | 2 j(P_h) >= 2w(h) + s(h) - 2w(k) - C, with w(k) <= omega(k) <= A | re-derived; uses only even symbols, Cor 4.1 and Gross-Zagier, not the odd normalization of 9.5, so it is not circular | holds |
| 9.5, Lemma 9.11 | ultrafilter stabilization of label tables; recurrence congruences | b_s = p^s mod 2^m checked | holds |
| Lemma 9.12 | a nonempty K-split witness for rational E[2] | extra depth (9.13), (9.14); (9.15) a_p(E^(k)) = p + 1 mod 8 from H_p[p^3] = (a - 1)(a - p - 1) times a unit with a even; the division (9.16) and integrality (9.17), including the case J = U; the two fresh traces raise the valuation in both inert-count cases; witness: p inert in K and trivial on E[8] gives p = 1 mod 8, a_p(E^(k)) = -a_p(E) = -2 mod 8, so (a_p - 1 - p)/4 is odd; t(u^2) = t(u)^2 mod 2 for a 2-dimensional trace | holds |
| Lemma 9.13 | orientation correction | G_Q = G_K u G_K c; a c-invariant quadratic character of G_K extends unramified off S0; the annihilator of the c-invariants is the image of 1 + c (1 + c is self-adjoint); flips change the total by (1 + c)v | holds |
| Prop 9.14 | s2(E) = 1 gives a(E) = 1 | companion k with L(E^(k), 1) != 0 fixed before the cube dimension; K = Q(sqrt k) freshly ramified, so independent of the old label fields; quadratic and full two-torsion cases build terminal packets with both polynomials nonzero; Thm 8.3 networks at every nonzero address; at the addresses ord E^(h) = 1 and ord E^(hk) = 0 with 2 j_h(k) <= 4w(h) + C; at address zero s2(E^(k)) = 0, so s2(E/K) = 1 by Lemma 2.2; Thm 4.2 gives a simple zero of L(E,s)L(E^(k),s), and the second factor is nonzero | holds |
| Thm 1.1 | assembly | corank 0 by Props 9.6-9.7; Prop 9.10 before the odd normalization; corank 1 by Prop 9.14; Gross-Zagier-Kolyvagin gives r = a and Sha finite; (9.5) keeps the Selmer corank hypothesis throughout | holds |

Remarks. Six readings depend on restored symbols, each forced by the step that uses it: the q-truncation range in
Section 6; "nu^2 is a nonsquare" and "L(E^(h), 1) != 0" in Lemma 7.3; the form of (7.12); the block order of
(8.3)/(8.4); the factorization in (9.15), which the extraction prints as (a - 1)(a - 4p - 1); and "!=" in
"an even unit gives L(h) != 0" (Prop 9.1) and "L(E^(k), 1) != 0" (Prop 9.14), where the extraction prints "=".
Prop 9.14 also needs the upper bound 2 j_h(k) <= 4w(h) + C, whose inequality sign is lost; it is the direction
Theorem 4.2 requires.

What this changes: all nine sections of [48] have had one independent read with no gap, so the companion LO05's
Lemma 3.4 uses (Theorem 1.1 of [48], Selmer corank at most one) is checked on that read. The second companion [49]
is unread and the second independent audit of LO05 has not been done. LO05 stays REPORTED_SOLVED.
