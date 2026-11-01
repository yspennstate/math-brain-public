Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware 3-SAT: anchored degree-one rescue matchings and a strict variational penalty

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with three distinct variables and uniform independent signs**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, and a literature-status correction

The predecessor report used the explicit-decimal rigorous bracket

\[
3.52\le c_n\le 4.4898
\]

for the Friedgut sharp-threshold sequence `c_n`. This remains the strongest explicit decimal bracket that I have independently recovered and checked in theorem form this run:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]}
\]

so **there is no fleet-produced source-endpoint movement in this run**.

There is, however, an important source-status correction that must not be lost. For fixed `k=3`, convergence of the sharp-threshold sequence is still not known; one should not silently speak of an already-established single limiting threshold. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (2026), explicitly states both facts:

1. for small fixed `k`, existence of a uniform satisfiability threshold remains open;
2. interpolation gives a **rigorous upper bound on the threshold sequence matching the 1RSB variational prediction**.

Their table lists the physics value `d_sat(3)≈12.801` in average-variable-degree normalization `d=k alpha`, corresponding numerically to `alpha≈4.267`. I did **not** recover an independently interval-certified numerical evaluation of the interpolation functional at `k=3`, so I record the strongest supported theorem-form status as

\[
3.52\le\liminf c_n\le\limsup c_n\le U_{\mathrm{1RSB}}(3),
\]

where the interpolation theorem supplies `U_1RSB(3)`, while the decimal `≈4.267` remains a literature-reported numerical evaluation rather than a newly certified constant from this worker. Thus `4.4898` is no longer the conceptual strongest upper mechanism, even though it remains the explicit decimal theorem endpoint independently reconstructed here.

Sources checked this run:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193;
- Diaz--Kirousis--Mitsche--Perez-Gimenez, *A new upper bound for 3-SAT*, arXiv:0807.3600 / FSTTCS 2008;
- Chatterjee et al., *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (2026), DOI `10.1017/S0963548326100406`;
- Franz--Leone, *Replica bounds for optimization problems and diluted spin systems*, arXiv:cond-mat/0208280, for the rigorous interpolation/replica upper-bound mechanism.

Large-`k` threshold identification, sharp-window results, `k`-wise-independent clause models and cavity/replica predictions by themselves do not settle classical iid `k=3`.

## 1. Short handoff and exact failures preserved

The preceding NM13-13 run proved a clean two-flip rescue lemma and proposed a score penalty on rescue stars. A neighboring PROB10-04 run then found the critical obstruction: **arbitrary rescue stars do not compose**. There is an exact four-variable formula in which two children are individually rescued by the same root but flipping both children after the root falsifies another clause. Therefore the old factor `prod_y 1/(r_y+1)` cannot be inserted wholesale into the Diaz count.

Other exact failures that remain binding:

- positive clause-local multiplicative second-moment weights hit the identical-pair barrier `alpha<=log 2/log(5/4)=3.1062837...`, already below the 3.52 lower bound;
- quotienting by solution-graph balls of radius `o(n/log n)` changes counts only by `exp(o(n))` and cannot pay an exponential overlap defect;
- the full-component quotient still has an unpaid cross-component overlap moment;
- whitening/core history counting lacks a uniform exponential multiplicity lower bound.

The companion NM13-06 is now on a constructive majority-assignment / nonbacktracking two-choice repair route. Its newest result proves a strongly subcritical **local** repair Galton--Watson mean through 4.4898 but correctly notes that this cannot imply satisfiability there. The present run remains complementary: it develops a cluster-aware **upper-counting** penalty.

## 2. The key repair of the false rescue-star idea: force a matching

I return to the Diaz `M=23` type system, but use only two very specific extended clause types. Their notation classifies a clause by

\[
\alpha=\begin{pmatrix}\mathrm{ps}&\mathrm{ns}\\\mathrm{pu}&\mathrm{nu}\end{pmatrix},
\qquad \sum \alpha=3,
\]

where `ps`/`pu` are positive satisfied/unsatisfied copies and `ns`/`nu` are negative satisfied/unsatisfied copies. In a blocking clause the unique satisfied negative copy is of subtype `ns1`; in a nonblocking clause a satisfied negative copy is `ns2`.

Define the **anchor type**

\[
a=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\tag{2.1}
\]

Such a clause has one `ps`, one `ns2`, and one `pu`. Its `ps` literal therefore remains protected if that `ps` variable is flipped: the `ns2` literal is another satisfied literal.

Define the **rescue blocker type**

\[
b=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\tag{2.2}
\]

Such a clause is blocking: it has one unique satisfied `ns1`, one `pu`, and one `nu`.

Now select only the following variable classes.

- A **root** is a light true variable of Diaz type `t_{1,1}` whose unique `ps` copy lands in an `a`-clause.
- A **child** is a light false variable of extended degree `(i,1,1)` for some `0<=i<=M`, whose unique `ns1` copy lands in a `b`-clause.
- An edge `x->y` is present when the root `y`'s unique `nu` copy occupies the unique `nu` slot of the child's `b` blocker.

Because a root has degree `(1,1)`, it has only one `nu` copy. Because a child has negative degree one and `k=1`, it has only one negative occurrence, namely its `ns1` blocker. Hence these edges form a **matching**, not a star system. This is the structural change that removes the previous counterexample.

## 3. Anchored degree-one rescue lemma

### Lemma 3.1

Let `A` be a Diaz flat-satisfying assignment. Suppose `x->y` is an edge as above. Then flipping `y:1->0` and then `x:0->1` preserves flat satisfiability.

### Proof

The root `y` has exactly two occurrences.

Its unique positive occurrence lies in an `a`-clause. That clause contains an `ns2` literal which is true under `A`. This `ns2` literal cannot belong to a selected child: a selected child has negative degree one and its sole negative occurrence is `ns1`, not `ns2`. It also cannot belong to a selected root, because roots are true and their negative literals are unsatisfied `nu` copies. Thus the `ns2` anchor is not changed by any selected root/child flip. In particular, flipping `y` down leaves its `a`-clause satisfied.

The unique negative occurrence of `y` is the `nu` slot of the child's `b` blocker. After `y` is flipped down, that `nu` literal becomes true, so the blocker is now doubly safe before `x` changes.

The child `x` has negative degree one. Its sole negative occurrence is the `ns1` copy in that same blocker. Flipping `x` up destroys that one literal, but the newly true `nu` literal of `y` remains. Every other occurrence of `x` is positive and therefore changes from false to true. Thus no other clause can lose satisfaction when `x` is flipped.

Hence both steps preserve flat satisfiability. QED.

The exact checker exhausts all relevant proper 3-literal local clause sign patterns for three selected children and two external anchors. It checked 115 admissible nonblocker clause cases and 12 mandatory blockers, with zero falsifications after the simultaneous selected-pair flips. This finite check is a self-check of the case classification; the proof above is the theorem argument.

## 4. Random scores give an exact `2^{-E}` penalty

Give all light variables iid continuous positive weights `W_v` and, among flat-satisfying assignments, choose one maximizing

\[
S_W(A)=\sum_v W_v A(v).
\]

The positivity of the weights implies that the maximizer is automatically Diaz-`flat'`: every false light variable has a blocking clause, since otherwise flipping it to true would increase the score.

If `x->y` is one of the matching edges in Lemma 3.1, maximality forces

\[
W_x\le W_y.
\tag{4.1}
\]

The matching edges use pairwise disjoint root/child variables. Therefore, for `E` such edges, the `E` inequalities are independent under iid continuous weights and

\[
\boxed{
\Pr_W[W_x\le W_y\text{ on every selected edge}]=2^{-E}.
}
\tag{4.2}
\]

This factor is distribution-free among iid continuous weights. It is also stronger and cleaner than the old star occupancy factor because no multi-child composition is being assumed.

## 5. Exact three-stage refinement inside the Diaz type count

Fix one Diaz coarse type tuple `z`. Use scaled counts (all counts divided by `n`):

\[
P=\ell_{ps},\quad T=t_{1,1},\quad A=c_a,
\]

\[
Q=\ell_{ns1},\quad F=\sum_{i=0}^{M}f_{i,1,1},\quad B=c_b,
\]

\[
L=\ell_{nu}.
\]

The first refinement asks how many of the `Tn` marked `t_{1,1}` `ps` copies land in the `An` anchor-type `ps` slots among all `Pn` `ps` slots. If this number is `un`, the exact relative count is hypergeometric:

\[
R_{ps}(u)=
\frac{\binom{An}{un}\binom{(P-A)n}{(T-u)n}}
{\binom{Pn}{Tn}}.
\tag{5.1}
\]

Likewise, if `hn` of the `Fn` marked degree-one-child `ns1` copies land in the `Bn` blocker-type `ns1` slots among all `Qn` `ns1` slots,

\[
R_{ns1}(h)=
\frac{\binom{Bn}{hn}\binom{(Q-B)n}{(F-h)n}}
{\binom{Qn}{Fn}}.
\tag{5.2}
\]

Conditional on `u,h`, the `un` root `nu` copies are a fixed marked set being matched uniformly to the `Ln` `nu` slots, of which `hn` are now distinguished child-blocker slots. Hence the number `E` of rescue edges is hypergeometric and the score-averaged factor is exactly

\[
\Phi_n(u,h)=
\frac{1}{\binom{Ln}{un}}
\sum_e
\binom{hn}{e}
\binom{(L-h)n}{un-e}
2^{-e}.
\tag{5.3}
\]

This is an **exact finite refinement** of the copy-allocation stage of the Diaz count; no independence approximation has been used.

## 6. A closed variational inequality from Maclaurin's inequality

Equation (5.3) has an elementary sharp-enough upper bound. Give each of the `hn` distinguished `nu` slots weight `1/2`, and each of the other `(L-h)n` slots weight `1`. Then the numerator in (5.3) is the elementary symmetric polynomial `e_{un}` of these weights, while the denominator is `C(Ln,un)`. Maclaurin's inequality gives

\[
\Phi_n(u,h)^{1/(un)}
\le \frac{hn(1/2)+(L-h)n}{Ln}
=1-\frac{h}{2L}.
\]

Therefore

\[
\boxed{
\Phi_n(u,h)
\le\left(1-\frac{h}{2L}\right)^{un}
\le \exp\left[-\frac{uh}{2L}n\right].
}
\tag{6.1}
\]

This converts the cluster constraint into a two-dimensional variational correction.

Write `H(q)=-q log q-(1-q)log(1-q)` and

\[
I(u;a,t,p)
=aH(u/a)+(p-a)H((t-u)/(p-a))-pH(t/p),
\tag{6.2}
\]

on the hypergeometric feasible interval. Stirling's formula applied to (5.1)--(5.2), followed by (6.1), yields the exponent correction

\[
\boxed{
\Delta(z)\le
\max_{u,h}
\left\{
I(u;A,T,P)+I(h;B,F,Q)-\frac{uh}{2L}
\right\}.
}
\tag{6.3}
\]

Both hypergeometric rate terms are nonpositive. The first vanishes only at `u=AT/P`, the second only at `h=BF/Q`. If

\[
0<T,A<P,\qquad 0<F,B<Q,\qquad L>0,
\tag{6.4}
\]

then those two zero locations have `u>0` and `h>0`, so the last term is strictly negative there. On the other hand, forcing `u=0` or `h=0` makes at least one of the hypergeometric rate terms strictly negative. The feasible rectangle is compact and the objective is continuous with the standard `0 log 0=0` extension. Consequently

\[
\boxed{\Delta(z)<0\quad\text{under (6.4).}}
\tag{6.5}
\]

This is the main mathematical advance of the run: **an explicit cluster-aware variational inequality that gives a strictly negative exponential correction at every interior Diaz type possessing positive masses of the two selected variable classes and the two selected clause types.**

At the published Diaz interior critical point, all displayed Lagrange multipliers are positive. Their critical formulas therefore give positive `t_{1,1}`, positive `f_{i,1,1}` on allowed degree classes, and positive masses for both clause types (2.1) and (2.2). Thus the reported interior maximizer lies in the strict-penalty regime (6.4). What remains is not positivity of the mechanism; it is a **certified global reoptimization / transfer**.

## 7. Exact executable checks

Artifacts:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T01-58-11Z__anchored_matching_exact.py`

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T01-58-11Z__anchored_matching_exact.out`

The executed checker verifies:

- 115 admissible local nonblocker clause cases and 12 mandatory rescue blockers: zero failures;
- the exact hypergeometric identity (5.3) against brute-force subset enumeration for all 505 triples `(L,H,U)` with `1<=L<=10`;
- the Maclaurin upper bound for all 505 triples: zero failures;
- a fully exact nested three-stage toy refinement, giving ratio `98839/110880<1`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The toy ratio is **not** a source numeric; it is only an exact bookkeeping self-check.

## 8. What this does and does not prove about the threshold

### Source-level quantity

Explicit decimal bracket:

\[
[3.52,4.4898]\to[3.52,4.4898].
\]

**No source endpoint moved.**

The stronger literature-level theorem form is the interpolation/1RSB upper functional described in Section 0, whose reported physics evaluation is near `4.267`; I do not convert that rounded value into a certified decimal theorem constant without reconstructing the interpolation functional numerically.

### Demonstrated mechanism gain

Before this run, the promising rescue idea had a fatal composition counterexample and required star-occupancy bookkeeping.

After this run:

1. restricting roots to `t_{1,1}` and children to `j=1,k=1` forces rescue incidences to be a matching;
2. the anchor clause type `(ps,ns2,pu)` prevents the root-support clause from becoming a hidden root-root conflict;
3. the blocker type `(ns1,pu,nu)` gives a one-clause exact two-flip rescue;
4. iid score maximality supplies the exact factor `2^{-E}`;
5. copy-allocation averaging yields the closed variational penalty (6.3), strictly negative at every interior coarse type satisfying (6.4).

Thus the run removes the exact obstruction that killed the naive rescue-star shortcut and replaces it with a finite-dimensional penalty compatible with the Diaz configuration model.

## 9. Why I do not claim a new decimal upper bound yet

There are two distinct remaining issues.

First, even within the historical Diaz architecture, a new density below `4.4898` requires rerunning or bounding the complete outer optimization as the impure-core degree and clause-type data vary with density. The strict penalty at the published interior maximizer is not by itself a certified decimal endpoint.

Second, the 2026 literature status means that merely shaving `4.4898` is not enough to improve the strongest theorem-form upper mechanism: interpolation already supplies the 1RSB upper functional, numerically reported near `4.267`. Therefore spending the next run only squeezing another fourth decimal out of Diaz would be strategically misaligned unless the matching penalty transfers to the interpolation/cover functional.

The source transfer is therefore labeled **CONDITIONAL / NOT YET A THRESHOLD IMPROVEMENT**.

## 10. Next attack

The next run should pursue one of two source-relevant continuations, preferring the first.

1. **Lift the matching penalty to a cover/1RSB-compatible order parameter.** The degree-one anchored pairs are local cluster witnesses, and the exact `2^{-E}` factor should appear as an extra entropy cost in a cover-count or 1RSB trial measure. Derive the corresponding correction to the rigorous interpolation upper functional at `k=3`; this is the route capable of improving the strongest supported upper mechanism.
2. **Numerically certify the existing interpolation functional at `k=3`** with rigorous intervals, turning the literature-reported `d≈12.801` / `alpha≈4.267` into an explicit decimal theorem endpoint before attempting a further correction.

Do not return to arbitrary rescue stars, the clause-local weighted second moment, submesoscopic ball quotients, or whitening-history multiplicity without a new obstruction-removing idea.

## ledger_delta

```yaml
worker: NM13-13
parent: T04
status: OPEN_PARTIAL
runtime_model: GPT-5.6 Sol
runtime_reasoning: UNVERIFIED
source_explicit_decimal_before: "[3.52,4.4898]"
source_explicit_decimal_after: "[3.52,4.4898]"
source_endpoint_movement: NONE
source_status_correction: "fixed-k=3 uniform threshold existence remains open; rigorous interpolation/1RSB upper functional is stronger in theorem form, with literature-reported physics evaluation near alpha=4.267 but not independently interval-certified here"
mechanism_gain: "proved anchored degree-one rescue matching and strict two-coordinate variational correction Delta(z)<0 on interior Diaz types"
finite_core: "exact local clause check + exact hypergeometric identity/Maclaurin check; ALL_EXACT_CHECKS_PASS=True"
companion: "NM13-06 remains constructive majority/two-choice repair; no duplication"
next: "transfer matching penalty to 1RSB/cover interpolation or rigorously interval-certify the k=3 interpolation functional"
```
