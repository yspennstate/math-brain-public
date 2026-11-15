# Improved canonical local radius for every regular degree d>=5

T067-LOCAL-RADIUS5-001 v1. Status: proof (unaudited).
This is a local exclusion result, not a claim of canonical entry at degree5.
No assertion of priority is made.

Let q=3, d be an integer at least5, and lambda=1/sqrt(d)>0. Consider the
permutation-invariant uniform-prior posterior law of the canonical tail of
the ferromagnetic Potts broadcast process. Put a=3p-1, M=E||a||^2, x=M/9.
If this law is a BP fixed point and x<=217/4500, then x=0.

Use the prefix drift criterion (11),(12) of UNIFORM-LOCAL-001 v1, with
Mstar=217/500 and delta=1/1000. Its hypotheses and moment estimates are
unchanged: the reviewed CUBIC-FUSION and TERNARY-MOMENTS F2,C inequalities
apply to the canonical fixed point. All actual lambda here are below the
fixed reference 2887/5000. We use neither an unrestricted F1 corollary nor
the invalid extra assertion in RESCALE v1.

In that criterion, g_k=k(k-1)/(12d^2)>0 and A_k,B_k are the explicit
nonnegative prefix remainder bounds. The inequality

  (1-delta)g_k - Mstar A_k - Mstar^2 B_k >= 0               (1)

for k=2,...,d gives, inductively for 0<M<=Mstar,

  M_k <= kM/d - delta g_k M^2 < kM/d.

For k=d this contradicts the fixed-point identity M_d=M. The only new
obligation is (1) on the larger parameter rectangle.

Set l=lambda, d=1/l^2, k=2+r(d-2), l=Lz, with 0<=r,z<=1 and
L=559017/1250000. Clearing the denominator in (1) multiplies it by
8640000(1-l)^3(1+l)^3, positive at every actual l in (0,L]. The resulting
polynomial has bidegree(17,6). Its tensor Bernstein representation has
120 strictly positive and6 zero coefficients, and none negative. Thus it
is nonnegative throughout the rectangle. Since 5L^2>1, every d>=5 is
included. Values at l=0 are only limits of the polynomial, never an
infinite-degree probabilistic recurrence.

The symbolic producer is checks/uniform_local_certificate.py with:

  --M 217/500 --lambda-max 559017/1250000 --margin 1/1000 --name radius_d5_048

The complete raw polynomial, the two basis conversions and their positive
normalizations are saved as uniform_local_radius_d5_048_{raw,bern1,bern2,
report}.json. The separate checker replay_selected_local_certificates.py
imports no symbolic producer. It reconstructs the rational prefix-sum
numerator, verifies its full coefficientwise identity to the raw data,
and redoes both Bernstein conversions. It also checks the unsummed
recurrence at28 integer pairs on square degrees9 through400. These sample
checks validate the encoding; the whole rectangle proves the assertion.
The replay receipt is uniform_local_radius_d5_048_replay.json.

This separate reconstruction was performed by the same worker. An external
mathematical audit is still required. In particular no finite-depth BP
entry calculation at degree5 is contained in this claim.
