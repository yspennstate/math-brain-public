Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort selector or receipt, so I do not claim otherwise.

# PROB10-02 / R17 — one-sided information debt, a source-valid Bellman transfer, and a no-free-peek obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every construction below is driven by the actual source bits of the two strings. No independent Bernoulli matching array is introduced.

**R17 source endpoint movement in this run: none.** Status remains **OPEN / PARTIAL**. The substantive progress is a new dependence-preserving finite-state lower-bound mechanism with a rigorous finite-to-infinite transfer, plus an exact obstruction explaining why the tempting cheaper `max/expectation` interchange is invalid unless exposed-but-unconsumed source information is retained.

## 0. Continuity, handoff, ownership, and the actual current metric

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

### 0.1 Actual R17 predecessor H0021 remains handed off

I reread `operations/claims/H0021.md`, current blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`. It still records

`UNASSIGNED (released by R17 under later owner refocus)`

and preserves the full R16/R17 history. In particular it preserves R17's substantive H0021 report

`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`

with navigation commit

`c8891869a1335d67bada83f23f63f2ce09603565`,

keeps the frozen H0021 metric `Delta_near=2`, keeps the R16 six-run historical stagnation and two consumed recoveries, and keeps R17's own H0021 unchanged streak equal to one with zero R17 recoveries consumed. No H0021 claim, counter, artifact, or failure count is edited or reset here.

### 0.2 Previous R17 LCS state and failed transfers

The newest completed R17 report before this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T0952Z_r17_recursive_bellman_congruence_b61e.md`

(blob `04226c67bc4dd182052fcc5494b51f195af89a92`). It proved an all-`ell` exact recursive Bellman congruence for the genuine binary finite-lookahead operator, with
\[
c_\ell=\frac{2\,4^{\ell-1}+3\,2^{\ell-1}+1}{3},
\qquad
c_{22}=2,932,033,104,555.
\]
Exact stable refinement found no further ordinary behavioral merger through `ell<=8`, and exact MTBDD compression of `T_ell^{29}0` through `ell=9` remained far too modest to make a dense `ell=22` witness plausible. These failures are retained; this run does **not** restart exact lumping or reset any no-movement count.

The older C049/C050 lower-side blocker also remains in force. In the public binary finite-lookahead normalization, beating the current public lower endpoint requires an exact source-valid increment
\[
\boxed{r>r_0:=\frac{99083249}{150916751}}
\tag{0.1}
\]
under `gamma=2r/(1+r)`. Dense `ell=22`, complement-only storage, complement/swap group quotienting, reversal symmetry, and generic MTBDD compression have already been tried or obstructed. This run therefore changes method **within LCS**, as required after repeated unchanged R17 source metrics.

### 0.3 Current ownership is nonduplicating

Current neighboring scopes recovered on master are:

- **P02**: finite covering/cone variational **upper** route;
- **P13**: genuine-source band/boundary recursion and lower-side finite-to-stationary transfer;
- **R17**: finite-lookahead Bellman structure. This run takes a new *information-state* route: reveal one extra source bit on one side, retain any unconsumed information exactly, and prove a source-valid block transfer.

No peer claim file is overwritten.

### 0.4 Actual current interval before this R17 mathematics

A newer P02 report was already present on current master and must be used rather than the older `U_*` baseline:

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T10-03-15Z__matched-successor-defect-report.md`

(blob `2596bca4d6d8b52b27b80626df09a3b0caaa7829`). It retains
\[
L=\frac{99083249}{125000000}=0.792665992.
\]
With
\[
p=256717,\quad q=800000,\quad d=q-p=543283,\quad t=p/q,\quad S=q^6d,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\quad
b=4220452010631561279,
\]
and
\[
D_{new}=515110016194946010524505039025520073185829,
\]
that report defines
\[
\beta_{new}=\frac ab-\frac{D_{new}}{2ab},
\qquad
\lambda_{new}=\frac{t^2}{S}\beta_{new},
\qquad
U_{new}=\frac{\log(4t^2)}{\log\lambda_{new}}.
\tag{0.2}
\]
Its exact positive-series logarithm certificate proves
\[
U_{new}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443029952.
\tag{0.3}
\]
Thus the exact metric entering and leaving this R17 run is
\[
\boxed{W=U_{new}-L.}
\tag{0.4}
\]
The decimal in (0.3) gives the rigorous separator
\[
W<0.03360995076228262501510658153729663282346199619319002388080618331256294443029952,
\]
but the tracked object is the symbolic exact expression (0.4), not a guessed decimal. P02's tiny endpoint improvement is companion-track progress and is **not** attributed to R17.

## 1. Fresh literature/status check

A bounded current search on 20 September 2026 remains consistent with the exact two-string binary coefficient being unresolved.

- Alexander Tiskin, `https://arxiv.org/abs/2212.01582v2`, last revised 13 August 2024, still treats the exact binary coefficient as unresolved. Its v2 comments explicitly say that earlier claims concerning the stochastic process and `gamma` turned out to be incorrect and were omitted. None of those withdrawn claims is used here.
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `https://arxiv.org/abs/2407.10925`, give the retained rigorous public lower bound `0.792665992` and describe exact Chvatal--Sankoff constants as open.
- Ray Li, William Ren and Yiran Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings*, first published online in 2026 by Cambridge, still present determination of the two-string binary constant as open and summarize the public bound history.
- Lueker's 2009 JACM upper bound `0.826280` remains the conventional published upper endpoint. The stronger P02 endpoint above is repository-internal and still pending the repository's independent-review / priority standard.

A fresh search also surfaced Lember--Sova (2026), *Extremal Alignments in LCS-Inference*. Its headline rate result concerns a related pairwise Markov/strongly-related-sequence setting and does not close the independent iid binary constant. No novelty claim for the information-debt construction below is made from this bounded search.

## 2. Idea fixed before code

Before writing the checker I persisted

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1012Z_r17_information_debt_idea_f2c4.md`

at commit `0a87497cde4086f31a0b12dd0dc4e7f58392d217`.

The three distinct attacks fixed there were:

1. prove or falsify a **no-free-peek** theorem: a nontrivial action based on an exposed but unconsumed source bit cannot forget that bit while preserving the iid projection;
2. repair the defect by an exact finite **boundary-information debt** state and derive a Bellman/source transfer;
3. test a completely different deterministic compression: opposite heads with a shorter leading run should supposedly tell us which side to skip. Preserve a minimal counterexample if false.

The rest of this report executes those three attacks.

## 3. Attack 1 — exact no-free-peek theorem

At a mismatch state, let `U,V` be fresh independent fair bits immediately beyond the currently visible windows. Suppose an algorithm reveals both bits and chooses action `A` (advance the first string) with probability
\[
p_{uv}\in[0,1],\qquad u,v\in\{0,1\}.
\]
If `A` is chosen, `U` is consumed into the shifted first window but `V` is **not** consumed. If `B` is chosen, `V` is consumed but `U` is not.

A tempting compressed process would now forget the unconsumed revealed bit and pretend that it is fresh fair input on a later step. The following shows exactly when that is legal.

### Theorem 3.1 — no nontrivial memoryless two-bit peek

Assume the post-action state records the consumed bit but records no information about the unconsumed revealed bit. If the unconsumed bit is required to remain fair conditional on the action and on the consumed bit, then all four action probabilities are equal:
\[
\boxed{p_{00}=p_{01}=p_{10}=p_{11}.}
\tag{3.1}
\]
Thus the action cannot depend nontrivially on the revealed pair.

#### Proof

Conditional on `U=u`, action `A` must not bias the unconsumed bit `V`. Since `V` is initially fair, this requires
\[
p_{u0}=p_{u1},\qquad u=0,1.
\tag{3.2}
\]
Likewise, conditional on `V=v`, action `B` must not bias the unconsumed `U`. Since `P(B|u,v)=1-p_{uv}`, this requires
\[
1-p_{0v}=1-p_{1v},\qquad v=0,1.
\tag{3.3}
\]
Equation (3.2) makes each row constant; (3.3) makes the two rows equal columnwise. Hence every `p_{uv}` is the same. QED.

The one-sided specialization is even sharper. If only `U` is revealed and action `B` can be chosen after seeing it, then forgetting `U` while treating it as fair later requires
\[
1-p_0=1-p_1,
\]
so `p_0=p_1`. Therefore **any useful one-sided peek that sometimes leaves `U` unconsumed must retain information about `U` in the state**.

This isolates the exact dependence error in the naive operator
\[
\mathbf E_{U,V}\max\{h(\sigma_Ua,b),h(a,\sigma_Vb)\}.
\]
It pointwise dominates the ordinary mismatch update, but iterating it as if both unused bits were fresh silently changes the source law. This run does not make that invalid interchange.

The exact checker exhausts all sixteen deterministic rules `p:{0,1}^2->{0,1}`. The only rules satisfying the freshness equations are the two constants, masks `0` and `15`. That finite check is a regression test; Theorem 3.1 is the proof for arbitrary randomized `p_{uv}`.

## 4. Attack 2 — exact one-sided information-debt process

The obstruction suggests the minimal repair: expose only one additional bit and, if it is not consumed, carry its value forward as a debt state.

Fix a window length `ell>=1`. Write the visible windows as
\[
a=a_1\cdots a_\ell,\qquad b=b_1\cdots b_\ell,
\]
and let
\[
\sigma_u(a)=a_2\cdots a_\ell u.
\]
The information status is one of
\[
N,\quad A_0,\quad A_1.
\]
`N` means no source bit beyond the visible windows has been exposed. `A_u` means the next first-string bit beyond the window has already been exposed and equals `u`, but has not yet been consumed. No further first-string bit is revealed while such a debt is outstanding.

This gives exactly
\[
\boxed{3\,4^\ell}
\tag{4.1}
\]
formal states, versus `4^(ell+1)=4*4^ell` raw states for full two-sided `(ell+1)`-lookahead. At `ell=21` the raw counts are `13,194,139,533,312` versus `17,592,186,044,416`. This is only a raw-state comparison: the previous R17 recursive quotient for full lookahead is much smaller than the raw space, so (4.1) is **not** claimed by itself to make the next endpoint computation feasible.

### 4.1 Exact Bellman operator

Let `h(a,b,s)` be a real potential. Define `F_ell h` as follows.

If `s=N` and `a_1=b_1`, the policy takes the matching heads, earns one reward, consumes both, and refills with fresh actual source bits:
\[
(F_\ell h)(a,b,N)
=1+\frac14\sum_{u,v}h(\sigma_u a,\sigma_v b,N).
\tag{4.2}
\]

If `s=N` and `a_1\ne b_1`, the ordinary no-peek actions have values
\[
A_0=\frac12\sum_u h(\sigma_u a,b,N),
\qquad
B_0=\frac12\sum_v h(a,\sigma_v b,N).
\tag{4.3}
\]
The new action first reveals only the next first-string bit `u`. After seeing `u`, it may either consume the first head, which clears the exposure, or consume the second head, in which case the revealed `u` remains outstanding as debt `A_u`. Hence
\[
P_A=rac12\sum_{u\in\{0,1\}}
\max\left\{
 h(\sigma_u a,b,N),
 \frac12\sum_v h(a,\sigma_v b,A_u)
\right\}.
\tag{4.4}
\]
Set
\[
(F_\ell h)(a,b,N)=\max\{A_0,B_0,P_A\}.
\tag{4.5}
\]

If `s=A_u` and the heads match, the already exposed first-string bit is consumed when both heads advance, while only the second side receives a fresh refill:
\[
(F_\ell h)(a,b,A_u)
=1+\frac12\sum_v h(\sigma_u a,\sigma_v b,N).
\tag{4.6}
\]
If the heads mismatch,
\[
(F_\ell h)(a,b,A_u)=
\max\left\{
 h(\sigma_u a,b,N),
 \frac12\sum_v h(a,\sigma_v b,A_u)
\right\}.
\tag{4.7}
\]

### Lemma 4.1 — exact source realization

Equations (4.2)--(4.7) are the Bellman equations of a causal policy on two genuine independent iid binary source strings.

#### Proof

Maintain consumed indices `(i,j)`. In state `N`, the windows are exactly the currently exposed unconsumed strings `X_{i+1}^{i+ell}` and `Y_{j+1}^{j+ell}` and no bit beyond them has been queried. Formula (4.2) queries one new bit from each independent tail. Formula (4.3) queries only the refill bit of the side actually advanced. In the peek action (4.4), query `U=X_{i+ell+1}` first. If the first side advances, `U` becomes its new last visible bit and there is no debt. If the second side advances, query only its fresh refill `V=Y_{j+ell+1}`, and retain the unconsumed value `U` explicitly as `A_U`. While in `A_u`, formulas (4.6)--(4.7) never query a new first-string bit until the recorded `u` is consumed. Every other queried bit is a previously unqueried source coordinate, hence remains fair and independent by deferred decisions. Induction on decision time proves the stated state semantics and transition probabilities. QED.

This is exactly the dependence bookkeeping absent from the invalid free-peek operator.

### 4.2 Bellman subsolutions give finite-horizon reward guarantees

Suppose a finite potential `h` and scalar `rho` satisfy
\[
\boxed{F_\ell h\ge h+\rho\mathbf1.}
\tag{4.8}
\]
At each state choose an action attaining the relevant maximum, including the inner choice after observing `u` in (4.4). Let `R_N` be the number of matched-head rewards earned in `N` alignment decisions. Then for every starting state `s`,
\[
\mathbf E_s R_N
\ge N\rho+h(s)-\mathbf E_s h(S_N)
\ge N\rho-\operatorname{osc}(h).
\tag{4.9}
\]
This is the standard telescoping proof applied to the exact source process of Lemma 4.1; no stationarity or simulation is needed.

### Theorem 4.2 — dependence-preserving finite-to-infinite block transfer

Every exact subsolution (4.8) yields the original-source lower bound
\[
\boxed{
\gamma_2\ge \frac{2\rho}{1+\rho}.
}
\tag{4.10}
\]

#### Proof

Fix a horizon `N`. Run the policy from (4.8) for exactly `N` alignment decisions on fresh source tails. Let `I_N,J_N` be the numbers of first- and second-string symbols consumed and `R_N` the number of matches taken. Every decision is either one match consuming two symbols and earning one reward, or one skip consuming one symbol and earning zero. Therefore pathwise
\[
I_N+J_N=N+R_N.
\tag{4.11}
\]
The process ever inspects at most `ell+1` positions beyond the consumed index on either source. Put `K=ell+1`. After a block ends, discard all source positions through `I_N+K` and `J_N+K`. By the deferred-decisions construction in Lemma 4.1, no position after those cut points has been inspected, so the two remaining tails are again independent iid fair strings conditional on the entire block history.

Now alternate two independent block types on successive fresh tails: an `A`-oriented block governed by `F_ell`, followed by its string-swapped `B`-oriented copy. If `(R,I,J)` is the first block vector and `(R',I',J')` is an independent copy before swapping, then one pair of blocks uses
\[
I+J'+2K
\]
first-string positions and
\[
J+I'+2K
\]
second-string positions, and creates `R+R'` matched symbols. Both side-length expectations are therefore
\[
\mu=N+\mathbf E R_N+2K
\tag{4.12}
\]
by (4.11), while expected matched reward per pair is `2 E R_N`.

Pairs are iid because each begins beyond every coordinate exposed by the previous pair. By the strong law (equivalently, repeated deferred decisions plus the ordinary iid law), after `M` pairs both used source lengths divided by `M` converge to `mu`, and the concatenated matched subsequence length divided by `M` converges to `2 E R_N`. For any fixed `delta>0`, with probability tending to one all paired blocks fit inside two deterministic prefixes of length `ceil((1+delta)M mu)` and their concatenated matches have length at least `(2 E R_N-delta)M`. Hence
\[
\gamma_2\ge
\frac{2\mathbf E R_N}{N+\mathbf E R_N+2K}.
\tag{4.13}
\]
The right side is increasing in `E R_N`. With `C=osc(h)`, (4.9) gives, for large `N`,
\[
\gamma_2\ge
\frac{2(N\rho-C)}{N+(N\rho-C)+2K}.
\tag{4.14}
\]
Let `N->infinity`; `K` and `C` are fixed because the Bellman state space is finite. This yields (4.10). QED.

The block-pair argument is useful because it does **not** assume that an oriented policy has zero symbol-consumption drift. Its swapped copy cancels the drift in the law, while fresh-block separation costs only `O(ell/N)` and vanishes before the infinite-string limit.

This is the main mathematical advance of the run. It is a genuine finite-state stationary/Bellman characterization with a proved transfer to the original iid binary LCS problem. No novelty claim is made without a dedicated audit.

### 4.3 Exact finite certificates through `ell=6`

The checker iterates (4.2)--(4.7) with exact `Fraction` arithmetic. For `h=F_ell^{35}0` it computes the exact rational interval
\[
\rho^-_\ell=\min_s(F_\ell h-h)(s),
\qquad
\rho^+_\ell=\max_s(F_\ell h-h)(s).
\tag{4.15}
\]
The lower number is itself a rigorous Bellman subsolution certificate by construction, so Theorem 4.2 applies to `rho^-_ell`. Displayed decimals below are only renderings of exact rational arithmetic:

| `ell` | ordinary Bellman bracket | one-sided-debt bracket | transferred lower `2 rho^-/(1+rho^-)` |
|---:|:---|:---|:---|
|1|`[0.500000000000000, 0.500000000000000]`|`[0.571428571428571, 0.571428571428572]`|`0.727272727272727`|
|2|`[0.571428571428571, 0.571428571428572]`|`[0.597345132512862, 0.597345132823744]`|`0.747922437492452`|
|3|`[0.597345132310224, 0.597345132894401]`|`[0.610112434232757, 0.610112544403221]`|`0.757850720559754`|
|4|`[0.611053880372108, 0.611054069817020]`|`[0.618018575693627, 0.618021192055141]`|`0.763920247860800`|
|5|`[0.620015432793953, 0.620020161025781]`|`[0.624355243887918, 0.624378626800642]`|`0.768742239405113`|
|6|`[0.626343180528034, 0.626382009010169]`|`[0.629219567676884, 0.629339517063670]`|`0.772418377682626`|

At every displayed width the one-sided information state materially strengthens the finite mechanism over ordinary same-width lookahead. The checker explicitly asserts the strict separation through `ell<=5`; the exact `ell=6` output also lies above the same-width ordinary interval. But even the `ell=6` transferred lower certificate is far below
\[
L=0.792665992,
\]
so these finite computations **do not move the source endpoint** and are not counted as interval progress.

The important computational target is instead structural: at base lookahead `ell=21`, the debt process uses three raw information statuses instead of the four combinations of two fully exposed extra bits. Whether a certificate at that scale crosses (0.1) is completely unresolved. The previous recursive exact quotient remains a competing, and at present smaller, representation; no feasibility claim is made from the raw count alone.

## 5. Attack 3 — run-prefix dominance fails exactly

A very different attempted compression was to avoid extra source information entirely by making the mismatch action deterministic from leading-run lengths. The natural conjecture was:

> if the two heads disagree and the first leading run has length `i<j`, advancing the first (shorter-run) string is always weakly better for deterministic LCS continuation.

This is false.

The checker exhausts all equal-length binary pairs through length five and finds no counterexample there. At length six it finds
\[
A=010011,\qquad B=110100.
\]
The heads disagree, and the leading run lengths are
\[
i=1<2=j.
\]
Nevertheless exact dynamic programming gives
\[
LCS(A_2^6,B)=3,
\qquad
LCS(A,B_2^6)=4.
\tag{5.1}
\]
Thus advancing the **longer** leading-run side is strictly better in this state. This rules out the proposed universal run-length-only action collapse. The finite minimality statement here is only with respect to the exhaustive equal-length search through `n<=6`; no broader minimal-counterexample claim is needed.

## 6. Exact checker and archived output

Checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1031Z_r17_information_debt_exact_f2c4.py`

creation commit `8c394a0133b6a4135b8deb63e34e67d0bd4082e7`.

Archived stdout:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1031Z_r17_information_debt_exact_f2c4.out`

creation commit `bb36e73a78934ebfc359a1635221da7359ce6faa`.

The executed checker returns code zero and ends

`ALL_EXACT_CHECKS_PASS`

and `RETURN_CODE=0`.

It verifies:

1. among all 16 deterministic two-bit peek policies, only the two constant rules satisfy the exact memoryless freshness equations;
2. no shorter-run counterexample exists in the exhaustive search for equal lengths `2<=n<=5`, and the explicit length-six counterexample (5.1) is found;
3. exact rational ordinary and information-debt Bellman iterations through `ell=6`;
4. that the displayed `rho^-_ell` is a literal componentwise subsolution residual for the archived exact potential; and
5. that none of the transferred finite certificates beats the current source lower endpoint `L`.

The finite checks support the written proofs but do not replace Theorem 3.1, Lemma 4.1, or Theorem 4.2.

## 7. Source-level before/after versus mechanism progress

Because P02's 10:03 report is already part of the current master baseline, the source metric for this R17 run is
\[
L\le\gamma_2\le U_{new},
\qquad
W_{before}=U_{new}-L.
\]
After this R17 run,
\[
L\le\gamma_2\le U_{new},
\qquad
\boxed{W_{after}=W_{before}.}
\]
So **R17 source movement is zero**.

Mechanism progress is separate and substantive:

- a precise proof now rules out free adaptive peeking without state memory;
- a `3*4^ell` one-sided information-debt Bellman process preserves the exact source dependence;
- every exact debt-process Bellman subsolution now has a proved transfer `gamma_2 >= 2 rho/(1+rho)` by a drift-free paired-block argument;
- exact small-width certificates show that retaining one exposed bit strictly strengthens ordinary same-width lookahead;
- a deterministic leading-run collapse is ruled out by an exact counterexample.

This is a different method from the preceding exact-congruence / MTBDD run and stays entirely within PROB10-02.

## 8. Exact unresolved full-scope gap

The source problem remains open. This run does **not** determine `gamma_2`, beat `L`, or alter the current upper endpoint.

The most concrete new lower-side target is now:

\[
\boxed{
\text{find an exact subsolution of }F_{21}h\ge h+\rho\mathbf1
\text{ with }
\rho>\frac{99083249}{150916751}.
}
\tag{8.1}
\]
By Theorem 4.2 such a witness would immediately improve the rigorous lower endpoint for the genuine dependent binary strings. The full `F_21` raw state space is still enormous, so (8.1) requires a second structural step: a one-sided debt-specific quotient, local/separable potential, or exact separation oracle over mismatch states. The no-free-peek theorem says that simply deleting the debt information cannot be that step.

A complementary exact question is whether the one-sided debt operator admits a substantially coarser **one-sided Bellman inequality quotient** than the exact full-lookahead congruence. That is the recommended next R17 route. It is materially different from rerunning generic bisimulation: only a subsolution inequality must be preserved, and the debt automaton exposes exactly where source information enters.

The upper-side companion route remains P02's covering/cone dual and is not duplicated here.

No closure is claimed. Closure still requires a full source-matching proof, exact certificates for the finite computational core, current prior-art checking, and the repository's separately recorded independent-validation standard.

```yaml
ledger_delta:
  track: R17
  target: "PROB10-02 full binary Chvatal-Sankoff constant"
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  source_status: OPEN
  status: PARTIAL
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "U_new from P02 2026-09-20T10-03-15Z matched-successor-defect report"
  upper_after: "same U_new"
  metric_before: "U_new-L"
  metric_after: "U_new-L"
  source_movement: none
  mechanism_progress:
    - "proved no-free-peek theorem for forgotten unconsumed source bits"
    - "defined exact one-sided information-debt Bellman process with statuses N,A0,A1"
    - "proved block-pair finite-to-infinite transfer gamma_2 >= 2 rho/(1+rho) for every exact subsolution"
    - "exact rational Bellman checks through ell=6"
    - "exact run-prefix dominance counterexample at n=6"
  current_lower_metric_target: "rho > 99083249/150916751"
  h0021: "released/unassigned; history and Delta_near=2 preserved"
  closure: false
```

No schedule, cadence, enabled state, email, Drive item, public posting, workflow, purchase, permission, shared-root ledger, or peer claim file was modified.