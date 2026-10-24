Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and no authenticated applied-effort receipt is exposed. SOURCE-LEVEL MOVEMENT SINCE THE PREVIOUS P13 REPORT is companion-derived: `L <= gamma_2 <= U_prim` is tightened to `L <= gamma_2 <= U_F < U_2 < U_prim` by P02's later two-step and Farey--Collatz certificates. P13 MECHANISM MOVEMENT: at correlated strip half-width `w=2`, the proved finite-to-infinite additive constant drops from `98` to the exact value `3540086521721361940943/157978390359101387424 < 23`.**

# P13 / T02 — complete short synchronizing language at width 2

## 1. Scope and continuity

This run follows `operations/PROGRESS20_2026-09-20.md` and its LIVE20 assignment of P13 to T02: dependence-preserving boundary recursion for the Chvatal--Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The same raw `Y` letter is used against every `X` letter in a column. No independent Bernoulli matching model is substituted.

Current source navigation remains Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. The v2 arXiv comments say that claims in the original preprint about the stochastic process and `gamma` were incorrect and were removed; the current abstract still calls the binary coefficient unresolved. The rigorous public lower endpoint retained here is

\[
L=0.792665992=\frac{99083249}{125000000}
\]

from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer. Li--Ren--Wen, published online 2026-03-02, still treat the two-string binary constant as open while studying the many-string generalization.

Necessary repository dependencies only:

- controlling policy `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`;
- previous P13 report `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T03-03-05Z__one-defect-reset-exact-error.md`, blob `2040446847b5594df0dd9d44ef64fd89bc3afab6`;
- latest P02 companion report `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T04-03-12Z__farey-collatz-dual-report.md`, blob `7f75484503fa5534cf357738df36fac84ace033f`;
- R17's exact width-`<=5` Bellman obstruction, used only to identify what this new transfer cannot yet do.

Short pre-LIVE20 P13 handoff, preserved and not reopened: P0342 had already been terminally handed off at frozen source metric `2/2`; the later P0205 screen admitted no successor because the source's `tau(infinity)` notation was not source-faithfully frozen. The retired I0051/clade work remains retired.

## 2. Source-level before/after, separate from the P13 mechanism

The preceding P13 report carried P02's primitive-content endpoint

\[
U_{\rm prim}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})},
\qquad t=\frac{256717}{800000}.
\]

Since then P02 first proved a two-step rational Collatz rate `lambda_2`, and then the current Farey--Collatz rate `lambda_F`, with

\[
\lambda_F<\lambda_2<\lambda-\varepsilon_{\rm prim}<1.
\]

Because `0<4t^2<1` and `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`, the project-level internally exact interval moves from

\[
\boxed{L\le\gamma_2\le U_{\rm prim}}
\]

to

\[
\boxed{L\le\gamma_2\le U_F<U_2<U_{\rm prim}},
\qquad U_F:=\frac{\log(4t^2)}{\log\lambda_F}.
}
\]

P02's exact log enclosure additionally proves

\[
U_F<
0.8262759427622826250151065815372966328234619961931900238808061833125629444302995644982136949828322096567193237968597809380
<U_2.
\]

This is the strict source-level interval shrink in this run's combined T02 state. It is P02's complementary covering/cone contribution. The new P13 result below is separate: it strengthens the rigorous finite-to-infinite lower transfer, but does not itself raise `L` in this run.

## 3. Exact dependence-preserving boundary recursion

Fix strip half-width `w` and write `m=2w`. A formal boundary state is

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m)\in\{0,1\}^{2m}.
\]

For one fresh source pair `(u,v)`, with `u` and `v` independent fair bits, set

\[
d_0=0,
\qquad
d_i=(1-g_i)\left(d_{i-1}\vee\mathbf 1_{\{x_i=v\}}\right),
\quad1\le i\le m.
\tag{3.1}
\]

Then the exact next state is

\[
x'=(x_2,\ldots,x_m,u),
\tag{3.2}
\]

\[
g'_i=g_{i+1}+d_{i+1}-d_i,
\quad1\le i<m,
\tag{3.3}
\]

\[
g'_m=(1-d_m)\mathbf 1_{\{u=v\}}.
\tag{3.4}
\]

The center-crossing strip reward is

\[
\rho_w(S;u,v)=g_{w+1}+d_{w+1}\in\{0,1\}.
\tag{3.5}
\]

The important dependence point is explicit in (3.1): a *single common bit* `v` drives every comparison `x_i=v` in the column. There is no independent match bit at each cell.

For later notation write the four equiprobable source-pair letters

\[
A=(0,1),\quad B=(1,0),\quad C=(0,0),\quad D=(1,1).
\]

## 4. General synchronizing-language transfer theorem

For a source word `r=z_1...z_k` in `{A,B,C,D}^k`, let `F_r` be the composition of the exact maps (3.1)--(3.4). Call `r` **synchronizing** if `F_r` is constant on all formal states. This is stronger than constancy on the reachable recurrent class.

Let `R` be any finite collection of synchronizing words and let

\[
\tau_R:=\min\{t\ge1:\text{some }r\in R\text{ ends at source time }t\}.
\]

### Theorem 4.1 — reset-language finite-to-infinite transfer

If `E tau_R < infinity`, then the correlated width-`w` strip chain has a unique stationary average reward `gamma_w`, and for every formal starting state `s` and every `N>=1`,

\[
\boxed{
\left|\mathbf E_sR_N-N\gamma_w\right|\le \mathbf E\tau_R,
}
\tag{4.1}
\]

where `R_N` is the cumulative strip reward over `N` source pairs. Consequently

\[
\boxed{
\gamma_2\ge\gamma_w\ge
\frac{\mathbf E_sR_N}{N}-\frac{\mathbf E\tau_R}{N}.
}
\tag{4.2}
\]

**Proof.** Start one strip chain from `s` and another from a stationary initial state, and drive them by the *same actual iid source-pair stream*. At the first ending time of a word `r in R`, both states are sent by the same constant map `F_r` to exactly the same state, regardless of their states before that word began. From that time onward they are identical under the common source stream. This coupling also gives uniqueness of the stationary law on the recurrent class.

Each one-step LCS strip reward lies in `{0,1}`. Therefore the two cumulative rewards can differ by at most one per step before coalescence and agree afterward. Hence

\[
|\mathbf E_sR_N-N\gamma_w|
\le \mathbf E\min(N,\tau_R)
\le \mathbf E\tau_R,
\]

which proves (4.1). Finally the width-`w` strip only restricts the admissible LCS paths in the full grid, so its asymptotic reward satisfies `gamma_w <= gamma_2`. Dividing (4.1) by `N` gives (4.2). QED.

No independent-cell domination enters this proof; all coupling randomness is the true iid source-pair stream.

## 5. New exact finite theorem at `w=2`: complete minimal reset language through length five

Set `w=2`, so `m=4` and there are exactly `2^(2m)=256` formal states. The new checker exhausts those states and every source word of length at most five under the exact recursion (3.1)--(3.4).

A synchronizing word is called **minimal for first hitting** if it contains no shorter synchronizing factor already retained. Exact exhaustive enumeration proves:

1. no synchronizing word has length `1`, `2`, or `3`;
2. the only minimal synchronizing words of length `4` are
   \[
   AAAA,\qquad BBBB;
   \]
3. there are exactly **78** additional minimal synchronizing words of length `5`;
4. hence the retained first-hit reset language has exactly **80** words.

This is a finite theorem whose core is the executed exhaustive checker, not an inference from sampling. Every candidate is evaluated on all 256 formal states, and every rejected word of length at most five is also tested unless it already contains a shorter reset factor.

The full 80-word language is printed in the archived exact output. In particular it is much richer than the previous analytic reset family: the one-defect theorem from the preceding run captured only a small subset of the short synchronizing language.

## 6. Exact prefix automaton and exact coupling constant

Let `tau_2^*` be the first ending time of any of those 80 reset words. Because `A,B,C,D` are the four actual source-pair values, each has probability exactly `1/4` independently over time.

The exact first-hit prefix automaton has **113** nonabsorbing prefix states. For each prefix state `q`, let `E_q` be the expected remaining time to absorption. The first-step equations are

\[
E_q=1+\frac14\sum_{z\in\{A,B,C,D\}:\delta(q,z)\text{ nonabsorbing}}
E_{\delta(q,z)}.
\tag{6.1}
\]

The checker solves all 113 equations over `fractions.Fraction` and then substitutes the solution back into every equation exactly. It obtains

\[
\boxed{
\mathbf E\tau_2^*
=
\frac{3540086521721361940943}
{157978390359101387424}
=22.408675728840986\ldots<23.
}
\tag{6.2}
\]

The previous P13 analytic one-defect theorem gave at `w=2`

\[
C_2^{\dagger}
=\frac{8\,4^{4}+10}{21}=98.
\]

Therefore the proved width-two additive transfer constant strictly improves by

\[
\boxed{
98-\mathbf E\tau_2^*
=
\frac{11941795733470574026609}
{157978390359101387424}
=75.591324271159010\ldots
}
\tag{6.3}
\]

and the new/old ratio is

\[
\frac{3540086521721361940943}{15481882255191935967552}
\approx0.228660.
\]

Combining Theorem 4.1 with (6.2), for every starting state and every horizon `N`,

\[
\boxed{
|\mathbf E_sR_N-N\gamma_{w=2}|
\le
\frac{3540086521721361940943}{157978390359101387424}
<23,
}
\tag{6.4}
\]

and hence

\[
\boxed{
\gamma_2\ge\gamma_{w=2}
\ge \frac{\mathbf E_sR_N}{N}-\frac{23}{N}.
}
\tag{6.5}
\]

Equation (6.5) is a proved asymptotic transfer, so future finite-horizon computations using it are legitimate lower certificates for the strip and therefore for `gamma_2`; a raw finite computation without this transfer would not be.

## 7. What this does *not* yet move

The stronger coupling does **not** raise the source lower endpoint in this run. R17's exact Bellman computation already proves

\[
\gamma_{w=2}<0.737503809<0.792665992=L,
\]

and in fact proves `gamma_w<L` for every `w<=5`. Thus even a zero-error stationary computation at `w=2` cannot beat the retained source lower endpoint. This is a hard quantitative obstruction, not a numerical-precision issue.

Accordingly:

- **source-level movement:** `U_prim -> U_F`, supplied by P02's independent covering/cone route;
- **P13 mechanism movement:** width-two finite-to-infinite constant `98 -> E tau_2^* < 23`;
- **no false promotion:** the width-two mechanism improvement is not reported as a new lower bound on `gamma_2`.

## 8. Failed/generalized route kept conditional

The width-two enumeration strongly suggests trying to characterize synchronizing words at arbitrary `m` rather than adding special reset patterns one at a time. A particularly tempting family is

\[
A^rZA^{m-r}
\quad\text{and}\quad
B^rZB^{m-r},
\qquad0\le r\le m,
\]

with one arbitrary defect `Z`. The previous run proved only one particular placement analytically. I did **not** complete a proof for all defect positions at arbitrary width in this run, so no width-uniform waiting-time improvement is claimed from that pattern. The exact width-two language theorem above does not justify extrapolation in `m`.

## 9. Residual obstruction and next attack

The fixed-width complete-language method demonstrates that the special analytic reset family was leaving a factor greater than four on the table already at `w=2`, but widths `w<=5` cannot move the source lower endpoint. The next useful attack is therefore to derive a **symbolic carry-level characterization of short synchronizing words for general `m=2w`**, beginning with the one-defect-anywhere family above, and to turn that characterization into a rigorous overlapping-pattern hitting-time bound. The quantitative objective is a coupling constant materially smaller than `Theta(4^(2w))`, ideally gaining at least a factor growing with `w`, so that widths `w>=6` become computationally useful.

If that symbolic characterization fails, the fallback is the earlier event-specific route: couple only the boundary event entering `gamma_w=2/3+pi_w(B_w)/3`, not the entire strip state.

## 10. Essential exact artifact

Executed checker:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T04-17-26Z__width2_sync_language_checker.py`

Creation commit: `1e30ef7e63a2d9ceae14e762c8e916932a0ffc47`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T04-17-26Z__width2_sync_language_checker.out`

Creation commit: `999691fe7e69946980050b75ba6e7dca4136a02a`.

The output ends `ALL_EXACT_CHECKS_PASS` and includes the complete 80-word minimal reset language, exact 113-state hitting-time solution, exact residual verification, previous constant `98`, and exact improvement.

## 11. Status and ledger_delta

The source problem remains **OPEN / PARTIAL**. The internally stronger upper endpoint is a private candidate pending normal independent review and priority checking; no public-priority claim is made.

```yaml
ledger_delta:
  slot: P13
  parent: T02-binary-LCS
  source_model: iid independent uniform binary strings
  bernoulli_matching_substitution: false
  source_before:
    lower: 0.792665992
    upper: U_prim
  source_after:
    lower: 0.792665992
    upper: U_F
    strict_relation: U_F < U_2 < U_prim
    movement_owner: P02 companion covering/cone route
  p13_mechanism_before:
    width: 2
    additive_error_constant: 98
  p13_mechanism_after:
    width: 2
    additive_error_constant_exact: 3540086521721361940943/157978390359101387424
    additive_error_constant_decimal: 22.408675728840986
    strict: true
  finite_to_infinite_transfer_proved: true
  source_lower_endpoint_moved_by_p13: false
  width_le_5_lower_route_blocked: true
  previous_p13_successor_handoff_preserved: P0342_terminal_then_P0205_no_admission
  retired_clade_reopened: false
  artifacts_executed: true
  source_status: OPEN_PARTIAL
  next_attack: general symbolic synchronizing-language/carry characterization for m=2w
```
