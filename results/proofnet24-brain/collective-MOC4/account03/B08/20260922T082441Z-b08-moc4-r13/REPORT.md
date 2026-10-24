# account03/B08 MOC4 research report — r13

Status: **AUXILIARY_ONLY**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution status: **WITHOUT_VERIFIED_BRAIN**.

## Assignment and fresh controls

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, owner-control revision `2026-09-22.2`, and the exact account03/B08 assignment: construct exact or rigorously enclosed candidates over **true unitary matrices and complex spectra**, checking one common separating direction against all 24 spectral permutation products. Old benchmark/installation work is superseded.

Assigned OTHER-account partner actually consumed: account04/B09, `MOC4-OPEN-GAP-GENERICIZATION-v1` (handoff `20260922T071523Z`). That result shows that any strict target counterexample can be moved to simple/nonzero generic spectra, so this run stayed on an exact simple/nonzero complex-spectrum mechanism and did not reopen singular-limit bookkeeping. I also used the current MOC4 lead's mixed-quartic/reserve perspective only as non-answer-bearing coordination: the construction below isolates an exact two-root finite-distance interaction that local strict pair gates do not control.

## New result: `MOC4-PAIR-TRAP-NO-MARGIN-v1`

Take the fixed simple nonzero spectra

\[
a=(23+19i,\ 1+17i,\ 25-26i,\ -35+19i),
\]
\[
b=(-21+13i,\ -1+23i,\ 26-27i,\ 32-21i).
\]

Every one of the sixteen sums `a_i+b_j` is nonzero. For a permutation `p`, write

\[
v_p=\prod_{j=1}^4(a_j+b_{p(j)}).
\]

Let

- `p=4321`, so `v_p=-1262976+2125032 i`;
- `q=3412`, so `v_q=929730+823140 i`.

Define the primitive tie normal

\[
n_0=(216982,365451)
\]

and the integer Bezout perturbation

\[
d=(-17957,-30244).
\]

The difference `v_q-v_p=(2192706,-1301892)` in `(Re,Im)` coordinates satisfies exactly

\[
n_0\cdot(v_q-v_p)=0,\qquad d\cdot(v_q-v_p)=6.
\]

For every integer `N>=1`, define the common real-linear support direction

\[
L_N(z)=(216982N-17957)\Re z+(365451N-30244)\Im z.
\]

### Exact coexposed edge and arbitrarily small strict deficit

At the tie direction `n_0`, `p` and `q` are exactly co-maximal among **all 24** permutation products:

\[
L_0(v_p)=L_0(v_q)=502552011000.
\]

The next-best permutation is lower by exactly

\[
39641580000.
\]

At `N=1`, the direction is

\[
L_1(z)=199025\Re z+335207\Im z.
\]

Exact enumeration of all 24 vertices gives **24 distinct support values** and

\[
\max_\sigma L_1(v_\sigma)=L_1(v_{3412})=460961803230,
\]
\[
L_1(v_{4321})=460961803224.
\]

Thus the exact common-direction deficit of the true unitary permutation candidate `P_4321` is only

\[
6.
\]

The minimum support among the 24 vertices is `-2764694608000`, so the full support width is

\[
3225656411230,
\]

and the normalized deficit is

\[
\frac{6}{3225656411230}
 =\frac{3}{1612828205615}
 \approx 1.86008651730892\times 10^{-12}.
\]

This is an exact all-24 common-direction calculation, not a bistochastic relaxation and not a statement about formal quasidistribution signs.

For general `N>=1`, `q` remains the unique global support maximizer, `p` remains strictly second, and

\[
L_N(v_q)-L_N(v_p)=6
\]

for every `N`. The proof is elementary: at `n_0`, the pair `p,q` is tied strictly above every other vertex; at `N=1`, `q` is strictly above `p` and `p` is strictly above all others; every relevant difference for larger `N` is its positive `N=1` value plus `(N-1)` times a nonnegative tie-normal margin. Since the support width grows linearly in `N`, the normalized strict deficit tends to zero.

**Consequence.** There is no uniform positive normalized support margin obtainable solely from strict elementary pair gates, even for one fixed simple/nonzero complex spectrum pair and exact true unitary witnesses.

## The candidate is strictly maximal on every elementary SU(2) pair orbit

At the permutation `p=4321`, its six transposition-neighbor losses under `L_1` are exactly

| swapped rows | neighboring permutation | `L_1(v_p)-L_1(v_neighbor)` |
|---|---:|---:|
| (1,2) | 3421 | 79,221,639,744 |
| (1,3) | 2341 | 614,779,338,360 |
| (1,4) | 1324 | 487,173,330,150 |
| (2,3) | 4231 | 3,225,656,411,224 |
| (2,4) | 4123 | 434,225,479,974 |
| (3,4) | 4312 | 36,360,921,450 |

All are strictly positive.

This checks the **full continuous pair orbit**, not merely discrete swaps. If an embedded `SU(2)` gate mixes rows `r,s` of a permutation unitary and `x=sin^2(theta)`, determinant bilinearity in the corresponding two-by-two block gives exactly

\[
D(x)=(1-x)v_p+xv_{\tau_{rs}p},
\]

independent of the internal phase. Hence

\[
L_1(D(x))=(1-x)L_1(v_p)+xL_1(v_{\tau_{rs}p})<L_1(v_p)
\]

for every nontrivial `0<x<=1` and for each of the six pairs. Therefore `P_4321` satisfies all six strict continuous pair-maximality gates even though it is not the global support maximizer.

This sharpens the operational lesson from the named partner's strict-pair gate work: **pair strictness is necessary at a target-level maximizer but cannot by itself supply a quantitative global margin.**

## Exact two-root finite-distance tunnel

The better permutation is obtained by the two disjoint swaps

\[
3412=(12)(34)\,4321.
\]

Apply independent embedded row rotations in planes `(1,2)` and `(3,4)` to `P_4321`, and set

\[
x=\sin^2\theta,\qquad y=\sin^2\phi.
\]

Because the two planes are disjoint, the determinant is exactly the four-vertex convex combination

\[
D(x,y)=(1-x)(1-y)v_{4321}
+x(1-y)v_{3421}
+(1-x)yv_{4312}
+xyv_{3412}.
\]

Under the same single common support direction `L_1`, define

\[
A=L_1(v_{4321})-L_1(v_{3421})=79221639744,
\]
\[
B=L_1(v_{4321})-L_1(v_{4312})=36360921450,
\]
\[
\delta=L_1(v_{3412})-L_1(v_{4321})=6.
\]

Then exactly

\[
L_1(D(x,y))-L_1(v_{4321})
=-Ax-By+(A+B+\delta)xy,
\]

with

\[
A+B+\delta=115582561200.
\]

Thus each root orbit separately is strongly downhill, while their mixed finite-distance term eventually wins. Along the diagonal `x=y=t`, improvement occurs if and only if

\[
t>\frac{A+B}{A+B+6}
=\frac{19263760199}{19263760200}
\approx0.9999999999480891.
\]

So one must perform both swaps to within about `5.19e-11` in the `sin^2` parameter before this two-root path even exceeds the strict pair trap. This is an exact model of a large positive mixed/quartic interaction hidden behind negative one-root curvature.

The entire two-plane family is itself a convex combination of four permitted spectral permutation products, so this phenomenon is **not** a counterexample to MOC4. It is a proof-method adversary showing why local pair strictness, Hessian negativity in individual roots, or a uniform slack heuristic cannot close the target without a determinant-specific control of mixed interactions.

## Why this is useful for the current collective proof

The campaign lead is currently paying mixed-Schur/cross-block quartic reserves. The example above supplies a fully exact calibration where two strict root losses are `7.92e10` and `3.64e10`, yet a mixed term of `1.1558e11` leaves the globally better endpoint only `6` support units away. Therefore any proposed global argument that lower-bounds target slack from individual-root strictness must explicitly retain the mixed cross term; dropping it can lose essentially the entire margin.

The account04/B09 open-gap genericization was consumed in choosing the correct regime: no singular/repeated-spectrum limit is needed to realize this no-margin obstruction. The spectra here are simple and nonzero and all `a_i+b_j` are nonzero.

## Next B08 obligation

`MOC4-MIXED-TUNNEL-OFF-MONOMIAL-v1`: perturb this exact four-vertex tunnel into a genuinely nonmonomial exact rational-Cayley unitary while preserving a unique common support direction and strict pair gates, then either (a) obtain an even stronger inside-hull exact certificate that quantifies the determinant-specific mixed payment, or (b) if an all-24 common separating gap becomes negative, verify it as a true MOC4 counterexample. A second route is to derive a determinant-specific upper bound on the mixed coefficient at interior pair-stationary points, calibrated against the exact `A+B+delta` phenomenon here.

## Integrity / scope

No arbitrary bistochastic array and no negative formal coefficient is called a target counterexample. No target-level counterexample is claimed. No benchmark gold/keys, FEI proof material, credentials, private transcripts, email, Drive, public dispatch, paid API/Codex, scheduler repair, cross-account native action, or notification mutation was used. Identity and task state were preserved; settings not independently exposed remain UNVERIFIED.
