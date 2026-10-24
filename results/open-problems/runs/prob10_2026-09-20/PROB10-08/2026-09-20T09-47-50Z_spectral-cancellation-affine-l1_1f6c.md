Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime telemetry establishes that model/effort setting.

# PROB10-08 — spectral positivity/cancellation barrier and sharper affine `L1` geometry

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL / substantive mechanism movement / no new source-level cutoff class this run / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Contract, continuity, ownership, and consumed state

The exact source remains Justin Salez, arXiv:2508.21055v1, Problem 2.3: every bounded-degree vertex-transitive spectral-expander sequence should exhibit total-variation cutoff for the source's rate-one continuous-time SRW convention `H_t=e^{t(P-I)}`. This is not the posted Abelian Cayley/product-condition target.

Before the new attack I recovered the required state rather than resetting I0112:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved pre-refocus successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`;
- R16 stuck-recovery history, especially `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, which records the already-failed product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature, local-limit/AEP and subcommutation routes;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T08-46-43Z_affine-outlier-l1-interpolation_b72f.md`, blob `b892fa52e9638c4eeaec1a322579162152dd6469`;
- neighboring P26 cutoff-transfer report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`, blob `fd122a821741be5930402d33bed302d43a6f9544`; P26 owns the Green-shell/biregular-halving route;
- neighboring NM13 cutoff report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`, blob `1c033f20afeaee2d9e1e5b1028afc45e3bd9a01c`; NM13 owns arc/Hodge/reversal/orbit routes.

The R16/H0002 handoff remains intact: the actual successor is Christoph--Morawski--Wigderson Question 5.1 with the all-prefix isotonic/KKT obstruction. This PROB10 refocus does not erase or reassign it.

## 1. Current primary-source boundary

I re-read the current Altschuler proof, arXiv:2609.14945, and refreshed its current record/correction status. The bounded check still exposes **v1, submitted 14 September 2026**; no v2, correction, or erratum surfaced.

The exact LRE dependency remains localized before spectral cleanup:

1. Lemma 3.2 transfers long-range vertex growth to the oriented-edge NBRW state space;
2. Lemma 3.3 converts that maximal-rate set growth to Shannon entropy;
3. Proposition 3.1 obtains NBRW endpoint entropy `log n-O(log log n)`;
4. only then does ordinary spectral expansion clean the residual entropy deficit into TV mixing.

Thus Altschuler supplies the right target mechanism but does **not** show that transitivity plus spectral expansion implies the needed entropy growth. His theorem remains a baseline, not a new R16 result.

## 2. Why a different method was mandatory

The frozen R16 metric is already at its possible exponent floor `W_exp=1/2 provisional`, and several consecutive runs have not moved the source-level scope. Repeating another Green/superlevel sufficient criterion would violate the stuck rule. The preceding affine run instead left a concrete unresolved issue: the slow high-multiplicity spectral block had a first polynomial `L1` rarity estimate, but it was unclear what spectral positivity alone can force and whether the special affine estimate could be materially sharpened.

This run therefore changes category from heat-kernel superlevel relations to **signed spectral-projector cancellation**.

## 3. Main new theorem — positivity forces cancellation of an isolated slow block

Let a finite connected regular graph on `n` vertices have normalized generator `L=I-P`. Suppose the smallest positive relaxation rate is `lambda>0`, with orthogonal spectral projector `Pi`, while all remaining positive rates are at least `lambda+Delta`, `Delta>0`. Define

\[
A_x=\sum_y|\Pi(x,y)|.
\]

The matching proof artifact proves

\[
\boxed{
A_x\le 4n^{\lambda/[2(\lambda+\Delta)]}.
}
\tag{3.1}
\]

The proof is short but structural. Decompose

\[
H_t(x,y)=n^{-1}+e^{-\lambda t}\Pi(x,y)+R_t(x,y).
\]
Because the projector row has total sum zero, its negative entries have total mass `A_x/2`. Heat-kernel positivity therefore forces the faster remainder to cancel at least

\[
e^{-\lambda t}A_x/2-1
\]
of positive mass on the negative set. Spectral separation gives the opposing estimate

\[
\|R_t(x,\cdot)\|_1\le\sqrt n\,e^{-(\lambda+\Delta)t}.
\]
Choosing `t=lambda^{-1} log(A_x/4)` gives (3.1).

**Meaning.** An isolated high-multiplicity slow eigenspace is not a positive Markov component. If its projector has polynomial `L1` rows, the faster spectrum must cancel its negative part for logarithmic time. Therefore spectral separation plus `L2` estimates alone cannot decide TV behavior; one needs signed-cancellation, matrix-coefficient `L1`, Shannon information, or another positivity-sensitive input.

This is an obstruction theorem, not a new sufficient criterion and not source closure.

## 4. Exact affine improvement — the projection loss is 18, not 20

For the Haiman--Schildkraut--Zhang--Zhao 18-regular affine family

\[
\Gamma_q=\operatorname{SL}(2,q)\ltimes\mathbb F_q^2,
\qquad r=q^2,
\]
the predecessor used the bulk `L2` bound

\[
\beta=2+4\sqrt7=12.583005\ldots
\]
and a crude compressed `L1` norm `20+o(1)`.

For the normalized point contrast `u_0`, if `g` has mean zero then

\[
(P_Wg)(0)=0,
\qquad
(P_Wg)(x)=g(x)+\frac{g(0)}{r-1}\quad(x\ne0).
\]
Hence

\[
\boxed{\|P_Wg\|_{1,\pi}\le\|g\|_{1,\pi}},
\]
and since the full adjacency is a sum of 18 permutations,

\[
\boxed{\|C_W\|_{1\to1}\le18.}
\tag{4.1}
\]

A separate two-dimensional Rayleigh test on the point contrast and its translation perturbation gives

\[
\boxed{
\mu_q\ge\mu_0-o(1),
\quad
\mu_0=
\frac{16-\beta+\sqrt{(16+\beta)^2+8}}2
=16.0698011904\ldots .
}
\tag{4.2}
\]

Interpolating (4.1) with the bulk `L2` bound and solving the exact `L^p` resolvent equation yields the sharpened actual-eigenvector theorem:

\[
\boxed{
\|u\|_{1,\pi}=O_\eta(r^{-\eta})
\quad\forall\eta<\eta_{\rm aff},
}
\]
where
\[
\boxed{
\eta_{\rm aff}
=\frac{\log(\mu_0/\beta)}{2\log(18/\beta)}
=0.3415891874\ldots .
}
\tag{4.3}
\]

The predecessor had only `0.2592245387...`.

By transitivity,

\[
\mathbb E_g|\langle u,\phi_q(g)u\rangle|
\le\|u\|_{1,\pi}^2,
\]
so every matrix-coefficient exponent below

\[
\boxed{2\eta_{\rm aff}=0.6831783749\ldots}
\]
is certified for the **actual** slow eigenvector.

Using the already-established multiplicity and decay-rate bounds, the whole slow Peter--Weyl block is TV-negligible by

\[
\boxed{t=(3.825774+o(1))\log r,}
\tag{4.4}
\]
versus the predecessor's `5.814959... log r`. The crude separated-bulk `L2` bound becomes negligible only by

\[
(4.153595+o(1))\log r.
\]
Thus the high-multiplicity slow outlier is **no longer the bottleneck of this spectral upper-bound route**. This still is not a cutoff theorem: neither constant is claimed to be the mixing location and no matching lower TV profile is proved.

## 5. Applying the positivity theorem to the affine stress family

The affine slow rate is `delta_q=1-mu_q/18`, while the separated bulk rate is at least

\[
\gamma_{\rm bulk}=1-\beta/18=0.3009441531\ldots .
\]
The new positivity theorem alone allows a slow-projector row `L1` amplitude of polynomial size; using (4.2) it permits roughly

\[
N^{0.1782\ldots}=r^{0.4455\ldots+o(1)}.
\]
The special affine geometry improves this to `r^{0.316822+o(1)}` through (4.3), but it remains polynomial. This cleanly identifies why a generic spectral argument cannot finish the family: positivity enforces cancellation, not bounded `L1` mass.

## 6. Third approach — Renyi interpolation is provably insufficient

I also tested whether the old polynomial Green/collision excess could be repaired by moving from order-two entropy toward Shannon through Renyi order `1+theta`.

If `L=np` is a likelihood ratio under the uniform law and

\[
R=E[L^2]=n\sum p_i^2,
\]
then for every `0<theta<=1`, moment interpolation gives

\[
E[L^{1+\theta}]\le R^\theta,
\]
so

\[
\boxed{
D(p\|u)\le D_{1+\theta}(p\|u)\le\log R.
}
\tag{6.1}
\]
There is no small factor as `theta` tends to zero. Equality occurs when `p` is uniform on a subset, for which all Renyi divergences equal `log R`. Therefore merely choosing a fractional Renyi order cannot turn polynomial collision excess into the `o(log n)` Shannon deficit needed for cutoff. This route is now explicitly closed unless extra structure is inserted.

## 7. Three materially different approaches compared

1. **Signed spectral positivity/cancellation — retained.** Gives the exact universal barrier (3.1) and explains why a slow projector cannot be treated as a positive component.
2. **Affine special-geometry `L^p` resolvent — retained as auxiliary movement.** Exact `L1` contraction plus a better Rayleigh lower bound improves the true slow-mode exponent and removes that block as the current affine spectral bottleneck.
3. **Fractional-Renyi interpolation from Green/L2 — rejected.** The uniform-subset equality case proves no entropy gain is possible from collision information alone.

These routes do not duplicate P26's Green-shell/biregular halving or NM13's arc/Hodge/reversal constructions, and they do not restart the old R16 product/Poincare/tensor routes.

## 8. Source before/after and metrics

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  new_complete_cutoff_class_this_run: false
  mechanism_progress:
    - "isolated-slow-block positivity/cancellation theorem A_x <= 4 n^{lambda/(2(lambda+Delta))}"
    - "affine compressed L1 bound sharpened from 20+o(1) to 18"
    - "actual affine slow eigenvector exponent improved 0.259224... -> 0.341589..."
    - "slow affine Peter-Weyl block no longer bottleneck of current crude spectral upper route"
    - "fractional Renyi interpolation from collision proved insufficient without additional structure"
  independent_audits: 0
  worldwide_novelty: "UNVERIFIED"
```

The unchanged source metric is intentional: no new complete source-admissible class with a proved TV cutoff is being promoted merely from an auxiliary spectral estimate.

## 9. Tests actually run

No finite mixing plots, graph enumeration, Monte Carlo simulation, or finite-size extrapolation was used. The new statements are analytic and have no finite computational core. Calculator-level floating-point evaluation was used only for displayed constants; the arguments themselves are symbolic.

## 10. Matching artifact and readback

Full proof artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T09-47-50Z_spectral-cancellation-affine-l1_1f6c.md`

created at commit

`076ca200e73ef0180da56b82998efb05e164abcc`,

blob

`9f24e37734e307113a3c072cda6e679cf5e453b8`,

and read back at that exact commit before this report write.

## 11. Remaining full-scope gap

The source-level missing statement is unchanged but sharper: obtain a **Shannon/typical-mass estimate from vertex transitivity plus ordinary spectral expansion alone**, or construct an admissible counterexample sequence. The new positivity theorem shows why isolated spectral information cannot substitute for that estimate. For the affine stress family specifically, the next nonduplicating target is an `L1`/entropy treatment of the separated bulk plus a matching TV profile, rather than another global `L2` bound.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, workflow, shared ledger, peer-track file, or force push was changed.
