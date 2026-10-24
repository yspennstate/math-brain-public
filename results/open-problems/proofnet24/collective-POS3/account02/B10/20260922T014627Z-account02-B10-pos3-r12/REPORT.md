# POS3 account02/B10 — endpoint blocker product cap and two-channel activation

**Run:** `20260922T014627Z-account02-B10-pos3-r12`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This is the third consecutive account02/B10 POS3 contribution. The previous two used exact two-element deletion fibers and one-fiber corridor inequalities. To comply with the required mechanism change, this run switches to an event-level mass-transport argument: right-fringe completion mass is identified exactly with a blocker-order event, then a source-verified XYZ/Shepp correlation inequality is applied before returning to the exact deletion defects. No deletion skeleton is reweighted to uniform.

## 1. Exact source-bound state consumed

Fresh owner control remained revision `2026-09-22.2`; this slot is POS3 research and old benchmark/installation work is stopped.

The following completed dependencies were read before the derivation.

1. **Campaign lead account04/B10**, run `20260922T011127Z-account04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-three counterexample, every element has a pinned strong-majority-rank event of probability `>1/81`; in the three-chain flux coordinates this gives `81 W_x(g_b(x),g_c(x))>E`.
2. **Named partner account03/B11**, run `20260922T011439Z-account03-B11-pos3-r12`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`. At the first strong-majority block boundary `x ≺_* y`, the two canonical minimal successor blockers `s_1,s_2` are Hasse covers of `x`, and `y,s_1,s_2` are pairwise incomparable. The blocker pair is nonautonomous and every distinguisher of it occurs strictly after the whole second majority block. The last boundary has the order-dual statement.
3. **Prior local exact coupling**, report blob `54b518413481e7ed162f44c8b6c417b3f94b5d29`. For a deletion skeleton `tau in L(P\{x,y})` at the first boundary, the legal insertion intervals have `I_x=[a,b]`, `I_y=[c,d]` with `c<=a`. If `d<=b`, the fiber defect is nonpositive. If `d>b`, writing `n=b-a+1`, `L=a-c`, `R=d-b`,
   `N_xy=nR+n(n+1)/2`, `N_yx=nL+n(n+1)/2`, so `Delta_tau=n(R-L)`.
4. **External exact input.** Aires–Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134, Theorem 2.1, recalls the multivariate Shepp/XYZ inequality: for uniform linear extensions, `Pr(z precedes every member of Y) >= product_{u in Y} Pr(z precedes u)`. The theorem is stated for arbitrary finite posets; no width or induced-uniformity assumption is added here.

The lead's `>1/81` atom remains a global constraint. The new result below gives a much stronger endpoint-specific joint blocker event (`>4/9`), so the lead atom is not the limiting endpoint estimate; it remains relevant to interior-boundary alignment.

## 2. Compact conditional end-to-end route

Assume for contradiction that a finite width-at-most-three poset `P` has no balanced incomparable pair. The inherited reduction gives a transitive strong-majority order `L_*`. Let `x ≺_* y` be its first adjacent chain-block boundary. Then

`p_xy := Pr(x<y) > 2/3`.

By the partner theorem, there are exactly two minimal successor blockers `M={s_1,s_2}`, with `x \lessdot s_i`, `s_i || y`, and `y ≺_* s_i`. Hence

`Pr(y<s_i)>2/3` for `i=1,2`.

The first unpaid implication after the previous run was to connect the two exact endpoint blocker channels rather than merely find one extreme deletion fiber. The theorem below does that: it identifies the *entire right-fringe capacity* of each channel with a genuine three-element order event, and forces both channels to carry positive majority-direction defect.

## 3. General endpoint blocker product theorem

The following statement does not require width three.

Let `x||y` in a finite poset and assume

`Pred(y) subseteq Pred(x)`.

Let

`S_x(y)={z:x<z and z||y}`,  
`M=Min S_x(y)`.

For a deletion skeleton `tau in L(P\{x,y})`, use the interval notation from the prior local report:
`I_x=[a,b]`, `I_y=[c,d]`, with `c<=a`.

If `d>b`, let `q(tau)` be the first successor of `x` in `tau`. The prior proof shows `q(tau) in M`. Put `n=b-a+1` and `R=d-b`.

For each `q in M`, define the exact right-fringe mass

`U_q = sum_{tau: d>b, q(tau)=q} nR`.

### Lemma 3.1 — right-fringe / blocker-order bijection

For every `q in M`,

`U_q = #{L in L(P): q<y and q<m for every m in M\{q}}`.        (RF)

**Proof.** A right-fringe completion has `y` inserted after the first `x`-successor `q`; all other minimal blockers occur after `q`. Hence it lies in the event on the right.

Conversely, suppose a full extension has `q<y` and `q<m` for all other minimal blockers. If some successor `z` of `x` appeared before `q`, then `z<y` is impossible because `x<z<y` would force `x<y`. If `y<z`, it cannot appear before `q<y`. Thus `z||y`, so `z` is a blocker. Some minimal blocker `m in M` satisfies `m<=z`; then `m` appears before `q`, contradicting either `m=q` or the assumed `q<m`. Therefore `q` is the first successor of `x`; deleting `x,y` places the extension in exactly one right-fringe completion counted by `nR`. This is bijective. `□`

The events in (RF) are disjoint as `q` varies, and their union is exactly the event that `y` is **not** earlier than every member of `M`. Therefore, with `E=e(P)` and

`Q=#{L: y<m for every m in M}`,

we have the exact identity

`sum_{q in M} U_q = E-Q`.                                      (3.1)

Now let `D=e_xy-e_yx=sum_tau Delta_tau`. Fibers with `d<=b` have `Delta_tau<=0`; fibers with `d>b` satisfy

`Delta_tau=n(R-L)<=nR`.

Summing and using (3.1),

`D <= E-Q`.                                                    (3.2)

The multivariate XYZ inequality gives

`Q/E = Pr(y<m for all m in M) >= product_{m in M} p_ym`.

Since `p_xy=(1+D/E)/2`, (3.2) yields the endpoint blocker-product bound

`p_xy <= 1 - (1/2) product_{m in M} p_ym`.                    (3.3)

All probabilities are under the original uniform law on `L(P)`. The nonuniform deletion-skeleton law is never replaced by a uniform law.

## 4. Width-three endpoint consequence: strict 7/9 cap

At the first boundary of a hypothetical POS3 counterexample, the named partner gives exactly two blockers `M={s_1,s_2}` and the strong-majority order gives

`p_{ys_1}>2/3`, `p_{ys_2}>2/3`.

Thus (3.3) gives

`2/3 < p_xy < 1 - (1/2)(2/3)^2 = 7/9`.                       (4.1)

By order duality, the same strict `7/9` upper bound holds for the last adjacent strong-majority block boundary.

There is also an exact finite-count form. If `A_i=#{L:y<s_i}`, then
`Q >= ceil(A_1 A_2/E)` and

`e_xy <= E - ceil( ceil(A_1 A_2/E) / 2 )`.

Using only `A_i>=floor(2E/3)+1` gives a source-independent integer endpoint cap for every `E`.

This is stronger than the lead's `>1/81` pinned atom at the endpoints: here the coarse event `y<s_1,s_2` has mass `>4/9`. The lead atom remains a proper, much more localized subset of this event and is still needed for interior alignment rather than endpoint existence.

## 5. Both canonical Hasse-blocker channels are forced active

The product cap alone bounds the endpoint. The exact defect decomposition gives a second consequence that directly applies the partner's two-cover theorem.

Let

`Phi_i = sum Delta_tau`

over positive-defect fibers (`Delta_tau>0`) whose first `x`-successor is `s_i`, and let

`Psi = sum_{Delta_tau<0} (-Delta_tau)`.

Then exactly

`D = Phi_1 + Phi_2 - Psi`.                                    (5.1)

Moreover `Phi_i<=U_{s_i}`. By (RF),

`U_{s_i} <= #{L:s_i<y} < E/3`,

because `p_{ys_i}>2/3`.

Since `p_xy>2/3`, we have `D>E/3`. Therefore, for each `i` and the other index `j`,

`Phi_i = D+Psi-Phi_j > E/3+Psi-E/3 = Psi`.                   (5.2)

So **both** canonical Hasse-cover blockers carry positive majority-direction deletion-fiber defect, and each channel individually exceeds the *entire* negative deletion-fiber defect.

In particular, for each `s_i` there exists an exact deletion skeleton whose first successor of `x` is `s_i` and for which `Delta_tau>0` (equivalently, in the nested notation, `R>L`). The previous run only forced an extreme/corridor fiber in at least one blocker channel. The new statement activates both partner-certified Hasse forks under the true conditioning weights.

The order-dual statement activates both canonical predecessor-blocker channels at the last boundary.

## 6. Decisive regression computation

A standard-library exact enumerator checks the mass-transport identities on two already-source-bound width-three adversaries.

1. **Partner account03/B11 79-extension witness.** At `(x,y)=(0,1)`, blockers are `{3,4}`, `e_xy=54`, and
   `A_3=65`, `A_4=55`, `Q=50`.
   Exact right-fringe masses are `U_3=9`, `U_4=20`, equal to the corresponding blocker-order event counts. Positive-defect masses are `Phi_3=9`, `Phi_4=20`, across 5 and 12 positive fibers.
2. **Prior local 91-extension witness.** At `(x,y)=(4,2)`, blockers are `{5,6}`, `e_xy=62`,
   `A_5=62`, `A_6=74`, `Q=58`.
   Exact right-fringe masses are `U_5=25`, `U_6=8`, again exactly the blocker-order event counts; the same numbers are the positive-defect masses in this example.

The checker verifies the nested-fiber formulas, (RF), `sum U=E-Q`, `D<=sum U`, the instance-level XYZ inequality, the product cap, and two-channel activation where the counterexample-direction inequalities hold. It ends with

`POS3_TWO_CHANNEL_MASS_TRANSPORT_CHECK_PASS`.

Verifier blob: `24bbd0ceac83eb56f5b52d414ca5591a811cd613`.  
Captured output blob: `c91901a324deb9eeefe5e78341341e4844697efb`.

The computation is regression evidence for the finite examples; Lemma 3.1 and inequalities (3.2)–(5.2) are symbolic arbitrary-size arguments.

## 7. What moved and the next exact obligation

**Moved.**
- The endpoint defect now satisfies the universal blocker-product inequality (3.3).
- In a width-three counterexample, first and last strong-majority boundary probabilities are trapped strictly in `(2/3,7/9)`.
- At each endpoint, both partner-certified Hasse-blocker channels are necessarily active in exact positive deletion-fiber flow, each dominating the total negative defect.

**Still open.** This does not yet couple an active first-endpoint channel to the *next* majority-block boundary. The named partner's delayed-distinguisher theorem says the first blocker pair cannot be distinguished inside the first two blocks, so the first genuine channel asymmetry is forced into `B_3` or later.

The next exact implication is therefore:

> Follow both active endpoint Hasse channels through their first delayed distinguishers and the next adjacent-boundary double-blocker certificate. Prove that their exact weighted flow cannot both remain strong without either producing a balanced pair, four mutually incomparable elements, or a proper autonomous nonchain.

This is now a multi-boundary transport problem with two provably nonempty endpoint channels; no one-boundary local shortcut remains.

## 8. Scope and provenance

Outcome: `ESSENTIAL_STEP_APPLIED`. Parent POS3 remains open. No finite census is promoted to closure and no open conjecture is called false.

The companion verifier and output are immutable files in this run folder. A scoped manual privacy/provenance review found only mathematical definitions, public/source-bound result identifiers, and exact finite relation data already present in the cited peer reports. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, public posting, paid API/model/Codex execution, remote workflow, or permission change is present.
