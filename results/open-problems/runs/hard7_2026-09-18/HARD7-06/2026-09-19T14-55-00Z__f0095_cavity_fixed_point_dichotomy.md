Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `W_3: 0.6565076662 -> 0.6565076662`; methods actually used: B1 / B11 / B3.**

# HARD7-06 bounded research iteration — a scalar cavity transform, a finite-support/fixed-point dichotomy, and a forced boundary atom

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does not prove existence of the limiting ordinary Erdős--Rényi 3-colourability threshold. It deliberately does not shave another decimal from the current Ayre--Coja-Oghlan--Greenhill (ACG) upper endpoint. The substantive advance is structural: after an exact fractional-linear change of variables, the `q=3` ACG functional becomes a two-term scalar cavity functional, and every convex-mixture local minimizer has the following dichotomy:

> either its message law has finite support, or its transformed message law is an exact recursive distributional fixed point.

For the infinite-support branch the fixed point forces a positive atom at the compactification boundary `alpha=1`. At the current certified degree `d=4.6865076662`, exact arithmetic plus a rigorous exponential enclosure reduces the possible boundary-atom mass to one of two short intervals,

\[
 p_0\in(0.8611,0.8612)\quad\text{or}\quad p_0\in(0.0680,0.0681).
\]

The current explicit three-atom upper-bound witness has boundary mass `0.0839432`, so it is **not** an exact cavity fixed point; this is consistent with the dichotomy because that witness is finitely supported. No claim is made that the current witness is a true local or global minimizer.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, required reads, and current source status

I resumed the already-admitted canonical target `F0095`; I did not restart the original random-3-SAT candidate or mint another alias. The create-only claim remains `operations/claims/F0095.md`, owned by HARD7-06 and source-valid for Alan Frieze's ICM 2014 chromatic-number conjecture. The source statement preserved there is

> **Conjecture.** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

HARD7-06 freezes the first small unresolved location case `k=3`: convergence to a constant average-degree location for the ordinary sparse Erdős--Rényi 3-colourability transition, not merely Achlioptas--Friedgut sharpness around an `n`-dependent location.

Before new mathematics I reread the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the F0095 claim; the newest own checkpoint `2026-09-19T13-45-23Z__f0095_contact_column_generation_46865076662.md`; and neighboring HARD7 state. No competing canonical F0095 owner, release, posted equivalent, or settled campaign row was recovered.

### Fresh bounded literature screen — 19 September 2026

I reran current searches rather than inheriting the previous status sentence.

- Ayre--Coja-Oghlan--Greenhill, *Lower Bounds on the Chromatic Number of Random Graphs*, Combinatorica 42 (2022), DOI `10.1007/s00493-021-4236-z`, remains the rigorous ordinary-model variational upper-bound engine used here.
- Bapst--Coja-Oghlan--Hetterich--Rassmann--Vilenchik, *The Condensation Phase Transition in Random Graph Coloring*, CMP 341 (2016), DOI `10.1007/s00220-015-2464-z`, explicitly places distributional fixed-point equations inside the rigorous/random-colouring cavity literature for sufficiently large colour number. Therefore **distributional cavity fixed points are established prior-art machinery**; I do not claim that generic mechanism as novel.
- Mizgerd--Perkins--Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, RSA 68 (2026), DOI `10.1002/rsa.70081`, published 6 June 2026, proves scaling-window results in a triangle-free conditioned model at a different density scale. It is not the ordinary `G(n,d/n)` fixed-`q=3` source problem.
- A bounded current search for 2025--2026 ordinary random-graph `3-colorability threshold`, `3-colourability threshold`, and fixed-`q=3` threshold-location results recovered the conditioned triangle-free paper and unrelated Gallai edge-colouring work, but no source-matching constant-location theorem.

This is bounded negative evidence only, not a worldwide openness or novelty certificate. F0095 remains **OPEN**. The specific scalar reparameterization and local-minimizer dichotomy below are labelled **newly derived in this repository / novelty UNVERIFIED**.

## 2. Frozen source-relevant metric: no movement

The fixed campaign quantity remains

\[
W_3:=U_3-L_3.
\]

The preceding exact checkpoint established

\[
L_3=4.03,\qquad U_3=4.6865076662,
\qquad W_3=0.6565076662.
\]

This run changes neither endpoint:

\[
\boxed{W_3:0.6565076662\longrightarrow0.6565076662\quad\text{(no movement).}}
\]

This is the first unchanged run after the latest moving checkpoint, so Section I's three-run stuck trigger does not fire. The reason for accepting no endpoint movement is precisely the owner's 90-percent rule: the run spends its mathematical effort on a different route into the infinite-dimensional variational structure rather than another arithmetic tightening of the same three-atom law.

## 3. B1 — change category: an exact scalar cavity coordinate

Start from the `q=3` ACG functional used in the preceding checkpoint. For a message `alpha in [0,1]`, define the fractional-linear coordinate

\[
\boxed{\lambda=\Lambda(\alpha):=\frac{1-\alpha}{2+\alpha}\in[0,1/2].}
\tag{3.1}
\]

The inverse is

\[
\alpha=\frac{1-2\lambda}{1+\lambda}.
\tag{3.2}
\]

The two ACG factors simplify exactly:

\[
A(\alpha)=\frac{2+\alpha}{3}=\frac1{1+\lambda},
\qquad
B(\alpha)=\frac{1+2\alpha}{3}=\frac{1-\lambda}{1+\lambda}.
\tag{3.3}
\]

Let `mu=Lambda_# a` be the pushforward of the ACG law `a`. Under the Poisson point process with intensity `d mu`, write the incoming transformed messages as `lambda_1,...,lambda_D`, where `D~Poisson(d)`, and put

\[
P:=\prod_{i=1}^D(1-\lambda_i),
\qquad
Q:=\prod_{i=1}^D(1-2\lambda_i),
\qquad
K:=\prod_{i=1}^D\frac1{1+\lambda_i}.
\tag{3.4}
\]

Then the ACG vertex probability is

\[
3\prod_iA(\alpha_i)-3\prod_iB(\alpha_i)+\prod_i\alpha_i
=K(3-3P+Q).
\tag{3.5}
\]

For two transformed messages `lambda,lambda'`, the edge factor is

\[
1-\frac{(1-\alpha)(1-\alpha')}{3}
=
\frac{1+\lambda+\lambda'-2\lambda\lambda'}
{(1+\lambda)(1+\lambda')}.
\tag{3.6}
\]

The `log(1+lambda)` terms cancel between the Poisson vertex contribution and the quadratic edge contribution. Therefore the full functional is exactly

\[
\boxed{
\Phi_d(\mu)
=
\mathbb E\log(3-3P+Q)
-\frac d2\,\mathbb E\log(1+\lambda+\lambda'-2\lambda\lambda'),}
\tag{3.7}
\]

with `lambda,lambda'` iid from `mu` in the second expectation.

This is not just cosmetic. The original products of three different rational functions of `alpha` have collapsed to products of the two affine functions `1-lambda` and `1-2lambda`. In this coordinate, the contact equation becomes an explicit recursive distributional equation.

## 4. B11 — dualize KKT contact equality into equality of laws

The previous checkpoint proved the exact first-variation identity

\[
D\Sigma_d(a)[\nu]=d\int h_a(z)\,\nu(dz)
\tag{4.1}
\]

for signed zero-mass directions `nu`, where

\[
h_a(z)=\mathbb E\log S(N_a+\delta_z)-\int\log R(z,y)a(dy).
\]

The new coordinate makes the *difference* of this contact potential explicit.

For one realised incoming Poisson cloud define `P,Q,K` as above. In the old alpha coordinate,

\[
C=2P_A-P_B=K(2-P),
\qquad
D_0=P_A-2P_B+P_0=K(1-2P+Q).
\]

Hence insertion of `z` changes the vertex term by `log(C+zD_0)-log C`. The edge quotient is

\[
\frac{R(z,y)}{R(0,y)}=1+z\Lambda(y).
\]

Define the random outgoing transformed message

\[
\boxed{T:=\frac{1-2P+Q}{2-P}.}
\tag{4.2}
\]

Then

\[
\boxed{
h_a(z)-h_a(0)
=
\mathbb E\log(1+zT)-\mathbb E\log(1+z\Lambda),}
\tag{4.3}
\]

where `Lambda~mu` is independent of the Poisson cloud in the first term.

### Lemma 4.1 — the cavity map stays in the compact interval

For every deterministic finite incoming list `lambda_i in [0,1/2]`,

\[
\boxed{0\le T\le1/2.}
\tag{4.4}
\]

#### Proof

Let

\[
\Delta:=1-2P+Q.
\]

Starting from the empty product `P=Q=1`, so `Delta=0`. If a new message `lambda` is appended, then

\[
P_{new}=P(1-\lambda),\qquad Q_{new}=Q(1-2\lambda),
\]

and direct subtraction gives

\[
\boxed{\Delta_{new}=\Delta+2\lambda(P-Q).}
\tag{4.5}
\]

Because each `1-lambda_i >= 1-2lambda_i >=0`, we have `P>=Q>=0`, so (4.5) proves `Delta>=0`. Also `2-P>=1`. Thus `T>=0`.

For the upper bound,

\[
2\Delta\le2-P
\iff 2Q\le3P,
\]

which holds because `0<=Q<=P`. Hence `T<=1/2`. `square`

### Theorem 4.2 — finite-support / cavity-fixed-point dichotomy

Call `a` a **convex-mixture local minimizer** if for every probability law `b` on `[0,1]`, the path

\[
a_t=(1-t)a+tb
\]

has nonnegative right derivative of `Sigma_d(a_t)` at `t=0`. Then any such minimizer satisfies exactly one of the following alternatives:

1. `a` has finite support; or
2. with `mu=Lambda_#a`, the transformed incoming law is an exact fixed point of (4.2):
   \[
   \boxed{\mathcal L(T)=\mu.}
   \tag{4.6}
   \]

Conversely, (4.6) implies that the first variation vanishes in every admissible signed zero-mass direction. This converse is **first-order stationarity only**; it does not imply a local or global minimum because the ACG functional has not been shown convex.

#### Proof

For the perturbation `(1-t)a+t delta_z`, (4.1) gives

\[
0\le d\left(h_a(z)-\int h_a(x)a(dx)\right).
\]

Set

\[
c:=\int h_a(x)a(dx).
\]

Then `h_a(z)>=c` for every `z in [0,1]`. Since its `a`-average equals `c`, equality holds `a`-almost surely, and continuity of (4.3) gives

\[
h_a(z)=c\qquad\text{for every }z\in\operatorname{supp}(a).
\tag{4.7}
\]

If the support is finite, alternative 1 holds. Otherwise compactness gives an accumulation point of the support in `[0,1]`. By Lemma 4.1, both `T` and `Lambda` lie in `[0,1/2]`; therefore the power series for the two logarithms in (4.3) converges uniformly for `|z|<2`. Thus `h_a(z)-h_a(0)` is real analytic on an open interval containing `[0,1]`. Equation (4.7) supplies infinitely many zeros with an accumulation point, so the analytic identity theorem yields

\[
h_a(z)-h_a(0)\equiv0.
\tag{4.8}
\]

Expanding (4.3) around zero gives, for every `k>=1`,

\[
\mathbb E T^k=\mathbb E\Lambda^k.
\tag{4.9}
\]

Both laws are probabilities on the compact interval `[0,1/2]`. The Hausdorff moment problem is determinate there, so (4.9) implies (4.6).

Conversely, if (4.6) holds then the two expectations in (4.3) coincide for every `z in [0,1]`; hence `h_a` is constant. Substitution into (4.1) makes every zero-mass directional derivative vanish. `square`

### Why this is a genuine route change

The preceding run reduced arbitrary support creation to a one-dimensional contact-pricing inequality. Theorem 4.2 goes one step further: an infinite support cannot be a featureless continuum optimum. It must solve a specific recursive distributional equation. Therefore the infinite-dimensional search naturally splits into two mathematically distinct branches:

- prove a finite-contact/support theorem and solve a finite-dimensional master problem; or
- classify/stabilize fixed points of the scalar cavity map (4.2).

That is stronger information than another optimized support point.

## 5. B3 — prove a stronger boundary consequence completely

The recursion (4.2) has a simple exact atom structure.

### Lemma 5.1 — positivity needs at least two positive inputs

Let `K_+` be the number of incoming messages with `lambda_i>0`. Then

\[
\boxed{T>0\iff K_+\ge2.}
\tag{5.1}
\]

#### Proof

The denominator in (4.2) is positive, so `T=0` iff `Delta=1-2P+Q=0`. The recurrence (4.5) starts at zero. Before the first positive message, `P=Q=1`. After exactly one positive message, `P>Q`, but the increment that created it was taken while `P=Q`, so `Delta` remains zero. Any second positive message has both `lambda>0` and `P-Q>0`, making the increment in (4.5) strictly positive. Thereafter `Delta` stays positive. `square`

### Theorem 5.2 — every infinite-support minimizer has a forced boundary atom

Suppose alternative 2 of Theorem 4.2 holds and put

\[
q:=\mathbb P\{\Lambda>0\}.
\]

Poisson thinning shows that the number of positive incoming messages is

\[
K_+\sim\operatorname{Poisson}(dq).
\]

Using (5.1) and the fixed-point identity,

\[
q=\mathbb P\{T>0\}
=\mathbb P\{K_+\ge2\}
=1-e^{-dq}(1+dq).
\tag{5.2}
\]

Equivalently, with

\[
p_0:=\mathbb P\{\Lambda=0\}=\mathbb P\{\alpha=1\},
\]

we obtain the exact scalar equation

\[
\boxed{
p_0=e^{-d(1-p_0)}\left[1+d(1-p_0)\right].}
\tag{5.3}
\]

An infinite-support fixed point is not the trivial `mu=delta_0`, so `q>0`. Equation (5.2) also rules out `q=1` because its right side is strictly less than one for finite `d`. Hence

\[
\boxed{0<p_0<1.}
\tag{5.4}
\]

Thus **every infinite-support convex-mixture local minimizer is forced to carry a positive atom at `alpha=1`**.

This is a source-useful conceptual explanation for the boundary atom discovered in the earlier three-atom search. It does not assert that the earlier witness is itself a local minimizer.

### Corollary 5.3 — exact atom brackets at the current certified endpoint

Freeze

\[
d=4.6865076662.
\]

Let

\[
F(q)=1-e^{-dq}(1+dq)-q.
\tag{5.5}
\]

The exact checker proves the signs

\[
F(0.1388)<0<F(0.1389),
\qquad
F(0.9319)>0>F(0.9320).
\tag{5.6}
\]

Moreover

\[
F'(q)=d^2q e^{-dq}-1.
\tag{5.7}
\]

The function `d^2 q e^{-dq}` increases until `q=1/d` and decreases thereafter, so `F'` has at most two zeros. By Rolle's theorem `F` therefore has at most three zeros on `[0,1]`. Since `F(0)=0` and (5.6) gives two additional sign-changing roots, these are all the roots. Consequently every nontrivial fixed point at this `d` obeys

\[
\boxed{
q\in(0.1388,0.1389)\cup(0.9319,0.9320),}
\tag{5.8}
\]

or equivalently

\[
\boxed{
p_0\in(0.8611,0.8612)\cup(0.0680,0.0681).}
\tag{5.9}
\]

The current exact three-atom witness has `p_0=0.0839432`, outside both intervals. Therefore it is not a fixed point of (4.2). Again, this does not disqualify it from being an excellent finite-support upper-bound witness; it only identifies which side of Theorem 4.2 it occupies.

## 6. Exact self-check and idea-before-code ordering

The new route was written before code at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T14-47-00Z__f0095_cavity_transform_idea.md`

creation commit

`434e29dd5d29a60ca486330af59565fc74c999c6`.

Only after that did I build the self-check

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T14-47-00Z__f0095_cavity_transform_exact.py`

creation commit

`7db1ef3a2247e0fae15d723ad50fcc46fb47d0dd`.

It checks the fractional-linear identities and the `Delta` recurrence symbolically. For (5.6) it uses `Fraction` arithmetic and rigorous positive-Taylor/geometric-tail enclosures of `exp(x)`, then reciprocates to enclose `exp(-x)`; no floating-point number decides a sign. The archived output is

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T14-47-00Z__f0095_cavity_transform_exact.out`

creation commit

`f620eea80d827bbae466b34f83647af31ab98efa`.

It ends

```text
NONZERO_ROOT_BRACKETS_q = (0.1388,0.1389), (0.9319,0.9320)
BOUNDARY_ATOM_BRACKETS_p0 = (0.8611,0.8612), (0.0680,0.0681)
ALL_EXACT_CHECKS_PASS = True
```

This is a **self-check**, not an independent closure audit. The theorem-sized claims are proved on the page above; the checker is only a finite/symbolic verification aid.

## 7. What failed, what succeeded, and the next mathematical fork

**B1 succeeded.** The transformed functional (3.7) removes a whole family of nuisance denominators by exact cancellation and exposes the cavity products directly.

**B11 succeeded conditionally at the correct level.** KKT contact equality plus analyticity turns an infinite support into equality of two compactly supported probability laws. This does not prove a minimizer exists or that a fixed point is stable/minimizing.

**B3 succeeded.** The stronger atom theorem (5.3)--(5.9) is a complete structural consequence of the fixed-point branch and forces a boundary mass. It is not itself the source threshold theorem.

The highest-value next question is now sharper than “optimize another atom.” One should decide whether the high-boundary-mass branch in (5.9) can be excluded by the **second variation/local-minimum condition**, or whether the cavity map admits a stable infinite-support fixed point on either branch. A useful next triple should therefore be different from B1/B11/B3; a natural choice is **B5 / B20 / B24**:

- B5: interpolate the boundary-atom mass `p_0` and differentiate the second variation;
- B20: identify exactly why the naive fixed-point iteration is unstable on one branch and whether that instability is a negative Hessian direction;
- B24: find the extremal fixed point / extremal support law compatible with (5.9).

If that route does not move either `W_3` or the remaining structural obligation for three consecutive runs, Section I must be invoked rather than generating more cavity algebra.

## 8. Capability honesty

The runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The currently exposed scheduler schema still has title, prompt, schedule/timing mode, and enabled state, but no authenticated model-family selector, reasoning-effort selector, or guaranteed duration. Changing that would require the platform to expose those controls (or an authorized product/support path); a GitHub edit cannot do it. Historical `You cannot modify this task` denials are context-dependent: the current root `RESULTS.md` records that P26 later accepted a full update in another exposed context while other-context denials remain preserved. This HARD7-06 run does not modify any schedule.

## 9. Ledger delta for the designated shared-root maintainer

```yaml
track: HARD7-06
canonical_target: F0095
status: PARTIAL
source_status: OPEN
metric: W_3
before: 0.6565076662
after: 0.6565076662
movement: none
methods: [B1, B11, B3]
new_structural_result: >-
  Every convex-mixture local minimizer of the q=3 ACG functional is either
  finitely supported or its transformed message law solves the exact cavity
  RDE T=(1-2P+Q)/(2-P). Any infinite-support branch has a forced alpha=1
  atom satisfying p0=exp(-d(1-p0))*(1+d(1-p0)).
current_d_exact_atom_brackets:
  - "p0 in (0.8611,0.8612)"
  - "p0 in (0.0680,0.0681)"
closure: false
independent_audits: 0
```
