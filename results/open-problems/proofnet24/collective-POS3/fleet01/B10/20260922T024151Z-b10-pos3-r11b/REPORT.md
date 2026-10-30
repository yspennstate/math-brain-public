# POS3 fleet01/B10 — quantitative TP2 of the exact three-chain flux

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run changes mechanism from the preceding fleet01/B10 cover-selection/nested-profile falsification. Instead of trying to choose a favorable deleted chain, it returns to the exact three-chain ideal-lattice path model and proves an intrinsic correlation inequality for its full two-dimensional flux. The new theorem is arbitrary-size and uses the actual uniform law on full linear extensions throughout.

## 1. Exact collective state consumed

The active collective allocation is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; new benchmark/installation work is stopped for this slot.

I used the following exact completed collective state.

1. **Campaign lead fleet04/B10**, run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-at-most-three counterexample, the transitive strong-majority order pins every element to its majority rank with probability `>1/81`. In three-chain coordinates this gives
   
   `81 W_x(g_b(x),g_c(x)) > E`,
   
   where `E=e(P)` and `W_x` is the exact two-chain flux through the edge which inserts `x`.

2. **Named assigned partner fleet02/B11**, run `20260922T011526Z-b11-pos3-r12-17156e52`. It preserves the earlier exact ordinal-factorization reduction, so a cardinality-minimal counterexample may be taken incomparability-connected, and it isolates the surviving proper-autonomous-chain branch via its exact binomial corridor law. I apply that reduction in the conditional architecture below: the theorem proved here is aimed at the complementary fixed-three-chain flux geometry of the connected core and does not replace the partner's one-dimensional autonomous-chain branch by a falsely uniform quotient.

3. **fleet01/B19**, run `20260922T014910Z-b19-pos3-r11`, report blob `004a04191bf389e3493c3346fd57e67b35500049`, and its later first-interruption renewal report. These prove exact chain-insertion weights and show that deleting the first majority block gives a nonuniform law with a controlled renewal decomposition. Thus any argument here must be made before deletion, in the unit-weight full-extension path law, or retain the exact deletion multiplicities.

4. **fleet02/B10**, run `20260922T014627Z-fleet02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`. At the first/last strong-majority boundaries a hypothetical counterexample has endpoint probability strictly in `(2/3,7/9)` and both canonical Hasse-blocker channels are active. Its residual is explicitly multi-boundary.

5. **This slot's preceding report**, blob `b33f4c52f0da12d8bcb9f30b89c9ceb1a88b3936`. It gives a 9-element connected module-prime width-three poset for which every chain deletion in every three-chain cover retains a strictly nested incomparable profile pair. Hence the current run deliberately does not try to eliminate nested profiles by changing the cover.

The freshest compatible B11 induction work also refutes the stronger statement that an arbitrary balanced pair of the smaller poset must survive the exact ideal-block reweighting. The remaining induction statement is existential/adaptive, not pairwise.

## 2. External inequality used exactly

The only external counting inequality needed below is the lower half of the Fishburn minimal-elements correlation inequality. In the notation `e(R)` for the number of linear extensions of a finite poset `R`, if `u,v` are distinct minimal elements of an `m`-element poset, then

`e(R)e(R-u-v) / (e(R-u)e(R-v)) >= m/(m-1)`                 (2.1)

for `m>2`; for `m=2` the same formula holds directly with value `2`. By order duality it also holds for two distinct maximal elements.

A current source is Swee Hong Chan and Igor Pak, *Correlation inequalities for linear extensions*, Theorem 1.1; the same inequality is summarized as Theorem 7.1 in their survey *Linear extensions of finite posets*. The lower bound is the Fishburn inequality. I use only the lower bound, not the newer upper bound.

## 3. Exact three-chain edge flux

Fix any partition of `P` into three chains

`C_a=(a_1<...<a_p)`, `C_b=(b_1<...<b_q)`, `C_c=(c_1<...<c_l)`.

Fix `x=a_r`. For integers `0<=s<=q`, `0<=t<=l`, define the chain-prefix set

`I_{s,t}={a_1,...,a_{r-1}} union {b_1,...,b_s} union {c_1,...,c_t}`.       (3.1)

Call `(s,t)` **x-admissible** when both `I_{s,t}` and `I_{s,t} union {x}` are ideals of `P`. Equivalently, a linear extension can reach that ideal state and take the `x`-edge next.

Let

`W_x(s,t)=#{L in L(P): exactly s elements of C_b and t elements of C_c precede x}`.     (3.2)

This is the fleet01/B10 exact flux cell. If `(s,t)` is x-admissible and

`R_{s,t}=P \ (I_{s,t} union {x})`,

then the prefix before `x` and suffix after `x` are independent counting choices, hence

`W_x(s,t)=e(I_{s,t}) e(R_{s,t}).`                                (3.3)

If the cell is not admissible, `W_x(s,t)=0`.

Equation (3.3) is simply the unit-weight ideal-lattice path factorization: a full extension counted by the cell is a path from the empty ideal to `I_{s,t}`, then the `x` edge, then a path from `I_{s,t} union {x}` to `P`.

## 4. New theorem: the flux matrix is quantitatively TP2

### Theorem 4.1 — quantitative elementary-square inequality

For every elementary square with `0<=s<q` and `0<=t<l`, write

`W_00=W_x(s,t)`, `W_10=W_x(s+1,t)`, `W_01=W_x(s,t+1)`, `W_11=W_x(s+1,t+1)`.

Then

`W_00 W_11 >= W_10 W_01`.                                      (4.1)

More strongly, whenever `W_10 W_01>0`, put

`k=(r-1)+s+t`,

`n_- = k+2 = r+s+t+1`,

`n_+ = |P|-k-1 = |P|-r-s-t`.

Then `n_-,n_+>=2` and

`W_00 W_11 / (W_10 W_01)`

`>= [n_-/(n_--1)] [n_+/(n_+-1)]  > 1`.                         (4.2)

The `m=2` factors are interpreted directly as `2`.

### Proof

Assume first that `W_10 W_01>0`. Put

`I=I_{s,t}`, `b=b_{s+1}`, `c=c_{t+1}`.

The positivity of the two cross cells says that

`I+b`, `I+c`, `I+b+x`, `I+c+x`

are ideals. Ideals are closed under intersection and union, so

`I`, `I+b+c`, `I+x`, `I+b+c+x`

are ideals too. Hence `W_00,W_11>0`. In particular `b` and `c` are incomparable with each other and with `x` in precisely the way required by these four edge states.

For the **prefix factor**, let

`J=I union {b,c}`.

Both `b` and `c` are maximal elements of the induced poset `J`: if, say, `b<z` for some `z in I`, then ideality of `I` would force `b in I`; and `b,c` cannot be comparable because both `I+b` and `I+c` are ideals. The size of `J` is `n_-=|I|+2`. Applying the dual of (2.1) gives

`e(I) e(I+b+c) / [e(I+b)e(I+c)] >= n_-/(n_--1)`.               (4.3)

For the **suffix factor**, let

`R=P \ (I union {x})`.

Both `b` and `c` are minimal in `R`. Indeed all of their predecessors are already in `I`; neither can have `x` below it, because then the corresponding cross cell with that element before `x` would be impossible. The size of `R` is `n_+`. Applying (2.1) gives

`e(R)e(R-b-c) / [e(R-b)e(R-c)] >= n_+/(n_+-1)`.                (4.4)

Now use (3.3):

`W_00=e(I)e(R)`,

`W_10=e(I+b)e(R-b)`,

`W_01=e(I+c)e(R-c)`,

`W_11=e(I+b+c)e(R-b-c)`.

Multiplying (4.3) and (4.4) is exactly (4.2).

If `W_10 W_01=0`, the right side of (4.1) is zero and the ordinary TP2 inequality is immediate. This proves the theorem. `□`

### Corollary 4.2 — full TP2 / monotone likelihood ratio

The whole matrix `W_x=(W_x(s,t))` is TP2. In particular, for `s_1<s_2` and `t_1<t_2`,

`W_x(s_1,t_1)W_x(s_2,t_2) >= W_x(s_1,t_2)W_x(s_2,t_1)`.        (4.5)

On the positive support, the ratio

`W_x(s_2,t)/W_x(s_1,t)`

is nondecreasing in `t`. Thus, if

`S=J_b(x)=#{C_b-elements before x}`,

`T=J_c(x)=#{C_c-elements before x}`

under the **uniform full-extension law**, then the conditional law of `T` is monotone-likelihood-ratio increasing as `S` increases.

**Reason.** Adjacent TP2 inequalities chain to arbitrary minors. The support itself is closed under coordinatewise meet and join because it is defined by ideal states and an available `x` edge, so zeros do not create a hidden sign reversal.

## 5. Exact candidate balanced-pair inequality under the actual uniform law

Normalize `p_{s,t}=W_x(s,t)/E`, where `E=e(P)`. Summing (4.5) over two ordered row blocks and two ordered column blocks preserves the determinant sign. Therefore every two thresholds satisfy

`Pr(S<=s,T<=t) Pr(S>s,T>t)`

`>= Pr(S<=s,T>t) Pr(S>s,T<=t)`.                                (5.1)

Equivalently, the two chain-prefix counts are positively quadrant dependent. A useful conditional form is

`Pr(T>=t | S>=s) >= Pr(T>=t)`                                   (5.2)

whenever the conditioning event has positive probability, with the symmetric lower-tail statement as well.

This is the requested candidate inequality in the exact three-chain coordinates: it is not an inequality for a falsely uniform deletion law. Every probability in (5.1)-(5.2) is under the original uniform law on all linear extensions of `P`.

There is also a quantitative local strengthening. Whenever all four elementary cells participate, the odds ratio is at least

`[n_-/(n_--1)] [n_+/(n_+-1)]`,                                 (5.3)

so the same-direction attraction is strictly stronger near the ends of an extension and tends toward ordinary TP2 only when both sides are large.

## 6. Consequence in a hypothetical no-balanced width-three poset

Let `g_b(x)` and `g_c(x)` be the majority-gap indices selected by the common strong-majority order. For a genuinely two-sided incomparable gap on chain `C_b`, no-balancedness gives

`Pr(S>=g_b)>2/3`, `Pr(S<=g_b)>2/3`,

and hence

`Pr(S=g_b)>1/3`.                                                 (6.1)

The same holds for `T` at `g_c`. This is the previously known heavy-slice normal form.

The new TP2 theorem says these two heavy coordinates cannot be anti-correlated to evade one another. For example,

`Pr(S>=g_b, T>=g_c) >= Pr(S>=g_b)Pr(T>=g_c) > 4/9`,             (6.2)

and dually

`Pr(S<=g_b, T<=g_c)>4/9`.                                      (6.3)

More generally, every threshold pair on the two other chains obeys the same monotone-likelihood-ratio order, not just the four majority-neighbor comparisons used by a single XYZ application.

The lead's existing `>1/81` central-cell theorem remains stronger for the singleton event

`{S=g_b,T=g_c}`

than anything claimed here. I do **not** replace it. The gain is structural: the full exact flux surface has a fixed total-positivity sign and a quantitative elementary-square factor. Thus a future consecutive-boundary argument can propagate likelihood-ratio information through the entire row/column system rather than control isolated pair events independently.

## 7. What this pays in the conditional end-to-end route

Assume a cardinality-minimal POS3 counterexample exists. Apply the named partner fleet02/B11 reduction so its incomparability graph is connected; handle a proper autonomous chain through the partner's exact binomial-corridor branch, and otherwise work in the connected three-chain core. The inherited collective state then supplies:

1. a transitive strong-majority order with at least five chain blocks;
2. exact heavy one-chain slices `>E/3`;
3. exact central cells `>E/81` from the lead;
4. two active endpoint Hasse-blocker channels and endpoint probability `<7/9`;
5. unavoidable nested profile defects from the preceding fleet01/B10 report;
6. **new in this run:** every `W_x` is quantitatively TP2, so the two other-chain coordinates have a global monotone-likelihood-ratio coupling under the true uniform law.

This pays a previously unrecorded sign question in the flux route: the two-dimensional exact extension multiplicity surface is not arbitrary and cannot contain an anti-TP2 local defect. Search of the current collective POS3 archive before writing this report found no prior TP2 statement for `W_x`; this is only a statement about the checked archive, not a literature-priority claim.

The first essential unpaid implication is now sharper:

> **Consecutive-flux transport problem.** For two consecutive strong-majority block boundaries, express the transition between their exact TP2 flux surfaces and show that the endpoint two-channel surplus cannot propagate across every interior boundary while preserving simultaneously the `>E/3` heavy marginal gaps, the lead's `>E/81` central cells, and the active double-blocker constraints.

A proof can now assume each individual flux surface is positively associated/MLR; the missing difficulty is the **inter-element transport**, not the sign of the two-coordinate law for one fixed element.

## 8. Exact regression certificate

The companion verifier applies the theorem to the exact 9-element source-valid poset from the preceding fleet01/B10 report,

`0<1, 0<3, 1<4, 1<5, 2<5, 3<5, 4<7, 5<6, 5<8, 6<7`,

whose full extension count is `109` and which has exactly `16` unordered three-chain covers.

It exhausts all 16 covers, every element, and every elementary flux square. Results:

- `109` exact linear extensions;
- `16` unordered three-chain covers;
- `1176` elementary flux squares;
- `144` squares with both cross terms positive, where the quantitative Fishburn factor is applicable;
- every ordinary TP2 inequality passes;
- every quantitative inequality (4.2) passes;
- the minimum cross-multiplied integer slack in the quantitative inequality is `144`.

Terminal marker:

`POS3_FLUX_FISHBURN_TP2_CHECK_PASS`.

Verifier SHA-256: `ca4b243cdfc9c54c76d1857565936554c814273fd17fde4ec04aba82f413289c`.  
Output SHA-256: `e497bc7ebf8222baba3c6e83c215c087900bb5fadffe5610dfc7bca9756c7f61`.

The computation is only a regression check on the cited finite certificate. Theorem 4.1 is the arbitrary-size proof and does not depend on this enumeration.

## 9. Status / safeguards

- exact three-chain path-flux factorization: inherited and restated;
- quantitative elementary-square TP2 theorem: **PROVED**;
- full TP2 / MLR / positive-quadrant inequality for each fixed-element flux: **PROVED**;
- parent width-three `1/3–2/3` statement: **OPEN / NOT PROVED**;
- outcome: `ESSENTIAL_STEP_APPLIED`.

No benchmark material, FEI proof content, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive action, public posting, paid model/API/Codex call, remote workflow, permission change, or brain-readiness claim is present in this scientific artifact.
