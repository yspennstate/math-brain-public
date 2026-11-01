Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** The runtime exposes no authenticated applied-effort receipt.

# P13 / T02 — minimal terminal-output automaton at width six and reset-anchored k=78 transfer

## 0. Before / after, separated by level

### Source-level binary Chvátal–Sankoff interval

The target is
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every transition in this report uses one actual incoming `Y` bit across the entire strip column; independent Bernoulli matching is not substituted.

The previous P13 report carried the companion-derived source interval
\[
L\le\gamma_2\le U_{tail},\qquad
L=0.792665992=\frac{99083249}{125000000}.
\]
The newest completed P02 companion now visible on `master` is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T16-03-00Z__terminal-slack-minimization-dual-report.md`.

It proves, under P02's already-established actual-string covering transfer,
\[
\boxed{L\le\gamma_2\le U_{ts}<U_{tail}},
\]
with exact rational-logarithm separation
\[
U_{ts}<
0.8262759427622826250151065815372966328234619961931900238808061833125629444301
<U_{tail}.
\]
Thus the source-level certified repository interval strictly shrinks from `[L,U_tail]` to `[L,U_ts]`. This movement is **P02-derived**, not attributed to the width-six calculation below.

Fresh source navigation rechecked Alexander Tiskin, `arXiv:2212.01582v2`: the arXiv record still calls the binary coefficient unresolved; v2 was submitted 2024-08-13; and the comments explicitly say earlier claims concerning the process and `gamma` turned out to be incorrect and were omitted. The public lower endpoint retained here is the Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer bound `0.792665992` from `arXiv:2407.10925`.

### P13 mechanism-level movement

The preceding P13 run proved the leading-one shield bisimulation and obtained the exact `k=63` terminal-event interval
\[
I_{63}\approx[0.7787335500510791363,\ 0.7806329454947566650]
\]
for `gamma_6`, with width
\[
0.00189939544367752865799\ldots.
\]
It proposed further output-preserving automaton reduction, while recording the previous adversarial-suffix relaxation failure.

This run obtains two substantive results.

1. **Decisive obstruction / completed Moore route.** Exact output-preserving Moore refinement on the recurrent width-six chain stabilizes with exactly `4,484,525` classes, the same number as the explicit shield quotient. Therefore the shield quotient is already the **minimal deterministic terminal-output automaton** on the width-six recurrent class. There is no further exact Moore/bisimulation compression of `g_m` at this width.

2. **Immediate materially different route: reset-anchored transfer.** After closing the Moore route, the run switches to a regeneration/synchronizer argument. First, one more exact dependent event step gives a strictly nested `k=64` interval. Then all length-14 words containing any of the 970 previously proved reset patterns are used as common-state anchors. This produces an explicit `k=78`-level uniform event bracket without propagating a 156-bit vector over all `4,484,525` quotient states. The resulting certified `gamma_6` interval is
\[
\boxed{
\frac{71140531402459326477028245651161163596004151414}
{91343852333181432387730302044767688728495783936}
\le\gamma_6\le
\frac{71300161991984164266309518834217064763439765574}
{91343852333181432387730302044767688728495783936}
}
\]
that is
\[
\boxed{
0.77882122973060686756905198877691798\ldots
\le\gamma_6\le
0.78056880863654765213536675265396758\ldots
}.
\]
Its exact width is
\[
\boxed{
\frac{159630589524837789281273183055901167435614160}
{91343852333181432387730302044767688728495783936}
}
=0.00174757890594078456631\ldots.
\]
This is a strict `7.992887...%` width reduction from `I_63` (old/new factor `1.0868724938...`).

Status: **PARTIAL / source OPEN / exact internal theorem and computation pending later independent review.**

## 1. Scope, continuity, handoff, exclusions

Controlling owner policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns P13 to the dependence-preserving boundary-recursion route and P02 to the complementary stationary/variational upper route.

Necessary continuity only was read: the latest P13 report, the newest completed P02 companion report, the governing policy, root `POSTED.md`, the relevant exact checker dependency, and the current Tiskin/lower-bound sources. No whole-repository reread was performed. Root `POSTED.md` contains no T02 posting exclusion.

Short actual pre-LIVE20 P13 successor handoff is preserved: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation `tau(infinity)` could not be frozen source-faithfully. Retired I0051/clade work remains retired and was not reopened.

No email, Drive, public posting, paid compute, workflow, permission, peer-history, historical-claim, or schedule change was made.

## 2. Genuine dependent boundary recursion

Fix half-width `w`, put `m=2w`, and write a formal strip state
\[
s=(x_1,\ldots,x_m;g_1,\ldots,g_m),\qquad x_i,g_i\in\{0,1\}.
\]
For one fresh **actual source pair** `(u,v)`, define the shared-column carry
\[
d_0^{(v)}=0,
\qquad
d_i^{(v)}=(1-g_i)\left(d_{i-1}^{(v)}\vee {\bf1}_{\{x_i=v\}}\right).
\tag{2.1}
\]
The same incoming `v` appears at every site in the column. The update is
\[
g'_i=g_{i+1}+d_{i+1}^{(v)}-d_i^{(v)},\quad 1\le i<m,
\tag{2.2}
\]
\[
g'_m=(1-d_m^{(v)}){\bf1}_{\{u=v\}},
\tag{2.3}
\]
\[
x'=(x_2,\ldots,x_m,u),
\tag{2.4}
\]
and the central reward is
\[
\rho(s;u,v)=g_{w+1}+d_{w+1}^{(v)}.
\tag{2.5}
\]
Let `T_a` be one of the four deterministic source-pair transitions and `P=\frac14\sum_aT_a` the Markov operator.

The inherited pointwise coboundary is
\[
\boxed{\rho+P\phi-\phi=1-g_m},
\qquad
\phi=\sum_{i=w+1}^{m-1}g_i+2g_m.
\tag{2.6}
\]
Transporting it gives, for every `k>=0`,
\[
\boxed{\rho+P\phi^{[k]}-\phi^{[k]}=1-P^kg_m},
\qquad
\phi^{[k]}=\phi+\sum_{j=0}^{k-1}P^j(1-g_m).
\tag{2.7}
\]
Therefore any uniform bounds
\[
a\le P^kg_m\le b
\tag{2.8}
\]
imply the exact asymptotic transfer
\[
\boxed{1-b\le\gamma_w\le1-a}.
\tag{2.9}
\]
This is the bridge that prevents finite event enumeration from being mislabeled as an asymptotic bound by itself.

The same identity gives a finite-reward error bound. If `A_N(s)=E_sR_N/N` and `epsilon=b-a`, then
\[
\boxed{
A_N(s)-\epsilon-\frac{\phi^{[k]}(s)-\min\phi^{[k]}}N
\le\gamma_w\le
A_N(s)+\epsilon+\frac{\max\phi^{[k]}-\phi^{[k]}(s)}N.
}
\tag{2.10}
\]
At the corresponding potential minimizer/maximizer the relevant one-sided `1/N` term vanishes.

## 3. Exact obstruction theorem: the shield quotient is Moore-minimal on `R_6`

The preceding run proved the all-width shield canonicalization `C`: if the gradient starts with `ell` ones, zero the first `ell` raw `X` bits. It proved
\[
g_m(C(s))=g_m(s),\qquad C(T_as)=C(T_aC(s))
\tag{3.1}
\]
for every source letter `a`. Hence each shield class is contained in a terminal-output Moore-equivalence class.

For `w=6`, the unique recurrent class has
\[
|R_6|=5,735,086,
\]
and the shield quotient has
\[
|C(R_6)|=4,484,525.
\]

Now start Moore refinement with the output partition `Pi_0` according to `g_m`. Given `Pi_r`, define `Pi_{r+1}` by the exact signature
\[
\left(g_m(s),[T_0s]_{\Pi_r},[T_1s]_{\Pi_r},[T_2s]_{\Pi_r},[T_3s]_{\Pi_r}\right).
\tag{3.2}
\]
Two states are in the same stable block iff they have the same terminal-output trace for every finite input word; the stable partition is therefore the minimal deterministic Moore quotient for this output.

The exact checker obtains block counts
\[
2,4,23,274,4361,69897,457292,1080045,\ldots,
4484457,4484525,4484525.
\]
The partition reaches `4,484,525` blocks at round 20 and is unchanged at round 21. Since the shield bisimulation already provides a quotient with exactly `4,484,525` classes, the stable Moore quotient and the shield quotient have the same size. Consequently
\[
\boxed{\text{the width-six shield quotient is Moore-minimal for terminal output }g_m.}
\tag{3.3}
\]

This is a decisive obstruction: exact output-preserving partition refinement cannot further reduce the width-six event state space. The run therefore did not spend another cycle polishing Moore refinement; it switched immediately to the regeneration argument below.

## 4. One more exact event step: `I_64 subsetneq I_63`

Define the integer event count
\[
F_k(s)=4^kP^kg_m(s),
\qquad
F_{k+1}(s)=\sum_{a=1}^4F_k(T_as).
\tag{4.1}
\]
The checker propagates (4.1) on the exact shield quotient using integer arithmetic. At `k=64`,
\[
4^{64}=340282366920938463463374607431768211456,
\]
\[
F_{64}^{\min}=74668564626402241482881701527782212316,
\]
\[
F_{64}^{\max}=75263238098543308898864996100588186436.
\]
Thus
\[
I_{64}=\left[
\frac{265019128822395154564509611331180025020}{4^{64}},
\frac{265613802294536221980492905903985999140}{4^{64}}
\right]
\tag{4.2}
\]
for `gamma_6`, numerically
\[
I_{64}\approx[0.77882122197642394165,\ 0.78056881024413819095].
\]
Its width is
\[
0.00174758826771424929480\ldots.
\]

Both endpoints move inward strictly from `I_63`. Exact common-denominator slacks are
\[
4F_{63}^{\max}-F_{64}^{\max}
=29833210268846166942781368247147068>0,
\tag{4.3}
\]
\[
F_{64}^{\min}-4F_{63}^{\min}
=21824094883521931257537374012506608>0.
\tag{4.4}
\]
So `I_64 subsetneq I_63`; its width is `7.992394...%` smaller.

## 5. New theorem: reset-superword anchored transfer

The point of this step is to move past the direct `unsigned __int128` event horizon by a mathematically different mechanism.

### Lemma 5.1 — anchored synchronizer block

Let `f` be any real function on a finite Markov state space with
\[
a\le f\le b.
\]
Let `W` be a set of source words of a fixed length `L` such that every `q in W` is a synchronizing word: `T_qs=z_q` is independent of the starting state `s` (the common image may depend on `q`). Put
\[
A_W=\sum_{q\in W}f(z_q).
\]
Then for every starting state,
\[
\boxed{
\frac{A_W+(4^L-|W|)a}{4^L}
\le P^Lf(s)\le
\frac{A_W+(4^L-|W|)b}{4^L}.
}
\tag{5.1}
\]
In particular,
\[
\boxed{\operatorname{span}(P^Lf)\le
\left(1-\frac{|W|}{4^L}\right)(b-a).}
\tag{5.2}
\]

**Proof.** Expand `4^LP^Lf(s)` as the sum of `f(T_qs)` over all `4^L` actual source-pair words. For `q in W`, `T_qs=z_q`, so those contributions equal the state-independent sum `A_W`. Every remaining summand lies in `[a,b]`. This gives (5.1), and subtraction gives (5.2). QED.

No independence between cells is used: `q` is a word in actual source pairs and each `T_q` is the composition of the shared-`Y` column transitions (2.1)--(2.4).

### Width-six application

The previously proved width-six reset language has 970 minimal patterns:

- 2 of length 12,
- 66 of length 13,
- 902 of length 14.

Take **all distinct length-14 words containing at least one of these proved reset patterns anywhere**. Each such word is itself synchronizing. The exact set union has
\[
\boxed{|W_{14}|=1438}.
\tag{5.3}
\]
For `f=P^{64}g_m`, the exact checker evaluates the common-image anchor sum through the `F_64` numerators:
\[
\boxed{
A_{64}=107520239445555964569850771306084143052674.
}
\tag{5.4}
\]
There are
\[
4^{14}-1438=268434018
\]
non-reset-superwords. Applying Lemma 5.1 with `a=F_64^min/4^64` and `b=F_64^max/4^64` yields uniform bounds on `P^{78}g_m`:
\[
\frac{20043690341197268121420783210550623965056018362}{2^{156}}
\le P^{78}g_m(s)\le
\frac{20203320930722105910702056393606525132491632522}{2^{156}}.
\tag{5.5}
\]
Combining (5.5) with the coboundary transfer (2.9) gives the `gamma_6` interval stated in Section 0.

The new event width is
\[
\varepsilon_{78}^{anchor}
=
\frac{159630589524837789281273183055901167435614160}{2^{156}}.
\tag{5.6}
\]
On the same denominator, the `I_64` width is
\[
159631444665290728136217367033496862426398720,
\]
so the strict improvement numerator is
\[
\boxed{855140452938854944183977595694990784560>0.}
\tag{5.7}
\]
Equivalently, Lemma 5.1 contracts the `I_64` width by the exact factor
\[
1-\frac{1438}{4^{14}}
=1-0.000005356967449188232421875.
\tag{5.8}
\]
The numerical gain is deliberately reported as small but rigorous. Its value is methodological: it advances the exact certification beyond the direct 128-bit propagation horizon using only the already-proved synchronizer language and the `F_64` values on common images.

## 6. Finite-to-infinite error bound after the anchored step

Equation (5.5) supplies valid uniform `a,b` for `P^{78}g_m`. Insert these in (2.10), with `k=78`. Writing
\[
\epsilon_{78}=\frac{159630589524837789281273183055901167435614160}{2^{156}},
\]
we obtain for every starting state `s` and every finite horizon `N`,
\[
\boxed{
A_N(s)-\epsilon_{78}-
\frac{\phi^{[78]}(s)-\min\phi^{[78]}}N
\le\gamma_6\le
A_N(s)+\epsilon_{78}+
\frac{\max\phi^{[78]}-\phi^{[78]}(s)}N.
}
\tag{6.1}
\]
At a minimizer/maximizer of the transported potential, the corresponding one-sided `1/N` term is zero. Thus the finite computation has a proved finite-to-infinite transfer; it is not a standalone finite estimate being promoted to `gamma_2`.

Finally, `gamma_6<L`, so this P13 result by itself does **not** improve the source lower endpoint. The source-level shrink in Section 0 comes only from P02's complementary variational certificate.

## 7. Exact checker and executed output

Final exact checker:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T17-18-00Z__w6_moore_reset_anchor_checker.cpp`

creation commit `734d5be7291ca107a625fd049fbe3bce658644a9`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T17-18-00Z__w6_moore_reset_anchor_checker.out`

creation commit `60ed3d85fa1e83c58f19a575e81da5f8f4fea002`.

The final checker includes the current output bit explicitly in every Moore-refinement signature, verifies stabilization, performs exact integer event propagation, constructs the complete distinct length-14 reset-superword set, evaluates all anchor numerators exactly, checks the strict-width identity, and ends

`MOORE_MINIMAL_SHIELD_QUOTIENT_PASS`,
`RESET_SUPERWORD_ANCHOR_PASS`,
`ALL_EXACT_CHECKS_PASS`.

## 8. Failure / obstruction and next attack

**Closed route:** further exact Moore minimization at width six is impossible: the shield quotient is already minimal for the terminal observable. This turns the previous "try more output partition refinement" idea into a proved finite obstruction rather than another speculative optimization.

**Earlier failed route preserved:** the adversarial fresh-carry suffix relaxation was too loose; at retained suffix length 8 its lower envelope remained zero and its upper envelope stayed around `0.233` by step 50, above the source-relevant `1-L=0.207334008` threshold.

Because the Moore route closed with no further compression, this run immediately executed the different reset/regeneration route and obtained the strict interval contraction above. Thus the run is not a third unchanged pass over the same obstruction.

**Next attack:** use the reset language as a small exact interface rather than as a full-state reset-time bound. Compose the 4,291-state reset-avoidance prefix automaton with a **temporally feasible left-carry transducer** and only the trailing terminal-event suffix. On reset transitions, collapse immediately to the known common image; on non-reset transitions, retain only carry histories realizable by the shared source bits. The target is a width `w>=7` uniform bound
\[
\max_sP^kg_m(s)<1-L=0.207334008,
\]
which by (2.9) would finally give a source-valid lower improvement. If this composed avoidance/carry interface remains essentially as large as the full wider recurrent chain, the preserved distinct fallback is a regeneration separator with blockwise feasible-interface inequalities, not another Moore pass or the already-failed fresh-adversarial-carry relaxation.

## 9. ledger_delta

```yaml
ledger_delta:
  slot: P13
  parent: T02_BINARY_LCS
  source: "Chvatal-Sankoff gamma_2 for two independent iid uniform binary strings"
  model: "true source-pair strip; one shared incoming Y bit per column; NOT independent Bernoulli matching"
  status: PARTIAL
  source_status: OPEN
  source_before: "L <= gamma_2 <= U_tail"
  source_after: "L <= gamma_2 <= U_ts < U_tail"
  source_movement_owner: "P02 companion terminal-slack minimization dual"
  lower_endpoint: "L = 99083249/125000000 = 0.792665992"
  p13_before: "k=63 width-six event interval width 0.00189939544367752865799..."
  p13_after: "reset-anchored k=78 uniform event interval width 159630589524837789281273183055901167435614160 / 2^156"
  p13_after_decimal: "0.00174757890594078456631..."
  p13_width_reduction_vs_k63: "7.992887...%"
  theorem_1: "width-six shield quotient is the minimal deterministic Moore quotient for terminal output g_m"
  theorem_2: "reset-superword anchor lemma: span(P^L f) <= (1-|W|/4^L) span(f), with explicit anchored endpoints"
  exact_reset_superwords_L14: 1438
  obstruction: "no further exact output-preserving Moore compression at width six"
  prior_failed_route_preserved: "fresh-adversarial suffix carry envelope too loose"
  next_attack: "compose reset-avoidance DFA with temporally feasible left-carry interface and terminal suffix at w>=7"
  checker_commit: "734d5be7291ca107a625fd049fbe3bce658644a9"
  output_commit: "60ed3d85fa1e83c58f19a575e81da5f8f4fea002"
  runtime_model: "GPT-5.6 Sol"
  reasoning_level: "UNVERIFIED"
```
