TASK: B14 ACCOUNT: account02 RUN: 2026-09-21T19:58:15.024610949Z — sequential affine erasure refund and exact crossing-amplified spendable drop

**Status:** PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated `math_brain` or cognitive-memory retrieval/context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. Configured reasoning level, provider reasoning-token usage, and provider thinking time: UNKNOWN / not exposed.

**FULL-PROBLEM CHANGE:** NO full FEI bound is proved.

**MECHANISM CHANGE:** YES. The previous B14 affine-partition report reduced the hard shell-poor case to paying the one-shot parity-hash erasure `H(X|Y)`. This run proves that that one-shot erasure is an avoidable overcharge when the same affine coalescence is executed as a genuine sequence of restrictions. The sequential ledger gains an exact nonnegative projection/recombination refund, preserves the actual original-coordinate centered-influence cost, and converts the remaining target from a sign-free hash-entropy bound to a restriction-history quantity that depends on genuine Boolean descendants.

No novelty or publication-priority claim is made.

## 0. Fresh dependencies and the required three-report comparison

Fresh scientific master and P03 entry rules were read. The current joint FEI state and the newest compatible neighboring work were also consumed. In particular:

- account01/B18's curvature-refunded crossing result supplies the folded-influence crossing bookkeeping and the bounded potential `j(p)`;
- account04/B14's newer crossing-amplified corrected-erasure report supplies the exact physical identities `Delta J = I_A+C_A` and `Delta F = B_A-Q_A` and its mass-weighted selector consequences.

The previous three substantive B14 reports before this one were:

1. `20260921T175746Z-block-js-critical-han`: coherent restriction information tensorized over physical blocks, but the proper-block upper selector did not beat the singleton envelope;
2. `20260921T190143Z-affine-pair-global-budget`: pair-parity restriction gave a genuine nonnegative centered drop and an exact hybrid-tree telescope, but aggregate pair supply was not itself spendable at one node;
3. `20260921T193008Z-affine-partition-hash-budget`: bucket coalescence made a constant fraction of the shell-poor pair supply spendable, but left the one-shot parity-hash erasure `H(X|Y)` unpaid.

Thus the same universal theorem has not been re-labelled: the mechanism has moved from physical blocks to affine spendability and now to a sequential negative-credit ledger. The remaining quantified obligation is stated in Section 8.

## 1. Normalization and the affine partition

Let

`f:F_2^n -> {-1,+1}`,  `a_S=fhat(S)`,  `mu(S)=a_S^2`,  `X~mu`.

Write

`H=H(X)`,  `p_i=Pr(i in X)`,  `I=sum_i p_i`.

Character-center the parent so `p_i<=1/2` for every coordinate and put

`J=sum_i p_i`.

This does not change `H` or the folded influence. Define

`j(p)=1-h_2(1/2+sqrt(p(1-p)))`,
`Phi=sum_i j(p_i)`.

The inherited scalar estimate is

`0 <= Phi <= c_* J`,  where `c_*=2/ln 2`.                 (1.1)

Partition the coordinates into nonempty buckets `P={B_b}` and choose an anchor `a_b` in each bucket. For the potential bound below, choose `a_b` to maximize `j(p_i)` in its bucket. Put

`A = union_b (B_b \ {a_b})`,
`M_P = sum_b j(p_{a_b})`.

Make the invertible linear change of physical variables

`x_{a_b}=y_{a_b}`,
`x_i=y_i+y_{a_b}` for `i in B_b\{a_b}`.              (1.2)

In the dual spectral coordinates this sends

`X'_i=X_i` for `i in A`,
`X'_{a_b}=Y_b := xor_{i in B_b} X_i`.                 (1.3)

Let

`r_b=Pr(Y_b=1)`, `q_b=min(r_b,1-r_b)`, `Q_P=sum_b q_b`.

If necessary multiply by anchor characters so the transformed anchor bits have means `q_b<=1/2`; this leaves every nonanchor bit and all entropy quantities unchanged. Restrict all coordinates of `A`; the final Boolean children live on the anchor quotient. Recenter each final child only after the restrictions are complete.

Let

`D_P := J(f)-E_z J(g_z)`                              (1.4)

be the actual original-root folded-influence drop. It is this `D_P`, not the influence of an unpriced new basis, that is spendable in a global tree.

## 2. PROVED: exact affine crossing-amplified drop

For final restriction label `z`, let `u_b(z)` be the raw influence of quotient anchor `b` in the parent-centered orientation of (1.3). Influence martingality gives

`E_z u_b(z)=q_b`.

Define the posterior-majority crossing refund

`c_b(P)=E_z (2u_b(z)-1)_+`,
`C_P=sum_b c_b(P)`.                                    (2.1)

Because

`min(u,1-u)=u-(2u-1)_+`,

we obtain

`E_z J(g_z)=sum_b [q_b-c_b(P)] = Q_P-C_P`.            (2.2)

Therefore

`boxed: D_P = J-Q_P+C_P`.                             (2.3)

In particular

`D_P >= J-Q_P >=0`,  `0<=C_P<=Q_P`.                   (2.4)

This is strictly sharper than the previous lower bound `D_P>=J-Q_P`: posterior threshold crossings increase the SAME globally telescoping original-coordinate budget rather than forming a separate heuristic credit.

### Proof scope

Equation (2.2) is the account01/account04 folded-influence drift applied after the genuine invertible change (1.2), with all transformed nonanchors physically restricted. The nonanchor transformed influences are exactly the original `p_i`; no transformed-coordinate cost is dropped. Rewriting the expected final folded influence in the original parent ledger gives (2.3). QED.

## 3. Sequential realization of the SAME affine coalescence

Fix an order `a_1,...,a_r` of `A`. Execute the restrictions one coordinate at a time in the transformed basis (1.2), without branch-dependent character recentering until all of `A` has been removed. This produces exactly the same final leaves as the simultaneous block restriction.

At stage `s`, for a previous restriction history `z_<s`, let `f_{z_<s}` be the current Boolean descendant. The exact singleton entropy decomposition is

`Delta_s H(z_<s) = B_s(z_<s)+JS_s(z_<s)`,             (3.1)

where `B_s` is the spectral erasure of the current splitter bit and `JS_s` is the coherent recombination information for that split.

Set

`B_seq(P,pi) = sum_s E_{z_<s} B_s(z_<s)`,
`JS_seq(P,pi)= sum_s E_{z_<s} JS_s(z_<s)`.             (3.2)

Telescoping the genuine sequential restrictions gives

`Delta_P H = B_seq+JS_seq`.                            (3.3)

For the simultaneous affine block, write

`B_P = H(X|Y)`,
`Delta_P H=B_P+JS_P`.                                  (3.4)

Here `Y=(Y_b)_b` is the parity-hash label from (1.3).

## 4. PROVED: projection/recombination refund

### Theorem 4.1

For every Boolean `f`, every bucket partition `P`, every choice of anchors, and every order `pi` of the nonanchors,

`boxed: JS_seq >= JS_P`,                               (4.1)

hence

`boxed: B_seq <= B_P = H(X|Y)`.                        (4.2)

Moreover the difference is exact:

`R_proj(P,pi):=B_P-B_seq=JS_seq-JS_P >=0`.             (4.3)

### Proof

Let `Z=(Z_1,...,Z_r)` be the uniform restriction labels and let `T` denote the final quotient spectral label sampled from the final child spectrum. The simultaneous recombination term is

`JS_P=I(Z;T)=sum_s I(Z_s;T | Z_<s)`.                  (4.4)

For a fixed history `Z_<s`, let `T_s` be the immediate child spectral label after the `s`-th split, before later coordinates are removed. After averaging the future restriction labels, the conditional law of `T` is the projection of the immediate child squared-spectrum law onto the final surviving coordinates: the future sign average kills the cross terms. Thus, conditionally on the history, the channel from the immediate spectral label to the final label is a data-processing step, so

`I(Z_s;T | Z_<s) <= I(Z_s;T_s | Z_<s)`.               (4.5)

The right side is exactly the stagewise `JS_s`, averaged over the history. Sum (4.5) over `s` to obtain (4.1). Equations (3.3)--(3.4) then give (4.2)--(4.3). QED.

**Interpretation.** The one-shot hash erasure in the previous report discarded a nonnegative information credit created when later restrictions project away part of the immediate recombination label. Sequential execution recovers that credit exactly.

## 5. PROVED: root-potential cap for the entire sequential recombination bill

The inherited singleton strong-concavity bound gives, at every stage and history,

`JS_s(z_<s) <= j(P_s(z_<s))`,                          (5.1)

where `P_s(z_<s)` is the current influence of the splitter. Under restrictions of other transformed coordinates, splitter influence is a martingale. Since `j` is symmetric and concave,

`E_{z_<s} j(P_s(z_<s)) <= j(E P_s)=j(p_{a_s})`.        (5.2)

The transformed nonanchor influence `p_{a_s}` is exactly its original physical influence. Therefore

`boxed: JS_seq <= sum_{i in A} j(p_i) = Phi-M_P`.      (5.3)

Combining (3.3) and (5.3),

`boxed: Delta_P H <= B_seq + Phi-M_P`.                 (5.4)

This is the first useful replacement of the previous one-shot upper charge by a quantity that can be strictly smaller while retaining the same actual affine leaves and the same original-coordinate drop `D_P`.

For corrected entropy `E=H-Phi`, with the final child potential evaluated after recentering,

`Delta_P E
 <= B_seq-M_P+E_z Phi(g_z)
 <= B_seq-M_P+c_* E_z J(g_z)`.                         (5.5)

Using (2.2)--(2.3),

`boxed: Delta_P E <= B_seq-M_P+c_*(Q_P-C_P)
                    = B_seq-M_P+c_*(J-D_P)`.           (5.6)

Thus posterior crossings improve BOTH sides of the local ledger: they enlarge the spendable denominator `D_P` and reduce the surviving potential surcharge.

## 6. Shell-poor cores: all non-erasure terms are now explicitly paid

The preceding B14 random-colour coalescence theorem says that for a centered node with first-shell fraction

`r_c = Pr(|X|=1)/J`,

an `m`-colour partition exists with

`J-Q_P >= (1-r_c)J/m`.                                (6.1)

For `m=2` put

`delta=(1-r_c)/2`.                                     (6.2)

Then the SAME genuine affine partition obeys

`D_P >= delta J`.                                      (6.3)

Consequently (5.6), dropping the favorable `-M_P`, gives

`Delta_P E <= B_seq + c_* ((1-delta)/delta) D_P`.      (6.4)

At the inherited current hard-core calibration

`r_c < 0.3156061323581677`,

we have

`delta > 0.34219693382091615`,

and therefore

`c_* (1-delta)/delta < 5.546567649579054`.             (6.5)

Equivalently, for plain entropy, (5.4) and `Phi<=c_*J` imply

`Delta_P H <= B_seq + (c_*/delta)D_P`,                 (6.6)

with

`c_*/delta < 8.431957731356981`.                       (6.7)

So after sequentialization, every term OTHER THAN `B_seq` has a dimension-free payment on the shell-poor affine step. The remaining obstacle is no longer the full sign-free hash erasure `H(X|Y)`.

## 7. A conditional universal compiler with an explicit residual

Choose a hybrid physical/affine descendant maximizing `H/J` and then of minimum dimension. It is in particular physical-restriction critical, so the inherited centered-shell localization applies; it is also critical for each allowed affine coalescence because all affine children lie in the same descendant closure.

Let its ratio be `R=H/J`. For every allowed affine first step,

`Delta_P H >= R D_P`.                                  (7.1)

Suppose there is a dimension-independent constant `L` such that every shell-poor critical core with `r_c<=r_0` admits a two-colour partition and an ordering for which

`B_seq(P,pi) <= L D_P`.                                (7.2)

If `delta_0=(1-r_0)/2`, then (6.6) and (7.1) give

`R <= L + c_*/delta_0`.                                (7.3)

At `r_0=0.3156061323581677`,

`R <= L + 8.431957731356981`.                          (7.4)

The earlier centered selector already localizes any sufficiently high-ratio obstruction into this shell-poor regime. Hence proving (7.2) for the selected minimal hybrid-critical core would give an actual finite universal FEI bound after taking the maximum with the already-controlled lower-ratio regime.

This is an exact new implication toward full FEI. It preserves the EXISTENTIAL selector: no claim is made for every prescribed coordinate, every partition, or every ordering.

## 8. Why the previous residual was too strong, and why the new one is different

The one-shot target

`H(X|Y) <= L D_P`                                      (8.1)

for a fixed number `m` of quotient bits is already essentially FEI-hard under tensor replication. Indeed, for any centered Boolean `f` and its `t`-fold disjoint tensor power,

`H(f^{otimes t})=tH(f)`, `J(f^{otimes t})=tJ(f)`.

For ANY `m`-bucket parity hash `Y`,

`H(X^{(t)}|Y) >= tH(f)-m`,                             (8.2)

because `H(Y)<=m`, while every genuine folded drop satisfies

`D_P <= tJ(f)`.                                        (8.3)

If (8.1) held uniformly for a fixed `m`, even allowing the partition to depend on `t`, then

`tH(f)-m <= L tJ(f)`;

letting `t->infinity` would itself prove `H(f)<=LJ(f)`. Thus the old sign-free hash-erasure target was not a simpler auxiliary lemma; tensor replication exposes that circularity.

The new residual `B_seq` escapes this exact no-go because

`B_seq = H(X|Y)-R_proj`,                               (8.4)

and `R_proj` is generated by the spectra of genuine intermediate Boolean restriction descendants. It depends on signed/coherent recombination information, not only on the initial probability law `mu`. The next theorem should therefore spend or lower-bound this projection refund (or directly upper-bound `B_seq`) with a nonreused restriction budget. This is materially different from retrying a sign-free parity-profile inequality, a global phase/rank/l1 optimization, or a pointwise every-coordinate payment.

## 9. Diagnostic computation

A native floating diagnostic was run on:

- every nonconstant Boolean truth table through dimension three, over every canonical surjective two-colouring; and
- a deterministic seed-1402 sample of 1000 dimension-four Boolean functions with one- or two-bucket coalescences.

Total checked cases: `1776`.

Observed:

- maximum exact-identity residual: `2.220446049250313e-16`;
- maximum positive violation of `B_seq<=B_P`, `JS_seq<=Phi-M_P`, or (5.6): `0.0` at tolerance `5e-10`;
- strict projection refund `B_P-B_seq>5e-10` occurred in `897` cases;
- largest observed strict refund: `1.0487949406953985` bits.

This computation is diagnostic only. The theorem is the analytic proof above; sampled `n=4` behavior is not a certificate for all dimensions.

## 10. Current literature and novelty status

The May 29, 2026 González--MacManus--Pereyra work remains directly relevant: it develops restriction-decrement/stopping-tree criteria under which FEI compiles. Potapov's September 18, 2026 paper proves FEI for plateaued and partially bent classes, not universally. Neither source, as inspected in this run, supplies the sequential affine projection-refund theorem above or closes the universal conjecture. A bounded search failure is not novelty evidence, so priority is UNVERIFIED.

## 11. Genuine before/after and next exact obligation

**Before this run:** the strongest B14 affine step had a spendable shell-poor drop `D_P>=delta J` but paid corrected entropy only after leaving the one-shot sign-free quantity `H(X|Y)` as the residual.

**After this run:** the same realizable affine leaves have

`D_P=J-Q_P+C_P`,

and sequential execution replaces the residual by

`B_seq=H(X|Y)-R_proj`, `R_proj>=0`,

while all sequential recombination obeys the one-time root cap `JS_seq<=Phi-M_P`. At the inherited shell-poor calibration, the entire non-erasure overhead is at most `8.431957731356981 D_P` in the plain-entropy ledger, and crossings only improve it.

**Remaining universal obligation:** prove a dimension-independent existential bound `B_seq<=L D_P` (or an even stronger globally summable negative-credit version) for a suitable partition/order on the minimal hybrid-critical shell-poor core. This target must use genuine intermediate Boolean restriction structure. It must NOT revert to the refuted sign-free parity profile, global phase/rank/l1 optimization, a comparison of universal suprema misread pointwise, the false erasure constant four, or every-prescribed-coordinate payment.

**Full FEI remains OPEN / NOT PROVED.**
