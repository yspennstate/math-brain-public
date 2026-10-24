# Three crossings can survive both restrictions while the local split bound fails

Date: 2026-10-02. **Complete proof-method obstruction.** This is not an
FEI counterexample. It strengthens the scope of the previously audited
[largest-weight local obstruction](three_crossing_largest_weight_obstruction.md):
even requiring all three crossings to remain actual in **both** pivot
restrictions does not restore a dimension-independent local entropy
increment bound. It also shows why a crossing-count-only variant of
the [lacunary tree descent](three_crossing_lacunary_entropy_known_derivation.md)
cannot prove ordinary FEI for all nearby-three-crossing functions.

## Exact rational construction

Let `N>=3` be odd, `w=N+1`, and `K=2N^6`. Use `N` original coordinates
`x_j` of weight one, one pivot `z` of weight `w`, and `K` further
coordinates `y_l` each of weight `a=3w/K`. Define

\[
 V=a\sum_{l=1}^K y_l,\qquad
 S=wz+\sum_{j=1}^N x_j+V.
\]

The pivot is the unique largest weight (`w>1>a>0`). Let `F` have the
four labels `-,+,-,+` at the three cuts

\[
 -w<2<w,
\]

and put `f_N=F(S)`. All weights and cuts are rational. The outer cuts
span `2w`, and both adjacent gaps are at most `2w`; the construction
lies inside the remaining nearby-window regime.

There are no endpoint ties. Writing `r` for the number of positive `y`
coordinates,

\[
 V=\frac{3w(r-N^6)}{N^6}.
\]

The original score `wz+sum x_j` is odd, `N^6` is odd, and `3w` is even.
Thus every full score has odd numerator over denominator `N^6`, whereas
all three cuts are even integers.

### Every component remains nonempty in both restrictions

Fix all `x_j=-1` and vary `r` from zero to `K`. For `z=-1`, the score
grid runs from `-4w-N` to `2w-N=w+1`. For `z=+1`, it runs from
`1-3w` to `1+3w`. Both grids extend strictly below `-w` and above `w`.
Their common step is

\[
 2a=\frac{3w}{N^6}<1.
\]

Each interior interval has length at least `N-1>=2`, and both outer
intervals contain a grid endpoint. Hence all four alternating components
are nonempty in **each** pivot branch. All three cuts are genuine sign
changes in the ordered attained-score list of each branch. The whole
function also has exactly three actual crossings.

## It is an extremely small perturbation of the old obstruction

Delete the `y` contribution but retain all its coordinates as irrelevant,
and denote the resulting function by `f_N^0`. The old exact construction
gives, with `epsilon=2^-N`,

\[
 I_z(f_N^0)=\epsilon,
 \qquad
 \frac{\Delta_zH(f_N^0)}{\epsilon}
 \ge L_N:=\frac{N+3}{2}-\log_2\frac{N(N+1)}2
 \longrightarrow\infty
\]

for odd `N>=15`. Its branch functions are majority and majority with
the single all-minus value flipped. The complete old coefficient proof
is in the linked predecessor and is not inferred from numerical tests.

The old score is an odd integer, so its distance from every even cut is
at least one. If `|V|<1`, all labels remain unchanged, in the full
function and in either pivot branch. The elementary Rademacher Chernoff
estimate `cosh t<=exp(t^2/2)` gives

\[
 \begin{aligned}
 d_N&:=\Pr(|V|\ge1)
 \le2\exp\left[-\frac{K}{18w^2}\right]\\
 &\le2\exp(-N^4/36),
 \end{aligned} \tag{1}
\]

because `w<=2N`. The total and both branch disagreement probabilities
are at most `d_N`. In particular,

\[
 I_z(f_N)\le\epsilon+2d_N. \tag{2}
\]

## Self-contained spectral entropy continuity

For Boolean functions `u,v` disagreeing with probability at most `d`,
Parseval gives `||uhat-vhat||_2<=2sqrt(d)`. Cauchy--Schwarz then yields

\[
 \frac12\sum_S|\widehat u(S)^2-\widehat v(S)^2|
 \le\frac12\|\widehat u-\widehat v\|_2
                \|\widehat u+\widehat v\|_2
 \le2\sqrt d. \tag{3}
\]

For probability laws on an alphabet of size `D`, let their total
variation distance be `t`. A maximal coupling uses their common masses
`min(P_j,Q_j)` to agree with probability `1-t`. Conditional on a
disagreement and the other variable, there are at most `D-1` possible
values. The entropy chain rule therefore proves both directions of

\[
 |H(P)-H(Q)|\le h_2(t)+t\log_2(D-1). \tag{4}
\]

Let `M=N+K+1` be the full dimension and
`t_N=2sqrt(2) exp(-N^4/72)`. For `N>=15`, `t_N<1/2`, so the right
side of (4), bounded by
`omega_N=t_N M+h_2(t_N)`, is increasing throughout the relevant range
`0<=t<=t_N`. The full function and its two restrictions therefore give

\[
 |\Delta_zH(f_N)-\Delta_zH(f_N^0)|\le2\omega_N. \tag{5}
\]

The branch alphabet has only `2^(M-1)` values, so the same `omega_N`
is a valid upper bound for each branch.

The entropy inequality `h_2(t)<=t[log_2(1/t)+log_2e]` shows
`omega_N` is at most a polynomial in `N` times `exp(-N^4/72)`.
Consequently `omega_N/epsilon ->0` and `d_N/epsilon ->0`.
Combining (2) and (5),

\[
 \frac{\Delta_zH(f_N)}{I_z(f_N)}
 \ge\frac{\epsilon L_N-2\omega_N}{\epsilon+2d_N}
 \longrightarrow\infty. \tag{6}
\]

Thus a largest-pivot local FEI bound fails despite complete crossing
retention in both restrictions. Rare tail scores can change a combinatorial
crossing count while having negligible entropy or influence effect.

## Scope of the failure

This does not disprove ordinary FEI, a measure-sensitive stopping tree,
the trace candidate using the actual middle crossing, or the completed
parallel-slab/parity-slab theorems. The old `zf_N^0` was a slab in its
original defining score. Here `zf_N` has three actual score crossings
in each fixed-`z` branch and hence is **not** a slab in that same defining
score. No claim is made that it cannot admit a different slab or
character-slab representation. It is unnecessary to classify such
representations to prove the local-method obstruction.

The
[standalone independent checker](verify_three_crossing_direct_entropy_heat.py)
and [full report](three_crossing_direct_entropy_heat_checks.json)
check the rational score grids and endpoint parity exactly. They also
check the predecessor coefficient identity and continuity scale with
separately labeled numerical entropy evaluations. No full truth table
with `2N^6` tiny coordinates is enumerated or claimed to be enumerated.
