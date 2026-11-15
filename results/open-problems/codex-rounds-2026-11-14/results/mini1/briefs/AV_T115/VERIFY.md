# T115: the Gotsman–Linial influence bound

Checked 14 November 2026. Verdict: SOLVED-CLAIMED for the entire statement in our row. This records what the manuscripts claim and what the formal statements cover; it does not certify the proofs.

## 1. Average sensitivity of polynomial threshold functions

Author as printed: **OpenAI**. Date as printed: **September 25, 2026**. Opened the actual manuscript's [main TeX file](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/main.tex) and [introduction](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/sections/01-introduction.tex). The PDF is [main.pdf](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf); its web wrapper opened, but direct PDF text retrieval failed. The quotations below come from the TeX itself.

Theorem 1, exact source text (retaining TeX mathematical notation):

```tex
Let $n\ge1$ and $1\le d\le n$ be integers. Let $p$ be a real multilinear
polynomial of degree at most $d$, and define
$f:\{-1,1\}^n\to\{-1,1\}$ by $f(x)=\sgn(p(x))$, with $\sgn(0)=1$.
Then, for average sensitivity under the uniform law,
\[
 I(f)\le 8d\sqrt n.
\]
```

The manuscript defines

\[
 I(f)=\sum_{i=1}^n\mathbb P\{f(X)\ne f(X^{\oplus i})\},
 \qquad X\text{ uniform on }\{-1,1\}^n.
\]

Comparison with our statement:

| Our wording | Manuscript | Coverage |
| --- | --- | --- |
| Every degree-d polynomial threshold function | Every real multilinear polynomial of degree at most d, with no regularity assumption | Same class on the cube: reducing exponents using x_i²=1 preserves values and cannot increase total degree. Exact degree d is included in degree at most d. |
| f=sign(p) on {−1,1}^n | Identical cube and sign threshold | Same model. Zeros are expressly allowed with sign(0)=1. The usual alternative tie convention is also covered by replacing p by −p and complementing the output. Arbitrary point-dependent tie assignments are not the model. |
| Total influence (average sensitivity) | Sum of single-bit flip probabilities under the uniform law | Exactly the same quantity E s_f(X), not E sqrt(s_f(X)), maximum sensitivity, Gaussian surface area, or noise sensitivity. |
| At most C d sqrt(n), absolute C | At most 8 d sqrt(n) | The whole bound, with a concrete universal constant. No hidden dependence on d and no logarithmic loss in n. |
| All dimensions and degrees | n>=1 and 1<=d<=n, both varying | Covers every nontrivial range. For d>n use multilinear degree at most n (or I(f)<=n); degree zero gives a constant function and zero influence. The n=0 cube also has zero influence if included. |

This claims the order bound requested in T115, including growing degree, rather than a fixed-degree asymptotic or a special class. It does not claim the sharp numerical constant or identify exact extremizers. Those stronger questions are outside our row.

## 2. A superquadratic separation between sensitivity and block sensitivity

Author as printed: **OpenAI**. Date: **September 25, 2026**. Opened [build/paper.tex](https://github.com/openai/math/blob/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/paper.tex) and the actual [introduction](https://github.com/openai/math/blob/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/sections/00-introduction.tex).

Theorem 1.1, exact source text:

```tex
For every real \(C>0\), there are a positive integer \(n\) and a
nonconstant total Boolean function \(f:\{0,1\}^n\to\{0,1\}\) such that
\[
 \bs(f)>C\,s(f)^2.
\]
More precisely, for every integer \(d\ge1\) the construction below gives
a nonconstant total Boolean function \(f\) with
\[
 \frac{\bs(f)}{s(f)^2}\ge \frac{2^d}{4(d+2)^2}.
\]
```

Here s(f)=max_x s(f,x) and bs(f) is maximum block sensitivity. The {0,1} versus {−1,1} encoding is harmless, but the quantifiers, quantity and direction differ: this is an existence lower bound separating two worst-case measures for arbitrary total Boolean functions. It imposes no degree-d threshold representation. Its d is a construction parameter, not a threshold-degree bound. It covers no part of our universal upper bound on average sensitivity. Candidate verdict: NOT-THIS.

## 3. A power saving for intersective polynomial differences with an exponent depending only on the degree

Author as printed: **OpenAI**. Date: **October 5, 2026**. Opened the actual [main TeX file](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/main.tex) and [introduction](https://github.com/openai/math/blob/main/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/sections/introduction.tex) through the GitHub connector.

Theorem 1.1, exact source text:

```tex
For every integer $k\ge2$, there is a constant $c_k\in(0,1)$ with the
following property. For every intersective polynomial $h\in\Z[x]$ of degree
$k$ with positive leading coefficient, there are a constant $C_h\ge1$ and an
integer $N_h\ge1$ such that, whenever $N\ge N_h$ and $A\subseteq[N]$ satisfy
\[
 (A-A)\cap h(\N_+)\subseteq\{0\},
\]
one has
\[
 |A|\le C_h N^{1-c_k}.
\]
```

The paper sets N_+={1,2,...}, [N]={1,...,N}, and calls an integer polynomial intersective when it has a root modulo every positive integer. This concerns the cardinality of integer sets avoiding nonzero polynomial differences. There is no Boolean threshold function, cube dimension, influence or sensitivity. Polynomial degree controls a density-decay exponent here; neither the quantity nor the model matches T115. Candidate verdict: NOT-THIS.

## Follow-ups and formalisation

Primary formalisation sources opened:

- [Lean family 127 scope note](https://github.com/openai/math/blob/main/lean/docs/127.md): says the formalized result is the uniform 8d sqrt(n) bound for real multilinear threshold polynomials, with sign(0)=1, and distinguishes it from exact extremizers.
- [Comparator challenge](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GotsmanLinial.lean): defines the cube, flip, threshold sign and average sensitivity, and quantifies n>=1 and 1<=d<=n with no regularity or nonvanishing premise. Its challenge theorem ends in `sorry`.
- [Solution Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GotsmanLinial/Main.lean): supplies a separate final `gotsmanLinialStatement` theorem. Its polynomial theorem first removes cube zeros while preserving signs, then constructs the weighted projections rather than assuming their existence. Earlier intermediate lemmas have explicit hypotheses; the final result discharges them.
- [Statement.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GotsmanLinial/Statement.lean): includes the sign-vector encoding and uniform-count interpretation.
- [Lean README](https://github.com/openai/math/blob/main/lean/README.md): points to Comparator verification instructions and recommends compiling small portions.

Also opened the [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md), the solution's [Model.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GotsmanLinial/Model.lean), and the [challenge JSON](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GotsmanLinial.json). The JSON selects `OAI.Combinatorics.GotsmanLinial.Main` as the solution and permits only `propext`, `Quot.sound`, and `Classical.choice`; the challenge placeholder is not an admission in the submitted solution. The release configuration has nanoda disabled. No local Lean build or full dependency audit has been run.

### Later scholarly acknowledgement

Opened the [arXiv page](https://arxiv.org/abs/2604.08095v3) and [full HTML manuscript](https://arxiv.org/html/2604.08095v3) of **Fan Chang, Joseph Slote, Chun-Kai Tseng, Alexander Volberg, and Haonan Zhang**, “The estimates for Boolean surface area of polynomial threshold functions,” revised **October 26, 2026**. The arXiv title is reproduced here; the HTML heading varies slightly. Its abstract describes the conjecture as recently solved by OpenAI; its introduction, equations (1.6) and (1.15), states the bound AS[f]<=8d sqrt(n), and its bibliography identifies the September 25 OpenAI manuscript. This is a direct acknowledgement by later authors working on PTF sensitivity, beyond an automated release catalogue. It is not a referee report or a detailed audit of OpenAI's proof. Its own main quantity remains E sqrt(s_f), as our note says.

### Independent formal-check records

Opened the original pinned report files below through the GitHub connector, following links discovered in Plectis Atlas. These are reports of other people's checks, not checks rerun here.

| Original record opened | What its GotsmanLinial entry reports |
| --- | --- |
| [MathVet, challenge-status.csv, commit 14c7f918cd336d0da03a02aae5a0eed4a429d4db](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/challenge-status.csv) | Family 127; scope `full`; `comparator-sandboxed-pass`; completed October 8, 2026; no shadowing, zero closure problems, and only the three standard permitted axioms. |
| [Carlos Toledo, cert-machine, openai-math-kernel.json, commit 9814e4c06281e34a113ce853d7d99ccce160b750](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json) | `CERTIFIED`, definition holes zero, exit 0, acceptance by both Lean's kernel and nanoda; run October 10, 2026 at 14:00:12 UTC. Release commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. The record expressly limits this certification to the formal challenge. |
| [Neal McBurnett, configs.csv, commit 824beb05b35eb09eeb8c8571be7dbb61975c2e46](https://github.com/nealmcb/openai-math-lean-tooling/blob/824beb05b35eb09eeb8c8571be7dbb61975c2e46/results/cmp-all/configs.csv) | `accepted` for the same solution module; run October 10, 2026; check time 143.007 seconds, peak check RSS 3.3 GiB, nanoda=False. These are the remote report's measurements; no such build was run on this Mac. |

Together with the definitions read above, these records support saying that a matching formalisation exists and independent acceptance has been reported. They do not constitute a referee decision on the manuscript. They concern a pinned release, while the main theorem quotation above was read from the current main branch.

### Expositions, inaccessible lead, and negative searches

Opened [Plectis's manuscript conversion](https://wcook04.github.io/plectis-atlas/papers/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026.html), [its family 127 page](https://wcook04.github.io/plectis-atlas/families/127.html), [oai-math-revised's paper page](https://mathcommunity.github.io/oai-math-revised/papers/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/), and [AI Proved What's exposition](https://aiprovedwhat.com/episodes/127-ptf-average-sensitivity/). They provide explanations and pointers; none substitutes for the primary manuscript or original check records.

A later Research Square item titled “A compensated coupling bound for the average sensitivity of polynomial threshold functions” surfaced through an [AI-generated Gist.Science synopsis](https://gist.science/paper/rs/rs-11323154), dated October 13, 2026. Attempts to open the [original article](https://www.researchsquare.com/article/rs-11323154) and [PDF](https://www.researchsquare.com/article/rs-11323154/v1.pdf) both returned HTTP 403. Accordingly, no mathematical result or author attribution from that inaccessible paper is used here; this is an unverified follow-up lead.

Searched the exact first title with OpenAI/arXiv/error/refutation, `GotsmanLinial` with verification/CERTIFIED, and Gotsman/OpenAI with error/refutation/gap/incorrect; also searched each other candidate's exact title with error/refutation/arXiv. No arXiv copy of the first OpenAI manuscript, specific refutation, published referee report, or detailed independent expert proof audit was located in these searches. This is a search result, not a claim that none exists. Repository issue searches for `sensitivity` and `Gotsman`, and a PR search for `sensitivity`, returned zero matches; the `intersective` issue search also returned zero. The opened repository [history.md](https://github.com/openai/math/blob/main/history.md) contained no matching sensitivity/Gotsman/family-127 entry.

### Follow-ups for the two nonmatching candidates

Opened the primary [family 132 Lean note](https://github.com/openai/math/blob/main/lean/docs/132.md): its formalisation concerns precisely the maximum-sensitivity/block-sensitivity separation, including a fixed exponent greater than 2. No T115 bound follows from that scope.

Opened the primary [family 182 Lean note](https://github.com/openai/math/blob/main/lean/docs/182.md): it covers the square-difference-free special case only, and does not list the general intersective-polynomial candidate as formalized. Opened the [arXiv page](https://arxiv.org/abs/2611.05267) and [full HTML](https://arxiv.org/html/2611.05267v1) of **Steve Fan, Andrew Lott, Ákos Magyar, Máté Matolcsi, and Imre Z. Ruzsa**, “On the van der Corput property for cubes,” submitted **November 3, 2026**. Its introduction explicitly calls the general OpenAI result a claim by a different method, and compares its cubic-case parameters with the authors' own cubic result. That is later discussion of candidate 3, not a refutation and not relevant to T115's model.

## Recommended replacement for “where it stands”

OpenAI's AI-generated preprint “Average sensitivity of polynomial threshold functions” (September 25, 2026) claims the full bound I(f)<=8d sqrt(n), uniformly in degree and dimension. A matching Lean formalisation has independent Comparator acceptance reports, and the October 26 revision of arXiv:2604.08095 explicitly acknowledges and uses the bound. Update the row to solved-claimed; no published referee report or detailed independent mathematical proof audit was located.

## Spot check

Selected the edge-recovery lemma in [the manuscript's actual Section 4](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/sections/04-edge-recovery.tex), with the construction in [Section 3](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/sections/03-weighted-grading.tex). This is the central bridge from a weighted grading to an unweighted edge count; without it, the binomial energy estimate would not bound total influence. The lemma says, for every positive cube weight w and every sign function h, that the number of ordered equal-sign neighbor pairs is at most 2||MH+HM||_HS², where M is the centered grading constructed from w.

Here is a check of its steps, with N=2^n. The invertible multiplier D=sqrt(w) sends the degree filtration V_k to nested spaces K_k of the same dimensions. Their orthogonal increments E_k therefore have dimensions binomial(n,k), so M has squared Hilbert–Schmidt norm nN/4. Coordinate multiplication Z_i commutes with D and increases degree by at most one; self-adjointness gives zero blocks between grades more than one apart.

Set C_i=[M,Z_i]. Its (s,r) block is (s−r) times the corresponding Z_i block. With J acting by (−1)^k on E_k, the operator O_i=(Z_i−JZ_iJ)/2 retains exactly the adjacent blocks and has operator norm at most 1. Conjugating O_i by the unitary acting by i^k on E_k multiplies these blocks by i(s−r); hence it equals i C_i. Thus ||C_i||_op<=1. In the vertex basis C_i(x,y)=(y_i−x_i)M(x,y); choosing a differing coordinate gives |M(x,y)|²<=1/4 for every off-diagonal entry. The phase sign works for both s−r=+1 and −1.

Block orthogonality also gives ||C_i||_HS²<=N. Summing the vertex formula yields

\[
 \sum_{x,y}\rho(x,y)|M(x,y)|^2
 =\tfrac14\sum_i\|C_i\|_{HS}^2
 \le nN/4=\|M\|_{HS}^2.
\]

Let A_0 be diagonal energy, F energy at distance at least two, and A_h energy on equal-sign ordered edges. Subtracting total energy gives F<=A_0. There are nN ordered neighbor pairs, so their total deficit from squared entry 1/4 equals A_0+F<=2A_0. Nonnegativity of each deficit then gives |E_h|/4<=A_h+2A_0. Finally T(x,y)=(h(x)+h(y))M(x,y) detects all diagonal energy and all A_h with squared factor 4; therefore

\[
 |E_h|\le4A_h+8A_0
 \le8(A_h+A_0)\le2\|T\|_{HS}^2.
\]

This independently recovers the claimed factor 2 and checks the ordered-edge normalization and all positivity assumptions in this lemma. No gap was found in this local argument. This does not audit the remaining proof or establish correctness of the main theorem.
