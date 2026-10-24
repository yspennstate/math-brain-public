Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #2, #9, #29.**

# R09 — Blanc–Renaudie `d=7,8,9,10`: parity obstruction, randomized blocking, and an unconditional global Fourier gap

## 1. Continuity, source status, and ownership

I continued from `runs/R09/20260918T2331Z_blanc_unified_matching_smoothness_a91f6c.md`. I did **not** reopen Tang Question 4.11, G0013, the retired Chen–Wang Gaussian-subuniformity successor, or the distinct C0064 Fourier-infrared-bound source. The latest Tang handoff remains controlling and records `TANG-2020-Q4.11` as `RETIRED_FROZEN_REFUTED`.

Before research I re-read `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active exclusive claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the preceding R09 report, the related C0064 attempt evidence, and the relevant older R09 exact F2 checker. The active claim remains exclusively R09-owned and `READY / CLOSABLE OUTSIDE / OPEN`, with frozen metric

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous Blanc–Renaudie initialization certificate is proved}\}=0.
\]

A fresh bounded search on 2026-09-19 local / 2026-09-18 UTC recovered Arthur Blanc-Renaudie's `arXiv:2609.20764`, submitted 2026-09-17 and updated 2026-09-18, and no later source-matching resolution of the nearest-neighbour `d=7,8,9,10` cases. This is bounded negative evidence, not a worldwide novelty certificate. The source itself records nearest-neighbour `d>=11` as known and `d=7,8,9,10` as the remaining numerical regime. Theorem 1.1 and Corollary 1.2 are still the source-valid finite-certificate route.

The source quantities used below were checked against Theorem 3.24, Proposition 3.25 and Lemma 5.14. In the nearest-neighbour model let

\[
r_p(x):=\frac{\tau_p(x)}{\chi(p)},\qquad
q_p(x):=\mathbb P_p^\otimes(\Delta(\vec A_1)=x)
=\frac{(D*\tau_p)(x)}{\Omega\chi(p)},\qquad \Omega=2d,
\tag{1.1}
\]

where `D` is the nearest-neighbour adjacency kernel. Thus `r_p` and `q_p` are probability measures on `Z^d` and

\[
\widehat q_p(\kappa)=A_d(\kappa)\widehat r_p(\kappa),
\qquad
A_d(\kappa)=\frac1d\sum_{j=1}^d\cos \kappa_j.
\tag{1.2}
\]

The preceding R09 run defined the endpoint-conditioned surviving two-middle-increment subprobability

\[
\zeta_{A,B}(x)
=\mathbb P_p^\otimes\bigl(T_{\rm cut}>3,\Delta(\vec A_1)+\Delta(\vec A_2)=x\mid \vec A_0=A,\vec A_3=B\bigr),
\]

with total mass `s(A,B)=P_3^⊗(A,B)`, and the directional fractional unit-shift matching mass `m_i(A,B)`. That run proved that a positive `m_i` simultaneously yields the bridge mass needed for mixing and the quadratic Fourier contraction needed by Proposition 3.25. This run attacks whether that matching property is structurally automatic.

## 2. Method #2 — ATTACK THE NEGATION FIRST: fixed-block matching has a real parity obstruction

The strongest possible failure already occurs at `p=0`. Every pointed cluster is then a singleton, so each middle increment is an independent uniformly random signed coordinate step

\[
U\in\{\pm e_1,\ldots,\pm e_d\}.
\]

For the fixed two-middle-increment block, `U_1+U_2` has even checkerboard parity. A unit coordinate shift has odd parity. Therefore the support of the two-step law and its unit translate are disjoint, and the fractional unit-shift matching mass is exactly

\[
\boxed{\mathfrak m_i(U_1+U_2)=0.}
\tag{2.1}
\]

This is an obstruction to the *stronger R09 matching criterion*, not to Blanc–Renaudie's theorem: the source invokes its Markov-renormalisation theorem only at large susceptibility, far from `p=0`. But it identifies a genuine mechanism that any surgery-free proof must overcome. Survival alone does not imply shift-smoothness; parity/aperiodicity has to enter somewhere.

### 2.1 Exact F2 positive-p negation search

I then tried to find a positive-p version of the obstruction in the smallest source-exact nontrivial cluster core. Reusing the previously certified exact specialization of `C_cut` on pointed clusters with underlying size at most two, I enumerated every endpoint-direction / endpoint-nonzero-tail class and computed the exact surviving two-middle displacement measure. On each coordinate line the maximum fractional unit matching equals a minimum weighted vertex cover on a path, so it is computed by exact dynamic programming.

At the calibration `p=1/(4d)` the exhaustive minima of

\[
\frac{\text{maximum unit-shift matching mass}}
     {\text{surviving F2 middle-pair mass}}
\]

are:

| `d` | exact minimum | decimal | endpoint classes |
|---:|---|---:|---:|
| 7 | `2375073108661923112872511488983649758802 / 19178123694298524270075679041418852974977` | 0.123842829805504 | 210 |
| 8 | `95103853455989983642633146827136808353505148530 / 857607216466505983307341314700417434066358599511` | 0.110894418365362 | 272 |
| 9 | `6330826709325380988463448464792260410318779602050781250 / 63108909810370779682543388474874482635444886434659702421` | 0.100315894036963 | 342 |
| 10 | `662111926225389693778291519763704966042312563418695606462128034 / 7233446449093795874028813752906544263390385484152696801671474747` | 0.091534779566708 | 420 |

The unique symmetry classes attaining the minima are `(0,0)` and `(1,1)` in the signed-direction enumeration `[+e_1,-e_1,+e_2,-e_2,...]`: the incoming endpoint direction and the outgoing endpoint's nonzero tail are aligned with the matching coordinate. Thus the attempted positive-p negation **failed** on the full F2 core, but it located the exact extremal geometry.

This is diagnostic only. `F2` has vanishing mass in the large-susceptibility regime, so these constants do not certify Proposition 3.25 for the full chain and do not move `M_A`.

The exact checker is

`artifacts/R09/20260919T0033Z_blanc_matching_parity_f2_7e4c2a.py`

with archived output

`artifacts/R09/20260919T0033Z_blanc_matching_parity_f2_7e4c2a.out`.

It ends `ALL_EXACT_CHECKS_PASS`.

## 3. Method #9 — RANDOMIZE: random block parity kills the `p=0` obstruction exactly

The parity obstruction comes from insisting that every block contain exactly two middle increments. The most economical deperiodization is to randomize the block length. At `p=0` define

\[
\mu_d:=\frac12\,\mathcal L(U_1+U_2)
      +\frac12\,\mathcal L(U_1+U_2+U_3).
\tag{3.1}
\]

The even and odd checkerboard classes are now both present. Exact weighted-path matching gives, in the target dimensions,

\[
\boxed{
\mathfrak m_{e_1}(\mu_d)
=\frac{18d^2-27d+13}{8d^3}.
}
\tag{3.2}
\]

The checker verifies this identity exactly for `d=7,8,9,10`, giving

\[
\frac{353}{1372}\approx0.257289,
\quad
\frac{949}{4096}\approx0.231689,
\quad
\frac{307}{1458}\approx0.210562,
\quad
\frac{1543}{8000}=0.192875.
\]

So randomizing between the two- and three-increment blocks turns an exact zero matching mass into an `Theta(1/d)` mass even at the maximally periodic endpoint `p=0`.

This does **not** yet replace source Proposition 3.25. Blanc–Renaudie's proof is organized around a deterministic three-transition block with fixed endpoint conditioning. To use (3.2) one must rewrite the transfer argument with a randomized `3/4`-transition renewal block (or an equivalent lazy block) and show that the altered block decomposition still supplies the product/Fourier estimate in Theorem 3.24. The value of (3.2) is that it rules out checkerboard periodicity as a fundamental obstacle: a one-bit block-parity randomization removes it with an explicit nonvanishing constant.

## 4. Method #29 — ADD THE POINTS AT INFINITY: compactify on the Fourier torus

The fixed-block obstruction suggested separating two questions:

1. is the **unconditioned** increment law already aperiodic/smooth on the whole torus? and
2. how much of that smoothness can endpoint survival conditioning destroy?

For nearest-neighbour percolation both questions admit exact inequalities.

### 4.1 FKG gives adjacent comparability of the two-point function

Fix a signed coordinate unit vector `e`. The events `{0 <-> x}` and `{edge (x,x+e) is open}` are increasing. By FKG,

\[
\tau_p(x+e)
\ge \mathbb P_p(0\leftrightarrow x,\{x,x+e\}\text{ open})
\ge p\,\tau_p(x).
\]

Interchanging `x` and `x+e` gives

\[
\boxed{p\,\tau_p(x)\le\tau_p(x+e)\le p^{-1}\tau_p(x).}
\tag{4.1}
\]

Hence, with

\[
a_p:=\frac{1-p}{1+p},
\]

we have pointwise

\[
|r_p(x+e)-r_p(x)|
\le a_p\,[r_p(x+e)+r_p(x)].
\]

After summation,

\[
\boxed{
d_{\rm TV}(r_p,\tau_e r_p)\le a_p.
}
\tag{4.2}
\]

Convolution preserves (4.1), so the same bound holds for `q_p` and every convolution power of `q_p`. Therefore the unit-shift overlap satisfies

\[
H_e(f):=\sum_x\min\{f(x),f(x-e)\}
=1-d_{\rm TV}(f,\tau_e f)
\ge\frac{2p}{1+p}
\tag{4.3}
\]

for `f=q_p*q_p`.

A feasible fractional matching is

\[
\eta_x:=\frac12\min\{f(x),f(x+e)\},
\]

because `eta_x+eta_{x-e}<=f(x)`. Thus the **unconditioned two-middle-increment law** has

\[
\boxed{
\mathfrak m_e(q_p*q_p)\ge\frac{p}{1+p}.
}
\tag{4.4}
\]

This is positive for every `p>0`, while the `p=0` checkerboard obstruction is recovered continuously as the bound vanishes.

### 4.2 Exact transfer from the unconditioned law to a surviving endpoint bridge

Fix endpoints `A,B`, write

\[
R(x):=(q_p*q_p)(x),\qquad \zeta(x):=\zeta_{A,B}(x),\qquad s:=\sum_x\zeta(x)=P_3^\otimes(A,B).
\]

Conditioned on the endpoints, the two middle states are still iid with law `pi_p`; survival only deletes pairs. Consequently

\[
0\le\zeta(x)\le R(x),\qquad \sum_x[R(x)-\zeta(x)]=1-s.
\tag{4.5}
\]

For any nonnegative `g<=f`,

\[
H_e(g)\ge H_e(f)-2\|f-g\|_1,
\tag{4.6}
\]

because each deleted mass can damage the two neighboring minima by at most its own amount. Combining (4.3)–(4.6), and using matching mass at least half of shift overlap, yields the exact bridge-transfer inequality

\[
\boxed{
\mathfrak m_e(A,B)
\ge
\left[\frac{p}{1+p}-(1-s(A,B))\right]_+.
}
\tag{4.7}
\]

More generally, if the actual computable unconditioned overlap `H_e(q_p*q_p)` is used rather than the FKG lower bound,

\[
\boxed{
\mathfrak m_e(A,B)
\ge
\frac12\left[H_e(q_p*q_p)-2(1-s(A,B))\right]_+.
}
\tag{4.8}
\]

Equation (4.7) is not by itself enough for source Proposition 3.25: the crude FKG form becomes positive only when

\[
s(A,B)>\frac1{1+p},
\]

whereas the source's admissible survival threshold `rho` can be much smaller. But it is a sharp structural reduction: **endpoint conditioning is now the only place where the matching smoothness can be lost.** Any improvement of the unconditional shift overlap, or any proof that survival deletions are not adversarially aligned with the shift pairs, immediately improves the source Fourier constant.

### 4.3 A global unconditional quadratic Fourier gap with explicit constants

The same comparability gives a direct torus estimate. Fourier transforming `r_p-\tau_e r_p` gives

\[
2|\sin(\kappa_i/2)|\,|\widehat r_p(\kappa)|
\le \|r_p-\tau_e r_p\|_1
\le2a_p,
\]

so

\[
\boxed{
|\widehat r_p(\kappa)|
\le \min\left\{1,\frac{a_p}{|\sin(\kappa_i/2)|}\right\}.
}
\tag{4.9}
\]

This controls every nonzero lattice-parity corner. Near the origin the nearest-neighbour averaging factor `A_d` supplies the curvature.

There is also an elementary source-regime lower bound on `p`. Counting self-avoiding/open paths crudely by all nonbacktracking paths gives, for `p<1/(2d-1)`,

\[
\chi(p)
\le1+\frac{2dp}{1-(2d-1)p}.
\tag{4.10}
\]

At `p=1/(4d)` the right side is strictly below `2`. Therefore

\[
\boxed{\chi(p)\ge2\quad\Longrightarrow\quad p>\frac1{4d}.}
\tag{4.11}
\]

For `d=7,8,9,10`, set

\[
\alpha_d:=\frac{4d-1}{4d+1},\qquad
s_0:=\cos(\pi/12),
\]

and

\[
c_d:=\min\left\{
\frac{2}{d\pi^2},
\frac{36(1-\sqrt3/2)}{25\pi^2},
\frac{1-\alpha_d/s_0}{\pi^2}
\right\}>0.
\tag{4.12}
\]

### Proposition 4.1 (unconditional global Fourier gap)

For nearest-neighbour bond percolation on `Z^d`, `d in {7,8,9,10}`, at every subcritical `p` with `chi(p)>=2`,

\[
\boxed{
|\widehat q_p(\kappa)|
\le1-c_d\|\kappa\|_\infty^2,
\qquad \kappa\in[-\pi,\pi]^d.
}
\tag{4.13}
\]

The constants are approximately

\[
\begin{array}{c|c}
d&c_d\\\hline
7&0.003659941715150292\\
8&0.002783073100764769\\
9&0.002095797700300440\\
10&0.001542624816999892
\end{array}
\]

#### Proof

Let `t=||kappa||_∞` and use (1.2).

If `t<=5pi/6` and `A_d(kappa)>=0`, at least one coordinate has absolute value `t`, while every other cosine is at most one. Hence

\[
A_d(\kappa)
\le1-\frac{1-\cos t}{d}
\le1-\frac{2t^2}{d\pi^2}.
\]

If instead `A_d(kappa)<0`, then every `cos kappa_j>=cos t>=-sqrt(3)/2`, so

\[
|A_d(\kappa)|\le\sqrt3/2
\le1-\frac{36(1-\sqrt3/2)}{25\pi^2}t^2.
\]

Since `|rhat_p|<=1`, these two cases give (4.13) in the middle/low-frequency region.

Now let `t>=5pi/6` and choose `i` with `|kappa_i|=t`. By (4.11), `p>1/(4d)`, hence

\[
a_p=\frac{1-p}{1+p}\le\alpha_d.
\]

Also `|sin(kappa_i/2)|>=cos(pi/12)=s_0`. Equation (4.9) therefore gives

\[
|\widehat q_p(\kappa)|
\le|\widehat r_p(\kappa)|
\le\frac{\alpha_d}{s_0}<1.
\]

Since `t<=pi`,

\[
\frac{\alpha_d}{s_0}
\le1-\frac{1-\alpha_d/s_0}{\pi^2}t^2.
\]

Taking the minimum of the three constants proves (4.13). `square`

This proposition has the same global quadratic *form* that the source ultimately needs for its Fourier product, but only for the **unconditioned iid increment law**. It does not prove Proposition 3.25 because endpoint survival conditioning can delete Fourier-smoothing pairs. The new point is that no additional lattice aperiodicity theorem is needed for `q_p`: the unconditional law already has an explicit global gap throughout the source's large-susceptibility regime.

## 5. What moved conceptually, and what did not

The fixed source metric did not move:

\[
\boxed{M_A:0\to0.}
\]

No dimension is certified, so the status remains `PARTIAL / OPEN`. The result of this run is a sharper localization of the remaining obligation:

- a fixed two-increment matching criterion can genuinely fail by parity;
- a one-bit randomized block length removes that obstruction exactly;
- at every positive `p`, FKG already gives quantitative unit-shift overlap of the unconditional increment law;
- in the source large-susceptibility regime, the unconditional increment law has an explicit global quadratic Fourier gap on the entire torus;
- therefore the unresolved hard part is specifically **how the endpoint cut/survival conditioning deletes the naturally present shift pairs**.

The next attack should not build a larger checker for the same F2 quantity. The only Section-B methods not yet used on this Blanc–Renaudie target are **#5, #22, #23**. The useful next run is therefore: add an interpolation parameter that progressively switches on the endpoint cut filter and differentiate the shift-overlap loss (#5); read failed/local-modification routes in the source and adjacent Markov local-CLT literature specifically for conditioning-stable aperiodicity (#22); and assume the opposite of the source's surgery philosophy by trying to prove that the raw survival filter itself preserves a fixed fraction of adjacent displacement pairs (#23).

## 6. Model-control and permission status

The model-control limitation is unchanged. The exposed task interface supports title/prompt, schedule/timing, enablement and timing mode, but exposes no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. `GPT-6 / maximum` therefore remains prompt-only here. Enforcing it would require an authorized product/workspace/API/admin surface with persistent model and reasoning fields plus run attestation.

The historical P26 `You cannot modify this task` event was later superseded by a successful update from another authorized context; it is not evidence of a current P26 block. A live task-edit denial must be handled through the task's owning authorized context, an authorized ownership/admin transfer, or platform support. Permission bypass or duplicate-task creation is not an acceptable workaround.

## 7. Ledger delta

```yaml
ledger_delta:
  worker: R09
  deployment: NEW-METHODS-2026-09-16
  active_claim: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  source_status: OPEN_CURRENT
  status_before: OPEN
  status_after: OPEN
  metric_name: M_A
  metric_before: 0
  metric_after: 0
  movement: NO_MOVEMENT
  stagnation_count: UNKNOWN
  methods: [2, 9, 29]
  tang_status: RETIRED_FROZEN_REFUTED
  results:
    - exact p=0 parity obstruction for fixed two-middle shift matching
    - exhaustive exact F2 positive-p negation search in d=7,8,9,10; no zero-margin counterexample
    - exact randomized 2/3-step p=0 deperiodization matching formula
    - FKG adjacent-ratio and unit-shift-TV inequalities for normalized two-point/increment laws
    - exact survival-filter transfer inequality for directional matching mass
    - explicit unconditional global quadratic Fourier gap for d=7,8,9,10 when chi>=2
  artifacts:
    - artifacts/R09/20260919T0033Z_blanc_matching_parity_f2_7e4c2a.py
    - artifacts/R09/20260919T0033Z_blanc_matching_parity_f2_7e4c2a.out
  next_methods: [5, 22, 23]
```
