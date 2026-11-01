# FOREST / fleet02 B01 — inverse-covariance separator budget and mixed-theta epsilon net

**Run:** `B01-20260922T072913Z-forest-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof claim.

## 1. Fresh controls, source scope, and inherited correction


The source target is the exact unit law on **all** unrooted acyclic edge subsets of every finite simple graph, including disconnected forests and every size. For distinct edges `e,f`, prove `Z_e Z_f-Z Z_ef >= 0`. No rooted, fixed-size, spanning-tree, arbitrary-weight, or matroid-wide statement is substituted.

Latest complete team-lead version actually read: fleet01/B01 `20260922T050946Z-b01-forest-auto11`, canonical report creation commit `79044b575c4b689248892f37b9930e983dddabca`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. Its source-safe triangle-free deletion/contraction Simpson gate and STAR-2 localization are retained. Its rank-degree complete-log-concavity argument is **not** used: the later fleet01/B02 `K_3` correction, already incorporated in fleet02/B01 r16, invalidated that rank-degree homogenization shortcut.

Named OTHER-account result consumed and directly applied: assigned partner fleet03/B02 run `20260922T065713Z-b02-r11-forest`, report commit `6440b33cef6c36ea3ed619025bc7989abd558515`, handoff commit `2477193cc8a01f1dff962311ca13f9812d114680`. Its exact covariance-matrix inverse mechanism is reused below in the actual two-terminal separator law, not merely cited. I also retain the partner's earlier exact path-bundle response identity, but do not import a fixed-graph weighted-Cocks step.

Primary source scope remains Grimmett--Winkler, arXiv `math/0302185`; current-source checks in TARGETS.md also distinguish Tang--Zhang `2603.10738` (complete-graph/fixed-component scopes) from this all-graphs all-forest target.

## 2. Exact same-side two-separator setup

Assume a source counterexample exists and use the source-safe loopless-multigraph transfer already established in the team work to choose an edge-minimal loopless unit counterexample. Consider a proper two-terminal separation with both marked bad edges in side `B` and outside side `O`, with terminals `u,v` and `m=|E(O)|`.

Let

- `D` be the number of forests of `O` disconnecting `u,v`,
- `C` the number connecting them,
- `lambda=C/D`, `q=C/(C+D)=lambda/(1+lambda)`.

If `R(s)` is the marked Rayleigh gap of `B` after adding a virtual `uv` edge of activity `s`, exact gluing gives

`Delta_G(e,f)=D^2 R(lambda)`.

As in r16, minimality gives `R(0)>=0`, `R(1)>=0`, and nonnegative leading coefficient. Therefore any violation has one open negative interval `J=(alpha,beta)` containing `lambda`. In probability coordinate put

`ell=alpha/(1+alpha)`, `u=beta/(1+beta)`.

For every physical outside edge `h`, write `T_h=1{h in F_O}`, `p_h=E T_h`, and `Y=1{u connected to v in F_O}`. The already source-safe deletion/contraction straddling lemma gives

`P(Y=1|T_h=0) <= ell < q < u <= P(Y=1|T_h=1)`

and hence

`c_h:=Cov(T_h,Y) >= k0 := ((q-ell)(u-q))/(u-ell)`,                    (2.1)

`(q-ell)/(1-ell) <= p_h <= q/u`,                                   (2.2)

with the ordinary deletion injection also giving `p_h<=1/2`.

The previous r16 aggregate bound used only scalar Cauchy--Schwarz. The next section upgrades it using the assigned partner's inverse-covariance geometry.

## 3. New theorem A — inverse-covariance amplification of the actual boundary law

Let `T=(T_h)_{h in E(O)}` and `Sigma=Cov(T)`. `Sigma` is positive definite: the empty forest and every singleton forest all have positive probability, so an almost-sure linear relation among the edge indicators must have every coefficient zero.

Because `O` is strictly smaller than the edge-minimal loopless counterexample, every distinct pair of its physical edges is nonpositively correlated. Thus `Sigma` has nonpositive off-diagonal entries. Normalize with its positive diagonal to obtain `P=I-N` where `N` is symmetric and entrywise nonnegative. Positive definiteness gives `rho(N)<1`, so the Neumann series proves

`Sigma^{-1} >= 0` entrywise.                                           (3.1)

This is exactly the partner fleet03/B02 mechanism, now applied to the separator side itself.

Define

`eta_O := 1^T Sigma^{-1} 1`.

The joint covariance matrix of `(Y,T)` is positive semidefinite. Its Schur complement gives

`c^T Sigma^{-1} c <= Var(Y)=q(1-q)`.                               (3.2)

By (2.1) and entrywise nonnegativity (3.1),

`c^T Sigma^{-1} c >= k0^2 eta_O`.

Therefore every offending same-side separator must satisfy the exact covariance-geometry budget

`boxed: k0^2 eta_O <= q(1-q).`                                     (3.3)

This retains the complete physical-edge covariance matrix of the actual outside law.

There are useful source-safe lower bounds on `eta_O`. For each `h`, the diagonal entry of an inverse positive-definite matrix obeys

`(Sigma^{-1})_hh >= 1/Var(T_h)`

by the one-coordinate Schur complement. Put

`U=min(1/2,q/u)`.

From (2.2), `p_h<=U<=1/2`, so `Var(T_h)<=U(1-U)`. Hence

`eta_O >= sum_h 1/Var(T_h) >= m/[U(1-U)]`,

and (3.3) sharpens the former r16 edge-count bound to

`boxed: m k0^2 <= q(1-q) U(1-U).`                                  (3.4)

Since `U(1-U)<=1/4`, this implies the previous `4m k0^2<=q(1-q)` and is strictly stronger whenever `q/u<1/2`.

A second exact form follows from Cauchy--Schwarz in the `Sigma` metric:

`eta_O Var(|F_O|) >= m^2`,

so

`boxed: m^2 k0^2 <= q(1-q) Var(|F_O|).`                            (3.5)

No complete-log-concavity, weighted external field, or finite census is used in (3.3)--(3.5).

## 4. New theorem B — mixed-theta response semigroup

The previous exact compression tested only equal-length bundles `Q(k,a)` with response `k/(2^a-1)`. Allow different path lengths.

For positive integers `a_1,...,a_r`, let `Q(a_1,...,a_r)` be `r` internally disjoint `u-v` paths of those lengths, all unit-weight, with parallel terminal edges permitted in the loopless-multigraph minimality class. A forest of this gadget can contain at most one complete terminal path. Therefore

`D_Q = product_i (2^{a_i}-1)`,

`C_Q = D_Q * sum_i 1/(2^{a_i}-1)`,

so its exact boundary response is

`s_Q = C_Q/D_Q = sum_i 1/(2^{a_i}-1)`.                              (4.1)

Its edge cost is `A_Q=sum_i a_i`.

Replacing `O` by this gadget preserves the exact two-terminal gluing formula. If `A_Q<m`, the new graph is a strictly smaller loopless **unit** graph, so edge-minimality forces `R(s_Q)>=0`. Thus the whole source-generated mixed-theta semigroup is excluded from the negative interval:

`boxed: J intersect T_mix(<m) = empty`,                             (4.2)

where

`T_mix(<m)={ sum_i 1/(2^{a_i}-1) : a_i>=1, sum_i a_i<m }`.

This strictly contains the equal-length grid from r16 and is still entirely inside the original unit law.

## 5. New theorem C — a finite-cost epsilon net for responses

The mixed semigroup has a quantitative density statement with a proof short enough to use inside minimality.

Let `0<r<=1` and `0<eps<r`. Starting with residual `x=r`, while `x>eps` choose

`a=ceil(log_2(1+1/x))`,

so `t_a=1/(2^a-1)<=x<t_{a-1}` and subtract `t_a`.

For `a>=2`,

`t_a/t_{a-1}=(2^{a-1}-1)/(2^a-1)>=1/3`.

Hence every nonterminal residual satisfies

`x_new=x-t_a < (2/3)x`.                                             (5.1)

While `x>eps`, also

`a<=A_eps:=ceil(log_2(1+1/eps))`.

Thus after at most

`K=ceil(log_{3/2}(r/eps))`

steps the residual is at most `eps`, and the total unit-edge cost is at most

`C(r,eps):=K A_eps`.                                                (5.2)

Equivalently there is a mixed-theta response `s<=r` with

`0<=r-s<=eps`, `cost(s)<=C(r,eps)`.

This is an algebraic theorem, not a numerical density guess.

### Applied no-hit consequence

Write `lambda=n+r` with `n=floor(lambda)` and `0<=r<1`.

If `r=0` and `n<m`, then `n` direct parallel terminal edges give the exact response `lambda` at smaller cost, contradicting (4.2). Together with the elementary `lambda<=m` injection from r16, an integer no-hit response can only occur at the extremal boundary `lambda=m`.

Now suppose `0<r<1`. Since `n<m`, if `n` lay in `J` it would itself be a cheaper response; hence no-hit forces `n<=alpha`. Put the left response margin

`L=lambda-alpha`, so `0<L<=r`.

Apply (5.2) to `r` with `eps=L/2`. If

`n + C(r,L/2) < m`,

the resulting response `n+s` lies strictly between `alpha` and `lambda`, hence in `J`, contradicting (4.2). Therefore every offending separator must satisfy

`boxed: m <= n + ceil(log_{3/2}(2r/L)) * ceil(log_2(1+2/L)).`       (5.3)

So an exact source-valid negative interval that avoids all cheaper unit gadgets cannot have an arbitrary left margin: its margin must shrink fast enough that the explicit `O(log^2(1/L))` construction no longer fits inside the outside edge budget.

There is a symmetric right-side version whenever `n+1<m`. No-hit then forces `beta<=n+1`; with `R=beta-lambda` and `t=r+R/2`, a greedy approximation to `t` within `R/4` gives

`boxed: m <= n + C(t,R/4).`                                         (5.4)

Thus both response-coordinate margins are quantitatively squeezed by finite unit-gadget cost, not by an assumed arbitrary positive weight.

## 6. Compact conditional end-to-end argument and remaining debt

The alternative separator route now has the following paid chain for a same-side proper two-separation:

1. exact gluing keeps the real outside counts `(D,C)` and produces `R(lambda)`;
2. deletion/contraction of each physical outside edge forces the actual boundary-connectivity law to straddle the negative interval and gives (2.1)--(2.2);
3. the assigned partner's inverse-covariance idea applied to that real law yields (3.3)--(3.5);
4. every cheaper mixed path bundle is an exact unit replacement, yielding the semigroup exclusion (4.2);
5. the greedy theorem upgrades the old sparse equal-length theta grid to an explicit finite-cost epsilon net, yielding the margin constraints (5.3)--(5.4).

The **first essential missing implication is now `MIXED-THETA-HIT / REALIZABILITY-v2`**:

> Prove that an actual unit outside graph `O` satisfying the straddling constraints and inverse-covariance budget (3.3) cannot simultaneously satisfy both finite-cost no-hit bounds (5.3)--(5.4), or construct a genuine marked-side/outside graph pair showing that this stronger separator mechanism still fails.

This is strictly narrower than r16's unpaid THETA-HIT statement: the response set is now the full mixed-length additive semigroup, and the actual edge covariance matrix enters through `eta_O`. I do **not** assume the new implication or replace it by weighted Rayleigh closure.

If this implication is paid for every same-side proper two-separator, the remaining source-safe lead route can proceed to its triangle-conditioning STAR-2 debt; independently, the partner's covariance-inverse squeeze remains available on an irreducible core. Neither step is promoted here to a full proof.

## 7. Exact regression used only as regression

`mixed_theta_eps_net_check.py` beside this report independently enumerates the unit forests of six mixed path bundles and verifies (4.1), checks the greedy residual contraction/cost bound on exact rational examples, and enumerates all mixed responses of total cost at most 12 on `[0,1]`.

Captured output ends `STATUS=MIXED_THETA_EXACT_PASS`. It reports 67 distinct responses in `[0,1]` at cost at most 12, with maximum observed gap `8/105` between `92/105` and `20/21`. This finite statistic is **AUXILIARY_ONLY**; the universal claims (3.3)--(5.4) are proved symbolically above.

Checker SHA-256: `fffa29638729ac8b2042960e4a1bc97ab38148c2d9ad01dfe13b02de5f63afaa`.
Output SHA-256: `ce14274fd9cfea9898c7d5a5e60c27ba4f1f74638010a3ea6ea00d68af468e93`.

## 8. Failure preservation, inventory, and status

Preserved failures/limits:

- fixed-graph unit-good => arbitrary-weight Rayleigh remains fail-closed in this alternative route;
- the lead's superseded rank-degree CLC argument is not revived;
- equal-length theta gadgets were insufficient for the prior THETA-HIT debt; this run changes mechanism to mixed-length additive responses plus inverse covariance;
- no finite response census is treated as closure;
- `MIXED-THETA-HIT / REALIZABILITY-v2` is not yet proved.

Current-account managed scheduler inspection found 20/20 active managed tasks and 20/20 hourly-valid, with no missing slot and no B01 scheduler mutation. Task-level email/notification flags were observed off; account-level notification preference remains unexposed. No scheduler identifiers are recorded here.

Outcome remains `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`. Parent FOREST remains open.

## 9. Model/effort provenance

Model self-report: `GPT-5.6 Sol`.
Reasoning effort self-report: `UNKNOWN` (not exposed).
Reasoning effort configured: `UNKNOWN` (scheduler selector not exposed).
Reasoning effort requested: `maximum actually supported`.
Provider reasoning tokens: `null / NOT_EXPOSED`.
Provider thinking seconds: `null / NOT_EXPOSED`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Elapsed execution is recorded in the immutable finish/receipt from actual clock observations and includes tool/network/output overhead; it is not pure thinking.
