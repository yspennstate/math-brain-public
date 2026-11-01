Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but the exposed runtime/scheduler provides no model-family or reasoning-effort selector, so I do not claim otherwise. **no movement — successor metric UNMEASURED -> UNMEASURED; Section-B moves tried: 11, 18, 19.**
Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (2002 manuscript; 2014 recompilation), Open Problem 8.23, Section 8.4 — characterize the source time `s*` in terms of the Dirichlet form `E`.

# C28 closable transition — I0032 source correction, operator dualization, and spectral-profile route

Run date: 16 September 2026. Repository: `yspennstate/math-open-problems`, branch `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Prior Paley root preserved unchanged in HARD RESERVE: `proofnet24/C28-paley-etf`.
Status: **CLAIMED / PENDING_ADMISSION, not READY; mathematical status PARTIAL / source problem still treated as OPEN on bounded current evidence**.

## 1. Continuity, ownership, and old-target handoff

I read the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current new-methods/fleet controls, the exact intake I0032 row, repository-wide I0032 attempt/claim search, the newest C28 Paley report, and the newest C29 replacement report relevant to C28's audit duty. The large intake mirrors are connector-truncated in a single rendering; I used exact-ID search and do not claim a manual byte-for-byte display of every intake row.

The old C28 Paley-ETF attack is now HARD RESERVE, not erased. Its supported metric remains

`6.657535556520428...` at `(p,m)=(73,14)`

in the frozen `epsilon=1/10`, `m=ceil(p^(3/5))` regime, with exact one- and two-swap local maximality certificates. The quantifier correction is retained: one finite badly conditioned submatrix cannot refute Bandeira's existential asymptotic uniform-bound assertion; a negative source resolution needs a family matching its quantifiers.

For I0032, direct fetch of `operations/claims/I0032.md` returned 404 before this run's write, and repository-wide search found deployment/prompt metadata but no mathematical C28 I0032 run report; `proofnet24/C28-hypercontractivity` itself was absent. Thus no historical numerical comparison factor is invented. I created the exclusive provisional claim `operations/claims/I0032.md` and read it back at creation commit `d30503e5c810bdf9dd5e59c5de70175698a96373`. The claim is PENDING_ADMISSION / NOT READY.

## 2. Source correction: `s*` is not the hypercontractive time `s_q`

The original Aldous-Fill HTML/PDF was read directly, not only the intake paraphrase.

The Chapter 8 setting is a finite irreducible reversible chain, with the continuous-time semigroup `P_s`. In Section 8.2.3 they define

\[
N(s):=\|P_s\|_{2\to\infty}
=\max_i\|P_i(X_s\in\cdot)\|_2
=\max_i\sqrt{\frac{p_{ii}(2s)}{\pi_i}},
\tag{AF 8.39}
\]

and give

\[
N^2(s)=1+\max_i\pi_i^{-1}\sum_{m=2}^n u_{im}^2e^{-2\lambda_m s}.
\tag{AF 8.40}
\]

Section 8.4.2 says, verbatim in substance, that it would be useful for the comparison technique to characterize in terms of `E` the value `s*` such that `N(s)=2 (say)`, and Open Problem 8.23 is simply `Characterize s* in terms of E.` Immediately *after* that, the source introduces the genuinely hypercontractive thresholds

\[
s_q:=\inf\{s\ge0:\|P_s\|_{2\to q}\le1\},
\]

and Theorem 8.24 relates the `s_q` to the log-Sobolev time. Therefore the intake label “hypercontractivity parameter s_star” is misleading if read literally: **source `s*` is the fixed `2 -> infinity` norm threshold `N(s)=2`, not `s_q`.**

The source states that `N` decreases continuously from `pi_*^{-1/2}` to 1. Consequently, literal equality `N(s*)=2` has a positive root only when `pi_*<1/4`, is attained at `s*=0` when `pi_*=1/4`, and has no equality root when `pi_*>1/4`. For a full-domain metric I freeze the harmless threshold convention

\[
\boxed{s_*:=\inf\{s\ge0:N(s)\le2\}},
\tag{2.1}
\]

which agrees with the source root whenever that root exists and gives `s*=0` otherwise.

The source Dirichlet form is

\[
\mathcal E(g,g)=\frac12\sum_i\sum_{j\ne i}\pi_iq_{ij}(g(j)-g(i))^2
\tag{2.2}
\]

in continuous time. Throughout this report “in terms of E” keeps the source state space and stationary `pi` as part of the Dirichlet-form setting; I do not pretend that an unlabeled quadratic form with the reference measure discarded contains more information than it does.

## 3. Move 18 — say it in another language: `s*` is a fixed-threshold L2 heat-kernel time

Let

\[
h_s(x,y)=P_s(x,y)/\pi(y).
\]

By reversibility and Chapman-Kolmogorov,

\[
\sum_y\frac{P_s(x,y)^2}{\pi(y)}
=\frac{P_{2s}(x,x)}{\pi(x)}.
\]

Since `sum_y pi(y) h_s(x,y)=1`, this gives

\[
N(s)^2
=1+\max_x\sum_y\pi(y)(h_s(x,y)-1)^2.
\tag{3.1}
\]

Hence the source threshold is exactly

\[
\boxed{
s_* = \inf\left\{s:\max_x\chi^2(P_s(x,\cdot)\|\pi)\le3\right\}.
}
\tag{3.2}
\]

So the target is a fixed-threshold worst-start `L2(pi)`/chi-square heat-kernel mixing time, not a hypercontractive onset time. Aldous-Fill's own identity `hat d(2s)=N(s)^2-1` is the corresponding uniform-kernel formulation.

This language change immediately identifies the closest mature machinery: Faber-Krahn/spectral-profile bounds for heat-kernel decay, rather than treating `s*` as another log-Sobolev constant.

## 4. Counterexample-first inside the new language: log-Sobolev time alone cannot characterize `s*` up to a universal factor

A tempting source-near proposal would be `s_* asymp tau_l`, because `tau_l` has the exact variational characterization `sup L(g)/E(g,g)` and Section 8.4 is about log-Sobolev/hypercontractivity. The source's own `d`-cube formulas disprove this proposal.

For the continuized simple walk on the `d`-cube,

\[
N^2(s)=(1+e^{-4s/d})^d
\]

and `tau_l=d/2`. Therefore for `d>=3` the source threshold is exactly

\[
\boxed{
s_*(Q_d)=\frac d4\log\frac{1}{4^{1/d}-1}.
}
\tag{4.1}
\]

Indeed `N(s_*)=2` is equivalent to `(1+e^{-4s_*/d})^d=4`. Consequently

\[
\frac{s_*(Q_d)}{\tau_l(Q_d)}
=\frac12\log\frac1{4^{1/d}-1}
=\frac12\log d-\frac12\log(\log4)+o(1),
\tag{4.2}
\]

which diverges. Thus **there is no universal constant `C` with `s_* <= C tau_l` over the full source class.** This is a source-admissible exact family, not a finite simulation.

This does not refute Open Problem 8.23; it rules out one natural too-coarse Dirichlet-form summary.

## 5. Move 11 — dualize/operator form

Let `L=-Q` be the nonnegative self-adjoint generator on `L2(pi)`, so

\[
\mathcal E(f,g)=\langle f,Lg\rangle_\pi.
\]

For a state `x`, let `r_x=1_{\{x\}}/pi(x)`. Then

\[
N(s)^2=\max_x\langle r_x,e^{-2sL}r_x\rangle_\pi.
\tag{5.1}
\]

If `1=phi_1,phi_2,...,phi_n` is an orthonormal eigenbasis with eigenvalues `0=lambda_1<lambda_2<=...`, then

\[
N(s)^2=1+\max_x\sum_{k=2}^ne^{-2\lambda_k s}\phi_k(x)^2.
\tag{5.2}
\]

This is useful conceptually but **not** claimed as a solution to the source problem. Given the entire finite Dirichlet operator and reference measure, diagonalizing `L` and solving (5.2) reconstructs `s*` tautologically. Aldous-Fill explicitly want a characterization useful with the comparison technique; replacing the semigroup by its full spectral decomposition does not supply the missing comparison-friendly extremal formula.

The dualization says what any successful characterization must somehow compress: not merely the eigenvalues but the worst-state spectral weights `phi_k(x)^2` across scales.

## 6. Move 19 — make the comparison idea an explicit procedure, then freeze the candidate

The closest source-matched later route is Goel-Montenegro-Tetali's spectral profile. For a nonempty `S`, define

\[
\lambda_{\mathcal E}(S)
:=\inf_{\substack{f\ge0,\,\operatorname{supp}f\subset S\\f\ \mathrm{nonconstant}}}
\frac{\mathcal E(f,f)}{\operatorname{Var}_\pi f},
\]

and

\[
\Lambda_{\mathcal E}(r)
:=\inf_{\pi_*\le\pi(S)\le r}\lambda_{\mathcal E}(S).
\tag{6.1}
\]

This is an explicit extremal construction from the Dirichlet form and stationary measure, with no heat kernel in its definition. I now **freeze** the first candidate characterization to be

\[
S_{\rm sp}(\mathcal E):=
\begin{cases}
\displaystyle\int_{4\pi_*}^{4/3}\frac{dv}{v\Lambda_{\mathcal E}(v)},&\pi_*<1/4,\\
0,&\pi_*\ge1/4.
\end{cases}
\tag{6.2}
\]

The frozen successor metric is the smallest uniform `C>=1`, if finite, for which both

\[
C^{-1}S_{\rm sp}(\mathcal E)\le s_*\le C S_{\rm sp}(\mathcal E)
\tag{6.3}
\]

hold over all finite irreducible reversible continuous-time chains in the source normalization. At this run's start no candidate had been recovered, so the metric was UNMEASURED. It remains UNMEASURED because only one direction is currently certified.

### Proposition C28-I0032-SP-UPPER-01

For every chain in the frozen class,

\[
\boxed{s_*\le S_{\rm sp}(\mathcal E).}
\tag{6.4}
\]

#### Proof

Goel-Montenegro-Tetali define `I_x(t)=Var_pi(h_t(x,\cdot))` and prove

\[
I_x'(t)\le-I_x(t)\Lambda_{\mathcal E}(4/I_x(t)).
\]

Equivalently, their Theorem 2.1 introduces `V(t)` through

\[
t=\int_{4\pi_*}^{V(t)}\frac{dv}{v\Lambda_{\mathcal E}(v)}
\]

and proves

\[
\sup_x I_x(t)\le4/V(t).
\]

If `pi_*<1/4`, putting `V(t)=4/3` gives `sup_x I_x(t)<=3` at `t=S_sp(E)`, and (3.2) yields `s_*<=S_sp(E)`. If `pi_*>=1/4`, `N(0)=pi_*^{-1/2}<=2`, so both sides of (6.4) are zero. QED.

Thus the candidate already has **one-sided comparison factor 1**, but that is not the tracked two-sided factor.

The corresponding explicit procedure is: solve the restricted Dirichlet Rayleigh problems defining `Lambda(r)`, integrate (6.2), and compare to the source threshold. It may be computationally expensive; its research value is that it survives ordinary Dirichlet-form comparison inequalities.

## 7. Why this is not already solved by the spectral profile

Current literature sharply warns against overclaiming. Goel-Montenegro-Tetali (2006) give the spectral-profile upper bound. Kozma (2009), *On the precision of the spectral profile*, proves that the standard spectral-profile estimate for fixed-threshold `L_infinity` mixing is sharp only up to a `log log` factor and constructs examples showing that factor cannot be universally removed. Hermon (2018), *On sensitivity of uniform mixing times*, proves an optimal `Theta(log log n)` change in `L_infinity` mixing under bounded edge-weight perturbations on bounded-degree graphs. Hermon-Kozma (2024) still cite Aldous-Fill Open Problem 8.23 in the context of robustness/geometric mixing questions. Hermon-Peres (2018) obtain constant-factor characterizations of conventional `L2` mixing and of the log-Sobolev constant through hitting/restricted-eigenvalue quantities, but their threshold and target are not the source `N(s*)=2` quantity.

I do **not** infer from Kozma's fixed `L_infinity` threshold examples that (6.3) already has infinite best factor: the source threshold corresponds to `max chi^2 <=3` (equivalently the particular `N=2` level), and transferring a sharpness example between different fixed thresholds needs a proof. That transfer is the next counterexample-first test.

A bounded fresh search on 2026-09-16 used `Open Problem 8.23`, `Aldous Fill s* Dirichlet form`, `N(s)=2`, `uniform mixing Dirichlet characterization`, and citing literature. I found no paper explicitly claiming a source-exact resolution. A failed bounded search is not proof of bibliographic nonexistence.

## 8. Directed audit duty: C28 -> C29

The newest C29 claim is no longer the old MUB gauge claim already audited by C28. C29's replacement work on Meroni's directional-convexity Conjecture 34 proves `C29-DC34-UPPER-02`: for the normalized noncoplanar four-point lift over parallelogram coordinates `p(s,t)=sU+tV`, the upper boundary of the functional `D`-convex hull is exactly

\[
z_{\max}(s,t)=st.
\]

I independently checked that claim. The point `(s,t,st)` is attained by two successive laminations along the two allowed edge directions. For the reverse inequality, `g(s,t)=st` is affine along those two directions, while along the third source direction `(1,-alpha)` its second directional derivative is `-2 alpha<0`. Therefore `z-g(s,t)` is convex on every allowed vertical plane and vanishes on all four lifted data points, so functional `D`-convexity forces `z<=st`.

Verdict:

\[
\boxed{\texttt{C28-AUDIT-C29-DC34-UPPER-02 = PASS (claim-scoped)}}.
\]

This does **not** audit C29's lower-boundary formula, nonsemialgebraicity conjecture, full candidate hull, or source-level closure.

## 9. Metric, admission status, and next research test

Frozen successor metric before: **UNMEASURED**.  
Frozen successor metric after: **UNMEASURED**.  
Movement: **none**.  
I0032 no-movement count: **1**.  
Old Paley no-movement history remains in its reserve handoff and is not relabeled as I0032 history.

What did move is the research state: exact source normalization is corrected, a natural false candidate (`tau_l`) is eliminated by an exact source family, an operator dual form is isolated, and one comparison-friendly E-only candidate `S_sp` is frozen with the exact one-sided factor 1.

The next run should attack the missing direction of (6.3) **before** deriving more upper bounds. In particular, take Kozma's sharpness family and determine exactly whether its `N(s)=2` time still separates from the threshold-specific spectral-profile integral by an unbounded factor. If yes, the frozen candidate is refuted and the run must replace it with a genuinely different E-functional; if no, the threshold `N=2` has exposed structure absent from conventional uniform mixing.

## 10. Runtime/model-control escalation

The situation is unchanged at the tool boundary: the exposed task interface supports prompt/title/schedule/timing/enabled state, but has no model-family selector and no reasoning-effort selector. Therefore GPT-6/maximum is prompt-only here. Making it enforceable requires product/backend support exposing those fields, or an authorized enclosing runtime that pins them and reports authenticated runtime metadata.

The historical P26 `You cannot modify this task` event is a permission-context boundary. Repository deployment evidence records that a later P26 update succeeded from an authorized context. If that denial recurs, the legitimate workaround is modification by the owner/admin from the task's owning workspace/context; do not bypass access controls and do not create a duplicate schedule.

## ledger_delta for P26

- C28 successor: I0032 / Aldous-Fill Open Problem 8.23, canonical claim created `operations/claims/I0032.md` @ `d30503e5c810bdf9dd5e59c5de70175698a96373`.
- Activity: CLAIMED / PENDING_ADMISSION / NOT READY; mathematical status PARTIAL, source still treated OPEN on bounded current evidence.
- Metric: uniform two-sided factor for frozen spectral-profile candidate `S_sp`; `UNMEASURED -> UNMEASURED`; I0032 unchanged count 1.
- Source correction: `s*` is the `N(s)=||P_s||_{2->infinity}=2` threshold, not the hypercontractive `s_q`.
- New certified one-sided result: `s_* <= S_sp(E)` with factor 1; not a two-sided metric value.
- Exact obstruction: on the `d`-cube, `s_*=(d/4)log(1/(4^(1/d)-1))` and `tau_l=d/2`, so `s_*/tau_l -> infinity`; no universal `s_* <= C tau_l`.
- Preserve Paley reserve metric `6.657535556520428...` at `(73,14)` and its quantifier correction; do not reset or reinterpret it.
- Directed audit: `C28-AUDIT-C29-DC34-UPPER-02 = PASS (claim-scoped)`.
- No shared root ledger was edited by C28.
