Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.**

# NM13-13 / T04 — exponential-cell Radau correction and survey-averaged density transfer

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Status: **OPEN / PARTIAL; published source bracket unchanged; project upper candidate strictly improved; CANDIDATE_FULL pending later independent review**

## 0. Short handoff and strongest supported baseline

The controlling owner directive is `operations/PROGRESS20_2026-09-20.md`. NM13-13 owns T04 cluster-aware / variational threshold bounds; NM13-06 is the constructive companion. This run read only the controlling LIVE20 policy, `operations/claims/PROB10-04.md`, root `POSTED.md`, the latest own substantive report, and the latest relevant NM13-06 T04 reports.

The directly recovered published explicit-decimal bracket for classical iid random 3-SAT with independent fair signs on three distinct variables remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52`; Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at `4.4898`. Carenini's 16 August 2026 scaling-window theorem gives an `O(n/log n)` window for each fixed `k>=3` but does not locate the fixed-`k=3` center. Large-`k` threshold theorems, sharp-window existence, k-wise-independent variants, and cavity/replica numerics do not settle this exact iid `k=3` target.

Hence the **published-source bracket is unchanged**:

\[
\boxed{[3.52,4.4898]\to[3.52,4.4898]}.
\]

The strongest project candidate before this run is the preceding NM13-13 density-transfer certificate

\[
\alpha_{\rm prev}=4.38885875992,
\]

which itself starts from NM13-06's exact outer-boundary-layer seven-support survey at `alpha0=4.38885876`. The later NM13-06 seven-support nested report at `4.38886058` is weaker numerically and therefore does not replace this baseline.

This run proves strict negativity of the same hard-field coefficient at

\[
\boxed{
\alpha_1={2194429378461\over500000000000}=4.388858756922,
}
\]

so, subject to the inherited interpolation-to-source transfer surviving independent review, the **project CANDIDATE_FULL bracket** moves

\[
\boxed{[3.52,4.38885875992]\to[3.52,4.388858756922]}.
\]

The explicit endpoint gain is

\[
\boxed{2.998\times10^{-9}}.
\]

This is kept separate from the mechanism gains below. It is not promoted to a published theorem and does not prove existence of the limiting threshold.

## 1. Exact parked failures preserved

The following predecessor failures remain parked rather than being relabeled as progress.

* Arbitrary rescue stars do not compose; anchored degree-one rescue matching still lacks a full global Díaz-polytope reoptimization.
* Positive clause-local multiplicative second moments meet the identical-pair obstruction near `3.10628...`.
* Quotienting by sublinear solution balls yields only `e^{o(n)}` savings; full-component quotienting leaves an uncontrolled cross-component overlap moment.
* Whitening/core counting still lacks a uniform exponential cluster-multiplicity theorem.
* The q-binomial radius-two route reached only about `4.5923`; the equal-weight two-support hard-field family stalled near `4.4178`.
* On the constructive companion route, independent one-shot zero-break thinning has a positive residual-density obstruction. A/B menus are union-closed, so the old global menu-disjointness surrogate was too strong. The exact A/B/C/D normal form leaves finite-density C-promotions and D-forbidden triples as the globalization obstruction. Absorption-aware cascades and four-spectrum identities have not produced a source-valid terminal lower-bound margin above `3.52`.

No item above is claimed resolved here.

## 2. Inherited hard-field coefficient and archived nested correction

For the exact symmetric seven-support survey

\[
R\in\left\{
{7\over200000},{651\over100000},{789\over10000},{1\over2},
{9211\over10000},{99349\over100000},{199993\over200000}
\right\}
\]

with weights

\[
\left\{
{147\over100000},{2717\over50000},{3669\over20000},{13037\over25000},
{3669\over20000},{2717\over50000},{147\over100000}
\right\},
\]

the project hard-field coefficient is

\[
A(\alpha,\nu)=E\log(1-QQ')-2\alpha E\log(1-R_1R_2R_3).
\tag{2.1}
\]

NM13-06's immutable outward-interval checker at

\[
\alpha_0={109721469\over25000000}=4.38885876
\]

certified, after the base eleven-interior-node left-Radau rule but before the secondary positive correction,

\[
B_{\rm base}^{\rm hi}
=1.598545065794609960668504250300780096891114046697565\times10^{-7},
\]

and a secondary Christoffel/Gauss/Riemann correction lower bound

\[
C_{\rm Riem}^{\rm lo}
=1.610642812100063864766410939010528071371412619274617\times10^{-7}.
\]

The preceding NM13-13 run used only a first-order tangent improvement, multiplying this correction by `1.008`, and obtained

\[
A(\alpha_0,\nu)\le-2.4982888802254415\times10^{-9}.
\]

The present run strengthens both the correction and the density transfer analytically.

## 3. New lemma I: exponential-cell lower envelope

For each secondary Gaussian node `z`, the archived correction integrand is

\[
f_z(t)=\frac{e^{-Nt}}
{\prod_{i=1}^{11}(1-x_i e^{-t})^2(1-z e^{-t})},
\qquad N=2323.
\tag{3.1}
\]

Its logarithmic decay rate is

\[
D_z(t):=-{f_z'(t)\over f_z(t)}
=N+2\sum_{i=1}^{11}{x_i e^{-t}\over1-x_i e^{-t}}
+{z e^{-t}\over1-z e^{-t}}.
\tag{3.2}
\]

Every summand is decreasing in `t`, so `D_z(t)` is decreasing. The archived root brackets have radius `1e-24`. This run replaces the previous three-decimal outer ceilings by six-decimal rational ceilings and proves exactly, from the alternating series for `e^{-1/50}`, that

\[
e^{-0.02}>0.98019867.
\]

Substitution into (3.2) yields the rigorous uniform bound

\[
\boxed{D_z(t)\ge D_* >3244.5491713643045}
\tag{3.3}
\]

for every certified base/secondary node and every `0<=t<=0.02`.

On a right-Riemann cell `[b-h,b]`, `h=5\times10^{-6}`, for `0<=s<=h`,

\[
\log {f_z(b-s)\over f_z(b)}
=\int_{b-s}^{b}D_z(t)\,dt\ge D_*s.
\]

Therefore

\[
\int_{b-h}^{b}f_z(t)\,dt
\ge f_z(b){e^{D_*h}-1\over D_*}.
\tag{3.4}
\]

The verifier does not invoke a floating exponential: with `x=D_*h` it lower-bounds

\[
{e^x-1\over x}
\]

by the first seven positive Taylor terms and obtains the exact rational factor

\[
\boxed{F_{\rm cell}\ge1.0081554143152433759713536396478\ldots}.
\tag{3.5}
\]

All weights and prefactors in the archived correction are positive, so the entire archived `C_Riem` may be multiplied by this factor. Consequently

\[
\boxed{
A(4.38885876,\nu)
\le -2.52332057519986119119\times10^{-9}.
}
\tag{3.6}
\]

Relative to the preceding tangent certificate, the demonstrated same-density gain is at least

\[
\boxed{2.50316949744197\times10^{-11}}.
\]

This is a genuine lower-envelope improvement of the complete-tail certificate, not a deeper moment truncation or a new survey fit.

## 4. New lemma II: survey-averaged one-sided density derivative

The preceding density transfer bounded every extra compound-Poisson mark by the worst possible mark cost, giving the crude constant `28.8`. The finite survey permits an expectation-level bound instead.

Write

\[
F(Z,Z')=\log(Z+Z'-ZZ')
\]

for the first term in (2.1). Couple `alpha_0=alpha_1+delta` by adding independent Poisson marks of mean `(3/2)delta` to each of the two literal copies. One added mark multiplies one copy of `Z` by

\[
s=1-R_1R_2.
\]

If that mark is added to the first copy, then

\[
{ sZ(1-Z')+Z'\over Z(1-Z')+Z'}\in[s,1].
\]

Thus removing that mark can increase `F` by at most

\[
-\log(1-R_1R_2).
\]

Telescope over all extra marks and take expectation. Since the expected total number of extra marks across the two copies is `3 delta`,

\[
E F_{\alpha_1}-E F_{\alpha_0}
\le 3\delta M,
\qquad
M:=E[-\log(1-R_1R_2)].
\tag{4.1}
\]

Now put

\[
J:=E[-\log(1-R_1R_2R_3)]>0.
\]

The clause contribution to `A` is `2 alpha J`, hence lowering density helps exactly by `2 delta J`. Combining this with (4.1) gives the new one-sided variational inequality

\[
\boxed{
A(\alpha_1,\nu)-A(\alpha_0,\nu)
\le \delta\,(3M-2J).
}
\tag{4.2}
\]

This is strictly stronger than a worst-mark Lipschitz bound and is valid for any fixed finite survey for which `M<infinity`.

## 5. Exact rational bounds for the new density constant

The verifier bounds `M` entirely by exact rational inequalities. For each of the 49 rational products `p=R_iR_j`, it chooses a `1e-8` rational ceiling `C_{ij}` and proves

\[
e^{C_{ij}}>{1\over1-p}
\]

using a finite positive Taylor polynomial (maximum degree 35). Therefore

\[
-\log(1-p)<C_{ij}
\]

without relying on floating logarithms. Weighting those 49 exact inequalities gives

\[
\boxed{M\le0.379005821217658468}.
\tag{5.1}
\]

For the helpful clause drift, positivity of the logarithmic series and independence give

\[
J=\sum_{m\ge1}{(E R^m)^3\over m}
\ge\sum_{m=1}^{50}{(E R^m)^3\over m},
\]

and exact rational arithmetic yields

\[
\boxed{J\ge0.1586777008235910400205384155264\ldots}.
\tag{5.2}
\]

Hence

\[
\boxed{
3M-2J
\le0.8196620620057933239589231689471\ldots <0.82.
}
\tag{5.3}
\]

The old transfer constant was `28.8`; the new certified constant is smaller by a factor greater than `35`. This is the main mechanism gain of the run.

## 6. Strict project-endpoint improvement

Take

\[
\delta={3078\over10^{12}}=3.078\times10^{-9},
\qquad
\alpha_1=\alpha_0-\delta
={2194429378461\over500000000000}
=4.388858756922.
\]

Using (3.6) and (5.3), the exact verifier obtains transfer penalty

\[
\le2.5229198268538318511455655140190\times10^{-9},
\]

and therefore

\[
\boxed{
A(4.388858756922,\nu)
\le -4.00748346029340048\times10^{-13}<0.
}
\tag{6.1}
\]

The previous project candidate was `4.38885875992`, so the strict endpoint gain is exactly

\[
\boxed{4.38885875992-4.388858756922=2.998\times10^{-9}}.
\]

The executed artifact ends with

`CERTIFIED_EXPONENTIAL_CELL_GAIN = True`,  
`CERTIFIED_AVERAGED_LIPSCHITZ = True`,  
`CERTIFIED_STRICT_DENSITY_IMPROVEMENT = True`.

## 7. Transfer to the exact iid proper-clause model and status

The interpolation-to-random-3-SAT transfer is inherited unchanged from the current candidate chain: strict hard-field negativity is pulled back to finite interpolation parameters; the `p=3` interpolation remainder has the required sign; concentration gives linear minimum violated-clause energy in the Poisson with-replacement model; repeated-variable clauses contribute only `O_p(1)`; and same-density de-Poissonization changes the proper-clause count by only `O_p(sqrt(n))`, which cannot erase linear energy.

Subject to that inherited transfer surviving later independent review, (6.1) gives the project candidate theorem

\[
\boxed{
\Pr[\Phi_{n,\lfloor4.388858756922n\rfloor}\text{ is satisfiable}]\to0.
}
\]

Status remains **CANDIDATE_FULL pending later independent review**. No limiting-threshold existence claim is made, and no replica/cavity prediction is treated as proved.

## 8. Complementarity with NM13-06 and next attack

NM13-06 remains complementary. Its constructive lower-bound route still has the finite-density C-promotion / D-forbidden-triple globalization obstruction; its upper-side survey work supplied the seven-support boundary-layer law used here. This run does not alter that survey or overwrite the companion files. It extracts more value from the same certified law through a stronger complete-tail cell inequality and an expectation-level density coupling.

The next upper-side attack should use the same principle at the functional level rather than another decimal-only transfer: derive a differentiable or convex envelope for `alpha -> A(alpha,nu)` from the compound-Poisson generator, including the exact average mark cost as the law evolves, or optimize a new survey against the certified derivative bound. If three substantive runs fail to move a mathematical quantity, switch to a distinct overlap/cluster-count route as required by the owner directive.

## 9. Essential executed artifacts

Verifier source:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T16-58-01Z__t04_expcell_averaged_density_transfer_verifier.py`

created at commit `5bef94c84df7abc41ab68cbd93a9035ce611defc`.

Actual executed stdout:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T16-58-01Z__t04_expcell_averaged_density_transfer_verifier.out`

created at commit `de1a5a37799800e4c13a2b16d10b6f9179e9db1`.
