# Row DG06 (the Carathéodory conjecture): the smooth counterexample checked

12 Nov 2026. Source read in full: arXiv 2610.34036v1 (N. Ando, M. Umehara, 25 Oct 2026, "A simple construction
of smooth counterexamples to the Loewner and Carathéodory conjectures"). The counterexamples were announced by
L. Alpöge (19 Aug 2026); Ando and Umehara give a shorter construction and state that their paper is
self-contained for the umbilic of index 2 and for the closed surface. Alpöge's own text was not read.

## The statements

- Loewner: an isolated umbilic of a surface in R^3 has index at most 1.
- Carathéodory: a closed convex surface in R^3 has at least two umbilics.

Both are refuted in the C-infinity category:

- for every k >= 1 the function H_k(z) = exp(-|z|^(-k/4)) F(z^(-k/2)), with
  F(x + iy) = a(x) - a(y) + sin x sin y and a(t) = sin^4 t + 3 sin^2 t, is smooth, flat at 0, and its Hessian
  eigenline field has an isolated singularity of index 1 + k/2 at 0 (Theorem 1.3);
- with f = exp(-delta (1 + |W|^2)^(1/4)) F(W), W the stereographic coordinate, the function
  rho = 1 + eps f / (1 + |W|^2) is, for small delta and eps, the support function of a strictly convex closed
  smooth surface whose only umbilic is the point at W = infinity, of index 2 (Theorem 2.2).

## What was checked by hand

1. Lemma 1.1. a''(t) = 6 - 16 sin^4 t, so 4 F_zz = 12 - 16 (sin^4 x + sin^4 y) - 2i cos x cos y. The imaginary
   part vanishes only where cos x = 0 or cos y = 0, and there the real part is at most -4. So F_zz has no zero.
2. Lemma 2.1 (formula (2.7) and the bounds on the cut-off): for small delta, |f_WW| >= (c/2) exp(-delta D^(1/4))
   on the whole plane, D = 1 + |W|^2, c = inf |F_zz|.
3. The identity rho_WW + (2 conj(W)/D) rho_W = eps f_WW / D, and that the left side is the umbilic criterion
   (Lemma 1.4: it is the trace-free part of the spherical Hessian of the support function in a conformal chart).
4. Theorem 2.2. f and all its derivatives decay faster than any power, so rho - 1 extends to the sphere and is
   flat at the pole; the surface is strictly convex for small eps; by 2 and 3 there is no umbilic at finite W;
   the pole is an umbilic because the surface agrees with the unit sphere to infinite order there; its index is 2
   because the indices sum to 2.

No step failed.

## What was checked numerically (dg06_check.py, dg06_index.py, dg06_index2.py and their .out files)

1. c = inf |F_zz| = 0.1761 (grid 1440 x 1440 on a period), sup |F| = 4.083, sup |F_W| = 2.950; delta = 0.03
   satisfies condition (2.3).
2. Lemma 2.1 with delta = 0.03, the second derivative taken symbolically from f itself and not from (2.7): the
   minimum of |f_WW| exp(delta D^(1/4)) over |X|, |Y| <= 45 (1.65 million points) is 0.1618, above c/2 = 0.0880.
3. Lemma 1.4 against the surface itself: the surface was built in R^3 from the support function (the
   1-homogeneous extension, Hessian by differences at 40 digits) and the difference and the sum of its principal
   radii of curvature agree with D^2 |rho_WW + (2 conj(W)/D) rho_W| and 2 rho + D^2 rho_{W conj(W)} to 19 digits,
   for the paper's rho and for an unrelated test function.
4. The identity of item 3 above at 40 random points: relative difference 8e-41.
5. Theorem 1.3. The winding number of (H_k)_zz around the origin, k = 1, 2, 3, 4, by two routes (differences at
   50 digits; a closed formula checked against them to 2e-14). On small circles (|z|^(-k/2) = 30, 400, 2000) the
   index is 1.5, 2.0, 2.5, 3.0, unchanged when the sampling is made five times denser. On larger circles it is
   different (for k = 1: 0.5 at |z| = 0.35, 2.5 at |z| = 0.11): H_k has further singular points at moderate
   distance from the origin, and the leading term takes over only once |z|^(-k/2) is large (about 50 for k = 1).
   This does not affect the theorem, which is local, but a plot at ordinary scale would not show the claimed index.

Not checked: strict convexity for a specific eps (the argument needs only that eps is small), and Alpöge's
original functions.

## Other literature

Two arXiv searches (lit/search/s1.xml, s2.xml) found no correction or reply. arXiv 0808.0851 (Guilfoyle,
Klingenberg, "Proof of the Carathéodory Conjecture", v4 of 2024) claims the conjecture for C^{3,alpha} surfaces;
that claim and a C-infinity counterexample cannot both hold, and the counterexample is a short explicit
construction which passed every check above. The real-analytic case is the subject of the classical proofs
(Hamburger 1940-41, with later versions by Bol, Klotz, Titus, and Ivanov 2002); these were not re-read here and
are quoted from memory. The new surfaces are not real-analytic and do not touch that case.

## Proposal for the row

The row as stated (smooth surfaces) is refuted. Replace it, or restate it to the real-analytic Loewner and
Carathéodory statements with the note that the literature treats them as proved by long arguments that few have
checked; as an open problem the row no longer belongs in a top-200 list.
