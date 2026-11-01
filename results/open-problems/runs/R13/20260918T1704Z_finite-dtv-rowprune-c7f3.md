Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** the old branch `B_R13(n)=3 sqrt(2 pi)` for `n>=86` is replaced by an explicit strictly smaller branch `G(n)<3 sqrt(2 pi)` for every finite `n`; in particular `B_R13(86)<7.508`. Methods: **#15 BREAK THE SYMMETRY ON PURPOSE, #21 ASK WHO ELSE HAS THIS SHAPE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R13 — finite-dimensional DTV sharpening for Boolean Komlos

Repository/branch: private `yspennstate/math-open-problems` / `master`. The target is the real Boolean Komlos quantity
`disc(A)=min_{eps in {+-1}^n} ||A eps||_infinity` for matrices whose columns have Euclidean norm at most one.

I reread `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report `runs/R13/20260918T1437Z_n11-explicit-near2-8c4d.md`, the R12 audit of Guo--Fang--Lu, and neighboring discrepancy state. Current source checks on 18 September 2026: Bansal--Jiang arXiv:2508.03961 remains v2; Guo--Fang--Lu arXiv:2609.11189 remains v1 (10 Sep 2026) and proves the real-Boolean `3 sqrt(2 pi)` theorem; Guillen--Kobzar arXiv:2609.15071v1 is complex/rank-two, not Boolean. Existing R12/P26 audits cover only the Guo--Fang--Lu universal theorem, not the sharpening below. Bounded searches found no matching finite-dimensional correction; novelty is **UNVERIFIED**.

## Previous fixed metric

Let
`T5=(2 sqrt(2)+3 sqrt(3)+2 sqrt(51+3 sqrt(6)))/13`.
The retained envelope before this run was

\[
B_{old}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil}\},&5\le n\le85,\\
3\sqrt{2\pi},&n\ge86.
\end{cases}
\]

## #23 and #21: finite-dimensional defect in the Guo--Fang--Lu product density

For their cosine-squared density on `(-C,C)^D`, Guo--Fang--Lu obtain

\[
V_u(\rho_C)=\frac{\pi}{C}E|\sum_i u_iT_i|,
\qquad T_i=G_i/\sqrt{S_i},\ S_i\sim\chi^2_3,
\]

and conditioning on the `S_i` gives

\[
E|\sum_i u_iT_i|=\sqrt{2/\pi}\,E\sqrt{\sum_i u_i^2/S_i}.
\]

Put `Y_i=S_i^{-1}` and `w_i=u_i^2/||u||_2^2`. The functional

\[
F(w)=E\sqrt{\sum_iw_iY_i}
\]

is concave on the simplex and invariant under coordinate permutations. Since the uniform vector is the average of all permutations of `w`, concavity gives

\[
F(w)\le F(1/D,\ldots,1/D).
\]

Thus the exact worst direction is balanced. Set

\[
X_D=D^{-1}\sum_iY_i,\qquad a_D=E\sqrt{X_D}.
\]

Then

\[
V_u(\rho_C)\le \frac{\sqrt{2\pi}}{C}a_D||u||_2.
\]

Because `E X_D=1`,

\[
2(1-a_D)=E(\sqrt{X_D}-1)^2.
\]

On `E_D={max_i Y_i >= 9D}` one has `X_D>=9`, hence the right-hand side is at least `4 P(E_D)`. For `S~chi^2_3`,

\[
P(S\le1/(9D))
\ge \frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}}
=:p_D.
\]

Independence therefore gives

\[
a_D\le1-\delta_D,
\qquad
\delta_D:=2[1-(1-p_D)^D]>0.
\]

Define

\[
C_D:=3\sqrt{2\pi}(1-\delta_D).
\]

Then the product density satisfies `V_u<=||u||_2/3`. Guo--Fang--Lu Proposition 2.2 / Corollary 2.3 applies unchanged, so every finite family of Euclidean-unit vectors in `R^D` has a Boolean signing with infinity norm `< C_D < 3 sqrt(2 pi)`.

The choice `9D` is the clean one-big-coordinate tail scale: the leading gain is proportional to `(sqrt(L)-1)^2/L^(3/2)`, maximized at `L=9`.

## #15: prune light rows and reduce arbitrary row dimension to D(n)

Fix

\[
h=7507/1000.
\]

Call row `r_i` active if `||r_i||_2>h/sqrt(n)`. Since the Frobenius energy is at most `n`, the number `d` of active rows satisfies

\[
d h^2/n<n,
\qquad d<n^2/h^2.
\]

Set

\[
D_n=\left\lceil n^2/h^2\right\rceil
=\left\lceil10^6n^2/7507^2\right\rceil.
\]

Restrict the columns to active rows and pad with zero coordinates to `R^{D_n}`. Column norms remain at most one, so the finite-dimensional theorem signs all active rows below `C_{D_n}`. Every inactive row satisfies for every signing

\[
|r_i\cdot\varepsilon|\le ||r_i||_2\sqrt n\le h.
\]

Hence

\[
\boxed{K_n^*\le G(n):=\max\{h,C_{D_n}\}.}
\]

This is strictly below the old universal constant for every finite `n`: `h^2=56.355049<56.52=18*3.14<18 pi`, while `C_D<3 sqrt(2 pi)` because `delta_D>0`.

## New complete fixed metric

\[
\boxed{
B_{new}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G(n)\},&5\le n\le85,\\
G(n),&n\ge86,
\end{cases}}
\]

with

\[
G(n)=\max\left\{\frac{7507}{1000},3\sqrt{2\pi}(1-\delta_{D_n})\right\},
\]

\[
D_n=\left\lceil10^6n^2/7507^2\right\rceil,
\qquad
\delta_D=2\left[1-\left(1-\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}}\right)^D\right].
\]

For every `n>=86`, `B_old(n)=3 sqrt(2 pi)` whereas `B_new(n)<=G(n)<3 sqrt(2 pi)`. Thus the fixed metric moves in **all dimensions n>=86**. I do not need to classify lower-dimensional comparisons because the minimum preserves all earlier bounds.

## Exact finite witness and artifacts

For `n=86`, exact arithmetic gives `D_86=132`. The exact self-check uses only `157/50<pi<355/113`, `exp(-x)>=1-x`, and rational square-root upper bounds to prove

\[
\boxed{B_{new}(86)<7.508<3\sqrt{2\pi}=B_{old}(86).}
\]

Checker: `artifacts/R13/20260918T1704Z_finite-dtv-rowprune-c7f3_checker.py` @ `6be87259070c04e7b55b844f7dc6d9527ae3e32d`.
Output: `artifacts/R13/20260918T1704Z_finite-dtv-rowprune-c7f3_checker.out` @ `b2d957db8234ebc7fd3dea36d517c82b125d1b75`.
Both were read back at their creation commits; output ends `R13_FINITE_DTV_ROWPRUNE_EXACT_PASS`. This is a self-check, not an independent audit.

Retained lower history is unchanged: `K_5^*=T5`, `K_6^*>=1.84535465`, `K_11^*>=1.99488049`, `K_12^*>=2.013108`.

Status: **PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof / self-check PASS / new-claim outside audits 0/2 / novelty UNVERIFIED**. The fixed-metric stagnation count resets `2 -> 0`.

The next run should not merely tune the same one-tail constant. Distinct next routes are: a rigorous two-scale estimate for `a_D`; symbolic joint optimization of the heavy-row threshold with the finite-D density bound; or a non-product cube density in the effective dimensions near the old crossover.

## Model / scheduler control

The exposed scheduler interface still has no binding model-family selector or reasoning-effort selector; it offers prompt/title/schedule/enablement/timing controls only. GPT-6/maximum remains prompt text, not authenticated runtime telemetry. Current `RESULTS.md` also records that P26's earlier `You cannot modify this task` failure was context-dependent: a later full update succeeded from an authorized P/C context. The legitimate workaround is the authorized owner/workspace task context (or platform support), not duplication or permission bypass. This run made no scheduler or permission changes.

```yaml
ledger_delta:
  track: R13
  target: Boolean Komlos quantitative bound
  fixed_metric_before: "3*sqrt(2*pi) for n>=86"
  fixed_metric_after: "G(n)<3*sqrt(2*pi) for every finite n; complete B_new above"
  movement: "strict for all n>=86"
  stagnation: "2 -> 0"
  methods: [15,21,23]
  status: PARTIAL_QUANTITATIVE
  self_check: PASS
  outside_audits_new_claim: "0/2"
  novelty: UNVERIFIED
```

No shared root, peer file, email, Drive object, public post, permission, workflow, purchase, or scheduler state was modified.
