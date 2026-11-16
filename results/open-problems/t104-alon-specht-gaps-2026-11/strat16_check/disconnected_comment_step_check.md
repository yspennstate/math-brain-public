# STRAT16 disconnected_certificate.py: the comment-only step (an agent, 13 Nov 2026 ~15:00 +04)

Asserted by the script: the X3 padding identity, the bracket 7/3 + 31/3 z + 2z^2 + (53/3 + 11/3 z) g + (10+2z) q with
positive coefficients, and for r = 3, 4 the polynomial 2(k+1)(k-2) - 2kr + 2(k+2) has positive coefficients in z = k-5.

Comment only (not asserted): on the selected S5=0 equality, X1=0 makes L a graph projection (STRAT7 RESULT l.147: T=0 forces
every nonzero eigenvalue to equal lambda), its rank including the external edge is 2, 3 or 4, and h >= 1.

Hand check. With h = 1 the bracket is f(r) = 2(k+1)(k-2) - 2kr + 2(k+2) = 2k(k - r):
  r=2: 2k(k-2)   r=3: 2k(k-3)   r=4: 2k(k-4)   r=5: 2k(k-5), which is 0 at k=5 (N=7).
So rank 5 (the edge plus a five-vertex component with all four nonzero eigenvalues equal, i.e. a scaled K5 beside the edge)
is exactly where strictness fails at N=7 if h = 1. The script's comment excludes rank 5 without saying why.
Questions for the write-up: (a) why rank 5 cannot occur in the selected class (tr L5 <= 4 and the edge weight 1/(2M) >= 1/5
from LOG 14:5x may exclude it - check); (b) the claim h >= 1 from 'every selected carrier has degree >= 1/2'.
Neither is a counterexample: at worst the equality analysis at N=7 needs the K5+edge point named or excluded.

## Resolved (same day, next tick): the comment step holds
- Scope: the script treats DISCONNECTED five-parts. A five-vertex part with c >= 2 components has Laplacian rank <= 5 - c <= 3,
  so with the external edge (rank 1) the total rank is <= 4. Rank 5 needs a connected five-part (scaled K5); not in scope here.
- h >= 1: with X1=0, L0 is a projection (STRAT7 l.147). Each connected component of a projection Laplacian with kernel 1 on
  that component is I - J/n_c, so every vertex has degree (n_c-1)/n_c >= 1/2. h = sum_i P_ii (L0)_ii with tr P = 2 and P
  supported on carrier vertices, hence h >= 1 (the edge vector gives exactly 1/2, the five-part vector >= 1/2).
- Then the bracket is >= 2k(k-r) with r <= 4, strictly positive for k >= 5. Step verified by hand; the rank-5 worry was a
  scope misreading on my part. (Side check: even edge + scaled K5 has h = 1/2 + 4/5 = 13/10, bracket 2k(k-5)+2(k+2)(3/10) > 0.)

## Independent minimum search (NUMERICAL, my_min_search.py, written from RESULT.md (1), 60 SLSQP starts per k, Mac mini 1)
Every start converged to A = J/5, i.e. C = I - J/5 (the edge beside a scaled K5, rank 5 total), for every u:
  k=5 (N=7): T = 0.04032   k=6: 0.112   k=10: 0.257   k=1e6: 0.480
Exact check by hand at A = J/5: tr C = 4, M = 5/2, h = 1/2 + 4/5 = 13/10, B = 0, Y = 0, tr C - tr C^2 = 0, so
T = (3/2)/k^2 [2(k+1)(k-2) - 10k + (13/5)(k+2)] / (25/4); at k=5 the bracket is 36 - 50 + 18.2 = 4.2, T = 0.252/6.25 = 0.04032;
at k -> infinity T = 3/6.25 = 0.48. Both match the search. This point is the g = 0 endpoint of the rank-two boundary that
rank_two_certificate.py certifies. So the numerical minimum of the whole 2+5 closure sits on an already-certified family,
not on the open rank-three boundary; margin at N=7 is 0.040 (thin but positive), growing with N. Local search only.

## Face-by-face search at N=7 (NUMERICAL, my_min_faces.py; every edge set with 4..7 edges forced, 3 SLSQP starts each)
792 faces, 215 with a feasible optimum. Lowest values ~ -3e-13 .. +3e-15 (round-off). Every such minimiser has the SAME
structure: one five-part edge of weight 1/2, the other three vertices isolated (A_ii = 1), C eigenvalues {0,0,0,0,1}, u the
edge contrast - i.e. the two-equal-edges point (the five-part collapsed to an edge beside the external edge), which is the
known S5 = 0 equality case. So: no negative value anywhere in the forced sparse faces; the only zeros seen are the
expected two-edge equality limit; the unforced search's interior minimum is edge + K5 (T = 0.0403). Consistent with the
equality statement STRAT16 is aiming for. Corroboration only (local search, 3 starts per face).
