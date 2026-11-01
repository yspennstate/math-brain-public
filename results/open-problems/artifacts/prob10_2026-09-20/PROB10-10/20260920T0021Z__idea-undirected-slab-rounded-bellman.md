# PROB10-10 idea before repository checker — undirected slabs + rigorous rounded Bellman

Runtime requested: GPT-6 maximum. Actual runtime exposed to this worker: GPT-5.6 Sol; reasoning level UNVERIFIED. I do not claim GPT-6 maximum.

Frozen source target and metric are unchanged from `operations/claims/PROB10-10.md`:

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved here}\}.
\]

Current source value is `c_*=0`.  The previous run proved the oriented random-endpoint slab compiler and certified `mu(1,1)<=0.790093366681362...`, but the retained axis lower bound only makes `mu(1,1)<0.60048` sufficient for a positive source defect.

This run will not resume the retired fixed-corner route.  Three different attacks are:

1. **B6 — deform the successful slab compiler from oriented to genuinely undirected finite-width slabs.**  In coordinates `s=x+y`, `d=x-y`, restrict one block to `0<=s<=2m`, `|d|<=w`, but allow all undirected nearest-neighbor edges whose endpoints remain in the slab.  Successive blocks still use disjoint edge-level sets, so random translation by the previous exit does not destroy independence.  Reflection gives zero transverse drift.  If `q^U_{m,w}` is the expected restricted block passage time and `D` the exit displacement in `(m+D,m-D)`, the intended theorem is
   \[
   \frac{\mathbb E T(0,nm(1,1))}{nm}
   \le \frac{q^U_{m,w}}m+\frac{2\sqrt{\mathbb E D^2}}{m\sqrt n},
   \qquad
   \mu(1,1)\le q^U_{m,w}/m.
   \]
   This keeps the block dependence exact while allowing the backtracking that the oriented block forbids.

2. **B8 — discretize only the finite Bellman core, with one-sided arithmetic.**  For the previous oriented block, exact `Fraction` arithmetic becomes expensive at `m=4`.  Instead fix integer scale `Q` and propagate *upward-rounded* Bellman numerators.  For infected state `S`, total boundary rate `b(S)` and transient rates `r_S(v)`, define
   \[
   U(S)=\left\lceil\frac{Q+\sum_v r_S(v)U(S\cup\{v\})}{b(S)}\right\rceil.
   \]
   Induction on the number of remaining transient vertices proves `E(S)<=U(S)/Q`; this is a rigorous rational certificate, not floating-point evidence.  A parallel recursion with absorbing endpoint contribution `D^2` certifies an upper bound on `E D^2` and therefore an explicit finite-to-infinite error coefficient.

3. **B20 — identify why the current algorithm fails before extending it.**  The source defect moves only if the diagonal upper construction is combined with an axis lower bound strongly enough to make `2 mu(e1)-mu(1,1)>0`.  The immediate test is whether a certifiable larger oriented block materially reduces the previous `0.790093...` bound, and how its reachable-state count grows.  If state growth is explosive and the source threshold remains far away, the next mathematical route should be the undirected finite-width compiler above, not a receipt-only larger exact enumeration.

Negation tests to apply:

- random block exits must not create linear transverse drift;
- undirected backtracking must not reuse previous-block edges;
- the deterministic final correction must lie on fresh edge levels;
- rounded arithmetic must be one-sided in the correct direction at every Bellman state;
- any finite numerical experiment is auxiliary only unless the inequality is certified by the rounded recursion.

No source closure is anticipated from a single finite block.  A positive `c_*` remains the source-level goal; block-bound movement is recorded separately.