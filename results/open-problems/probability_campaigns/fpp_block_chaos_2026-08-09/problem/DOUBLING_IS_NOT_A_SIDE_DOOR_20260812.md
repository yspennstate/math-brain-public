# Variance doubling is not a side-door: what the natural routes give, and why constant-A
# doubling IS the wall. 2026-08-12 pass 89. By-hand; half a page.
# STATUS: two small verified computations + one equivalence observation. Nothing moves chi.

The checklist's item-5 sub-problem: unconditional variance doubling, Var(X_{2n}) <= A Var(X_n)
with constant A. Fire 82's literature pass found it unnamed. Before anyone spends real time:
here is where the obvious routes land.

## Route 1 (Efron-Stein / influences) gives A ~ n/log n, not a constant

For bounded weights tau_e in [a, b]: Efron-Stein,
    Var(X_{2n}) <= (1/2) Sum_e E[(X - X^{(e)})^2],
and resampling one edge moves X by at most (b - a), and only if e lies on a geodesic of the
smaller configuration, so
    Var(X_{2n}) <= (1/2)(b-a)^2 E|gamma_{2n}|.
For a > 0 the geodesic length is linear deterministically-in-expectation
(|gamma| <= X_{2n}/a <= C n after the shape theorem; for a = 0 substitute Kesten's length
bound under F(0) < p_c). Net:
    Var(X_{2n}) <= C' n.
That is the classical linear variance bound, scale-compared: with the only unconditional
lower bound Var(X_n) >= B log n (NP95 Thm 2, transcription on file), this route certifies
    A(n) ~ n / log n
- the SAME ratio as the global certified window. Nothing about the doubling FORM extracts
more; the route never sees the two scales interact.

## Route 2 (subadditivity) gives nothing

X_{2n} <= X_n + X'_n (concatenation through n e1) is pointwise domination, and pointwise
domination compares no variances - the min over paths AVOIDING the midpoint can have larger
fluctuation than the through-midpoint sum. (Same observation as checklist item 5; recorded
here so the two dead routes live next to each other.)

## The equivalence observation (why this is the wall and not a shortcut)

If constant-A doubling held unconditionally, the maintain-up bootstrap's step certifies:
from R(j) = U(j)/L(j) <= K, a pre-halving bound U_raw(j+1) <= A U(j) gives
    beta_cert = U_raw(j+1)/L(j) <= A K = O(1),
and the refereed halving engine RUNS - the one-directional induction the campaign proved
"does not start" would start. So constant-A doubling is AT LEAST as strong as the beta = O(1)
premise, i.e. at least as hard as the (L1') variance-ratio wall (CRUX 9.8). Conversely the
influence computation above shows the generic machinery caps at the window ratio. Anyone
attacking "just doubling" is attacking the wall with fewer tools.

COROLLARY for the record: the two named regularity sub-problems are NOT symmetric.
MONOTONICITY (Var nondecreasing in n) remains a genuinely separate, plausibly softer target
(open even for the mean; arXiv 1202.2665). DOUBLING with constant A is wall-equivalent and
should be treated as a reformulation of the main obstruction, not as low-hanging fruit.
The checklist's closing-verdict list is annotated accordingly.
