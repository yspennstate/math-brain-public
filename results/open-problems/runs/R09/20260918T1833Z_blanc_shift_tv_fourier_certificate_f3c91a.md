Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #11, #17, #19.**

# R09 — Blanc-Renaudie mean-field `d=7,8,9,10`: shift-TV / matching certificate for the high-frequency step

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime/control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long execution guarantee.

The task-management schema exposed here still has no bindable model-family field and no reasoning-effort field; it exposes task text/schedule/enablement controls, not a persistent model selector or authenticated run attestation. I made no scheduler change. The current root ledger also corrects an older operational detail: P26's historical `You cannot modify this task` error was later followed by a successful full prompt update from another authorized context, so that exact P26 denial is not a current failure in that context. The same ledger records that R-series edits were denied in that P/C context. The lawful remedy for a task that still returns a permission denial is the owning/otherwise-authorized context, an authorized ownership/admin transfer, or platform support; no duplication or permission bypass is warranted.

## 2. Continuity, source status, ownership, and metric

Before research I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive R09 claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the newest complete R09 report `runs/R09/20260918T1738Z_blanc_finite_perron_lambda_9c41e7.md`, and the neighboring C0064 intake/attempt evidence. The exact source remains exclusively R09-owned. A current repository search for arXiv `2609.20764` returns the R09 claim/reports plus a neighboring admission screen explicitly noting that the source is already claimed; there is no ownership conflict.

Fresh public source/status queries on 2026-09-18 recover Arthur Blanc-Renaudie, *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764, submitted 2026-09-17 and updated 2026-09-18. No later source-matching proof of the nearest-neighbor `d=7,8,9,10` cases was recovered in the bounded dated search. This is negative search evidence, not a worldwide novelty certificate. The source itself still identifies nearest-neighbor `d>=11` as known and `7<=d<=10` as the remaining numerical-proof regime.

The related intake C0064 remains distinct: it asks for the Fourier infrared bound in nearest-neighbor percolation for every `d>6`; its old C0064-A001 attempt stopped because the NoBLE/lace bootstrap did not close in `d=7,...,10`. I do not identify that Fourier statement with Blanc-Renaudrie's pointwise asymptotic without a written implication.

The frozen metric is

\[
M_A:=\#\{d\in\{7,8,9,10\}: \text{a complete rigorous certificate of Blanc-Renaudrie Theorem 1.1(a) has been obtained}\}.
\]

No dimension is certified in this run:

\[
\boxed{M_A:0\longrightarrow0.}
\]

The result below attacks the **remaining Fourier/local-CLT bottleneck** isolated in the previous run. It does not by itself certify a dimension.

## 3. Source point attacked this run

The source defines i.i.d. pointed clusters under `P_p^otimes` with

\[
\mathbb P_p^\otimes(\vec A_i=\vec A)=\frac{\mu_p(\vec A)}{\Omega\chi(p)},
\]

and the killed chain uses `T_cut`. For endpoint states `\vec A_0,\vec A_3`, it defines

\[
\Upsilon_{3,\kappa}(\vec A_0,\vec A_3)
=
\left|
\mathbb E_p^\otimes\left[
 e^{i\langle \kappa,\Delta(\vec A_1)+\Delta(\vec A_2)\rangle}
\mid \vec A_0,\vec A_3,T_{\rm cut}>3
\right]
\right|.
\]

Proposition 3.25 asks, roughly, for a uniform quadratic gap

\[
\Upsilon_{3,\kappa}\le 1-c\|\kappa\|_\infty^2
\]

outside an arbitrarily small exceptional set of endpoint pairs whose three-step survival probability is non-negligible. The source proves this through local modifications. The previous R09 run identified this as one of the two remaining expensive constant-producing steps.

This run gives a different exact finite certificate for that quadratic Fourier gap.

---

## 4. Method #11 — DUALIZE: the Fourier gap is a weighted matching / vertex-cover problem

### 4.1 A directional matching functional

Let `q` be any probability mass function on `Z^d`. For a coordinate `i`, write `e_i` for the corresponding unit vector and define

\[
\boxed{
\mathfrak m_i(q)
:=
\sup\left\{
\sum_{y\in\mathbb Z^d}\eta_y:
\eta_y\ge0,\quad
\eta_y+\eta_{y-e_i}\le q_y\ \forall y
\right\}.
}
\tag{4.1}
\]

For finite-support rational `q`, this is a rational linear program.

The constraint says that a submeasure `eta` and its unit translate can both be removed from `q`. If `m=sum eta_y`, then

\[
q=\eta+\tau_{e_i}\eta+r,
\qquad r\ge0,
\qquad \|r\|_1=1-2m.
\]

### Theorem 4.1 — matching-to-Fourier gap

For every probability mass function `q` on `Z^d`, every `kappa in [-pi,pi]^d`, and every coordinate `i`,

\[
\boxed{
|\widehat q(\kappa)|
\le
1-\frac{\mathfrak m_i(q)}{\pi^2}\,\kappa_i^2.
}
\tag{4.2}
\]

Consequently, with

\[
\mathfrak m_*(q):=\min_{1\le i\le d}\mathfrak m_i(q),
\]

we have

\[
\boxed{
|\widehat q(\kappa)|
\le
1-\frac{\mathfrak m_*(q)}{\pi^2}\|\kappa\|_\infty^2.
}
\tag{4.3}
\]

#### Proof

Take any feasible `eta` in (4.1), of mass `m`. Since `q=eta+tau_{e_i}eta+r`,

\[
\widehat q(\kappa)
=(1+e^{i\kappa_i})\widehat\eta(\kappa)+\widehat r(\kappa).
\]

Therefore, because `|hat eta|<=m` and `|hat r|<=1-2m`,

\[
|\widehat q(\kappa)|
\le
2m\cos(|\kappa_i|/2)+(1-2m)
=1-2m\bigl(1-\cos(|\kappa_i|/2)\bigr).
\]

For `|t|<=pi`,

\[
1-\cos(|t|/2)\ge \frac{t^2}{2\pi^2},
\]

so

\[
|\widehat q(\kappa)|\le1-m\kappa_i^2/\pi^2.
\]

Take the supremum over feasible `eta` to obtain (4.2). For (4.3), choose a coordinate `i` with `|kappa_i|=||kappa||_infty`. `square`

### 4.2 Exact dual

For finite-support `q`, (4.1) is a capacitated fractional matching LP on the graph whose edges are the pairs `{y,y+e_i}`. Its exact LP dual is

\[
\boxed{
\mathfrak m_i(q)
=
\min\left\{
\sum_y q_y s_y:
 s_y\ge0,\quad s_y+s_{y+e_i}\ge1\ \forall y
\right\}.
}
\tag{4.4}
\]

The directional graph is bipartite (indeed a disjoint union of one-dimensional chains). Hence the weighted vertex-cover polytope is integral, so an optimum may be taken with `s_y in {0,1}`. Thus `m_i(q)` is exactly the minimum `q`-weight vertex cover of those directional chains. It can be computed by elementary dynamic programming chain by chain; a general LP solver is unnecessary.

This is the useful dualization: the source's analytic high-frequency contraction can be tested by a finite weighted vertex-cover calculation on the **three-step displacement law**.

### 4.3 Stability under truncation

A second consequence of the dual form is

\[
\boxed{
|\mathfrak m_i(q)-\mathfrak m_i(q')|
\le d_{\rm TV}(q,q').
}
\tag{4.5}
\]

Indeed one may restrict dual feasible functions to `0<=s<=1` by clipping, and expectations of such functions differ by at most total variation. Taking the infimum in both directions proves (4.5).

This one-Lipschitz property is what makes an exact finite truncation certificate possible.

---

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the matching margin is a standard lattice-smoothness quantity

The directional LP has a simple lower bound. Put

\[
\eta_y=\frac12\min(q_y,q_{y+e_i}).
\]

Then

\[
\eta_y+\eta_{y-e_i}\le q_y,
\]

so it is feasible, and

\[
\boxed{
\mathfrak m_i(q)
\ge
\frac12\sum_y\min(q_y,q_{y+e_i})
=
\frac12\bigl(1-d_{\rm TV}(q,\tau_{e_i}q)\bigr).
}
\tag{5.1}
\]

Therefore Theorem 4.1 immediately gives the cruder but very transparent certificate

\[
\boxed{
|\widehat q(\kappa)|
\le
1-rac{1-d_{\rm TV}(q,\tau_{e_i}q)}{2\pi^2}\kappa_i^2.
}
\tag{5.2}
\]

The literature search found this same **shift-total-variation** quantity under the standard name of a lattice smoothness coefficient in local limit / discrete approximation work: for an integer-valued `W`, `S_1(L(W))=2 d_TV(L(W),L(W+1))` is explicitly used as a smoothness measure in local-limit theorems. Thus the quantity appearing here is not an arbitrary new diagnostic: it is exactly the standard obstruction to lattice smoothing, now applied coordinatewise to Blanc-Renaudrie's conditional two-step displacement law.

I did not find, in the bounded search, the exact inequality (4.2) stated in this matching form; I therefore make **no priority claim** for the abstract Fourier lemma. The relevant point for R09 is the source-specific reduction of Proposition 3.25 to an exact shift-overlap / vertex-cover certificate.

I also rechecked the nearest solved percolation case. Fitzner--van der Hofstad's 2017 proof for nearest-neighbor `d>=11` is computer-assisted and uses rigorous simple-random-walk integrals plus a NoBLE bootstrap. Their general NoBLE paper records, for percolation at `d=11`, a small example bootstrap matrix with largest eigenvalue about `0.073`. But neither that paper nor the bounded current search supplies a rigorous `d=7,8,9,10` triangle/cut constant that can simply be inserted into Blanc-Renaudrie's Remark 3.6. The old C0064 attempt encountered the same dimensional obstruction. So this literature route did **not** move `M_A`.

---

## 6. Method #19 — MAKE IT AN ALGORITHM: a finite exact certificate for Proposition 3.25 at fixed `p`

This is the main constructive result of the run.

Fix a rational `p<pc`. Let `S` be a finite Simon--Lieb block with

\[
a=\varphi_p(S)<1.
\]

The previous R09 run proved

\[
\chi_S(p)\le\chi(p)\le U:=\frac{\chi_S(p)}{1-a}.
\tag{6.1}
\]

Choose finite pointed-cluster sets `F` (allowed intermediate states) and `G` (allowed endpoint states). Define their raw masses

\[
M_F:=\sum_{\vec A\in F}\mu_p(\vec A),
\qquad
M_G:=\sum_{\vec A\in G}\mu_p(\vec A).
\]

Since `P_p^otimes(A)=mu_p(A)/(Omega chi(p))`, (6.1) gives the exact tail upper bounds

\[
\boxed{
\bar t_F:=1-\frac{M_F}{\Omega U}
\ge \mathbb P_p^\otimes(\vec A\notin F),
\qquad
\bar t_G:=1-\frac{M_G}{\Omega U}
\ge \mathbb P_p^\otimes(\vec A\notin G).
}
\tag{6.2}
\]

(For valid exact inputs the displayed right-hand lower fractions cannot exceed one.)

### 6.1 Exact truncated three-step law

For fixed endpoints `A0,A3 in G`, define, for each displacement `y in Z^d`,

\[
r_y^{F}(A_0,A_3)
:=
\sum_{A_1,A_2\in F}
\mu_p(A_1)\mu_p(A_2)
\,1_{(A_0,A_1),(A_1,A_2),(A_2,A_3)\notin C_{\rm cut}}
\,1_{\Delta(A_1)+\Delta(A_2)=y}.
\tag{6.3}
\]

Let `R_F=sum_y r_y^F`. When `R_F>0`, put

\[
q^F_{A_0,A_3}(y)=r_y^F/R_F.
\tag{6.4}
\]

The factors `(Omega chi(p))^{-2}` cancel in this conditional law. For rational `p` and finite clusters, every `mu_p(A)` is a finite reliability polynomial evaluated at `p`; hence (6.3)--(6.4) are exact rational quantities.

For each coordinate compute

\[
m_i^F(A_0,A_3)=\mathfrak m_i(q^F_{A_0,A_3})
\]

by the exact chain vertex-cover dynamic program from Section 4.

### Proposition 6.1 — finite truncation certificate for the source's three-step Fourier contraction

Fix `rho,rho'>0`. Set

\[
\delta_F:=\frac{2\bar t_F}{\rho}.
\tag{6.5}
\]

For an endpoint pair `(A0,A3) in G^2`, call it **potentially relevant** if the trivial finite/tail upper bound does not already force

\[
\mathbb P_p^\otimes(T_{\rm cut}>3\mid A_0,A_3)\le\rho.
\]

A computable sufficient irrelevance test is

\[
\frac{R_F(A_0,A_3)}{(\Omega\chi_S(p))^2}+2\bar t_F\le\rho,
\tag{6.6}
\]

because `chi(p)>=chi_S(p)` and any surviving path omitted by `F^2` requires at least one of the two intermediate states to lie outside `F`.

Suppose:

1. `2\bar t_G<=rho'`;
2. for every potentially relevant endpoint pair in `G^2`, `R_F>0` and

\[
\boxed{
\min_i m_i^F(A_0,A_3)-\delta_F\ge m_0>0.
}
\tag{6.7}
\]

Then, for every `kappa in [-pi,pi]^d`,

\[
\boxed{
\mathbb P_p^\otimes\left(
\Upsilon_{3,\kappa}(A_0,A_3)
>
1-\frac{m_0}{\pi^2}\|\kappa\|_\infty^2,
\quad
\mathbb P_p^\otimes(T_{\rm cut}>3\mid A_0,A_3)>\rho
\right)
\le\rho'.
}
\tag{6.8}
\]

Thus the conclusion of Blanc-Renaudrie Proposition 3.25 at this fixed `p,rho,rho'` is certified by finitely many exact cluster probabilities and finitely many exact weighted vertex-cover computations.

#### Proof

First, by independence of the endpoint states under `P_p^otimes`,

\[
\mathbb P(A_0\notin G\text{ or }A_3\notin G)\le2\bar t_G\le\rho'.
\tag{6.9}
\]

Consider endpoints inside `G`. If (6.6) holds, their full three-step survival probability is at most `rho`, so they cannot contribute to the event in (6.8).

Now consider a pair in `G^2` whose full survival probability exceeds `rho`. Conditional on the endpoints, the intermediate states remain two independent `P_p^otimes` draws before imposing survival. Hence

\[
\mathbb P(A_1\notin F\text{ or }A_2\notin F)\le2\bar t_F.
\]

Conditioning additionally on survival, whose probability is `>rho`, shows that the omitted conditional mass is at most

\[
\delta_F=2\bar t_F/\rho.
\]

Therefore, if `q` denotes the full conditional law of `Delta(A1)+Delta(A2)` and `q^F` the law in (6.4),

\[
d_{\rm TV}(q,q^F)\le\delta_F.
\]

By (4.5), for every coordinate,

\[
\mathfrak m_i(q)\ge m_i^F-\delta_F\ge m_0.
\]

Theorem 4.1 then gives

\[
\Upsilon_{3,\kappa}=|\widehat q(\kappa)|
\le1-(m_0/\pi^2)\|\kappa\|_\infty^2.
\]

Thus no endpoint pair inside `G^2` with survival `>rho` belongs to the bad event. By (6.9), the bad event has probability at most `rho'`. `square`

### 6.2 Why this is a real algorithm, not another qualitative lemma

For a fixed rational `p`, every item in Proposition 6.1 is finite:

- `a`, `chi_S`, and the finite-volume connection probabilities are finite reliability computations;
- each cluster probability `mu_p(A)` is an exact finite polynomial evaluation;
- `M_F,M_G`, every `r_y^F`, and every irrelevance test (6.6) are exact rationals;
- each directional matching margin is a minimum-weight vertex cover on disjoint finite chains and is exact;
- no unknown infinite-volume `chi(p)` appears except through the certified interval in (6.1).

Moreover, the same construction can be made **uniform on a rational compact interval of p** without sampling the interval: all finite cluster probabilities are polynomials in `p`, and every candidate finite matching / tail inequality is semialgebraic. A fixed feasible matching certificate and fixed endpoint classification can therefore be verified over an interval by exact polynomial-sign methods (Sturm sequences, Bernstein subdivision, or rational interval arithmetic). This is an algorithmic route to the uniformity that the source theorem ultimately needs.

I have **not** executed the enormous cluster enumeration required to make `bar t_F` and `bar t_G` small near criticality, so no finite source claim is asserted and no checker-only artifact was manufactured this run.

---

## 7. A second byproduct: a universal fixed-p Doeblin minorization (and why it is not enough)

The preceding matching route also suggested checking whether the source's Theorem 3.14 mixing step can be bypassed by an elementary common atom.

Let `U_1` be the `Omega` live pointed singleton states. For every live source state `A` and every `B in U_1`, the transition is non-cut (this is the same singleton observation used in the previous R09 size-two calculation). Each singleton has

\[
\mu_p(B)=(1-p)^\Omega.
\]

The source's Lemma 3.1 gives

\[
\frac{\inf h_p}{\|h_p\|_\infty}
\ge\frac{(1-p)^\Omega}{\Omega\chi(p)},
\qquad \lambda_p\le1.
\]

Using the exact Doob kernel

\[
P_p^h(A,B)=
\frac{h_p(B)}{\lambda_p h_p(A)}
\frac{\mu_p(B)}{\Omega\chi(p)}
1_{(A,B)\notin C_{\rm cut}},
\]

we obtain, uniformly in every live source `A` and every singleton target `B`,

\[
P_p^h(A,B)
\ge
\frac{(1-p)^{2\Omega}}{\Omega^2\chi(p)^2}.
\]

Summing over the `Omega` singleton targets gives the common one-step minorization mass

\[
\boxed{
\varepsilon_{\rm sing}(p)
=
\frac{(1-p)^{2\Omega}}{\Omega\chi(p)^2}.
}
\tag{7.1}
\]

Hence ordinary Doeblin coupling yields, for every fixed `p<pc`,

\[
\boxed{
\|P_p^{h,k}(A,\cdot)-v_p\|_{\rm TV}
\le(1-\varepsilon_{\rm sing}(p))^k.
}
\tag{7.2}
\]

This is a completely explicit fixed-p mixing rate. But it also explains why the obvious atom route cannot replace Theorem 3.14 in the source's quantitative bootstrap: `epsilon_sing(p)` decays like `chi(p)^{-2}` as `p` approaches criticality, while Theorem 3.14 needs a contraction base bounded away from one once `chi(p)` is large, with constants depending only on the structural parameters. Thus the singleton route is useful as a sanity check and fallback fixed-p certificate, but **not** as the uniform source-scale mixing input.

This negative result changes the next search: for Theorem 3.14, one needs a common minorizing family carrying a constant fraction of the pointed-cluster law, or a different spectral/coupling argument; a bounded collection of obvious atoms plus only the source's global `h` ratio is structurally too weak.

---

## 8. What moved, what did not, and the remaining bottleneck

The fixed source metric did not move:

\[
\boxed{M_A=0.}
\]

What did move mathematically is the bottleneck map:

- the previous run made the Perron-eigenvalue lower bound a finite exact problem;
- this run makes the **three-step Fourier contraction at fixed p** a finite exact weighted-matching problem with a rigorous tail completion;
- the elementary singleton minorization shows why the most naive direct replacement for Theorem 3.14 cannot be uniform near criticality.

Thus the principal remaining quantitative obstruction is now even more concentrated: obtain a **uniform near-critical mixing certificate** (Theorem 3.14 scale) without the source's expensive local-modification constants, and make the Proposition 6.1 finite families large enough / uniform enough that their tail budgets are practical.

The most attractive next target is not another spectral checker. It is to search for a regeneration or conductance argument on a **large good-state set of constant `P_p^otimes` mass**, because that is exactly what the singleton failure shows is required for a `chi`-uniform contraction.

Reserved fresh moves for the next ordinary research run: **#6, #13, #28** — deform from the exactly solvable singleton/two-vertex chain toward a constant-mass good set; identify a monotone regeneration/conductance quantity; and prove the desired mixing for typical cluster states while quantifying the exceptional mass.

## 9. Literature / ownership record for this run

Dated checks performed 2026-09-18:

- exact arXiv ID/title search for `2609.20764`: source recovered, submitted 2026-09-17 and updated 2026-09-18; no later source-matching resolution found in the bounded search;
- Fitzner--van der Hofstad 2017 / NoBLE search: rigorous nearest-neighbor mean-field proof remains `d>=11`; computer-assisted numerical infrastructure exists, but no rigorous `d=7,...,10` plug-in constants were found;
- lattice local-limit smoothness search: shift total variation `d_TV(L(W),L(W+1))` is a standard smoothness quantity in local-limit / discrete approximation literature, supporting the reformulation in Section 5 but not establishing priority for Theorem 4.1;
- repository exact-ID search: exclusive R09 claim remains canonical; neighboring screen records it as already claimed; no competing owner found.

No public posting, email, Drive action, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-file edit was made.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  active_claim: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  source: arXiv:2609.20764
  metric: M_A
  before: 0
  after: 0
  movement: no
  stagnation_count: UNKNOWN
  status: PARTIAL_OPEN_CURRENT
  methods_used: [11, 17, 19]
  new_results:
    - directional_matching_to_Fourier_gap_theorem
    - exact_weighted_vertex_cover_dual
    - TV_Lipschitz_stability_of_matching_margin
    - finite_tail_completed_fixed_p_certificate_for_Proposition_3_25
    - explicit_fixed_p_singleton_Doeblin_minorization
  source_dimensions_certified_this_run: []
  checker_created: false
  checker_reason: analytic_theorems_and_algorithm_only_no_new_finite_instance_claim
  next_methods: [6, 13, 28]
  remaining_obligation: >-
    Build a chi-uniform near-critical mixing certificate and instantiate the finite
    Fourier-matching/tail certificate strongly enough to satisfy the full quantitative
    constant chain for at least one of d=7,8,9,10.
```
