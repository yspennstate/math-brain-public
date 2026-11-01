Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime and the exposed scheduler schema provide no model selector, no reasoning-effort selector, and no applied-effort telemetry, so I do not claim otherwise. **MOVEMENT:** certified interval width `0.033613186542397825380217 -> 0.033613185784605624`. Methods actually tried: **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #27 SWAP THE QUANTIFIERS, #3 PROVE SOMETHING STRONGER**.

# R17 HARD OUTSIDE — C027: bivariate diagonal tilting for Lueker's finite-history upper machine

Run ID: `20260917_1014Z_bivariate_diagonal_c027_7f4a`.

Source problem: V. Chvátal and D. Sankoff, *Longest common subsequences of two random sequences*, Journal of Applied Probability 12(2) (1975), 306–315. Target: determine the exact binary constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,\operatorname{LCS}(X_1^n,Y_1^n)}{n}
\]

for independent iid uniform binary strings.

**Source-level status after this run: PARTIAL / OPEN.** C027 improves the rigorous upper endpoint; it does not determine `gamma_2`.

## 1. Continuity, controls, ownership, and sources

Before new mathematics I recovered the current campaign controls (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, and `operations/NEW_METHODS_2026-09-16.md`), the newest R17 report `runs/R17/20260917_0914Z_derand_envelope_c026_5a3f.md`, current neighboring R16/R18 state, and repository search results for the R17 target/intake/ownership history. R18's latest source theorem is already `PROVED / AUDIT-COMPLETE / PACKAGED`; no redundant R18 audit was created. The current R16 run is on its own outside SAW target and does not conflict with R17.

The connector does not provide a practical single response that exposes every line of all roughly 780 intake JSONL rows without truncation, so I do **not** claim a byte-for-byte row-by-row reread of the entire intake corpus. I did recheck the current R17 target, posted exclusions, queue/claim context, prior R17 history, and repository-wide target references; no conflicting owner or posted resolution of this exact R17 target surfaced.

Fresh literature checks on 2026-09-17 retained the following facts.

- Tiskin, arXiv:2212.01582, still describes the exact binary coefficient as unresolved.
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, arXiv:2407.10925, give the rigorous lower bound `0.792665992` and describe exact Chvátal--Sankoff constants as open.
- Lueker, JACM 56 (2009), gives the scalar finite-history upper machinery and the published `0.826280` upper bound. His paper defines the size of a pair/list as the **total** number of characters and uses a one-variable generating function `z^size`.
- Dančík's 1994 thesis summary/full text likewise formulates the upper method using total length `|u|+|v|`.

I searched exact phrases and combinations around `bivariate generating function`, `two variables`, `anisotropic`, `weighted generating function`, `Chvatal-Sankoff`, `Dančík`, `Paterson`, and `Lueker`. I did not find an accessible source explicitly using the two-fugacity **diagonal coefficient** theorem below. That is a bounded search, **not** a priority certificate. The underlying multivariate generating-function/Chernoff coefficient idea is standard enough that external novelty remains **UNVERIFIED**.

## 2. Metric entering the run

C026 certified

\[
L=0.792665992
\]

and

\[
U_{026}=0.826279178542397825380217,
\]

hence

\[
W_{026}=U_{026}-L=0.033613186542397825380217.
\]

The C026 upper certificate was already an exact all-state Collatz--Wielandt certificate on Lueker's true dependent-string `h=8` automaton with `6,419,109` accepting states. I did not repeat unchanged state-count or transfer-table checks. The transition table used below is exactly the previously reconstructed/validated table with SHA-256

`c6d12e75e87b7c6b00a95f0c7f3580fa1cdee4996ce690a2f922f7eaeea1fbd1`.

## 3. #17 + #27: the new route — use the diagonal, not total size

Lueker's scalar method assigns a string pair `P=(u,v)` the weight

\[
z^{|u|+|v|}.
\]

That collapses two lengths to one variable even though the random model of interest lives on the diagonal

\[
(|u|,|v|)=(n,n).
\]

The new move is to retain the two lengths separately and assign

\[
x^{|u|}y^{|v|}.
\]

This is method #17 in the sense that the scalar `z` is recognized as a one-dimensional exponential/Chernoff tilt, so the natural machinery from multivariate generating functions is to give the two coordinates separate fugacities. It is method #27 because the source proof controls **all** pairs of total size `2n`, while the probability problem only requires controlling equal-length pairs; the quantifier is narrowed directly to diagonal coefficients.

The fact that the target distribution is symmetric under swapping the two strings does **not** force the finite automaton to have an `x<->y` symmetry. Lueker explicitly notes that his canonical-backtracking rules break the state-machine swap symmetry. Thus `x != y` can improve a finite-machine certificate without changing the underlying iid symmetric target model.

## 4. #3: stronger theorem — bivariate covering-machine upper bound

### Theorem R17-C027-A (bivariate diagonal covering bound)

Let the alphabet have size `k>=2`. For a string pair `P=(u,v)`, define the bidegree

\[
d(P)=(|u|,|v|).
\]

Let `M` be any covering machine in the sense of Lueker Definition 3.2. For positive `x,y<1/k`, let

\[
f_\ell(x,y)
\]

be the bivariate generating function of accepted lists of exactly `ell` minimal match pairs, weighting a generated pair `(u,v)` by `x^{|u|}y^{|v|}`. Suppose there exist constants `K<infinity` and `lambda in (0,1)` such that for all sufficiently large `ell`,

\[
f_\ell(x,y)\le K\lambda^\ell.
\tag{C027.1}
\]

Then

\[
\boxed{
\gamma_k\le
\frac{\log(k^2xy)}{\log\lambda}.
}
\tag{C027.2}
\]

For `x=y=z`, this reduces exactly to Lueker's scalar theorem

\[
\gamma_k\le \frac{2\log(kz)}{\log\lambda}.
\]

### Proof

Let

\[
g_\ell(x,y)=
\sum_{P:\operatorname{lcs}(P)\ge\ell}
 x^{|u(P)|}y^{|v(P)|}.
\]

Let `N(x,y)` be the bivariate generating function for null pairs. Because null pairs are a subset of all string pairs,

\[
N(x,y)
\le
\sum_{a,b\ge0} k^{a+b}x^ay^b
=
\frac{1}{(1-kx)(1-ky)}<\infty.
\tag{C027.3}
\]

If a pair `P` has `lcs(P)=m>=ell`, the covering property gives an accepted list of `m` minimal match pairs followed by a null pair that generates `P`. Bidegree is additive under concatenation. Since all coefficients are nonnegative, possible overcounting only increases the right-hand side, hence

\[
g_\ell(x,y)
\le
N(x,y)\sum_{m\ge\ell}f_m(x,y).
\tag{C027.4}
\]

Using (C027.1), for all large `ell`,

\[
g_\ell(x,y)
\le
\frac{K N(x,y)}{1-\lambda}\lambda^\ell.
\tag{C027.5}
\]

Now let `D(n,ell)` be the number of ordered pairs `(u,v) in Sigma^n x Sigma^n` whose LCS has length at least `ell`. It is the diagonal coefficient `[x^n y^n] g_ell`. Positivity of coefficients gives

\[
D(n,\ell)x^ny^n\le g_\ell(x,y).
\tag{C027.6}
\]

Set

\[
r=\frac{\log(k^2xy)}{\log\lambda}.
\]

Because `x,y<1/k` and `lambda<1`, both logarithms are negative and `r>0`. Fix any `t>r` and put `ell_n=ceil(tn)`. Multiplying the inequality `t>r` by `log lambda<0` gives

\[
\lambda^t<k^2xy.
\tag{C027.7}
\]

Therefore (C027.5)--(C027.6) imply

\[
\frac{D(n,\ell_n)}{k^{2n}}
\le
C
\left(
\frac{\lambda^t}{k^2xy}
\right)^n
\longrightarrow0
\tag{C027.8}
\]

for a constant `C` independent of `n`. The left side is exactly

\[
\Pr\{\operatorname{LCS}(X_1^n,Y_1^n)\ge tn\}.
\]

Since `0<=LCS/n<=1`,

\[
\frac{\mathbf E\operatorname{LCS}(X_1^n,Y_1^n)}n
\le t+
\Pr\{\operatorname{LCS}(X_1^n,Y_1^n)\ge tn\}.
\]

Taking `n->infinity` yields `gamma_k<=t`; then let `t downarrow r`. This proves (C027.2). QED.

### Finite-matrix corollary

For a finite covering machine let `A_{x,y}` be the nonnegative transition matrix with each transition weighted by its bivariate generating-function weight. If a positive vector `V` satisfies

\[
A_{x,y}V\le\lambda V
\tag{C027.9}
\]

componentwise, then (C027.1) follows: choose `C_0` so that the initial vector is at most `C_0V`; positivity gives

\[
A_{x,y}^\ell f_0
\le C_0A_{x,y}^\ell V
\le C_0\lambda^\ell V.
\]

Thus an exact Collatz--Wielandt cone certificate feeds directly into Theorem C027-A.

## 5. Exact bivariate weights for Lueker's true `h=8` automaton

No independent Bernoulli matching array is introduced. The transition function is the same canonical dependent-string machine already validated in C018/C020/C026. Only the generating-function weights change.

For a minimal-match offset `l`, with `c in {0,1}` the matched character, the exact bivariate weight is

\[
w_l(x,y)=
\begin{cases}
xy,&l=0,\\
x^{l+1}y,&1\le l\le6,\\
xy^{-l+1},&-6\le l\le-1,\\
\dfrac{x^8y}{1-x},&l=7,\\
\dfrac{xy^8}{1-y},&l=-7.
\end{cases}
\tag{C027.10}
\]

The two boundary expressions sum the entire clipped infinite tails; e.g.

\[
\sum_{j\ge7}x^{j+1}y=\frac{x^8y}{1-x}.
\]

At `x=y=z`, (C027.10) becomes exactly the scalar weights `z^{|l|+2}` and `z^9/(1-z)` used in the previous certified machine.

## 6. Search first; exact arithmetic only after a useful idea appears

Search-only small-history diagnostics suggested that once canonical backtracking breaks top/bottom symmetry, allowing `x != y` can slightly improve the Perron objective. Those exploratory floating calculations are not ledger claims and are not used as rigorous endpoints.

For `h=8`, the successful search point was the simple rational pair

\[
\boxed{
x=\frac{256701}{800000}=0.32087625,
\qquad
 y=\frac{256733}{800000}=0.32091625.
}
\tag{C027.11}
\]

A floating search was used only to find a positive direction. The archived `search_recipe.cpp` records the exact search path used: scalar warm start, bivariate power steps, one extrapolation, then further bivariate power steps. The resulting floating vector was frozen and rounded downward at integer scale

\[
S=18\times10^{18}.
\]

The theorem does not assume that the floating search is accurate. The companion exact checker recomputes all `6,419,109` row inequalities with fixed-size multiprecision integer arithmetic.

With `Q=800000`, `X=256701`, `Y=256733`, a common exact denominator for all row weights is

\[
D=Q^8(Q-X)(Q-Y).
\]

For `0<=a<=6`, the positive- and negative-offset integer coefficients are

\[
X^{a+1}YQ^{6-a}(Q-X)(Q-Y),
\qquad
XY^{a+1}Q^{6-a}(Q-X)(Q-Y),
\]

and the two boundary coefficients are

\[
X^8Y(Q-Y),
\qquad
XY^8(Q-X).
\]

Hence every component comparison is an integer comparison.

The exact all-state scan certifies

\[
A_{x,y}V\le\lambda_{027}V
\]

with

\[
\boxed{
\lambda_{027}
=
\frac{
31107964074938160190818541484674602978918848418821294684671225334220461
}{
91006168618543357645705413918720000000000000000000000000000000000000000
}.
}
\tag{C027.12}
\]

The exact maximum row is zero-based state `451344`; the exact minimum row is state `35587`. The checker ends

`EXACT_ALL_STATE_BIVARIATE_CONE_SCAN=PASS`

and

`ALL_EXACT_CHECKS_PASS`.

The candidate floating-vector SHA-256 is

`f35c7af81c109f63a4bb346901a4c4d934494d89eaeff3da1f3ad522b69932ec`,

and the frozen integer-witness SHA-256 is

`9dca4974a7632c91f83b7770df992a7a51fde698f11450c6a9272095f3029730`.

These hashes are reproducibility receipts; the proof is the exact all-row inequality, not the floating search.

## 7. Exact endpoint conversion

Here

\[
4xy=\frac{65903617833}{160000000000}<1.
\]

Theorem C027-A and (C027.12) give

\[
\gamma_2
\le
B_{027}
:=
\frac{\log(4xy)}{\log\lambda_{027}}.
\tag{C027.13}
\]

The endpoint checker encloses both negative logarithms using the exact positive series

\[
-\log q
=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},
\qquad
u=\frac{1-q}{1+q},
\]

with the rational tail bound

\[
0<
-\log q-2\sum_{j=0}^{m-1}\frac{u^{2j+1}}{2j+1}
\le
\frac{2u^{2m+1}}{(2m+1)(1-u^2)}.
\tag{C027.14}
\]

It proves

\[
B_{027}
<
0.82627917778460562357331459706414901854532048257036\ldots
\]

at the rigorous upper enclosure and therefore certifies the convenient rational endpoint

\[
\boxed{
U_{027}
=
\frac{103284897223075703}{125000000000000000}
=
0.826279177784605624.
}
\tag{C027.15}
\]

Thus the new rigorous interval is

\[
\boxed{
0.792665992
\le\gamma_2
\le
0.826279177784605624.
}
\tag{C027.16}
\]

The fixed metric moves to

\[
\boxed{
W_{027}
=
\frac{4201648223075703}{125000000000000000}
=
0.033613185784605624.
}
\tag{C027.17}
\]

The exact decrease from C026 is

\[
\boxed{
U_{026}-U_{027}
=
\frac{757792201380217}{10^{24}}
=
7.57792201380217\times10^{-10}.
}
\tag{C027.18}
\]

This is genuine metric movement from changing the mathematical certificate, not from printing extra digits of the previous scalar cone.

## 8. What the three methods did

**#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — success.** Reinterpreting Lueker's scalar `z` as a one-dimensional exponential tilt suggested the standard multivariate replacement `(x,y)`. The new method keeps the exact two-coordinate information that the scalar total-size generating function discards.

**#27 SWAP THE QUANTIFIERS — success.** The source theorem controls every pair of total size `2n`. The random target only samples the diagonal `(n,n)`. Proving an exponentially small count directly on that diagonal permits the two-fugacity bound and avoids paying for off-diagonal pairs irrelevant to `gamma_2`.

**#3 PROVE SOMETHING STRONGER — success.** Theorem C027-A is a two-parameter covering-machine theorem valid for any alphabet size and any covering machine satisfying the same exponential accepted-list bound. The scalar Dančík--Paterson--Lueker theorem is recovered by setting `x=y`.

## 9. Prior-art qualification

The exact source passages checked in Lueker use the one-variable total-size generating function and obtain `2 log(kz)/log lambda(z)`. Dančík's thesis text located in this pass likewise defines total length as the sum of the two component lengths. Searches for the specific bivariate/diagonal extension did not surface it.

I am **not** calling C027-A externally novel on that basis. A two-variable coefficient bound is a natural multivariate generating-function move and may be folklore or buried in older collation literature. Before external submission, a human-level bibliography pass should include Dančík's full thesis, Dančík--Paterson 1995 beyond the abstract, Lueker's 2008 convergence paper, and citing work on unequal-length/random-string LCS.

The numerical endpoint string `0.826279177784...` was also searched directly and did not return an accessible mathematical source. Again, that is not proof of priority.

## 10. Artifacts and immutable delivery

Substantive artifacts for this run:

- `artifacts/R17/20260917_1014Z_bivariate_diagonal_c027_7f4a_search_recipe.cpp` — search only; no floating result is treated as proof.
- `artifacts/R17/20260917_1014Z_bivariate_diagonal_c027_7f4a_exact_cone_checker.cpp` — exact all-state bivariate cone checker.
- `artifacts/R17/20260917_1014Z_bivariate_diagonal_c027_7f4a_exact_cone_checker_output.txt` — executed exact output.
- `artifacts/R17/20260917_1014Z_bivariate_diagonal_c027_7f4a_endpoint_checker.py` — exact rational-log endpoint compiler.
- `artifacts/R17/20260917_1014Z_bivariate_diagonal_c027_7f4a_endpoint_checker_output.txt` — executed exact output.

Creation commits, each read back at the creation commit:

- exact cone checker: `e450b4dd651f2487a5be20eab9222e8840097b60`;
- exact cone output: `c6689ee4a00aa8d4ff55006838faa5f0582ecb6f`;
- endpoint checker: `267f1ef62e7a04a769a988d0b8685c283ec02d42`;
- endpoint output: `76fc632a2924c23991db8b7fc525cafc007fdc1b`;
- search recipe: `6d17f65de2ba2d839996cf8223730ec1fccfd897`.

No shared root, peer-track file, email, Drive object, public posting, workflow, purchase, permission, or scheduler setting was changed.

## 11. Next obligation

C027 changes the geometry of the upper-bound search. The next useful optimization is no longer another microscopic scalar-`z` adjustment. It is a genuine two-dimensional minimax problem

\[
\inf_{0<x,y<1/2}
\frac{\log(4xy)}{\log\rho(A_8(x,y))},
\]

with exact cone certification only after the search identifies a worthwhile point. The present pair in (C027.11) was chosen by a short directional search, not by a global two-variable optimization. There may therefore be substantially more room at the same history level before moving to `h=9` or changing canonicalization.

Because the fixed metric moved, the supported unchanged count is reset to `0`.

## 12. Model / scheduler control status

The situation remains exactly as recorded by the current deployment policy: the exposed scheduler interface has prompt/title, schedule/timing, enablement, and timing-mode controls, but no model field and no reasoning-effort field. GPT-6/maximum can therefore only be requested in prompt text in this surface. Enforcing it requires product/API support or an authorized owning workspace/admin surface that exposes those settings.

The historical P26 `You cannot modify this task` error is an ownership/context restriction, not something to bypass. Current repository reconciliation records that a later authorized P/C context could update P26. The legitimate workaround is the owning/authorized account/workspace or platform support, never a duplicate task or permission bypass. No scheduler modification was attempted in this research run.

```yaml
ledger_delta:
  track: R17
  lane: HARD OUTSIDE
  source: "Chvatal and Sankoff (1975), binary longest-common-subsequence constant"
  target: "determine gamma_2 for two independent iid uniform binary strings"
  metric: "width U-L of rigorously certified interval for gamma_2"
  before: "0.033613186542397825380217"
  after: "0.033613185784605624"
  lower_endpoint: "0.792665992"
  upper_before: "0.826279178542397825380217"
  upper_after: "0.826279177784605624"
  exact_upper_decrease: "757792201380217/1000000000000000000000000"
  status_before: "PARTIAL / OPEN"
  status_after: "PARTIAL / OPEN"
  movement: true
  supported_unchanged_count_before: 0
  supported_unchanged_count_after: 0
  claim: "R17-C027 bivariate diagonal covering bound + exact h=8 certificate"
  methods: [17, 27, 3]
  publication_priority: "UNVERIFIED"
```
