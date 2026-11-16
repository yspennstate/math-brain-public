# LO05: Hilbert's tenth problem over the rational numbers

Row LO05 of the top-200 general list (DESERVE.tsv line 568). Checked 12 Nov 2026 by an agent.

## Status

Claimed solved (negatively) by one preprint and not confirmed by anyone independent.

- OpenAI, "Hilbert's tenth problem over the rational numbers", 62 pages, in the public repository openai/math
  (commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a; folders dated 24 Sep and 6 Oct 2026). The two versions
  differ only in the date and in the dates of three cited OpenAI preprints. Theorem 1.1: no algorithm decides
  whether a polynomial with integer coefficients, in any number of variables, has a rational zero. Section 7
  adds Turing degree 0' and a quartic normal form.
- Z.-W. Sun, arXiv 2610.20691 (14 Oct 2026, 43 pages) takes "the height and Selmer-theoretic inputs" of the
  preprint as given and sharpens the statement to 86 unknowns. It restates the inputs precisely and reworks
  the reduction, so the reduction has had a second reader; the inputs themselves are used, not re-proved.
- No Lean formalization is listed for it in the repository's formalization index.
- Three dated arXiv searches (24, 40 and 6 entries; lit/search) show no other follow-up, confirmation or dispute.

The proof rests on two further OpenAI preprints from the same release, each a large claim in its own right:
"A pointwise 2-converse for elliptic curves with rational two-torsion" (used in Section 3) and
"Fontaine-Mazur modularity at the prime 2" (the odd regular case with no hypothesis on the residual image,
used in Section 4.7). Neither has been read here. The row cannot be more settled than those two.

Proposal for the list: keep LO05 as REPORTED_SOLVED, off the attack list, not marked solved.

## The argument

The proof does not define Z in Q by an existential formula and does not build a Diophantine model of the
integers, so it is not in conflict with the obstructions that Mazur's conjecture would give to those routes
(Cornelissen-Zahidi). For each polynomial f it produces a computable sequence of finite tests, each answered
by finitely many rational-solvability queries, with: f has an integer zero if and only if every test
succeeds. Given an oracle for rational solvability one searches for an integer zero and for a failing test
in parallel.

If all tests succeed, compactness gives a ring R with a zero a of f inside an elementary extension of Q.
The tests attach to each ring element a point T_a = eta(a) P of a fixed rank-one elliptic group
(E: y^2 = x^3 - d^2 x over Q(sqrt 2), d = 75 - 53 sqrt 2), additively and injectively. Two local comparisons
with truncated formal logarithms, on E and on its conjugate, show that at suitable primes a ring element
agrees with its index to high precision. The primes come from a height estimate (Theorem 2.4, proved in
Section 4): for a rational point s of the projective line away from five fixed points,
h(s) <= H M(s)^c, where M(s) is the product of the primes at which s meets one of the five points to odd
order. Its proof uses the Shimura curve of discriminant 210, whose quotient by its Atkin-Lehner involutions
is a line branched over five points, a family of abelian surfaces with quaternionic multiplication over it,
modularity of the attached two-dimensional representations with level bounded by a power of M(s), and height
bounds for modular Jacobians. With delta = f(eta(a)) nonzero, every contact prime divides delta to high
order, so all heights in R are bounded linearly in B = max |eta(a_j)|, while the canonical height of
eta(a_j) P grows like B^2. So the indices are ordinary integers and delta = 0.

## What was checked here (lo05_check.py, lo05_check.out)

Section 5 (Propositions 2.1 and 2.2) in full, by hand and by computer:

- d has norm 7 and is positive at both embeddings; w = -5 + 4 sqrt 2 = d (1 + sqrt 2)^3; w^3 - w = -8d;
  Q = (-dw, 2 sqrt 2 d^2) lies on E; x(Q) = -(1 + sqrt 2) times a square, so its class is outside
  {1, -1, d, -d}; -4 is not a square modulo 7. All exact.
- The descent: the image of alpha has order 8 (unit classes times {1, d}, reached by the torsion points and
  Q), the image of alpha' is trivial (valuations at the primes above 2 and 7, total positivity), and
  8 * 1 = 4 * 2^rank gives rank 1. Each step read and found correct, including the index formula (5.1)
  for a curve with full two-torsion.
- Independent of the paper: the point counts of E at 24 reductions at split primes have greatest common
  divisor 4, so the torsion of E(F) is exactly the two-torsion and Q has infinite order; 2Q computed and
  checked on the curve.
- Inequality (5.2), t - 1 - v_p(t) >= K for t > K and p > K + 1: 16.8 million cases, no failure.

Section 4.1, one consistency check: the Shimura curve of discriminant 210 has no elliptic points and genus 5,
and a genus-0 quotient by its 16 Atkin-Lehner involutions has exactly five branch points of index two. This
is the "five points" of the height estimate.

## Not checked

Sections 2, 3, 4 (after 4.1), 6 and 7, about 50 pages: the compactness reduction, the pole-parity
predicate, the height estimate (Faltings heights, the endomorphism dichotomy, the modular level bound),
the prime patterns. The two OpenAI preprints the proof depends on. Sun's paper beyond its introduction.

## What would upgrade the row

A reading of Section 4 by someone who works on effective Mordell through modularity, or independent
confirmation of the two cited preprints (the modularity statement at 2 above all), or a formalization.
