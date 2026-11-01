Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — constant hereditary allocation for quadratic phases with one affine-flat sign defect

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved. The source-level quantity “finite universal upper bound for `C_FEI`” remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**.

**New mechanism-level theorem.** Let `A` be any affine subspace of `F_2^n` (possibly all of the cube; the empty set is harmless) and let `q:F_2^n->F_2` have algebraic degree at most two. Put

\[
f(x)=(-1)^{q(x)+1_A(x)}=(-1)^{q(x)}\sigma_A(x),
\qquad \sigma_A=1-2\,1_A.
\]

Then:

1. there exists a full adaptive physical restriction tree `T` such that
   \[
   \boxed{R_T(f)\le 4 I(f);}
   \tag{A}
   \]
2. directly,
   \[
   \boxed{H(\widehat f^{\,2})\le C_{\rm flat} I(f),}
   \tag{B}
   \]
   where
   \[
   C_{\rm flat}
   =\frac{h_2(7/16)}{7/16}+\frac2{\ln2}
   =5.145274443580206\ldots.
   \tag{C}
   \]

The constants are independent of `n`, the codimension or orientation of `A`, and the rank/density of the quadratic phase. No fresh variables are introduced. In particular the defect set may have exponentially many points and may be an oblique parity-defined flat; this strictly changes the mechanism from the preceding finite-cardinality Hamming-defect theorem.

This is still a restricted class theorem, **not full FEI**.

## Dependencies actually consumed

The progress-first directive was followed. I read only the dependencies needed for this route, rather than rescanning the archive.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains the T01 FEI owner; roughly 90% of effort is new derivation; NM13-02 is the complementary entropy worker.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the arbitrary-seed fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` requires appended control variables and a density hypothesis, and is explicitly not full FEI.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open and the false pointwise erasure, all-fixed-coefficient affine-drift, resolvent/interpolation, and Han absolute-overlap routes remain retired.
- Newest preceding P03 substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T07-29-11+0300__fei-finite-defect-quadratic-stopping.md`, blob `4595de09809b9a7f7bd2fe91a7bf1354a81c863b`: proves an `O(log log t)` hereditary/FEI theorem for arbitrary `t`-point Hamming perturbations of a quadratic phase and explicitly suggests replacing defect cardinality by a restriction-stable structural complexity.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__fei-reed-muller-hereditary-allocation.md`, blob `fbcc39447666a43d398403ad2e89b7e50c6adf1b`: for a degree-`<=d` Boolean phase, with
  \[
  \kappa_d=2^{d-1}h_2(2^{1-d}),
  \]
  it proves `H<=kappa_d J<=kappa_d I` and, on every adaptive full physical restriction tree, `R_T<=kappa_d J_T<=kappa_d Q_T`.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: supplies the exact partial-tree identities
  \[
  H-H_L=R_T+S_T,\qquad I-I_L=Q_T,
  \]
  and the valid dependent-branch payment
  \[
  0\le S_T\le\frac2{\ln2}J_T\le\frac2{\ln2}Q_T.
  \]
- Newest available companion report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T07-05-27+0300__descendant-influence-hereditary.md`, blob `dfbd0ec25828d1edff10d6b7f9bf8a10e45b66e0`: proves a descendant-influence recursive certificate and announces an influence-lifetime/fractional high-degree-monomial-cover route. The present affine-flat-defect route is complementary and does not edit or claim that peer scope.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI theorem or exact affine-flat-quadratic theorem was found there.

No peer file or peer claim was edited.

## Current public-source scope

A fresh source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture*. Its current text still states the universal Friedgut--Kalai FEI conjecture and develops a coordinate-restriction/stopping-tree sufficient framework plus proper positive subclasses; it does not give a universal finite FEI constant. The Friedgut--Kalai 1996 source attribution is preserved.

A bounded search for FEI together with affine-subspace/quadratic-defect terms did not recover the theorem below. That is negative evidence only. **Publication priority is UNVERIFIED.**

## 1. Notation and the inherited exact tree identities

Work on `F_2^n`. For a Boolean `g`, let `Z` denote its squared-Fourier random set,

\[
\Pr(Z=S)=\widehat g(S)^2.
\]

For a physical coordinate `i`, write

\[
\alpha_i(g)=\operatorname{Inf}_i(g),\qquad
j_i(g)=\min\{\alpha_i(g),1-\alpha_i(g)\},
\]

and

\[
B_i(g)=H(Z_i\mid Z_{-i}).
\]

For a finite adaptive physical restriction prefix `T_0`, with cylinder weights `w_v`, queried coordinates `i(v)`, and leaves `ell`, put

\[
R_{T_0}=\sum_{v\text{ internal}}w_vB_{i(v)}(f_v),
\quad
J_{T_0}=\sum_vw_vj_{i(v)}(f_v),
\quad
Q_{T_0}=\sum_vw_v\alpha_{i(v)}(f_v),
\]

\[
H_L=\sum_\ell w_\ell H(f_\ell),
\qquad
I_L=\sum_\ell w_\ell I(f_\ell).
\]

The inherited proved identities give

\[
H(f)-H_L=R_{T_0}+S_{T_0},
\tag{1.1}
\]

\[
I(f)-I_L=Q_{T_0},
\tag{1.2}
\]

and

\[
0\le S_{T_0}\le\frac2{\ln2}J_{T_0}
\le\frac2{\ln2}Q_{T_0}.
\tag{1.3}
\]

Equation (1.2) is also obtained directly by iterating

\[
I(g)=\operatorname{Inf}_i(g)+\frac12I(g^+)+\frac12I(g^-).
\tag{1.4}
\]

No independence between dependent branches is asserted or needed.

## 2. Exact Fourier law and a constant FEI bound for one affine-flat sign defect

Let

\[
A=x_0+V\subseteq F_2^d
\]

be a nonempty affine subspace of codimension `r`; let

\[
W=V^\perp,\qquad \delta=|A|/2^d=2^{-r},
\]

and put `sigma_A=1-2 1_A`.

### Lemma 2.1 (exact spectrum of an affine-flat sign)

The squared Fourier law of `sigma_A` has

\[
\widehat{\sigma_A}(0)^2=(1-2\delta)^2,
\tag{2.1}
\]

and, for every nonzero `w in W`,

\[
\widehat{\sigma_A}(w)^2=4\delta^2,
\tag{2.2}
\]

with all remaining Fourier coefficients zero.

#### Proof

The normalized Fourier transform of the affine-subspace indicator is

\[
\widehat{1_A}(w)
=\delta\,(-1)^{w\cdot x_0}1_{\{w\in W\}}.
\]

Since `sigma_A=1-2 1_A`, the zero coefficient is `1-2delta`, while every nonzero `w in W` has coefficient `-2delta(-1)^{w dot x_0}`. Squaring gives (2.1)--(2.2). QED.

### Lemma 2.2 (flat-sign entropy is at most four times influence)

For every nonempty affine subspace `A`,

\[
\boxed{H(\sigma_A)\le4I(\sigma_A).}
\tag{2.3}
\]

If `r>=2`, then also `J(sigma_A)=I(sigma_A)`.

#### Proof

The total spectral mass away from zero is, by Lemma 2.1,

\[
M=(2^r-1)4\delta^2=4\delta(1-\delta).
\]

All `2^r-1` nonzero atoms have equal mass. Therefore

\[
H(\sigma_A)=h_2(M)+M\log_2(2^r-1).
\tag{2.4}
\]

Use the elementary bound `h_2(M)<=M log_2(e/M)` to get

\[
\begin{aligned}
H(\sigma_A)
&\le M\log_2\frac{e(2^r-1)}M\\
&=4\delta(1-\delta)\bigl(2r+\log_2e-2\bigr)\\
&\le8\delta r,
\end{aligned}
\tag{2.5}
\]

because `log_2 e-2<0`.

Now consider a physical direction `e_i`. Translation by `e_i` either preserves `A` (when `e_i in V`) or takes it to a disjoint affine coset (when `e_i notin V`). Hence

\[
\operatorname{Inf}_i(\sigma_A)
=\begin{cases}
0,&e_i\in V,\\
2\delta,&e_i\notin V.
\end{cases}
\tag{2.6}
\]

Let `k=#{i:e_i notin V}`. The `d-k` standard basis vectors lying in `V` are linearly independent, so

\[
d-k\le\dim V=d-r,
\]

hence `k>=r`. Thus

\[
I(\sigma_A)=2\delta k\ge2\delta r.
\tag{2.7}
\]

Combining (2.5) and (2.7) proves (2.3). If `r>=2`, then `2delta<=1/2`, so every nonzero coordinate influence in (2.6) is already folded and `J=I`. QED.

### Corollary 2.3 (affine-character twists)

If `chi` is any affine character and `r>=2`, then

\[
\boxed{H(\chi\sigma_A)\le4J(\chi\sigma_A)\le4I(\chi\sigma_A).}
\tag{2.8}
\]

#### Proof

Multiplication by a character translates the Fourier law, so it preserves spectral entropy. On physical coordinate `i`, it either leaves `Inf_i` unchanged or sends it to `1-Inf_i`; hence it preserves folded influence `j_i` coordinatewise. Thus

\[
H(\chi\sigma_A)=H(\sigma_A)
\le4J(\sigma_A)=4J(\chi\sigma_A)
\le4I(\chi\sigma_A).
\]

QED.

This lemma is the first key distinction from the preceding finite-Hamming-defect argument: an affine-flat defect may contain exponentially many points, yet its entropy/influence ratio has an absolute bound independent of ambient dimension and codimension.

## 3. A nonzero quadratic polar row is stable under an affine-flat defect

Let `q` be quadratic on `F_2^d`, and suppose coordinate `i` has nonzero row in the polar matrix of `q`. For the pure quadratic phase `g=(-1)^q`, the multiplicative derivative in direction `i` is a nonconstant affine character, so

\[
\operatorname{Inf}_i(g)=\frac12.
\tag{3.1}
\]

Let `f=g sigma_A`, where `A` has codimension `r`.

### Lemma 3.1 (flat-defect stability)

\[
\boxed{
\left|\operatorname{Inf}_i(f)-\frac12\right|
\le2^{1-r}.
}
\tag{3.2}
\]

#### Proof

On each `i`-edge, the disagreement indicator of `g sigma_A` is the xor of the disagreement indicators of `g` and `sigma_A`. Therefore changing from `g` to `g sigma_A` can alter the disagreement status only on `i`-edges where `sigma_A` changes. Hence

\[
|\operatorname{Inf}_i(g\sigma_A)-\operatorname{Inf}_i(g)|
\le\operatorname{Inf}_i(\sigma_A).
\]

By (2.6), `Inf_i(sigma_A)` is either zero or `2delta=2^{1-r}`. Together with (3.1), this proves (3.2). QED.

Fix an integer cutoff `s>=2` and define

\[
a_s:=\frac12-2^{-s},
\qquad
c_s:=\frac{h_2(a_s)}{a_s}.
\tag{3.3}
\]

If `r>=s+1`, (3.2) gives

\[
j_i(f)\ge a_s.
\tag{3.4}
\]

The spectral-bit marginal identity is

\[
\Pr(i\in Z)=\operatorname{Inf}_i(f),
\]

so conditioning only lowers entropy:

\[
B_i(f)=H(Z_i\mid Z_{-i})
\le H(Z_i)=h_2(j_i(f)).
\tag{3.5}
\]

Since `h_2(x)/x` decreases on `(0,1/2]`, (3.4)--(3.5) imply

\[
\boxed{B_i(f)\le c_s j_i(f).}
\tag{3.6}
\]

For later use,

\[
c_3=2.54515734113324\ldots,
\qquad
c_4=2.2598843618022797\ldots.
\tag{3.7}
\]

No fresh-control variable, root-curvature charge, or child-independence substitution appears here.

## 4. Restriction stability of the class

The class is stable under arbitrary physical restrictions in exactly the form needed by a stopping tree.

If `A=x_0+V` is restricted by `x_i=b`, then `A` either disappears or its surviving section, after deleting coordinate `i`, is again an affine subspace of the residual cube. Its codimension either stays the same or decreases by one. A quadratic polynomial remains quadratic under restriction, and its polar matrix becomes the corresponding row/column deletion.

Thus every node of a physical restriction tree has the form

\[
f_v=(-1)^{q_v}\sigma_{A_v},
\tag{4.1}
\]

where `q_v` is quadratic and `A_v` is an affine subspace or empty.

This is the restriction-stable structural replacement for raw defect cardinality sought in the preceding P03 report.

## 5. Small-codimension leaves reduce to the proved bounded-degree theorem

Suppose a nonempty affine subspace `A` has codimension `r`. Choose independent affine equations

\[
\ell_1(x)=b_1,\ldots,\ell_r(x)=b_r
\]

cutting out `A`. Over `F_2`,

\[
1_A(x)=\prod_{j=1}^r (1+\ell_j(x)+b_j),
\tag{5.1}
\]

so its multilinear algebraic degree is at most `r`.

Consequently, if `r<=s` and `s>=2`, then the Boolean phase

\[
q+1_A
\]

has degree at most `s`. The earlier P03 Reed--Muller theorem therefore gives

\[
H((-1)^{q+1_A})\le\kappa_s I((-1)^{q+1_A}),
\tag{5.2}
\]

and also provides a full physical completion with hereditary allocation

\[
R\le\kappa_s I,
\tag{5.3}
\]

where

\[
\kappa_s=2^{s-1}h_2(2^{1-s}).
\tag{5.4}
\]

If the affine section has become empty, the leaf is merely quadratic and is covered a fortiori by the same degree-`s` theorem.

Numerically,

\[
\kappa_3=3.2451124978365313\ldots,
\qquad
\kappa_4=4.348515545596771\ldots.
\tag{5.5}
\]

## 6. The adaptive affine-flat stopping tree

Fix `s>=2`. Starting from `f=(-1)^q sigma_A`, at a node with residual quadratic phase `q_v` and residual affine set `A_v`:

1. if `A_v` is empty, **stop**;
2. if `A_v` is nonempty of codimension `r_v<=s`, **stop**;
3. if the polar matrix of `q_v` is zero, **stop**;
4. otherwise `r_v>=s+1`; choose any coordinate whose polar row is nonzero and query it.

The process terminates because each query decreases the residual dimension.

At every internal node, (3.6) applies. Hence for the stopping prefix `T_0`,

\[
\boxed{R_{T_0}\le c_s J_{T_0}\le c_s Q_{T_0}.}
\tag{6.1}
\]

Every stopping leaf is of one of the following types:

- **small-codimension / empty affine section:** paid by the degree-`s` theorem with constant `kappa_s`;
- **polar-zero, high-codimension leaf:** the quadratic phase is affine, and Corollary 2.3 pays it with constant `4` because `r_v>s>=2`.

Thus every stopping leaf has both FEI and a full hereditary completion with the common constant

\[
K_s:=\max\{\kappa_s,4\}.
\tag{6.2}
\]

## 7. Hereditary allocation theorem: choose s=3

Complete every stopping leaf of `T_0` by a full physical tree enjoying the leaf certificate `R<=K_s I`, and splice the completions into one full tree `T`.

By (6.1), the leaf certificates, and the exact queried/residual influence budget (1.2),

\[
\begin{aligned}
R_T(f)
&\le c_s Q_{T_0}+K_s I_L\\
&\le \max\{c_s,K_s\}\,(Q_{T_0}+I_L)\\
&=\max\{c_s,K_s\}\,I(f).
\end{aligned}
\tag{7.1}
\]

Now choose `s=3`. By (3.7) and (5.5),

\[
c_3<4,
\qquad
\kappa_3<4,
\]

so `K_3=4`. Equation (7.1) becomes

\[
\boxed{R_T(f)\le4I(f).}
\tag{7.2}
\]

This proves theorem (A).

The significant point is not merely another direct class FEI estimate: the class has an explicit **fresh-variable-free hereditary allocation certificate with a dimension-independent constant**.

## 8. Direct FEI theorem: choose s=4

Apply the exact partial-tree decomposition (1.1), the local allocation bound (6.1), the inherited dependent-branch recombination estimate (1.3), and the leaf FEI bounds:

\[
\begin{aligned}
H(f)
&=R_{T_0}+S_{T_0}+H_L\\
&\le\left(c_s+\frac2{\ln2}\right)Q_{T_0}+K_sI_L\\
&\le C_s\,(Q_{T_0}+I_L)\\
&=C_s I(f),
\end{aligned}
\tag{8.1}
\]

where

\[
C_s:=\max\left\{K_s,c_s+\frac2{\ln2}\right\}.
\tag{8.2}
\]

For `s=4`,

\[
K_4=\kappa_4=4.348515545596771\ldots,
\]

while

\[
c_4+\frac2{\ln2}
=5.145274443580206\ldots.
\]

Therefore

\[
\boxed{H(\widehat f^{\,2})\le5.145274443580206\ldots\,I(f).}
\tag{8.3}
\]

This proves (B)--(C).

For comparison, `s=3` gives `C_3=5.430547422911166...`; the `s=4` choice is the better of these two natural cutoffs. No claim of an optimal FEI constant for the class is made.

## 9. Why this is a material extension of the preceding P03 theorem

The immediately preceding P03 theorem paid an arbitrary defect set `D` of cardinality at most `t` with a hereditary/FEI constant `O(log log t)`. That mechanism must treat the geometry of `D` as adversarial.

Here `A` may have cardinality

\[
|A|=2^{n-r},
\]

which can be exponentially large. The class is instead controlled because affine-flat geometry supplies two exact restriction-stable features:

1. the defect perturbation of a nonzero quadratic polar row is exactly at most `2^{1-r}`;
2. once the quadratic polar part vanishes, the flat sign has an explicit `2^r`-point spectral law and an absolute `H<=4I` bound.

Thus cardinality is replaced by **affine codimension plus exact flat geometry**, and the final constants no longer depend on the defect size at all.

This route is complementary to NM13-02's announced high-degree-monomial influence-lifetime/fractional-cover program. It does not duplicate that peer route.

## 10. Retired routes remain retired

Nothing in this proof revives any of the following:

- the false pointwise erasure shortcut;
- any fixed-coefficient affine-drift payment;
- the retired resolvent/interpolation inequalities;
- Han's refuted all-coordinate absolute-overlap selector;
- the derivative-degree scalar schedule refuted by the one-point family;
- a blind universal root square-curvature bound;
- a universal direct consumed-curvature/query ratio.

The fresh-control theorem from `PROB10` remains restricted to appended controls and is not used in the proof above.

## 11. Executed sanity checks

A new checker was executed and preserved at

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__check_affine_flat_quadratic.py`

creation commit `67d649a459b0d93a7a1e144aedb2d43f4acaf198`, blob `ff0a13f5d75950c0a38f80d4aa7fecd85fd4b874`.

Its actual output was preserved at

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__affine_flat_quadratic_check.json`

creation commit `8b2d5c5cf81a2cabe1918192ef889e24e7e9b488`, blob `80b4f1febfb4125ce5fa8889ebfc28a4d1f32a03`.

The checker performed:

- **317,726 exhaustive cases**: every quadratic phase times every affine subspace through dimension four;
- for cutoff `s=3`, **2,500** deterministic-seed random oblique affine-flat/quadratic trees through dimension eight, containing **14,353 internal queried nodes**;
- for cutoff `s=4`, **2,500** analogous trees, containing **8,297 internal queried nodes**;
- the exact affine-flat entropy formula through codimension 30;
- **500** additional random oblique affine-character/flat leaves through dimension ten.

Recorded results include:

- minimum internal folded influence exactly `3/8` for `s=3` and `7/16` for `s=4`, matching the proved thresholds;
- maximum observed `B_i/j_i` `2.431166951881776` for `s=3`, below `c_3`, and `2.2344569919499935` for `s=4`, below `c_4`;
- maximum influence-budget error `0.0`;
- maximum leaf-bound violation `0.0`;
- maximum hereditary-allocation violation `0.0` for `s=3` and negative for `s=4`;
- maximum direct-FEI violation negative in both sampled cutoffs;
- maximum exact flat-leaf ratio `H/(2 delta r)` through codimension 30 equal to `3.9628463322790015<4`;
- checker status `PASS`.

These finite checks support but do not replace the all-dimensional proof.

## 12. Remaining full-scope obstruction and next attack

Full FEI remains open because an arbitrary Boolean defect is not one affine flat, and arbitrary restrictions need not retain a single-flat representation.

This run nevertheless removes a named obstruction from the preceding route: **literal defect cardinality is not the right structural price**. A defect can be exponentially large and still have a constant hereditary allocation certificate if its affine geometry is rigid enough.

The next nonredundant P03 attack should test the first genuine recombination beyond one flat:

\[
(-1)^q\sigma_{A\triangle B}
\]

for two affine subspaces `A,B`, or more generally a bounded affine-flat arrangement. Restrictions preserve a bounded arrangement, but overlaps can make both polar-row perturbation and the polar-zero spectral leaf nontrivial. The decisive question is whether the single-flat constant-payment mechanism recombines with a constant independent of ambient dimension and relative orientation, or whether two flats already furnish a counterexample to that route. This is complementary to NM13-02's high-degree-ANF cover program.

## Metrics

- full FEI: `OPEN -> OPEN`;
- finite universal source constant: `UNKNOWN -> UNKNOWN`;
- P03 native finite-dimensional atlas: `6 -> 6`;
- fresh-variable dependence in the new theorem: `none`;
- new class: arbitrary quadratic phase times the sign defect of one arbitrary affine subspace;
- new hereditary allocation constant: `4`;
- new class FEI constant: `5.145274443580206...`;
- independent audit: `pending`;
- publication priority: `UNVERIFIED`.

## ledger_delta

```yaml
ledger_delta:
  owner: P03
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_atlas_before: 6
  native_atlas_after: 6
  new_claim:
    id: P03-FEI-AFFINE-FLAT-QUADRATIC-HEREDITARY-01
    status: PROVED_SELF_CHECKED
    scope: "For every affine subspace A of F_2^n and every quadratic q, f=(-1)^(q+1_A) admits a full physical restriction tree with R_T<=4 I(f), and H(f)<=5.145274443580206... I(f). Constants are independent of dimension, affine-flat codimension/orientation, and quadratic rank."
    fresh_variables: false
    full_FEI: false
    audit: pending
    priority: unverified
  mechanism_gain:
    - replaces finite Hamming-defect cardinality by restriction-stable affine-flat geometry
    - exact flat-sign Fourier law yields H<=4I on high-codimension affine-phase leaves
    - nonzero quadratic polar rows remain uniformly folded-influence-paid while flat codimension exceeds a fixed cutoff
    - dependent branches are recombined only through the already-proved P03 paid-recombination identity
  preserved_failures:
    - pointwise_erasure
    - fixed_coefficient_affine_drift
    - resolvent_interpolation
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_root_square_curvature
    - direct_curvature_over_queried_influence_cubic_star
  companion_coordination:
    worker: NM13-02
    newest_blob: dfbd0ec25828d1edff10d6b7f9bf8a10e45b66e0
    complementary_scope: affine_flat_defect_geometry_not_high_degree_monomial_influence_lifetime
  artifacts:
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__check_affine_flat_quadratic.py
    - proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__affine_flat_quadratic_check.json
  next_attack: two_affine_flat_symmetric_difference_or_bounded_affine_arrangement_recombination
```

**End of complete run report.**
