Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE MOVEMENT: certified binary Chvátal–Sankoff interval shrinks from `0.792665992 <= gamma_2 < 0.8262759427622826251` to `0.792665992 <= gamma_2 < 0.826275942762282625015106581538`; width decreases by `8.4893418462e-20`. MECHANISM MOVEMENT (separate): exact dependence-preserving carry extinction, an exact boundary-event coboundary formula for the correlated strip, a reachable-state `2w` reset (improving the older `4w` formal-state reset), and an explicit finite-to-infinite error bound. The new boundary theorem itself does not yet improve the lower endpoint.

# P13 T02 — correlated binary LCS boundary recursion, reachable reset, and certified endpoint refinement

## 1. Scope and recovered state

This run follows `operations/PROGRESS20_2026-09-20.md`, latest LIVE20 assignment T02. The source problem is the Chvátal–Sankoff constant for two independent uniformly random binary strings,
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbb E L_n}{n}.
\]
Tiskin, arXiv:2212.01582v2, still presents the binary problem as unresolved; importantly, the actual source model has raw-letter dependence along rows and columns and is not the independent Bernoulli matching model. Heineman–Miller–Reichman–Salls–Sárközy–Soiffer, arXiv:2407.10925, give the certified lower endpoint `0.792665992`.

The complementary P02 route is `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T00-42-00Z__run-report.md`. P02 owns the variational/interpolation direction and had already refined the inherited C045 upper certificate to
\[
\gamma_2<0.8262759427622826251.
\]
I do not duplicate that variational proof here. I reuse the exact C045 rational data only to compile a sharper rigorous decimal endpoint after developing the boundary route below.

The main prior correlated-strip dependency is R17's
`runs/prob10_2026-09-20/PROB10-02/20260920T0012Z_r17_carry_separator_c1e8.md`.
It introduced the exact width-`w` strip state retaining the raw binary window and frontier gradients, and the carry factorization used here.

Short previous-P13-successor handoff, as requested: before LIVE20, P13 had terminally handed off P0342 after its frozen `2/2` source metric and was subsequently `ADMISSION_PENDING`; the newest pre-LIVE20 P13 report was `proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T23-24-30Z__admission-p0205-resolvent-source-ambiguity-i0054-c078.md`, which admitted no P0205 successor because the source's `tau(infinity)` notation was ambiguous. That history is preserved only as a handoff. Retired I0051/clade work is not reopened.

## 2. Exact correlated strip transition

Fix strip half-width `w` and write `m=2w`. At a column time the state is
\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m),\qquad x_i,g_i\in\{0,1\},
\]
where the `x_i` are the actual raw `X` letters in the moving width-`2w` window and the `g_i` are vertical frontier increments of the band-restricted LCS dynamic program. A fresh column exposes one actual source pair `(u,v)`, with `u,v` independent fair bits. Crucially, the same `v` is used against every `x_i`; we do not replace the match indicators by independent Bernoulli variables.

For a fixed `v`, define carries
\[
d_0^{(v)}=0,\qquad
 d_i^{(v)}=(1-g_i)\bigl(d_{i-1}^{(v)}\vee {\bf1}_{\{x_i=v\}}\bigr),\quad 1\le i\le m.
\tag{2.1}
\]
Then R17's exact transition is
\[
 g_i'=g_{i+1}+d_{i+1}^{(v)}-d_i^{(v)},\quad 1\le i<m,
\tag{2.2}
\]
\[
 g_m'=(1-d_m^{(v)}){\bf1}_{\{u=v\}},
\tag{2.3}
\]
and the one-column diagonal reward is
\[
 \rho(S;u,v)=g_{w+1}+d_{w+1}^{(v)}.
\tag{2.4}
\]
The raw window shifts by `x'=(x_2,...,x_m,u)`.

Everything below is for this dependent source-faithful transition.

## 3. The boundary carry extinction identity

### Theorem 3.1 (exact one-column boundary recursion)

Run (2.1) twice with the same `(x,g,v)` but with left incoming carries `c_0=0` and `c_0=1`; call the resulting carries `c_i^{(0)}` and `c_i^{(1)}`. Then for every `i`,
\[
\Delta_i:=c_i^{(1)}-c_i^{(0)}
=\prod_{j=1}^i(1-g_j){\bf1}_{\{x_j\ne v\}}.
\tag{3.1}
\]
In particular `Delta_i` is `1` until a unique possible extinction point and is `0` thereafter. Consequently the outgoing-gradient discrepancy
\[
\Delta_{i+1}-\Delta_i
\]
is nonzero at at most one position: a single boundary discrepancy cannot branch within a column.

**Proof.** At `i=0`, the carry difference is `1`. Suppose the formula holds through `i-1`. If `g_i=1`, both recursions reset to zero, so `Delta_i=0`. If `g_i=0` and `x_i=v`, both recursions become one, again giving `Delta_i=0`. If `g_i=0` and `x_i!=v`, each recursion simply copies its previous carry, so `Delta_i=Delta_{i-1}`. These are exactly the three cases in the product on the right of (3.1). The last assertion follows because a `{0,1}` sequence of the form `1,...,1,0,...,0` has at most one nonzero first difference. QED.

If the `x_j` are iid fair source letters and `v` is an independent fair column letter, then, for any fixed gradient pattern,
\[
\{\Delta_k=1\}\subseteq\{x_1=\cdots=x_k=1-v\},
\]
so
\[
\Pr(\Delta_k=1)\le 2^{-k},
\tag{3.2}
\]
with equality for `g=0^k`. The exact checker exhausts `k<=8` and obtains `1/2,1/4,...,1/256`.

This is a dependence-preserving statement: the same `v` appears in all factors. The numerical `2^{-k}` comes from counting the raw-letter event that the entire block is the single opposite symbol, not from replacing the cells by independent matching coins.

## 4. An exact boundary-event representation of the strip growth

Define the one-site additive potential
\[
h_0(S)=\sum_{i=w+1}^{m-1} g_i+\frac23 g_m.
\tag{4.1}
\]
Let `P_w` denote the true correlated strip transition and `r(S)=E[rho(S;u,v)|S]` its expected one-step reward.

For each `v`, the carry `d_m^(v)` is `1` exactly when, after the last index at which `g=1` resets the carry, the remaining raw `x` suffix contains the symbol `v`. Let `B_w(S)` be the event/property

> `g_m=0` and the zero-gradient suffix after the final `g_i=1` contains both binary symbols.

(If there is no `g_i=1`, the suffix begins at `x_1`.)

### Theorem 4.1 (boundary coboundary identity)

For every formal strip state,
\[
r(S)+(P_wh_0)(S)-h_0(S)
=\frac23+\frac13{\bf1}_{B_w(S)}.
\tag{4.2}
\]
Hence, for the stationary law `pi_w` of the reachable strip chain,
\[
\boxed{\gamma_w=\frac23+\frac13\pi_w(B_w)},
\tag{4.3}
\]
where `gamma_w` is the stationary strip reward, and `gamma_w<=gamma_2` because the strip only restricts admissible LCS paths.

**Proof.** For fixed `v`, substitute (2.2)–(2.4) into (4.1). The interior carry terms telescope:
\[
\rho+h_0(S')-h_0(S)
=\frac13g_m+d_m^{(v)}+\frac23(1-d_m^{(v)}){\bf1}_{\{u=v\}}.
\]
Averaging first over `u` gives
\[
\frac13+\frac13g_m+\frac23d_m^{(v)}.
\]
Averaging over `v` gives
\[
\frac13+\frac13g_m+\frac13(d_m^{(0)}+d_m^{(1)}).
\tag{4.4}
\]
If `g_m=1`, both terminal carries are zero and (4.4) is `2/3`. If `g_m=0`, at least one terminal carry is one (the nonempty zero-gradient suffix contains at least its final bit). The sum of the two carries is one exactly when that suffix is monochromatic and is two exactly when it contains both symbols. Thus (4.4) is `2/3` off `B_w` and `1` on `B_w`, proving (4.2). Averaging (4.2) under stationarity kills the coboundary and gives (4.3). QED.

This is the main structural simplification of this run: the whole correlated strip growth rate is reduced exactly to the stationary probability of one explicit boundary suffix event.

The current source lower endpoint `L=0.792665992` would be beaten by a strip if and only if one can certify
\[
\pi_w(B_w)>3L-2
=\frac{47249747}{125000000}
=0.377997976.
\tag{4.5}
\]
This is now the quantitative target for the next boundary computation.

## 5. Reachable states reset in `2w`, not `4w`

R17's earlier uniqueness argument used the word `(u,v)=(0,1)` repeated `4w` times to reset every *formal* state. For finite-to-infinite transfer we only need the actually reachable DP states, where a factor-of-two geometric argument is available.

### Theorem 5.1 (reachable `2w` constant-mismatch reset)

Let `S` be any reachable width-`w` strip state. Put `m=2w`. For either `a in {0,1}`, append `m` consecutive source pairs
\[
(u_t,v_t)=(a,1-a),\qquad t=1,\ldots,m.
\tag{5.1}
\]
Then the terminal state is independent of `S` and equals
\[
z_a=(a^m;0^m).
\tag{5.2}
\]

**Proof.** Because `S` is reachable, it is a genuine band-DP frontier at some column `j`, with raw window `X_{j-w+1},...,X_{j+w}`. Under (5.1), after `m=2w` steps the final raw window is entirely the newly appended letter `a`, so its `x` component is `a^m`.

It remains to prove every final gradient is zero. Let the final column be `J=j+2w`. The final frontier rows range from `J-w=j+w` through `J+w=j+3w`. Every `X` position strictly larger than `j+w` is one of the newly appended `a` letters. Any diagonal edge in the width-`w` band using such an `X` position `r>j+w` must pair it with a `Y` position `s>=r-w>j`. But all newly appended `Y_{j+1},...,Y_J` equal `1-a`, so no such diagonal match exists. Therefore no score can be gained after the path's row first reaches `j+w`. Any optimal band path to `(i,J)`, `i>=j+w`, can be truncated at row `j+w` without deleting a scored diagonal, while any optimal path to `(j+w,J)` can be extended vertically to `(i,J)` inside the band at zero cost. Hence all final DP values across those rows are equal, so every final frontier gradient is zero. QED.

The two reset words `(0,1)^m` and `(1,0)^m` are disjoint and each has probability `4^{-m}`. Thus for every reachable state
\[
P_w^m(S,\cdot)\ge 4^{-m}\delta_{z_0}+4^{-m}\delta_{z_1}.
\tag{5.3}
\]
Writing
\[
q_w=2\,4^{-2w},
\tag{5.4}
\]
the `m`-step Dobrushin coefficient is at most `1-q_w`. This proves uniqueness of `pi_w` and gives the explicit contraction
\[
\operatorname{osc}(P_w^N f)
\le \operatorname{osc}(f)(1-q_w)^{\lfloor N/(2w)\rfloor}.
\tag{5.5}
\]

Combining (4.3) with (5.5), for every reachable start `S`,
\[
\boxed{
\left|\frac23+\frac13\Pr_S(B_w(S_N))-\gamma_w\right|
\le \frac13(1-q_w)^{\lfloor N/(2w)\rfloor}.
}
\tag{5.6}
\]
This is a direct finite-horizon-to-infinite-strip error bound for the new boundary statistic.

There is also a cumulative-reward form. Since the expected one-step reward lies in `[0,1]`, summing the contraction over time gives, for `R_N=sum_{t=0}^{N-1} rho_t`,
\[
\boxed{
|\mathbb E_S R_N-N\gamma_w|
\le\sum_{t\ge0}(1-q_w)^{\lfloor t/(2w)\rfloor}
=\frac{2w}{q_w}=w4^{2w}.
}
\tag{5.7}
\]
Therefore any exact finite computation of `E_S R_N` has the rigorous source transfer
\[
\boxed{
\gamma_2\ge\gamma_w\ge \frac{\mathbb E_S R_N}{N}-\frac{w4^{2w}}{N}.
}
\tag{5.8}
\]
The constant is large, but the transfer is explicit and fully proved; finite strip arithmetic is no longer silently promoted to an asymptotic `gamma_2` statement.

The exact checker confirms the reachable-state counts `14,224,3098,39774` for `w=1,2,3,4`, verifies the `2w` reset state-by-state, and returns the corresponding uniform additive constants `16,512,12288,262144` in (5.7).

## 6. A proof-class obstruction: all-formal one-site potentials stop at `2/3`

The run also identifies why the earlier separator's very cheap local ansatz stalls.

Consider any position-dependent additive one-site potential
\[
h_\phi(S)=\sum_{i=1}^{m}\phi_i(x_i,g_i),
\tag{6.1}
\]
with arbitrary real values of the four-symbol functions `phi_i`. Suppose its Bellman lower inequality is required on every formal binary state `(x,g)`.

### Theorem 6.1

The best uniform Bellman residual obtainable in the class (6.1) is exactly `2/3` for every `w`.

**Proof of upper bound.** Consider the four constant formal phases `S_{ab}=(a^m;b^m)`. Give them weights
\[
\Pr(a=0,b=0)=\frac13,\quad
\Pr(0,1)=\frac16,\quad
\Pr(1,0)=\frac13,\quad
\Pr(1,1)=\frac16.
\tag{6.2}
\]
Equivalently `a` is fair and `b` is independent with `Pr(b=1)=1/3`. For every interior site the transition preserves the constant symbol `(a,b)`. At the fresh right boundary, averaging over `(u,v)` sends the weighted law of `(a,b)` back to the same law: `u` is fair, the new final gradient has probability `1/3` of being one, and by bit-complement symmetry these are independent. Hence
\[
\sum_{a,b}p_{ab}\,\mathbb E[h_\phi(S'_{ab})-h_\phi(S_{ab})]=0
\]
for every choice of the one-site functions. The expected reward in a `b=1` phase is `1`; in a `b=0` phase it is `1/2`. Under (6.2) its weighted mean is
\[
\frac13\cdot1+\frac23\cdot\frac12=\frac23.
\]
Therefore the minimum of the four Bellman residuals is at most their weighted average `2/3`.

**Lower bound.** The explicit potential (4.1) is itself of form (6.1), and (4.2) shows its residual is always either `2/3` or `1`. Thus `2/3` is attained. QED.

So another optimization of single-site weights cannot advance the lower endpoint. A successful separator must use reachable-state structure, a genuinely nonlocal boundary suffix statistic, or higher-order information that escapes this dual obstruction.

## 7. Certified source-level interval shrink

This part is deliberately separated from the new boundary mechanism.

The inherited C045 exact upper certificate has
\[
x=y=\frac{256717}{800000},\qquad
A=4x^2=\frac{65903618089}{160000000000},
\]
and
\[
\lambda=
\frac{10114875937111444750637950885399422919832438289108176982868202874026753}
{29591135160849999997918500618240000000000000000000000000000000000000000}.
\]
The already-proved covering transfer gives the continuous endpoint
\[
\alpha=\frac{\log A}{\log\lambda}.
\]
P02 had certified `alpha < 0.8262759427622826251`.

I reran this same exact rational certificate with rational upper/lower bounds for `-log z` from
\[
-\log z=2\sum_{k\ge0}\frac{y^{2k+1}}{2k+1},\qquad y=\frac{1-z}{1+z},
\]
and the positive geometric tail bound. With 500 terms for `A` and 700 for `lambda`, exact rational arithmetic gives
\[
\alpha<0.826275942762282625015106581538.
\tag{7.1}
\]
No floating-point inequality is used in the certificate.

Thus the source interval moves from
\[
[0.792665992,\ 0.8262759427622826251)
\]
to
\[
\boxed{[0.792665992,\ 0.826275942762282625015106581538)}.
\tag{7.2}
\]
Its displayed certified width moves from
\[
0.0336099507622826251
\]
to
\[
0.033609950762282625015106581538,
\]
a strict decrease of
\[
\boxed{8.4893418462\times10^{-20}}.
\]
This is genuine source-level interval movement because the C045 finite certificate already has the proved asymptotic covering transfer. It is, however, an endpoint-compilation improvement, not a numerical consequence of Theorems 3.1–5.1. The boundary theorems are the separate mechanism gain intended to support a future nontrivial lower movement.

## 8. Failed / superseded boundary route recorded honestly

Exploratory P13 artifacts written earlier in this run at `00-47-00Z` include a stronger-looking negative-binomial/Chernoff propagation estimate. I am **not using that stronger estimate in this report**. Its intended step was a conditional tail `Pr(J>=r | history)<=2^{-r}` for repeated disagreement jumps. In the true correlated lookahead state, the `X` bits a future jump may traverse can already be present in, and correlated with, the current frontier state, so conditional freshness is not automatic. The one-column identity (3.1) is exact, but iterating it with iid conditional jumps needs an additional argument that has not been proved here. The reachable `2w` reset and Dobrushin proof in Section 5 avoids that gap entirely and is the certified finite-to-infinite bound for this report.

This also explains why independent Bernoulli matching cannot be substituted: doing so would make precisely the unjustified conditional-independence step look automatic.

## 9. P02 coordination and next attack

P02 remains on the variational/interpolation side. P13's complementary object is now the exact boundary probability in (4.3). The next source-relevant lower attack is therefore sharply formulated:

1. build a finite boundary/suffix recursion that computes or rigorously brackets `pi_w(B_w)` without enumerating all `2^(4w)` formal states;
2. preserve the shared raw `X` window and common column letter `v` exactly;
3. target the explicit threshold `47249747/125000000` from (4.5);
4. combine any finite computation with (5.6) or (5.8), rather than calling a finite strip value a bound on `gamma_2` without transfer.

The one-site dual theorem rules out another linear-gradient-weight tuning as the next route. The promising state compression is the zero-gradient boundary suffix together with just enough carry/reachability information to evolve its `B_w` probability.

## 10. Executed exact checks and immutable artifacts

New checker:
`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T01-19-00Z__reachable_reset_endpoint_checker.py`

Output:
`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T01-19-00Z__reachable_reset_endpoint_checker.out`

Executed output:
```text
UPPER_BEFORE 0.8262759427622826251
UPPER_AFTER 0.826275942762282625015106581538
WIDTH_BEFORE 0.0336099507622826251
WIDTH_AFTER 0.033609950762282625015106581538
STRICT_DECREASE 8.4893418462E-20
ENDPOINT_PASS
CARRY_EXTINCTION_K_LE_8_PASS
REACHABLE_RESET 1 states 14 length 2 minorization_q 1/8 finite_to_infinite_additive_C 16
REACHABLE_RESET 2 states 224 length 4 minorization_q 1/128 finite_to_infinite_additive_C 512
REACHABLE_RESET 3 states 3098 length 6 minorization_q 1/2048 finite_to_infinite_additive_C 12288
REACHABLE_RESET 4 states 39774 length 8 minorization_q 1/32768 finite_to_infinite_additive_C 262144
REACHABLE_2W_RESET_AND_MIXING_CONSTANT_PASS
ONE_SITE_ADDITIVE_DUAL_OBSTRUCTION_PASS
ALL_EXACT_CHECKS_PASS
```

These finite checks are self-checks for the analytic proofs above; they are not treated as universal proofs beyond their enumerated ranges.

## 11. ledger_delta

```yaml
ledger_delta:
  slot: P13
  native_slot_id: 6aa7b253b37c8191b693d8dc79298d37
  assignment: T02-binary-Chvatal-Sankoff-boundary-recursion
  source_model: iid-uniform-binary-strings
  forbidden_substitution: independent-Bernoulli-matching
  source_metric:
    type: certified_interval_width
    before_interval: "0.792665992 <= gamma_2 < 0.8262759427622826251"
    after_interval: "0.792665992 <= gamma_2 < 0.826275942762282625015106581538"
    before_width: "0.0336099507622826251"
    after_width: "0.033609950762282625015106581538"
    strict_width_decrease: "8.4893418462e-20"
    movement_source: exact-recompilation-of-inherited-C045-with-existing-proved-transfer
  mechanism_gain:
    - exact carry-boundary discrepancy product identity
    - nonbranching one-column boundary extinction
    - exact strip identity gamma_w = 2/3 + pi_w(B_w)/3
    - reachable-state constant-mismatch reset length improved 4w -> 2w
    - uniform finite-to-infinite error |E R_N-N gamma_w| <= w*4^(2w)
    - all-formal one-site additive Bellman potentials proved capped at 2/3
  lower_endpoint_moved: false
  boundary_theorem_itself_moved_source_endpoint: false
  source_status: ACTIVE-PARTIAL
  p02_coordination: variational-route-left-to-P02
  previous_p13_handoff: P0342-terminal-then-admission-pending-no-P0205-claim
  retired_clade_reopened: false
  superseded_unproved_route: conditional-geometric-disagreement-Chernoff-not-used
  next_attack: finite reachable boundary-suffix recursion for pi_w(B_w), target > 47249747/125000000
```
