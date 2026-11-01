Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Metric moved: inherited `W_3=0.9064 -> 0.6570`; after correcting the inherited primary-literature baseline, the genuinely new mathematical movement is `0.6670 -> 0.6570`. Methods actually tried: **B5 / B20 / B28**.

# HARD7-06 run 11 — exact two-atom interpolation moves the rigorous 3-colourability upper endpoint to 4.687

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does **not** prove existence of the constant 3-colourability threshold. It gives a source-relevant rigorous upper-bound improvement for the ordinary sparse Erdos--Renyi model and two route-diagnostic results.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and what was actually reread

I resumed the admitted target `F0095`; I did not restart from the original random-3-SAT candidate. At run start I reread:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current claim `operations/claims/F0095.md`;
- the latest HARD7-06 report and artifact;
- the intake/history around `F0095` and the neighbouring random-CSP ownership history.

The repository still records `F0095` as owned by HARD7-06. Other current tracks explicitly treat that claim as HARD7-06-owned; no release, duplicate canonical claim, posted result, or settled equivalent was found. The originally suggested fixed-`k` random 3-SAT threshold remains unavailable to this track because the canonical `F0097` lifecycle belongs to R03; I do not alias or duplicate it.

The exact source target remains Frieze's ICM-2014 chromatic-number conjecture, with the fixed `k=3` subproblem interpreted as convergence of the ordinary sparse Erdos--Renyi 3-colourability transition to a constant. The frozen quantity remains

\[
W_3:=U_3-L_3,
\]

with `L_3` a rigorous w.h.p. 3-colourable average-degree endpoint and `U_3` a rigorous w.h.p. non-3-colourable endpoint in `G(n,d/n)`.

## 2. Current-literature correction before new mathematics: the inherited 4.9364 upper endpoint was obsolete

The preceding admission report deliberately froze the conservative primary-verified bracket

\[
L_3=4.03,\qquad U_3=4.9364,\qquad W_3=0.9064,
\]

because it had not yet recovered the primary proof behind the stronger modern upper value.

This run recovered and checked the relevant primary source:

Peter Ayre, Amin Coja-Oghlan, Catherine Greenhill, **Lower Bounds on the Chromatic Number of Random Graphs**, Combinatorica 42 (2022), 617--658, DOI `10.1007/s00493-021-4236-z`, arXiv `1812.09691`. Primary full text checked at

`https://web.maths.unsw.edu.au/~csg/papers/ACG-interpolation.pdf`.

For the binomial random graph they define, for a probability law `a` on `[0,1]`,

\[
\Sigma^*_{d,q}(a)
=
\mathbb E\log\!\left[
\sum_{i=0}^{q-1}(-1)^i\binom q{i+1}
\prod_{h=1}^{D}\left(1-\frac{(i+1)(1-\alpha_h)}q\right)
\right]
-
\frac d2\,\mathbb E\log\!\left(1-\frac{(1-\alpha_1)(1-\alpha_2)}q\right),
\tag{2.1}
\]

where `D~Po(d)` and the `alpha_h` are iid with law `a`, and then

\[
d_q^*:=\inf\{d>0:\inf_a\Sigma^*_{d,q}(a)<0\}.
\tag{2.2}
\]

Their Theorem 1.3 states

\[
q\ge3,\ d>d_q^*\quad\Longrightarrow\quad
\chi(G(n,d/n))>q\quad\text{w.h.p.}
\tag{2.3}
\]

The same primary paper explicitly evaluates the one-atom trial law `a=delta_{0.25}` and obtains

\[
\Sigma^*_{4.697,3}(\delta_{0.25})<0,
\]

hence `d_3^*<=4.697`. Therefore the primary-source-verified pre-research bracket for this run is actually

\[
4.03\le \theta_3\le4.697,
\qquad
W_3\le0.6670.
\tag{2.4}
\]

This correction is literature reconciliation, **not** a new HARD7-06 theorem.

A fresh current-status check also found Coja-Oghlan--Krieg--Lawnik--Scheftelowitsch, *Bad Local Minima Exist in the Stochastic Block Model*, J. Stat. Phys. 191 (2024), article 148, DOI `10.1007/s10955-024-03366-w`. Its introduction explicitly says the Achlioptas--Moore `4.03` lower bound still stands as the best current lower bound and identifies `4.697` from Ayre--Coja-Oghlan--Greenhill as the current upper bound for three colours. Searches dated 2026-09-19 for `3-colorability 4.697`, `4.687 random graph chromatic number`, the exact Ayre--Coja-Oghlan--Greenhill title, and 2025--2026 follow-ups did not recover a later rigorous ordinary-Erdos--Renyi 3-colourability endpoint below `4.697`. The 2026 fractional-chromatic-number paper is a different parameter. This is bounded negative evidence, not an exhaustive novelty certificate.

## 3. B5 succeeds: a two-atom law gives a rigorous 4.687 upper endpoint

The source paper itself remarks that `4.697` could be sharpened by optimizing over distributions with small finite support. I followed that route instead of building another checker around the old number.

Take

\[
a=p\delta_x+(1-p)\delta_y,
\qquad
p=\frac{117}{500},\quad
x=\frac{1911}{2500},\quad
y=\frac{61}{500}.
\tag{3.1}
\]

Thus numerically

\[
p=0.234,\qquad x=0.7644,\qquad y=0.122.
\]

For `q=3` define

\[
A(z)=\frac{2+z}{3},\qquad B(z)=\frac{1+2z}{3}.
\]

Condition on `D` and let `K~Bin(D,p)` be the number of `x`-atoms among the `D` iid samples. The quantity inside the first logarithm in (2.1) becomes exactly

\[
S_{D,K}
=3A(x)^K A(y)^{D-K}
-3B(x)^K B(y)^{D-K}
+x^K y^{D-K}.
\tag{3.2}
\]

The edge term is the finite mixture

\[
E_{\rm edge}
=p^2\log R(x,x)+2p(1-p)\log R(x,y)+(1-p)^2\log R(y,y),
\tag{3.3}
\]

where

\[
R(a,b)=1-\frac{(1-a)(1-b)}3.
\]

Therefore

\[
\Sigma^*_{d,3}(a)
=e^{-d}\sum_{D\ge0}\frac{d^D}{D!}
\sum_{K=0}^D\binom DKp^K(1-p)^{D-K}\log S_{D,K}
-\frac d2 E_{\rm edge}.
\tag{3.4}
\]

### Proposition 3.1 — exact certificate below 4.687

For the rational law (3.1),

\[
\boxed{\Sigma^*_{4.6869,3}(a)<0.}
\tag{3.5}
\]

Consequently

\[
\boxed{d_3^*\le4.6869<4.687,}
\tag{3.6}
\]

and Ayre--Coja-Oghlan--Greenhill Theorem 1.3 gives

\[
\boxed{\chi(G(n,4.687/n))>3\quad\text{w.h.p.}}
\tag{3.7}
\]

In particular the campaign's rigorous upper endpoint can be replaced by

\[
U_3=4.687.
\tag{3.8}
\]

With the independently primary-verified lower endpoint `L_3=4.03`, the tracked width moves to

\[
\boxed{W_3=4.687-4.03=0.6570.}
\tag{3.9}
\]

Thus the honest accounting is

\[
\underbrace{0.9064}_{\text{inherited conservative baseline}}
\ \longrightarrow\ 
\underbrace{0.6670}_{\text{recovered published 4.697 endpoint}}
\ \longrightarrow\ 
\underbrace{0.6570}_{\text{new exact two-atom certificate}}.
\tag{3.10}
\]

The second arrow, of width `0.0100`, is the new mathematics in this run.

### Proof of Proposition 3.1 and why the certificate is genuinely rigorous

For numbers `alpha_h in (0,1]`, interpret each incoming message independently as follows: it forbids no colour with probability `alpha_h`, and otherwise forbids one uniformly random colour from the three. By inclusion-exclusion, the probability that not all three colours have been forbidden is precisely

\[
3\prod_h\frac{2+\alpha_h}{3}
-3\prod_h\frac{1+2\alpha_h}{3}
+\prod_h\alpha_h.
\]

Hence for every `D,K`, not merely for the finitely checked values,

\[
0<S_{D,K}\le1,
\qquad
\log S_{D,K}\le0.
\tag{3.11}
\]

This sign is useful: truncating the Poisson sum in (3.4) after `D=16` discards only non-positive terms, so the truncated first expectation is an **upper bound** on the full first expectation.

The checker then encloses every logarithm using the exact identity

\[
\log z=2\sum_{j=0}^{N-1}\frac{t^{2j+1}}{2j+1}+R_N,
\qquad
 t=\frac{z-1}{z+1},
\]

with power-of-two scaling to `1/2<=z<=2` and the rational remainder bound

\[
|R_N|\le
\frac{2|t|^{2N+1}}{(2N+1)(1-t^2)}.
\tag{3.12}
\]

It uses `N=14`. It lower-bounds `e^{-d}` by taking the reciprocal of a positive-Taylor upper bound on `e^d`; because the Poisson-log sum is negative, that direction again gives an upper bound on the first term. For the edge contribution it takes lower bounds on the three logarithms, which give an upper bound after multiplication by `-d/2`.

Every comparison controlling the sign is therefore a `fractions.Fraction` comparison. The archived output gives

\[
\text{first-term upper}\approx-0.4708167391384784350,
\]

\[
E_{\rm edge}^{\rm lower}\approx-0.2009054425842470293,
\]

and finally

\[
\boxed{
\Sigma^*_{4.6869,3}(a)
\le -4.879714424739224148\times10^{-6}<0.
}
\tag{3.13}
\]

No simulation, floating-point sign decision, asymptotic fit, or unproved optimizer claim enters (3.13). The float strings in the artifact are display only.

This is a **self-check**, not either of the two independent audits required for closure/paper packaging.

## 4. B20 — the 4.03 lower-bound obstruction is a branching-process eigenvalue crossing

I also followed the lower-endpoint route rather than treating `4.03` as a black-box constant.

The 2024 Coja-Oghlan--Krieg--Lawnik--Scheftelowitsch analysis revisits the Achlioptas--Moore smoothed Brelaz algorithm and writes the admissible degree for its one-parameter implementation as

\[
d_{\max}(\alpha)=
\max\left\{d>0:\max_{t:\gamma(t)>0}\lambda(t)<1\right\},
\tag{4.1}
\]

where

\[
\lambda(t)=
\frac{2\sum_{i=1}^{\Delta}i(i-1)u_i(t)}
{3\sum_{i=1}^{\Delta}i(w_i(t)+u_i(t))},
\qquad
\gamma(t)=\sum_{\ell=0}^{\Delta}\ell(\ell-2)(u_\ell(t)+w_\ell(t)).
\tag{4.2}
\]

For `alpha=14` they recover `d=4.03`, agreeing with Achlioptas--Moore. Their proof couples the cascade of forced recolourings/list updates to a branching process; the strict inequality `lambda(t)<1` is the subcriticality condition that keeps the cascade controlled.

So the practical reason the classical constructive lower-bound route stops where it does is not merely an unstable numerical ODE. Its proof architecture needs a reproduction eigenvalue below one. Once the relevant local cascade approaches criticality, the same state description loses the uniform subcritical slack required by the branching-process argument.

**B20 outcome:** no lower-endpoint movement this run, but the missing ingredient is now specific: improving `L_3` through this algorithmic family requires a state/action refinement that changes the cascade reproduction kernel, not merely a different numerical integrator or a static reweighting of the same edge events.

## 5. B28 — global colour-pair typicality cannot repair the bad symmetric overlap

The previous run found a positive pair exponent along the symmetric overlap family

\[
A_s=\frac19
\begin{pmatrix}
1+2s&1-s&1-s\\
1-s&1+2s&1-s\\
1-s&1-s&1+2s
\end{pmatrix},
\tag{5.1}
\]

including the exact witness `Phi_3.83(7/25)>0`. A natural B28 response is to count only colourings with a typical global edge profile. The following observation rules out that level of typicality.

### Proposition 5.1 — global pair-count typicality leaves the symmetric-overlap exponent unchanged

Fix rational `0<s<1` and compatible `n`, and let `sigma,tau` be balanced colourings with overlap `A_s`. Condition `G(n,m)` on being proper under both `sigma` and `tau`. For either colouring separately, let `M_12,M_13,M_23` be the numbers of graph edges between its three unordered pairs of colour classes. Then for every fixed `epsilon>0`,

\[
\Pr\left(
\max_{ab\in\{12,13,23\}}
\left|M_{ab}-\frac m3\right|\le\epsilon m
\ \text{for both }\sigma\text{ and }\tau
\ \middle|\ \sigma,\tau\text{ proper}
\right)
=1-e^{-\Omega(m)}.
\tag{5.2}
\]

Consequently restricting the balanced-colouring count to this global typical slice changes the pair contribution at `A_s` only by `exp(o(n))`; its normalized exponential rate is still `Phi_d(A_s)`.

#### Proof

Conditional on both colourings being proper, the `m` graph edges are a uniform `m`-subset of the unordered vertex pairs that are bichromatic under both colourings. The joint type matrix `A_s` is invariant under every simultaneous permutation of the three colour labels. This `S_3` action is transitive on the three unordered `sigma`-colour pairs, while preserving the allowed-edge set. Therefore the three allowed-edge populations seen as `sigma` pairs are equal (up to the harmless integer rounding forced by compatible finite `n`), and each sampled edge has marginal category proportion `1/3+O(1/n)`. The same argument applies to `tau`.

Sampling without replacement gives the usual hypergeometric concentration for each of the six counts. A union bound yields (5.2). Since `m=Theta(n)`, multiplying a fixed-overlap pair contribution by a conditional probability `1-e^{-Omega(n)}` leaves its exponential rate unchanged. QED.

Thus the earlier exact witness survives global pair-count typicality. **B28 outcome:** any useful typical-profile restriction must see genuinely vertex-resolved neighbourhood/list information, not only balance and aggregate counts between colour classes. This dovetails with the B20 diagnosis, because the Achlioptas--Moore mechanism is expressed precisely in evolving vertex-local states `u_i,w_i`.

## 6. Additional B5 no-go: fixed positive edge-local colour weights cannot repair the raw second moment

The successful interpolation law above acts on cavity messages, not directly as a static weight on graph edges. It is useful to see why the simpler static class is too weak.

Let `W` be a symmetric `3x3` matrix with

\[
W_{ii}=0,\qquad W_{ij}>0\ (i\ne j),
\]

and define for balanced colourings

\[
Z_W(G)=\sum_{\sigma\ \mathrm{balanced}}
\prod_{\{u,v\}\in E(G)}W_{\sigma(u),\sigma(v)}.
\tag{6.1}
\]

Because the diagonal entries vanish, `Z_W>0` still certifies a proper 3-colouring.

Write `r=(1/3,1/3,1/3)^T`, `q=r^TWr`, and let `A` be a balanced overlap matrix. At exponential scale the normalized pair exponent is

\[
\Phi_{d,W}(A)=H(A)-2\log3+
\frac d2\log\frac{Q_W(A)}{q^2},
\qquad
Q_W(A)=\operatorname{Tr}(A^T W A W).
\tag{6.2}
\]

At the independent overlap `A_0=rr^T`, put `v=Wr`. For every tangent matrix `X` with zero row and column sums,

\[
D Q_W(A_0)[X]=2v^T Xv,
\]

and the entropy derivative vanishes. Hence

\[
D\Phi_{d,W}(A_0)[X]
=d\,\frac{v^T Xv}{q^2}.
\tag{6.3}
\]

If `v` is not constant, set `u=v-(\mathbf1^Tv/3)\mathbf1` and `X=uu^T`. Then `X` is a valid tangent direction and

\[
v^TXv=(u^Tv)^2=\|u\|^4>0.
\]

For sufficiently small positive `t`, `A_0+tX` remains entrywise positive, so (6.3) gives an immediate correlated-overlap improvement for **every `d>0`**.

If `v` is constant, the three row sums of `W` are equal. Writing its off-diagonal weights as `a,b,c`, equality of `a+b`, `a+c`, and `b+c` forces `a=b=c`. Thus `W` is a scalar multiple of the ordinary proper-edge indicator, and the normalized second moment is exactly the unweighted one. The previous run's Hessian then gives the `d>4` instability (and its explicit `d=3.83` witness is even stronger).

Therefore no fixed positive edge-local colour-pair weighting can repair the raw balanced second moment through the target regime. The successful two-atom cavity interpolation is genuinely a different category of object.

## 7. What is proved, what remains open, and prior-art caution

What this run proves, conditional only on the published Ayre--Coja-Oghlan--Greenhill theorem, is the rigorous numerical implication

\[
\chi(G(n,4.687/n))>3\quad\text{w.h.p.}
\]

from an exact rational certificate for a concrete two-atom trial law.

What it does **not** prove:

1. it does not prove the Frieze/Erdos constant-threshold conjecture for `k=3`;
2. it does not prove that `4.687` is the exact threshold;
3. it does not improve the `4.03` colourable lower endpoint;
4. it does not turn the physics prediction into a proof of threshold existence;
5. it does not certify global novelty merely because the bounded searches found no earlier `4.687` rigorous certificate.

The physics literature quoted by Ayre--Coja-Oghlan--Greenhill predicts about `4.687` by population dynamics. That prediction is prior art for the **number**, not a rigorous proof of the endpoint. The 2022 paper explicitly states `4.697` as its certified easy finite-support bound and says further finite-support optimization could sharpen it. The 2024 paper still calls `4.697` the current rigorous upper bound. I found no later ordinary-ER paper replacing it in the bounded 2026-09-19 searches, but a proper publication claim would still require a citation-graph / author-follow-up check and the protocol's independent mathematical audits.

Status therefore remains **PARTIAL**, not PROVED/CLOSED.

## 8. Exact artifacts and readback

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T06-49-03Z__f0095_two_atom_interpolation.py`

creation commit:

`58d3c6b3014804b4f6dc259125259e33d88bb665`

Archived execution output:

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T06-49-03Z__f0095_two_atom_interpolation.out`

creation commit:

`c9b953ab611add34647a7c64175d472a7ed20d7e`

Both were read back at their creation commits. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The finite checker is a self-check for the variational sign; the theorem-sized reductions and the all-`D` sign needed for safe Poisson truncation are proved on the page above.

## 9. Next research moves — rotate away from B5/B20/B28

The metric moved, so Section I is not triggered. The next execution should use a different triple:

- **B16 — COMPUTE EVERY SMALL CASE:** search low-denominator two- and three-atom laws near the current certificate, but only retain candidates that can be converted to exact rational interval certificates; the goal is a real decrease of `U_3`, not a floating-point optimum.
- **B24 — FIND THE EXTREMAL OBJECT:** derive first-order stationarity/support conditions for minimizers of `a -> Sigma^*_{d,3}(a)` and test whether a two-point extremizer is structurally forced near the threshold.
- **B30 — ONE SCALE/DIRECTION AT A TIME:** localize the variational problem in `d` and message-support intervals, seeking a certified interval for `d_3^*` from the interpolation side rather than a single witness.

A useful next milestone is either `U_3<4.687` by another exact law, or a rigorous structural statement about finite-support optimizers. Do not spend the next run merely adding precision to the same `4.6869` sign.

## 10. Runtime / scheduler capability honesty

The exposed native scheduler still provides task title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector and no guaranteed execution duration**. GPT-6 / maximum is therefore request text only. This run actually identifies as GPT-5.6 Sol; the reasoning level is not exposed and is recorded as `UNVERIFIED`.

Changing scheduled model/reasoning would require the platform to expose those fields or an authorized scheduler surface that controls them. Repository text cannot create such a selector.

The repository records historical modification probes, including a P26 context, that returned `You cannot modify this task`. That is a permission/ownership boundary. The legitimate workaround is for the task owner to use the authorized account/workspace scheduler surface or platform support to repair ownership/permissions. Do not bypass the denial, clone a duplicate job, or reactivate a disabled task. No scheduler was modified in this research run.

## 11. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  target: F0095
  status: PARTIAL
  source_status: OPEN_UNDER_BOUNDED_CURRENT_LITERATURE_REVIEW
  metric: W_3
  metric_definition: "rigorous average-degree bracket width U_3-L_3 for ordinary ER 3-colourability"
  inherited_before: "0.9064 (L_3=4.03, U_3=4.9364)"
  corrected_published_before: "0.6670 (L_3=4.03, U_3=4.697, ACG 2022 primary theorem)"
  after: "0.6570 (L_3=4.03, U_3=4.687)"
  movement: "new mathematical improvement 0.0100 after literature normalization; 0.2494 versus inherited campaign number"
  methods: [B5, B20, B28]
  exact_new_result: "for a=(117/500)delta_(1911/2500)+(383/500)delta_(61/500), Sigma^*_{4.6869,3}(a)<0 by exact rational enclosure; hence d_3^*<4.687 and chi(G(n,4.687/n))>3 whp"
  route_result_1: "global colour-pair typicality does not change the symmetric-overlap exponential obstruction"
  route_result_2: "no fixed positive symmetric edge-local colour-pair weighting repairs the independent-overlap second moment in the target regime"
  lower_endpoint: "4.03 unchanged; Brelaz route bottleneck identified as branching reproduction eigenvalue lambda(t)<1"
  exact_checker: "ALL_EXACT_CHECKS_PASS=True"
  independent_audits: 0
  source_closed: false
  next_methods: [B16, B24, B30]
```

No shared root ledger was edited by this worker; this delta is for the authorized maintainer. No email, Drive, public posting, scheduler mutation, or paper packaging was performed.