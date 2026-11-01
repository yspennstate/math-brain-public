Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86)` improves from `148709/20000 = 7.43545` to `740179/100000 = 7.40179`, an exact certified decrease `1683/50000 = 0.03366`. Methods actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE.**

# R13 — cosine-power deformation and three-threshold finite-dimensional Komlós bound

Repository/branch: private `yspennstate/math-open-problems` / `master`.

R13 remains the HARD OUTSIDE owner of the real Boolean Komlós target E0042. The fixed quantity is the complete rigorously certified pointwise upper envelope `B_R13(n)` for

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty
\]

when the real matrix `A` has arbitrary row dimension and every column has Euclidean norm at most one. Complex phases, rank-two/vector colorings and average-case bounds are not substitutes.

Before research I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, intake E0042, the newest R13 report `runs/R13/20260918T1734Z_continuous-layercake-a91c.md`, and the closest discrepancy-neighbor history. The current R02 sign-matrix route is in successor-admission hold rather than a competing Komlós assignment; the old R16 Beck--Fiala slot has rotated away from Beck--Fiala. No shared root or peer file was edited.

## Current-source check

The original intake E0042 is Bandeira's Open Problem 0.1, the real Boolean Komlós conjecture. Bansal--Jiang's current exposition still records their real-Boolean `O((log n)^(1/4)(log log n)^(7/4))`-type improvement. Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, claims the source-level real Boolean theorem with universal constant `3 sqrt(2 pi)`. Their Lemma 2.4 uses the product `cos^2` density on a cube, Proposition 2.2/Corollary 2.3 converts a directional-total-variation bound into genuine Boolean signs, and their Remark 2.5 says the `sqrt(2 pi)` variation coefficient is asymptotically sharp for that fixed `cos^2` product family, not among all cube-supported densities. Guillen--Kobzar, arXiv:2609.15071, submitted 14 September 2026, allows arbitrary complex unit phases and explicitly identifies the real-input version with rank-two vector discrepancy, so it is not the Boolean statement.

Fresh bounded searches on 18 September 2026 for `cos^p` / cosine-power cube densities combined with Komlós or directional total variation returned the Guo--Fang--Lu paper and summaries, but no matching finite-dimensional `p != 2` deformation or the three-threshold correction below. This is negative search evidence only: **novelty remains UNVERIFIED**.

## Baseline retained from the preceding R13 report

Let

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The exact finite history remains

\[
K_5^*=T_5,\qquad
K_6^*\ge1.84535465,\qquad
K_{11}^*\ge1.99488049,\qquad
K_{12}^*\ge2.013108.
\]

The preceding upper-envelope ingredients were

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\quad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2\bigl[1-(1-p_D)^D\bigr],
\quad
G_0(n)=\max\left\{\frac{7507}{1000},3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\},
\]

and the continuous-layer-cake branch

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=\max\left\{\frac{148709}{20000},3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

At `n=86`, the preceding report proved `H(86)=148709/20000=7.43545`, while `G_0(86)>=7507/1000`; hence the preceding complete envelope had exactly

\[
B_{old}(86)=\frac{148709}{20000}=7.43545.
\]

The preceding method triple was `#3,#5,#30`; it is not repeated here.

## Method #6 — deform the cube density away from the asymptotically optimal exponent

The key new route is to replace the fixed `cos^2` factor by a one-parameter family. For `p>1`, `C>0`, and dimension `D`, let

\[
\rho_{C,p}(x)=Z_{C,p}^{-D}
\prod_{i=1}^D\cos^p\!\left(\frac{\pi x_i}{2C}\right)
\mathbf 1_{(-C,C)^D}(x),
\]

where `Z_{C,p}` is the one-dimensional normalizing integral. Since `p>1`, the zero extension is in `W^{1,1}` and has no boundary jump. If `X` has density `rho_{C,p}` and

\[
T_i=\tan\left(\frac{\pi X_i}{2C}\right),
\]

then the `T_i` are independent with density proportional to

\[
(1+t^2)^{-(p+2)/2}.
\]

Equivalently,

\[
T_i\stackrel d=\frac{G_i}{\sqrt{S_i}},
\qquad G_i\sim N(0,1),\quad S_i\sim\chi^2_{p+1},
\]

all independent. Differentiating the log density and conditioning on the `S_i` gives the exact directional-variation identity

\[
V_u(\rho_{C,p})
=\frac{p\pi}{2C}\sqrt{\frac2\pi}
\,\mathbb E\sqrt{\sum_i\frac{u_i^2}{S_i}}.
\tag{1}
\]

Put `z=p-1`, `Y_i=z/S_i`, and `w_i=u_i^2/||u||_2^2`. Since `E(S_i^{-1})=1/(p-1)`, `E Y_i=1`, and (1) becomes

\[
V_u(\rho_{C,p})
=\frac{\sqrt{\pi/2}}{C}\frac{p}{\sqrt{p-1}}
\,F_{p,D}(w)\,\|u\|_2,
\]

\[
F_{p,D}(w)=\mathbb E\sqrt{\sum_iw_iY_i}.
\tag{2}
\]

`F_{p,D}` is concave on the simplex and invariant under coordinate permutations. Averaging all permutations of `w` and applying concavity therefore yields the exact worst-direction reduction

\[
F_{p,D}(w)\le a_{p,D}:=
\mathbb E\sqrt{\frac1D\sum_{i=1}^DY_i}.
\tag{3}
\]

The asymptotic prefactor

\[
b(p)=\sqrt{\frac\pi2}\frac{p}{\sqrt{p-1}}
\]

is minimized at `p=2`, so simply changing `p` cannot improve the asymptotic product-family constant. The finite-dimensional opportunity is the opposite: for `p<2`, the inverse-chi-square scale `Y_i` has a heavier tail and the strict Jensen defect in (3) is larger. I chose the algebraically convenient

\[
\boxed{p=\frac95},\qquad
S_i\sim\chi^2_{14/5},\qquad
Y_i=\frac{4}{5S_i}.
\]

Then

\[
b(9/5)=\frac{9\sqrt{10\pi}}{20}.
\tag{4}
\]

So the deformation is asymptotically slightly worse than `p=2`, but can be strictly better in the finite active dimension relevant after row pruning.

## Method #25 — count a three-level tail event instead of one big coordinate

Let

\[
X_D=\frac1D\sum_{i=1}^DY_i,
\qquad a_D=\mathbb E\sqrt{X_D}.
\]

Because `E X_D=1`,

\[
2(1-a_D)=\mathbb E(\sqrt{X_D}-1)^2.
\]

Keeping the `X_D>=1` part and using layer cake gives

\[
2(1-a_D)
\ge\int_1^\infty(1-t^{-1/2})\Pr(X_D\ge t)\,dt.
\tag{5}
\]

For `S~chi^2_{14/5}` its density is

\[
\frac{s^{2/5}e^{-s/2}}{2^{7/5}\Gamma(7/5)}.
\]

For `k=1,2,3`, `D>=134`, and `t>=1`, the event `Y_i>=Dt/k` is `S_i<=4k/(5Dt)`. Using `e^{-s/2}>=1-s/2` over this interval gives

\[
\Pr\left(Y_i\ge\frac{Dt}{k}\right)
\ge \frac{A_{k,D}}D\,t^{-7/5},
\tag{6}
\]

where, with the rigorously certified rational upper bound

\[
\bar\Gamma:=\frac{88869}{100000}>\Gamma(7/5),
\]

we may take

\[
A_{k,D}=
\frac{5}{7\bar\Gamma}
\left(\frac{2k}{5}\right)^{7/5}
\left(1-\frac{2k}{5D}\right)D^{-2/5}.
\tag{7}
\]

The gamma bound is elementary and recorded exactly by the checker. Robbins' upper bound at `x=7/5` gives

\[
\Gamma(7/5)
<\frac57\sqrt{2\pi}\left(\frac75\right)^{19/10}e^{-563/420}.
\]

Using `pi<355/113`, `(517/500)^10<7/5`, and the degree-six positive Taylor lower bound for `e^{563/420}` yields

\[
\Gamma(7/5)<0.8886816062<\frac{88869}{100000}.
\tag{8}
\]

Now count the same tail event at three scales. If among the `Y_i` there is

- one value at least `Dt`, or
- two values each at least `Dt/2`, or
- three values each at least `Dt/3`,

then `X_D>=t`.

Let `x=t^{-7/5}`, `a_k=A_{k,D}/D`, and define the artificial categorical tail probabilities `q_k=a_k x`. The actual one-coordinate category stochastically dominates this artificial category because all three threshold tail probabilities satisfy (6). Hence the increasing three-level event has probability at least the corresponding artificial probability.

Its complement has no coordinate in the top category, at most one coordinate in the top two categories, and at most two coordinates in the top three categories. Therefore the exact lower polynomial is

\[
\begin{aligned}
Q_D(x)=1
&-(1-a_3x)^D\\
&-D(a_3-a_1)x(1-a_3x)^{D-1}\\
&-\binom D2\Big[(a_3-a_2)^2
+2(a_2-a_1)(a_3-a_2)\Big]x^2(1-a_3x)^{D-2}.
\end{aligned}
\tag{9}
\]

Thus `Pr(X_D>=t)>=Q_D(t^{-7/5})`. Write

\[
Q_D(x)=\sum_{\ell=1}^D c_{\ell,D}x^\ell.
\]

Substituting (9) into (5) evaluates completely as the finite sum

\[
\boxed{
\beta_D^{(9/5,3)}
:=\frac12\sum_{\ell=1}^Dc_{\ell,D}
\left(
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right),}
\tag{10}
\]

and

\[
a_D\le1-\beta_D^{(9/5,3)}.
\tag{11}
\]

Combining (2)--(4), the cube of half-side

\[
\boxed{
C_D^{(9/5,3)}
=\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_D^{(9/5,3)}\right)}
\tag{12}
\]

has directional variation at most `1/3` in every unit direction. Guo--Fang--Lu's Proposition 2.2/Corollary 2.3 therefore supplies genuine Boolean signs into that cube. Nothing here uses complex phases or vector coloring.

## Exact specialization at D=134

The exact checker proves (8), and from (7) it proves the rational lower coefficients

\[
A_{1,134}>\frac{31323}{10^6},\qquad
A_{2,134}>\frac{8241}{10^5},\qquad
A_{3,134}>\frac{2899}{20000}.
\tag{13}
\]

For example, after substituting the gamma bound, each fractional-power inequality in (13) is reduced to a fifth-power comparison of integers; no floating-point inequality is used for the certificate.

Substituting the three rational values from (13) into the polynomial (9) and the finite sum (10) gives the exact rational lower certificate

\[
\beta_{134}^{(9/5,3)}>0.021801997253521478\ldots .
\]

Using only the classical rational bound `pi<355/113`, the checker also certifies

\[
\sqrt{10\pi}<\frac{1121}{200}.
\]

Consequently

\[
C_{134}^{(9/5,3)}
<7.401779737281917\ldots
<\boxed{\frac{740179}{100000}=7.40179}.
\tag{14}
\]

## Row pruning and movement of the fixed metric

Take

\[
h_9:=\frac{740179}{100000}.
\]

For an arbitrary real unit-column `m x 86` matrix, call a row active when

\[
\|r_i\|_2>\frac{h_9}{\sqrt{86}}.
\]

The Frobenius budget is

\[
\sum_i\|r_i\|_2^2\le86.
\]

If `d` rows are active, strict activity gives

\[
d<\frac{86^2}{h_9^2}.
\]

The checker proves exactly

\[
134<\frac{86^2}{h_9^2}<135,
\]

so `d<=134`. Restrict to those rows, pad by zero rows to dimension 134, and apply (14). Every inactive row satisfies for every Boolean signing

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\sqrt{86}\le h_9.
\]

Therefore

\[
\boxed{K_{86}^*\le\frac{740179}{100000}=7.40179.}
\tag{15}
\]

Relative to the immediately preceding certified envelope,

\[
\frac{148709}{20000}-\frac{740179}{100000}
=\boxed{\frac{1683}{50000}=0.03366}.
\]

So the fixed metric genuinely moves and the unchanged-run count resets to zero.

## General new branch and complete retained envelope

The preceding construction is not confined to `n=86`. For `n>=86`, define

\[
D_9(n)=\left\lceil\frac{n^2}{h_9^2}\right\rceil-1
=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1.
\]

Then `D_9(n)>=134`. Use (7)--(10) with `D=D_9(n)` and define

\[
J(n)=\max\left\{
h_9,
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_{D_9(n)}^{(9/5,3)}\right)
\right\}.
\tag{16}
\]

The same row-pruning proof gives `K_n^*<=J(n)` for every `n>=86`. No claim is made that `J(n)` is the best branch for every such `n`; it is retained by a pointwise minimum with all earlier certificates.

The complete certified envelope after this run is therefore

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},\ T_5\sqrt{\lceil n/5\rceil},\ G_0(n)\},&5\le n\le85,\\[1mm]
\min\{G_0(n),\ H(n),\ J(n)\},&n\ge86.
\end{cases}}
\tag{17}
\]

All dimensions, constants and restrictions are explicit. In particular, (17) certifies the strict movement (15) without discarding any earlier branch.

## Method #15 — breaking coordinate symmetry is a genuine no-go for this objective

I also tested whether a better finite-dimensional cube density could come from assigning different one-dimensional exponents or factors to different coordinates. For the worst-direction objective this cannot help by itself.

Let `G` be the coordinate-permutation group of the cube and let `rho` be any feasible probability density supported in the cube with

\[
\sup_{\|u\|_2=1}V_u(\rho)\le\kappa.
\]

Symmetrize it:

\[
\bar\rho(x)=\frac1{|G|}\sum_{P\in G}\rho(Px).
\]

Directional variation is convex in the density, and permutation of coordinates sends `V_u(rho(P\cdot))` to `V_{P^{-1}u}(rho)`. Hence

\[
V_u(\bar\rho)
\le\frac1{|G|}\sum_{P\in G}V_{P^{-1}u}(\rho)
\le\kappa\|u\|_2.
\]

Thus every asymmetric candidate has a permutation-symmetric candidate with no worse worst-direction variation. This kills coordinate-asymmetric exponent tuning as a route to improving the minimax cube constant. It does **not** rule out symmetric but nonproduct densities, which remain a live route.

Outcome of the three methods:

- **#6:** success — the `p=9/5` deformation trades a slightly worse asymptotic prefactor for a stronger finite-dimensional Jensen defect.
- **#25:** success — the exact three-threshold occupancy count improves the one-big-coordinate tail certificate and closes the rational `D=134` target needed for (15).
- **#15:** useful failure — coordinate-permutation asymmetry cannot improve the minimax directional-TV constant because symmetrization never increases it.

## Exact self-check and immutable delivery

Exact checker:

`artifacts/R13/20260918T1834Z_cospower-3threshold-c9e4_checker.py`

creation commit `67d7f25e8ff1cde4ecb3702fe375757a35dd4ad3`, read back at that exact commit.

Archived executed output:

`artifacts/R13/20260918T1834Z_cospower-3threshold-c9e4_checker.out`

creation commit `9d5dd96426d37413705a6633fe0f88c7cd4a85bd`, read back at that exact commit. It ends

`R13_COSPOWER_3THRESHOLD_EXACT_PASS`.

The checker is a **self-check**, not an independent audit. It uses exact rational arithmetic for every finite comparison. Its explicitly stated analytic inputs are the classical bound `pi<355/113`, Robbins' gamma upper inequality, and the positive Taylor lower bound for `e^x`.

The new cosine-power theorem has outside audits `0/2`. The older R12/P26 audits of the base Guo--Fang--Lu universal theorem do not count as audits of this new finite-dimensional deformation. Accordingly nothing is called closed or paper-ready.

Status: **PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof / exact self-check PASS / outside audits of the new sharpening 0/2 / novelty UNVERIFIED**.

The next high-value route should not be another decimal retuning of `p` or `h`. The two genuinely different opportunities are: (i) optimize over symmetric **nonproduct** cube densities, since #15 rules out gaining merely by coordinate asymmetry; or (ii) couple the exact five-column theorem `K_5^*=T_5` to the finite-dimensional DTV density through a row-energy decomposition rather than row deletion.

## Model / scheduler-control status

The available task-control surface still has no binding model-family selector or reasoning-effort selector, and no authenticated completed-run reasoning receipt. `GPT-6 / maximum` therefore remains prompt-only in this environment; this report truthfully records `GPT-5.6 Sol / UNVERIFIED`.

The historical `You cannot modify this task` response is an authorization/account-context boundary. Repository records show some edits can succeed from an authorized owner/workspace context even when denied elsewhere. The legitimate remedy is the owning task surface or platform/admin support, not permission bypass, task duplication or a repository edit presented as a scheduler repair. No scheduler or permission change was attempted in this run.

```yaml
ledger_delta:
  track: R13
  lane: HARD_OUTSIDE
  source_id: E0042
  source: "real Boolean Komlos; current navigation Bansal-Jiang arXiv:2508.03961, Guo-Fang-Lu arXiv:2609.11189v1"
  fixed_metric: "complete rigorously certified pointwise upper envelope B_R13(n)"
  before:
    B_R13_86: "148709/20000 = 7.43545"
    envelope: "B_old with G0 and H branches from 20260918T1734Z"
    unchanged_count: 0
  after:
    B_R13_86: "740179/100000 = 7.40179"
    improvement: "1683/50000 = 0.03366"
    new_branch: "J(n), p=9/5 cosine-power density + 3-threshold tail count, n>=86"
    unchanged_count: 0
  methods_this_run: [6, 15, 25]
  method_outcomes:
    6: "SUCCESS: finite-D cosine-power deformation"
    15: "NO-GO: coordinate permutation asymmetry symmetrizes without worsening minimax TV"
    25: "SUCCESS: exact 3-threshold occupancy count"
  finite_core:
    dimension: 134
    gamma_upper: "Gamma(7/5) < 88869/100000"
    A1_lower: "31323/1000000"
    A2_lower: "8241/100000"
    A3_lower: "2899/20000"
    density_signing_upper: "< 7.401779737281917..."
    row_prune_h: "740179/100000"
  artifacts:
    checker: "artifacts/R13/20260918T1834Z_cospower-3threshold-c9e4_checker.py @ 67d7f25e8ff1cde4ecb3702fe375757a35dd4ad3"
    output: "artifacts/R13/20260918T1834Z_cospower-3threshold-c9e4_checker.out @ 9d5dd96426d37413705a6633fe0f88c7cd4a85bd"
    self_check: PASS
  audits_new_claim: "0/2"
  novelty: UNVERIFIED
  status: PARTIAL_QUANTITATIVE
  next_routes:
    - "symmetric nonproduct cube density"
    - "five-column exact block theorem + DTV energy decomposition"
```
