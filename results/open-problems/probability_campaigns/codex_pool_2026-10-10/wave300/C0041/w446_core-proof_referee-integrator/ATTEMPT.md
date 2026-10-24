# C0041: checked reduction and attempt at the missing quantitative lemma

Date: 2026-10-10. Author w446. Independent referee requested: w449. The parent theorem is **not** proved in this packet.

## Target and the hardest missing input

For iid uniformly elliptic nearest-neighbor RWRE on Z^d, d≥2, suppose P_0(X_n·ell→+∞)=1 for a fixed unit ell. The target is positive deterministic velocity in direction ell. The 2026-09-23 claimed proof reduces this to estimate (5): after changing to a transient coordinate direction, for some ε∈(0,1), the environment probability of `a_N(0)<N^(−ε)` is `O(N^(−D))` for every D, where `a_N(x)=P_{x,ω}(T_{x1+N}<T_{x1−1})`. The old owner attempt C0041-A001 instead identified integrability of time-valued regeneration as missing. The estimate would provide that integrability; proving it from one-direction transience is the genuinely hard new input. The manuscript's Sections 3–8 claim such a proof; I have not validated their full chain.

## A finite-region cost lemma, correcting the first-step factor

Let `S={x:0≤x1≤N−1}` and let `D⊂S` be finite with `m=|D|≥1`. Write `τ_S` for first exit from S, `τ_D` for first exit from D, and `τ=τ_S∧τ_D`. Fix a quenched environment with every allowed step at least κ>0. Assume `a_N(y+e1)≥a>0` for every y∈D, using the relative-height definition above. Then for each y∈D and integer k≥1,

`P_{x,ω}(V_y≥k) ≤ (1−κa)^(k−1)`, where `V_y=Σ_{n<τ}1{X_n=y}`.

Consequently, for integer t≥0,

`P_{x,ω}(τ>t) ≤ m(1−κa)^(ceil((t+1)/m)−1)`.

**Proof.** At any visit to y before τ, the chance of the prescribed first step y→y+e1 is at least κ. Conditional on that step, the probability of hitting height `y1+1+N` before dropping to `y1` is `a_N(y+e1)≥a`. Before that success the walk cannot revisit y, and the upper hit is beyond the top of S; if it exits D earlier, τ has already occurred. Thus the chance that this visit is the last visit to y before τ is at least κa. Apply the quenched strong Markov property at the successive visit stopping times: the tail in visit count is bounded by a geometric tail, with no independence assertion. On τ>t, there are t+1 visits to m sites, so some V_y≥ceil((t+1)/m). Union bound gives the displayed inequality. The argument also handles a y whose first upward step exits S immediately: the prescribed longer event is a subset of paths with no revisit before τ.

**Scope.** This proves a conditional finite-region time bound, not the required high-probability environment estimate. For a box of m=O(N^(2d−1)) sites and `a=N^(−ε)`, its exponent becomes useful when `t` exceeds order `mN^ε`. Spatial confinement and control of the probability that the `a_N` bound fails at adaptive sites are separate inputs. Uniform ellipticity supplies κ; omitting it is the local gap in the manuscript's Section 2.4 first-step argument.

## Attempt to derive the needed estimate and exact failure

One tempting route is to combine w444's L2 frequency of fully inward-oriented boxes with the preceding time bound. That does not yield estimate (5). The event `a_N(0)<N^(−ε)` is about a quenched crossing probability through an entire slab. L2 measures only one coherent inward-drift pattern in one finite box. There is no implication from a small `a_N` to that pattern, nor a summable enumeration of all alternative barriers and slow regions under the original assumptions. The adaptive-center bound L3 holds at a fixed deterministic horizon N; sending the horizon to infinity introduces the growing factor `(2N+1)^d`. This is the precise unproved bridge in that route.

The manuscript's different route is to control shared and independent two-walk endpoint laws on Gaussian scales, then derive an outward-order kernel with polynomial cost (Proposition 6.5) and a stationary-profile entropy contradiction (Proposition 8.6). I checked the statement of Proposition 6.5, its use in (46)–(48), and the conditional reduction in Proposition 2.5. I did not independently rederive Proposition 6.5 or the finite-window entropy transfer of Lemma 8.2. Their joint verification is the proof gate before any resolution label.

NEXT: Have w449 audit the finite-region cost lemma and κ correction; then independently audit the Proposition 6.5 outward-order bound and the Lemma 8.2 entropy transfer at their actual stopping layers.
