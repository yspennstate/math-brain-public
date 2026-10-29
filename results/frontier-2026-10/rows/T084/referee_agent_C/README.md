# T084 referee check (agent C, 17 October 2026)

Independent check of claims C1-C4 in `../reviews_agent_B/`. These scripts were written before the
reviewed code was read.

Model: random-cluster weight lam^|A| q^k(A) on K_n, u = 1 - q. For two edges e, f,
N = Z_e Z_f - Z Z_ef and Cov(X_e, X_f) = -N / Z^2.

| file | what it does |
|---|---|
| `brute.py` | enumerates every edge subset of K_n (union-find for k(A)) and returns N as {(lam power, u power): coeff} |
| `rec.py` | a recursion over connected-cluster weights with up to four marked vertices and the marked edges deleted; N by inclusion-exclusion on the deletions; `bern(N)` gives the Bernstein coefficients of N/u on [0,1]. `python rec.py adj|dis nlo nhi` |
| `c4.py` | the u^1 coefficient identity on 60 random graphs (seed 84, n = 4..7, up to 15 edges) |
| `run_ext.py` | the Bernstein check for n = 31..40 |
| `VERDICT.md` | the verdict sent to the row's lead, and the structure notes |

Results:
- `brute.py` and `rec.py` agree term by term (adjacent n = 3..6, disjoint n = 4..6), and `rec.py` equals
  `kn_poly_adjacent.numerator` / `kn_poly_disjoint.numerator` term by term for n = 3..11 / 4..11.
- The Bernstein coefficients of N/u at degree d = 2n-3 (adjacent) and 2n-4 (disjoint) have no negative
  lam-coefficient for n = 3..30 (adjacent) and 4..30 (disjoint); n = 31..40 in `ext_31_40.txt`. b_0 is nonzero
  and b_{d-1} = b_d = 0, which is forced: every Z carries a factor q, so q^2 divides N.
- The u^1 identity holds on all 60 random graphs. It also has a short proof: expand q^k = 1 - k u + O(u^2); the
  u^1 coefficient is lam^2 (1+lam)^(m-2) sum_B lam^|B| [k(B) - k(B+e) - k(B+f) + k(B+e+f)], which is
  nonnegative because graphic rank is submodular.

This is a finite computation. It does not prove the statement for every n.

## D1-D3 (17-18 October)

| file | what it does |
|---|---|
| `d1check.py` | D1: N equals the swap sum over pairs (A without e, B with e and f), each pair weighted lam^(|A|+|B|) q^(k(A)+k(B)) (q^(d2-d1) - 1); checked against `brute.py` |
| `d3.py` | D3: per lam power, the q-series coefficients of N/u^2 = a_1/(1-q) + sum_{k>=2} a_k (1-q)^(k-2) are nonnegative. `python d3.py kn adj|dis nlo nhi` or `python d3.py rand seed count` |
| `d3_six.py` | D3 on every graph on 6 vertices up to isomorphism, every edge pair |
| `d3_seven.py` | D3 on every graph on 7 vertices with at most 13 edges up to isomorphism, every edge pair (brute force) |
| `fastN.py`, `fast_check.py` | N for every edge pair of one graph in a single sweep over edge subsets: component counts by a DP over edges, then per (|A|, k(A)) bin the Gram matrix of the edge indicators gives Z_ef for all pairs; `fast_check.py` compares it with `brute.py` |
| `d3_seven_dense.py` | D3 on every graph on 7 vertices with 14 to 21 edges up to isomorphism, every edge pair (`fastN.py`) |
| `d3_eight_rand.py` | D3 on random graphs on 8 vertices with 12 to 20 edges, every edge pair (`fastN.py`) |
| `d3_exh.py` | D3 on every graph on 5 vertices and every edge pair, and on dense random graphs on 6-7 vertices |
| `ext_31_40.txt`, `d3_adj.txt`, `d3_dis.txt`, `d1check_out.txt`, `d3_exh_out.txt`, `d3_rand_out.txt` | outputs |

Results:
- D1: the swap sum equals brute N on 33 of 33 graphs (K_4, K_5 adjacent and disjoint, 30 random). The control
  N = lam(u - 2u^2) is flagged by `d3.series_ok_dict`, so the D3 test can fail.
- D3 on K_n: no negative coefficient for n = 9..30, adjacent and disjoint, and a_1 != 0 throughout.
- D3 on general graphs: no failure on any of the 8,040 edge pairs with N != 0 among all graphs on 5 vertices, on
  117 dense random graphs on 6-7 vertices (11-15 edges), or on 120 random graphs (seed 84, n = 4..7).
- Bernstein check extended to n = 31..40: clean.
- D3 on every graph on 6 vertices up to isomorphism (all 156 classes of the networkx atlas, `d3_six.py`, output
  `d3_six_out.txt`): 3,616 edge pairs with N != 0, no failure.
- `fastN.py` agrees with `brute.py` on 144 of 144 edge pairs (8 random graphs on 4-6 vertices), with the K_n recursion
  `rec.py` on K_7 (adjacent and disjoint pairs), and reproduces the 6-vertex count above (3,616 pairs, no failure).
- D3 on every graph on 7 vertices with 14 to 21 edges up to isomorphism (146 classes, `d3_seven_dense.py`, output
  `d3_seven_dense_out.txt`): 15,499 edge pairs with N != 0, no failure.
- D3 on 40 random graphs on 8 vertices (seed 88, 12 to 20 edges, `d3_eight_rand.py`, output `d3_eight_rand_out.txt`):
  4,922 edge pairs with N != 0, no failure.
- The same on 200 more random graphs on 8 vertices (seed 89, output `d3_eight_rand89_out.txt`): 23,210 edge pairs
  with N != 0, no failure.
- D3 on every graph on 7 vertices with at most 13 edges up to isomorphism (898 classes, `fastN.py`, output
  `d3_seven_fast_out.txt`): 34,263 edge pairs with N != 0, no failure. With the dense classes above this covers all
  1,044 graphs on 7 vertices. The brute-force run of the same classes (`d3_seven.py`, `d3_seven_out.txt`) gives the
  same 34,263 pairs and no failure.

Like the rest, these are finite checks, not a proof for all n.

## Every K_n by vertex support, and a stronger statement E1 (18 October)

| file | what it does |
|---|---|
| `kappa.py` | writes the D3 coefficients on K_n as c(n, i, t) = sum_r kappa(i, t, r) C(n - V0, r) and computes every kappa with r <= NMAX - V0 by binomial inversion from K_V0 .. K_NMAX. `python kappa.py adj\|dis NMAX` |
| `kpoly.py` | the same, as a polynomial fit in n with the degree bound 2i - V0 fixed in advance and every further n used as a check |
| `kappa_control.py` | the inversion applied to N itself instead of N/(1-q)^2 |
| `kappa_union.py` | grouping by edge union instead of vertex support (fails, see below) |
| `e1_check.py`, `e1_rand.py` | E1 on K_n, on every graph on V vertices up to isomorphism, and on random graphs (`fastN.py`) |
| `kappa_adj_summary.tsv`, `kappa_dis_summary.tsv` (per (i, r): entries, least kappa nonnegative, digit counts, monotonicity in t; the full tables, 20 MB each, are not committed - `kappa.py` regenerates them), `kpoly_*_log.txt`, `kpoly_*_out.json`, `e1_*_out.txt` | outputs |

Setup. At lam^i, N on K_n is a signed sum over edge-set pairs (A, B), each weighted q^(2n - rank A - rank B). Measured
from 2n - i, the q-power is the pair's total cycle rank, which does not depend on n. So the coefficient c(n, i, t) of
q^(2n-i+t) in N/(1-q)^2 is a signed count of pair shapes. A shape whose edges, together with e and f, span exactly
r + V0 vertices (V0 = 3 for an adjacent pair, 4 for a disjoint one) has C(n - V0, r) placements in K_n, so

    c(n, i, t) = sum_r kappa(i, t, r) C(n - V0, r)   for every n >= V0,

with kappa(i, t, r) determined by K_(r+V0) alone. Past the top of the window the coefficient equals a_1, because N
vanishes at q = 1. If every kappa is nonnegative, D3 holds on every K_n.

Results.
- Every kappa with r <= 26 (adjacent) and r <= 25 (disjoint) is nonnegative: 157,080 and 154,308 nonzero entries.
  A pair at lam^i uses at most i - 2 edge slots besides e and f, so r <= 2i - 4. The table is therefore complete
  for i <= 15 (adjacent) and i <= 14 (disjoint). Within it, the largest nonzero support is r = 2i - 6 (adjacent)
  and 2i - 8 (disjoint). For larger i, only entries with r up to the computed bound are covered.
- The polynomial form is confirmed independently by `kpoly.py`. For i <= 13 the degree-(2i - V0) interpolant
  reproduces every later n up to 29, with at least three checks per coefficient family (68 of 68 adjacent, 65 of 65
  disjoint), and its coefficients in the basis C(n - V0, r) are all nonnegative.
- Control: the same inversion applied to N's own q-coefficients gives 2,511 negative kappa (adjacent) and 2,342
  (disjoint) at n <= 12, so the inversion does not force a sign.
- Top layer: at r = 2i - 6 (adjacent) kappa(i, t, r) = (2k)!/k! with k = i - 3, at every offset t (1, 2, 12, 120,
  1,680 for i = 3..7). That counts k new edges on 2k new vertices, each placed in A or in B. The next two layers
  also close (adjacent, checked for every i <= 15, independent of t):
  kappa(i, 2i - 7) = (2k)!/k! (2i - 1)/2, and
  kappa(i, 2i - 8) = (2k)!/k! (12k^3 + 44k^2 + 21k - 71) / (12(2k - 1)).
  The second formula comes from a quartic fit on k = 1..5 and holds on k = 6..12. Its cubic has one real root,
  0.958, so the layer is positive for every k >= 1, with the thinnest margin at k = 1 (value 1/2). From
  r = 2i - 9 down, kappa depends on t. For disjoint pairs (k = i - 4, every i <= 15) the top layer is
  kappa(i, 2i - 8) = 2 (2k)!/k! and the next is kappa(i, 2i - 9) = 2i (2k)!/k!. From r = 2i - 10 down, kappa
  depends on t.
- kappa(i, t, r) is nondecreasing in t in all 7,477 (adjacent) and 7,111 (disjoint) groups (i, r).
- Edge support fails. Grouping pairs by H = A u B and asking D3 of each K(H) breaks already on K_4 with a disjoint
  pair (-2 at lam^6), and on 46 of 510 edge pairs over the graphs on at most 5 vertices without isolated vertices.
  Positivity on K_n needs the whole sum over the spanning graphs of each vertex set.

E1. Monotonicity in t says that on K_n the first differences of the D3 coefficients, which are the q-coefficients of
N/(1-q), are nonnegative too. As a statement for every graph:

    (E1) for every lam-power, N/(1-q) = N/u expanded in q has nonnegative coefficients.

E1 implies D3 (D3 is its partial sums) and is strictly stronger: N = lam u^2 passes D3 and fails E1, and both controls
lam(u - 2u^2) and lam u^2 are flagged by `e1_check.e1_neg`. In the swap-class notation of the dossier (17 Oct 22:52),
N/u = sum_s lam^s sum_j (P[s][j+1] - Q[s][j]) q^j, so E1 is P[s][K] >= Q[s][K-1] for every s and K. At every size
and cluster count, the bad pairs are no more numerous than the good pairs with exactly one more cluster. That is the
Hall condition with no cumulation, and the count an injection adding exactly one cluster would need.

E1 checks:
- K_n, n = 3..12, both pairs: no negative coefficient.
- K_n, n = 13..30, both pairs (`e1_kn_out.txt`): no negative coefficient.
- Every graph on 5 vertices up to isomorphism, every edge pair: 336 pairs with N != 0, no failure.
- Every graph on 6 vertices up to isomorphism (all 156 classes), every edge pair: 3,616 pairs with N != 0 (the D3 count), no failure.
- 40 random graphs on 7 vertices (seed 90, 8 to 18 edges): 3,330 pairs with N != 0, no failure.
- 30 random graphs on 8 vertices (seed 91, 12 to 20 edges, `e1_eight_rand91_out.txt`): 3,696 pairs with N != 0, no failure.
- every graph on 7 vertices up to isomorphism (1,042 with at least two edges, `e1_seven.py`, `e1_seven_out.txt`): 49,762 pairs with N != 0, no failure.

None of this is a proof for every n or every graph. On K_n it turns "for every n" into "for every r", each r a
finite computation on K_(r+V0), and E1 names a sharper statement for the matching to aim at.

### E1 as a comparison of separating and connecting pairs (18 October, 03:4x)

Write e = uv. In N = Z_e Z_f - Z Z_ef, the pairs (A, B) with e in A and e in B appear in both terms and cancel. Pair
each remaining positive pair (X + e, Y) with the negative pair (X, Y + e), where X, Y are edge sets of G - e and f is
in Y. With k(X + e) = k(X) - 1 + [u ~ v in X], this gives

    N/(1-q) = lam * sum_{X, Y in G - e, f in Y} lam^(|X|+|Y|) q^(k(X)+k(Y)-1)
              * ( [u !~ v in X, u ~ v in Y] - [u ~ v in X, u !~ v in Y] ).

Swapping X and Y in the second term turns E1 into one statement. Among pairs (X, Y) of edge sets of G - e in which X
separates u from v and Y connects them, at every fixed |X| + |Y| and k(X) + k(Y),

    #{f in Y - X} >= #{f in X - Y}.

Summed over k, this is immediate: (X, Y) -> (X - f, Y + f) keeps X separating, Y connecting and the size. The map
fails only on the cluster count, which it moves by [f is a bridge of X] - [f joins two components of Y]. `e1_swap.py`
checks the identity coefficient by coefficient against fastN's N, from both orders of (e, f) (`e1_swap_out.txt`):
154 of 154 cases on random 5-vertex graphs, 288 of 288 on random 6-vertex graphs. The map keeps the cluster total
on 57% and 52% of the f-in-X pairs, so it is not the injection; a proof has to handle the two cases where the
indicators differ.

Dead route (`e1_types.py`, `e2_check.py`, `e2_out.txt`). On K_5 with an adjacent pair, the good pairs the move does
not reach (f pivotal: X + f connects u, v, or Y - f does not) outnumber all bad pairs in every (size, k) row. Call that
E2; it would imply E1. It is false: K_4 with a disjoint pair fails it in 4 rows (at (5, 4): G = 16, B = 5, pivotal 0),
K_5 with a disjoint pair in 23, and 133 of 292 ordered pairs on random 5-vertex graphs fail it. E1 held in every one of
these cases. Where f lies on no path from u to v (a pendant f, say), G = B exactly, consistent with N = 0 when e
and f lie in different blocks.

A reduction that is proved (`e1_reduce.py`, `e1_reduce_out.txt`). For a pair (X, Y) let W be the cluster of X + Y
that contains f. If W misses u, it misses v too, because Y connects them. Then swap X and Y on every edge inside W. No
edge of X or Y leaves W, so k(X) + k(Y) is unchanged. Every u-v path stays outside W, so X still separates and Y
still connects. The size is unchanged, and f moves between X - Y and Y - X. X + Y is unchanged, so W is too and the
swap is an involution. So E1 holds iff it holds on the pairs with f in the X + Y cluster of u. The numbers agree:
the outside counts cancel in every row on K_4, K_5 (both pair types), 292 ordered pairs on random 5-vertex graphs
and 158 on random 6-vertex graphs, and E1 holds on the inside pairs in all of them. On complete graphs nearly every
pair is inside (K_5, disjoint: 3 outside pairs of each kind against 15,957 and 11,349 inside), so the reduction
mostly matters for sparse graphs.

The same swap works one level down (`e1_reduce2.py`, `e1_reduce2_out.txt`). Remove f from X + Y. Suppose the cluster
D of one endpoint of f misses both u and v. Then f is the only edge of X + Y joining D to the rest, so swapping X and
Y on D and on f keeps everything above and moves f across. That reduces E1 to the pairs where both ends of f reach
{u, v} without using f. The cancellation checks out in every row on the same cases, and E1 holds on what is left;
the dangling pairs are 3 of 121 good pairs on K_4 (adjacent) and 527 of 15,960 on K_5 (disjoint). The hard core is
the pairs where f closes or bypasses a route between u and v in X + Y.
