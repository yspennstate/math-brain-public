# FOREST handoff — account01/B03 — 20260922T014518Z

Outcome: **CANDIDATE_REFUTED** for the current lead's claimed end-to-end closure step; parent target remains **OPEN**. The lead's complete-graph Hermite subtheorem is **not** refuted. Context: `WITHOUT_VERIFIED_BRAIN`.

Consumed latest complete lead: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`.

Consumed and applied named OTHER-account partner result: account02/B01 `B01-20260922T0004Z-forest-r11`, report blob `bf7b362f6cdb15453102b54e91be937cd89258f5`. Its exact K_{2,2} witness rules out sectorwise boundary conditioning; the formulas below retain the full induced response.

## Decisive source-scope correction

The cited Cocks/Semple-Welsh results do not justify the fixed-graph step

`unit p-NC on K_n => M(K_n) p-NC for all positive weights`.

Semple-Welsh's minor and series/parallel closure theorems are for the **weighted independence-correlated** class, and they explicitly state that they cannot show that a graph satisfying unit Conjecture 1.1 remains good under minors or series/parallel extension. Cocks proves a **class-level equivalence**: the unit conjecture for all graphs is equivalent to positive-weight correlation for all graphic matroids; the converse encodes rational weights by parallel copies in a generally different graph. Thus the current lead chain has a missing bridge: prove positive-weight p-NC for each M(K_n), or enough unit p-NC for all required parallel extensions of K_n, before invoking weighted minor closure.

## Exact overlap/reconnection identity

For H uniform over all forests of `G-{e,f}`, let X,Y be individual addability of e,f, S simultaneous addability, and Q=XY-S. With x=EX, y=EY, r=ES, q=EQ,

`D := xy-r = q-Cov(X,Y)`.

The target is exactly `D>=0` and this includes disconnected H and overlapping cycles.

For any third edge g, T=1_{g in H}, p=P(T=1), and conditional `D_t=x_t y_t-r_t`, exact expansion gives

`D=(1-p)D_0+pD_1-p(1-p)(x_1-x_0)(y_1-y_0)`,

or

`Cov(X,T)Cov(Y,T)/Var(T)=(1-p)D_0+pD_1-D`.

In a lexicographically minimal simple counterexample, deletion gives `D_0>=0`, and the exact extension identity

`Cov_{G-f}(1_e,1_g)=Cov(X,T)/(1+x)^2`

(and symmetrically) gives `Cov(X,T)<=0`, `Cov(Y,T)<=0` from proper simple deletions.

The only unresolved term is the contraction side: contracting g can create parallel classes/positive integer activities. For a strict violation delta=-D>0 the fail-closed form is

`Cov(X,T)Cov(Y,T)/Var(T) >= delta - p*max(0,-D_1)`.

Thus the exact missing quantity is the **contraction-weight debt** `max(0,-D_1)`. Loop and marked-parallel contraction boundary cases have D_1>=0 automatically; only genuine induced unmarked parallel classes need the weighted gate.

If D_1>=0 is later proved, an elementary obtuse-Bessel argument yields, with k=|E(G-{e,f})|,

`(2k-1) delta <= sqrt(Var(X)Var(Y)) + q`.

## Exact finite audit

Fresh exact Fraction arithmetic over every simple graph on <=5 vertices and every marked `(e,f,g)` checked 46,563 triple instances:
- conditioning identity failures 0;
- extension-identity failures 0;
- positive Cov(X,T_g) 0;
- positive Cov(Y,T_g) 0;
- conditional D_1<0 instances 0;
- positive raw Cov(X,Y) pairs 5,973, confirming q is essential.

First raw-positive witness: `K_4-{23}`, e=01, f=02, with N=8, x=3/4, y=7/8, r=q=3/8, Cov(X,Y)=3/32 and D=9/32, so the actual Rayleigh gap is 18.

Canonical report:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B03/20260922T014518Z-account01-B03-forest-auto11/report.md`
blob `12497c20d33b0b868ad57f89d5dfdc2bf20c814b`.

Checker blob `1c52c0e60ea091dba8b2a08c2fb5aabb33866321`; output blob `cf0c8f7450c324af333f542ab1115efa12da353a`.

Next exact obligation: repair the lead closure by proving the positive-weight K_n theorem / parallel-extension family, or attack the local contraction-weight debt directly without sectorwise conditioning. No full proof is claimed.
