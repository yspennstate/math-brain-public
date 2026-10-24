# FOREST / account04 B01 — exact two-edge-cut trichotomy and bridge-path collapse

**Run:** `account04-b01-20260922T093735Z-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** OPEN; no full-proof claim.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and peer state actually used

Target: for every finite simple graph, under the uniform law on all unrooted forests (all sizes, disconnected forests included), prove pairwise edge negative correlation.

Latest complete lead version consumed: account01/B01 `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, canonical report commit `79044b575c4b689248892f37b9930e983dddabca`. That report identifies the source-safe deletion/contraction Simpson mechanism and the separator debt after rejecting the fixed-graph weighted-Cocks shortcut.

Named OTHER-account result consumed and directly applied: account02/B01 `B01-20260922T090454Z-forest-r17`, report commit `19ba03bd035c953f9f6a137965d48822a6f702ff`, candidate `ALL-EDGE-MATCHING-INCONSISTENCY / BRIDGE-PATH-CLOSURE-v1`. It proves a class-wide simple-to-loopless-unit transfer, then in an edge-minimal loopless unit counterexample gives the all-third-edge Simpson inequality, global positive-covariance matching, connectedness of `M-{e,f}`, and a bridge skeleton in which every bridge is crossed by exactly one marked edge. It also imports account03/B02's exact three-edge-cut exclusion.

Assigned partner account01/B02 `20260922T032220Z-account01-B02-forest11` was also inspected. I preserve its warning that contraction can create parallel labelled edges; the argument below therefore works in the loopless labelled multigraph universe rather than silently simplifying parallel classes.

The account03/B02 triad theorem `20260922T080202Z-B02-forest-r11` is used only where stated: if `{e,f,g}` is a three-edge cut in the unit setting, the marked pair is nonpositively correlated.

## 2. Exact all-parameter two-edge-cut polynomial

Let a loopless graph or labelled multigraph be split by a vertex bipartition into sides `A,B`, with exactly two crossing labelled edges

`r = a b`, `s = a' b'`,

where `a,a'` are on side `A` and `b,b'` are on side `B`. Give `r,s` activities `x,y>0`; internal side activities may be arbitrary positive values. Write

- `Z_A,Z_B` for the side forest polynomials;
- `C_A,C_B` for the side forest polynomials restricted to forests connecting the corresponding boundary terminals (`a~a'` or `b~b'`);
- `D_A=Z_A-C_A`, `D_B=Z_B-C_B`.

For a fixed pair of side forests, all four subsets of `{r,s}` are acyclic except that `{r,s}` is forbidden exactly when both side forests connect their two boundary terminals. Therefore

`boxed: Z_G = (1+x)(1+y) Z_A Z_B - x y C_A C_B.`                 (2.1)

This identity is all-parameter and needs no closure theorem.

## 3. New theorem A — one marked cut edge localizes to a smaller unit graph

Assume `r` is one member of the bad marked pair and the other mark `f` lies internally in side `A`; `s` is unmarked. Expand in the activity `u` of `f`:

`Z_A(u)=A_0+u A_1`, `C_A(u)=C_0+u C_1`.

Because a multiaffine Rayleigh difference is independent of the activities of its two marked variables, set `x=u=0` in (2.1). A direct four-term expansion gives

`Delta_G(r,f) = y(1+y) Z_B C_B (A_0 C_1-C_0 A_1).`              (3.1)

Let `h=aa'` be a new virtual labelled edge on side `A`. Its forest polynomial is

`Z_{A+h}=Z_A+t D_A`,

and the Rayleigh difference `Delta_{A+h}(h,f)` is independent of `t`; at `t=0`,

`Delta_{A+h}(h,f)=D_0 A_1-A_0 D_1=A_0 C_1-C_0 A_1.`             (3.2)

Hence

`boxed: Delta_G(r,f)=y(1+y)Z_B C_B Delta_{A+h}(h,f).`            (3.3)

Degenerate cases are safe. If `C_B=0`, the left side is zero. If `a=a'`, then `D_A=0` and again the gap is zero. Otherwise `h` is a nonloop; it may be parallel to an existing edge, which is allowed in the loopless labelled multigraph class.

In an edge-minimal loopless **unit** counterexample, specialize `y=1`. The graph `A+h` has `|E(A)|+1 < |E(G)|` labelled nonloop edges, so minimality makes its marked gap nonnegative. Thus a bad pair cannot contain exactly one member of a two-edge cut.

This is the missing exact separator case needed below; it does not invoke arbitrary external-field closure or collapse a parallel class.

## 4. New theorem B — opposite-side internal marks factor through two smaller virtual-edge gaps

Now suppose neither cut edge is marked, with `e` internal to `A` and `f` internal to `B`. Write

`Z_A=A_0+uA_1`, `C_A=C_0+uC_1`,
`Z_B=B_0+vB_1`, `C_B=E_0+vE_1`.

Put `Q=(1+x)(1+y)` and `q=xy`. Expanding (2.1) in `u,v` gives the exact factorization

`boxed:
Delta_G(e,f)=Q q (A_0 C_1-A_1 C_0)(B_0 E_1-B_1 E_0).`          (4.1)

Each factor is a virtual-edge Rayleigh gap:

`A_0 C_1-A_1 C_0 = Delta_{A+h_A}(h_A,e)`,
`B_0 E_1-B_1 E_0 = Delta_{B+h_B}(h_B,f)`.

Consequently, in an edge-minimal loopless unit counterexample, marks on opposite shores of an unmarked two-edge cut cannot form a bad pair: both augmented side graphs are strictly smaller loopless unit graphs, so both factors are nonnegative.

Together with the elementary case in which the two marked edges themselves form the whole two-edge cut (`Delta=Z_A Z_B C_A C_B >=0` at unit activities), an edge-minimal loopless unit counterexample has the following exact trichotomy:

> Every two-edge cut either is harmless by the formulas above, or it is **unmarked and both members of the bad pair lie on the same shore**.

That last same-shore case is the only two-edge-cut configuration not eliminated by unit minimality.

## 5. New theorem C — the account02 bridge-path skeleton collapses

Apply account02/B01 `B01-20260922T090454Z-forest-r17`. Let `M` be its edge-minimal loopless unit counterexample with bad pair `e,f`, and put `G0=M-{e,f}`. That result proves `G0` is connected and that if `g` is a bridge of `G0`, then:

- neither mark crossing the bridge cut would make `g` a coloop of `M`, impossible by minimality;
- both marks crossing would make `{e,f,g}` a three-edge cut, excluded by the account03/B02 triad formula;
- hence exactly one of `e,f` crosses.

But in the third case the cut of `M` is exactly `{g,e}` (or `{g,f}`), a two-edge cut containing exactly one member of the bad pair. Theorem A rules this out.

Therefore the bridge-path residual collapses completely:

`boxed: M-{e,f} is connected and bridgeless.`                    (5.1)

Equivalently every unmarked edge lies on a cycle already after deleting the two bad marked edges. This applies inside the all-edge Simpson / global-matching route and removes the `BRIDGE-PATH-CLOSURE` branch left open in account02/B01 r17.

This conclusion is compatible with, but logically distinct from, account03/B02's bridgeless conclusion obtained after assuming a separate 3-connected simple minimal-core package: here it is derived directly inside the loopless-unit all-edge-Simpson route, and the previously unresolved exactly-one-crossing bridge case is paid by (3.3).

## 6. Exact form of the sole surviving two-edge-cut debt

Suppose an unmarked unit two-edge cut `{r,s}` remains and both bad marks lie in side `A`. At `x=y=1`, (2.1) becomes

`Z_G = (4Z_B-C_B) Z_A + C_B D_A`

and therefore, if `h=aa'`,

`Z_G=(4Z_B-C_B) [Z_A + theta D_A]`,

where

`boxed: theta = C_B/(4Z_B-C_B).`                                 (6.1)

Thus

`boxed: Delta_G(e,f)=(4Z_B-C_B)^2 Delta_{A+h}(e,f; y_h=theta).`  (6.2)

Conditioning on `r=0` induces virtual activity `0`; conditioning on `r=1` induces

`theta_1=C_B/(2Z_B-C_B).`                                       (6.3)

Writing the outside terminal response `lambda=C_B/(Z_B-C_B)`,

`theta=lambda/(4+3lambda)`, `theta_1=lambda/(2+lambda)`,

so for `lambda>0`

`boxed: 2 theta < theta_1 < 3 theta.`                             (6.4)

In the edge-minimal loopless unit counterexample, deletion/contraction of `r` are smaller unit instances, so if

`R(t)=Delta_{A+h}(e,f;y_h=t)`,

then a bad same-shore cut must satisfy the rigid source-generated straddling

`R(0)>=0`, `R(theta)<0`, `R(theta_1)>=0`,                        (6.5)

with `R` a quadratic whose leading coefficient is the smaller contraction gap `Delta_{A/h}(e,f)>=0` (loops discarded, parallel labelled edges retained).

Therefore the first unpaid two-edge-separator implication is no longer an arbitrary weighted closure statement. It is:

> **TWO-CUT-STRADDLING-CLOSURE-v1.** Rule out a loopless unit side `A`, bad marks `e,f`, and a realizable outside response `lambda=C_B/D_B` for which the Rayleigh quadratic `R` has the exact sign pattern (6.5) at the linked parameters (6.4); or construct a genuine source-valid example realizing it.

This is strictly downstream of the already-paid bridge-path branch. I do not assume it.

## 7. Compact conditional end-to-end chain

A source counterexample can be transferred to the loopless labelled unit class as in account02/B01. Choose one with the fewest labelled edges. The all-edge Simpson identity and matching theorem of that run apply to every third edge. The new two-edge-cut formulas show that any two-edge cut touching a mark, or separating the two marks to opposite shores, is harmless. Combined with the peer triad theorem, `M-{e,f}` is connected and bridgeless. The only edge-separator residue is an unmarked two-edge cut with both bad marks on one shore, and its entire outside influence is the single source-generated scalar `theta` with the exact deletion/contraction bracket (6.4)-(6.5).

Paying `TWO-CUT-STRADDLING-CLOSURE-v1`, or deriving an inconsistency directly from the all-edge Simpson matching constraints in the bridgeless core, would move this route beyond the current separator barrier. Neither is claimed here.

## 8. Failure / computation record

No finite census or numerical experiment is used as evidence for this run. The displayed identities are direct symbolic expansions of (2.1). I deliberately did not rerun prior theta or small-graph checkers merely to manufacture activity.

A tempting overstatement is **not** made: (6.2) does not let unit edge-minimality evaluate `R(theta)` because `theta` is generally not 1 and exact unit realization need not be smaller. That is precisely the surviving debt.

## 9. Status

`ESSENTIAL_STEP_APPLIED`.

Parent FOREST target: **OPEN**. No full proof candidate is asserted, and no peer PASS is inherited as truth.
