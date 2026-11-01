Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort receipt, so I do not claim otherwise.

# PROB10-02 / R17 — canonical greedy-embedding frontiers, a stopping-line upper transfer, and an exact depth-two certificate

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every random object below is built from the two actual source strings. **No independent Bernoulli matching array is used.**

**Status: OPEN / PARTIAL. Source endpoint movement in this R17 run: none.** The run proves a new dependence-preserving canonical-embedding upper mechanism with an exact finite-to-infinite transfer, then certifies a depth-two macro upper bound below `0.857`. This is substantially weaker than the current P02 source upper endpoint, so it is auxiliary mechanism progress only.

## 0. Continuity, ownership, source metric, and literature

### 0.1 Actual R17 predecessor and the pre-refocus H0021 successor

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

The actual newest completed R17 report entering this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T1223Z_r17_symmetric_single_debt_run_macro_71e4.md`.

It proved a five-status symmetric one-debt lower process with an exact width-eight mechanism certificate and, separately, a binary run-exhaustion semi-Markov recurrence. It did **not** move the source interval. Its failures/counterexamples, one-sided Snell predecessor, sharp path-span results, and all earlier R17 LCS artifacts remain preserved; no failure count is reset here.

The actual pre-PROB10 successor is still exactly the H0021 handoff in `operations/claims/H0021.md`, blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`. H0021 remains **UNASSIGNED (released by R17 under later owner refocus)** with frozen `Delta_near=2`. R16's six-run historical stagnation and two consumed recoveries remain preserved; R17's own H0021 substantive unchanged streak remains one with zero R17 H0021 recovery runs consumed. Navigation commit `c8891869a1335d67bada83f23f63f2ce09603565` remains the required historical pointer. No H0021 claim, ownership field, metric, artifact, or counter is changed in this run.

### 0.2 Same-source ownership and nonduplication

The current same-source split has advanced concurrently and is respected:

- **P02** owns the covering/cone stationary upper-dual lane. Its newest completed report read here is `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T13-10-25Z__padic-type01-dual-report.md`.
- **P13** owns the genuine-source strip/boundary recursion lane. Its newest completed report read here is `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T13-12-00Z__cesaro-block-transfer-and-carry-quotient.md`.
- **R17** remains on the finite-lookahead / information-structure lane, but after repeated source-level stagnation this run deliberately changes method: it uses the tree of **canonical greedy embeddings of candidate subsequence words**, not covering labels and not strip gradients.

The present theorem therefore does not overwrite P02 or P13 ownership.

### 0.3 Certified source interval before and after

Retain the rigorous public lower endpoint
\[
L=\frac{99083249}{125000000}=0.792665992.
\]

The newest completed P02 report above gives the current repository-internal exact upper candidate. In its notation
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,\qquad S=q^6d,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\]
\[
D_{01}=\frac{193538062500189963289079961190606496838227098001860830360348197}
{1094462055227467919},
\]
\[
\beta_{01}=\frac ab-\frac{D_{01}}{2ab},\qquad
\lambda_{01}=\frac{t^2}{S}\,\beta_{01},
\]
and
\[
\boxed{U_{01}=\frac{\log(4t^2)}{\log\lambda_{01}}}.
\]
P02's exact logarithm enclosure certifies
\[
U_{01}<0.82627594276228262501510658153729663282346199619319002388080618331256294443029.
\]
Thus the exact source metric entering and leaving the present R17 run is
\[
\boxed{W_{before}=W_{after}=U_{01}-L.}
\]
The displayed separator implies only the diagnostic inequality
\[
W_{after}<0.03360995076228262501510658153729663282346199619319002388080618331256294443029.
\]
P02's endpoint is companion-track work pending the repository's review / public-priority standard and is not attributed to R17.

### 0.4 Bounded current literature check

A fresh bounded source check on 20 September 2026 remains consistent with the exact binary coefficient being unresolved.

- Chvatal--Sankoff, *Longest common subsequences of two random sequences* (1975), introduced the limiting constant and the classical bounds.
- Alexander Tiskin, `https://arxiv.org/abs/2212.01582v2`, last revised 13 August 2024, still treats the binary coefficient as unresolved. The v2 comments explicitly say that earlier claims about the stochastic process and `gamma` were incorrect and were removed. **No withdrawn v1 statement is used here.**
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `https://arxiv.org/abs/2407.10925`, prove the lower endpoint `0.792665992`.
- Lueker's 2009 JACM paper gives the conventional published upper `0.826280`.
- Li--Ren--Wen, published online by Cambridge University Press on 2 March 2026, still describe determining the two-string binary constant as open and summarize the public range.

This is bounded status checking, not a claim of exhaustive worldwide novelty.

## 1. Idea written before code and the three attacks

Before any checker was created, the new route was persisted at

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1330Z_r17_greedy_frontier_idea_84c7.md`

at commit `c3ee66afc04a6a67a3e1a66045ede560c405cdda`.

The run then executed three materially distinct attacks plus one falsification test:

1. **canonical greedy-frontier stopping line:** prove a lossless Pareto-pruned word tree and a rigorous first-moment finite-to-infinite upper transfer;
2. **depth one, analytic:** compute its transform exactly and compare it with the classical unpruned word union bound;
3. **depth two, exact macro:** use binary run lengths to integrate the four-word Pareto frontier exactly up to a geometric tail, producing an exact rational upper certificate;
4. **falsification of a tempting shortcut:** show that a one-layer extension-signature Markov closure has a spurious all-reward-one self-loop and therefore cannot be used as an upper proof.

The first three are new mathematics in this R17 lane; the fourth preserves an obstruction instead of silently promoting a false finite closure.

## 2. Canonical greedy embedding tree

Let `X=(X_1,X_2,...)` be an infinite binary string. For a finite word `w`, define its **greedy embedding endpoint** recursively by
\[
T_X(\varnothing)=0,
\]
\[
T_X(wc)=\min\{j>T_X(w):X_j=c\},\qquad c\in\{0,1\}.
\tag{2.1}
\]
For an iid fair binary string this is finite almost surely for every finite `w`. Define `T_Y` independently and
\[
P(w):=(T_X(w),T_Y(w)).
\tag{2.2}
\]

### Lemma 2.1 — canonical-word equivalence

For integers `n,k>=0`,
\[
LCS(X_1^n,Y_1^n)\ge k
\quad\Longleftrightarrow\quad
\exists w\in\{0,1\}^k:\ P(w)\le(n,n)
\tag{2.3}
\]
coordinatewise.

#### Proof

If `w` is a common subsequence of the two prefixes, greedy embedding finishes no later than any other embedding of the same word, so both greedy endpoints are at most `n`. Conversely `P(w)<=(n,n)` explicitly gives a common embedding in both prefixes. QED.

### Lemma 2.2 — subtree monotonicity

Fix a deterministic binary string `X`. If two starting positions satisfy `i<=j`, then for every finite word `z`, the greedy endpoint obtained by embedding `z` after `i` is no later than the one obtained after `j`.

Hence, for two source strings, if
\[
P(u)\le P(v),
\]
then for every suffix word `z`,
\[
P(uz)\le P(vz).
\tag{2.4}
\]

#### Proof

For one target symbol, the first occurrence after an earlier starting position is no later than the first occurrence after a later starting position. Iterate this monotonicity over the letters of `z`. Apply it independently in `X` and `Y`. QED.

Thus a word whose endpoint is coordinatewise dominated can be deleted together with its entire same-suffix subtree without changing whether some descendant can enter a coordinate box.

## 3. Pareto block frontiers and the stopping-line lemma

Fix a block depth `r>=1`. For fresh independent iid tails `(X,Y)`, let
\[
\mathcal F_r(X,Y)\subseteq\{0,1\}^r
\]
be one deterministic representative for each Pareto-minimal endpoint among
\[
\{P(w):|w|=r\}.
\]
If two words have identical endpoint points, keep the lexicographically first one. This tie convention is immaterial to the existence problem because identical points have identical future starting positions.

For `0<z<1`, define the finite-block transform
\[
\boxed{
m_r(z):=\mathbf E\sum_{w\in\mathcal F_r(X,Y)}
 z^{T_X(w)+T_Y(w)}.
}
\tag{3.1}
\]

### Lemma 3.1 — frontier membership is a stopping-line event

For a fixed word `w` of length `r`, the event
\[
w\in\mathcal F_r(X,Y)
\]
is measurable with respect to the two stopped prefixes
\[
\sigma(X_1,\ldots,X_{T_X(w)})
\quad\text{and}\quad
\sigma(Y_1,\ldots,Y_{T_Y(w)}).
\]
Consequently, conditional on this event and these stopped prefixes, the two tails after `T_X(w)` and `T_Y(w)` are independent iid fair binary strings.

#### Proof

For any competitor `v` of length `r`, the statement `T_X(v)<=T_X(w)` is decidable from the prefix of `X` through `T_X(w)`: it holds exactly when greedy embedding of `v` completes inside that prefix. The same is true in `Y`. Hence whether some `v` coordinatewise dominates `w`, including the deterministic equal-point tie rule, is determined by the two stopped prefixes.

Each `T_X(w)` is a stopping time for the filtration of `X`, and analogously for `Y`. The strong Markov/deferred-decisions property for an iid sequence says that the tail after such a finite stopping time is fresh iid and independent of its stopped past. Since `X` and `Y` are independent, their two residual tails remain independent as well. QED.

This is precisely where the genuine source dependence is kept: siblings may be heavily dependent, but linearity plus the stopping-line property is enough for the expected weighted population; no independent sibling model is substituted.

## 4. Recursive macro pruning and exact first-moment factorization

Starting at the root, recursively apply the depth-`r` Pareto rule to the fresh residual pair at every retained macro node. Let `A_q` be the retained words after `q` macro generations, so every `a in A_q` has length `qr`. Put
\[
Z_q:=\sum_{a\in A_q} z^{T_X(a)+T_Y(a)}.
\tag{4.1}
\]

### Theorem 4.1 — lossless macro pruning and multiplicative expectation

For every `q>=0`:

1. if some binary word of length `qr` has endpoint at most `(n,n)`, then some retained word `a in A_q` does too;
2. the exact expectation is
\[
\boxed{\mathbf E Z_q=m_r(z)^q.}
\tag{4.2}
\]

#### Proof

For (1), process the word block by block. Whenever its next `r`-block is dominated at the current macro node, replace that block by a frontier block whose local endpoint is coordinatewise no later and retain the same remaining suffix. Lemma 2.2 shows the final endpoint does not increase. Iterate through all blocks.

For (2), use induction. At a retained parent, each candidate retained child `w` contributes the parent weight times `z^{local endpoint sum}` times the future weighted population rooted at that child. By Lemma 3.1, conditional on the event that this child is retained and on its stopped endpoint, its two residual tails are fresh iid; therefore its conditional expected future factor is the same deterministic number `E Z_{q-1}`. Sibling tails need not be jointly independent because expectation is summed child by child. Summing and taking expectation gives
\[
\mathbf E Z_q=m_r(z)\,\mathbf E Z_{q-1},
\]
with `Z_0=1`. QED.

## 5. Exact finite-to-infinite upper transfer

### Theorem 5.1 — canonical-frontier upper bound

For every `r>=1` and every `0<z<1` with `m_r(z)<1`,
\[
\boxed{
\gamma_2\le U_r(z):=
\frac{2r\log(1/z)}{-\log m_r(z)}.
}
\tag{5.1}
\]
Moreover, for every integer `q>=1`,
\[
\boxed{
\Pr\{LCS(X_1^n,Y_1^n)\ge qr\}
\le z^{-2n}m_r(z)^q.
}
\tag{5.2}
\]

#### Proof

On the event `LCS_n>=qr`, Theorem 4.1 supplies a retained `a in A_q` with both endpoints at most `n`. Since `0<z<1`, its contribution to `Z_q` is at least `z^{2n}`. Thus
\[
1_{\{LCS_n\ge qr\}}\le z^{-2n}Z_q.
\]
Take expectations and use (4.2) to obtain (5.2).

Now fix `alpha>U_r(z)` and take `q_n=floor(alpha n/r)`. The logarithm of the right side of (5.2), divided by `n`, tends to
\[
2\log(1/z)+\frac{\alpha}{r}\log m_r(z)<0.
\]
Therefore `P(LCS_n/n>=alpha)->0` exponentially. Since `0<=LCS_n/n<=1`,
\[
\frac{\mathbf E LCS_n}{n}
\le \alpha+\Pr\{LCS_n/n\ge\alpha\}.
\]
Take `n->infinity`, then `alpha downarrow U_r(z)`. QED.

**Finite-to-infinite error:** there is no asymptotic truncation term in (5.1); once an upper value for `m_r(z)` is certified, (5.1) transfers it directly. Any finite integration truncation used to certify `m_r` must of course be added explicitly, as done in Section 7.

## 6. Attack B — exact depth-one transform

At depth one there are only the candidate words `0` and `1`.

If `X_1=Y_1` (probability `1/2`), the common first bit has endpoint `(1,1)` and dominates the other bit. Its frontier weight is `z^2`.

If `X_1!=Y_1` (probability `1/2`), both one-letter words are Pareto-minimal. Conditional on the first bit, the initial run length `R` has
\[
\Pr(R=r)=2^{-r},\qquad r\ge1.
\]
The two frontier points have the forms `(1,R_Y+1)` and `(R_X+1,1)`, with independent `R_X,R_Y`. Hence
\[
\mathbf E z^{R+2}
=z^2\sum_{r\ge1}2^{-r}z^r
=\frac{z^3}{2-z}.
\]
Therefore
\[
\boxed{
m_1(z)=\frac{z^2}{2}+\frac{z^3}{2-z}.}
\tag{6.1}
\]

For comparison, the completely unpruned canonical-word union bound has one-letter transform
\[
2\left(\frac{z}{2-z}\right)^2,
\]
which is the familiar first-moment route behind the classical Chvatal--Sankoff upper scale. Immediate Pareto pruning strictly decreases the transform for `0<z<1`.

At `z=1/3`,
\[
m_1(1/3)=\frac7{90}.
\tag{6.2}
\]
The corresponding diagnostic upper is about `0.8603410`; this is already below the elementary unpruned bound but remains far above the current rigorous source upper.

## 7. Attack C — exact depth-two macro certificate

At depth two there are four target words `00,01,10,11`. Their greedy endpoint vector in one source string has an especially small run representation.

Condition on starting bit `0` and let the first three run lengths be `R_1,R_2,R_3`, iid with `P(R_i=r)=2^{-r}`. Then
\[
T(00)=\begin{cases}2,&R_1\ge2,\\R_2+2,&R_1=1,\end{cases}
\tag{7.1}
\]
\[
T(01)=R_1+1,
\tag{7.2}
\]
\[
T(10)=R_1+R_2+1,
\tag{7.3}
\]
\[
T(11)=\begin{cases}R_1+2,&R_2\ge2,\\R_1+R_3+2,&R_2=1.\end{cases}
\tag{7.4}
\]
Starting bit `1` simply complements target labels, interchanging `00<->11` and `01<->10`.

Equations (7.1)--(7.4) are proved directly by locating the earliest required symbols in consecutive runs. The exact checker independently verifies them over all starts and `1<=R_i<=5` using literal greedy embedding.

### 7.1 Exact finite sum at `z=1/3`

Take `M=20` and first sum only over the event that all first three runs in each source string are at most `M`. The exact checker aggregates the one-string endpoint maps with common dyadic denominator
\[
D=2^{1+3M}.
\]
There are `1560` distinct endpoint maps under this truncation. Pareto-minimal pairs are then summed exactly with common `3`-power denominator. The executed exact value is
\[
 m_{2,\mathrm{trunc}}
=
\frac{1723757591172391977322540103397029032225108180311671875}
{290885567248183331831024113936217248185545312242413600768}.
\tag{7.5}
\]

The probability that at least one of the six run lengths exceeds `M` is exactly
\[
 p_{tail}
=1-(1-2^{-20})^6
=
\frac{7605885467505140603142067453951}
{1329227995784915872903807060280344576}.
\tag{7.6}
\]
On this omitted event the depth-two frontier has at most four words, and every depth-two endpoint is at least `2` in each string. Thus at `z=1/3` its total weight is at most
\[
4z^4=\frac4{81}.
\]
Therefore
\[
 m_2(1/3)\le m_{2,\mathrm{trunc}}+\frac4{81}p_{tail}
=:\overline m_2,
\tag{7.7}
\]
with exact rational
\[
\boxed{
\overline m_2=
\frac{1723839786559977604263656518625891806838896023470020987}
{290885567248183331831024113936217248185545312242413600768}.
}
\tag{7.8}
\]
Diagnostic decimal value is about `0.005926178472406639`; the proof uses the rational (7.8).

The checker proves exactly
\[
\boxed{\overline m_2<\left(\frac7{90}\right)^2=m_1(1/3)^2.}
\tag{7.9}
\]
Hence depth-two cross-branch Pareto pruning gives a strict gain over merely applying the depth-one pruning independently twice.

### 7.2 Logarithm-free rational upper comparison

Using (5.1) and `m_2<=overline m_2`,
\[
\gamma_2\le\frac{4\log3}{-\log m_2(1/3)}
\le\frac{4\log3}{-\log\overline m_2}.
\]
To avoid floating logarithms, the checker verifies the exact integer inequality
\[
3^{4000}\,\overline m_2^{857}<1.
\tag{7.10}
\]
This is algebraically equivalent to
\[
\boxed{
\frac{4\log3}{-\log\overline m_2}<\frac{857}{1000}=0.857.
}
\tag{7.11}
\]
Thus the new route proves the standalone rigorous bound
\[
\boxed{\gamma_2<0.857}
\tag{7.12}
\]
from canonical greedy-frontier pruning alone.

This does **not** improve the source endpoint because P02 already gives `U_01<0.82627595`. Its value is the new exact representation and transferable upper mechanism, not the numerical endpoint.

## 8. Attack D — exact obstruction to the one-layer extension-signature Markov shortcut

A tempting simplification is to retain only the four one-sided extension bits
\[
\sigma(x,y)=
( LCS(x,y0)-L,
  LCS(x,y1)-L,
  LCS(x0,y)-L,
  LCS(x1,y)-L),
\]
where `L=LCS(x,y)`, and then treat this signature as a Markov state under paired source extension.

The exact checker finds the explicit pair
\[
x=00001011,\qquad y=11110100
\]
with
\[
\sigma(x,y)=(1,1,1,1),
\]
and, for **all four** fresh source pairs `(u,v)`,
\[
\sigma(xu,yv)=(1,1,1,1).
\tag{8.1}
\]
At this signature the diagonal LCS increment is `1` for every `(u,v)`: it is `1` on a matching pair, and on a mismatch it is the maximum of two one-sided extension bits, both equal to `1`.

Therefore any upper relaxation that forgets the hidden deeper extension structure and treats the four-bit signature as a closed Markov state acquires an apparent reward-one self-loop. Reusing that projected self-loop indefinitely would yield the useless upper rate `1`. The witness does **not** assert that one fixed hidden prefix supports an infinite reward-one evolution; it proves exactly why the projected finite profile is non-Markovian and why a projectively consistent stopping-line construction such as Sections 2--7 is required.

## 9. Verification artifacts

Idea-before-code artifact:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1330Z_r17_greedy_frontier_idea_84c7.md`

created at commit `c3ee66afc04a6a67a3e1a66045ede560c405cdda`.

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1342Z_r17_greedy_frontier_exact_84c7.py`

created at commit `875c99ae2c78d4eddd8c8d14db77dfd26cb05a8d`.

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1342Z_r17_greedy_frontier_exact_84c7.out`

created at commit `dbb0bf74504f40047dae3907f82d20a35b99c8b0`.

The output ends

`ALL_EXACT_CHECKS_PASS`

and

`RETURN_CODE=0`.

The checker verifies:

- the binary run formulas (7.1)--(7.4) independently by literal greedy embedding on a finite run grid;
- the exact truncated probability mass;
- the exact rational `m_{2,trunc}` and tail probability;
- the exact tail majorant and rational `overline m_2`;
- `overline m_2 < (7/90)^2`;
- the integer-power certificate equivalent to `U_2(1/3)<857/1000`;
- the one-layer signature self-loop obstruction (8.1).

This is a self-check, not an independent audit.

## 10. Before / after ledger

### Source level

Before:
\[
L\le\gamma_2\le U_{01},\qquad W_{before}=U_{01}-L.
\]

After:
\[
\boxed{L\le\gamma_2\le U_{01},\qquad W_{after}=W_{before}.}
\]

No R17 source endpoint changed.

### Auxiliary mechanism level

New exact results in this run:

1. canonical greedy embeddings plus Pareto subtree domination give a lossless pruned word tree;
2. Pareto-frontier membership is a two-source stopping-line event, which yields the exact multiplicative transform `E Z_q=m_r(z)^q` without independent-sibling substitution;
3. every finite `m_r(z)<1` certificate transfers rigorously by (5.1) to the true infinite LCS constant;
4. depth one has the closed transform `m_1(z)=z^2/2+z^3/(2-z)`;
5. at depth two and `z=1/3`, an exact run-length integration plus explicit geometric tail gives `m_2<=overline m_2<(7/90)^2` and the rigorous standalone upper `gamma_2<0.857`;
6. a four-bit extension-signature closure is exactly obstructed by the explicit all-ones projected self-loop.

## 11. Remaining full-scope gap and next precise route

The source problem remains far from closed in this lane because `0.857` is weaker than the current `U_01<0.826276`. The new theorem is useful only if the block-frontier transform can be pushed substantially lower.

The most precise next nonduplicating route is **not** another one-debt lower policy. It is to increase macro depth while preserving the stopping-line proof. For depth `r`, `m_r(z)` is a finite-word Pareto-frontier expectation. A viable exact strategy is to build a finite automaton for the joint greedy-endpoint order type, use rational `z`, and certify `m_r(z)` by an exact transfer matrix plus explicit geometric stopping tails. The first milestone is a depth `r>=3` certificate that improves the per-letter exponent
\[
-\frac1r\log m_r(z)
\]
beyond the depth-two value by enough to point toward the P02 range. If finite automaton size explodes, the obstruction must be recorded and the next method should use an exact stopping-line quotient rather than reverting to the false one-layer signature Markovization.

No complete determination of `gamma_2` is claimed. Source status remains **OPEN / PARTIAL**.

## 12. Delivery / safety

Only authorized conflict-safe GitHub content writes were used. No force push, schedule/cadence change, enabled-state change, email, Drive write, public posting, workflow edit, permission change, or overwrite of historical claims was performed.
