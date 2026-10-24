Model actually run: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-13 / T04 — tangent-corrected nested Radau tail and strict density transfer

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Status: **OPEN / PARTIAL; source-published bracket unchanged; project upper candidate strictly improved; CANDIDATE_FULL pending later independent review**

## 0. Short handoff, current ownership, and exact baseline

The controlling owner directive is `operations/PROGRESS20_2026-09-20.md`: NM13-13 owns T04 cluster-aware/variational threshold bounds and NM13-06 is the constructive companion. I read the current LIVE20 mapping and the latest relevant T04 commits only.

The important current-master handoff is the NM13-06 report `2026-09-20T18-26-20__t04_outer_boundary_layer_upper.md`, commit `30189fe101e4ce440aa8666be71f9ea1c950b4bc`. It supersedes NM13-13's preceding `4.38886077` candidate and rigorously certifies, at the project-functional level, the exact seven-support survey at

\[
\alpha_0=\frac{109721469}{25000000}=4.38885876
\]

with archived outward-interval upper value

\[
A(\alpha_0,\nu)\le -1.20977463054539040979\times 10^{-9}.
\]

That companion run also produced a much more polarized outer boundary layer; this report does not overwrite it. Instead it strengthens the **same** complete-tail lower bound analytically and then transfers the extra margin to a strictly smaller density.

## 1. Source threshold before / after, separate from the project candidate

The strongest directly recovered published explicit-decimal bracket for classical iid proper random 3-SAT remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin (`math/0310193`) prove satisfiability w.h.p. below `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez (`arXiv:0807.3600`) prove a.a.s. unsatisfiability at density `4.4898`. Carenini, ECCC TR26-145, published 16 August 2026, proves an `O(n/log n)` scaling window for each fixed `k>=3` but does not locate the `k=3` center. Large-`k` threshold theorems, sharp-window existence and k-wise-independent variants therefore do not settle this target. Replica/cavity numbers remain conjectural here.

Hence the **published-source explicit-decimal bracket is unchanged**:

\[
\boxed{[3.52,4.4898]\to[3.52,4.4898]}.
\]

Separately, under the inherited project interpolation transfer, the strongest project candidate before this run is

\[
[3.52,4.38885876].
\]

This run proves strict negativity of the same hard-field functional at

\[
\boxed{\alpha_1=\frac{54860734499}{12500000000}=4.38885875992},
\]

so the **project CANDIDATE_FULL bracket** moves

\[
\boxed{[3.52,4.38885876]\to[3.52,4.38885875992]}.
\]

The explicit endpoint gain is

\[
\boxed{8\times10^{-11}}.
\]

This is deliberately stated separately from the much larger same-density mechanism gain below. It is not promoted to an externally certified theorem and does not prove existence of the limiting `k=3` threshold.

## 2. Exact parked failures preserved

The following predecessor failures remain parked rather than being recycled as progress.

* Arbitrary rescue stars do not compose; anchored degree-one rescue matching still lacks a full global Díaz-polytope reoptimization.
* Positive clause-local multiplicative second moments meet the identical-pair obstruction near `3.10628...`.
* Quotienting by sublinear solution balls yields only `e^{o(n)}` savings; full-component quotienting leaves an uncontrolled cross-component overlap moment.
* Whitening/core counting still lacks a uniform exponential cluster-multiplicity theorem.
* The q-binomial radius-two route reached only about `4.5923`; the equal-weight two-support hard-field family stalled near `4.4178`.
* On the constructive companion route, independent one-shot zero-break thinning has a positive residual-density obstruction. A/B menus are union-closed, so the old global menu-disjointness surrogate was too strong. The exact A/B/C/D normal form leaves finite-density C-promotions and D-forbidden triples as the globalization obstruction. Absorption-aware cascades and four-spectrum identities have not yet produced a source-valid terminal margin above `3.52`.

No failure above is claimed resolved by this run.

## 3. Inherited nested product-tail certificate

For the fixed symmetric seven-support survey from NM13-06, the project hard-field coefficient is

\[
A(\alpha,\nu)=E\log(1-QQ')-2\alpha E\log(1-R_1R_2R_3).
\]

The companion certificate truncates the squared Hausdorff-moment series at `K=2300`, applies an eleven-interior-node left Gauss--Radau rule to the `X=QQ'` tilted law, and lower-bounds the Christoffel remainder by a four-node Gaussian rule for a secondary law plus a positive right-Riemann integral. Its archived interval output gives

\[
B_{\rm base}^{\rm hi}=1.598545065794609960668504250300780096891114046697565\times10^{-7}
\]

for the upper value *before* the secondary correction, and

\[
C_{\rm Riem}^{\rm lo}=1.610642812100063864766410939010528071371412619274617\times10^{-7}
\]

for the secondary positive correction. Thus the old upper certificate is `B_base^hi-C_Riem^lo`.

The present run strengthens only this last Riemann step. All Radau/Hankel/root/weight/moment checks remain the companion's immutable outward-interval certificate.

## 4. New lemma: tangent correction to every Riemann cell

For each secondary Gaussian node `z` the correction integrand in the archived checker is

\[
f_z(t)=\frac{e^{-Nt}}
{\prod_{i=1}^{11}(1-x_i e^{-t})^2(1-z e^{-t})},
\qquad N=K+2R+1=2323.
\tag{4.1}
\]

Every factor has a nonnegative exponential-series expansion, hence

\[
f_z(t)=\sum_{m\ge0}c_m e^{-(N+m)t},\qquad c_m\ge0.
\]

Therefore `f_z` is decreasing and convex. More precisely

\[
-\frac{f_z'(t)}{f_z(t)}
=N+2\sum_{i=1}^{11}\frac{x_i e^{-t}}{1-x_i e^{-t}}
+\frac{z e^{-t}}{1-z e^{-t}}.
\tag{4.2}
\]

The archived checker certifies root brackets of radius `1e-24` about its listed base and secondary centers. Replacing those centers by the following **coarser outward rational ceilings** for the scaled base roots,

`0.109, 0.390, 0.854, 1.512, 2.378, 3.472, 4.828, 6.496, 8.554, 11.155, 14.692`,

and by `20.459` for the largest secondary root, is therefore valid. On the whole Riemann range `0<=t<=0.02`,

\[
e^{-t}\ge e^{-0.02}>\frac{49}{50},
\]

because `-log(49/50)>1/50`. Substitution in (4.2), performed exactly by the preserved verifier, gives

\[
-\frac{f_z'}{f_z}>3236.6622\ldots>3200
\tag{4.3}
\]

uniformly for every base/secondary node used by the certificate.

Now let one Riemann cell be `[b-h,b]` with `h=5\times10^{-6}`. Convexity puts the tangent at the right endpoint below the graph:

\[
\int_{b-h}^{b}f_z(t)\,dt
\ge h f_z(b)-\frac{h^2}{2}f_z'(b).
\]

Using (4.3),

\[
\boxed{
\int_{b-h}^{b}f_z(t)\,dt
\ge h f_z(b)\left(1+\frac{3200h}{2}\right)
=1.008\,h f_z(b).
}
\tag{4.4}
\]

All outer prefactors and secondary Gaussian weights in the companion correction are positive. Hence the **entire archived Riemann correction lower bound may be multiplied by `1.008`** without rerunning or modifying the Radau solve.

This is a strict variational/numerical inequality improvement, not a deeper truncation and not a new survey fit.

## 5. Demonstrated same-density mechanism gain

Using the archived outward interval endpoints and (4.4),

\[
A(\alpha_0,\nu)
\le B_{\rm base}^{\rm hi}-1.008\,C_{\rm Riem}^{\rm lo}
\]

and the exact-arithmetic verifier obtains

\[
\boxed{
A(4.38885876,\nu)
\le -2.49828888022544150160\times10^{-9}.
}
\tag{5.1}
\]

Relative to the archived upper value, the **same-density certificate-objective gain** is at least

\[
0.008\,C_{\rm Riem}^{\rm lo}
=\boxed{1.28851424968005109181\times10^{-9}}.
\tag{5.2}
\]

This mechanism gain is more than sixteen times the final density-endpoint movement when both are compared as raw decimal numbers; they are not the same metric and are not conflated.

## 6. New one-sided density-Lipschitz lemma

It remains to convert the extra margin into an explicit smaller density without fabricating an uncomputed interpolation value.

Let `alpha_1<alpha_0` and couple the two compound-Poisson constructions by taking the `alpha_0` process to be the `alpha_1` process plus independent extra marks of rate

\[
\Delta\lambda=\frac32(\alpha_0-\alpha_1)
\]

in each copy. Write `Z=1-Q`, `Z'=1-Q'` and

\[
F(Z,Z')=\log(Z+Z'-ZZ').
\]

Adding one mark to the first copy replaces `Z` by `sZ`, where `s=1-R_1R_2`. The ratio of the new and old logarithm arguments is

\[
\frac{sZ(1-Z')+Z'}{Z(1-Z')+Z'}\in[s,1].
\]

Thus one mark changes `F` by at most `-log s`. For the present survey

\[
s\ge s_{\min}=1-(199993/200000)^2=\frac{2799951}{40000000000}.
\]

The verifier proves exactly that `-log s_min<48/5=9.6`: the first six terms of the exponential series give `e^{4/5}>89/40`, and `(89/40)^12>1/s_min`.

There are two independent copies, so the expected number of extra marks is `3(alpha_0-alpha_1)`. Therefore

\[
E F_{\alpha_1}-E F_{\alpha_0}
\le \frac{144}{5}(\alpha_0-\alpha_1).
\tag{6.1}
\]

The clause term needs no absolute-value penalty: if

\[
L=E\log(1-R_1R_2R_3)<0,
\]

then lowering `alpha` changes `-2 alpha L` **downwards**. Hence the full coefficient obeys the one-sided bound

\[
\boxed{
A(\alpha_1,\nu)-A(\alpha_0,\nu)
\le \frac{144}{5}(\alpha_0-\alpha_1).
}
\tag{6.2}
\]

Take

\[
\delta=\alpha_0-\alpha_1=8\times10^{-11}.
\]

Then the transfer penalty is at most

\[
\frac{144}{5}\delta=2.304\times10^{-9}.
\]

Combining with (5.1),

\[
\boxed{
A(4.38885875992,\nu)
\le -1.9428888022544150\times10^{-10}<0.
}
\tag{6.3}
\]

This completes the strict functional-level endpoint improvement without treating an unknown baseline as zero and without numerical extrapolation in density.

## 7. Transfer to classical iid proper random 3-SAT and status

The source-model transfer is inherited, not newly audited here: strict hard-field negativity is pulled back to finite interpolation parameters; the `p=3` interpolation remainder has the required sign; concentration yields linear minimum violated-clause energy in the Poisson with-replacement model; repeated-variable clauses contribute only `O_p(1)`; and same-density de-Poissonization changes the proper clause count by only `O_p(sqrt(n))`, which cannot erase linear energy.

Subject to that inherited transfer surviving later independent review, (6.3) gives the project candidate theorem

\[
\boxed{
\Pr[\Phi_{n,\lfloor4.38885875992n\rfloor}\text{ is satisfiable}]\to0.
}
\]

Status remains **CANDIDATE_FULL pending later independent review**. No limiting-threshold existence claim is made.

## 8. Companion NM13-06 and next attack

NM13-06 remains complementary. Its current constructive obstruction is finite-density control of C-promotions and D-forbidden triples, while its newest upper-side contribution is the seven-support outer boundary layer used here. This report adds a grid-cell tangent minorant plus a density-stability transfer; it does not duplicate the companion's survey search.

The next worthwhile upper-side attack is to replace the first-order tangent correction by a certified exponential-cell lower bound using the full node-dependent logarithmic derivative, or to rebuild the secondary correction with an analytically integrated positive exponential expansion. Either would strengthen the complete-tail functional before another survey reoptimization. If repeated endpoint gains become numerically stagnant for three substantive runs, switch to an overlap/cluster-count route rather than continue decimal polishing.

## 9. Essential executed artifacts

Verifier source:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T15-54-26Z__t04_tangent_transfer_verifier.py`

created at commit `9a14f889078f4c13e205b76d67086fcff264a330`.

Actual executed stdout:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T15-54-26Z__t04_tangent_transfer_verifier.out`

created at commit `3fadf0c05fc2b212218bf0b660060496ec583f90`.

The verifier checks the coarse root ceilings, the exact rational `D>3200` inequality, the exact `1.008` tangent factor, the rational proof of `-log s_min<9.6`, the same-density strengthened upper value, and the explicit downward-density transfer to `4.38885875992`.
