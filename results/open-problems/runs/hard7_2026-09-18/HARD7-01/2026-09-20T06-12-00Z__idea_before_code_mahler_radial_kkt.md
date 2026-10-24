Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-01 route note — coupled radial KKT / secondary-fan descent at the first 12-vertex boundary

This note is intentionally written **before** constructing the exact checker for this run.

The incoming source metric is `d_sym=3`, unchanged, and the last report triggered `STUCK1` after the combinatorial/shadow-incidence route reached an exact realizable `n=4,V=12,F=22,I=98` boundary polytope. The recovery choice for this run is: **reduce the new analytic stationarity obstruction to a finite exact computation and run it, within the same symmetric Mahler target.** I will not rotate targets in this run.

Methods, all different from the immediately preceding `B1/B20/B26`, are **B5 / B18 / B22**.

## B18 — say the local-minimum problem in the language of radial chambers

For the explicit centrally symmetric polytope

`P=conv{+-v_1,...,+-v_6}`

from the preceding run, replace the six antipodal pairs by

`v_i(t)=(1+a_i t)v_i`,

so `P_t=conv{+-v_i(t)}`. At the degenerate point `t=0`, five opposite facet pairs are five-vertex facets. A generic one-sided radial direction resolves each circuit into a regular triangulation. Hence the **right derivative of primal volume is a finite secondary-fan calculation**, not a smooth Hessian calculation.

For a chamber with tetrahedral boundary facets `T`,

`|P_t| = sum_{F in T} |det(v_{i_1}(t),...,v_{i_4}(t))|/4!`,

so after the chamber is certified the right derivative is exact and rational.

The polar has a complementary fixed-normal description

`P_t^circ={y: |<v_i,y>| <= (1+a_i t)^(-1), i=1,...,6}`.

Its first variation at `t=0` can therefore be computed directly from the twelve existing polar facets. If `c_i` is the total four-dimensional cone-volume from the origin to the opposite pair of polar facets belonging to `i`, then in dimension four

`(d/dt)|P_t^circ|_{0+} = -4 sum_i a_i c_i`.

This remains valid even though the polar's face subdivision changes: simultaneous motion of two or more supporting hyperplanes affects volume only at second order, while each single facet contributes its area times its normal displacement.

Thus a local Mahler minimizer must satisfy, for every radial direction `a`,

`D_+ M_P(a) := |P^circ| D_+|P|(a) + |P| D_+|P^circ|(a) >= 0`.

The exact missing lemma for the explicit boundary witness is therefore:

> Find one rational/integer vector `a` for which the right chamber is certifiable and `D_+ M_P(a)<0`.

This would **not** solve the 12-vertex class or move `d_sym`; it would rigorously eliminate the exact equality-incidence witness as a local minimizer and show why scalar incidence/full-spark conditions are insufficient.

## B5 — add a parameter and differentiate

Exploratory arithmetic points to the coupled direction

`a=(-1,3,3,3,-1,-6)`.

The exact checker should do two things, not merely sample a small `t`:

1. exhaust all `C(12,4)=495` signed tetrahedral candidates and use the first nonzero Taylor coefficient of the affine supporting determinant at `t=0+` to certify the complete right-hand facet chamber;
2. compute the exact one-sided derivative of both primal and polar volumes, then the volume-product derivative.

A fixed nearby rational point may be printed only as a sanity check; the theorem-deciding certificate is the exact right derivative.

## B22 — read the neighboring failures/successes before claiming novelty

Fresh bounded literature checks for this run use:

- Lopez--Reisner (1998), which proves the symmetric conjecture for at most `2n+2` vertices or facets for `n<=8`, so `V<=10` in dimension four is already known;
- Daniel Martin Jimenez Cuevas, arXiv:2606.14709 (2026), whose abstract gives an exact radial-KKT framework and strict radial local minimality of the Hanner orbit;
- Agam Guberman, arXiv:2608.10994 (2026), whose primary abstract says floating-body methods constrain combinatorial structure of volume-product minimizers;
- Chen--Li--Xi--Xu, arXiv:2605.13795 / 2605.09334 (2026), for the dimension-three endpoint.

The exact theorem text of the two 2026 local-structure papers was not fully retrievable from the available primary abstract pages in this bounded run. Therefore I will **not** use a secondary paraphrase of their detailed theorem as a certified premise, and any priority claim for the finite radial obstruction below remains `UNVERIFIED`.

If the exact derivative is negative, the next mathematical step is to derive the corresponding finite piecewise-linear radial stationarity system for an *arbitrary* `V=12,F=22,I=98` equality-class polytope, rather than spend another run searching isolated witnesses.
