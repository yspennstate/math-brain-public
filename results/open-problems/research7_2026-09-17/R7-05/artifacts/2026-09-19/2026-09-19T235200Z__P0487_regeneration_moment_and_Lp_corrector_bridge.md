Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — regeneration-moment and integrable-corrector bridges

Date: 2026-09-19 UTC / 2026-09-20 Asia/Jerusalem  
Worker: C04 / R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Status: **PROVED PARTIAL**; no full-source closure claimed.

## 1. Source target and inherited theorem

Target: Drewitz--Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20. In an i.i.d. uniformly elliptic nearest-neighbor environment on `Z^d`, `d>=2`, does positive limiting velocity in direction `ell` imply the polynomial ballisticity condition `(P)_M` at the standard large-`M` threshold?

The current standard quantitative threshold is `M>=15d+5` in the later equivalence theorem of Guerra--Ramírez. Berger--Drewitz--Ramírez's effective-polynomial paper uses the corresponding strict threshold in one of the implications. Nothing below changes the original quantifiers: i.i.d., uniformly elliptic, `d>=2`, and positive velocity are the only source assumptions.

Inherited from the preceding R7-05 run:

1. Every finite-state Markov-additive walk with positive stationary mean increment has a positive Perron corrector for a small exponential tilt and therefore an exponential wrong-way slab bound.
2. Hence every finite-periodic uniformly elliptic RWRE with positive velocity has exponential wrong-way slab control.
3. More generally, if an environment admits `theta>0` and a bounded positive corrector `H` bounded away from zero with

   `sum_e omega(x,e) exp(-theta e.ell) H(x+e) <= H(x)`

   for every `x`, then the wrong-way slab probability is exponentially small.

The unresolved source issue is that positive velocity in the infinite i.i.d. environment space does not itself provide a bounded Perron eigenfunction/corrector.

This run replaces boundedness by moment control on finite boxes, and separately gives a regeneration criterion that is already strong enough to imply the source polynomial condition through the standard asymptotic polynomial condition.

---

## 2. Exact regeneration localization of every wrong-way slab event

Fix a unit direction `u` with positive limiting velocity component. Let `tau_1^u` be the first standard regeneration time in direction `u`; by convention it is `+infinity` if no such time occurs. Its defining properties are:

- `X_{tau_1^u}.u` is a strict new record above the initial level;
- after `tau_1^u`, the walk never falls below the regeneration level `X_{tau_1^u}.u`.

For `a>0`, write

`H_a^u = inf{n>=0 : X_n.u >= a}`

and

`H_a^{-u} = inf{n>=0 : X_n.u <= -a}`.

Nearest-neighbor steps satisfy `|(X_{n+1}-X_n).u|<=1`.

### Lemma 2.1 — first-regeneration localization

For every `b,L>0`,

`{H_{bL}^{-u} < H_L^u} subset {tau_1^u > bL}`.                 (2.1)

#### Proof

On `A={H_{bL}^{-u}<H_L^u}`, let `sigma=H_{bL}^{-u}`. Then `X_sigma.u<=-bL`.

Suppose instead that `tau_1^u<=sigma`. Since `tau_1^u` is a strict regeneration record above the starting level, `X_{tau_1^u}.u>0`. By the no-backtracking property after regeneration,

`X_n.u >= X_{tau_1^u}.u > 0`

for all `n>=tau_1^u`, contradicting `X_sigma.u<=-bL`.

Hence `sigma<tau_1^u`. Since the projection changes by at most one per step and starts at zero, reaching `-bL` requires at least `bL` steps. Therefore `tau_1^u>sigma>=bL`. QED.

The lemma has an even sharper spatial version. Define the pre-regeneration backtracking radius

`R_u := max(0, - inf_{0<=n<=tau_1^u} X_n.u)`.

Then directly

`{H_{bL}^{-u} < H_L^u} subset {R_u >= bL}`.                    (2.2)

Thus the source's wrong-way probability is controlled by a *single initial regeneration block*. Later i.i.d. regeneration increments do not enter this event.

---

## 3. A complete moment criterion implying the asymptotic polynomial condition

The asymptotic polynomial ballisticity condition `(P*)_M|ell` used in Berger--Drewitz--Ramírez asks, in particular, for every fixed `b>0` and every direction `u` in a neighborhood of `ell`,

`limsup_{L->infinity} L^M P_0(H_{bL}^{-u}<H_L^u)=0`.

### Theorem 3.1 — regeneration-radius criterion

Let `M>0`. Suppose that for every direction `u` in some neighborhood of `ell`,

`E_0[R_u^M] < infinity`.                                      (3.1)

Then `(P*)_M|ell` holds.

In particular, the stronger assumption

`E_0[(tau_1^u)^M] < infinity`                                (3.2)

for all such `u` implies `(P*)_M|ell`.

#### Proof

Fix `b>0` and an admissible `u`. By (2.2),

`L^M P_0(H_{bL}^{-u}<H_L^u)
 <= L^M P_0(R_u>=bL)
 <= b^{-M} E_0[R_u^M 1_{R_u>=bL}]`.

Since `R_u^M` is integrable, the final truncated expectation tends to zero by dominated/monotone tail convergence. This is exactly the required polynomial limit for the chosen `b,u`. Since both were arbitrary in the source neighborhood, `(P*)_M|ell` follows.

Finally `R_u<=tau_1^u` because the walk has unit-bounded projected increments, so (3.2) implies (3.1). QED.

### Corollary 3.2 — a source-valid sufficient regeneration estimate

If (3.1) holds for one exponent `M>15d+5` (or at any exponent strong enough for the standard Berger--Drewitz--Ramírez threshold), then the established implication `(P*)_M => (T')`, together with the later Guerra--Ramírez equivalence, yields the source finite-box polynomial ballisticity condition `(P)_{M_0}` at the standard threshold `M_0>=15d+5`.

Therefore P0487 would follow from positive velocity if one could prove the single missing implication

`positive velocity  =>  E_0[R_u^M]<infinity`

for one sufficiently large `M`, uniformly in the sense of holding for every `u` in a neighborhood of `ell`.

This is substantially narrower than asking for an arbitrary global corrector: only the depth of the *initial* pre-regeneration backtracking excursion needs a high moment.

---

## 4. Why the usual positive-speed regeneration fact is insufficient

The classical regeneration framework distinguishes the first regeneration block from subsequent stationary blocks. In particular, existing ballistic RWRE work records that positive speed controls the mean duration of a typical inter-regeneration block, while stronger results assume extra moments of the first regeneration time and/or later regeneration increments.

Lemma 2.1 explains why this distinction is not cosmetic for P0487: wrong-way slabs are decided before the first successful regeneration. Information only about the law of `tau_{k+1}-tau_k` for `k>=1` does not control the initial backtracking radius `R_u`.

The following exact countermodel shows that no argument using only abstract regeneration, bounded increments, and finite mean *later* regeneration times can bridge the gap.

### Proposition 4.1 — regenerative obstruction model

There exists a bounded-step process on `Z` with deterministic positive asymptotic speed `1`, with every post-first regeneration duration equal to `1`, but whose wrong-way slab probability satisfies only

`P(H_L^-<H_L^+) asymp 1/(L (log L)^2)`.                        (4.1)

Hence it fails `(P*)_M` for every `M>1`.

#### Construction and proof

Let `B` be an integer-valued random variable on `{2,3,...}` with

`P(B=n)=c/[n^2 (log(n+1))^2]`,                                (4.2)

where `c` normalizes the distribution. Then

`E[B]<infinity`,

but `E[B^{1+eps}]=infinity` for every `eps>0`, and the integral test gives

`P(B>=L) asymp 1/[L(log L)^2]`.                               (4.3)

Conditioned on `B`, define a nearest-neighbor path as follows:

1. move left deterministically from `0` to `-B` in `B` steps;
2. move right deterministically for `B+1` steps, reaching `+1` at time `2B+1`;
3. thereafter move right by `+1` at every step.

Take the first regeneration time to be `tau_1=2B+1`; every later integer time is a regeneration time, so all post-first regeneration durations are exactly `1`. The asymptotic velocity is therefore exactly `+1`.

For the symmetric interval `[-L,L]`, if `B>=L` the path hits `-L` before `+L`; if `B<L` it turns at `-B` and subsequently reaches `+L` without ever hitting `-L`. Thus

`P(H_L^-<H_L^+)=P(B>=L)`,

and (4.1) follows from (4.3). QED.

This process is **not** an i.i.d. RWRE and therefore is not a counterexample to P0487. Its role is methodological: the i.i.d. spatial environment and uniform ellipticity must be used to control the initial trap/backtracking block. Regeneration algebra alone cannot do it.

---

## 5. Integrable unbounded correctors: finite-box back-face theorem

The preceding run required a corrector bounded above and below. That is far stronger than necessary for a finite polynomial criterion. Polynomial moments of the corrector and its reciprocal suffice because the exponential tilt can absorb polynomial oscillation on a polynomial-volume box.

Let the environment-space tilted operator be

`(K_theta h)(omega)
 = sum_e omega(0,e) exp(-theta e.u) h(tau_e omega)`.            (5.1)

Assume `h:Omega->(0,infinity)` is measurable and

`K_theta h <= h`                                              (5.2)

`P`-almost surely. By shift invariance and a countable intersection, (5.2) then holds simultaneously at every lattice translate for `P`-almost every environment.

Let `B_L` be any finite box (including one lattice layer around its boundary) with

`|B_L| <= C L^D`                                              (5.3)

for fixed `C,D`. Let `A_L^-` denote the event that the walk exits through a back face on which `X.u<=-cL`, for a fixed `c>0`.

### Theorem 5.1 — `L^p` corrector back-face criterion

Assume for some `s,q>0`,

`E[h^s]<infinity`,  `E[h^{-q}]<infinity`.                     (5.4)

Then for every prescribed polynomial exponent `M>0`,

`P_0(A_L^-)=o(L^{-M})`.                                       (5.5)

More quantitatively, for any `a,b>0`,

`P_0(A_L^-)
 <= E[h^s] L^{-as}
    + C E[h^{-q}] L^{D-bq}
    + L^{a+b} exp(-theta c L)`.                               (5.6)

Choosing `as>M` and `bq>D+M` proves (5.5).

#### Proof

Define the good-environment event

`G_L={h(omega)<=L^a}`

intersected with

`{h(tau_x omega)>=L^{-b} for every x in B_L}`.

By Markov's inequality, stationarity, and a union bound (no spatial independence is needed),

`P(G_L^c)
 <= E[h^s]L^{-as}+C E[h^{-q}]L^{D-bq}`.                       (5.7)

For `omega in G_L`, set

`M_n=exp(-theta X_n.u)h(tau_{X_n}omega)`.

Equation (5.2) makes `M_n` a nonnegative quenched supermartingale. Stop it at the box-exit time. Initially

`M_0=h(omega)<=L^a`.

On a back-face exit, `X_tau.u<=-cL` and the endpoint is included in the one-layer enlargement used in `B_L`, so

`M_tau>=exp(theta cL)L^{-b}`.

Optional stopping therefore gives

`P_{0,omega}(A_L^-)
 <= L^{a+b} exp(-theta cL)`.

Average over `G_L` and add (5.7) to obtain (5.6). Finally choose `a,b` with strict inequalities `as>M` and `bq>D+M`; multiplying (5.6) by `L^M` makes all three terms tend to zero. QED.

### Important scope limitation

Theorem 5.1 controls the **back face**. The effective finite-box condition `(P)_M` counts all non-front exits, including lateral faces. A corrector tilted only in direction `u` does not penalize a nearly transverse side exit. Thus a direct finite-box route to `(P)_M` additionally needs a polynomial lateral-confinement estimate.

Consequently, the following is immediate but genuinely source-relevant:

> **Corrector-plus-confinement bridge.** If positive velocity yields (i) a positive tilted corrector satisfying (5.2) with any nonzero positive moment of `h` and negative moment of `h`, and (ii) lateral exit probability `o(L^{-M})` in the source boxes for some `M>=15d+5`, then `(P)_M` follows.

The regeneration-radius route in Sections 2--3 avoids this lateral issue by proving the asymptotic wrong-way condition `(P*)_M` first.

---

## 6. What moved and what did not

### New proved obligations

- **O3 complete:** every wrong-way slab event is localized before the first directional regeneration; `(P*)_M` follows from an `M`-th moment of the pre-regeneration backtracking radius.
- **O4 complete:** bounded correctors are not necessary on finite polynomial-volume boxes; any positive and negative moments of an unbounded corrector give arbitrary polynomial back-face decay.
- **O5 obstruction complete:** positive speed plus abstract regeneration and finite mean later blocks is insufficient; an explicit bounded-step regenerative process can have speed `1` and only `1/[L(log L)^2]` wrong-way decay.

### Remaining source gap

The source implication itself remains open in this work. The most concentrated missing lemma is now:

`positive velocity in iid uniformly elliptic RWRE`

`=> high moment of R_u for every u near ell`,                 (6.1)

for one exponent above the standard threshold.

An alternative route is:

`positive velocity => integrable tilted corrector + lateral confinement`. (6.2)

The obstruction model shows that (6.1) cannot follow from regenerative renewal structure alone. A successful proof has to use the i.i.d. spatial environment and uniform ellipticity to rule out sufficiently heavy initial traps.

### Full-source metric

`FULL_SOURCE_IMPLICATION` (positive velocity `=> (P)_M` under exactly the Drewitz--Ramírez hypotheses):

`0 -> 0`.

This unchanged headline does not erase the new exact bridge lemmas above.

---

## 7. Next attack

The next useful attack should focus directly on (6.1), not on another finite-periodic example.

A concrete route is to condition on the first depth-`r` backward excursion and expose the minimal i.i.d. environment set that can sustain it. Uniform ellipticity prevents deterministic traps but does not itself make atypical local biases exponentially rare, so the key question is whether a depth-`r` *pre-regeneration* excursion forces either:

1. a long sequence of distinct unfavorable slabs, whose environmental probabilities tensorize under i.i.d.; or
2. repeated returns to a smaller trap region, which can be charged against positive velocity through an occupation-time/renewal inequality.

The desired quantitative target is a recursive or fractional-moment bound

`P_0(R_u>=2r) <= C P_0(R_u>=r)^{1+eta} + exp(-c r)`            (7.1)

for some `eta,c>0` and all large `r`, uniformly for `u` near `ell`. Any such superlinear recursion would bootstrap to moments beyond `15d+5`, close `(P*)_M`, and then close `(P)_M` via the established equivalences.

No claim is made here that (7.1) is already proved.