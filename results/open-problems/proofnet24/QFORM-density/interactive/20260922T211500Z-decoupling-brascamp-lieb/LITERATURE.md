# Literature for the bounded-density problem

Programme QFORM-DENSITY-3EIG-20260922. Tags: [V] read in the primary source; [S] from a secondary source
that quotes it; [I] derivation not found in the literature.

## Verdict

No paper, preprint or lecture note found states the problem (universal C, independent coordinates with
densities <= 1, at least three eigenvalues of modulus >= 1, sup_s P(|X^T A X - s| <= eps) linear in eps).
Neither a proof nor a counterexample was found. For a fixed number of variables and a smooth amplitude the
answer is classical: a nondegenerate quadratic form in k variables has oscillation index k/2, so the
pushforward density is bounded exactly when k >= 3. The conjecture asks for uniformity in n and over rough
product densities. Glazer and Mikulincer (arXiv:2108.04268, Sec. 1.3) name that gap: "it is still a
non-trivial task to obtain effective sublevel and Fourier estimates in terms of the lct, which are uniform
on reasonable complexity classes of mu" [V].

## Closest results

- Banks, Garza Vargas, Kulkarni, Srivastava, arXiv:2005.08930 (AIHP 60(4), 2024), Thm 2.1 [V]: for
  q = X^T Z Y + X^T U + V^T Y + W with X, Y independent random matrices (entries with densities <= K),
  delta_inf(q) <= (1+k^2)(C_RV^2 K^2 sqrt(2 e pi k) min_{j > k^2+k+1} 1/(sqrt(j-k+1) s_j(Z)))^{k^2}; the k = 1
  corollary gives delta_inf(q) <= 2 (C_RV K)^2 sqrt(2 e pi) min_{j >= 2} 1/(sqrt(j) prod_{i <= j} s_i(Z)^{1/j}).
  Mechanism: condition on Y, the form is linear in X (Rudelson-Vershynin), then a negative moment of a
  bounded-density marginal. For bipartite forms x_I^T Z x_J (+ linear) this settles the problem with an
  explicit constant [I]: density <= 4 sqrt(pi)/sqrt(s_1 s_2) <= 2 sqrt(pi). It says nothing when the diagonal
  blocks A_II, A_JJ are nonzero. The authors name the obstacle to their own strengthening: bounding the
  density of A y for a product vector y and an arbitrary matrix A [V].
- Rudelson-Vershynin, arXiv:1402.4492 (IMRN 2015) [V]: Thm 1.1 (d-dim projection density <= (CK)^d);
  Thm 1.2 (linear forms <= sqrt(2) K, via Rogozin and Ball); Lemma 3.1 (rearrangement of |phi_X|: <= 1 - c(t/K)^2
  for t < 2 pi K and <= sqrt(2 pi K/t) beyond); Prop 5.1 (leverages <= 1/2: Fourier inversion + Brascamp-Lieb);
  Sec. 6 (tensorisation removing large-leverage coordinates by conditioning).
- Livshyts-Paouris-Pivovarov, arXiv:1507.07949 [V]: sharp marginal densities of product measures,
  min((n/(n-k))^{(n-k)/2}, 2^{k/2}); 2 sqrt(2) for k = 3.
- Madiman-Melbourne-Xu, arXiv:1705.00642 [V]: Thm 1.4 (multidimensional Rogozin; for linear maps the centred
  cube is extremal); Thm 1.5 (extreme points: for coordinate-convex lower semicontinuous functionals the
  supremum over densities <= m is attained on indicators m 1_U). Applied to M(Q_# prod mu_i) this reduces
  the conjecture to laws uniform on sets of measure one [I].
- Rogozin, Teor. Veroyatnost. i Primenen. 32 (1987) [S]; Bobkov-Chistyakov, Zap. POMI 408 (2012) and
  J. Theoret. Probab. 28 (2015) [S].
- Gotze, Z. Wahrsch. 50 (1979); Bentkus-Gotze, PTRF 109 (1997), Lemma 5.1, symmetrisation inequality
  2|E e{tP(Z+U+V+W)}|^2 <= E e{2t<Q Z~, U~>} + E e{2t<Q Z~, V~>} [V, as restated in Gotze-Zaitsev].
  Gotze-Zaitsev, arXiv:1104.0519 (Ann. Probab. 42, 2014): rate O(N^{-1}) for d >= 5 (optimal, lattice
  points); these concern sums of i.i.d. vectors.
- Choudhary-Kuchibhotla, arXiv:2606.25441 (2026) [V]: Levy concentration of Gaussian quadratic forms; three
  nonzero eigenvalues give an integrable characteristic function; lambda_1 = -lambda_2 = 1 gives
  Q_S(eps) ~ eps ln(1/eps). Bobkov-Naumov-Ulyanov, arXiv:2012.10747 [V]: two-sided bounds for Gaussian
  quadratic forms. For Gaussian inputs with any means and variances >= 1/(2 pi) the conjecture holds with
  C = pi (Ostrowski, then the separable bound) [I].
- Quadratic Littlewood-Offord (discrete inputs): Costello-Tao-Vu (Duke 2006), Costello (Israel J. Math.
  2013), Nguyen (Duke 2012), Meka-Nguyen-Vu arXiv:1507.00829, Kwan-Sauermann arXiv:2312.13826 [V]: atoms of
  size ~ m^{-1/2}; decoupling in physical space loses a square root, Fourier-space decoupling does not.
- Polynomial anti-concentration: Carbery-Wright (MRL 2001), Glazer-Mikulincer arXiv:2108.04268,
  arXiv:2603.22664, Kosov arXiv:2511.02679, arXiv:2608.03922 [V]: eps^{1/2} for quadratics, or eps log(1/eps)
  for multi-affine quadratics with BV densities; none uses the spectrum.
- Oscillatory integrals with rough amplitudes: Phong-Stein-Sturm (Math. Ann. 2001); Gilula-Gressman-Xiao
  arXiv:1612.00050 [V]: "modulating each function f_j by e^{-i lambda phi_j(x_j)} ... terms which depend on
  only one coordinate function do not affect the norm", so pointwise-in-lambda bounds uniform over rough
  amplitudes see only the off-diagonal part of the phase.

## Consequences recorded [I]

- Lower bound for the constant: 3 sqrt(2) ~ 4.243 (rotated (1,1,-1) form, uniform inputs, central limit).
- The three-dimensional coarea inequality with only a bounded 3-D density is false (thin shell).
- Esseen: Q_Y(eps) <= (96/95)^2 max{eps, 1/a} integral_{-a}^{a} |phi_Y| (Petrov, Lemma 1.16) - an
  integrable characteristic function is sufficient for a linear rate, not necessary.

## Limits of the search

Google Scholar was unavailable; Rogozin 1987, Bobkov-Chistyakov and Ball were read through quotations in
RV15, LPP and MMX; talks and slides are poorly indexed, so "not found" is not "does not exist".
