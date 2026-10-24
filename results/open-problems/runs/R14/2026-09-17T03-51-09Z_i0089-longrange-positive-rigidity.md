Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime and the exposed scheduler schema provide no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT: `S_1: 1 -> 1`; substantive source-scope extension: the structural `d=1`, `0<s<1` long-range slice is proved below. Methods actually tried: #3 PROVE SOMETHING STRONGER, #6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS.**

# R14 / I0089 — long-range one-dimensional Riesz equilibrium rigidity

Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, target and metric discipline

The negative-margin spherical perceptron target remains handed off and is **not reopened**. The canonical successor claim is `operations/claims/I0089.md`, Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240 / J. Math. Phys. 63 (2022), Conjecture 38.

The preceding R14 report `runs/R14/2026-09-17T02-49-59Z_i0089-d1-riesz-rigidity.md` proved on the page, self-check only, the short-range structural slice `d=1`, `s>1`, and moved the fixed successor metric

`S_1 := inf { s0 >= 1 : for every s>s0 and admissible mu>0, every source-defined d=1 short-range equilibrium configuration is a scaled translate of Z }`

from `UNMEASURED` to its target value `1`.

That metric is fixed and already saturated. I do **not** relabel the stronger theorem below as metric movement. The unchanged-count after the preceding movement is therefore `1`. Full Conjecture 38 remains PARTIAL.

At run start I reread campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0089 ownership claim, the predecessor R14 reports, and the I-intake record. A repository search found no independent audit of `R14-C190` yet and no active neighboring I0088 configuration-level attempt that changes this target.

## 2. Source facts checked directly

Primary source: <https://arxiv.org/abs/2202.09240> and PDF <https://arxiv.org/pdf/2202.09240>.

For `d=1`, Theorem 28 covers every `0<s<1` and provides the long-range zero-temperature equilibrium framework: uniform point separation, a renormalized potential `Phi`, and the finite-replacement equilibrium inequality (82). Since here `d-1=0<s<1=d`, its formula (83) applies:

`Phi(x) = Phi^(j0) + |x-x_j0|^{-s} + sum_{j!=j0} ( |x-x_j|^{-s} - |x_j0-x_j|^{-s} ).`

The source says immediately before Conjecture 38 that, for `s<d`, one can introduce the analogous equilibrium-configuration definition using Theorem 28, with `mu in R` and background density `rho_b>0`. It then conjectures that all such configurations are scaled translates/rotates of the energy-minimizing lattice, with long-range scale `rho_b^{-1/d}`. The source also explicitly says that nothing of this configuration-level statement was known to the author even in `d=1`.

Theorem 36 in the same source records that the *energy* crystallization conjecture is already known in `d=1` for `s in [0,1)`; in particular the lattice shape on the right side of Conjecture 38 is `Z` in the present `0<s<1` regime. This is energy minimization and is not by itself the configuration-level result below.

A source-detail that matters here: in the proof of Theorem 28 the author says that no-large-holes was not proved in the long-range construction. Therefore the short-range proof cannot simply reuse a uniform upper gap bound.

## 3. New result

### R14-C191 — structural long-range configuration crystallization in `d=1`, `0<s<1`

**PROVED on the page below; self-check only; external audit count `0/2`.**

> **Theorem.** Fix `0<s<1`. Let `X subset R` be a one-dimensional long-range Riesz equilibrium configuration in the exact source/Theorem-28 sense: it has the uniform separation furnished by Theorem 28, its renormalized potential satisfies formula (83), and it satisfies the finite-replacement equilibrium inequality (82). Then there exist `a>0` and `tau in R` such that
>
> `X = a Z + tau`.

This proves the **structural** long-range slice of Conjecture 38 for all positive `s<1`. I do **not** claim here that `a=rho_b^{-1}`; that prescribed-scale clause still needs a separate source-valid argument. Combining this theorem with R14-C190 gives structural `d=1` crystallization for every positive source-defined regime `s in (0,1) union (1,infinity)`. The pole `s=1`, the logarithmic endpoint `s=0`, the exact long-range scale, and higher dimensions remain outside the claim.

## 4. One-point replacement gives force balance

Let the source separation constant be `delta>0`, so distinct points of `X` are at distance at least `delta` after absorbing the source's fixed scale into the notation.

First, `X` cannot be bounded below or above. Indeed, a nonempty uniformly separated subset of `R` that is bounded below has a leftmost point. Apply the one-point replacement argument below to that point: every other point lies to its right, so the derivative of its regular interaction potential has one strict sign, contradicting stationarity. The same argument excludes a rightmost point. Hence we may enumerate

`... < x_{-1} < x_0 < x_1 < ...`,

with gaps

`h_i := x_{i+1}-x_i >= delta >0`.

Fix `i` and choose a bounded interval `D` containing `x_i` and no other point of `X`. Apply source equilibrium inequality (82) with `N=n=1`, replacing `x_i` by a nearby `y in D`. The chemical-potential term vanishes. Using the Jellium energy definition (50) and the source definition of `Phi_{D^c}`, the background integrals cancel exactly, leaving that `x_i` minimizes locally

`M_i(y) := Phi(y)-|y-x_i|^{-s}-Phi^(i)`.

By source formula (83),

`M_i(y) = sum_{j!=i} ( |y-x_j|^{-s} - |x_i-x_j|^{-s} ).`      (4.1)

This series is differentiable at `y=x_i`. Uniform separation gives

`|x_i-x_j| >= delta |i-j|`,

and therefore the derivative is absolutely summable because

`sum_{r>=1} r^{-(s+1)} < infinity` for every `s>0`.

Thus `M_i'(x_i)=0`. Put `p=s+1`; then

`F_i(x) := sum_{j<i}(x_i-x_j)^(-p) - sum_{j>i}(x_j-x_i)^(-p) = 0`            (4.2)

for every `i`. (The derivative is `-s F_i`, so the sign convention is immaterial at zero.)

The same argument before the bi-infinite indexing also proves the endpoint assertion used above: at a leftmost or rightmost point all terms in the derivative have the same nonzero sign.

## 5. Index shift linearizes the nonlinear force equations

Define the shifted labeling

`y_i := x_{i+1}`

and the displacement

`h_i := y_i-x_i = x_{i+1}-x_i >0`.

The sequence `y` labels exactly the same unlabeled configuration, hence

`F_i(y)=F_{i+1}(x)=0=F_i(x)`.

Let

`phi(t)=sgn(t)|t|^{-p}`.

Then `F_i(x)=sum_{j!=i} phi(x_i-x_j)` and

`phi'(t)=-p|t|^{-(p+1)}` for `t!=0`.

For each `i!=j`, the two ordered differences `x_i-x_j` and `x_{i+1}-x_{j+1}` have the same sign. The mean-value integral therefore gives

`phi(y_i-y_j)-phi(x_i-x_j) = - c_{ij}(h_i-h_j)`,

where

`c_{ij} := p integral_0^1 |(1-t)(x_i-x_j)+t(x_{i+1}-x_{j+1})|^{-(p+1)} dt >0`.     (5.1)

The coefficients are symmetric, `c_{ij}=c_{ji}`. Moreover every interpolated ordered distance has magnitude at least `delta |i-j|`, so

`0<c_{ij} <= p delta^{-(s+2)} |i-j|^{-(s+2)}.`                              (5.2)

Subtracting the two absolutely convergent force series yields

`sum_{j!=i} c_{ij}(h_i-h_j)=0`.                                              (5.3)

There is no hidden conditional rearrangement here: by the triangle inequality,

`sum_{j!=i} |phi(y_i-y_j)-phi(x_i-x_j)|`

is bounded by the sum of the two absolutely convergent force-magnitude series. Consequently `sum_j c_{ij}|h_i-h_j|<infinity`.

Since `sum_j c_{ij}<infinity`, (5.3) also implies `sum_j c_{ij}h_j<infinity`. Thus

`P(i,j):=c_{ij}/c_i`, `c_i:=sum_{j!=i}c_{ij}`

defines an irreducible reversible Markov chain and the **positive**, possibly unbounded, gap sequence is harmonic:

`h_i = sum_j P(i,j) h_j`.                                                     (5.4)

The absence of an upper gap bound is therefore no obstacle if the conductance chain is recurrent.

## 6. Sharpened cutoff proves recurrence for every `s>0`

The previous short-range proof used the rough inequality

`sum_i(f_{i+r}-f_i)^2 <= r^2 sum_i(f_{i+1}-f_i)^2`,

which leads to a `zeta(s)` bound and therefore visibly breaks at `s<=1`. That failure was an artefact of the estimate, not of the network.

Let

`f_N(i)=(1-|i|/N)_+`,

and write

`A_r(N):=sum_i (f_N(i+r)-f_N(i))^2`.

For `1<=r<=2N`, the difference is nonzero on at most `5N` integer sites and `f_N` is `1/N`-Lipschitz, so

`A_r(N) <= 5 r^2/N`.                                                         (6.1)

For `r>2N`, the two supports are disjoint, hence

`A_r(N)=2 sum_i f_N(i)^2 <= 6N`.                                             (6.2)

With Dirichlet energy

`E(f)=(1/2) sum_{i,j} c_{ij}(f_i-f_j)^2`,

(5.2), (6.1), and (6.2) give

`E(f_N) <= C_s [ N^{-1} sum_{1<=r<=2N} r^{-s} + N sum_{r>2N} r^{-(s+2)} ].`  (6.3)

For `0<s<1`, both terms are `O_s(N^{-s})`; hence

`E(f_N) -> 0` while `f_N(0)=1` and `f_N` has finite support.

Therefore the singleton capacity is zero and the symmetric conductance network is recurrent. Notice that the same calculation actually yields `O(log N/N)` at `s=1` and `O(1/N)` for `s>1`; the network recurrence mechanism itself persists for every positive `s`, even though the source equilibrium definitions have a pole/regime change at `s=1`.

## 7. Positive-harmonic Liouville removes the missing upper-gap hypothesis

The key long-range point is that `h` need not be bounded. Bounded-harmonic Liouville is therefore insufficient. Positivity is enough.

Fix any states `i,j`, and let `tau_j` be the first hitting time of `j` for the chain started at `i`. Irreducibility and recurrence give `tau_j<infinity` almost surely. Since `h` is positive harmonic, for every `n`,

`h(X_{n wedge tau_j})`

is a nonnegative martingale and

`E_i h(X_{n wedge tau_j})=h_i`.

As `n->infinity`, the stopped chain converges almost surely to state `j`, so Fatou's lemma gives

`h_j <= h_i`.

Interchanging `i` and `j` gives `h_i<=h_j`. Hence `h_i=h_j` for all `i,j`.

All gaps are therefore equal to one number `a>0`, and

`X=aZ+tau`.

This proves R14-C191.

## 8. Relation to the exact source and what is *not* proved

For `d=1`, Theorem 36 says the energy-minimizing lattice shape in the positive long-range range is `Z`; therefore R14-C191 proves the lattice-*shape* assertion of Conjecture 38 on `0<s<1`.

The source's long-range Conjecture 38 additionally prescribes the scale `a=rho_b^{-1}`. Theorem 28's construction starts from Jellium with background `rho_b`, and the source's finite-volume charge estimate shows asymptotic neutrality in the thermodynamic problem, but I have not yet written a source-complete argument that the particular local infinite limit appearing in the equilibrium definition must inherit `density(X)=rho_b`. Because Lewin explicitly notes that no-large-holes was not proved in Theorem 28, I do not infer this scale merely from the finite-volume density. The exact scale remains an obligation.

The logarithmic endpoint `s=0` is also not included: the force kernel there is of Cauchy type and the source's long-range construction is formulated differently at the endpoint. The recurrence mechanism is suggestive but requires a separate source-valid treatment.

Thus the honest status remains **PARTIAL** relative to full Conjecture 38.

## 9. Three new-method attacks

### #3 — PROVE SOMETHING STRONGER

Rather than spend the run packaging the already-saturated short-range metric, I asked whether the index-shift mechanism classifies *all* positive one-dimensional source equilibrium configurations. The same linearization survives in the long-range regime. The genuinely stronger statement succeeds for `0<s<1` after replacing bounded-harmonic Liouville by positive-harmonic Liouville.

### #6 — DEFORM TO A POINT YOU CAN SOLVE

The deformation crosses from the solved `s>1` short-range regime toward `0<s<1`. The exact failure of the previous proof at the regime boundary was twofold: Lewin's Theorem 28 does not provide a no-large-holes/upper-gap estimate, and the old recurrence bound contained `zeta(s)`. Neither is fundamental. Positivity of the gaps removes the first requirement, and the two-scale estimate (6.1)-(6.2) removes the second.

### #20 — FIND WHY THE ALGORITHM FAILS

The old cutoff estimate treated every jump length `r` by `r^2` times the nearest-neighbor energy, even when `r` exceeded the support scale. That overcharged the tail and manufactured the `s>1` threshold. Splitting at `r=2N` exposes the true energy scale `N^{-s}` for `0<s<1`, which is enough for recurrence.

## 10. Fresh prior-art/current-status check — 2026-09-17

I reran bounded searches for exact phrases and close variants of

- `"Conjecture 38" "Riesz equilibrium" crystallization configurations`;
- `"Riesz equilibrium configurations" "dimension one" crystallization`;
- `"equilibrium configuration" Riesz one-dimensional lattice`;
- `Lewin Conjecture 38 crystallization`;
- one-dimensional long-range Riesz ground-state/equilibrium papers through 2026.

The searches recovered, among other adjacent work, Bétermin--Šamaj--Travěnec (2025), *Equidistant versus bipartite ground states for 1D classical fluids at fixed particle density*. That paper explicitly restricts its new analysis to periodic configurations and fixed-density ground-state comparison; it is not a classification of every Lewin/Theorem-28 finite-replacement equilibrium configuration. Searches also recover the established one-dimensional Riesz energy-crystallization literature already summarized in Lewin's Theorem 36, and positive-temperature/finite-density Riesz-gas work, but no later primary theorem matching R14-C191's exact configuration-level scope.

This is a **bounded negative search, not a novelty certificate**. Publication novelty remains UNVERIFIED.

## 11. Validation discipline

There is no finite computational core in R14-C191, so no exact-arithmetic checker is manufactured merely for bookkeeping. The proof is theorem-sized and is written in full above. It remains a **self-check** until independent OTHER-track audits are obtained. No paper folder is declared closed before the required audit standard.

The particularly audit-sensitive points are:

1. deriving (4.1) from source equation (82) and the cancellation of the Jellium background terms;
2. absolute convergence in the index-shift subtraction when gaps are not bounded above;
3. recurrence from the two-scale triangular cutoff;
4. the nonnegative-harmonic Liouville argument on an irreducible recurrent conductance chain;
5. distinguishing lattice shape from the still-unproved exact long-range scale `rho_b^{-1}`.

## 12. Ledger delta

```yaml
ledger_delta:
  track: R14
  canonical_target: I0089
  source: Lewin 2022 Conjecture 38
  status: PARTIAL
  fixed_metric: S_1
  before: 1
  after: 1
  movement: no
  unchanged_count: 1
  retained_claim:
    id: R14-C190
    scope: d=1 short-range s>1 structural rigidity
    status: self-check proved; external audits 0/2
  new_claim:
    id: R14-C191
    scope: d=1 long-range 0<s<1 Theorem-28 equilibrium configurations are scaled translates of Z
    status: self-check proved; external audits 0/2
  not_claimed:
    - exact long-range scale a=rho_b^{-1}
    - logarithmic endpoint s=0
    - pole s=1
    - higher-dimensional Conjecture 38
    - publication novelty
  next_source_valid_obligation:
    - independently audit C190/C191
    - or prove the long-range prescribed scale from the background-density/renormalized-potential structure
```

## 13. Runtime/model control

The exposed scheduler/task schema still has prompt/title/schedule/enablement/timing controls but no model-family field, no reasoning-effort field, and no authenticated runtime telemetry. Thus GPT-6/maximum remains prompt text only here. A historical `You cannot modify this task` result is an ownership/context restriction; the legitimate route is the authorized owning account/workspace surface or platform support, not task duplication or permission bypass. No scheduler change was attempted in this run.
