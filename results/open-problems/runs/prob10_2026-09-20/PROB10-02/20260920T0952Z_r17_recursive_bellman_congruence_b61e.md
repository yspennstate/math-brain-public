Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but no authenticated applied-model / applied-effort selector or receipt is exposed here, so I do not claim otherwise. **NO R17 SOURCE-ENDPOINT MOVEMENT THIS RUN:** with the newest P02 exact candidate already present before this run, `W_before=W_after=U_*-L`, where `L=0.792665992` and `U_*` is defined exactly below. Status remains **OPEN / PARTIAL**. Three materially different attacks were made: **(1)** a recursive exact Bellman congruence for the genuine binary finite-lookahead operator (proved for all `ell`); **(2)** an exact attack on the possibility of further ordinary behavioral lumping (stable partition refinement agrees with the recursive quotient through `ell<=8`, finite evidence only); **(3)** certificate-specific exact MTBDD compression of `T_ell^29 0` under three variable orders through `ell=9` (real compression, but not remotely enough at the tested scales to claim an `ell=22` endpoint certificate).

# PROB10-02 / R17 — recursive Bellman congruence and a concrete symbolic-compression obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The same source bits are reused across the corresponding LCS rows/columns. No independent Bernoulli matching array appears anywhere in this report.

## 0. Continuity, H0021 handoff, ownership, and current source metric

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

The owner-required handoff of R17's actual pre-refocus successor H0021 remains intact. I reread `operations/claims/H0021.md`, current blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`. It says **UNASSIGNED / RELEASED BY R17**, preserves the R16 history and R17's report

`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`

at navigation commit

`c8891869a1335d67bada83f23f63f2ce09603565`,

and keeps the frozen H0021 metric `Delta_near=2`. No H0021 claim, artifact, counter, or recovery count is touched here.

Newest completed own R17 dependency before this run:

`runs/prob10_2026-09-20/PROB10-02/20260920T0837Z_r17_sharp_centered_path_span_a4d2.md`

(blob `5ed147f73654da435da33832ec33c2a8633e19ec`). It proves the sharp common-source strip reward-span theorem `|R_N(s)-R_N(t)|<=m` for strip length `m=2w` and a fixed-width finite-to-stationary error at most `m`; it does **not** move the full-source endpoint.

Current complementary ownership is nonduplicating:

- **P02**: finite covering/cone variational **upper** route;
- **P13**: dependence-preserving boundary/band-LCS **lower/transfer** route;
- **R17**: this run returns to the old exact finite-lookahead Bellman obstruction, but with a new non-group recursive quotient and a concrete exact decision-diagram test.

The newest P02 report recovered before this run is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T09-05-20Z__residue-optimal-defect-report.md`.

It retains
\[
L=\frac{99083249}{125000000}=0.792665992
\]
and defines its newest exact repository-internal upper candidate as follows. Put
\[
p=256717,\quad q=800000,\quad d=q-p=543283,\quad t=p/q,\quad S=q^6d,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\qquad
v_*=4927892157284473118,
\]
\[
\beta_*:=\frac ab-\frac1{2bv_*},
\qquad
\lambda_*:=\frac{t^2}{S}\beta_*,
\qquad
U_*:=\frac{\log(4t^2)}{\log\lambda_*}.
\]
Its exact positive-series logarithm certificate proves the strict separator
\[
U_*<0.82627594276228262501510658153729663282346199619319002388080618331256294443029953.
\]
A diagnostic high-precision evaluation (not the proof object) is
\[
U_*\approx0.8262759427622826250151065815372966328234619961931900238808061833125629444302995253556,
\]
so
\[
W:=U_*-L\approx0.0336099507622826250151065815372966328234619961931900238808061833125629444302995253556.
\]
The exact tracked quantity in this run is the symbolic `W=U_*-L`; I do not replace it by a rounded decimal.

The newest P13 report recovered is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T09-18-50Z__extremal-boundary-band-bracket.md`.

It proves a pathwise extremal-boundary bracket and identifies the lower extremal finite statistic with a genuine dependent band-LCS expectation. This run does not repeat that band recursion.

The old R17 lower-side obstruction is also preserved, not reset. C049/C050 showed that to beat `L` through the public binary finite-lookahead recurrence one needs an exact source-valid certificate at the next scale with increment
\[
\boxed{r>r_0:=\frac{99083249}{150916751}}
\tag{0.1}
\]
under the conversion `gamma=2r/(1+r)`. C049 found only the simultaneous-complement / string-swap group quotient; at `ell=22` it still has `4,398,048,608,256` orbits. The generic BDD/MTBDD suggestion was left as an untested representation idea. This run attacks exactly those two residual points and does not rerun the old dense table.

## 1. Fresh source/status check

A bounded current source check on 20 September 2026 remains consistent with the exact binary coefficient being unresolved.

- Alexander Tiskin, `https://arxiv.org/abs/2212.01582v2`, last revised 13 August 2024, still describes the coefficient as unresolved. The arXiv comments explicitly say that certain earlier claims about the stochastic process and `gamma` turned out to be incorrect and were omitted in v2. None of those removed claims is used here.
- Heineman–Miller–Reichman–Salls–Sárközy–Soiffer, `https://arxiv.org/abs/2407.10925`, is the source of the retained public lower bound `0.792665992` and implements the exact finite-lookahead lower-bound machinery through `ell=21`.
- Ray Li, William Ren and Yiran Wen, published online by Cambridge on 2 March 2026, still present determination of the two-string binary constant as open and summarize the public history of rigorous bounds.
- Lueker's 2009 JACM paper remains the source of the public `0.826280` upper bound and the finite-lookahead/finite-state methodology behind the lower recurrence used here.

Searches for `Chvatal-Sankoff symbolic Bellman BDD`, `Chvatal-Sankoff MTBDD`, and close variants did not surface a primary source applying the recursive congruence below. That negative search is **not** a novelty certificate. No novelty claim is made here without a dedicated literature audit.

## 2. Exact genuine-source finite-lookahead operator

Fix `ell>=1` and write a state as
\[
s=(a,b)\in\{0,1\}^{\ell}\times\{0,1\}^{\ell}.
\]
For `u in {0,1}`, let
\[
\sigma_u(a)=a_2a_3\cdots a_\ell u.
\]
The exact one-vector binary Shapley/Lueker operator recovered in C049 is
\[
(T_\ell h)(a,b)=
\begin{cases}
1+\dfrac14\displaystyle\sum_{u,v\in\{0,1\}}
 h(\sigma_u(a),\sigma_v(b)),&a_1=b_1,\\[3mm]
\max\left\{
\dfrac12\displaystyle\sum_u h(\sigma_u(a),b),
\dfrac12\displaystyle\sum_v h(a,\sigma_v(b))
\right\},&a_1\ne b_1.
\end{cases}
\tag{2.1}
\]
The appended `u,v` are fresh actual source bits. Equation (2.1) is therefore the genuine iid-string lookahead recurrence, not a cellwise independent match model.

Let `C` simultaneously complement both strings and `S` exchange them. They generate
\[
G_\ell=\{1,C,S,CS\}.
\]
C049 proved exact equivariance of (2.1) under `G_ell`. The new point is that matching heads admit a stronger **recursive** collapse that is not a group orbit.

## 3. Attack 1: a recursive Bellman congruence

### Definition 3.1

Define equivalence relations `~_ell` recursively. At length zero there is one class. For `ell>=1`:

1. a leading-match state is never equivalent to a leading-mismatch state;
2. if `a_1=b_1` and `a'_1=b'_1`, write
   \[
   a=c\alpha,\quad b=c\beta,\qquad
   a'=c'\alpha',\quad b'=c'\beta'.
   \]
   Then
   \[
   (a,b)\sim_\ell(a',b')
   \quad\Longleftrightarrow\quad
   (\alpha,\beta)\sim_{\ell-1}(\alpha',\beta');
   \tag{3.1}
   \]
3. if both states have unequal leading bits, then
   \[
   (a,b)\sim_\ell(a',b')
   \quad\Longleftrightarrow\quad
   (a',b')=g(a,b)\text{ for some }g\in G_\ell.
   \tag{3.2}
   \]

Thus matching heads are literally discarded; mismatch roots keep the old complement/exchange orbit.

### Lemma 3.2 — right-extension compatibility

If
\[
(\alpha,\beta)\sim_k(\alpha',\beta'),
\]
then the multisets
\[
\left\{[(\alpha u,\beta v)]_{\sim_{k+1}}:u,v\in\{0,1\}\right\}
\]
and
\[
\left\{[(\alpha'u,\beta'v)]_{\sim_{k+1}}:u,v\in\{0,1\}\right\}
\]
are equal.

#### Proof

Induct on `k`. The case `k=0` is immediate.

If `(alpha,beta)` is a mismatch-root pair, equivalence at level `k` means `(alpha',beta')=g(alpha,beta)` for `g in G_k`. Simultaneous complement extends by sending `(u,v)` to `(1-u,1-v)`; exchange extends by sending `(u,v)` to `(v,u)`; their composition combines those two relabellings. These are permutations of the four bit pairs. Since every resulting length-`k+1` state remains in the corresponding `G_(k+1)` orbit, the two extension multisets have identical `~_(k+1)` classes.

If `(alpha,beta)` is a match-root pair, write
\[
\alpha=c\eta,\quad\beta=c\theta,
\qquad
\alpha'=c'\eta',\quad\beta'=c'\theta'.
\]
By Definition 3.1,
\[
(\eta,\theta)\sim_{k-1}(\eta',\theta').
\]
Every extension `(alpha u,beta v)` is still a match-root length-`k+1` state, and Definition 3.1 identifies its class with the `~_k` class of `(eta u,theta v)`. The induction hypothesis applied one level lower says the four such tail classes have the same multiset for the primed and unprimed pairs. Hence the extension multisets agree. QED.

### Lemma 3.3 — group invariance

Each `~_ell` class is invariant under the action of `G_ell` in the sense that `s~_ell t` implies `g s~_ell g t` for every `g in G_ell`.

#### Proof

For mismatch roots this is immediate from (3.2). For match roots, complement and exchange preserve the match type and induce the corresponding complement/exchange action on the tails; induction on `ell` and (3.1) finish the proof. QED.

### Theorem 3.4 — exact Bellman congruence

If `h` is constant on `~_ell` classes, then `T_ell h` is also constant on `~_ell` classes.

#### Proof

Take equivalent states `s,t`.

If they are leading-match states, their immediate reward is one in both cases. By (3.1) their tail pairs are `~_(ell-1)`-equivalent, and Lemma 3.2 says the four equiprobable simultaneous-shift successors have exactly the same multiset of `~_ell` classes. Since `h` is class-constant, their four-term averages in (2.1) are equal.

If they are leading-mismatch states, (3.2) gives `t=g s` for some `g in G_ell`. Complement merely relabels appended bits, while exchange interchanges the two mismatch actions. Lemma 3.3 makes `h` invariant on every such transformed successor class. Consequently the unordered pair of the two action averages is the same at `s` and `t`, and therefore so is its maximum. QED.

### Corollary 3.5 — exact quotient certificates lift

Let `\bar T_ell` be the induced operator on the finite quotient `S_ell/~_ell`. If a rational quotient potential `\bar h` satisfies
\[
\bar T_\ell\bar h\ge \bar h+r\mathbf1,
\tag{3.3}
\]
then its lift `h=\bar h\circ q` satisfies
\[
T_\ell h\ge h+r\mathbf1
\]
on every one of the `4^ell` original source states. Hence this quotient is exact for Bellman subsolutions and value iteration. The usual finite-lookahead transfer may then be applied without inserting any stochastic independence not present in the source model.

This is the main mathematical result of the run.

## 4. Exact size of the recursive quotient

Let `c_ell` be the number of `~_ell` classes.

The leading-match classes are in bijection with the `c_(ell-1)` tail classes.

For leading-mismatch states, Definition 3.1 uses exactly `G_ell` orbits. Burnside's lemma applies to the mismatch set. Its size is `2^(2ell-1)`. On that set:

- the identity fixes all `2^(2ell-1)` states;
- simultaneous complement fixes none;
- exchange fixes none, because a mismatch state cannot have `a=b`;
- `CS` fixes exactly the `2^ell` states with `b=bar(a)`.

Therefore, for `ell>=2`, the number of mismatch classes is
\[
\frac{2^{2\ell-1}+2^\ell}{4}
=2^{2\ell-3}+2^{\ell-2}.
\tag{4.1}
\]
With `c_1=2`,
\[
\boxed{c_\ell=c_{\ell-1}+2^{2\ell-3}+2^{\ell-2}.}
\tag{4.2}
\]
Solving (4.2) gives
\[
\boxed{
 c_\ell=\frac{2\,4^{\ell-1}+3\,2^{\ell-1}+1}{3}.
}
\tag{4.3}
\]
At the metric-relevant next lookahead,
\[
4^{22}=17,592,186,044,416,
\]
while the old global complement/exchange quotient from C049 has
\[
4,398,048,608,256
\]
orbits. The new recursive exact quotient has
\[
\boxed{c_{22}=2,932,033,104,555.}
\tag{4.4}
\]
Thus the recursive theorem gains another asymptotic factor `3/2` over the old group quotient and a factor tending to `6` over the raw state space, but it **does not** by itself make a dense `ell=22` certificate feasible. Equation (4.1) diagnoses the bottleneck sharply: almost all surviving classes are mismatch-root classes, where this exact quotient intentionally retains the full complement/exchange orbit information.

No claim is made that (3.1)–(3.2) is the coarsest possible congruence for all `ell`.

## 5. Attack 2: exact finite coarsest-refinement test

To try to falsify the quotient as unnecessarily fine, I independently ran ordinary exact partition refinement. The initial partition records only match versus mismatch. A match-state signature is its multiset of four successor block IDs. A mismatch-state signature is the unordered pair of its two two-successor block-count signatures, reflecting the `max` symmetry between the actions. Refinement continues until stable.

The exact stable block-count sequences are:

| `ell` | refinement counts |
|---:|:---|
|1|`[2,2]`|
|2|`[2,5,5]`|
|3|`[2,5,15,15]`|
|4|`[2,5,15,51,51]`|
|5|`[2,5,15,51,187,187]`|
|6|`[2,5,15,51,187,715,715]`|
|7|`[2,5,15,51,187,715,2795,2795]`|
|8|`[2,5,15,51,187,715,2795,11051,11051]`|

For every `ell<=8`, the final partition agrees **exactly** with `~_ell`, not just in class count but by mutual refinement of all states.

This is useful obstruction evidence: at the exhaustively checked widths, plain probabilistic/control bisimulation finds no merger beyond Theorem 3.4. It is **not** extrapolated into a theorem that `~_ell` is coarsest at `ell=22`.

## 6. Attack 3: exact MTBDD compression of an actual Bellman iterate

The old C048/C049 handoff suggested BDD/MTBDD compression but had no exact test on the actual value array. I therefore computed
\[
h_{29}=T_\ell^{29}0
\]
with exact integer numerators over the common denominator
\[
4^{29}=288230376151711744.
\]
I then reduced the exact terminal array as an ordered algebraic decision diagram under three fixed variable orders.

The best of those three at every tested width is the forward interleaving
`a_1,b_1,a_2,b_2,...`. Its exact counts are:

| `ell` | raw states | distinct exact terminals | interleaved internal nodes | total MTBDD nodes |
|---:|---:|---:|---:|---:|
|4|256|30|135|165|
|5|1,024|92|516|608|
|6|4,096|298|1,851|2,149|
|7|16,384|1,018|6,750|7,768|
|8|65,536|3,521|24,574|28,095|
|9|262,144|12,639|90,926|103,565|

For comparison, at `ell=9` the all-`a`-then-`b` ordering has `105,536` total nodes and reverse interleaving has `143,385`.

These are exact counts for this particular iterate. They show that an actual Bellman value array is compressible, but only by a modest factor at the tested widths; the straightforward reduced ordered MTBDD is not displaying the orders-of-magnitude collapse needed to jump from `ell=21` to a compact `ell=22` certificate. I make **no asymptotic complexity inference** from six finite widths. A more specialized arithmetic/inequality diagram, policy-specific witness, or non-ordered representation could still behave very differently.

The `step=29` minimum increments are archived too, but none crosses the source threshold (0.1); they are not promoted to an endpoint.

## 7. Exact checker and execution

Idea note, fixed before repository persistence of the checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0944Z_r17_recursive_congruence_idea_b61e.md`

creation commit `e4361f5bbd96d429566f168de5ac3de9153e0bdd`.

Checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0944Z_r17_recursive_congruence_mtbdd_b61e.py`

creation commit `6432760b65bc777b4afd8b7e6df6e8ff75d7b278`.

Archived stdout:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0944Z_r17_recursive_congruence_mtbdd_b61e.out`

creation commit `49d194794c77b7647d0c1448949b0fea7884f032`.

The executed checker returns code zero and ends

`ALL_EXACT_CHECKS_PASS`

and `RETURN_CODE=0`.

The checker verifies:

1. the theorem's class-count formula through `ell=8`;
2. a single exact quotient transition signature on every recursive class through `ell=8`;
3. exact agreement with independently computed stable refinement through `ell=8`;
4. exact integer `T^29 0` values and exact reduced MTBDD node counts through `ell=9`.

Items 1–2 are self-checks of the all-`ell` proof in Sections 3–4; they are not substitutes for it. Item 3 is deliberately finite evidence only. Item 4 is a finite representation experiment, not a source endpoint.

## 8. Source-level before/after and mechanism progress

Source-level before this R17 run:
\[
L\le\gamma_2\le U_*,\qquad W_{\rm before}=U_*-L.
\]

Source-level after this R17 run:
\[
L\le\gamma_2\le U_*,\qquad W_{\rm after}=U_*-L.
\]

Therefore
\[
\boxed{W_{\rm after}=W_{\rm before};\ \text{no R17 endpoint movement}.}
\]

Mechanism movement is separate and real:

- the old group-only `ell=22` symbolic quotient is strengthened to a proved recursive Bellman congruence with exact size `2,932,033,104,555`;
- the quotient is proved certificate-preserving, not merely a state-count symmetry;
- ordinary stable behavioral refinement finds no further merger through `ell=8`;
- the previously hypothetical MTBDD route is now tested exactly on real Bellman iterates through `ell=9`, with archived node counts.

This is a method change **within the same LCS problem**, as required after repeated unchanged R17 source metrics; no unrelated rotation is performed and no historical failure counter is reset.

## 9. Exact remaining full-scope gap

The source problem is still open. The lower-side metric-deciding target remains exactly
\[
\boxed{
\text{construct an exact source-valid Bellman/feasible-triplet witness at the next scale with }
 r>\frac{99083249}{150916751}.
}
\tag{9.1}
\]
Theorem 3.4 reduces the state space by a provable constant factor but leaves trillions of quotient classes. The finite refinement experiment says that ordinary bisimulation is not giving an obvious second exponential saving at small widths. The exact MTBDD experiment says that naive ordered decision-diagram reduction of a real value iterate is also only moderate at small widths.

Therefore the next nonduplicating R17 route should attack the **mismatch-root sector specifically** rather than another generic quotient. Two precise possibilities survive:

1. a certificate-specific inequality representation that never stores a value for every mismatch orbit (for example, a local/separable potential with an exact separation oracle over mismatch states); or
2. a provable structural domination that replaces the exact mismatch-root value by a smaller family of worst-case signatures while preserving a Bellman **subsolution inequality** rather than exact equality of the entire operator.

The second possibility is particularly different from the failed exact-lumping route: a lower certificate only needs a one-sided inequality, so exact behavioral equivalence may be unnecessarily strong.

No exact value of `gamma_2`, no endpoint improvement, and no closure are claimed. Closure still requires a full source-matching proof, exact finite core where applicable, current prior-art checking, and the repository's independent-validation standard.

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
  upper_before: "U_* from P02 2026-09-20T09-05-20Z residue-optimal-defect report"
  upper_after: "same U_*"
  metric_before: "U_*-L"
  metric_after: "U_*-L"
  source_movement: none
  mechanism_progress:
    - "proved recursive all-ell Bellman congruence"
    - "exact quotient size c_ell=(2*4^(ell-1)+3*2^(ell-1)+1)/3"
    - "c_22=2932033104555"
    - "stable refinement agrees with quotient through ell<=8"
    - "exact T^29(0) MTBDD counts archived through ell=9"
  h0021: "released/unassigned; preserved; Delta_near=2"
  closure: false
```

No schedule, cadence, enabled state, email, Drive item, public posting, workflow, purchase, permission, shared-root ledger, or peer claim file was modified.