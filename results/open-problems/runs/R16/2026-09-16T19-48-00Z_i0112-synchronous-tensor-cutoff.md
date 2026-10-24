Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 maximum was requested in prompt text, but the exposed scheduler has no model/reasoning selector. **Beck--Fiala metric: no movement (current all-t literature bound remains < 3 sqrt(2 pi t)); active successor metric moves provisionally `W_exp = UNMEASURED -> 1/2`. Methods actually tried: #10 DERANDOMIZE, #11 DUALIZE, #15 BREAK THE SYMMETRY.**
Problem/source: **R16 / I0112 — Justin Salez (2025), arXiv:2508.21055v1, Problem 2.3: prove that all bounded-degree vertex-transitive expander sequences exhibit total-variation cutoff.** Status: **PARTIAL**; theorem proved for a new synchronous direct-product class, but publication novelty and the two required outside audits remain pending.

# R16 — synchronous tensor products of Ramanujan expanders have cutoff

Run ID: `2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff`.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, mandatory source refresh, and metrics

The newest complete R16 report was read before research:

`runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md`.

That run had already handed off exhausted I0013 and admitted/claimed I0112. It proved that fixed **Cartesian** products preserve cutoff in continuous time, showed that such products can fail Altschuler's long-range expansion condition, and isolated the more interesting **direct/tensor graph product** whose transition kernel is `P tensor P`. Its frozen progress quantity was

\[
W_{\exp}:=\inf\left\{w\in[0,1]:
\begin{array}{l}
\text{R16 proves a source-admissible vertex-transitive expander family}\
\text{has cutoff window }O((\log |V|)^w)
\end{array}
\right\},
\]

with value `UNMEASURED` until a mathematically proved family outside the obvious already-published classes was produced.

The mandatory campaign/root state was refreshed before research: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own report, and the newest R12 report. Connector-scale corpus results can truncate, so I do **not** claim a semantic line-by-line reread of all ~780 intake rows; exact source/ownership searches were performed for the active target.

### Beck--Fiala source status

The originating Beck--Fiala target is not reopened. A fresh 16 September 2026 search again found Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1 (10 September 2026), proving the stronger Komlos theorem and explicitly the all-`t` consequence

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every finite set system of maximum degree `t`. Bansal--Jiang remains the earlier baseline (`t >= log^2 n` for square-root order, with polylogarithmic loss below). No v2, withdrawal, or proof-specific correction to the Guo--Fang--Lu v1 was found in this bounded search. Thus the source problem is presently literature-`KNOWN`; the fleet package/audit state is a separate matter.

### I0112 source status

Salez Problem 2.3 asks literally:

> Prove that all vertex-transitive expanders exhibit cutoff.

A fresh search found Dylan Altschuler, arXiv:2609.14945 (14 September 2026), proving a Gaussian-profile cutoff theorem for every fixed-degree **long-range expander** sequence and explicitly describing it as intermediate progress toward the transitive spectral-expander conjecture. No general resolution of Salez 2.3 was located.

The R12 current source was also checked rather than assuming the historical AT assignment. The newest located R12 report is `runs/R12/2026-09-16T19-30-29Z_stuck2_f61a83.md`, Paley degree-four SOS, `STUCK RECOVERY 2`; it is not a complete audit-ready package. Therefore `R16_AUDIT_R12=PENDING_NOT_READY`.

## 2. Main new theorem: synchronous direct squares have cutoff

### R16-I0112-C02 — synchronous direct-product cutoff

**Status: PROVED as a mathematical theorem in this report, conditional only on the published Lubetzky--Peres Ramanujan cutoff profile for the factor family. Novelty status: NOT CLAIMED; bounded prior-art clearance is recorded below.**

Fix an integer `d>=3`. Let `(G_N)` be any infinite sequence of connected, non-bipartite, vertex-transitive, `d`-regular Ramanujan graphs with `N=|V(G_N)| -> infinity`; one may take a suitable non-bipartite Lubotzky--Phillips--Sarnak Cayley subfamily. Let

\[
H_N:=G_N\times G_N
\]

be the **direct/tensor graph product**: the vertex set is `V(G_N)^2` and

\[
(x_1,x_2)\sim(y_1,y_2)
\quad\Longleftrightarrow\quad
x_1\sim y_1\text{ in }G_N\text{ and }x_2\sim y_2\text{ in }G_N.
\]

Write `P_N` for simple random walk on `G_N` and

\[
Q_N=P_N\otimes P_N
\]

for simple random walk on `H_N`. In Salez's continuous-time convention the semigroup is

\[
\mathsf H_N(t)=\exp\{t(Q_N-I)\}.
\]

Put

\[
\ell_N=\log_{d-1}N,
\qquad
a_d=\frac d{d-2},
\qquad
\tau_N=a_d\ell_N.
\]

Then `(H_N)` is a bounded-degree vertex-transitive expander sequence and its continuous-time simple random walk has total-variation cutoff at location `tau_N` with window

\[
O(\sqrt{\ell_N})=O(\sqrt{\log|V(H_N)|}).
\]

More precisely, if `D_N(t)` denotes worst-case total-variation distance on `H_N`, then

\[
\lim_{c\to\infty}\limsup_{N\to\infty}
D_N(\tau_N+c\sqrt{\ell_N})=0,
\tag{C02.1}
\]

and

\[
\lim_{c\to\infty}\liminf_{N\to\infty}
D_N(\tau_N-c\sqrt{\ell_N})=1.
\tag{C02.2}
\]

Since `|V(H_N)|=N^2`, this supplies the exponent `w=1/2` in the frozen R16 metric.

### Proof, structural part

`H_N` is `D=d^2` regular. Vertex transitivity follows from the coordinatewise action of `Aut(G_N) x Aut(G_N)`. A standard direct-product criterion says that the direct product of two connected graphs is connected iff at least one factor is non-bipartite; hence `H_N` is connected.

If

\[
1=\theta_{1,N},\theta_{2,N},\ldots,\theta_{N,N}
\]

are the normalized eigenvalues of `P_N`, then the normalized eigenvalues of `Q_N` are

\[
\theta_{i,N}\theta_{j,N},\qquad 1\le i,j\le N.
\tag{C02.3}
\]

Because `G_N` is non-bipartite Ramanujan,

\[
\max_{i\ge2}|\theta_{i,N}|\le
\rho_d:=\frac{2\sqrt{d-1}}d<1.
\]

Therefore every nonconstant eigenvalue of `Q_N` has absolute value at most `rho_d`; in particular

\[
\operatorname{gap}(H_N)\ge1-\rho_d>0.
\tag{C02.4}
\]

Thus `(H_N)` satisfies Salez's source hypotheses.

### Proof, upper side — Method #10 (DERANDOMIZE the common Poisson clock)

Let `K_t ~ Pois(t)`. Conditional on `K_t=k`, continuous-time simple random walk on the direct product has made exactly `k` **synchronous** factor steps, hence from `(x,y)` its law is

\[
P_N^k(x,\cdot)\otimes P_N^k(y,\cdot).
\tag{C02.5}
\]

Let

\[
d_N(k):=\max_x\|P_N^k(x,\cdot)-\pi_N\|_{\rm TV}.
\]

For product measures,

\[
\|\mu_1\otimes\mu_2-\nu_1\otimes\nu_2\|_{\rm TV}
\le
\|\mu_1-\nu_1\|_{\rm TV}
+
\|\mu_2-\nu_2\|_{\rm TV}.
\tag{C02.6}
\]

By convexity of total variation and (C02.5),

\[
D_N(t)\le2\,\mathbb E[d_N(K_t)].
\tag{C02.7}
\]

Now fix `c>0` and set

\[
t_N=\tau_N+c\sqrt{\ell_N},
\qquad
k_N=\left\lfloor\tau_N+\frac c2\sqrt{\ell_N}\right\rfloor.
\]

Markov contraction makes `d_N(k)` non-increasing, so

\[
\mathbb E[d_N(K_{t_N})]
\le
\mathbb P(K_{t_N}<k_N)+d_N(k_N).
\tag{C02.8}
\]

For all large `N`, `t_N-k_N >= (c/3)sqrt(ell_N)`, and Chebyshev gives

\[
\mathbb P(K_{t_N}<k_N)
\le
\frac{9t_N}{c^2\ell_N}
=
\frac{9a_d+o(1)}{c^2}.
\tag{C02.9}
\]

Lubetzky--Peres prove a Gaussian cutoff profile for every fixed-degree Ramanujan graph at

\[
a_d\log_{d-1}N+s\sqrt{\log N}.
\]

Since the chosen family is vertex-transitive, their fixed-start profile is the worst-case profile; hence

\[
\lim_{N\to\infty}d_N(k_N)
=\overline\Phi(\kappa_d c)
\tag{C02.10}
\]

for an explicit constant `kappa_d>0` after the harmless conversion between `sqrt(log N)` and `sqrt(ell_N)`.

Combining (C02.7)--(C02.10), taking `N->infinity` and then `c->infinity`, proves (C02.1).

**Interpretation of #10:** the synchronous product is not an independent-coordinate continuous-time product. The useful move is to condition on the **single common Poisson clock**, then replace that random clock by a deterministic threshold `k_N`. This is the exact point at which the route escaped the Cartesian-product proof from the previous run.

### Proof, lower side — radial martingale estimate in continuous time

Projection onto the first coordinate maps the continuous-time walk on `H_N` exactly to continuous-time simple random walk on `G_N`. Hence

\[
D_N(t)\ge D^{G_N}_N(t).
\tag{C02.11}
\]

We prove the needed lower window directly in Salez's continuous-time convention.

Fix a starting vertex `x` in a `d`-regular graph. The graph distance after `m` discrete steps is stochastically dominated by the reflected biased walk `(Y_m)` on `Z_{>=0}` with `Y_0=0`, deterministic step `0->1`, and for `r>=1`,

\[
\mathbb P(r\to r+1)=p=\frac{d-1}{d},
\qquad
\mathbb P(r\to r-1)=q=\frac1d.
\]

Set

\[
v=p-q=\frac{d-2}{d}=a_d^{-1}.
\]

Let

\[
L_m:=\sum_{j=1}^m\mathbf1_{\{Y_{j-1}=0\}}.
\]

Writing the increments as their conditional mean plus a martingale difference gives the exact decomposition

\[
Y_m=vm+(1-v)L_m+M_m,
\tag{C02.12}
\]

where `(M_m)` is a martingale with differences bounded by `2`.

The number of returns to zero has a geometric tail. Starting from `1`, the return probability for the biased walk is `q/p=1/(d-1)`, so

\[
\mathbb P(L_\infty\ge r)=(d-1)^{-(r-1)},\qquad r\ge1.
\tag{C02.13}
\]

Now set

\[
t_N^-:=\tau_N-c\sqrt{\ell_N},
\qquad
r_N:=\ell_N-\frac{vc}{2}\sqrt{\ell_N}.
\]

Let `K~Pois(t_N^-)`, independent of the reflected walk. Since

\[
vt_N^-=\ell_N-vc\sqrt{\ell_N},
\]

the event `Y_K>r_N` implies at least one of

\[
K-t_N^->\frac c6\sqrt{\ell_N},
\tag{C02.14}
\]

\[
M_K>\frac{vc}{6}\sqrt{\ell_N},
\tag{C02.15}
\]

or

\[
(1-v)L_K>\frac{vc}{6}\sqrt{\ell_N}.
\tag{C02.16}
\]

For the Poisson term,

\[
\mathbb P\left(K-t_N^->\frac c6\sqrt{\ell_N}\right)
\le
\frac{36t_N^-}{c^2\ell_N}
=\frac{36a_d+o(1)}{c^2}.
\tag{C02.17}
\]

For the martingale term, on `K<=2a_d ell_N`, Azuma with increments bounded by `2` gives

\[
\mathbb P\left(
M_K>\frac{vc}{6}\sqrt{\ell_N},\ K\le2a_d\ell_N
\right)
\le
\exp\left(-\frac{v^2c^2}{576a_d}\right).
\tag{C02.18}
\]

The omitted event `K>2a_d ell_N` is exponentially small. Finally, (C02.13) gives

\[
\mathbb P\left((1-v)L_K>\frac{vc}{6}\sqrt{\ell_N}\right)
\longrightarrow0
\quad(N\to\infty)
\tag{C02.19}
\]

for each fixed `c`.

A radius-`r` ball in a `d`-regular graph has at most `C_d(d-1)^r` vertices. Hence, with `B_N=B(x,r_N)`,

\[
\pi_N(B_N)
\le
C_d(d-1)^{-vc\sqrt{\ell_N}/2}
\longrightarrow0.
\tag{C02.20}
\]

Stochastic domination and (C02.17)--(C02.20) imply

\[
\liminf_{N\to\infty}D_N^{G_N}(t_N^-)
\ge
1-\frac{36a_d}{c^2}
-\exp\left(-\frac{v^2c^2}{576a_d}\right).
\tag{C02.21}
\]

Letting `c->infinity` and using (C02.11) proves (C02.2). The theorem follows.

## 3. Method #11 — DUALIZE: clear the obvious published spectral classes

The theorem above would not move the frozen metric if it were merely a disguised application of an already-published class theorem. I therefore attacked the family in spectral language.

### R16-I0112-C03 — the family violates Bordenave--Lacoin Theorem-B's displayed spectral-density hypothesis

**Status: PROVED for any high-girth Ramanujan factor family, including the standard LPS choice.**

Bordenave--Lacoin define, for a `D`-regular graph sequence with `M` vertices, the log-log eigenvalue-density exponent `I(u)` and require for every `u>rho_D=2sqrt(D-1)/D`

\[
I(u)\le
F_D(u):=
1-
2\frac{\operatorname{arcosh}(u/\rho_D)}{\log(D-1)}.
\tag{C03.1}
\]

Take `D=d^2`. In a logarithmic-girth LPS factor family, the empirical spectral distribution converges to Kesten--McKay (the elementary moment argument uses that every fixed-radius neighborhood is eventually a tree). Thus every fixed interval in the interior of `(-rho_d,rho_d)` carries a positive fraction of the `N` factor eigenvalues.

The tensor spectrum contains every factor eigenvalue as

\[
\theta_i\cdot1.
\]

Since `H_N` has `M=N^2` vertices, for every interior `u<rho_d` sufficiently close to `rho_d`,

\[
I_{H}(u)\ge\frac12.
\tag{C03.2}
\]

But at the factor edge

\[
\frac{\rho_d}{\rho_D}=\frac d{\sqrt{d+1}},
\]

and

\[
F_D(\rho_d)<\frac12
\qquad(d\ge3).
\tag{C03.3}
\]

Indeed, (C03.3) is equivalent to

\[
\operatorname{arcosh}\left(\frac d{\sqrt{d+1}}\right)
>
\frac14\log(d^2-1).
\]

After applying `cosh`, clearing the positive square root, and squaring, this is equivalent to

\[
4(2d+1)^2(d-1)^3>d^4(d+1).
\tag{C03.4}
\]

For `d>=3`,

\[
2d+1>2d,\qquad d-1\ge\frac{2d}{3},\qquad d+1\le\frac{4d}{3},
\]

so the left side of (C03.4) exceeds `(128/27)d^5`, while the right side is at most `(4/3)d^5`. Hence (C03.4) holds strictly. By continuity, `F_D(u)<1/2` on an interior interval immediately below `rho_d`, contradicting (C03.1) together with (C03.2).

Thus the displayed Bordenave--Lacoin Theorem-B criterion does not prove cutoff for this class.

### R16-I0112-C04 — the natural product cover fails Bordenave--Lacoin strong convergence

**Status: PROVED for the natural product cover. This does not exclude every imaginable alternative cover.**

Bordenave--Lacoin's general covered-expander theorem assumes **strong convergence**: for every finitely supported walk kernel `p`, the finite singular radius must converge to the singular radius on the infinite cover.

For the natural infinite direct-product cover `T_d x T_d` with synchronous isotropic walk, the transition operator is

\[
P_{T_d}\otimes P_{T_d},
\]

so its spectral/singular radius equals

\[
\rho_d^2.
\tag{C04.1}
\]

On the finite direct square, however,

\[
\sigma(Q_N)=\max_{(i,j)\ne(1,1)}|\theta_{i,N}\theta_{j,N}|
=\max_{i\ge2}|\theta_{i,N}|.
\]

For a high-girth Ramanujan family, Alon--Boppana plus the Ramanujan upper bound gives

\[
\sigma(Q_N)\longrightarrow\rho_d.
\tag{C04.2}
\]

Because `0<rho_d<1`, (C04.1) and (C04.2) are different. Hence the natural product actions do **not** converge strongly, already for the isotropic kernel used here. Bordenave--Lacoin's general strong-convergence theorem therefore cannot be invoked through this natural cover.

### Retained obstructions from the previous run

The preceding R16 report already proved two additional exclusions and they are not re-derived here:

1. for degree `D=d^2`, the direct square is eventually **not Ramanujan**; the exact trace certificate is
   \[
   d^3\frac{N-d}{N-1}>4(d^2-1),
   \]
   and for `d=6` it holds from `N=16` onward;
2. its local-growth base is at most `(d-1)^2`, while Altschuler's degree-`d^2` long-range scale is `d^2-1`, with exact ratio
   \[
   \frac{(d-1)^2}{d^2-1}=\frac{d-1}{d+1}<1.
   \]
   Thus a logarithmic-girth factor family fails the long-range expansion condition at logarithmic radii.

### Product-chain literature check

Chen--Kumagai's *Cutoffs for product chains* studies the coordinate-update kernel

\[
K=\sum_i p_i I\otimes\cdots\otimes K_i\otimes\cdots\otimes I,
\]

whose continuous-time semigroup factorizes into independent coordinate semigroups. The present walk has kernel

\[
P\otimes P,
\]

so both coordinates move on the same Poisson event. It is not their coordinate-update product construction.

A bounded search using `synchronous product random walk cutoff`, `direct product graph cutoff`, `tensor product graph cutoff`, `P tensor P cutoff`, and citations around Bordenave--Lacoin/Chen--Kumagai did not locate a theorem that directly contains C02. **This is not a proof of novelty.** The mechanism is elementary enough that it may be folklore or buried under different terminology, so publication novelty remains `OPEN` pending a dedicated prior-art audit.

## 4. Method #15 — BREAK THE SYMMETRY: two different factors

The square is not essential.

### R16-I0112-C05 — asymmetric synchronous products

**Status: PROVED.**

Let `(G_n)` and `(F_n)` be connected non-bipartite vertex-transitive Ramanujan families of fixed degrees `d,e`, with sizes `N_n,M_n -> infinity`. Write

\[
\tau_G=\frac d{d-2}\log_{d-1}N_n,
\qquad
\tau_F=\frac e{e-2}\log_{e-1}M_n,
\]

and

\[
T_n=\max(\tau_G,\tau_F),
\qquad
W_n=\max(\sqrt{\log N_n},\sqrt{\log M_n}).
\]

Then the continuous-time walk with discrete kernel

\[
Q_n=P_{G_n}\otimes P_{F_n}
\]

on the direct product `G_n x F_n` has cutoff at `T_n` with window `O(W_n)`. In particular

\[
W_n=O(\sqrt{\log(N_nM_n)}).
\]

**Proof.** Conditional on the common Poisson count `K`, the law is the product of the two factor laws after exactly `K` discrete steps. At `T_n+cW_n`, threshold `K` at `T_n+cW_n/2`; Poisson concentration gives an `O(c^{-2})` error, while each factor's Lubetzky--Peres profile is already on its post-cutoff side because `W_n` dominates both factor square-root windows. For the lower bound, project onto a factor attaining `T_n`; the radial continuous-time estimate used in C02 gives distance tending to one at `T_n-cW_n`. Since `W_n/T_n ->0`, this is cutoff. QED.

Thus the phenomenon is not an artefact of exact coordinate symmetry. The structural ingredient is the **shared synchronous jump count**, not equality of the factors.

## 5. Metric movement and what is / is not being claimed

The mathematical theorem C02 is source-admissible: `(H_N)` is a bounded-degree vertex-transitive spectral expander family, and its total-variation cutoff window is `O(sqrt(log |V|))`.

I therefore record

\[
\boxed{W_{\exp}:\ \text{UNMEASURED}\ \longrightarrow\ \frac12}
\]

as a **provisional repository metric movement**. The qualifier matters:

- the cutoff proof itself is complete on the page;
- the family is proved not to be degree-`d^2` Ramanujan, not long-range, not within Bordenave--Lacoin's displayed Theorem-B spectral-density hypothesis, and not within their general theorem through the natural strongly-convergent product cover;
- Chen--Kumagai's standard product-chain setup is a different, coordinate-update chain;
- nevertheless, the bounded prior-art search is not exhaustive, and no publication novelty is claimed until another track audits the literature and proof.

This is **PARTIAL progress toward Salez Problem 2.3**, not closure of the source conjecture.

## 6. Exact checker / finite core

A substantive exact-arithmetic checker was warranted because the run moved the metric and introduced a new spectral exclusion. It certifies only finite/algebraic subclaims, not the asymptotic cutoff proof:

- exact positivity of the Bordenave--Lacoin edge inequality for `d=3,...,10000` (the report proves all `d>=3` analytically);
- the retained `d=6` non-Ramanujan threshold `N=16`;
- exact local-growth-base ratio `(d-1)/(d+1)`;
- an exact rational tensor-spectrum identity on a small stochastic kernel.

Artifacts:

- `artifacts/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff_checker.py`;
- `artifacts/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff_checker.out`.

The executed output ends

`ALL_EXACT_CHECKS_PASS`.

Local output SHA-256 before upload:

`de97560221b7a5e728a42e1f63e2859b042a4e9749ecedd0d9f6ff878956b351`.

This is explicitly a **self-check**, not an independent audit.

## 7. Failure / obstruction ledger

- Fixed Cartesian products: already shown to preserve cutoff by exact continuous-time factorization; wrong route for a counterexample.
- Long-range expansion: not necessary; direct/Cartesian product examples can fail its tree-like growth scale.
- Degree-`D` Ramanujan theory: direct squares are eventually non-Ramanujan.
- Bordenave--Lacoin Theorem B: C03 gives an explicit spectral-density violation.
- Bordenave--Lacoin general strong-convergence theorem: C04 blocks the natural product cover.
- Standard product-chain theorem: asynchronous/coordinate-update rather than synchronous `P tensor P`.
- Full Salez 2.3: still OPEN. This run proves only one structured family.

## 8. Remaining obligations / next route

The highest-value next step is no longer another tensor-product lemma. It is to test whether the proof mechanism survives a **small coupling that destroys exact tensor structure** while retaining transitivity and expansion.

A concrete candidate is a Cayley generating measure on a product group of the form

\[
Q_{\eta}=(1-\eta)(P\otimes P)+\eta R,
\]

where `R` is a transitive cross-generator chosen so that no nontrivial coordinate projection is Markov. The proof would need a quantitative replacement for (C02.5): either a coupling to the synchronous skeleton or a spectral/varentropy perturbation estimate strong enough to preserve an `O(sqrt(log |V|))` window for fixed small `eta>0`.

That would move beyond a decomposable product family rather than merely widen C05.

Before that research earns publication-level novelty, the C02 package needs:

1. P26 full-proof audit;
2. one second independent track audit;
3. a dedicated prior-art search for synchronous/direct-product cutoff and covered-Cayley formulations.

R12 directed audit remains `PENDING_NOT_READY`; its latest report is a stuck recovery, not a complete package.

## 9. Runtime/model escalation

Nothing changed in the exposed task interface. It supports prompt/title/schedule/timing/enabled-state fields but **no model selector and no reasoning-effort selector**. Thus GPT-6/maximum remains prompt-only and cannot be represented as verified runtime configuration. Enforcing it would require an authorized product scheduler/API/UI that actually exposes those fields, or account/workspace administrator/platform-support remediation. Historical `You cannot modify this task` errors are ownership/permission issues; the compliant route is authorized ownership/workspace correction or platform support, not duplicate schedules or permission bypass. No scheduler state was changed here.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  source:
    id: I0112
    author: Justin Salez
    year: 2025
    locator: arXiv:2508.21055v1 Problem 2.3
  target: "All bounded-degree vertex-transitive expander sequences exhibit total-variation cutoff"
  metric:
    name: W_exp
    definition: "smallest exponent w for a proved source-admissible transitive-expander family with cutoff window O((log |V|)^w), excluding obvious previously-published classes"
    before: UNMEASURED
    after: "1/2 (provisional mathematical movement; novelty/prior-art audit pending)"
  status: PARTIAL
  unchanged_count: 0
  methods: [10, 11, 15]
  exact_evidence:
    - "R16-I0112-C02 synchronous direct-square cutoff at tau=d/(d-2) log_{d-1} N with O(sqrt(log N)) window"
    - "R16-I0112-C03 violation of Bordenave--Lacoin Theorem-B spectral-density hypothesis"
    - "R16-I0112-C04 failure of natural product-cover strong convergence: finite singular radius -> rho_d, cover radius = rho_d^2"
    - "R16-I0112-C05 asymmetric synchronous-product extension"
    - "artifacts/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff_checker.out ends ALL_EXACT_CHECKS_PASS"
  audits:
    p26: PENDING
    second_track: PENDING
  beck_fiala_origin:
    current_literature_bound: "disc(A) < 3 sqrt(2 pi t), all t,n, Guo--Fang--Lu arXiv:2609.11189v1"
    movement_this_run: none
```

## Primary references checked this run

- Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3.
- Dylan J. Altschuler, *Long-range expanders: construction and cutoff*, arXiv:2609.14945, 14 Sep 2026.
- Eyal Lubetzky and Yuval Peres, *Cutoff on all Ramanujan graphs*, arXiv:1507.04725.
- A. Lubotzky, R. Phillips, P. Sarnak, *Ramanujan graphs*, Combinatorica 8 (1988), 261--277.
- Charles Bordenave and Hubert Lacoin, *Cutoff at the entropic time for random walks on covered expander graphs*, arXiv:1812.06769 / JIMJ 21 (2022).
- Guan-Yu Chen and Takashi Kumagai, *Cutoffs for product chains*, arXiv:1701.06665 / SPA 128 (2018).
- Shengtao Guo, Ethan X. Fang, Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1.

**No closure claim for Salez Problem 2.3. No publication-novelty claim for C02.**
