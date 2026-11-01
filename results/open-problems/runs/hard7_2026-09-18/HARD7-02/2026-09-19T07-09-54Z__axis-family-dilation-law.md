Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed runtime/scheduler surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen metric: `S=5 -> 5`. STUCK1 recovery execution. Methods tried: B21, B5, B11.**

# HARD7-02 run 11 — exact dilation law for the C2 axis family

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN.** This run does not classify all dependence measures. It does, however, resolve the exact blocker chosen in the preceding STUCK1 report: for the source-valid axis family

\[
\theta_p=p\,\delta_{(1,0)}+(1-p)\,\delta_{(0,1)},\qquad 0<p<1,
\]

the full limiting eigenvalue law is not independent of `p`. More precisely, the whole family is an explicit dilation of the balanced law. In particular, at `alpha=1`, the precommitted comparison `p=1/4` versus `p=1/2` is unequal.

The frozen metric does **not** move, despite this source-relevant theorem, because the canonical claim defines `S` more narrowly: it counts only transformation laws descending from an exact finite-matrix spectral identity. The dilation law below is obtained from the corrected rank-marked limiting operator plus Hermitization, not from a deterministic finite-matrix identity. I am not changing the metric after seeing the result.

## 1. Continuity, repository state, ownership, source, and current-status check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the preceding checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T06-12-00Z__stuck1-axis-output-potential-plan.md`.

At run start I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md` and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current HARD7-02 claim and report chain, especially the corrected local-limit run at `2026-09-18T23-12-00Z__rank-marked-pwit-full-local-limit.md` and the rank-wedge run at `2026-09-19T05-12-00Z__rank-wedge-correlation-homogeneous-pwit-criterion.md`;
- the heavy-tail/non-Hermitian intake neighborhood and repository aliases/claims returned by current repository search.

Repository search still identifies Campbell–O'Rourke Question 1.8 as owned only by HARD7-02. The nearby C0031/C0032 heavy-tail questions concern almost-sure iid heavy-tail convergence/density identification and are not equivalent. The Bernoulli least-singular-value family and the owner's least-singular-value, Gaussian row-submatrix, Toeplitz/Hankel, additive-spike, and gated-product work remain excluded.

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`:

- https://arxiv.org/abs/2010.01261
- https://arxiv.org/html/2010.01261v3

The live arXiv record checked on 2026-09-19 still has v3 (2 February 2022) as the latest version. Section 1.3 still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

A fresh bounded search used the exact paper title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `axis`, `PWIT`, `dependence measure`, `log(p/(1-p))`, `dilation`, `erratum`, `correction`, and 2023--2026 date terms. It recovered the 2022 source, Bordenave–Caputo–Chafaï's iid heavy-tail paper, Campbell–O'Rourke's later Lévy–Khintchine Laplacian work, and unrelated non-Hermitian results; I found no source stating the axis-family dilation formula below or a full solution of Question 1.8. This is **bounded negative evidence only**, not a worldwide novelty certificate.

## 2. Frozen metric and exact recovery target

The claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

that are proved under the source hypotheses **and descend from exact finite-matrix spectral identities**.

Before this run: `S=5`.

After this run: **`S=5` (no movement).**

The STUCK1 recovery target was deliberately narrower than the full source question:

\[
\mu_{1,\theta_{1/4}}\stackrel{?}{=}\mu_{1,\theta_{1/2}}.
\]

That blocker is resolved below: they are unequal, and in fact differ by the exact spatial dilation `1/log(3)`.

## 3. The three new-method moves

### B21 — ask who else has this shape

The nearest solved spectral calculation is Bordenave–Caputo–Chafaï (2011), *Spectrum of Non-Hermitian Heavy Tailed Random Matrices*, arXiv `1006.1713`, especially their positive-stable PWIT fixed point and Lemma 4.5 identifying the limiting planar law from the boundary off-diagonal resolvent. Campbell–O'Rourke Remark 1.7 identifies the balanced axis case as the iid-type benchmark in their normalization.

The unexpected second match is the order-biased directed-graph kernel from HARD7-02 runs 7--8: its classical cycle threshold is

\[
\Lambda(p)=\frac{\log(p/(1-p))}{2p-1},\qquad \Lambda(1/2)=2.
\]

The calculation below produces **the reciprocal** of this constant as the Perron root of the rank-order cavity kernel. That was the clue that the rank variable can be eliminated exactly at the output level even though it cannot be erased locally.

### B5 — add the orientation parameter and solve its differential equation

Keep `p` symbolic rather than comparing `1/4` and `1/2` separately. The rank-marked stable scale `A_p(u)` satisfies a first-order ODE. A reflection-product invariant makes the nonlinear coefficient constant, so the entire continuum-type system collapses to one scalar stable fixed point.

### B11 — dualize to the positive order kernel

The same ODE is the Perron–Frobenius eigenproblem for

\[
(K_p f)(u)=(1-p)\int_u^1 f(v)\,dv+p\int_0^u f(v)\,dv.
\]

Its positive eigenfunction and eigenvalue are explicit. This identifies the exact dependence on `p` and makes the dilation factor unavoidable rather than a guessed fit.

## 4. Statement of the new source-level result

Put `q=1-p`, `beta=alpha/2`, and define continuously on `0<p<1`

\[
\lambda_p:=
\begin{cases}
\dfrac{2p-1}{\log(p/q)},&p\ne\tfrac12,\\[6pt]
\tfrac12,&p=\tfrac12.
\end{cases}
\]

Then `lambda_p=lambda_q>0`. Define

\[
k_{\alpha,p}:=\left(\frac{\lambda_p}{\lambda_{1/2}}\right)^{1/(2\beta)}
=\left(\frac{2(2p-1)}{\log(p/(1-p))}\right)^{1/\alpha},
\qquad k_{\alpha,1/2}=1.
\]

### Theorem — axis-family dilation law

Assume the source's Condition C2 with dependence measure

\[
\theta_p=p\delta_{(1,0)}+q\delta_{(0,1)},\qquad 0<p<1.
\]

Using the corrected rank-marked local limit established in HARD7-02 run 3, the limiting ESD satisfies

\[
\boxed{\qquad
\mu_{\alpha,\theta_p}=(D_{k_{\alpha,p}})_\#\mu_{\alpha,\theta_{1/2}},
\qquad D_k(z)=kz.
\qquad}
\]

Thus `p` and `1-p` give the same law, but every `p != 1/2` gives a strict contraction of the balanced law because `lambda_p<1/2` (equivalently the logarithmic mean inequality gives `Lambda(p)>2`).

For the precommitted test point `alpha=1, p=1/4`,

\[
\lambda_{1/4}=\frac1{2\log 3},\qquad
k_{1,1/4}=\frac1{\log 3}=0.910239226626837394\ldots,
\]

hence

\[
\boxed{\mu_{1,\theta_{1/4}}
=(D_{1/\log 3})_\#\mu_{1,\theta_{1/2}}
e\mu_{1,\theta_{1/2}}.}
\]

Because all the axis measures have the same product pushforward under `(z,w) -> zw`, namely `delta_0`, this is also an explicit **refutation of product-only full-source universality on the axis family**. It is not a refutation of Campbell–O'Rourke Question 1.8; it is a structural answer inside that question.

If `rho_{alpha,p}` denotes the planar density where defined, then the dilation gives

\[
\rho_{\alpha,p}(0)=k_{\alpha,p}^{-2}\rho_{\alpha,1/2}(0).
\]

In particular at `p=1/4`,

\[
\frac{\rho_{\alpha,1/4}(0)}{\rho_{\alpha,1/2}(0)}
=(\log 3)^{2/\alpha},
\]

and for `alpha=1` this ratio is

\[
(\log 3)^2=1.20694896081258198\ldots.
\]

The positivity/nondegeneracy of the balanced density is classical from Bordenave–Caputo–Chafaï; no absolute normalization of that density is needed for the ratio.

## 5. Proof: corrected axis cavity system

The proof deliberately does **not** invoke Campbell–O'Rourke Proposition 4.12 as a homogeneous RDE for asymmetric `theta_p`; run 3 showed why that loses the rank type. Instead use the corrected rank-marked PWIT already proved there.

A vertex has type `u in [0,1]`. Its fresh child process has kernel

\[
K_u(dv,dy)=1_{v>u}\,dv\,\nu(dy)+1_{v<u}\,dv\,(\tau_\#\nu)(dy),
\]

where `tau(z,w)=(w,z)` and `nu=theta_p x m_alpha`.

For `eta=it`, `t>0`, the diagonal resolvent entries are pure imaginary. Write them as `i h_t(u)` and `i g_t(u)` with positive random coefficients. In the axis family every edge has exactly one nonzero coordinate. Therefore the two off-diagonal self-energy sums vanish **identically**, not merely in expectation. The two diagonal self-energy sums are disjoint Poisson thinnings and hence independent positive `beta`-stable variables.

Let `S,S'` be independent positive `beta`-stable variables with the standard radial normalization

\[
\mathbb E e^{-sS}=\exp\{-\Gamma(1-\beta)s^\beta\}.
\]

Define

\[
m_t(u):=\mathbb E[h_t(u)^\beta],\qquad T_t:=\int_0^1m_t(v)\,dv,
\]

and the stable scale

\[
A_t(u):=q\int_u^1m_t(v)\,dv+p\int_0^u m_t(v)\,dv.
\]

Rank reflection together with coordinate swap gives the other diagonal scale

\[
B_t(u)=A_t(1-u).
\]

At the boundary `t=0`, temporarily assuming a positive boundary branch, put

\[
A(u):=A_0(u),\qquad C(u):=A(u)A(1-u),\qquad r:=|z|^2.
\]

The stable self-energies have the form

\[
X_u=A(1-u)^{1/\beta}S,\qquad
Y_u=A(u)^{1/\beta}S'.
\]

Inverting the `2 x 2` root Schur complement gives exactly

\[
h_0(u)=\frac{Y_u}{r+X_uY_u},\qquad
 g_0(u)=\frac{X_u}{r+X_uY_u},\qquad
 b_u(z,0)=-\frac{z}{r+X_uY_u}.
\]

Consequently

\[
m(u)=A(u)\,\Psi(C(u),r),
\]

where

\[
\Psi(C,r):=
\mathbb E\left[\left(
\frac{S'}{r+C^{1/\beta}SS'}
\right)^\beta\right].
\]

On the other hand differentiation of the definition of `A` gives

\[
A'(u)=(p-q)m(u)=(2p-1)m(u),
\]

with endpoint values

\[
A(0)=qT,\qquad A(1)=pT,
\qquad T=\int_0^1m.
\]

## 6. The reflection-product invariant

Differentiate

\[
C(u)=A(u)A(1-u).
\]

Since `C(1-u)=C(u)` identically,

\[
\begin{aligned}
C'(u)
&=(2p-1)\{m(u)A(1-u)-A(u)m(1-u)\}\\
&=(2p-1)A(u)A(1-u)
   \{\Psi(C(u),r)-\Psi(C(1-u),r)\}\\
&=0.
\end{aligned}
\]

Thus `C(u)` is constant over the continuum of rank types. This is the key new invariant: the rank type remains visible in each diagonal stable scale, but the **product** that controls the off-diagonal resolvent loses the type exactly.

Write `Psi` for this constant value of `Psi(C(u),r)`. Then

\[
A'(u)=(2p-1)\Psi A(u),
\]

so for `p != 1/2`

\[
\frac{A(1)}{A(0)}
=\exp((2p-1)\Psi)=\frac pq.
\]

Hence

\[
\Psi=\frac{\log(p/q)}{2p-1}=\frac1{\lambda_p}.
\]

At `p=1/2`, `A` is constant and `T=m`, `A=T/2`; therefore `Psi=2=1/lambda_{1/2}`, the continuous limit.

Equivalently, if

\[
Y_p(r):=C^{1/\beta},
\]

the entire continuum-type cavity problem reduces to the single scalar equation

\[
\boxed{\qquad
1=\lambda_p\,
\mathbb E\left[\left(
\frac{S'}{r+Y_p(r)SS'}
\right)^\beta\right].
\qquad} \tag{6.1}
\]

For every fixed `r>=0` the right side is strictly decreasing in `Y_p>0`, tends to infinity as `Y_p downarrow 0` (for `r>0` this uses the divergent critical moment `E[(S')^beta]=infinity`; for `r=0` it is immediate), and tends to zero as `Y_p -> infinity`, using `E[S^{-beta}]<infinity`. Therefore (6.1) has exactly one positive solution.

The actual type profile is also explicit:

\[
A(u)=Y_p(r)^{\beta/2}\left(\frac pq\right)^{u-1/2}.
\]

## 7. B11 interpretation: the same constant is a Perron root

Set

\[
(K_pf)(u)=q\int_u^1f(v)\,dv+p\int_0^u f(v)\,dv.
\]

For

\[
f_p(u)=\left(\frac pq\right)^{u-1/2},
\]

a direct integration gives

\[
K_pf_p=\lambda_p f_p,
\qquad
\lambda_p=\frac{2p-1}{\log(p/q)}.
\]

The positivity of `f_p` identifies this as the Perron scale relevant to the positive cavity branch. The reciprocal

\[
\lambda_p^{-1}=\frac{\log(p/q)}{2p-1}=\Lambda(p)
\]

is exactly the order-biased support/cycle threshold that appeared in runs 7--8. That threshold itself is classical in the directed-random-graph literature, as run 8 already corrected; the new use here is the exact cavity-output reduction, and I make no external novelty claim for it until prior-art review is independent and broader.

## 8. The positive branch is the physical `t downarrow 0` branch

The algebra above would be insufficient if (6.1) admitted a spurious positive boundary solution not selected by the resolvent at `eta=it`. This step rules that out.

Let

\[
c=\min(p,q),\qquad C_0=\max(p,q).
\]

From the definition of `A_t`, for every `u`,

\[
cT_t\le A_t(u),B_t(u)\le C_0T_t.
\]

The exact root inverse at positive `t` is

\[
h_t(u)=\frac{t+Y_u}{r+(t+X_u)(t+Y_u)}
       =\frac1{t+X_u+r/(t+Y_u)},
\]

with

\[
X_u=B_t(u)^{1/\beta}S,\qquad
Y_u=A_t(u)^{1/\beta}S'.
\]

### Uniform upper bound

Since `h_t <= X_u^{-1}`,

\[
m_t(u)\le \frac{\kappa_\beta}{B_t(u)}
\le \frac{\kappa_\beta}{cT_t},
\qquad \kappa_\beta:=\mathbb E S^{-\beta}<\infty.
\]

After integrating,

\[
T_t^2\le \kappa_\beta/c.
\]

### The branch cannot collapse to zero

Suppose along `t_n downarrow 0` one had `T_n:=T_{t_n}->0`. Put

\[
\delta_n=t_n/T_n^{1/\beta}.
\]

Using the upper bound on `X` and lower bound on `Y`,

\[
\frac{h_{t_n}(u)^\beta}{T_n}
\ge
\frac{(\delta_n+c^{1/\beta}S')^\beta}
{\left[r+T_n^{2/\beta}
 (\delta_n+C_0^{1/\beta}S)
 (\delta_n+c^{1/\beta}S')\right]^\beta}. \tag{8.1}
\]

If `delta_n -> infinity`, restrict to the event `S<=1,S'<=1`. The denominator in (8.1) tends to `r^beta` because `T_n^{2/beta} delta_n^2=t_n^2->0`, whereas the numerator diverges. Thus `m_t(u)/T_t` cannot have average one.

If `delta_n` stays bounded, restrict first to `S<=1,S'<=M`. For fixed `M`, the denominator again tends to `r^beta`; after taking `n->infinity`, let `M->infinity`. The critical positive moment `E[(S')^beta]=infinity` makes the lower bound on `m_t(u)/T_t` arbitrarily large, uniformly in `u`, again contradicting

\[
1=\int_0^1 \frac{m_t(u)}{T_t}\,du.
\]

For `r=0`, the simpler identity `h_t=(t+X)^{-1}` gives the same contradiction directly as `t,T_t->0`.

Therefore `T_t` stays bounded away from zero for every fixed `r` as `t downarrow 0`.

Together with the preceding upper bound, `A_t,B_t` stay in a compact positive interval. Also

\[
A_t'(u)=(2p-1)m_t(u)
\]

and the bound on `m_t` gives equicontinuity. Arzelà–Ascoli provides subsequential limits. The domination

\[
h_t(u)^\beta\le B_t(u)^{-1}S^{-\beta}
\]

is integrable uniformly on such a subsequence, so dominated convergence passes the fixed-point relation to `t=0`. Section 6 showed that the positive `t=0` solution is unique. Hence **every** subsequence has the same limit, and the physical boundary resolvent is exactly the branch described by (6.1).

## 9. Scaling the scalar fixed point

Let `lambda_0=lambda_{1/2}=1/2`. Define `k=k_{alpha,p}` by

\[
\lambda_p=\lambda_0 k^{2\beta}.
\]

If `Y_0` is the balanced solution of (6.1), then substituting

\[
r=k^2r_0,\qquad Y_p(r)=k^2Y_0(r_0)
\]

into (6.1) cancels the factor `k^{2 beta}` exactly. By uniqueness,

\[
\boxed{Y_p(r)=k^2Y_{1/2}(r/k^2).} \tag{9.1}
\]

The boundary off-diagonal root resolvent is independent of `u` because `C(u)` is constant:

\[
\bar b_p(z,0)
=-z\,\mathbb E\frac1{|z|^2+Y_p(|z|^2)SS'}.
\]

Using (9.1),

\[
\boxed{
\bar b_p(z,0)=k^{-1}\bar b_{1/2}(z/k,0).
} \tag{9.2}
\]

## 10. From the boundary resolvent to the limiting ESD

This is where nonnormality matters: local degree/cycle statistics alone would not be enough. The needed bridge is Hermitization.

The source's Theorem 3.1 is an exact finite-matrix identity:

\[
\mu_A=-\frac1{\pi n}\sum_{j=1}^n\partial b_j(\cdot,0)
\quad\text{in }\mathcal D'(\mathbb C).
\]

Run 3 established the corrected rank-marked local-operator limit for asymmetric `theta`; for each fixed `t>0`, the uniformly rooted finite resolvent therefore converges to the type-averaged rank-marked root resolvent. The source's least-singular-value and logarithmic-uniform-integrability estimates are finite-matrix estimates under C2 and do not require replacing the asymmetric rank-marked limit by the invalid homogeneous recursion. Repeating the standard subsequence argument used in Bordenave–Caputo–Chafaï Lemma 4.5 with the corrected root limit yields

\[
\boxed{
\mu_{\alpha,\theta_p}
=-\frac1\pi\partial\bar b_p(\cdot,0)
}
\quad\text{in }\mathcal D'(\mathbb C). \tag{10.1}
\]

Now apply (9.2). Wirtinger differentiation under the real dilation `z -> z/k` gives

\[
-\frac1\pi\partial\{k^{-1}\bar b_{1/2}(z/k,0)\}
=k^{-2}\rho_{1/2}(z/k)
\]

at density points, and distributionally this is exactly the pushforward by `D_k`. This proves

\[
\mu_{\alpha,\theta_p}=(D_k)_\#\mu_{\alpha,\theta_{1/2}}.
\]

This final step is source-level: no finite-size simulation, fixed cutoff, or sampled ESD is promoted to an asymptotic statement.

## 11. Why this resolves the STUCK1 blocker but does not close Question 1.8

The blocker was whether the full source output forgets axis imbalance. It does not: it remembers it through one scalar, the Perron scale `lambda_p`, and nothing else inside this one-parameter family.

The result also explains several earlier observations simultaneously:

1. **Transpose symmetry:** `lambda_p=lambda_{1-p}`.
2. **Balanced maximum:** `lambda_p<=1/2`, with equality only at `p=1/2`, so imbalance contracts the cloud.
3. **Triangular boundary:** `lambda_p->0` and `k_{alpha,p}->0` as `p->0` or `1`, consistent with eigenvalue collapse at the excluded one-sided triangular boundary.
4. **Run-5 forest collapse:** below the cycle threshold the product statistic is enough; above it, the surviving output information is precisely the order-kernel Perron scale.
5. **Run-9 rank wedge:** local dependence retains a full shared-rank correlation, yet the planar ESD compresses that correlation to the single invariant `lambda_p` in the axis family.

What remains open is the actual Campbell–O'Rourke classification away from axis support. For a general `theta`, the off-diagonal stable self-energies do not vanish and the reflection-product scalarization used here breaks. A next useful question is whether an analogous finite-dimensional Perron/operator invariant survives for a two-ray deformation of the axis family.

Because `S` did not move, Section I remains active under the literal frozen-metric rule. This run is the substantive execution of the first recovery choice, not a second thinking-only report. If the next invocation still meets the stuck criterion, it must follow the second/final Section-I recovery protocol before any third same-target recovery; after that the target rotates as required.

Fresh proposed nonrepeating methods for the next mathematical attack, if Section I permits it, are **B3 / B18 / B30**: strengthen to a two-ray family, rewrite its `2 x 2` self-energy as an operator-valued fixed point, and localize first at `z=0` before trying the full plane.

## 12. Exact self-check artifact

After deriving the theorem on paper, I added one exact symbolic checker solely for the algebraic core:

- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T07-09-54Z__axis-dilation-check.py`
- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T07-09-54Z__axis-dilation-check.out`

The script checks:

- `lim_{p->1/2} lambda_p=1/2`;
- the exact Perron eigenfunction identity for `K_p`;
- direct symbolic instances on both sides of `1/2`;
- `p <-> 1-p` symmetry;
- `lambda_{1/4}=1/(2 log 3)` and `k_{1,1/4}=1/log 3`;
- the fixed-point scaling cancellation.

Archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is explicitly a **self-check**. It does not certify the probabilistic local-limit/Hermitization steps and is not an independent audit.

Artifact creation commits in this run:

- checker: `f69bb0ced425d7a8c6e15dcfe34e6a1ba09ce3d6`;
- output: `4682ab2cb384e61a8e8981b1cb74054f6e768d19`.

## 13. Runtime capability / scheduler escalation note required by the owner

The exposed task interface still has prompt, schedule/timing, enabled-state, title, and related task controls, but **no binding model selector and no reasoning-effort selector** and no authenticated runtime-effort telemetry. Therefore this worker cannot make the requested GPT-6/maximum setting binding. Doing so would require a platform scheduler/API field that binds both model and reasoning effort, plus runtime metadata authenticating what actually executed. This invocation actually identifies as GPT-5.6 Sol; reasoning level is UNVERIFIED.

The current root `RESULTS.md` records that P26's historical `You cannot modify this task` denial was context-dependent: a later authorized native context successfully updated P26. The compliant workaround for any task that still rejects modification is to use an owner/account/workspace context with permission for that existing task (or platform support/ownership transfer), **not** to bypass permissions, create a duplicate schedule, or reactivate a disabled job. This run made no scheduler changes.

## 14. Honest status

- Campbell–O'Rourke Question 1.8: **PARTIAL / OPEN**.
- Axis subfamily output classification: **candidate theorem proved on-page in this track, independent audit pending**.
- Product-only full-source universality on the axis family: **REFUTED** by the dilation formula, but this is a subclaim, not the source question.
- Frozen metric: **`S=5 -> 5`, no movement**, because this theorem is not an exact finite-matrix-identity law under the claim's metric definition.
- Closure: **not claimed**; no paper folder and no audit request are created in this run.

```yaml
track: HARD7-02
source: Campbell-O'Rourke 2022 Question 1.8
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
status: PARTIAL
section_I_state: STUCK1_RECOVERY_EXECUTED
metric: S
before: 5
after: 5
movement: false
methods: [B21, B5, B11]
recovery_choice_executed: REFUTE_INSTEAD_OF_PROVE
recovery_target: alpha=1 axis p=1/4 versus p=1/2
recovery_result: unequal by exact dilation 1/log(3)
new_source_result: axis-family dilation law
axis_scale: k_alpha_p = [2(2p-1)/log(p/(1-p))]^(1/alpha)
product_only_axis_universality: REFUTED
source_question_closed: false
checker: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T07-09-54Z__axis-dilation-check.py
checker_output: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T07-09-54Z__axis-dilation-check.out
checker_status: ALL_EXACT_CHECKS_PASS
checker_role: self-check only
new_artifacts_this_run: 2
next_methods_if_allowed: [B3, B18, B30]
shared_root_files_modified: []
scheduler_changes: []
```
