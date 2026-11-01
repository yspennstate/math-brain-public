Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed task interface has no model selector, no reasoning-effort selector, and no authenticated runtime telemetry proving GPT-6/maximum, so I do not claim otherwise. **METRIC MOVED: I0110 `M_9 = 1/9 -> 2/9 CERTIFIED`; unchanged count resets to `0`; Section-B methods actually used: #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: **Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.1 (Derandomization), intake I0110.**

Status: **PARTIAL / SOURCE OPEN.** The previous Hasebe--Ueda I0084 assignment is not reopened. It already reached the controlling six-unchanged-run rotation with its exact arXiv-v2 ordinary-convolution handoff preserved at `artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`. The canonical active R19 claim is `operations/claims/I0110.md`.

# 1. Continuity and repository recovery

The immediately preceding complete R19 report is

`runs/R19/2026-09-16_22-36-10_UTC__i0110-treeball-localproduct.md`.

That report established the first honest baseline `M_9=1/9`, with the single counted common property being the Bordenave--Lacoin covered-expander entropic spectral hypothesis `P_BL`, and proved that the **global-inf** Pedrotti--Salez local-product constant is too strong even for random regular graphs because early tree geometry forces `gamma_*(o) <= 16/r`.

Before the new mathematics I reread/recovered the required repository state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and the current queue/deployment provenance it points to;
- canonical `operations/claims/I0110.md`;
- newest complete R19 report;
- neighboring Salez tracks `R01/I0113` and `R16/I0112`;
- newest R20/I0100 report, which had a new exact Jacobi/autocorrelation package ready for the directed audit obligation.

The intake corpus is too large for a one-response byte-for-byte connector rendering. I recovered the canonical I0110 claim/source identity and repository-wide exact-ID hits rather than falsely claiming a manual reread of every intake row.

P26 remains the shared-ledger writer. This run edits no shared root and no peer file.

# 2. Current source/status and primary-literature refresh

Search window: **16--17 September 2026 UTC**.

## 2.1 Original source remains open

Salez's current arXiv record remains `arXiv:2508.21055v1`. The live primary notes still state, immediately after the nine random-graph cutoff references `[80,16,14,21,13,61,22,52,62]`, that the common mechanism has not been identified and ask:

> Problem 2.1 (Derandomization). Find a structural property which is almost-surely satisfied by the various random graphs considered above, and which deterministically triggers cutoff.

Primary locations checked:

- `https://arxiv.org/abs/2508.21055`
- `https://www.ceremade.dauphine.fr/~salez/cutoff.pdf`

No source-matching later resolution was found in the bounded current search below. This is a negative search result, **not** a novelty certificate.

## 2.2 Later general cutoff criterion

Pedrotti--Salez, `arXiv:2607.05345`, _The local product condition implies cutoff_ (July 2026), still gives the universal non-equilibrium Poincare criterion. Its abstract states that the mixing-window width is `O(1/gamma_*)`, without reversibility or a chain rule. The preceding R19 run proved that the global infimum `gamma_*` is too small on the early tree epoch of fixed-degree random regular graphs. The restricted mixing-window version therefore remains the relevant local-product variant, not the global infimum.

Search:
`https://arxiv.org/abs/2607.05345`

No paper found in the bounded search verifies the Pedrotti--Salez condition for all nine ensembles in Salez Problem 2.1.

## 2.3 Bordenave--Lacoin gives an immediate metric correction

Bordenave--Lacoin, `arXiv:1812.06769v3`, _Cutoff at the entropic time for random walks on covered expander graphs_, gives a deterministic covered-expander spectral condition under which the entropic lower bound is sharp and cutoff occurs. Crucially, its current abstract explicitly states that the criterion applies

1. to anisotropic random walks on **random d-regular graphs**, and
2. to random walks on random `n`-lifts of a base graph, including non-reversible walks.

Primary:
`https://arxiv.org/abs/1812.06769`

The paper also recalls that the simple random-walk cutoff on random `d`-regular graphs was first established in the Lubetzky--Sly line represented by Salez reference `[80]`.

## 2.4 The Abelian source remains broader than expander-only criteria

Hermon--Olesker-Taylor, `arXiv:2102.02809v2`, now JEMS 28 (2026), proves cutoff for random Cayley walks on all finite Abelian groups in the stated regime, under `k-d(G) -> infinity`, with the cutoff time described through entropy of random walk on `Z^k`. This scope includes regimes not covered by a fixed positive spectral-gap criterion.

Primary/current:
- `https://arxiv.org/abs/2102.02809`
- JEMS 28 (2026), pp. 1913--1977, DOI `10.4171/JEMS/1743`.

This paper is the main stress test in Sections 6--7 below.

Dated queries included exact combinations of `Salez Problem 2.1 derandomization cutoff random graphs`, `local product random regular graph`, `covered expander random regular graph cutoff`, `random Abelian Cayley entropy cutoff`, and current citing/later Salez work. No all-nine source-matching resolution was located.

# 3. Metric movement: `M_9 = 1/9 -> 2/9`

Recall

\[
M_9
=
\#\{\text{the nine source-cited model results covered by one common property }P\},
\]

where the same explicit `P` must be

1. proved asymptotically almost surely for the cited ensemble, and
2. proved to deterministically trigger total-variation cutoff.

The preceding report conservatively counted only Salez reference `[22]` under `P_BL`.

That was an undercount. The **same** Bordenave--Lacoin deterministic hypothesis `P_BL` is explicitly applied in their paper to random `d`-regular graphs. Salez reference `[80]` is precisely the random-regular cutoff family (Lubetzky--Sly). Simple random walk is a special case of the anisotropic walk covered by the Bordenave--Lacoin application. Hence no property switch and no analogy are needed:

\[
\boxed{
P_{BL}\text{ covers both }[22]\text{ and }[80].
}
\]

Therefore

\[
\boxed{M_9: 1/9 \longrightarrow 2/9.}
\]

I do **not** count `[14]`, `[16]`, `[21]`, `[13]`, `[61]`, `[52]`, or `[62]` under `P_BL` without a source-valid deterministic theorem and a.s. verification in their full cited model scope.

Status of the source problem remains **PARTIAL / OPEN**.

# 4. Method #11 — DUALIZE: exact one-sided likelihood-ratio bounds

The global local-product route failed because it asks for control at every time, including the irrelevant early tree epoch. I therefore rewrote total variation using the likelihood ratio at only the two sides of a proposed mixing window.

Let `p` and `pi` be probability measures on a finite state space with `p << pi`, let

\[
R(y):=\frac{p(y)}{\pi(y)},
\]

and draw `Y ~ p`.

## R19-I0110-C004 — two one-sided likelihood-ratio inequalities

**STATUS: PROVED.**

For every `A>1`,

\[
\boxed{
\|p-\pi\|_{\rm TV}
\ge
\mathbb P_p(R(Y)\ge A)-A^{-1}.
}
\tag{4.1}
\]

For every `delta>0`,

\[
\boxed{
\|p-\pi\|_{\rm TV}
\le
\mathbb P_p(R(Y)>1+\delta)+\delta.
}
\tag{4.2}
\]

### Proof of (4.1)

Let

\[
B_A:=\{y:R(y)\ge A\}.
\]

Then

\[
\pi(B_A)
=
\sum_{y\in B_A}\frac{p(y)}{R(y)}
\le
\frac{p(B_A)}A
\le \frac1A.
\]

Therefore, using the variational characterization of total variation,

\[
\|p-\pi\|_{\rm TV}
\ge p(B_A)-\pi(B_A)
\ge
\mathbb P_p(R(Y)\ge A)-A^{-1}.
\]

### Proof of (4.2)

Let

\[
C_\delta:=\{y:R(y)>1+\delta\}.
\]

Using

\[
\|p-\pi\|_{\rm TV}
=
\sum_y (R(y)-1)_+\pi(y),
\]

split at `C_delta`. On its complement,

\[
(R-1)_+\le\delta.
\]

On `C_delta`,

\[
(R-1)_+\pi\le R\pi=p.
\]

Hence

\[
\|p-\pi\|_{\rm TV}
\le
p(C_\delta)+\delta.
\]

This proves (4.2).

## Corollary: a two-time deterministic cutoff trigger

Consider finite Markov chains with stationary laws `pi_n`, worst-case distance `d_n(t)`, and times

\[
t_n^-<t_n^+,
\qquad
\frac{t_n^+}{t_n^-}\to1.
\]

For every starting state `x`, let

\[
R_{n,t,x}(y)=\frac{P_n^t(x,y)}{\pi_n(y)},
\qquad
Y_{n,t,x}\sim P_n^t(x,\cdot).
\]

If there exist

\[
A_n\to\infty,
\qquad
\delta_n\downarrow0,
\qquad
\eta_n\downarrow0
\]

such that uniformly in starting states

\[
\mathbb P\!\left(
R_{n,t_n^-,x}(Y_{n,t_n^-,x})\ge A_n
\right)
\ge1-\eta_n,
\tag{4.3}
\]

and

\[
\mathbb P\!\left(
R_{n,t_n^+,x}(Y_{n,t_n^+,x})>1+\delta_n
\right)
\le\eta_n,
\tag{4.4}
\]

then

\[
d_n(t_n^-)\to1,
\qquad
d_n(t_n^+)\to0,
\]

and the sequence exhibits total-variation cutoff.

This is an exact deterministic trigger. It is not yet Salez's requested structural property because (4.3)--(4.4) still have to be derived from graph structure. Its value is that it uses only **two time slices** and a one-sided information statistic, so the early-time obstruction that killed the global `gamma_*` route is irrelevant.

# 5. A lift formulation: entropy before the threshold, collisions after it

Suppose an endpoint law `p` is the pushforward of a tractable lift:

\[
Z\sim q \text{ on }\Omega,
\qquad
\Phi:\Omega\to X,
\qquad
p=\Phi_\# q.
\]

Two elementary consequences expose the mechanism seen across random graph proofs.

## 5.1 Pre-mixing from a small typical image

For any `E subset Omega`,

\[
p(\Phi(E))\ge q(E),
\]

hence

\[
\boxed{
\|p-\pi\|_{\rm TV}
\ge
q(E)-\pi(\Phi(E)).
}
\tag{5.1}
\]

If `pi` is uniform on `N` states and

\[
E_a:=\{z:q(z)\ge e^a/N\},
\]

then

\[
|E_a|\le Ne^{-a}
\]

and therefore

\[
\boxed{
\|p-\pi\|_{\rm TV}
\ge q(E_a)-e^{-a}.
}
\tag{5.2}
\]

Thus concentration of lift information

\[
I(Z):=-\log q(Z)
\]

below `log N` gives the lower side of cutoff **without any injectivity assumption on the quotient map**. This cleanly includes tree covers and the `Z^k` lift of random Abelian Cayley graphs.

## 5.2 Post-mixing from a weighted pair collision

Let `Z,Z'` be independent with law `q`. Define

\[
\mathcal C(q,\Phi,\pi)
:=
\mathbb E\left[
\frac{\mathbf 1_{\{\Phi(Z)=\Phi(Z')\}}}{\pi(\Phi(Z))}
\right]-1.
\]

Since `p=Phi_# q`,

\[
1+\mathcal C
=
\sum_{y}\frac{p(y)^2}{\pi(y)}
=
1+\chi^2(p\|\pi).
\]

Therefore

\[
\boxed{
\|p-\pi\|_{\rm TV}
\le\frac12\sqrt{\mathcal C}.
}
\tag{5.3}
\]

For uniform `pi` on `N` states this becomes

\[
\mathcal C
=
N\,\mathbb P(\Phi(Z)=\Phi(Z'))-1.
\tag{5.4}
\]

Equations (5.2) and (5.4) make a plausible common language: **lift information controls the lower side; quotient collision controls the upper side**. Section 7 shows, however, that the raw second-moment/collision condition is too strong to be the final all-nine property.

# 6. New exact Abelian formula: random generators turn post-mixing into torsion arithmetic

The source's structurally opposite ensemble `[52]` is random Abelian Cayley graphs. Here the lift language becomes completely explicit.

Let `G` be a finite Abelian group, written additively, and choose

\[
Z_1,\ldots,Z_k\stackrel{\rm iid}{\sim}\mathrm{Unif}(G).
\]

Let

\[
W=(W_1,\ldots,W_k)
\]

have iid integer coordinates with common law `nu`, independently of the generators, and define the random homomorphic projection

\[
\Phi_Z(W)=\sum_{i=1}^k W_i Z_i\in G.
\]

Let `p_Z` denote the conditional law of `Phi_Z(W)` given the generators. Draw an independent copy `W'` and put

\[
D_i=W_i-W_i'.
\]

For `m>=1`, write

\[
r_m:=\mathbb P(m\mid D_1).
\]

## R19-I0110-C005 — exact averaged chi-square formula

**STATUS: PROVED.**

With `u_G` the uniform law on `G`,

\[
\boxed{
\mathbb E_Z\!\left[1+\chi^2(p_Z\|u_G)\right]
=
\sum_{x\in G} r_{\operatorname{ord}(x)}^{\,k}.
}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
\mathbb E_Z\chi^2(p_Z\|u_G)
=
\sum_{x\ne0}r_{\operatorname{ord}(x)}^{\,k}.
}
\tag{6.2}
\]

### Proof

Condition on the generators. Since `u_G(y)=1/|G|`,

\[
1+\chi^2(p_Z\|u_G)
=
|G|\sum_{y\in G}p_Z(y)^2
=
|G|\,\mathbb P\!\left(
\Phi_Z(W)=\Phi_Z(W')\mid Z
\right).
\tag{6.3}
\]

Condition next on

\[
D=(D_1,\ldots,D_k)
\]

and set

\[
g=\gcd(D_1,\ldots,D_k),
\]

with the usual convention that `g=0` if all entries vanish. The map

\[
T_D:G^k\to G,
\qquad
T_D(z_1,\ldots,z_k)=\sum_i D_i z_i
\]

is a group homomorphism. Its image is exactly

\[
D_1G+\cdots+D_kG=gG.
\]

The inclusion in `gG` is immediate because each `D_i` is divisible by `g`. Conversely Bezout gives integers `a_i` with `g=sum_i a_iD_i`, so for every `x in G`,

\[
gx
=
\sum_i D_i(a_ix)
\in\operatorname{im}T_D.
\]

Uniform input on `G^k` pushes forward uniformly onto the image. Hence

\[
\mathbb P_Z\left(\sum_iD_iZ_i=0\mid D\right)
=
\frac1{|gG|}
=
\frac{|G[g]|}{|G|},
\tag{6.4}
\]

where

\[
G[g]=\{x\in G:gx=0\}.
\]

Substituting (6.4) into (6.3) and averaging gives

\[
\mathbb E_Z[1+\chi^2]
=
\mathbb E_D|G[g]|.
\]

Now

\[
|G[g]|
=
\sum_{x\in G}
\mathbf1_{\{\operatorname{ord}(x)\mid g\}}.
\]

The event `ord(x)|g` is exactly the event that `ord(x)` divides **every** coordinate `D_i`. The coordinates are iid, so

\[
\mathbb P(\operatorname{ord}(x)\mid D_i\ \forall i)
=
r_{\operatorname{ord}(x)}^k.
\]

Summing over `x` proves (6.1).

### Continuous-time coordinate walk

For the rate-one continuous-time walk which chooses one of the `k` signed coordinate steps uniformly, each lift coordinate has characteristic function

\[
\mathbb E e^{i\theta W_i(t)}
=
\exp\!\left[
-\frac tk(1-\cos\theta)
\right].
\]

Thus `D_i(t)=W_i(t)-W_i'(t)` has characteristic function

\[
\exp\!\left[
-\frac{2t}{k}(1-\cos\theta)
\right],
\]

and Fourier inversion modulo `m` gives the exact formula

\[
\boxed{
r_m(t)
=
\frac1m
\sum_{\ell=0}^{m-1}
\exp\!\left[
-\frac{2t}{k}
\left(
1-\cos\frac{2\pi\ell}{m}
\right)
\right].
}
\tag{6.5}
\]

Therefore

\[
\boxed{
\mathbb E_Z\chi^2(p_{Z,t}\|u_G)
=
\sum_{x\ne0}
\left[
\frac1{\operatorname{ord}(x)}
\sum_{\ell=0}^{\operatorname{ord}(x)-1}
e^{-\frac{2t}{k}(1-\cos(2\pi\ell/\operatorname{ord}(x)))}
\right]^k.
}
\tag{6.6}
\]

This is an exact, finite target for the Abelian member `[52]`. It exposes precisely how the group invariant-factor structure enters the second-moment side.

A direct consequence by Markov's inequality is:

\[
\sum_{x\ne0}r_{\operatorname{ord}(x)}(t)^k=o(1)
\quad\Longrightarrow\quad
\|p_{Z,t}-u_G\|_{\rm TV}\xrightarrow{\mathbb P_Z}0.
\tag{6.7}
\]

# 7. Method #24 — FIND THE EXTREMAL OBJECT: `F_2^d` shows collision/chi-square is too strong

The exact formula above initially looked like a candidate route to cover `[52]` under the same two-scale property. The simplest admissible Abelian family shows where that route breaks.

Take

\[
G=(\mathbb Z/2\mathbb Z)^d,
\qquad
k=d+s.
\]

Every nonzero element has order `2`. Put

\[
b(t):=e^{-2t/k}.
\]

From (6.5),

\[
r_2(t)
=
\frac{1+e^{-4t/k}}2
=
\frac{1+b(t)^2}{2}.
\]

Hence (6.2) reduces exactly to

\[
\boxed{
\mathbb E_Z\chi^2(p_{Z,t}\|u_G)
=
(2^d-1)
\left(
\frac{1+b(t)^2}{2}
\right)^k.
}
\tag{7.1}
\]

Suppose now

\[
\frac{s}{k}\to\alpha\in(0,1).
\]

This lies inside the Hermon--Olesker-Taylor admissible regime: `k-d=s -> infinity`, `log k -> infinity`, and `log k = o(log|G|)=o(d)`.

At fixed `b in (0,1)`, the exponential rate of (7.1) is

\[
\frac1k\log\mathbb E\chi^2
\longrightarrow
\log(1+b^2)-\alpha\log2.
\tag{7.2}
\]

Thus the averaged chi-square threshold is

\[
\boxed{
b_{\chi^2}^2=2^\alpha-1.}
\tag{7.3}
\]

But the **Shannon entropic threshold** of the product lift is determined by

\[
h\!\left(\frac{1-b_H}{2}\right)
=
(1-\alpha)\log2,
\tag{7.4}
\]

where `h` is binary entropy in nats.

The two thresholds are not the same. Indeed Shannon entropy dominates Renyi-2 entropy:

\[
h(p)
\ge
-\log(p^2+(1-p)^2),
\]

with strict inequality for nonuniform nondegenerate Bernoulli laws. For

\[
p=\frac{1-b}{2},
\qquad
p^2+(1-p)^2=\frac{1+b^2}{2},
\]

equation (7.4) implies

\[
\alpha\log2
=
\log2-h(p)
<
\log(1+b_H^2),
\]

hence

\[
\boxed{
b_H^2>2^\alpha-1=b_{\chi^2}^2.}
\tag{7.5}
\]

Since `b(t)` decreases with time, the raw chi-square/collision criterion mixes **strictly later on the `t=Theta(k)` scale** than the Shannon entropic threshold when `alpha` is a fixed interior constant.

This is the exact obstruction I wanted from method #24:

> **The second-moment lift-collision criterion is too strong to be the final common structural property for Salez Problem 2.1.**

It is still a valid sufficient criterion and a useful diagnostic, but the full Abelian source scope forces a quantity closer to Shannon / a **typical likelihood ratio**, not a global second moment.

This is also why C004 is the more promising bridge than (5.3): C004 only asks that the likelihood ratio be `<=1+o(1)` with high probability under the **current law**, allowing a tiny exceptional set to carry a large `L^2` contribution.

# 8. Method #30 — ONE SCALE / ONE DIRECTION: a surviving two-time target

The previous global local-product route failed because

\[
\gamma_*\!=\inf_{t>0}\gamma(\mu_t)
\]

remembers the early tree epoch. The raw collision route fails because Renyi-2 sees exceptional heavy fibers beyond the Shannon mixing threshold.

Both failures point to a narrower object:

\[
\boxed{
\text{control only the upper tail of }
\log\frac{P_t(x,Y_t)}{\pi(Y_t)}
\text{ at }t=t_n^+,
}
\tag{8.1}
\]

and the lower tail in the opposite direction at `t=t_n^-`.

A source-level candidate property should therefore have two ingredients:

1. **pre-threshold AEP on a canonical lift**: lift information is concentrated below the stationary information scale, so a typical lift set maps into a set of vanishing stationary mass;
2. **post-threshold typical-fiber flattening**: for `Y_t` sampled from the endpoint law,
   \[
   \log\frac{P_t(x,Y_t)}{\pi(Y_t)}
   \le o(1)
   \]
   with probability `1-o(1)`.

C004 then gives deterministic cutoff immediately. Unlike `chi^2 ->0`, this formulation is compatible with the Shannon/Renyi separation in Section 7.

For `[80]` random regular graphs the natural lift is the regular tree. For `[52]` it is `Z^k`. For `[21]` the natural analogue is a weighted path/trajectory environment. For `[61]` it is the quasi-tree/random-matching auxiliary structure. Thus the property is at least expressed in the language that the nine model-specific proofs already use.

**No new `M_9` credit is assigned for this candidate.** The next real obligation is to derive (8.1) from one explicit structural hypothesis and verify it in multiple full source scopes without reading cutoff itself back into the hypothesis.

# 9. A concrete next bridge: fractional/Renyi order must move toward 1

Equation (7.5) identifies exactly why the second-moment route stops: it freezes the Renyi order at `2`. A plausible next deformation is to introduce an order parameter

\[
q=1+\theta,
\qquad \theta\downarrow0,
\]

and control fractional likelihood moments

\[
\mathbb E_{Y\sim p}
\left[
\left(\frac{p(Y)}{\pi(Y)}\right)^\theta
\right].
\]

At integer orders, lift moments are multi-replica collision probabilities; for random Abelian homomorphisms they should reduce to Smith-normal-form constraints of an integer difference matrix. The unresolved step is to obtain uniform control as `q downarrow1` strong enough to recover the one-sided probability statement (8.1), rather than merely another Renyi cutoff occurring too late.

This is the recommended creative continuation, not a claim.

# 10. Exact self-checks

The run-specific exact checker is

`artifacts/R19/2026-09-16_23-45-47_UTC__i0110_information_collision_and_r20_audit.py`

and its archived output is

`artifacts/R19/2026-09-16_23-45-47_UTC__i0110_information_collision_and_r20_audit.out`.

The checker uses exact `Fraction` arithmetic for:

1. 2646 finite rational instances of the C004 likelihood-ratio inequalities and the exact identity
   \[
   1+\chi^2=\sum p^2/\pi;
   \]
2. five finite Abelian-group instances of the random-homomorphism collision identity C005;
3. the independent R20 audit described next.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

These are **self-checks**, not substitutes for the written proofs above.

# 11. Directed independent audit of the new R20 package

Newest R20 package read:

`runs/R20/2026-09-16T22-50-00Z_i0100_jacobi_randomcone_51d7c3.md`.

Audit ID:

\[
\boxed{
\texttt{R19-AUDIT-R20-I0100-JACOBI-01 = PASS\_ALGEBRAIC\_CORE}.
}
\]

Scope is deliberately limited to R20 Proposition 4.1 and the exact one-parameter Jacobi/spectral-factor calculation through its minimum `sqrt(p)-1`. It does **not** audit the I0100 asymptotic conjecture, the random-circulant heuristic, or floating-point probes.

## 11.1 Autocorrelation identity

R20 defines

\[
a_j=\chi(1-g^j),\qquad j\in\mathbb Z_{p-1},
\]

with `g` primitive and `p=1 mod 4`, and claims

\[
C(0)=p-2,
\qquad
C(r)=0\ (r\text{ odd}),
\qquad
C(r)=-2\ (r\ne0\text{ even}).
\]

Independently:

\[
C(r)
=
\sum_{x\in\mathbb F_p^*}
\chi((1-x)(1-g^r x)).
\]

For `r !=0`, adding `x=0` and using the standard nondegenerate quadratic-character sum gives

\[
C(r)=-\chi(g^r)-1.
\]

A primitive root is a nonsquare, so

\[
\chi(g^r)=(-1)^r.
\]

The displayed cases follow exactly. At `r=0`, one sample vanishes and the other `p-2` samples have square `1`.

PASS.

## 11.2 Even/odd sums

The total sum is

\[
\sum_j a_j=-1.
\]

The Jacobi sum gives

\[
\sum_j(-1)^j a_j=-1.
\]

Therefore the even and odd decimations sum to `-1` and `0`, respectively.

PASS.

## 11.3 One-parameter objective

With `n=(p-1)/2`, `u=1-t`, R20 obtains

\[
B_n(u)
=
\frac{n(2n+u^2)}{u(2n+u)}.
\]

Direct differentiation gives

\[
B_n'(u)
=
\frac{2n^2(u^2-2u-2n)}
{u^2(2n+u)^2}.
\]

Thus the unique positive minimizer is

\[
u_*=1+\sqrt{2n+1}=1+\sqrt p,
\]

and exact substitution yields

\[
B_n(u_*)=\sqrt p-1.
\]

The nonzero spectral coordinates are squared moduli and hence nonnegative; the corrected zero coordinate is `u(2n+u)>0`.

PASS.

The independent exact checker verifies all autocorrelation shifts for every prime `p=1 mod 4` up to `421` (8124 cyclic shifts total), and verifies the minimizer identity in exact quadratic fields `Q(sqrt p)`.

No asymptotic I0100 closure is inferred from this audit.

# 12. Runtime/model control note

Nothing in the exposed task interface allows this worker to select GPT-6 or a reasoning-effort level. Those words remain prompt requests, not verified runtime settings. To make them enforceable, the product/task API would need to expose authorized model and reasoning fields, or an authorized owner/admin context would need to set them.

The historical `P26` response `"You cannot modify this task"` is a permission/ownership boundary, not something R19 may bypass. The repository later records that an authorized P/C context successfully updated that same P26 task. The valid workaround is therefore to use the authorized owner/admin context that has modification rights; do **not** clone the task or evade the permission boundary. This run makes no schedule changes.

# 13. What moved, what failed, and next obligation

## Moved

- `M_9: 1/9 -> 2/9` by correcting the `P_BL` coverage count to include both `[22]` and `[80]`.
- Proved C004, the exact two-sided one-time likelihood-ratio inequalities and resulting two-time cutoff trigger.
- Proved C005, the exact random-Abelian-generator chi-square/torsion formula.
- Isolated an exact `F_2^d` obstruction showing that raw collision/Renyi-2 control is too strong at the Shannon cutoff scale.
- Completed the independent R20 algebraic-core audit.

## Failed route, precisely

The natural pair-collision condition

\[
N\,\mathbb P(\Phi(Z)=\Phi(Z'))-1=o(1)
\]

cannot be the all-nine common criterion: in the admissible elementary-Abelian regime with `s/k -> alpha in (0,1)`, its threshold is governed by Renyi-2 and lies strictly after the Shannon entropic threshold.

## Remaining obligation

Do **not** return to the global `gamma_*` condition or raw chi-square.

The next I0110 attack should parameterize the information order toward Shannon:

1. derive a fractional-moment / truncated-collision analogue of C005 that controls the one-sided likelihood-ratio probability in C004;
2. test it first on the two opposite source families `[80]` random regular and `[52]` random Abelian Cayley;
3. increase `M_9` only if the **same explicit property** is proved both a.s. for a full cited ensemble and deterministically cutoff-triggering.

Recommended next Section-B moves, not used in this run: **#5 ADD A PARAMETER AND DIFFERENTIATE (Renyi order `q downarrow 1`), #23 DO WHAT THE PROPOSER DID NOT EXPECT, #27 SWAP THE QUANTIFIERS.**

# 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R19
  source:
    author: Justin Salez
    year: 2025
    arxiv: 2508.21055v1
    locator: Problem 2.1 (Derandomization)
    intake: I0110
  target: one structural property a.s. satisfied by the nine cited random-graph ensembles and deterministically triggering total-variation cutoff
  metric:
    name: M_9
    before: 1/9
    after: 2/9
    status: CERTIFIED_PARTIAL
    unchanged_count: 0
  status: PARTIAL
  tried_moves: [11, 24, 30]
  exact_evidence:
    - Bordenave--Lacoin arXiv:1812.06769v3 explicitly applies the same deterministic covered-expander criterion to random d-regular graphs, adding Salez [80] to already-counted [22]
    - R19-I0110-C004 written proof
    - R19-I0110-C005 written proof
    - exact self-check output ALL_EXACT_CHECKS_PASS
  audit_ids:
    - R19-AUDIT-R20-I0100-JACOBI-01=PASS_ALGEBRAIC_CORE
  remaining_obligation: derive a Shannon-scale/truncated or fractional-moment structural criterion that survives the F_2^d Renyi-2 obstruction; verify the same criterion on full source scopes before increasing M_9
  i0084_handoff: preserved; not reopened
```
