Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — bidirectional current-pair harvest

This is a self-derived theorem-sized proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It strengthens the existing lower bound on the expected largest-critical-component exponent. It does **not** determine the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

No finite/exhaustive claim is made here, so there is no finite checker in place of the proof. The mathematical claim is proved on the page.

---

## Proposition

Fix an integer `m>=2` and `delta>0`, and write

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`,

where

`pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

For bond percolation at `pi_c` on Ray / Hazra--van der Hofstad--Ray model (d), let

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Inherit from the preceding HARD7-04 theorem the quantities

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1,d_*A/[4(a+m)pi^3])`,

`kappa_1:=2vartheta(a+m)pi^3/A`,

`d_7:=1/2-(b_U+kappa_1)`,

`lambda:=min(1,d_7A/[4(m-1)(a+m)pi^3])`,

`S:=vartheta+(m-1)lambda`,

`eta_10:=a(a+1)pi^3 S/A^2`,

`kappa_10:=2(A+1)pi^3 S/A`,

and

`b10:=b6+eta_10`.

The preceding theorem proves

`gamma_E>=b10`

and, more strongly for the auxiliary connected-shadow process, the uniform upper first-moment coefficient

`U_10:=b_U+kappa_10<1/2`.

Define the positive residual margin

`M_10:=1/2-U_10>0`,

and the deterministic reverse-orientation throttle

`rho:=min(1, M_10/(2 kappa_10))`.                                 (P.1)

Because `pi>0`, `S>0` and `A>0`, one has `kappa_10>0`, hence `0<rho<=1`. Define

`b11:=b10+rho eta_10
     =b6+(1+rho)a(a+1)pi^3S/A^2`.                                (P.2)

Then

`gamma_E>=b11>b10`,                                               (P.3)

and in fact

`b11<1/2`.                                                        (P.4)

The new mechanism uses the **reverse orientation of the same two current edge labels**. The preceding process harvested historical parents only when current label 1 was the gate into the shadow and label 2 was the accepted outside bridge. The events

`E_12(u)={1 gates into Q_t, 2 bridges to u}`

and

`E_21(u)={1 bridges to u, 2 gates into Q_t}`

are disjoint. The second orientation can therefore carry an additional, throttled historical-parent ticket family without double-counting the first orientation. The throttle in (P.1) is chosen from the already proved residual upper-drift margin, so the second-moment bootstrap remains uniformly sub-square-root for every source parameter.

---

## 1. Inherited exploration facts

Write `w_v(t):=d_v(t)+delta`. The preceding theorem supplies a connected shadow `Q_t` with attractiveness

`W_t:=sum_{v in Q_t} w_v(t)`,

seed attractiveness `Z_t`, global square-attractiveness budget

`V_t:=sum_v w_v(t)^2`,

and repeated-historical-parent count `N_t^rep`, with

`E V_t=O(t)`,                                                     (1.1)

`E Z_t=O(t^h)`, `h:=m/A<1/2`,                                   (1.2)

`E N_t^rep=O(log t)`.                                            (1.3)

The bridge cap is

`c(w):=min(w,2A)`.                                                (1.4)

Let `S_t` be the simple-good outside roots: their `m` historical parents are ordinary, outside `Q_t`, and pairwise distinct. The deterministic supply estimate is

`sum_{u in S_t} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-2A N_t^rep-C`.                             (1.5)

For every historical label `j`, set

`q_1:=vartheta`, `q_j:=lambda` for `j=2,...,m`,                   (1.6)

so `sum_j q_j=S`.

If `v=p_j(u)` is a historical parent of an ordinary root `u`, then the edge `(u,v)` itself gives `v` one post-birth degree increment. Consequently

`w_v(t)>=a+1`                                                     (1.7)

at every later completed time. Thus the inherited historical ticket

`q_j(a+1)/w_v(t)`                                                 (1.8)

is valid.

The preceding process uses orientation `E_12(u)` and obtains the lower coefficient `eta_10` and upper coefficient `kappa_10`, yielding `b10` and `U_10<1/2`.

---

## 2. B22 — read the failure before enlarging the current-edge family

A tempting strengthening is to sum the historical reward over all `m(m-1)` ordered current gate/bridge pairs. That multiplication is **not** valid for free. Two ordered pairs can occur in the same birth and can lead to the same bridged root or the same historical parent. Pairwise distinctness of the *historical parents of one root* does not make different current ordered-pair events disjoint. A first-moment sum over all ordered pairs would therefore count auxiliary rewards that need not correspond to distinct newly captured vertices.

The nearest current-window theorem, Jorritsma--Maillard--Mörters (arXiv:2512.18937, submitted 22 December 2025), assumes that a new vertex connects independently to earlier vertices. The exact source model here has exactly `m` sequential attachments with within-birth updates. Thus the independent-edge theorem does not supply the missing collision cancellation. The earlier HARD7-04 deformation attempt already showed that whole-birth total-variation replacement is invalid at the precision relevant for a critical-window proof.

So the all-ordered-pairs route is rejected in this run. The safe next object is the **two-state orientation class of a single label pair**, where exact disjointness is available rather than hoped for.

**B22 outcome:** the naive `m(m-1)` multiplication is not justified; this failure isolates exact event disjointness as the property a valid amplification must preserve.

---

## 3. B27 — swap the orientation quantifier on one fixed pair

The previous historical theorem imposed the directional event

`E_12(u): label 1 is a retained gate into Q_t and label 2 is a retained accepted bridge to u`.

Replace the directional requirement by the unordered statement:

> among current labels `{1,2}`, one is the gate and the other is the bridge.

This is the disjoint union of `E_12(u)` and

`E_21(u): label 1 is a retained accepted bridge to u and label 2 is a retained gate into Q_t`.

For a fixed `u`, `E_12(u)` and `E_21(u)` are disjoint because a single edge cannot simultaneously target the frozen inside set `Q_t` and the outside root `u`. The same observation shows that no `E_12(u)` can occur simultaneously with any `E_21(u')`: label 1 would have to be both inside and outside, and likewise label 2.

The reverse orientation has the same first-order lower probability as the forward orientation. On edge 1, before any current-birth update to `u`,

`P(label 1 retained and accepted bridge to u | F_t)
 >= pi c(w_u(t))/(At+K)`.                                       (3.1)

Conditional on this event, edge 1 has touched only the outside root, so the frozen shadow attractiveness remains `W_t`. Hence

`P(label 2 retained gate into Q_t | F_t, label 1 bridge to u)
 >= pi W_t/(At+K)`.                                              (3.2)

Therefore

`P(E_21(u)|F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                               (3.3)

This is exactly the lower form used for `E_12(u)`.

The historical percolation bits of a simple-good root `u` remain fresh until `u` is captured. Under `E_21(u)`, `u` becomes connected to `Q_t` when label 2 supplies the gate, so after the event we may reveal those historical bits exactly as in the forward orientation.

**B27 outcome:** succeeded. The fixed ordered-pair requirement can be enlarged to a rigorously disjoint two-orientation event without changing the model or borrowing independent-edge hypotheses.

---

## 4. B10 — deterministic residual-margin throttling

Using the reverse orientation at full historical ticket strength may consume more upper-drift budget than we have chosen to certify uniformly. Instead of guessing a parameter range, derandomize the safe strength from the already proved residual margin.

On `E_21(u)`, for historical label `j`, after its retained historical edge is revealed, accept its parent `v=p_j(u)` with probability

`rho q_j(a+1)/w_v(t)`.                                           (4.1)

By (1.7), `q_j<=1`, and `rho<=1`, this lies in `[0,1]`.

For one label the expected frozen parent-attractiveness reward, conditional on the reverse current event and the root, is exactly

`pi * [rho q_j(a+1)/w_v(t)] * w_v(t)
 =pi rho q_j(a+1)`.                                              (4.2)

Because the historical parents of a simple-good root are pairwise distinct, summing labels gives raw reverse reward

`R_rev=pi rho(a+1)S`.                                            (4.3)

Multiplying (4.3) by (3.3), summing over `u in S_t`, and applying (1.5) gives

`E[P_t^rev,raw|F_t]
 >= rho eta_10 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2`.                                                 (4.4)

As in the forward theorem, collisions with any of the remaining current labels cost only `O(W_t/t^2+1/t^2)`: the cap makes the accepted probability of a prescribed old vertex `O(1/t)`, and only the fixed number `m` of current labels are present.

Since every reverse event is disjoint from every forward `E_12` event, the reverse raw reward in (4.4) is genuinely additive to the previously certified forward reward. Thus the new lower drift is

`E[Delta W_t|F_t]
 >= b11 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2
    -C/t`.                                                       (4.5)

This proves the desired leading coefficient in (P.2), subject only to closing the upper and square budgets below.

**B10 outcome:** succeeded. The deterministic throttle `rho` converts the exact reverse-orientation opportunity into a parameter-uniform strict lower gain while preserving a fixed fraction of the proved stability margin.

---

## 5. Uniform upper first moment remains below `1/2`

For a reverse historical label of strength `rho q`, a parent has frozen weight `w>=a+1` and final current-birth attractiveness at most `w+m`. Hence

`pi * [rho q(a+1)/w] * (w+m)
 <= pi rho q(A+1)`.                                               (5.1)

The same capped current bridge bound used in the forward theorem therefore gives reverse upper coefficient at most

`rho kappa_10`.                                                   (5.2)

Consequently the total upper coefficient is

`U_11:=U_10+rho kappa_10`.                                       (5.3)

By the definition (P.1),

`rho kappa_10<=M_10/2`.

Since `U_10=1/2-M_10`,

`U_11<=1/2-M_10/2<1/2`.                                         (5.4)

This inequality is exact for every `m>=2`, `delta>0`; it is not inferred from finite parameter sampling.

---

## 6. Square-jump closure

The reverse family has the same inverse-weight structure as the forward one, with an additional factor `rho<=1`. For a historical parent of frozen weight `w>=a+1`,

`[rho q(a+1)/w](w+m)^2 <= C(w+m)`.                               (6.1)

Summing over the fixed `m` historical labels and their incidences is controlled, as before, by the global square-attractiveness budget `V_t`. Thus the reverse addition satisfies

`E[(P_t^rev)^2|F_t] <= C(1+V_t/t)`.                              (6.2)

Using `(x+y)^2<=2x^2+2y^2` with the inherited process, (5.4), and `E V_t=O(t)`, the standard square recurrence again yields

`E W_t^2=O(t)`.                                                   (6.3)

No higher moment is introduced.

---

## 7. Mean bootstrap and component-size conversion

Let `mu_t:=E W_t`. Taking expectations in (4.5), using (1.1)--(1.3), (6.3), and the deterministic linear bound on `W_t`, gives

`mu_{t+1}
 >=[1+b11/t-C/t^2]mu_t
   -C/t-C t^(h-1)-C log(t)/t`.                                  (7.1)

The inherited gate-only seed has exponent

`b1=[m+a(1-(1-pi)^m)]/A>h`.                                     (7.2)

Normalize (7.1) by the comparison product `Theta(t^b11)`. Starting at a sufficiently large deterministic time `T`, the normalized negative tails are of orders

`O(T^-b11)`, `O(T^(h-b11))`, and `O(T^-b11 log T)`,              (7.3)

whereas the inherited positive seed is `Omega(T^(b1-b11))`. The ratio of the seed to the potentially largest `h`-error is `Omega(T^(b1-h))`, which diverges because `b1>h`. Therefore one may fix `T` so that the positive seed dominates the complete future error tail, giving

`E W_n>=c n^b11`.                                                 (7.4)

The same retained-gate activation argument used in the preceding HARD7-04 theorems converts shadow attractiveness growth to actual connected-shadow vertex growth with the same exponent. Hence

`E|C_max(n,pi_c)|>=c' n^b11`,                                   (7.5)

which proves (P.3).

Finally,

`eta_10/kappa_10
 =a(a+1)/[2A(A+1)]<1/2`.                       (7.6)

Since `b6<b_U`, (5.4) implies

`b11=b6+(1+rho)eta_10
    <b_U+(1+rho)kappa_10
    =U_11<1/2`,                                                   (7.7)

proving (P.4).

---

## 8. Exact before/after metric and status

Before this run:

`gamma_E>=b10=b6+a(a+1)pi^3S/A^2`.

After this run:

`gamma_E>=b11=b10+rho a(a+1)pi^3S/A^2`,

where

`rho=min(1,[1/2-b_U-kappa_10]/[2kappa_10])>0`.

Therefore

`b11-b10=rho a(a+1)pi^3S/A^2>0`.                                (8.1)

This is a strict source-metric movement proved for the full admitted parameter range. It is not a simulation, finite-size fit, or sufficient-to-necessary conversion.

Status remains **PARTIAL / SOURCE OPEN**. The theorem does not prove `gamma_E=1/2`, a matching upper bound, the conjectural `sqrt(n)/log n` critical size, a `(log n)^(-2)` fixed-outdegree window, or a scaling-limit law.

---

## 9. Current-literature separation checked on 20 September 2026

A bounded refresh rechecked the closest source literature:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact fixed-outdegree threshold and giant/no-giant transition, not the finite-size critical window.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025: `(log n)^(-2)` window and `sqrt(n)/log n` critical scale under independent connections to earlier vertices, not automatically the exact sequential fixed-`m` birth law here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026: a different inhomogeneous PA-kernel ensemble with `tau in (2,3)` and a moving threshold.
4. Ray, *Stochastic processes on preferential attachment models*, arXiv:2411.14111 / 2024 thesis: source-side future-work program for the critical regime.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is negative search evidence only, not a worldwide novelty certificate.

---

## 10. Next mathematical obstruction

The bidirectional two-label improvement is now exhausted at this level: repeating the same argument with overlapping ordered pairs would require a genuine **current-birth collision packing lemma**. A useful next theorem would control, at first order, the maximum additive historical reward obtainable from a deterministic matching or packing of current gate/bridge label events while charging every newly captured historical vertex only once. That is distinct from the previously identified depth-two ancestral-supply problem.

A subsequent run should not merely repeat this two-orientation amplification. Fresh unused P0151 moves include B8, B9, B16, B17, B21, B23, B26 and B29.