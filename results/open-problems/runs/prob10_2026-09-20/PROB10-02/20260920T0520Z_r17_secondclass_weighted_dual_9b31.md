Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated model/effort selector or applied-effort receipt is exposed here, so I do not claim otherwise. **NO R17 SOURCE-ENDPOINT MOVEMENT THIS RUN:** the exact project interval inherited at run start is `L <= gamma_2 <= U_W`, hence `W_before=W_after=U_W-L`; status **OPEN / PARTIAL**. Three materially different attacks were executed: **(A)** a second-class-particle/carrier description of a single discrepancy, **(B)** an environment-weighted one-step Collatz/Bellman dual after finite burn-in, and **(C)** a deterministic boundary-regeneration hypothesis, refuted by an exact interior self-loop.

# PROB10-02 / R17 — second-class defect geometry and an environment-weighted edge-chain dual

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}{n}
\]
for two independent iid uniform binary strings. Every transition below uses the same fresh source bit `v` against the entire raw window; no independent Bernoulli matching array and no simulation confidence interval is substituted.

## 0. Continuity, actual R17 handoff, ownership, and current metric

Controlling owner directive recovered: `operations/PROB10_2026-09-20.md`.

The actual pre-refocus R17 successor H0021 remains correctly handed off. `operations/claims/H0021.md` (blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`) says **UNASSIGNED / RELEASED BY R17**, preserves the R16 history and R17 report `runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`, preserves navigation commit `c8891869a1335d67bada83f23f63f2ce09603565`, and leaves `Delta_near=2`. No H0021 file or artifact is changed here.

Newest own completed PROB10-02 dependency before this run:

`runs/prob10_2026-09-20/PROB10-02/20260920T0413Z_r17_edge_path_coupling_5e2b.md`.

That report proved the exact single-defect substochastic chain `Q_m`, a Hamming-path coupling theorem, and the block-survival finite-horizon error. It also records the old R17 C033--C035 complement-gauge failure and terminal C050 handoff; none of those failed claims is revived.

Current ownership is complementary. `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`) assigns P02 the stationary/covering/cone route and P13 the dependence-preserving boundary/reset route. R17 stays on the history-coupled finite-state discrepancy route and does not overwrite either companion.

The newest complete same-source P02 report recovered is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T05-13-00Z__coefficient-weighted-two-step-report.md`.

It strictly improves P02's previous Farey endpoint. The exact inherited lower endpoint is
\[
L=\frac{99083249}{125000000}=0.792665992.
\]
Write `p=256717`, `q=800000`, `t=p/q`, and retain P02's exact constants
\[
S=q^6(q-p)=142418378752000000000000000000000000000000,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\qquad
m_0=p^7=73482242694633120311956186136958404773.
\]
P02 defines
\[
\beta_W=\frac ab-\frac{m_0}{2ab},
\qquad
\lambda_W=\frac{t^2}{S}\beta_W,
\qquad
U_W=\frac{\log(4t^2)}{\log\lambda_W}.
\]
Its exact positive-series certificate proves `gamma_2 <= U_W`; its diagnostic decimal is
\[
U_W=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564491109755\ldots.
\]
Therefore the source-level width before and after this R17 run is exactly
\[
\boxed{W_{\rm before}=W_{\rm after}=U_W-L},
\]
with diagnostic beginning
\[
0.033609950762282625015106581537296632823461996193190023880806183312562944430299564491109755\ldots.
\]
The strict move to `U_W` belongs to P02 and occurred before this run; it is not claimed as R17 movement.

Fresh bounded literature checking on 20 September 2026 still finds the exact binary coefficient unresolved. Tiskin `https://arxiv.org/abs/2212.01582v2` explicitly removed the erroneous claims from the earlier version and still describes the problem as unresolved. Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer `https://arxiv.org/abs/2407.10925` give the public rigorous lower endpoint above. Li--Ren--Wen, DOI `10.1017/S000497272610104X`, published online in 2026, still present determination of the two-string binary constant as open. Lueker's public upper bound remains `0.826280`. The stronger `U_W` is repository-internal and has not been promoted to independent/public certification here. A bounded negative search is status evidence, not a novelty certificate.

## 1. Idea before code and three attacks

The idea was committed before checker code at

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0520Z_r17_secondclass_weighted_dual_idea.md`

(commit `6b4a8e865fc2fbfcb2d4ed8c4875d690cdf74cf2`).

The three attacks are:

1. derive an exact second-class/carrier transition law and an absolute-position monovariant;
2. replace the previous scalar `T`-block contraction by an environment-weighted one-step Collatz vector `h_T=Q_m^T 1`;
3. test the tempting deterministic claim that the monovariant forces a boundary encounter in bounded time. It is false, and an exact self-loop records the obstruction.

## 2. Exact correlated strip and the inherited single-defect chain

Fix strip length `m=2w`. A formal state is
\[
S=(x;g),\qquad x,g\in\{0,1\}^m.
\]
For a fresh true source pair `(u,v)`, set
\[
d_0=0,
\qquad
d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\quad 1\le i\le m,
\tag{2.1}
\]
then
\[
x'=(x_2,\ldots,x_m,u),
\tag{2.2}
\]
\[
g'_i=g_{i+1}+d_{i+1}-d_i\quad(1\le i<m),
\qquad
g'_m=(1-d_m){\bf1}_{\{u=v\}}.
\tag{2.3}
\]
The same `v` appears at every site in (2.1); this is the genuine dependent match array.

An edge state `e=(x,g,j)` means that the lower front is `g`, `g_j=0`, and the upper front is `h=g+e_j`. The preceding R17 report proved that a common source update either absorbs the discrepancy or leaves exactly one discrepancy. Thus nonabsorbed edges form a finite substochastic chain `Q_m` with
\[
|E_m|=m2^{2m-1}.
\tag{2.4}
\]

## 3. New structural theorem: exact second-class transition law

Use one-based coordinates. Let `d^g,d^h` be the two carrier streams. They agree through coordinate `j-1`. Define
\[
A_v:=d^g_{j-1}\vee {\bf1}_{\{x_j=v\}}.
\tag{3.1}
\]
Since `g_j=0` and `h_j=1`,
\[
d^g_j=A_v,\qquad d^h_j=0.
\tag{3.2}
\]

### Theorem 3.1 — local defect motion

For one common update `(u,v)`:

* If `A_v=0` and `j>1`, the unique defect moves to coordinate `j-1`. If `A_v=0` and `j=1`, it is absorbed at the left boundary.
* If `A_v=1`, let `k>j` be the first index, if any, satisfying
  \[
  g_k=1\quad\text{or}\quad x_k=v.
  \tag{3.3}
  \]
  If such `k` exists, the unique defect moves to coordinate `k-1`.
* If `A_v=1` and no such `k<=m` exists, then the discrepancy reaches the right boundary. It is absorbed when `u\ne v` and survives at coordinate `m` when `u=v`.

Consequently, if a defect alive at source time `t` has relative coordinate `j_t`, then
\[
\boxed{Z_t:=t+j_t}
\tag{3.4}
\]
is nondecreasing for as long as the defect survives.

### Proof

Before `j`, the two carrier streams are identical. If `A_v=0`, (3.2) says they remain identical at `j`; the only difference in (2.3) comes from the front bit `h_j-g_j=1`, which appears one coordinate to the left after the shift. At `j=1` there is no such output coordinate and the left flux absorbs the defect.

If `A_v=1`, then immediately after `j` one has `d^g=1` and `d^h=0`. As long as a later site has both `g_i=0` and `x_i\ne v`, the lower carrier stays one and the upper carrier stays zero, so the carrier discrepancy persists and no front discrepancy is emitted. At the first site `k` with `g_k=1`, both carriers reset to zero; at the first site with `g_k=0,x_k=v`, the upper carrier catches the lower carrier at one. In either case the carrier discrepancy terminates exactly at `k`, and the telescoping term `d_{k}^h-d_k^g-(d_{k-1}^h-d_{k-1}^g)` in (2.3) emits the unique front discrepancy at `k-1`.

If no such site exists, the carrier discrepancy reaches `m`: `d_m^g=1,d_m^h=0`. Equation (2.3) then gives last-coordinate discrepancy `1` exactly when `u=v`; when `u\ne v` both last bits are zero and absorption occurs.

In every nonabsorbed case the next coordinate obeys `j_{t+1}>=j_t-1`. Hence
\[
Z_{t+1}=(t+1)+j_{t+1}\ge t+j_t=Z_t,
\]
proving (3.4). QED.

This is a useful change of language: the disagreement is a second-class particle whose absolute space-time location never moves left, while its relative coordinate can move left because the observation window itself shifts.

## 4. New exact weighted Collatz/Bellman dual

Let
\[
h_T:=Q_m^T\mathbf1,
\qquad
\alpha_T:=\|h_T\|_\infty,
\tag{4.1}
\]
and define
\[
\lambda_T:=
\max_{e:h_T(e)>0}
\frac{(Q_mh_T)(e)}{h_T(e)}.
\tag{4.2}
\]
If `h_T(e)=0`, then survival for `T` steps is impossible from `e`, hence also for `T+1`, so `(Q_mh_T)(e)=0`. Thus (4.2) gives the componentwise exact dual
\[
\boxed{Q_mh_T\le\lambda_T h_T.}
\tag{4.3}
\]
By positivity,
\[
Q_m^k h_T\le\lambda_T^k h_T,
\]
and therefore
\[
\boxed{Q_m^{T+k}\mathbf1\le\lambda_T^k h_T
\le \alpha_T\lambda_T^k\mathbf1.}
\tag{4.4}
\]
This is stronger than forgetting the environment after each `T`-block: after one burn-in it retains the exact survival profile as a positive Bellman/Collatz potential.

### Theorem 4.1 — refined finite-horizon/stationary error

Assume `lambda_T<1` and `m alpha_T<1`. For the width-`w` strip reward `R_N` and every initial formal state `s`,
\[
\boxed{
\left|\mathbf E_sR_N-N\gamma_w\right|
\le
C_m^{\rm wt}(T)
:=m+T+\frac{m\alpha_T}{1-\lambda_T}.
}
\tag{4.5}
\]
Consequently
\[
\boxed{
\frac{\mathbf E_sR_N-C_m^{\rm wt}(T)}N
\le \gamma_w\le
\frac{\mathbf E_sR_N+C_m^{\rm wt}(T)}N.
}
\tag{4.6}
\]

### Proof

Couple an arbitrary chain to a stationary copy using the same future source pairs. After `m` shifts their raw `x` windows agree exactly. Connect their two gradient fronts by a Hamming path of at most `m` ordered single-defect edges. For each initial edge, (4.4) bounds survival after `T+k` further source updates by `alpha_T lambda_T^k`. If all path edges have coalesced, the endpoints agree, so the union bound gives
\[
\Pr\{\tau>m+T+k\}
\le m\alpha_T\lambda_T^k.
\tag{4.7}
\]
The hypothesis `m alpha_T<1` removes any additional cap at one after the burn-in. Summing the coupling tail gives
\[
\mathbf E\tau
\le m+T+\sum_{k\ge0}m\alpha_T\lambda_T^k
=m+T+\frac{m\alpha_T}{1-\lambda_T}.
\tag{4.8}
\]
One-step strip rewards lie in `{0,1}` and agree after coalescence, so the expected cumulative reward discrepancy is at most `E tau`. The stationary copy has mean reward `N gamma_w`, proving (4.5) and (4.6). QED.

## 5. Exact finite computation: `C_8 < 43`

The checker evaluates the true correlated edge automaton exactly through `m=8`, with `T=4m`. It verifies Theorem 3.1's transition classification on every formal edge/input pair, computes integer survival-word counts for `h_T`, and forms the exact rational Collatz ratio (4.2).

For `m=8` (`w=4`) it obtains
\[
\alpha_{8}(32)
=
\frac{666247718450140937}{18446744073709551616}
\approx0.036117361187857674,
\tag{5.1}
\]
\[
\lambda_{32}
=
\frac{994266288913277}{1142366470455998}
\approx0.870356680301021202,
\tag{5.2}
\]
and hence
\[
C_8^{\rm wt}(32)
=
\frac{7210464892758867815625915024962903}
{170747884136781082886635253661696}
\approx42.22872177427849
<43.
\tag{5.3}
\]

The preceding R17 scalar block certificate was only `C_8<50`. Thus the environment-weighted dual gives a strict verified mechanism improvement
\[
\boxed{C_8<50\quad\longrightarrow\quad C_8^{\rm wt}<43.}
\tag{5.4}
\]
The output also gives exact weighted constants for every `2<=m<=7`; all satisfy `lambda_T<1` and `m alpha_T<1` at `T=4m`.

This is **not** source-level interval movement. It is a sharper exact finite-to-stationary transfer for the dependence-preserving width process.

## 6. Attack C fails exactly: the monovariant does not give deterministic regeneration

The nondecreasing absolute coordinate (3.4) tempts one to assert that every live defect must encounter a killing boundary within a deterministic `O(m)` number of steps. That is false.

For every `m>=4`, take
\[
x=0^m,
\qquad g=0^m,
\qquad j=2,
\tag{6.1}
\]
and apply source input `(u,v)=(0,0)`. Since the entire raw word matches `v`, the lower carrier is one throughout. At the defect site the upper carrier is reset to zero, then immediately catches up at the next zero site. Equations (2.2)--(2.3) return exactly the same raw word, lower front, and interior defect coordinate. Thus
\[
\boxed{(0^m,0^m,2)\xrightarrow{(0,0)}(0^m,0^m,2).}
\tag{6.2}
\]
Repeated `(0,0)` inputs therefore keep the defect alive in the same interior state for arbitrarily long finite times. The event has positive probability `4^{-r}` for `r` prescribed repetitions.

Hence there is no deterministic bounded-time boundary-hit theorem and no integer rank that strictly decreases on **every** nonabsorbing source transition. The useful statement must be stochastic/environment-weighted, which is exactly what (4.3) supplies.

The checker verifies (6.2) for every `4<=m<=8` and exhaustively verifies the local motion law and `Z`-monotonicity through `m=8`.

## 7. Source-level consequence and the remaining full-scope gap

The source metric does not move. Equation (4.6) certifies the stationary width constant `gamma_w`; it does not by itself raise `L`, because no exact finite computation in this run proves `gamma_w>L`, and it does not lower `U_W`, because no valid width-to-full upper transfer is supplied here. Previous exact R17 work already showed widths `w<=5` lie below the retained lower endpoint, so improving the `w=4` error constant cannot be promoted to a new lower bound.

The durable gain is the combination of:

1. an exact second-class-particle geometry for single discrepancies;
2. an exact environment-weighted one-step Bellman dual after finite burn-in;
3. a strict finite-to-stationary improvement `C_8<50 -> C_8^{wt}<43`;
4. an exact obstruction ruling out deterministic boundary regeneration.

R17's source no-movement count is **not reset** by this auxiliary progress. The owner-required response to repeated unchanged runs is obeyed by changing method within PROB10-02 rather than rotating away: the free-boundary/suffix-control route was obstructed, then disagreement flux and scalar edge-block coupling were developed, and this run changes again to second-class geometry plus an environment-weighted dual.

The next high-value route is now precise: use Theorem 3.1 to factor `h_T` by local zero-runs/carrier stopping sites, seeking a symbolic or automaton-compressed proof of `Q_m h <= lambda h` that avoids enumerating all `m2^(2m-1)` edges. The target is a certificate scalable to `m>=12` (`w>=6`), where an exact finite-horizon computation could in principle test the lower-endpoint criterion. A mere larger enumeration without such compression is not the next method.

## 8. Exact artifacts and actual execution

Idea before code:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0520Z_r17_secondclass_weighted_dual_idea.md`

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0520Z_r17_secondclass_weighted_dual_exact.py`

creation commit `587e093c839bde6b5a17ef0f43bc667506c75b92`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0520Z_r17_secondclass_weighted_dual_exact.out`

creation commit `dbd2a6a4006c8df7accbbcfd757d49e74962f3f2`.

The checker exited with code zero and ends `ALL_EXACT_CHECKS_PASS`. The execution host separately printed an unrelated spreadsheet-runtime warmup traceback on stderr during Python startup; it did not originate in the checker and did not affect its assertions or stdout. The archived output says this explicitly rather than silently deleting the execution condition.

## 9. Honest status / ledger delta

```yaml
ledger_delta:
  track: R17
  parent: PROB10-02
  target: binary Chvatal-Sankoff gamma_2
  model: true iid binary strings; dependent match array preserved
  status_before: OPEN/PARTIAL
  status_after: OPEN/PARTIAL
  lower_before: 99083249/125000000
  lower_after: 99083249/125000000
  upper_before: U_W from P02 coefficient-weighted two-step certificate
  upper_after: U_W
  width_before: U_W - 99083249/125000000
  width_after: U_W - 99083249/125000000
  source_metric_movement: none by R17 this run
  mechanism_before: scalar block edge-chain error; m=8 certificate C_8 < 50
  mechanism_after: environment-weighted Collatz edge dual; exact C_8 < 43
  new_structural_lemma: absolute second-class coordinate Z_t=t+j_t is nondecreasing while alive
  exact_obstruction: monochromatic interior defect self-loop under (u,v)=(0,0)
  handoff_H0021: preserved; UNASSIGNED; Delta_near=2
  companion_ownership: P02 covering/cone; P13 boundary/reset; R17 discrepancy/history coupling
  closure: false
```

No schedule, cadence, enabled state, workflow, permission, email, Drive item, public posting, or peer-owned file was changed.
