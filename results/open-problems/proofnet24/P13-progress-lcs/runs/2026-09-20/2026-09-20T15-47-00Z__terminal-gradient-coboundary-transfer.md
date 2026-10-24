Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# P13 / T02 — terminal-gradient coboundary and event-specific finite-to-infinite transfer

## 0. Before / after, separated by level

### Source-level binary Chvátal–Sankoff interval

The target remains
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every strip transition below uses one actual fresh `Y` bit across the entire column; independent Bernoulli matching is not substituted.

The preceding P13 report

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T14-13-00Z__residual-transport-width6-exact-transfer.md`

carried the companion-derived source interval
\[
L\le\gamma_2\le U_{01},\qquad
L=0.792665992=\frac{99083249}{125000000}.
\]

Since that snapshot, P02 has produced two completed immutable strictifications:

1. `2026-09-20T14-15-00Z__mixed-modulus-padic-dual-report.md` proves `U_mm<U_01`, with exact logarithmic separator
\[
U_{mm}<0.82627594276228262501510658153729663282346199619319002388080618331256294443024<U_{01}.
\]
2. `2026-09-20T15-04-28Z__mixed-modulus-exact-tail-dual-report.md` proves `U_tail<U_mm`, with exact separator
\[
U_{tail}<0.8262759427622826250151065815372966328234619961931900238808061833125629444302<U_{mm}.
\]

Thus the combined P02/P13 program has strict source-level movement in this invocation:
\[
\boxed{[L,U_{01}]\quad\longrightarrow\quad[L,U_{tail}]},
\qquad U_{tail}<U_{mm}<U_{01}.
\]
This source movement is **P02-derived** and is not attributed to the new P13 strip theorem below.

Fresh source navigation rechecked Alexander Tiskin, `arXiv:2212.01582v2`: v2 was revised 2024-08-13, the binary coefficient is still stated to be unresolved, and the arXiv comments explicitly say the earlier claims concerning the stochastic process and `gamma` that turned out to be incorrect were omitted. The rigorous public lower endpoint `0.792665992` remains the Heineman–Miller–Reichman–Salls–Sarkozy–Soiffer bound `arXiv:2407.10925`.

### P13 mechanism-level movement

The previous P13 route had reached an extremely sharp optimized full-state width-six Bellman interval but was obstructed in lifting its bias through the width-seven projection/carry quotient. Rather than spend another run polishing width six or repeating the `2,706`-state projection obstruction, this run executes the preserved genuinely different **event-specific mixed-terminal route**.

The new all-width pointwise identity is
\[
\boxed{r+P\phi-\phi=1-g_m},
\qquad
\boxed{\phi=\sum_{i=w+1}^{m-1}g_i+2g_m},
\qquad m=2w.
\]
It converts the whole strip reward into a Bellman residual depending on only the **single terminal gradient bit** `g_m`.

Residual transport then gives, for every `k>=0`,
\[
\boxed{
1-\max_s P^k g_m(s)\le \gamma_w\le 1-\min_s P^k g_m(s)
}
\]
on the recurrent strip class, plus an every-horizon finite-to-infinite reward transfer with residual error
\[
\boxed{\varepsilon_k=\operatorname{span}(P^k g_m)}.
\]

At width six the exact event interval at `k=31` is
\[
I_{31}=
\left[
\frac{1767510641892353807}{2305843009213693952},
\frac{3654583955361930715}{4611686018427387904}
\right]
\]
of width
\[
\frac{119562671577223101}{4611686018427387904}
=0.025926021654439232\ldots.
\]
At `k=62` it strictly contracts to
\[
\boxed{
I_{62}=
\left[
\frac{2069975663666535705612455258205975023}
{2658455991569831745807614120560689152},
\frac{16603709141959480080665007789765041183}
{21267647932558653966460912964485513216}
\right]
}
\]
with exact width
\[
\boxed{
\varepsilon_{62}=\frac{43903832627194435765365724117240999}
{21267647932558653966460912964485513216}
=0.0020643482893085716\ldots .
}
\]
The strict width shrink factor is
\[
\boxed{
\frac{|I_{31}|}{|I_{62}|}
=
\frac{551385500838505421750331573276770304}
{43903832627194435765365724117240999}
=12.5589377474296\ldots .
}
\]
Both endpoints move inward by exact positive cross-products archived in the checker output.

This event-specific interval is deliberately **not** advertised as numerically sharper than the preceding optimized full-state width-six Bellman interval of width about `1.25e-24`; it is much coarser. Its gain is structural: it replaces a multi-million-state bias object by an exact one-bit boundary observable while retaining a proved finite-to-infinite transfer. That is the route intended to scale beyond width six.

Status: **PARTIAL / source OPEN / exact internal candidate pending later independent review and public-priority checking.**

## 1. Scope, continuity, exclusions, and handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns P13 to T02 dependence-preserving boundary recursion, complementary to P02's stationary/variational upper route.

Necessary continuity only was read: the preceding P13 report, the preceding carry-quotient report, P02's two new companion reports, the source-valid R17 terminal-gradient identity dependency, root `POSTED.md`, and the current source records. No whole-repository reread was performed. `POSTED.md` contains no T02 exclusion.

Short actual pre-LIVE20 P13 successor handoff is preserved: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation `tau(infinity)` could not be frozen source-faithfully. Retired I0051/clade work remains retired and was not reopened.

No email, Drive, public posting, paid compute, permission, workflow, schedule, peer-history, or historical-claim overwrite was performed.

## 2. Genuine dependent strip recursion

Fix half-width `w`, put `m=2w`, and write a formal strip state
\[
s=(x_1,\ldots,x_m;g_1,\ldots,g_m),\qquad x_i,g_i\in\{0,1\}.
\]
For one fresh actual source pair `(u,v)`, define the shared-column carries
\[
d_0^{(v)}=0,
\qquad
d_i^{(v)}=(1-g_i)\left(d_{i-1}^{(v)}\vee{\bf1}_{\{x_i=v\}}\right),
\quad1\le i\le m.
\tag{2.1}
\]
The same `v` occurs in every match test in the entire column. The gradient update is
\[
g'_i=g_{i+1}+d_{i+1}^{(v)}-d_i^{(v)},\qquad 1\le i<m,
\tag{2.2}
\]
\[
g'_m=(1-d_m^{(v)}){\bf1}_{\{u=v\}},
\tag{2.3}
\]
and the central reward is
\[
\rho(s;u,v)=g_{w+1}+d_{w+1}^{(v)}\in\{0,1\}.
\tag{2.4}
\]
The raw window shifts by `x'=(x_2,...,x_m,u)`.

Let `P` be the Markov kernel generated by the four equiprobable actual source pairs and let `r(s)=E[\rho|s]`.

## 3. New theorem: an integer terminal-gradient coboundary

The earlier P13 boundary calculation used
\[
h_0(s)=\sum_{i=w+1}^{m-1}g_i+\frac23g_m
\]
and proved the pointwise identity
\[
r+Ph_0-h_0
=\frac13+\frac13g_m+\frac13\left(d_m^{(0)}+d_m^{(1)}\right).
\tag{3.1}
\]

The terminal update (2.3) gives another pointwise conditional expectation:
\[
Pg_m
=\frac14\sum_{v=0}^1\sum_{u=0}^1(1-d_m^{(v)}){\bf1}_{\{u=v\}}
=\frac12-\frac14\left(d_m^{(0)}+d_m^{(1)}\right).
\tag{3.2}
\]
Hence
\[
Pg_m-g_m
=\frac12-g_m-\frac14\left(d_m^{(0)}+d_m^{(1)}\right).
\tag{3.3}
\]

### Theorem 3.1 — terminal-gradient coboundary

Define the integer-valued potential
\[
\boxed{
\phi:=h_0+\frac43g_m
=\sum_{i=w+1}^{m-1}g_i+2g_m.
}
\tag{3.4}
\]
Then on every formal state,
\[
\boxed{r+P\phi-\phi=1-g_m.}
\tag{3.5}
\]

**Proof.** Add `(4/3)` times (3.3) to (3.1). The terminal-carry coefficient becomes
\[
\frac13-\frac43\cdot\frac14=0,
\]
the `g_m` coefficient becomes `1/3-4/3=-1`, and the constant becomes `1/3+(4/3)(1/2)=1`. Thus the right side is exactly `1-g_m`. QED.

No independent match variables appear in this cancellation: both terminal carries in (3.1)--(3.3) are generated by (2.1) with the same actual column bit reused through all `m` sites.

Averaging (3.5) under stationarity immediately recovers the R17 stationary identity
\[
\boxed{\gamma_w=1-\pi_w(g_m)},
\tag{3.6}
\]
but (3.5) is strictly stronger operationally because it is a pointwise Bellman identity and can therefore be transported and telescoped at finite horizons.

## 4. Event-specific residual transport and finite-to-infinite theorem

For `k>=0` put
\[
\boxed{
\phi^{[k]}:=\phi+\sum_{j=0}^{k-1}P^j(1-g_m).
}
\tag{4.1}
\]
The same coboundary calculation used in the preceding P13 residual-transport report gives
\[
\boxed{
r+P\phi^{[k]}-\phi^{[k]}=P^k(1-g_m)=1-P^kg_m.}
\tag{4.2}
\]

Let
\[
a_k:=\min_sP^kg_m(s),\qquad
b_k:=\max_sP^kg_m(s),\qquad
\varepsilon_k:=b_k-a_k.
\]
On the finite recurrent strip class, stationarity applied to (4.2) gives the exact boundary-event interval
\[
\boxed{1-b_k\le\gamma_w\le1-a_k.}
\tag{4.3}
\]

More importantly, let
\[
A_N(s):=\frac{\mathbf E_sR_N}{N}.
\]
The standard Bellman telescoping argument applied to (4.2) gives, for every state in the recurrent class and **every** horizon `N>=1`,
\[
\boxed{
A_N(s)-\varepsilon_k-
\frac{\phi^{[k]}(s)-\min\phi^{[k]}}N
\le\gamma_w\le
A_N(s)+\varepsilon_k+
\frac{\max\phi^{[k]}-\phi^{[k]}(s)}N.
}
\tag{4.4}
\]
At a minimizer and maximizer of the transported potential,
\[
\boxed{
\gamma_w\ge A_N(s_-^{[k]})-\varepsilon_k,
\qquad
\gamma_w\le A_N(s_+^{[k]})+\varepsilon_k
}
\tag{4.5}
\]
for every `N`, with no `1/N` boundary loss on the corresponding side.

Equations (4.3)--(4.5) are the required finite-to-infinite transfer. A finite computation of `P^kg_m` or `E_sR_N` is not by itself promoted to a statement about `gamma_w` or `gamma_2`; the Bellman identity (4.2) is the transfer mechanism.

Because strip paths are a subset of unrestricted LCS paths,
\[
\gamma_w\le\gamma_2.
\tag{4.6}
\]
Thus any future event certificate with lower endpoint `1-b_k>L` at a wider width would give a genuine source-lower improvement.

## 5. Exact width-six event certificate

The width-six recurrent class has the inherited exact size
\[
|R_6|=5,735,086.
\]
The new checker first verifies (3.5) pointwise on **all 5,735,086 recurrent states** using exact integer arithmetic. Since `phi` is integer-valued, the checked identity is simply
\[
\sum_{a=1}^4\rho(s,a)+\sum_{a=1}^4\phi(T_as)-4\phi(s)
=4(1-g_m(s)).
\tag{5.1}
\]

It then propagates the terminal bit with exact integers
\[
F_k(s):=4^kP^kg_m(s),
\qquad
F_{k+1}(s)=\sum_{a=1}^4F_k(T_as).
\tag{5.2}
\]
No floating arithmetic enters the proof computation.

At `k=30`,
\[
4^{30}=1152921504606846976,
\]
\[
F_{30}^{\min}=237795384677590044,
\qquad
F_{30}^{\max}=270210112419958892.
\]
The exact source-threshold cross product is negative:
\[
125000000F_{30}^{\min}-25916751\,4^{30}
=-155556472742250472094976<0.
\tag{5.3}
\]
So this event certificate does not yet prove `gamma_6<L` at `k=30`.

At `k=31`,
\[
4^{31}=4611686018427387904,
\]
\[
F_{31}^{\min}=957102063065457189,
\qquad
F_{31}^{\max}=1076664734642680290,
\]
and now
\[
\boxed{
125000000F_{31}^{\min}-25916751\,4^{31}
=117839653418124736620096>0.
}
\tag{5.4}
\]
Since `1-L=25916751/125000000`, (5.4) proves directly from the one-bit boundary event that
\[
\boxed{\gamma_6<L.}
\tag{5.5}
\]
Equivalently the exact event upper endpoint is
\[
\gamma_6\le
\frac{3654583955361930715}{4611686018427387904}
=0.7924615727868146\ldots<L,
\]
with exact positive gap
\[
L-\frac{3654583955361930715}{4611686018427387904}
=
\frac{1841244584658199009689}{9007199254740992000000000}>0.
\tag{5.6}
\]

At `k=62`, exact 128-bit propagation gives
\[
4^{62}=21267647932558653966460912964485513216,
\]
\[
F_{62}^{\min}=4663938790599173885795905174720472033,
\]
\[
F_{62}^{\max}=4707842623226368321561270898837713032.
\]
Therefore the exact interval `I_62` displayed in section 0 follows from (4.3). The executed output also records two positive cross-products proving
\[
\boxed{I_{62}\subsetneq I_{31}}
\tag{5.7}
\]
with both endpoints strictly inward, not merely a smaller floating display.

The checker terminates `ALL_EXACT_CHECKS_PASS`.

## 6. What this gains, and what it does not

This run has two distinct gains.

First, the general strip recursion now has a particularly simple exact Bellman representative: the central LCS reward is cohomologous to `1-g_m`. That reduces the asymptotic strip problem to a one-bit terminal observable **pointwise**, not only after stationarity. The resulting event residual can be transported with the same exact shared-source kernel and supplies the finite-to-infinite inequalities (4.3)--(4.5).

Second, the event-only certified width-six interval shrinks strictly by a factor `12.5589377474...` between `k=31` and `k=62`, and already at `k=31` proves `gamma_6<L` without the previously optimized multi-million-dimensional bias potential.

The limitation is important: this does **not** improve the best numerical width-six interval. The preceding optimized Bellman certificate is vastly narrower, and width six itself is below the source lower endpoint. Hence P13 does not claim source-level lower movement from this computation. The source interval movement in section 0 comes from P02's complementary upper route.

The reason to keep the event theorem is scalability: to improve the source lower endpoint at a wider strip, it is enough to certify
\[
\boxed{\max_sP^kg_m(s)<1-L=0.207334008}
\tag{6.1}
\]
for one `w,k`, rather than reconstructing a globally accurate bias for every state.

## 7. Failure accounting and next attack

The earlier raw width-seven projection lift remains obstructed by `64,202` outsider projections and a `2,706`-state persistent core. The exact carry quotient repairs the Markov information loss but still has `56,219,024` reachable contexts. The preceding P13 report therefore stated that another nonlocal carry correction should trigger the preserved event-specific recovery route. This run executes that different route rather than repeating the same lift.

The event route succeeds mathematically at width six but does not move the source lower endpoint because `gamma_6<L`. It also does not magically solve the width-seven state count if one naively propagates `P^kg_m` on every state. That is the remaining obstruction.

**Next attack:** minimize the deterministic source automaton with output `g_m` rather than the whole strip state. Start from the exact carry-core quotient and perform output-preserving Moore refinement: two contexts are equivalent when they have the same terminal-gradient output and, under each of the four actual source pairs, transition to equivalent contexts. This quotient preserves every future word trace of `g_m`, hence preserves `P^kg_m` for all `k` exactly. The goal is to compute the maximal event probability in (6.1) for wider widths without a full Bellman bias. If exact output-bisimulation remains essentially as large as the carry quotient, switch immediately to the spatial finite-range separator for the terminal-event residual rather than returning to the failed raw projection/bias lift.

This next attack is source-relevant: a successful `1-b_k>L` certificate at any wider width gives `gamma_2>=gamma_w>L` by (4.6).

## 8. Essential executed artifacts

1. Exact terminal-gradient/coboundary checker source:
   `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T15-36-00Z__w6_terminal_event_transport.cpp`
   creation commit `14febad4ff75779cca75f7947f728be13e862973`.

2. Actual executed checker stdout:
   `proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T15-36-30Z__w6_terminal_event_transport.out`
   creation commit `9307a00d76a7cf8841b870a1ecb320f67e9f6d4f`.

The executable was built locally with `g++ -O3 -std=c++17`. Runtime diagnostics are not part of the proof. The archived output contains all exact `k=30,31,62` extrema, threshold cross-products, strict-nesting cross-products, interval widths, and ends `ALL_EXACT_CHECKS_PASS`.

## 9. ledger_delta

```text
ledger_delta:
  slot: P13
  target: T02 binary Chvatal-Sankoff gamma_2, iid uniform binary strings
  source_before: [L, U_01]
  source_after:  [L, U_tail]
  source_gain: P02-derived strict chain U_tail < U_mm < U_01; not attributed to P13 strip computation
  p13_method_change: switched from obstructed width-7 bias/projection lift to event-specific terminal-gradient coboundary
  new_theorem: phi=sum_{i=w+1}^{2w-1} g_i + 2 g_{2w} satisfies r+Pphi-phi=1-g_{2w} pointwise under the genuine shared-Y recursion
  finite_to_infinite: transported residual is 1-P^k g_m; interval [1-max P^k g_m, 1-min P^k g_m] and every-horizon bias-extremal reward transfer hold exactly
  width6_event_interval_k31: [1767510641892353807/2305843009213693952, 3654583955361930715/4611686018427387904]
  width6_event_interval_k62: [2069975663666535705612455258205975023/2658455991569831745807614120560689152, 16603709141959480080665007789765041183/21267647932558653966460912964485513216]
  width6_event_width_k62: 43903832627194435765365724117240999/21267647932558653966460912964485513216
  event_width_gain_k31_to_k62: 12.5589377474296... strict nested factor
  exact_threshold: k30 does not certify gamma6<L; k31 does, by positive cross-product 117839653418124736620096
  dependence_check: same incoming Y bit v reused through entire strip column; no independent Bernoulli matching
  honest_limit: event interval is coarser than prior optimized width6 Bellman interval and does not move source lower endpoint
  obstruction: wider-width exact event propagation still risks state explosion; raw projection has 2706 persistent outsiders
  next_attack: exact output-bisimulation/Moore quotient for terminal-gradient traces on carry-core contexts; if large, spatial finite-range event separator
  handoff: P0342 frozen terminal 2/2; P0205 admitted no successor due source tau(infinity) ambiguity; retired clade work untouched
  status: PARTIAL / source OPEN / full candidates pending later independent review
```
