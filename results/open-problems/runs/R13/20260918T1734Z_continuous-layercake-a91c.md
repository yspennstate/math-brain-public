Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** the previous certified envelope at `n=86` had value at least `7507/1000=7.507`, while the new envelope satisfies `B_R13(86) <= 148709/20000 = 7.43545`, an improvement of at least `1431/20000=0.07155`. Methods: **#3 PROVE SOMETHING STRONGER, #5 ADD A PARAMETER AND DIFFERENTIATE/VARY IT, #30 ONE SCALE/DIRECTION AT A TIME.**

# R13 — continuous layer-cake directional-TV sharpening

Repository/branch: private `yspennstate/math-open-problems` / `master`. R13 remains the exclusive HARD OUTSIDE owner of intake `E0042`, the real Boolean Komlos problem. The target is

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty
\]

for arbitrary real matrices whose columns have Euclidean norm at most one. Complex phases, rank-two/vector colorings and average-case statements are not substitutes.

Before research I reread/recovered the controlling campaign surfaces (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`), the current R13 ownership/history, and the newest R13 report `runs/R13/20260918T1704Z_finite-dtv-rowprune-c7f3.md`. `QUEUE.md` continues to exclude Boolean Komlos/R13 from the unassigned reserve. No shared-root or peer-track file was edited.

Current-source check on 18 September 2026: Guo--Fang--Lu, arXiv:2609.11189, submitted 10 September 2026, states the real-Boolean universal bound `3 sqrt(2 pi)` via directional total variation; Bansal--Jiang, arXiv:2508.03961, remains the earlier `~O((log n)^(1/4))` Boolean bound; Guillen--Kobzar, arXiv:2609.15071, submitted 14 September 2026, permits arbitrary complex unit phases and hence is rank-two vector discrepancy on real inputs rather than Boolean discrepancy. Bounded searches for `finite-dimensional Komlos directional total variation`, `Jensen defect Komlos discrepancy`, and `3 sqrt(2 pi) Komlos finite dimension improvement` found the Guo--Fang--Lu paper and secondary summaries but no matching finite-dimensional layer-cake correction. This is not a worldwide novelty proof: **novelty UNVERIFIED**.

## Previous certified metric

Let

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The immediately preceding report introduced, for

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2\left[1-(1-p_D)^D\right],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},\,3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\]

Its complete envelope was

\[
B_{old}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n)\},&5\le n\le85,\\
G_0(n),&n\ge86.
\end{cases}
\]

In particular `B_old(86)=G_0(86)>=7507/1000` by definition. The finite lower-bound history is retained unchanged: `K_5^*=T_5`, `K_6^*>=1.84535465`, `K_11^*>=1.99488049`, `K_12^*>=2.013108`.

## #30: integrate every tail scale instead of choosing one threshold

This strengthens the one-big-coordinate estimate in the preceding report.

For the Guo--Fang--Lu product density in dimension `D`, their Gaussian/chi-square representation gives independent

\[
S_i\sim\chi^2_3,\qquad Y_i=S_i^{-1}.
\]

For a direction `u`, write

\[
w_i=\frac{u_i^2}{\|u\|_2^2},\qquad
F_D(w)=\mathbb E\sqrt{\sum_{i=1}^D w_iY_i}.
\]

`F_D` is concave on the simplex and invariant under coordinate permutations. Averaging all permutations of `w` gives the uniform vector, hence Jensen's inequality yields the exact worst-direction reduction

\[
F_D(w)\le F_D(D^{-1},\dots,D^{-1}).
\]

Set

\[
X_D=\frac1D\sum_{i=1}^DY_i,
\qquad
a_D=\mathbb E\sqrt{X_D}.
\]

For `S~chi^2_3`, `E(S^{-1})=1`, so `E X_D=1`. Therefore

\[
2(1-a_D)=\mathbb E(\sqrt{X_D}-1)^2.
\]

Let `f(x)=(sqrt(x)-1)^2`. Keeping only `X_D>=1` and using layer cake,

\[
2(1-a_D)
\ge \int_1^\infty f'(t)\Pr(X_D\ge t)\,dt
=\int_1^\infty(1-t^{-1/2})\Pr(X_D\ge t)\,dt.\tag{1}
\]

Now fix `t>=1`. If `max_iY_i>=Dt`, then `X_D>=t`. Since the `chi^2_3` density is

\[
\frac{s^{1/2}e^{-s/2}}{\sqrt{2\pi}},
\]

we have, using `e^{-x}>=1-x`,

\[
\begin{aligned}
q_D(t)&:=\Pr(Y_i\ge Dt)=\Pr\left(S_i\le\frac1{Dt}\right)\\
&\ge \frac{2}{3\sqrt{2\pi}}\left(1-\frac1{2D}\right)(Dt)^{-3/2}\\
&=\frac{2-1/D}{3\sqrt{2\pi}D^{3/2}}t^{-3/2}.\tag{2}
\end{aligned}
\]

By independence,

\[
\Pr(\max_iY_i\ge Dt)=1-(1-q_D(t))^D.
\]

For `0<=q<1`, Bernoulli's inequality applied to `(1-q)^{-D}` gives

\[
(1-q)^{-D}=\left(1+\frac q{1-q}\right)^D\ge1+Dq,
\]

hence

\[
1-(1-q)^D\ge\frac{Dq}{1+Dq}.\tag{3}
\]

Define

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D}.
\]

Equations (2)--(3), and monotonicity of `x/(1+x)`, imply

\[
\Pr(X_D\ge t)
\ge \frac{\alpha_Dt^{-3/2}}{1+\alpha_Dt^{-3/2}}
\ge \frac{\alpha_D}{1+\alpha_D}t^{-3/2}.\tag{4}
\]

Substitution into (1), together with

\[
\int_1^\infty(1-t^{-1/2})t^{-3/2}\,dt
=\int_1^\infty(t^{-3/2}-t^{-2})\,dt=1,
\]

gives the closed-form finite-dimensional Jensen defect

\[
\boxed{
a_D\le1-\beta_D,
\qquad
\beta_D:=\frac{\alpha_D}{2(1+\alpha_D)}>0.}
\tag{5}
\]

This uses the whole continuum of tail levels rather than the preceding report's single event `X_D>=9`.

Guo--Fang--Lu's exact representation for their cube density gives

\[
V_u(\rho_C)\le\frac{\sqrt{2\pi}}{C}a_D\|u\|_2.
\]

Choosing

\[
\boxed{C_D^{\mathrm{lc}}=3\sqrt{2\pi}(1-\beta_D)}\tag{6}
\]

makes `V_u(rho_C)<=||u||_2/3`. Their Proposition 2.2/Corollary 2.3 therefore applies without changing the Boolean problem: every finite family of Euclidean-unit vectors in `R^D` admits genuine signs in `{+-1}` whose infinity norm is strictly less than `C_D^{lc}`.

## #3: exploit the strict active-row count

Fix a parameter `h>0`. For an arbitrary unit-column `m x n` matrix, call row `r_i` active when

\[
\|r_i\|_2>\frac h{\sqrt n}.
\]

The Frobenius energy obeys

\[
\sum_i\|r_i\|_2^2\le n.
\]

If `d` rows are active, then, because the activity inequality is strict,

\[
d\frac{h^2}{n}<n,
\qquad d<\frac{n^2}{h^2}.
\]

Since `d` is integral this strengthens the padding dimension to

\[
\boxed{d\le D_h(n):=\left\lceil\frac{n^2}{h^2}\right\rceil-1.}\tag{7}
\]

Restricting columns to active rows cannot increase their Euclidean norms. Pad the active submatrix by zero rows to `R^{D_h(n)}` and use (6). Every inactive row satisfies, for every Boolean signing,

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\|\varepsilon\|_2
\le h.
\]

Thus

\[
\boxed{
K_n^*\le H_h(n):=
\max\left\{h,\,3\sqrt{2\pi}\bigl(1-\beta_{D_h(n)}\bigr)\right\}.}
\tag{8}
\]

This is a source-matching real-Boolean theorem for arbitrary row dimension.

## #5: tune the pruning scale at the old crossover

Take the exact rational value

\[
\boxed{h=\frac{148709}{20000}=7.43545.}
\]

For `n=86`,

\[
\frac{n^2}{h^2}
=\frac{2958400000000}{22114366681}
=133.7772879809\ldots,
\]

so (7) gives `D_h(86)=133`.

The exact checker uses only rational arithmetic plus the classical bound `pi<355/113`. It verifies

\[
\sqrt{2\pi}<\frac{250663}{100000},
\qquad
\sqrt{133}<\frac{57663}{5000}.
\]

Consequently

\[
\alpha_{133}
>\frac{132500000000}{5767138247031},
\]

and hence

\[
\beta_{133}
>\frac{66250000000}{5899638247031}.
\]

Using these in (6) yields the rational upper certificate

\[
C_{133}^{\mathrm{lc}}
<\frac{4386643794496594659}{589963824703100000}
=7.435445379560651\ldots
<\frac{148709}{20000}.
\]

Therefore

\[
\boxed{K_{86}^*\le H_h(86)=\frac{148709}{20000}=7.43545.}\tag{9}
\]

Since the old envelope had `B_old(86)=G_0(86)>=7507/1000=7.507`, the fixed metric improves at `n=86` by at least

\[
\boxed{
\frac{7507}{1000}-\frac{148709}{20000}
=\frac{1431}{20000}=0.07155.}
\]

## New complete fixed metric

Define, for `n>=86`,

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

and

\[
H(n)=\max\left\{\frac{148709}{20000},\,3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

The complete retained envelope is

\[
\boxed{
B_{new}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n)\},&5\le n\le85,\\
\min\{G_0(n),H(n)\},&n\ge86.
\end{cases}}
\]

No claim is made here that `H(n)` beats `G_0(n)` in every dimension; the pointwise minimum preserves every earlier certificate and (9) rigorously moves the metric at `n=86`. All constants, dimensions and restrictions are explicit.

## Exact self-check and delivery

Exact checker:
`artifacts/R13/20260918T1734Z_continuous-layercake-a91c_checker.py`, creation commit `b60fe3669b8644fb0219790caf5324b914b00405`, read back at that exact commit.

Archived executed output:
`artifacts/R13/20260918T1734Z_continuous-layercake-a91c_checker.out`, corrected-output commit `06e9e2223649ab340b5dbb2b6922b81c362d9253`, read back at that exact commit. It ends `R13_CONTINUOUS_LAYERCAKE_EXACT_PASS`. This is a **self-check**, not an independent audit.

The new layer-cake theorem has outside audits `0/2`; the older R12/P26 audits of the base Guo--Fang--Lu `3 sqrt(2 pi)` theorem do not count as audits of this finite-dimensional sharpening.

Status: **PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof / exact self-check PASS / outside audits of new claim 0/2 / novelty UNVERIFIED**. The fixed-metric unchanged count remains/reset to `0` because this run moved it.

Next high-value routes should be genuinely different from this run: optimize the product density rather than its tail estimate; derive a two-coordinate lower event for `X_D`; or combine the exact `K_5^*` block theorem with the finite-dimensional DTV theorem by splitting columns according to row energy. Do not spend the next run merely changing the rational `h` in (8).

## Model / scheduler control

The exposed task-control interface still has no binding model-family field and no reasoning-effort field; it exposes prompt/title/schedule/enablement/timing controls. Thus `GPT-6 / maximum` remains prompt text rather than authenticated runtime metadata, and this report correctly states `GPT-5.6 Sol / UNVERIFIED`. The legitimate response to a task returning `You cannot modify this task` is an authorized owner/workspace scheduler context or platform support; permission bypass or duplicate-task creation is not a valid workaround. No scheduler or permission state was changed in this run.

```yaml
ledger_delta:
  track: R13
  source: "Boolean Komlos / E0042; current navigation Bansal-Jiang arXiv:2508.03961 and Guo-Fang-Lu arXiv:2609.11189"
  metric: "complete rigorously certified pointwise upper envelope B_R13(n)"
  before: "B_old with G0(n) branch; B_old(86)=G0(86)>=7.507"
  after: "B_new=min(old,H) for n>=86; B_new(86)<=7.43545"
  movement: "strict at n=86 by at least 0.07155"
  unchanged_count: 0
  tried_moves: [3, 5, 30]
  remaining_obligation: "improve another dimension/source-matching branch or produce a new explicit finite obstruction; avoid mere h retuning"
  self_check: PASS
  outside_audits_new_claim: "0/2"
  novelty: UNVERIFIED
  artifact_commits:
    checker: b60fe3669b8644fb0219790caf5324b914b00405
    output: 06e9e2223649ab340b5dbb2b6922b81c362d9253
```
