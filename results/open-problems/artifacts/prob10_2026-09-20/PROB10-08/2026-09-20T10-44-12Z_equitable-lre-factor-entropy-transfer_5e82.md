Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but this runtime exposes no authenticated model/effort selector or telemetry establishing that setting.

# PROB10-08 artifact — equitable LRE factors suffice: entropy transfer through non-cover block quotients

Status: **PROVED restricted source-admissible class / Salez Problem 2.3 remains OPEN / PARTIAL / independent validation pending / worldwide novelty UNVERIFIED**.

Exact source target: Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3: every bounded-degree vertex-transitive spectral-expander sequence exhibits total-variation cutoff for the rate-one continuous-time simple random walk
\[
\mathsf H_t^G=e^{t(P_G-I)}.
\]
This is not the already-posted Abelian Cayley/product-condition target.

Primary current lead: Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. On 20 September 2026 the current arXiv record still exposes only v1; no v2/correction/erratum surfaced in the bounded current check. The proof uses long-range expansion before the ordinary spectral cleanup: Lemma 3.2 transfers maximal tree-rate growth to the oriented-edge NBRW state space, Lemma 3.3 converts that growth to Shannon entropy, Proposition 3.1 obtains endpoint entropy `log m - O(log log m)`, and Lemma 3.4 then uses spectral expansion to clean the entropy deficit. The theorem below transfers precisely that endpoint entropy through a much weaker object than a graph covering.

## 1. New idea before any coding

The earlier R16 quotient theorem required a same-degree graph covering. That requirement is much stronger than what the entropy proof actually uses. For an upper bound, one only needs:

1. a **Markov factor** whose endpoint has near-maximal entropy on the Altschuler scale;
2. equal factor fibers, so losing the hidden coordinate costs at most `log k` entropy; and
3. a spectral gap upstairs, to dissipate that residual `log k` information deficit.

A graph covering gives such a factor, but so does any equitable block system, including quotients with holding and multiple edges and with no local bijection. The theorem below makes this exact under the source's rate-one continuous-time convention.

The lower bound also transfers automatically because total variation decreases under projection. Thus the only price for replacing long-range expansion upstairs by long-range expansion **on an equitable quotient** is an additive entropy-cleanup time of order `log k`, where `k` is the block size.

## 2. Exact hypotheses

Fix constants
\[
d\ge3,\qquad c>0,\qquad \gamma>0,\qquad \alpha_0>0.
\]
For each `n`, let:

- `G_n=(V_n,E_n)` be a finite connected `D_n`-regular vertex-transitive graph, with `D_n` uniformly bounded;
- `N_n=|V_n|`, and `P_n` its simple-random-walk transition matrix;
- the one-sided spectral gap satisfy
  \[
  1-\lambda_2(P_n)\ge\gamma;
  \tag{2.1}
  \]
- `H_n=(W_n,F_n)` be a finite connected `d`-regular `c`-long-range expander, with `m_n=|W_n|\to\infty`, transition matrix `Q_n`, and `q=d-1`;
- `\phi_n:V_n\to W_n` be a surjection with every fiber of the same size
  \[
  k_n=\frac{N_n}{m_n};
  \tag{2.2}
  \]
- for some `\alpha_n\in[\alpha_0,1]`, the one-step walk on `G_n` lump exactly to a slowed SRW on `H_n`:
  \[
  (\phi_n)_*P_n(x,\cdot)
  =(1-\alpha_n)\delta_{\phi_n(x)}+\alpha_n Q_n(\phi_n(x),\cdot)
  \qquad(x\in V_n).
  \tag{2.3}
  \]

Condition (2.3) is the strong-lumpability/equitable-factor condition. It does **not** require a graph covering: edges may remain within a fiber, several upstairs edges may project to the same quotient edge, and no local bijection is assumed.

Write
\[
L_n=\log_q m_n,
\qquad
v=\frac{d-2}{d},
\qquad
T_n=\frac{L_n}{v}=\frac d{d-2}\log_q m_n.
\tag{2.4}
\]
All mixing times below refer to the rate-one continuous-time semigroup `e^{t(P-I)}`.

## 3. Main theorem — equitable-factor transfer

### Theorem 3.1

Under the hypotheses of Section 2, for every fixed `\varepsilon\in(0,1/2)` there is a constant
\[
C=C(d,c,\gamma,\alpha_0,\varepsilon)<\infty
\]
such that, for all sufficiently large `n`,
\[
\boxed{
 t_{\rm mix}^{G_n}(1-\varepsilon)
 \ge
 \frac{T_n}{\alpha_n}
 -C\frac{\sqrt{L_n}}{\alpha_n}
 }
\tag{3.1}
\]
and
\[
\boxed{
 t_{\rm mix}^{G_n}(\varepsilon)
 \le
 \frac{T_n}{\alpha_n}
 +C\frac{\sqrt{L_n}}{\alpha_n}
 +C\bigl(\log k_n+\log\log m_n+1\bigr).
 }
\tag{3.2}
\]
Consequently, if
\[
\log k_n=o(\log m_n),
\tag{3.3}
\]
then `(G_n)` exhibits total-variation cutoff and
\[
\boxed{
\frac{t_{\rm mix}^{G_n}(\varepsilon)-t_{\rm mix}^{G_n}(1-\varepsilon)}
     {t_{\rm mix}^{G_n}(1/2)}
=O_{d,c,\gamma,\alpha_0,\varepsilon}
\left(
L_n^{-1/2}+\frac{\log k_n+\log\log m_n+1}{L_n}
\right)=o(1).
}
\tag{3.4}
\]
If more strongly
\[
\log k_n=O(\sqrt{\log m_n}),
\tag{3.5}
\]
then
\[
\boxed{
 t_{\rm mix}^{G_n}(\varepsilon)
 -t_{\rm mix}^{G_n}(1-\varepsilon)
 =O_{d,c,\gamma,\alpha_0,\varepsilon}(\sqrt{\log N_n}).
}
\tag{3.6}
\]
Thus this class attains the R16 exponent floor `W_exp=1/2` whenever (3.5) holds.

### Scope note

This theorem is source-admissible because every `G_n` is assumed vertex-transitive, bounded-degree and uniformly spectrally expanding. The LRE condition is imposed only on the **factor** `H_n`, not on `G_n`. At the theorem-assumption level this strictly extends the earlier R16 graph-cover statement: (2.3) allows holding, edge multiplicities after projection and arbitrary dynamics inside equal fibers. Publication novelty is not claimed; the bounded search did not surface this exact theorem, but negative search is not a novelty certificate.

## 4. Input from Altschuler, and its continuous-time form

Only the following proved input is needed from Altschuler.

For a fixed-degree fixed-`c` LRE graph `H` on `m` vertices, let `K_j(w,\cdot)` be the endpoint law of a length-`j` NBRW and let
\[
j_m=\min\{j\ge1:dq^{j-1}\ge m\}=\log_q m+O_d(1).
\tag{4.1}
\]
Proposition 3.1 of arXiv:2609.14945v1 gives, uniformly in `w` and `j\ge j_m`,
\[
\boxed{
H(K_j(w,\cdot))\ge \log m-C_0\log\log m
}
\tag{4.2}
\]
for `C_0=C_0(d,c)`.

For completeness, we record the exact continuous-time radial consequence because the source problem uses continuous time. Let `\mathsf H_s^H=e^{s(Q-I)}`. Lift the walk to the infinite `d`-regular tree and write `R_s` for the tree distance from the root. Conditional on `R_s=j`, the projected endpoint law is exactly `K_j(w,\cdot)`, hence
\[
\mathsf H_s^H(w,\cdot)=\sum_{j\ge0}\Pr(R_s=j)K_j(w,\cdot).
\tag{4.3}
\]
Away from the root the continuous-time radial process has rate-one jumps `+1` with probability `q/d` and `-1` with probability `1/d`. Boundary visits are tight, so Poissonization of the usual biased-walk CLT gives
\[
\frac{R_s-vs}{\sqrt{s}}\Longrightarrow N(0,1),
\qquad v=\frac{d-2}{d}.
\tag{4.4}
\]
Indeed, for the compound-Poisson increments the variance per unit time is `E[\Delta^2]=1`; the finitely many root corrections are `O_P(1)`.

Set `s=T_m+z\sqrt{L}`, where `L=\log_qm` and `T_m=L/v`. Then
\[
\frac{L-vs}{\sqrt{s}}
\longrightarrow -v^{3/2}z.
\tag{4.5}
\]
The standard lower bound uses a radius `L-h_m` with `h_m\to\infty` and `h_m=o(\sqrt L)`: the corresponding ball has stationary mass `o(1)`, while (4.4) yields the Gaussian lower profile. For the upper bound, use (4.2) on the event `R_{s-r_m}\ge j_m` and then run the quotient chain for
\[
r_m=\lceil(\log\log m)^2\rceil=o(\sqrt L).
\]
The continuous-time kernel `\mathsf H_1^H` is symmetric and all of its nonconstant eigenvalues are at most `e^{-\gamma_H}` in absolute value, where the LRE condition supplies a fixed one-sided gap `\gamma_H>0`. Altschuler's Ozawa entropy-production argument therefore applies to `\mathsf H_1^H`, giving `o(1)` cleanup after `r_m` units. Thus
\[
\boxed{
\sup_w\left|
\|\mathsf H_{T_m+z\sqrt L}^H(w,\cdot)-\pi_H\|_{\rm TV}
-\Phi(-v^{3/2}z)
\right|\to0.
}
\tag{4.6}
\]
We use (4.2), (4.4) and the lower half of (4.6), not a new LRE theorem.

## 5. Exact factor identity in continuous time

Put
\[
\bar P_n=(1-\alpha_n)I+\alpha_nQ_n.
\]
Strong lumpability (2.3) gives, for every integer `r\ge0`,
\[
(\phi_n)_*P_n^r(x,\cdot)=\bar P_n^r(\phi_n(x),\cdot).
\tag{5.1}
\]
Poissonizing term by term,
\[
\begin{aligned}
(\phi_n)_*\mathsf H_t^{G_n}(x,\cdot)
&=e^{-t}\sum_{r\ge0}\frac{t^r}{r!}(\phi_n)_*P_n^r(x,\cdot)\\
&=e^{t(\bar P_n-I)}(\phi_n(x),\cdot)\\
&=e^{\alpha_nt(Q_n-I)}(\phi_n(x),\cdot)\\
&=\mathsf H_{\alpha_nt}^{H_n}(\phi_n(x),\cdot).
\end{aligned}
\tag{5.2}
\]
Equal fibers imply `(\phi_n)_*\pi_{G_n}=\pi_{H_n}`.

This identity is where a graph covering was used in the earlier R16 theorem. Here it follows solely from lumpability.

## 6. Lower bound

Total variation contracts under a measurable map. From (5.2), for every start `x`,
\[
\|\mathsf H_t^{G_n}(x,\cdot)-\pi_{G_n}\|_{\rm TV}
\ge
\|\mathsf H_{\alpha_nt}^{H_n}(\phi_n(x),\cdot)-\pi_{H_n}\|_{\rm TV}.
\tag{6.1}
\]
By (4.6), choose a fixed `A=A(d,c,\varepsilon)>0` so that, for all large `n`,
\[
\inf_w
\|\mathsf H_{T_n-A\sqrt{L_n}}^{H_n}(w,\cdot)-\pi_{H_n}\|_{\rm TV}>1-\varepsilon.
\tag{6.2}
\]
Taking
\[
t=\frac{T_n-A\sqrt{L_n}}{\alpha_n}
\]
in (6.1) proves (3.1).

## 7. The key new step — conditional entropy lifts through any equal-fiber factor

Fix `\varepsilon\in(0,1/2)` and put `\delta=\varepsilon/4`. Choose a fixed positive `A=A(d,c,\delta)` so large that the radial CLT gives, uniformly in the starting quotient vertex,
\[
\Pr\big(R_{T_n+A\sqrt{L_n}}\ge j_{m_n}\big)\ge1-\delta
\tag{7.1}
\]
for all sufficiently large `n`.

Define the upstairs time
\[
u_n=\frac{T_n+A\sqrt{L_n}}{\alpha_n}.
\tag{7.2}
\]
Let `X` have law `\mathsf H_{u_n}^{G_n}(x,\cdot)` and put `B=\phi_n(X)`. By (5.2), the law of `B` is the quotient law at time `T_n+A\sqrt{L_n}`. By (4.3) it has a convex decomposition
\[
\mathcal L(B)=\sum_j p_jK_j(\phi_n(x),\cdot),
\qquad p_j=\Pr(R_{T_n+A\sqrt{L_n}}=j).
\tag{7.3}
\]
We may couple an auxiliary integer `J` to `(X,B)` as follows: first sample `X`, set `B=\phi_n(X)`, and then, whenever `\Pr(B=b)>0`, sample
\[
\Pr(J=j\mid B=b)=\frac{p_jK_j(\phi_n(x),b)}{\Pr(B=b)}.
\tag{7.4}
\]
Then `(J,B)` has exactly the joint law specified by (7.3). Let
\[
E=\{J\ge j_{m_n}\}.
\]
Equation (7.1) gives `\Pr(E)\ge1-\delta`. Conditional on `E`, the law of `B` is a convex combination of `K_j` with `j\ge j_{m_n}`. Entropy is concave, so (4.2) yields
\[
H(B\mid E)\ge\log m_n-C_0\log\log m_n.
\tag{7.5}
\]
Because `B=\phi_n(X)` is a deterministic function of `X`,
\[
H(X\mid E)\ge H(B\mid E).
\tag{7.6}
\]
Let `\nu_n^x=\mathcal L(X\mid E)`. Since the stationary law upstairs is uniform on `N_n=m_nk_n` vertices,
\[
\begin{aligned}
D(\nu_n^x\|\pi_{G_n})
&=\log N_n-H(\nu_n^x)\\
&\le\log k_n+C_0\log\log m_n.
\end{aligned}
\tag{7.7}
\]
This is the central transfer estimate. No local bijection, path lifting, or control of the hidden-fiber dynamics was used.

## 8. Spectral cleanup upstairs

Let
\[
\eta_G=1-e^{-\gamma}>0.
\tag{8.1}
\]
The time-one continuous kernel
\[
K_G:=\mathsf H_1^{G_n}=e^{P_n-I}
\]
is symmetric stochastic. If `\lambda_i(P_n)\le1-\gamma` is nonconstant, its corresponding eigenvalue in `K_G` is
\[
e^{\lambda_i(P_n)-1}\le e^{-\gamma};
\]
all such eigenvalues are positive. Hence `K_G` has absolute spectral gap at least `\eta_G`.

Ozawa's entropy-production inequality in the form used by Altschuler's Lemma 3.4 gives for every law `\rho`
\[
H(\rho K_G)-H(\rho)
\ge\frac{\eta_G}{4}\|\rho-\pi_{G_n}\|_{\rm TV}^2.
\tag{8.2}
\]
Apply this successively to `\rho K_G^i`. Total variation is nonincreasing, so for every integer `r\ge1`,
\[
\frac{\eta_Gr}{4}
\|\rho K_G^r-\pi_{G_n}\|_{\rm TV}^2
\le \log N_n-H(\rho)
=D(\rho\|\pi_{G_n}).
\tag{8.3}
\]
For `\rho=\nu_n^x`, set
\[
\Delta_n:=\log k_n+C_0\log\log m_n+1
\]
and choose
\[
r_n=\left\lceil\frac{16\Delta_n}{\eta_G\varepsilon^2}\right\rceil.
\tag{8.4}
\]
Equations (7.7)--(8.4) imply
\[
\|\nu_n^x\mathsf H_{r_n}^{G_n}-\pi_{G_n}\|_{\rm TV}\le\varepsilon/2.
\tag{8.5}
\]

Before cleanup the full law is a mixture
\[
\mathsf H_{u_n}^{G_n}(x,\cdot)
=p_E\nu_n^x+(1-p_E)\xi_n^x,
\qquad p_E\ge1-\delta.
\tag{8.6}
\]
After another `r_n` units of time, convexity of total variation and the trivial bound `TV\le1` give
\[
\begin{aligned}
\|\mathsf H_{u_n+r_n}^{G_n}(x,\cdot)-\pi_{G_n}\|_{\rm TV}
&\le p_E\,\|\nu_n^x\mathsf H_{r_n}^{G_n}-\pi_{G_n}\|_{\rm TV}+(1-p_E)\\
&\le\varepsilon/2+\varepsilon/4<\varepsilon.
\end{aligned}
\tag{8.7}
\]
This is uniform in `x` and proves (3.2).

## 9. Cutoff ratio and the `1/2` window regime

Assume (3.3). Since `\alpha_n\ge\alpha_0`, the error terms in (3.1)--(3.2) are `o(L_n)`. Thus
\[
t_{\rm mix}^{G_n}(1/2)\sim\frac{T_n}{\alpha_n}\asymp L_n.
\tag{9.1}
\]
Subtracting (3.1) from (3.2) and dividing by (9.1) gives (3.4).

If (3.5) holds, then
\[
\log N_n=\log m_n+O(\sqrt{\log m_n}),
\]
so `\sqrt{L_n}\asymp\sqrt{\log N_n}` and every term in the window bound is `O(\sqrt{\log N_n})`. This proves (3.6).

## 10. Why this is genuinely broader than the earlier graph-cover lemma

A same-degree graph covering `G\to H` forces a local bijection: each upstairs neighbor of `x` projects bijectively to a distinct neighbor of `\phi(x)`. In (2.3) none of this is required.

For example, a block may contain internal edges, producing the holding mass `1-\alpha`; and several upstairs edge-types may project to the same quotient move. In a vertex-transitive graph, any automorphism-invariant equal block system is equitable, so (2.3) is the natural Markov-factor formulation whenever its quotient transition counts happen to be a uniform slowed SRW on `H_n`.

Altschuler's simple two-copy `H_m\square K_2` obstruction to `spectral => LRE` illustrates the distinction: projection onto `H_m` has one within-fiber edge and is not a same-degree graph covering, but it satisfies (2.3) with `k=2` and `\alpha=d/(d+1)`. That particular example is only an illustration and is not counted as fleet progress because fixed products were already understood by R16. The theorem applies much more generally to twisted/equitable extensions with no product decomposition.

## 11. Two routes deliberately rejected in this run

### 11.1 Quotient TV alone is not enough

It is tempting to use only the projected cutoff and the upstairs spectral gap. That cannot control the hidden coordinate. A bounded-degree product of two expanding transitive chains already shows the issue: one factor can have mixed while the other still carries order-one TV distance. The proof above therefore transfers **conditional Shannon entropy**, not merely quotient TV.

This is not a return to the old tensor-product research route; it is a falsification of an insufficient proof step.

### 11.2 The `log k` loss cannot be removed by black-box lumping

Suppose at some time a law is uniform on a set containing one representative from each of `m=N/k` blocks. Without using additional fiber structure, bounded degree alone requires order `log k` further path entropy before a typical trajectory can reach a positive fraction of all `N` vertices.

A simple support version makes the obstruction explicit. For a degree-`D` rate-one walk run for time `s`, let `J_s\sim\mathrm{Poisson}(s)` be the number of jumps. Conditional on `J_s\le2s`, from each starting point there are at most
\[
1+D+\cdots+D^{\lfloor2s\rfloor}\le C_DD^{2s}
\]
possible endpoints. Starting from at most `N/k` points, the endpoint lies, except for the Poisson upper tail, in a set of size at most
\[
C_D\frac NkD^{2s}.
\]
Thus if `s\le c_D\log k` with `c_D>0` sufficiently small, that set has stationary mass tending to zero whenever `k\to\infty`, while the walk places probability bounded away from zero there. Therefore an `O(\log k)` black-box cleanup loss is the correct structural scale absent extra information about the fibers. This is precisely why the polynomial-fiber Haiman affine stress family from the preceding R16 runs is not solved by Theorem 3.1.

## 12. Three materially different approaches compared

1. **Equitable-factor Shannon transfer — retained and proved.** Replace the covering hypothesis by exact strong lumpability. Conditional entropy on the quotient-good radial event lifts for free, and the upstairs spectral gap dissipates only the hidden-coordinate deficit `log k`.
2. **Projected TV plus stationary spectral gap — rejected.** It ignores hidden-coordinate information and gives no correct mixing upper bound in general.
3. **Erase the fiber penalty using generic bounded-degree smoothing — rejected by the support obstruction.** Without additional fiber geometry, an order-`log k` cleanup delay is unavoidable in the worst case. Polynomial-size fibers therefore require a genuinely different, internal entropy mechanism rather than another quotient-transfer theorem.

This route does not duplicate P26's Green-shell/biregular-halving program or NM13's oriented-edge/Hodge/orbit program, and it does not restart R16's product-varentropy, synchronous-tensor, moving-weight-Poincare, Hecke-curvature or global-subcommutation routes.

## 13. Source before/after and ledger delta

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk H_t=exp(t(P-I))"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  scope_movement: true
  newly_proved_class:
    - "bounded-degree vertex-transitive spectral expanders with an equal-fiber exact Markov factor onto a fixed-degree LRE graph, alpha>=alpha0, and log fiber=o(log quotient)"
    - "quantitative window O(sqrt(log m)/alpha + log k + log log m)"
    - "if log k=O(sqrt(log m)), window O(sqrt(log N))"
  relation_to_prior_r16: "strict theorem-level extension of same-degree graph-cover transfer to non-cover equitable/lumpable factors"
  independent_audits: 0
  worldwide_novelty: "UNVERIFIED"
```

The numerical R16 metric cannot improve below `1/2`; this run broadens the proved graph class instead of relabeling a constant improvement as metric movement.

## 14. Consumed repository history and ownership fences

Recovered before this proof:

- `operations/PROB10_2026-09-20.md` — current PROB10 contract;
- root `POSTED.md` — the posted Cayley/product-condition paper remains excluded and is not this target;
- `operations/claims/I0112.md` — canonical R16 ownership and frozen metric;
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md` — preserves the actual R16/H0002 successor, Christoph--Morawski--Wigderson Question 5.1, with its all-prefix isotonic/KKT obstruction;
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` and the linked earlier I0112 chain — product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature, local-AEP and global subcommutation failures remain exhausted;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T09-47-50Z_spectral-cancellation-affine-l1_1f6c.md` — isolated-slow-projector positivity barrier and the Haiman affine `L1` interpolation;
- neighboring P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md` — P26 owns the Green-shell/biregular-halving route;
- neighboring NM13 cutoff history through `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md` — NM13 owns arc/Hodge/reversal/orbit routes.

No canonical owner, shared ledger, peer report or historical file is edited by this artifact.

## 15. Tests actually run

No finite mixing plot, Monte Carlo simulation, graph census or finite-size extrapolation was used. The theorem is analytic and has no finite computational core. The only current checks were source/version and prior-art/ownership checks; no negative search is treated as a novelty certificate.

## 16. Remaining full-scope gap

The full Salez conjecture remains open. The theorem removes the **local-cover geometry** from the earlier quotient route, but still requires a quotient that already carries Altschuler's endpoint entropy and a hidden coordinate of entropy `o(log N)`.

The key remaining source-level obligation is therefore unchanged in substance but sharper in location:

> derive `o(log N)` endpoint information deficit directly from vertex transitivity plus ordinary spectral expansion, without assuming a pre-existing LRE factor; or construct a source-admissible counterexample.

For the Haiman affine stress family the natural quotient has polynomial fiber `k=N^{2/5+o(1)}`, so the `log k` loss is macroscopic and Theorem 3.1 deliberately does not claim cutoff there. That family still requires the different internal Shannon/hypocoercive mechanism isolated in the preceding R16 reports.
