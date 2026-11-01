# FOREST B03 attempt report — full-radius reconnection and 3-terminal polarization gate

**Run:** `20260922T052013Z-b03-forest-r11-d011c5`  
**Slot:** fleet01/B03  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent FOREST target:** `OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Model self-report:** GPT-5.6 Sol; configured/provider reasoning telemetry `UNKNOWN_NOT_EXPOSED`.

## 1. Scope and consumed versions

Target: for every finite simple graph `G`, under the unit-weight uniform law on all acyclic edge subsets (all sizes, disconnected forests and the empty forest included), prove pairwise negative correlation of distinct edge indicators.

Lead version consumed: fleet01/B01 handoff `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, blob `4cee205cb7d254caf785692838111988a0b8a155`. Its source correction is retained: the old fixed-graph Cocks weighted-upgrade bridge is not admitted; the first lead debt is a direct triangle/STAR-2 comparison.

Named OTHER-account result consumed and applied: partner fleet02/B01 `fleet02-B01-20260922T043445Z-k4-response-synthesis.md`, blob `082008f849c3c0f0ab93356e9d6116f21531386d`. It gives the exact three-terminal K4 synthesis criterion

`tau := d t-(ab+ac+bc) >= 0`,  and  `tau t <= abc`.

I also consumed the partner's newer two-cut influence budget `FOREST-2CUT-INFLUENCE-BUDGET-v1`, blob `6e4a41368ef6c32c2a9a0634ab1096dda8c85553`; it is compatible with, but logically separate from, the overlap-cycle argument below.

## 2. Exact residual count identity

Put `G0=G-{e,f}` and let `N` be the set of every forest of `G0`. Define

- `A={K in N: e is addable to K}`;
- `B={K in N: f is addable to K}`;
- `D={K in N: e and f are jointly addable to K}`.

Then

`Delta_ef = |A||B|-|N||D|`,

and cancellation of `A x D` on both sides gives the equivalent comparison

`|(N\A) x D| <= |A x (B\D)|`.                                      (R)

This formulation retains every disconnected base forest.  In the four addability cells it is the previously derived identity

`Delta = n10*n01-n00*n11+|N| q`,

where `q` counts states in which `e,f` are individually addable but jointly form a cycle.

## 3. New full-radius reconnection lemma

### Lemma (every residual domain pair has a reconnection target)
For every `(F,H) in (N\A) x D`, there exist a nonempty set `S` of edges on the unique `e`-path in `F` and a target pair `(F',H') in A x (B\D)` obtained by transferring either `S` or all but one edge of `S` from the first forest to the second.

### Proof
Because `F notin A`, the endpoints of `e` are connected in the forest `F`; let `P` be their unique path. Because `H in D`, both `H+e` and `H+f` are forests and `H+e+f` is a forest. Contract every connected component of `H`. The images `\bar e,\bar f` are therefore two distinct nonloop edges whose two-edge graph is a forest; in particular, they are not parallel.

Read the `H`-components met by `P`. This gives a walk from one endpoint-component of `\bar e` to the other. Loop-erase it and choose the corresponding crossing edges of `P`; call this nonempty set `S`. In the component quotient, `S` is a simple path `R` joining the endpoints of `\bar e`. Consequently `H union S` is a forest.

**Case 1: the two endpoint-components of `\bar f` are not both vertices of `R`.** Then `H union S` connects the endpoints of `e` but does not connect the endpoints of `f`. Hence

`H' := H union S in B\D`.

Set `F':=F\S`. Since `S` contains at least one edge of the unique `e`-path `P`, the endpoints of `e` are disconnected in `F'`, so `F' in A`.

**Case 2: both endpoint-components of `\bar f` occur on `R`.** Choose one selected edge `s` on the subpath of `R` between them and put `S'=S\{s}`. Removing `s` splits the selected quotient path into two pieces. The endpoints of `e` lie on opposite sides, and the endpoints of `f` also lie on opposite sides. Thus both marked edges are individually addable to

`H' := H union S'`,

but each joins the same two resulting connected components. Therefore adding both creates exactly one cycle: `H'` lies in the overlap state `Q`, hence in `B\D`.

Finally `S'` is nonempty. If `|S|=1`, the simple path `R` has just the two endpoint-components of `\bar e`; having both endpoints of `\bar f` on `R` would make `\bar f` parallel to `\bar e`, contradicting `H in D`. Therefore deleting `S'` from `F` breaks the unique `e`-path, and `F':=F\S' in A`.

This proves the lemma.  It includes disconnected `H`, adjacent marked edges, components containing many vertices of `P`, and the overlap-cycle boundary case.

### What the lemma does and does not pay
It proves **existence of a legal reconnection for every residual domain pair** in (R), with `Q` appearing exactly as the fallback when the second marked edge lies on the quotient reconnection path. It does **not** prove (R): a Hall/fiber-capacity or injectivity bound is still required. This distinction is essential.

## 4. Genuine obstruction to bounded-radius transfer on general graphs

A universal radius-two transfer-only version is false outside complete/dense graphs.

Take vertices `a,b,x,y,c,d`, marked edges `e=ab`, `f=cd`, and let `G0` have only the three path edges

`a-x, x-y, y-b`.

Let `F` be this full 3-edge path and `H` the empty forest. Then `(F,H) in (N\A) x D`. If at most two available base edges are transferred from `F` to `H`, the second coordinate still does not connect `a` to `b`, and of course does not connect `c` to `d`; it remains in `D`, never in `B\D`. Transferring the full 3-edge quotient path succeeds.

So any direct reconnection theorem for arbitrary simple graphs must permit radius equal to the relevant quotient-path length (or use a fundamentally non-transfer move). This does **not** refute the separate fleet04/B02 radius-two Hall proposal restricted to complete graphs, where shortcut edges exist.

## 5. Applying fleet02/B01: a local polarization gate for its K4 synthesis cone

For a genuine three-terminal forest response write

`v=(d,a,b,c,t)`

for the five terminal partitions `1|2|3, 12|3, 13|2, 23|1, 123`, and define

`tau(v)=dt-(ab+ac+bc)`,

`sigma(v)=abc-tau(v)t`.

The partner's exact K4 synthesis applies exactly when `tau>=0` and `sigma>=0`.

For an ordinary edge `g` with activity `w`, the response is affine:

`v(w)=v0+w v1`.

Thus

`tau(w)=tau0+P_tau w+tau1 w^2`,

where

`P_tau=d0*t1+d1*t0-(a0*b1+a1*b0+a0*c1+a1*c0+b0*c1+b1*c0)`.       (T)

Also

`sigma(w)=sigma0+S1 w+S2 w^2+sigma1 w^3`.                         (S)

Consequently, conditional on the endpoint responses already lying in the synthesis cone, a clean sufficient local induction gate is

`P_tau>=0`,

and

`sigma'(w)=S1+2 S2 w+3 sigma1 w^2 >=0  for every w>=0`.             (P)

When `sigma1>0`, (P) is equivalent to `S1>=0` plus, in the only nontrivial case `S2<0`,

`S2^2 <= 3 S1 sigma1`.

This isolates a much smaller algebraic/combinatorial debt than arbitrary weighted Rayleigh positivity. Terminal-identification and contraction-induced parallel classes must be treated as boundary cases in any universal induction; no such universal proof is claimed here.

Two exact auxiliary identities support the interpretation of `tau`. Adding a weighted terminal triangle changes `(d,a,b,c,t)` but leaves `tau` invariant. Adding a new degree-three Steiner vertex with incident activities `p,q,r` transforms

`tau'=(1+p+q+r)^2 tau + d^2 p q r`.

Hence `tau` is exactly the residual not generated by terminal-triangle response, and a genuine three-way branch contributes a manifestly positive term.

## 6. Exact finite audit of the polarization gate

The attached exact-integer zeta checker exhaustively enumerates every labelled simple graph on `n=3,...,7` with fixed terminals `0,1,2`. It checks the two partner inequalities and, for every present edge, the local coefficients (T) and (P).

Totals:

- graphs: `2,131,016`;
- graph/present-edge splits: `22,271,180`;
- failures of `tau>=0`: `0`;
- failures of `sigma>=0`: `0`;
- failures of `P_tau>=0`: `0`;
- failures of `sigma'(w)>=0` for `w>=0`: `0`.

A stronger tempting induction is genuinely false: `S2` is negative in `41,544` exact instances. The smallest witness found is the six-vertex graph

`{04,05,13,15,23,25,34}` with `g=15`,

for which

`v0=(30,3,13,9,7)`, `v1=(10,11,1,13,17)`,

`tau(w)=27+118 w+3 w^2`,

`sigma(w)=162+536 w-30 w^2+92 w^3`.

Thus coefficientwise positivity of `sigma` is not a viable proof mechanism even though the derivative remains positive. Across all negative-`S2` cases in this scan, the largest exact-condition ratio numerically evaluated as `S2^2/(3 S1 sigma1)` is `0.158411716986 < 1`.

The finite scan is regression evidence only. Checker Git blob: `4be6dabf4273764269acc740a5199d956e79e64b`. No finite enumeration is promoted to a universal theorem.

## 7. Compact conditional end-to-end argument and first missing implication

The direct count route is now:

1. exact cancellation reduces the marked-edge Rayleigh inequality to (R);
2. the full-radius lemma above supplies at least one legal target for **every** residual domain pair, with overlap states `Q` precisely absorbing the case in which the `f` endpoints lie on the reconnection path;
3. **missing essential implication:** upgrade pointwise existence to a global Hall/fiber-capacity inequality for these variable-radius reconnections (or an equivalent weighted shadow estimate), thereby proving (R).

The three-terminal alternative is:

1. prove the local polarization inequalities (T),(P), including contraction/parallel and terminal boundary cases;
2. deduce `tau,sigma>=0` for every genuine three-terminal response;
3. apply fleet02/B01's exact K4 synthesis to replace such a boundary response by a nonnegative graphic gadget;
4. use only a source-secure size-decreasing gluing/minimal-counterexample argument. The lead's withdrawn fixed-Cocks bridge is **not** used.

The first route is closer to this slot's assignment and is the recommended next step. A plausible next attack is a Hall proof stratified by the quotient-path length and by the interval positions of the two `f` endpoint-components. The sparse radius-two obstruction shows that a proof cannot cap that path length uniformly.

## 8. Honest status

`ESSENTIAL_STEP_APPLIED`. The full FOREST conjecture is not proved here. The new theorem is the full-radius **existence** reconnection lemma; the unresolved universal step is multiplicity/capacity control. The finite polarization audit and K4 synthesis gate are auxiliary but sharpen the alternative separator route. No benchmark/brain work, production mutation, scheduler mutation, email, Drive action, public posting, paid/remote compute, or permission change was performed.
