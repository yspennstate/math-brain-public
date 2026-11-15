# Row IT01 (the MDS conjecture): the even-characteristic preprint, its last section checked

12 Nov 2026. Source read: arXiv 2610.28208v1 (Bocong Chen, Jing Huang, 20 Oct 2026), "On the MDS conjecture in even
characteristic", 33 pages. Read from the text: the introduction, the setting of Section 2, the statements of
Sections 3 and 4, and Section 5 in full. One version on arXiv; the search of 12 Nov (lit/search/s1.xml, phrase
"MDS conjecture", newest first) shows no comment, correction or follow-up.

## The claim

Theorem 1.1: a nontrivial linear [n, k] MDS code over F_q, q even, has n <= q + 1, except n <= q + 2 for k = 3 and
k = q - 1. With Ball's theorem for prime q this leaves odd non-prime q as the open part of the linear MDS conjecture
(Ball and De Beule give k <= 2p - 2; arXiv 2610.03740 reports a range of k linear in q for each fixed odd p).

The introduction names a second, independent report of the same theorem: P. Kumar, "The MDS conjecture over finite
fields of even order", report and Lean formalization, Palomar record PALOMAR-2026-10-15-000014 (15 Oct 2026). It is
not on arXiv and was not read here. The authors say both arguments use the same mechanism (a Frobenius derivation,
a colon ideal in three variables, unimodality of a Gorenstein Hilbert function).

## How the proof is put together

Everything reduces to Lemma 5.4: for q even and 4 <= k <= q - 2 there is no [q + 2, k] MDS code. By duality
k <= m + 1 with m = q/2; put h = k - 3, so 1 <= h <= m - 2.

1. Lemma 2.1 (quoted from Ball and Lavrauw 2019, Theorem 13.1): the tangent polynomial of the arc, of degree h.
2. Sections 3 and 4: for a fixed set L0 of h coordinates and each further coordinate a, a subcode D_a of the dual
   code vanishing on L0, built by Reed-Solomon interpolation. Inclusion (9): every D_a lies in the dual code
   shortened at L0, which has dimension q - 2h - 1.
3. Proposition 4.6: the orthogonal complement of the sum of the D_a, inside F_q^(q+2-h), has dimension at most
   3 + kappa, where kappa = dim {T of degree h - 2 : J T in (X1^m, X2^m, X3^m)} and J is the product of the
   q + 2 - h linear forms of the arc projected to a plane.
4. Lemma 5.1: J Q in (X1^m, X2^m, X3^m) with deg Q <= h - 3 forces Q = 0.
5. Proposition 5.2: kappa <= h - 1, from Lemma 5.1 and the fact that F_q[X1, X2, X3]/((X1^m, X2^m, X3^m) : J) is
   Gorenstein of socle degree m + h - 5 with unimodal Hilbert function (Lemma 2.2, cited to Stanley 1978 and
   Zanello 2006).
6. Count: the sum of the D_a has dimension at least (q + 2 - h) - (h + 2) = q - 2h, one more than q - 2h - 1.

## What was checked here

By hand, Section 5 line by line. The degrees in Lemma 5.1 are right (d = m + 2 - h + r <= m - 1 and
deg K = q + 5 - 2h + 2r <= q - 1 for r <= h - 3); the identity delta K = (J Q)^2 holds in characteristic two with
q = 2m; the vanishing of A_i on each line needs d < q + 1 - h, true for h <= m + 1; the socle degree, the perfect
pairing, the inequality h - 2 <= s/2 (equivalent to h <= m - 1) and the binomial difference C(h,2) - C(h-1,2) = h - 1
are right; so are the final count and the three boundary cases in the proof of Theorem 1.1.

By computation (it01_check.py, output it01_check.out, 13 seconds; it01_arcs_side.py for the arcs). Lemma 5.1 and
Proposition 5.2 are statements about real planar arcs of size q + 2 - h, so they can be tested although the code of
Lemma 5.4 does not exist. The program builds J over F_8, F_16, F_32 and computes the graded pieces of the colon ideal
by linear algebra over the field, for h = 1, ..., m - 1:
- sub-families of the conic with its nucleus (q = 8, 16, 32) and of the translation hyperoval (1, t, t^4) (q = 32),
  the first q + 2 - h points and a random choice;
- arcs grown point by point in random order (q = 8 and 16; complete arcs of sizes 6 and 10, and 10, 11, 12 and 18
  came out; at q = 32 none reached the 19 points needed). The arc test was repeated a second way, by counting
  points on every line of the plane.

Result: in all 90 cases the colon ideal is zero in degrees up to h - 3 and kappa <= h - 1. In 38 of them kappa
equals h - 1 (mostly the conic families), so the bound of Proposition 5.2 is attained and cannot be improved. For
q = 8 and 16 the whole Hilbert function was computed: symmetric and unimodal in every case, as the Gorenstein
statement requires.

Controls. With every line through one point (a pencil) the colon ideal is nonzero in the degrees where Lemma 5.1
forbids it, so the program detects a failure. With a single concurrent triple put into a conic family nothing
fails: the test does not show that the hypothesis "no three concurrent" is needed in full.

## What was not checked

- Sections 3 and 4: the construction of the D_a, inclusion (9) and Proposition 4.6. The margin of the whole proof
  is one dimension and the bound kappa <= h - 1 is attained on real arcs, so the proof stands only if 3 + kappa in
  Proposition 4.6 and the inclusion (9) are exact as stated. These objects exist only for a hypothetical
  [q + 2, k] code and cannot be instantiated.
- Lemma 2.1 as specialised from Ball and Lavrauw, Theorem 13.1.
- That the unimodality theorem behind Lemma 2.2 is available over a field of characteristic two in the form used
  (the paper applies it over F_q). The computed Hilbert functions agree with it in every case tried.
- Kumar's report and its Lean development.

## Proposal for the row

Even characteristic: reported proved in October 2026 by two independent reports, one with a Lean formalization;
the final section of the arXiv proof checks out by hand and on computed examples, the reduction in Sections 3 and 4
is unread. Restate the row to the remaining case: for q = p^e with p odd and e >= 2, a linear [n, k] MDS code with
2 <= k <= q - 1 has n <= q + 1 (known for k <= 2p - 2 and in the ranges coming from planar arcs).
