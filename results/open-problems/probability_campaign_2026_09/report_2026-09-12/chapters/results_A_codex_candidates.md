## The written proofs of the Codex campaign, and the twelve candidate solutions

The campaign described in the earlier chapters produced two kinds of record. One is the
ledger: a line of JSON per problem, another per attempt, saying what was read, what was
tried, what the status is. The other is a directory of prose arguments, and it is the part
that carries the mathematics. This chapter is about that directory and about the twelve
rows of the ledger whose status is `candidate_full_solution`.

### What the proofs directory is

The directory is `~/Downloads/Probability_1000_20h_20260906/proofs/`. It
holds 25 files, all written on 6 and 7 September 2026, all plain Markdown, between 2,974
and 12,482 bytes. Between them they address 28 distinct problem identifiers: three files
cover two problems each, because in each of those cases one construction answers two
numbered questions in the same source. The pairs are P0266 with P0267 (Agresti and
Veraar's Problems 4 and 5), P0389 with P0390 (two activated-random-walk window questions),
and P0458 with P0459 (two questions printed together in the bilateral preference paper).
The files, their byte sizes and their SHA-256 digests are pinned in
`written_proof_catalog.json` under the 9 September audit tree, and the digests recorded
there still match the files on disk.

Two things about the directory matter more than its contents at first reading. The first
is that it is not reachable from one field of `attempts.jsonl`. An attempt record carries
`method`, `result`, `obstruction`, `novelty`, `verification`, `independent_review` and
`independent_check`, and for most rows a pointer to the file; but that pointer is spelled
`proof_path` on sixteen records, `proof_file` on seven, and `artifact` on four. Anyone
reading the ledger by iterating over a single key will see part of the directory and
conclude that the rest does not exist. That is what happened on 8 September: the reviewer
of that day worked through eight problems by re-deriving them from their sources before
discovering that written arguments for all eight were already on disk. The accident was
fortunate, because it turned eight readings into eight independent re-derivations, but it
is an accident and not a method.

The second is that the files are, without exception, more conservative about their own
status than a reader would expect of unreviewed self-graded work. Every one carries a
status line in its first paragraph. Five decline credit outright: two say in their headers
that the question was already settled in the literature, two carry the words
`known_rederivation` and `known_consequence` in their own filenames, and one (P0004) says
that its conclusion is already in a published paper which it names. Six more say in their
headers which part of the target they do not reach. The remaining fourteen say some
version of "complete candidate, author-checked, no independent review, no novelty claim",
and several name the specific prior-art lead that would sink the novelty claim if it held:
P0032 names Chacon-Ornstein, Rost and Thorisson; P0276 names the Pak reset constructions;
P0288 names Foley and McDonald; P0208 names Conder's lecture notes for the graph it uses.

### What the September audits found

Two audits read the directory end to end.

The first, on 8 September, read all 25 files and re-derived their load-bearing steps. Its
recorded finding is that no file contained a wrong calculation. The distribution it
reports is: thirteen arguments it judged to settle their stated question as mathematics
(the twelve `candidate_full_solution` rows, with P0266 and P0267 counted separately as the
ledger counts them); five that correctly label themselves as already known, excluded or
rederivations; six honest partials or literal-scope counterexamples whose own headers name
the unsolved part; and one, P0289, live with a verified mechanism and an unchecked
quantitative half. Nine of the thirteen were re-derived independently before the file was
read, and the audit's own summary of that exercise is "nine for nine on the mathematics".
Two errors were found in the course of it, and both were the auditor's own: a misreading
of the shape of the P0209 collapse, corrected by measurement, and a near miss on P0340
where a PDF text extractor renders $\log^2 n$ as "log2 n" and the refutation would have
evaporated had the reviewer read it as a base-2 logarithm.

The second audit, on 9 September, produced the catalog file named above and the defensible
count that governs this whole report. Its statement is worth quoting exactly, because the
temptation to round it up is strong: "Zero newly certified full solutions is the
defensible total when certification requires full source correctness, independent
verification, and verified prior openness/novelty. This does not mean every candidate is
wrong. There are 17 full-answer status claims in the current ledger: 12
candidate_full_solution, 4 proved labels and 1 refuted label. These are claims, not 17
independently certified discoveries." The twelve identifiers are P0032, P0033, P0174,
P0189, P0193, P0208, P0209, P0266, P0267, P0276, P0288 and P0340. Of these, P0032 and
P0174 are positive results; the other ten are counterexamples.

A third audit, on 10 September, chose the best publication candidate among all of them and
reviewed it independently. It selected P0266 and P0267, wrote them up as one paper, found
no mathematical error in the eight ways it tried to break the argument, and recorded that
the two open gates are prior art and a complete formalisation of the stochastic
construction rather than of its algebraic shell. Its comparison table ranks the others,
and three of its rankings are load-bearing for this chapter: P0288 has an identified
antecedent and "a rederivation should not be sold as a new answer"; P0032 carries a
"strong risk of being a classical shift-coupling consequence"; and for P0189 the scope gap
between a general hypothesis and a specialised conjecture "is decisive", so a general
counterexample must not be promoted to a statement about independent matrix ensembles.

### The vocabulary of the ledger, and what each word will and will not bear

Four phrases recur and they are not interchangeable.

*Candidate.* A written argument the author believes complete, with no gap the author can
find, which no second person has checked as mathematics and whose novelty and current open
status are unverified. The ledger's `result_status` for such a row is
`candidate_full_solution` or `candidate_counterexample`; its `verification` field is
`author_checked_not_independently_reviewed` or
`candidate_under_author_and_literature_checks`. Nothing in this report upgrades a
candidate.

*Author-checked.* The author re-derived the load-bearing steps, usually by a second route
recorded in the file, and often with an exact finite control. Six of the twelve files
carry a second route explicitly: P0174 differentiates the Biane profile directly as well
as reweighting the Cauchy profile; P0193 repeats its four crossings in the original
multiplicative variable without hyperbolic functions; P0208 computes the same hitting-time
sum spectrally; P0288 recovers its leading kernel from the odd sector by reflection; P0189
proves norm convergence twice, once through simplicity and once through a trace-power
lower bound; P0340 derives its tree identity both by induction and by telescoping.
Author-checked is stronger than unchecked and weaker than reviewed.

*Scoped review.* Several files carry a receipt from a reviewer who checked a named subset
of the argument against the named sources, with a SHA-256 for the exact bytes reviewed:
P0174, P0189, P0193, P0208, P0209, P0266, P0267, P0276 and P0288 all have one. Every
receipt says in its own text that it is not human certification, not a novelty
certificate, and not proof that the problem is presently open. For P0189 the receipt adds
a disqualification: the reviewer contributed two steps to the amended proof, so the
amended argument needs a different reviewer.

*Known rederivation.* Two files (P0248, P0249) reach a correct conclusion for a question
that another paper already settles, and the ledger sets `admitted: false` and
`result_status: excluded_prior_resolution` for both. Two more (P0096, P0140) are in the
same position with the labels `literature_counterexample_rederived` and
`literature_result_rederived_with_scope_correction`. The arguments survive as
explanations; they carry no solved-problem credit, and the ledger removes them from the
count.

A word on ledger revisions. Both `problems.jsonl` and `attempts.jsonl` are append-only: a
status change writes a new record with the same `problem_id` rather than editing the old
one. Twenty-three of the twenty-eight identifiers in this chapter have two records and one
(P0411) has three, so the last record per identifier is the operative one. Where the two
records disagree I follow the later one and say so. The four material revisions are these.
P0096 moved from `candidate_counterexample` at 19:13Z on 6 September to
`resolved_in_literature` with `admitted: false` at 19:17Z, four minutes later, when
Ahlberg's 2019 paper was found. P0248 and P0249 moved from `candidate_full_solution` to
`excluded_prior_resolution` at 23:37Z the same evening. P0288 gained, at 01:47Z on 7
September, the fields `prior_art_status` and `originality:
not_claimed_prior_art_obstruction_identified` naming Foley and McDonald. And P0276 moved
the other way, from `unsolved` at 00:04Z on 7 September to `candidate_full_solution`
twenty minutes later, when the weighted reset construction was transferred to an
unweighted Cayley graph.

### How the mathematics in this chapter was checked

For each of the twelve candidates I re-derived at least the step the argument rests on,
and I say in one sentence per result whether my re-derivation agreed. Where the step is
algebraic I did it symbolically; where it is a finite identity I enumerated; where it is an
asymptotic I computed the object directly at several scales and compared with the claimed
limit. None of that is independent review in the sense the audits use, because I am reading
the written argument rather than reconstructing the problem from its source, and because a
second reader of the same argument is not a referee. It is enough to catch an arithmetic
slip and not enough to certify a theorem. Nothing below claims novelty; the record says
zero results are independently certified, and I have found nothing that changes that.

### P0032. A finite random prefix in front of a law equivalent to Wiener measure

*The problem as posed.* Burdzy and Scheutzow, *Forward Brownian motion*, arXiv:1302.6958,
Problem 7.5, PDF page 26 (published 2014). The recorded quotation of the question is: "Is it
true that for any process $\{X_t, t \ge 0\}$ whose law is equivalent to BM, we can find some
random piece which we can put in front of $X$ such that the new process is Brownian
motion?" The ledger's `statement_caveat` records the interpretive decision the whole answer
depends on: "No independence or Brownian stopping-time restriction is explicit in the
source. The candidate proof uses a finite nonnegative integer random time depending on
entire paths and auxiliary randomness." The proof file argues that such a restriction cannot
be intended, because a joining time that were a stopping time for the ordinary Brownian
filtration would force the suffix itself to have Wiener law by the strong Markov property,
and then no general equivalent law could be accommodated at all.

*What was found.* The answer is yes, and under the weaker hypothesis of absolute continuity
rather than equivalence. The vehicle is a general lemma: let $(E,\mathcal F,P)$ be a
standard Borel probability space and $\theta$ an invertible, measurable, measure-preserving,
ergodic transformation with measurable inverse; let $Q = fP$ with $f \ge 0$ and
$\int f\,dP = 1$. Then on an extension carrying independent uniform random variables there
is an almost surely finite integer $N \ge 0$ such that $\theta^N Z$ has law $Q$ when $Z$ has
law $P$.

*How.* Write $Lh = h \circ \theta^{-1}$, so that pushing $hP$ forward under $\theta$ gives
$(Lh)P$. Set $a_0 = 1$, $b_0 = f$, and recursively

$$m_n = \min(a_n, b_n), \qquad a_{n+1} = L(a_n - m_n), \qquad b_{n+1} = b_n - m_n .$$

Here $a_n$ is the residual density of the mass not yet matched, transported forward one step
at a time, and $b_n$ is the residual target density. Inductively $0 \le a_n \le 1$, the
$b_n$ decrease below $f$, and since $L$ preserves integrals,
$\int a_n\,dP = \int b_n\,dP =: r_n$ with $r_n \downarrow r$ and
$\sum_{n \ge 0}\int m_n\,dP = 1-r$. Everything turns on $r = 0$.

Iterating gives the exact identity

$$a_n = 1 - \sum_{k=0}^{n-1} L^{\,n-k} m_k .$$

For each fixed $k$, the ergodic theorem for $\theta^{-1}$ gives
$M^{-1}\sum_{n=k+1}^{M-1} L^{\,n-k}m_k \to \int m_k\,dP$ in $L^1(P)$; truncating the sum
over $k$ at $K$ leaves a tail of $L^1$ norm at most $\sum_{k\ge K}\int m_k\,dP$, uniformly
in $M$, which vanishes as $K$ grows because the total matched mass is at most one. Hence
$M^{-1}\sum_{n<M}a_n \to r$ in $L^1$, with $r$ the constant function. Now suppose $r>0$.
Then $B = \{b_\infty \ge \delta\}$ has positive measure for some $\delta>0$, and on $B$ the
bound $a_n \le 1$ gives $m_n = \min(a_n,b_n) \ge \min(a_n,\delta) \ge \min(1,\delta)a_n$.
Averaging in $n$ and integrating over $B$,

$$\liminf_M \frac1M\sum_{n<M}\int_B m_n\,dP \ \ge\ \min(1,\delta)\,r\,P(B) > 0,$$

while the whole sum $\sum_n \int m_n\,dP$ is at most one, so its Cesaro average tends to
zero. That contradiction gives $r = 0$, hence $\sum_n m_n = f$ in $L^1$ and almost
everywhere. The matching is realised by rejection sampling: sample $Z$ with law $P$ and
independent uniforms $U_0,U_1,\ldots$; at stage $n$, if not yet accepted, accept when
$U_n \le m_n(\theta^nZ)/a_n(\theta^nZ)$. By induction the subprobability law of $\theta^nZ$
before the test is $a_nP$, the accepted mass at stage $n$ has law $m_nP$, and the survivors
push forward to $a_{n+1}P$; so $P(N \ge n) = r_n \to 0$ and $\theta^NZ$ has law
$\sum_n m_nP = fP$. Each $U_n$ is independent of $Z$ and of its predecessors, which is why
the test may inspect an entire trajectory.

The application takes $E = C_0(\mathbb R)$ with two-sided Wiener measure $P$ and
$(\theta w)(t) = w(t+1) - w(1)$, which is invertible and measure-preserving, and ergodic
because the path is measurably the bi-infinite i.i.d. sequence of unit-length increment
segments and $\theta$ shifts that sequence by one. Lifting the one-sided density
$f_+ = dQ_+/dW_+$ to $f(w) = f_+(w|_{[0,\infty)})$ and applying the lemma, the forward part
$Y_t = W_{N+t}-W_N$ has exactly the prescribed law, while $W$ on $[0,N]$ followed by
$W_N + Y_{\cdot-N}$ is the original Brownian path, so it has Wiener law. A regular
conditional distribution of $(W,N)$ given $Y$ transfers the coupling to a prescribed $X$
living on its own space.

The file also records the obstruction a reviewer raised and why it does not bite. If the
shift $n(z)$ were a deterministic measurable function of $z$ alone, the shifted law would
have density $g(y) = \sum_{k\in\mathbb Z}\mathbf 1\{n(\theta^{-k}y)=k\}$ with respect to
$P$ -- partition by $n=k$ and use invariance, with Tonelli applying because the summands are
nonnegative. That $g$ is integer-valued almost everywhere and integrates to one, so a
general non-integer $f$ cannot arise this way. It refutes a deterministic strengthening of
the lemma, not the randomised construction; the independent uniforms are exactly what make
the matched densities real-valued.

*My re-derivation.* I implemented the density recursion on finite ergodic systems
($E = \mathbb Z/n$, $\theta$ the shift by one, $P$ uniform, $f$ a random positive density
normalised to mean one) for $n = 5,7,12,60$: the total matched mass came out
$1.000000000000$ in every case, and the law of $\theta^NZ$ matched $fP$ to at most
$1.4\times10^{-16}$. The negative control is the informative one: with the non-ergodic
$\theta$ = shift by two on $\mathbb Z/8$ and $f$ supported on the odd residue class,
exactly $0.500000000000$ of the mass is ever matched and half of $b$ survives forever. So
ergodicity carries real weight and the scheme fails correctly without it. My re-derivation
agreed with the record. I did not verify the $L^1$ ergodic-theorem step in the
infinite-dimensional path setting beyond reading it; the file's own list of load-bearing
points names the direction of $L$ first, which is where an error would hide -- using
$h\circ\theta$ instead of $h\circ\theta^{-1}$ reverses the density transport and breaks the
induction.

*Verification state as recorded.* `result_status: candidate_full_solution` (later of two
records, 7 September 00:19Z; the earlier record at 6 September 16:11Z said
`candidate_proof`), `verification: candidate_under_author_and_literature_checks`,
`independent_review: none`, `current_status: unverified`. There is no Lean development for
this problem. The 8 September audit re-derived the lemma mechanics with the same negative
control and recorded the result as sound, while noting that it read the infinite-dimensional
ergodic step by eye.

*Prior art as recorded.* The file names the leads itself, and they are strong: the
Chacon-Ornstein and Rost filling schemes, Thorisson's shift-coupling theory, Pitman and
Tang, *The Slepian zeros and Brownian bridge embedded in Brownian motion* (2015), Theorem
5.7 (a two-sided random shift, where the nonnegative direction is the extra content here),
and Holroyd and Peres, *Extra heads and invariant allocations* (2005), arXiv:math/0306402,
Theorem 17 with the following remark, whose greedy transport can be restricted to
nonnegative integer displacements on $\mathbb Z$ but is displayed for binary target
capacities. The 8 September audit adds Last, Morters and Thorisson, *Unbiased shifts of
Brownian motion*, arXiv:1112.5373, as the specific paper to read before any novelty claim,
and the 10 September comparison ranks P0032 as carrying a "strong risk of being a classical
shift-coupling consequence". Weak counter-evidence the other way: Burdzy maintains a live
open-problems page and Problem 7.5 is not on it, its nearest entry being a different
concatenation question that is still marked unsolved. A curated page's silence cuts weakly
in both directions.

*Scope and what is open.* The construction gives no bound on $EN$, no computable
finite-lookahead rule, and no version in which the joining time is a stopping time of the
Brownian filtration -- which, as the file notes, is provably impossible in that form. It
proves the statement for absolutely continuous suffix laws, hence a fortiori for equivalent
ones. Whether the source intends an additional implicit restriction on the prefix is an
interpretive question the file flags and does not close, and it is the first thing a
specialist reader would decide.

### P0033. A stationary Galton-Watson flow that is not ergodic

*The problem as posed.* Lyons and Peres, *Probability on Trees and Networks*, version 19
August 2026, Question 17.18, printed page 575, PDF page 592. The ledger's statement: "If a
consistent equivariant Borel flow rule has a stationary probability measure equivalent to
Galton-Watson law, must the associated subtree Markov chain be ergodic?" The context makes
the question sharp. Proposition 17.17 proves ergodicity under strict positivity of all child
weights, and Exercise 17.22 exhibits a non-ergodic example whose stationary measure is
merely absolutely continuous. Equivalence is the extra requirement in question.

*What was found.* No. Take Galton-Watson measure $\mathrm{GW}$ with offspring law
$P(D=2) = 3/5$, $P(D=3) = 2/5$, so the tree is leafless with mean offspring $12/5$. There is
an isomorphism-invariant measurable colour $c(T)\in\{0,1\}$, each value of probability
$1/2$, which is the AND of its children's colours at a two-child vertex and the OR at a
three-child vertex. Both rules preserve unanimity, so every vertex has at least one child of
its own colour; let the flow choose uniformly among those. Then $\mathrm{GW}$ itself is
stationary for the induced chain, while the root colour is invariant along it and takes each
value with probability $1/2$. The chain is not ergodic, and its stationary measure is
$\mathrm{GW}$, hence trivially equivalent to it.

*How.* The technical content is that the colour is a function of the uncoloured tree, with no
residual randomness. Truncate at level $n$, colour the level-$n$ vertices independently
$\mathrm{Bernoulli}(1/2)$, propagate upward by the two Boolean rules, and let $q_n(T)$ be the
probability that the root is $1$, so $q_0 = 1/2$. The one-step mean map is

$$F(p) = \tfrac35 p^2 + \tfrac25\left[1-(1-p)^3\right], \qquad F(\tfrac12) = \tfrac3{20}+\tfrac7{20} = \tfrac12 .$$

Because the root formula is read-once on a tree, $q_{n+1}$ is a multilinear polynomial in the
boundary probabilities, so conditioning on the tree through level $n$ -- that is, on the
offspring numbers at depths below $n$ -- gives $E[q_{n+1}\mid\mathcal F_n] = q_n$. That is a
bounded martingale, convergent almost surely and in $L^2$ to some $q_\infty$ of mean $1/2$.

To rule out a surviving coin, put $r_n = E[q_n^2]$ and read it as the probability that two
independent boundary colourings of the same uncoloured truncation both give root $1$. Each
output has marginal probability $1/2$, and a pair with both marginals $1/2$ satisfies
$P(00) = P(11)$; so at a two-child AND vertex the joint success probability is $r_n^2$, and
at a three-child OR vertex inclusion-exclusion gives
$1 - 2\cdot\tfrac18 + r_n^3 = \tfrac34 + r_n^3$. Different child subtrees are independent,
so

$$r_0 = \tfrac14, \qquad r_{n+1} = \tfrac3{10} + \tfrac35 r_n^2 + \tfrac25 r_n^3 .$$

The increment factors exactly:

$$\tfrac3{10} + \tfrac35 r^2 + \tfrac25 r^3 - r = \left(r-\tfrac12\right)\left[\tfrac25 r^2 + \tfrac45 r - \tfrac35\right] .$$

On $[1/4,1/2]$ the quadratic bracket is negative -- it equals $-3/8$ at $1/4$ and $-1/10$ at
$1/2$ -- while $r-1/2 \le 0$, so the increment is positive. The map is increasing and fixes
$1/2$, so it carries the interval into itself; the competing positive root of
$2r^2+4r-3 = 0$ is $(\sqrt{10}-2)/2 = 0.5811\ldots > 1/2$, so $1/2$ is the only fixed point
there and $r_n \uparrow 1/2$. By $L^2$ convergence,
$E[q_\infty(1-q_\infty)] = 1/2 - \lim r_n = 0$, and nonnegativity forces
$q_\infty\in\{0,1\}$ almost surely. Set $c(T) = q_\infty(T)$ on that probability-one set;
the AND/OR recursion passes to the limit because each step is a continuous polynomial in the
children's values, and it may be applied simultaneously at all vertices, a countable set. For
a global Borel definition, set $c = 0$ off the set where the limit exists and is binary, and
use equal weights on all children where no same-colour child exists; that changes nothing
under $\mathrm{GW}$.

Stationarity is the step that has to be checked rather than asserted, because the flow's
choice depends on a tail function of the whole tree. Write $A_c = \{c(T) = c\}$ and
$\mathrm{GW}_c = \mathrm{GW}(\cdot\mid A_c)$, each event of probability $1/2$. Conditional on
$D = d$ and the child colour vector $(c_1,\ldots,c_d)$, the child subtrees are independent
with child $i$ distributed as $\mathrm{GW}_{c_i}$, because each colour is a measurable
function of its own subtree. The parent colour $c$ is determined by $d$ and that vector, and
$I_c = \{i: c_i = c\}$ is nonempty by the unanimity-preserving rules. Choosing uniformly from
$I_c$ uses no further information about the internal shape of the chosen subtree, so for
bounded measurable $h$,

$$E\left[\frac1{|I_c|}\sum_{i\in I_c} h(T_i) \ \Big|\ D=d,\ (c_i)\right] = \int h\,d\mathrm{GW}_c ,$$

whence $\mathrm{GW}_cK = \mathrm{GW}_c$ for the child-selection kernel $K$, and

$$\mathrm{GW}K = \tfrac12\mathrm{GW}_0K + \tfrac12\mathrm{GW}_1K = \tfrac12\mathrm{GW}_0 + \tfrac12\mathrm{GW}_1 = \mathrm{GW} .$$

The event $A_1$ then satisfies $K(T,A_1) = \mathbf 1_{A_1}(T)$ almost surely: a nontrivial
invariant event of measure $1/2$, so the stationary chain is not ergodic. Strict positivity of
every child weight fails exactly where it must -- at a two-child vertex with colours $0,1$
only the zero child is eligible -- and the source's Section 17.5 definition, printed pages
573 to 574, explicitly permits nonnegative child probabilities and imposes conditional-flow
consistency only at children of positive mass.

*My re-derivation.* I checked $F(1/2) = 1/2$ in exact rational arithmetic; ran the
second-moment recursion exactly for six steps ($1/4$, $11/32$, $6343/16384$, and on, the
denominators roughly cubing each time) and in floating point for two hundred, reaching
$0.49999999996$; and asked a computer algebra system to factor the increment, which returned
$(2r-1)(2r^2+4r-3)/10$ -- the same factorisation up to the constant $1/10$. The quadratic
bracket evaluates to $-0.375$ and $-0.1$ at the endpoints of $[1/4,1/2]$ and its positive
root is $0.58113883$. My re-derivation agreed with the record.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 16:41Z said
`candidate_counterexample`), `verification: candidate_under_author_and_literature_checks`,
`independent_review: none`, `novelty: unassessed`. No Lean development. The 8 September audit
checked every step and, importantly, supplied the stationarity argument in full: it is the
load-bearing claim and the file states it more briefly than the colour construction.

*Prior art as recorded.* The file names Johnson, Podder and Skerman, *Random tree recursions:
which fixed points correspond to tangible sets of trees?*, arXiv:1808.03019, as the relevant
primary source on endogeny, and does not assume its general criteria. The 8 September audit
adds that the tree-automaton and factor-of-i.i.d. literature is where to look, since an
AND/OR read-once formula on a Galton-Watson tree with a fixed point at $1/2$ is a natural
object and the two-valued limit is a Kesten-Stigum-flavoured argument. The ledger's own
`novelty` field is `unassessed`, which is weaker than `unverified`.

*Scope and what is open.* The construction relies on zero child weights, permitted by the
source definition and excluded by Proposition 17.17. It says nothing about flow rules with
strictly positive weights, and nothing about intermediate hypotheses -- positivity on a
subset, or a quantitative lower bound on the weight of the chosen child -- under which an
ergodicity theorem might survive. The offspring law $(3/5,2/5)$ is chosen so that $1/2$ is a
fixed point of $F$; which offspring laws admit such a colour is not addressed.

### P0174. A sharp diameter threshold for free Brownian unimodality

*The problem as posed.* Hasebe and Ueda, *Large time unimodality for classical and free
Brownian motions with initial distributions*, ALEA 15 (2018) 353-374, Problem 3.3;
arXiv:1710.08240v2, PDF page 6, journal page 359. The ledger's statement: "Find the optimal
universal $C$ such that every compactly supported law $\mu$ becomes unimodal after free
convolution with the variance-$t$ semicircle law for all $t \ge C$ times the square of its
support diameter." The source proves $C \le 4$ and prints $2 \le C \le 4$. The ledger's
`statement_caveat` flags the arithmetic: "The source prints $2 \le C \le 4$, but its own
symmetric-Bernoulli threshold $t=4$ and diameter $2$ imply only $C \ge 1$." The file also
records a date discrepancy in the archived PDF, whose arXiv revision date is 14 September
2018 while its manuscript header reads 4 November 2021; both are retained rather than
reconciled.

*What was found.* $C = 1$. If $\mu$ is compactly supported with support diameter $D$, then
$\mu \boxplus S(0,t)$ is unimodal whenever $t \ge D^2$, where $S(0,t)$ is the centred
semicircle law of variance $t$; and the symmetric two-point law shows the threshold cannot be
lowered. No symmetry, density or non-atomicity of $\mu$ is assumed, and $D = 0$ is the
trivial point-mass case.

*How.* Two elementary moment inequalities carry the proof. Let $Q$ be the law of a centred
variable $X$ supported in an interval of length $D$, and set $a = E_QX^2$, $b = E_QX^4$. Then

$$a \le \frac{D^2}{4}, \qquad b + 3a^2 \le D^2 a .$$

For the first, if the supporting interval is $[l,h]$ then $E[(X-l)(h-X)] \ge 0$ gives
$a \le -lh$, and $-lh \le D^2/4$ because $(l+h)^2 \ge 0$ with $h-l = D$. For the second, let
$X'$ be an independent copy; pointwise $(X-X')^4 \le D^2(X-X')^2$, and taking expectations
with $EX = 0$ gives $2b + 6a^2 \le 2D^2a$. That single line fixes both the coefficient $3$
and the appearance of the diameter rather than the radius. Equality in the first forces
$l = -D/2$, $h = D/2$ and $Q$ to put equal mass on the two endpoints.

Now the Cauchy profile. For $R>0$ put
$F_R(u) = \int ((x-u)^2+R^2)^{-1}\,d\mu(x)$. The claim is that $F_R$ has no local minimum of
value at most $1/D^2$. Let $u$ be a stationary point with $F_R''(u) \ge 0$, write $y = R^2$,
and reweight:

$$Z = \int \frac{d\mu(x)}{((x-u)^2+y)^2}, \qquad dQ(x) = Z^{-1}\frac{d\mu(x)}{((x-u)^2+y)^2} .$$

Differentiation under the integral is legitimate because $R>0$ and the support is compact.
Stationarity says $E_Q(X-u) = 0$, so the two inequalities apply to $a = E_Q(X-u)^2$ and
$b = E_Q(X-u)^4$. Differentiating twice,

$$\frac{F_R''(u)}{2Z} = E_Q\frac{3(X-u)^2-y}{(X-u)^2+y} = 3 - 4y\,E_Q\frac1{(X-u)^2+y},$$

so $F_R''(u)\ge0$ together with Jensen's inequality
$E_Q[((X-u)^2+y)^{-1}] \ge (a+y)^{-1}$ gives $(a+y)^{-1} \le 3/(4y)$, that is $y \le 3a$.
The normalisation of $Q$ supplies an exact reciprocal identity, since
$E_Q[((X-u)^2+y)^2] = Z^{-1}$ and $E_Q[(X-u)^2+y] = Z^{-1}F_R(u)$:

$$\frac1{F_R(u)} = \frac{b+2ay+y^2}{a+y} .$$

Therefore, using $b \le D^2a-3a^2$,

$$\frac1{F_R(u)} - D^2 \ \le\ \frac{y^2+2ay-3a^2-D^2y}{a+y} \ =\ \frac{(y-3a)(y+a)+(4a-D^2)y}{a+y} \ \le\ 0,$$

both bracketed summands being nonpositive by $y \le 3a$ and $4a \le D^2$. So every stationary
point with nonnegative second derivative has $F_R(u) \ge 1/D^2$. Equality forces both
summands to vanish, so $y = 3a$ and $4a = D^2$; equality in the variance bound then forces
$\mu$ itself to be the symmetric two-point law on $u \pm D/2$, since on those two points the
reweighting denominator is equal. With $c = D/2$, $R^2 = 3c^2$ and $s$ the displacement from
the midpoint, an exact computation gives

$$F_R(u+s) = \frac{s^2+4c^2}{s^4+4c^2s^2+16c^4}, \qquad F_R(u+s) - \frac1{4c^2} = -\frac{s^4}{4c^2\left(s^4+4c^2s^2+16c^4\right)} < 0 \quad (s\ne0),$$

so the only candidate equality point is a strict maximum, never a local minimum. Every local
minimum therefore has value strictly above $1/D^2$, and the boundary case $t = D^2$ is closed
with the rest.

That settles the question, because for $t \ge D^2$ the level $1/t \le 1/D^2$ can be attained
at most twice: three solutions $u_1<u_2<u_3$ would give either an interior local minimum below
the level, or, if $F_R \ge 1/t$ throughout $[u_1,u_3]$, a local minimum at exactly that level,
and $F_R$ cannot be constant on an interval since it vanishes at infinity. Biane's real
homeomorphism $\psi_t$ then converts the count into unimodality: with $v_t(u) \ge 0$ the
positive solution of $F_{v_t(u)}(u) = 1/t$ where one exists and $v_t = 0$ elsewhere, one has
$p_t(\psi_t(u)) = v_t(u)/(\pi t)$ for the continuous density $p_t$ of $\mu\boxplus S(0,t)$,
so each positive density level corresponds to a level set of a Cauchy profile with at most
two points, and the source's own level-set lemma gives unimodality.

*Sharpness.* Take $\mu = (\delta_{-c}+\delta_c)/2$, so $D = 2c$ and $D^2 = 4c^2$. At the
symmetry centre the profile equation gives $v_t(0)^2 = t-c^2$, and implicit differentiation
gives

$$v_t''(0) = \frac{3c^2-v_t(0)^2}{v_t(0)\left(c^2+v_t(0)^2\right)} = \frac{4c^2-t}{t\sqrt{t-c^2}},$$

which is positive exactly when $t<D^2$. So for $c^2<t<D^2$ the density has a strict interior
local minimum and is not unimodal, and for any proposed $C<1$ a time $t$ strictly between
$\max(C,1/4)D^2$ and $D^2$ satisfies $t \ge CD^2$ while unimodality fails. That proves
$C \ge 1$ without appealing to the source's printed bracket.

*My re-derivation.* Three checks. First, the two moment inequalities: over forty thousand
random centred laws with two to five atoms inside an interval of length one, the maxima of
$b+3a^2-D^2a$ and of $a-D^2/4$ were $8.3\times10^{-17}$ and $-4.5\times10^{-11}$, so both
hold and the first is tight. Second, the second-derivative formula: a computer algebra system
confirmed $F_R''(u) = 2\int\left(3(x-u)^2-y\right)\left((x-u)^2+y\right)^{-3}d\mu$
symbolically on a three-atom measure, and
$(y-3a)(y+a)+(4a-D^2)y = y^2+2ay-3a^2-D^2y$ is an identity. Third, the sharpness, which I did
exactly rather than by scanning, and which is cleaner than the route in the file. Put
$y = t-c^2$, so that $F_y(0) = 1/t$ identically; the profile of a two-atom law is rational,
and clearing denominators gives

$$F_y(u) - \frac1t \ =\ \frac{-u^2\left(u^2+t-4c^2\right)}{t\left(u^4+2tu^2-4c^2u^2+t^2\right)} .$$

So at that $R$ the level set $\{F_y = 1/t\}$ is exactly $\{0\} \cup \{\pm\sqrt{D^2-t}\}$:
three points when $t<D^2$, and the double root at the origin alone when $t \ge D^2$. My
re-derivation agreed with the record; substituting $t = 4c^2$ into the same identity
reproduces the file's quartic equality expansion term for term.

One methodological note. My first attempt counted sign changes of $F_R-1/t$ on a grid and
returned two crossings at $t = 3.99$ with $c = 1$, which read as a contradiction: the third root
sits at $u = \sqrt{D^2-t} = 0.0316$ and the profile is quartically flat near the origin, so a
grid of sixty thousand points over $[-8,8]$ cannot resolve it, and near $t = D^2$ the same grid
reports spurious crossings from floating-point noise. The exact factorisation settles the count.
That is the instrument trap the 8 September audit recorded for P0193 in another guise: state the
resolution of the instrument before believing a count.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 21:19Z said
`candidate_complete_proof`), `verification: author_checked_not_independently_reviewed`,
`independent_review: none`, `novelty: unverified`. A scoped parent review receipt is appended
to the file, naming a report at SHA-256
`f7c00a070ac27d9503d4b486e9c78dbe8ed1809f137836b2dc785ffdc100fd1a` whose own text says it is
not human certification, not a novelty certificate, and not proof of present openness, with
canonical audit-node binding pending. No Lean development; the content is analytic and there
is no finite core worth formalising.

*On the source's printed bracket.* The file, the ledger caveat and the 8 September audit all
record the same reading: the paper's example is the symmetric two-point law on $\{-1,1\}$
with threshold $t = 4$ and diameter $D_\mu = 2$, and the condition is $t \ge CD_\mu^2 = 4C$,
so $t \ge 4$ forces only $C \ge 1$. The audit re-derived the paper's own threshold inside the
paper's own frame, using its Lemma 3.1, before recording this, and stated the fork plainly:
if the printed $C \ge 2$ is right under some reading of $D_\mu$, then the candidate theorem
contradicts the paper and one of the two is wrong. I record the reading once and leave it
there.

*Prior art as recorded.* A bounded search on 8 September on the authors with the problem
number, and on "optimal constant" and "sharp diameter threshold", returned only the paper
itself, its Hokkaido and Kyoto repository copies, and adjacent unimodality work by the same
group. The citation check -- papers citing ALEA 15 (2018) 353-374 and mentioning Problem 3.3
-- is recorded as still owed. The 10 September comparison ranks P0174 as a possible research
note whose normalisation and prior-art questions need especially careful review, partly
because two independent results against one group's stated problems came out of a single
session.

*Scope and what is open.* Compact support is essential; nothing here applies to general
finite-variance inputs. The result concerns unimodality, not the shape of the mode. A later
note of 10 September, recorded as author-derived, controlled by exact symbolic identities and
high-precision numerics, and explicitly not refereed and not novelty-cleared, adds a sharp
mode-curvature bound $p_t''(m_t) \le -(t-D^2)/\left(4\pi(t-D^2/4)^{5/2}\right)$ for
$t>D^2$ with the same extremal law; it is separate progress and changes nothing about
P0174's status.

### P0189. Strong convergence without Brown-measure convergence

*The problem as posed.* van Handel, *The strong convergence phenomenon*, arXiv:2507.00346v2
(11 February 2026), Section 6.9, pages 69 to 70. The ledger's statement: "Does strong
convergence of a family of random matrices imply convergence of empirical
complex-eigenvalue measures of every noncommutative polynomial to its limiting Brown
measure?" The `statement_caveat` is the whole disposition of the result: "This is the
literal general statement. It does not impose independent entries, independence of the
matrix family, or a free limiting family. The narrower Ginibre-with-adjoints question is
recorded as a remaining subclass, not counted again."

*What was found.* No, for the literal general statement. There is a sequence of pairs of
unitary matrices, of growing dimension, converging strongly to the generators of an
irrational rotation algebra, whose sums are nilpotent -- so every empirical eigenvalue
measure of the sum is $\delta_0$ -- while the Brown measure of the limit is Haar measure on
the unit circle. The same example also blocks any universal lower bound on the limiting
spectral radius: every finite matrix has spectral radius zero and the limit has spectral
radius one.

*How.* Fix an irrational $\theta \in (0,1)$ and reduced rational approximants
$p_j/q_j \to \theta$ with $q_j \to \infty$. On the standard basis of $\mathbb C^{q_j}$
indexed by $k$ modulo $q_j$, with $\omega_j = \exp(2\pi i p_j/q_j)$, set

$$U_je_k = \omega_j^ke_k, \qquad Se_k = e_{k-1}, \qquad V_j = e^{\pi i/q_j}S .$$

Both are unitary, and

$$V_jU_j = \omega_jU_jV_j, \qquad U_j^{q_j} = I, \qquad V_j^{q_j} = -I .$$

Put $A_j = U_j+V_j$. Its characteristic polynomial is exactly $z^{q_j}$. The reason is that
$zI - U_j - V_j$ has nonzero entries only on the diagonal, where they are $z-\omega_j^k$,
and on the cyclic superdiagonal, where they are all $-e^{\pi i/q_j}$. Only two permutations
have all factors nonzero: the identity, contributing
$\prod_{k=0}^{q_j-1}(z-\omega_j^k) = z^{q_j}-1$ because $\omega_j$ is primitive; and the
full cycle, whose sign is $(-1)^{q_j-1}$ and whose entry product is
$(-e^{\pi i/q_j})^{q_j} = (-1)^{q_j}e^{\pi i} = (-1)^{q_j+1}$, so that its contribution is
$(-1)^{2q_j} = +1$. The two add to $z^{q_j}$, and Cayley-Hamilton gives
$A_j^{q_j} = 0$: every empirical eigenvalue distribution is $\delta_0$.

Strong convergence is the other half. Let $\mathcal A_\theta$ be the universal unital
irrational rotation C*-algebra generated by unitaries $u,v$ with
$vu = e^{2\pi i\theta}uv$; it is simple with a unique faithful tracial state $\tau$, which
the file takes from the cited primary paper rather than proving. In the norm quotient

$$\mathcal Q = \prod_j M_{q_j}(\mathbb C)\ \Big/ \bigoplus_j M_{q_j}(\mathbb C),$$

the direct sum being the sequences of vanishing operator norm, the classes of $(U_j)$ and
$(V_j)$ are unitaries satisfying the irrational relation exactly, because
$\omega_j \to e^{2\pi i\theta}$. Universality gives a unital homomorphism
$\mathcal A_\theta \to \mathcal Q$; simplicity makes it injective, hence isometric; and the
quotient norm of a bounded sequence is its limsup norm, so for every noncommutative
$*$-polynomial $P$,

$$\limsup_j \left\|P(U_j,V_j,U_j^*,V_j^*)\right\| = \left\|P(u,v,u^*,v^*)\right\| ,$$

and the same for every subsequence, which upgrades the limsup to a limit. An injective
$*$-homomorphism is completely isometric, so amplifying to $M_D(\mathcal A_\theta)$ covers
the survey's definition with fixed finite matrix coefficients. The file also gives a second
route to norm convergence that does not use simplicity: for each $m$,
$\|P_j\| \ge \left[(\mathrm{tr}_D\otimes\mathrm{tr}_{q_j})\left((P_j^*P_j)^m\right)\right]^{1/(2m)}$,
and taking $j$ then $m$ to infinity gives
$\liminf_j\|P_j\| \ge \|P\|$ by faithfulness of the limiting trace, while complete
contractivity of the quotient map gives the matching upper bound.

The normalised traces converge to $\tau$ as well. By the commutation relation every fixed
word is a phase times $U_j^aV_j^b$; for fixed $b \not\equiv 0$ and large $j$ the shift
$S^b$ has no diagonal entries, so the trace is zero, and for $b=0$ and fixed $a \ne 0$ the
geometric sum $\sum_k\omega_j^{ak}$ vanishes once $q_j > |a|$. The identity word has trace
one. Those are the canonical irrational-rotation trace values.

The mismatch is then immediate. Fang, Jiang, Lin and Xu, arXiv:1210.4771, Theorem 12.2,
establishes that the Brown measure of $u+v$ in the tracial von Neumann algebra generated by
the irrational rotation pair is Haar probability measure on the unit circle -- a literature
dependency, not a result proved here. The finite empirical measures are all $\delta_0$ and
do not converge to it. To make the matrices random rather than deterministic, conjugate the
pair by an independent Haar unitary $Q_j$: norms, normalised traces, nilpotency and
eigenvalue distributions are unchanged for every outcome. The two members of the pair are
then dependent, which the file states rather than hides; and the single random matrix
$Q_jA_jQ_j^*$ is already a counterexample for a one-variable polynomial. A block direct sum
of $a$ copies of the $j$-th pair and $b$ copies of the $(j+1)$-st, with $a,b \ge 0$ chosen
by the coin theorem applied to consecutive coprime continued-fraction denominators,
realises the example in every sufficiently large integer dimension.

*My re-derivation.* I computed $\det(zI-U_q-V_q)$ exactly, over $\mathbb Z[m]$ reduced
modulo the minimal polynomial of $m = e^{i\pi/q}$, for $q = 3,4,5,7,8,13$ and with
$p/q = 1/q$. In every case the determinant is $z^q$ on the nose and $A^q = 0$ as a matrix
identity. The first version of this check reduced modulo $m^q+1$ instead of the cyclotomic
polynomial $\Phi_{2q}$, and reported nonzero coefficients for odd $q$; those coefficients
turn out to be integer multiples of $\Phi_{2q}(m)$ -- for $q=3$ the leftover was exactly
$\pm(m^2-m+1) = \pm\Phi_6(m)$ -- so they vanish, and the right modulus makes that visible
instead of leaving it to be noticed. I also confirmed the word traces numerically at
$q = 7$ and $13$, and the file's own warning about numerical eigenvalues: at $q = 64$ and
$q = 256$ a double-precision eigenvalue routine reports a maximum modulus of $0.755$ and
$1.385$ for a matrix whose exact spectrum is $\{0\}$, because these matrices are extremely
non-normal. My re-derivation of the determinant, the nilpotency and the traces agreed with
the record. I did not verify the cited Brown-measure theorem or the simplicity and
unique-trace facts; they are literature inputs.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 21:40Z said
`candidate_complete_counterexample`), `verification:
primary_statement_checked_with_scope_caveat`, the attempt record's own verification field
reading `author_checked_limited_argument`, `novelty: not_claimed`. A scoped parent review
receipt is appended at SHA-256
`509f76b5e525eae23af4b986874988449d19eee3ae92e5550124936f6ee515d3`, and it carries a
disqualification that matters: the parent contributed the two extensions -- the
matrix-coefficient amplification and the trace-power lower bound -- during its first bounded
review on 6 September, so the amended argument still requires a different independent
reviewer. The 8 September audit describes the result as "correct in its concrete half with
the gap in a place the ledger itself had flagged", and lists the strong-convergence step as
one of three loose mathematical ends it left open. No Lean development.

*Prior art and scope as recorded.* `novelty: not_claimed`. The file is explicit that this is
a candidate refutation of the survey's literal implication and is not a refutation for
independent-entry ensembles, free limits, or holomorphic polynomials in independent Ginibre
matrices; it names Yi Han's June 2026 paper, arXiv:2606.01664, as claiming the latter case
and compatible with this construction. The 10 September comparison makes the same point as
a ranking: "Broad-versus-specialized hypothesis scope is decisive. Do not promote a general
counterexample to a result about independent matrix ensembles." The load-bearing obligations
the file lists are the precise survey scope, the primitive-root determinant sign, isometry
of the quotient homomorphism, the faithful-trace interpretation, and the cited Brown-measure
theorem.

*What is open.* The narrower conjectures the survey states for independent Ginibre matrices
and for free limiting families are untouched, and the ledger records them as a remaining
subclass rather than counting them again. Nothing here says what additional hypothesis on a
strongly convergent family would restore Brown-measure continuity.

### P0193. A compact initial law whose free multiplicative evolution is never log-unimodal

*The problem as posed.* Hasebe, Ueda and Wang, *Log-unimodality for free positive
multiplicative Brownian motion*, arXiv:2009.13848v1 (29 September 2020), Problem 4.7, PDF
page 11; published in Colloquium Mathematicum 169 (2022) 209-226. The ledger's statement:
"If $\nu$ is supported on a compact interval $[\alpha,\beta]$ with $0<\alpha<\beta$, must
$\sigma_t$ free-multiplied by $\nu$ be log-unimodal for all sufficiently large times?" The
`statement_caveat` says what the question is for: "This asks whether the support-ratio
restriction in Theorem 4.4 can be removed. Log-unimodality is unimodality after taking
logarithms. The known positive theorem assumes a multiplicatively symmetric log-unimodal
initial law; the question here allows non-log-unimodal initial laws."

*What was found.* No. With $\nu = (\delta_{1/10}+\delta_{10})/2$, supported on
$[1/10,10]$ and so compact and bounded away from zero, the law
$\sigma_t \boxtimes \nu$ fails log-unimodality for every $t \ge 5\pi$. The initial law is
multiplicatively symmetric but is not itself log-unimodal, so the source's positive theorem
for symmetric log-unimodal data does not apply.

*How.* The source supplies the criterion, and the argument is a count of solutions. Lemma
4.1(3), PDF page 8, says that in the normalisation
$\Sigma_{\sigma_t}(z) = \exp\left(\tfrac t2\tfrac{z+1}{z-1}\right)$ the law
$\sigma_t\boxtimes\nu$ is log-unimodal if and only if, for every $R \in (0,\pi)$, the
equation

$$\frac{\sin R}{R}\int_0^\infty \frac{r\xi}{1+r^2\xi^2-2r\xi\cos R}\,d\nu(\xi) = \frac1t \tag{1}$$

has at most two solutions $r>0$. The contrapositive needs four solutions for one $R$.

The integrand is a hyperbolic Cauchy kernel in disguise. Dividing numerator and denominator
by $r\xi$,

$$\frac{r\xi}{1+r^2\xi^2-2r\xi\cos R} = \frac{1}{r\xi+(r\xi)^{-1}-2\cos R} = K_R(\log r + \log\xi), \qquad K_R(s) = \frac1{2(\cosh s - \cos R)} .$$

So with $a = \log 10$ and $u = \log r$, the integral is
$F_R(u) = \tfrac12\left[K_R(u-a)+K_R(u+a)\right]$, and (1) becomes

$$F_R(u) = \frac{R}{t\sin R} . \tag{2}$$

For fixed $R \in (0,\pi)$, $F_R$ is continuous, positive, even, and tends to zero at both
infinities.

Now choose the level. The function $g(R) = R/\sin R$ is strictly increasing from $1$ to
infinity on $(0,\pi)$, because
$g'(R) = (\sin R - R\cos R)/\sin^2R$ and the numerator vanishes at zero with derivative
$R\sin R>0$; and $g(\pi/2) = \pi/2$. So for each $t \ge 5\pi$ there is a unique
$R_t \in [\pi/2,\pi)$ with $g(R_t) = t/10$, and then the right-hand side of (2) is exactly
$1/10$, with $\cos R_t \le 0$.

Two rational inequalities finish it. Since $\cosh(\log 10) = 101/20$,

$$F_{R_t}(0) = K_{R_t}(a) = \frac1{2\left(101/20-\cos R_t\right)} \le \frac{10}{101} < \frac1{10},$$

using $\cos R_t \le 0$; and at $u = a$ the centred kernel alone gives

$$F_{R_t}(a) = \frac{K_{R_t}(0)+K_{R_t}(2a)}{2} \ \ge\ \frac1{4\left(1-\cos R_t\right)} \ \ge\ \frac18 \ >\ \frac1{10},$$

with the same bound at $-a$ by evenness. With $F_{R_t} \to 0$ at both infinities, the
intermediate value theorem gives a solution of $F_{R_t}(u) = 1/10$ in each of the four
disjoint intervals $(-\infty,-a)$, $(-a,0)$, $(0,a)$, $(a,\infty)$. Exponentiating, (1) has
four distinct positive solutions, so Lemma 4.1 is violated. Note which way the two bounds
are uniform: the upper bound at the centre holds for every $R \ge \pi/2$, and the lower
bound at the flanks for every $R \in (0,\pi)$, so a single pair of inequalities covers the
whole half-line $t \ge 5\pi$ at once.

The file repeats the same signs in the original variable without hyperbolic functions, which
is worth having because it makes the boundary time $t = 5\pi$, where $R_t = \pi/2$,
transparent: at $r=1$ both atoms contribute $10/(101-20\cos R) \le 10/101$; at $r = 10$ the
atom $\xi = 1/10$ contributes, with its mass one half,
$1/\left(4(1-\cos R)\right) \ge 1/8$; at $r = 1/10$ the atom $\xi = 10$ does the same; and
the integral vanishes at both ends of $(0,\infty)$.

*My re-derivation.* I solved $g(R) = t/10$ by bisection on $[\pi/2,\pi)$ -- deliberately
bracketed, not scanned -- at $t = 5\pi, 16, 20, 50, 200, 1000, 10^5, 10^8$, confirmed that
the resulting level $R/(t\sin R)$ equals $1/10$ to forty digits in every case, and counted
sign changes of $F_{R_t}-1/10$ on a grid of $u$: four in every case. The two uniform bounds
held with room to spare, $F(0)$ ranging from $0.0826$ to $0.0990$ against the level $0.1$,
and $F(a)$ from $0.1299$ to $0.2550$. My re-derivation agreed with the record.

Two remarks on instruments. A uniform grid over $R \in (0,\pi)$ reports only two solutions at
large $t$, because the relevant $R_t$ approaches $\pi$: measured, $\pi-R_t$ is
$3.1\times10^{-4}$ at $t = 10^5$ and $3.1\times10^{-7}$ at $t = 10^8$, outside any grid that
stops short of $\pi$. Solve for $R$; do not scan for it. And an unbracketed root finder wanders:
my first attempt returned $R = 8.96$ at $t = 200$ and $R = -77.65$ at $t = 1000$, on other
branches of $R/\sin R$ entirely, and happened to report four crossings anyway because $\cos$ and
$\cosh$ do not care. Those rows were discarded and redone by bisection.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 21:54Z said
`candidate_complete_counterexample`), `verification:
author_checked_not_independently_reviewed`, `independent_review: none`, `novelty:
unverified`. A scoped parent review receipt is appended at SHA-256
`25f7346145df9adc8b33ff33d802994613bd24342b25825c6cbc7df0d8d9261a`, which found no gap in
its checked scope and states that structural validation is not mathematical certification.
No Lean development. The 8 September audit re-derived the reduction and the bounds and added
a positive control that is the strongest single piece of evidence for the root counter: on
three cases satisfying the source's Theorem 4.4 hypothesis ($\alpha=1$,
$\beta = 1.1, 1.2, 1.3$) the same counter returns at most two solutions at $t = 1.01D$ and
$t = 10D$, agreeing with the proved theorem.

*In scope, and not covered by the source's own counterexamples.* For this $\nu$,
$\beta^4-3\alpha^4 = 9999.9997$ is not less than $2\alpha^3\beta = 0.02$, so Theorem 4.4
does not apply. The source's Theorem 4.5 and Example 4.8 counterexamples have support
accumulating at zero or unbounded, which is exactly why Problem 4.7 asks about the case
bounded away from zero.

*Prior art as recorded.* Focused primary-source searches on 6 September found the original
paper, the authors' current publication pages, and Auer's 2026 paper on the law started at
one; no matching later resolution of this exact compact-initial-law question was verified.
The ledger's `status_search` field says in its own words that search absence is not
current-open evidence. The 8 September audit's assessment of the residual risk is direct: a
two-atom measure is the first thing anyone would try on this question, so a published note
may already contain it.

*Scope and what is open.* The argument proves failure for every $t \ge 5\pi$ and asserts
nothing about smaller times or about the optimality of $5\pi$. It says nothing about which
weaker hypothesis on $\nu$ would restore eventual log-unimodality; the mechanism suggested
by the file is that $K_R(s) \to \left[4\cosh^2(s/2)\right]^{-1}$ as $R \uparrow \pi$, a
kernel whose width does not diverge, so a separated two-point mixture stays bimodal -- but
that is the motivation, and the finite-time rational inequalities are the proof.

### P0208. An arc-transitive graph that mimics the cycle

*The problem as posed.* Aldous and Fill, *Reversible Markov Chains and Random Walks on
Graphs*, 2002 unfinished monograph, 2014 recompilation, Open Problem 7.27, PDF page 259;
the chapter is internally dated 31 January 1994. The recorded quotation: "Is it true that,
over arc-transitive graphs excluding the $n$-cycles, $\tau^* = O(n\log n)$, $\tau_2 = O(n)$
and $\tau^*/(2\tau_0) = 1+o(1)$?" Here $\tau^*$ is the maximal mean commute time, $\tau_2$
the relaxation time, and $\tau_0$ the stationary-average hitting time. The three assertions
are counted as one question. The sentence before it in the source says why the question is
answerable at all: Example 7.14 shows one can invent vertex-transitive graphs mimicking the
cycle, but it is not clear whether arc-transitive ones exist.

The ledger's `statement_caveat` records a printed defect: "The source definition has a
variable-assignment typo; the intended standard ordered-edge transitivity is used, as in
the surrounding tori examples." Page 254's formula for arc-transitivity, read literally,
would allow the images of two identical starting vertices to differ, which excludes any
graph with a vertex of degree two -- so the proof file works with the standard definition,
transitivity of the automorphism group on ordered adjacent pairs, and says so rather than
claiming to satisfy the misprint.

*What was found.* All three assertions fail. Let $m \ge 5$ be odd and take the lexicographic
product of the $m$-cycle with the edgeless graph on two vertices:

$$V_m = (\mathbb Z/m\mathbb Z)\times\{0,1\}, \qquad (i,b)\sim(i\pm1,c) \ \text{ for } c\in\{0,1\} .$$

This is connected, simple, $4$-regular, arc-transitive, and has $n = 2m$ vertices, so it is
not an $n$-cycle. Its $\tau^*$ and $\tau_2$ are both of order $n^2$, and
$\tau^*/(2\tau_0) \to 3/2$.

*How.* Arc-transitivity first. The dihedral symmetries act on the first coordinate, and
swapping the two vertices inside any single fibre preserves every edge, because the twins are
non-adjacent and have identical neighbourhoods. Given two directed edges, a dihedral symmetry
carries one ordered base edge to the other, and then two independent fibre swaps -- at the
two distinct endpoint fibres -- match both second coordinates.

Hitting times next. The first-coordinate projection is simple random walk on the $m$-cycle,
and at each step the second coordinate is replaced by a fresh fair bit independent of the
base step. So from base distance $j \in \{1,\ldots,m-1\}$ the mean time to reach fibre zero
is the cycle's $H_j = j(m-j)$, from $H_0 = H_m = 0$ and
$H_j = 1+\tfrac12(H_{j-1}+H_{j+1})$; at the first arrival in the fibre the fresh bit lands on
the specified vertex with probability one half. For the twin, let $h$ be the mean hitting
time from $(0,1)$ to $(0,0)$: the first positive return of the base walk to $0$ has mean $m$,
the bit then succeeds with probability one half, and on failure the twin state recurs, so
$h = m + h/2$ and $h = 2m$. Hence

$$h\big((j,b),(0,0)\big) = j(m-j)+m \quad (j \ne 0), \qquad h\big((0,1),(0,0)\big) = 2m .$$

The formula is symmetric in source and target, and gives $2m-1 = n-1$ for adjacent vertices,
which is what the source's Lemma 7.19 requires of any vertex-transitive graph. Its maximum
over $j$ is $\lfloor m^2/4\rfloor+m$, so

$$\tau^* = 2\left\lfloor m^2/4 \right\rfloor + 2m, \qquad \tau_0 = \frac1{2m}\left[2m + 2\sum_{j=1}^{m-1}\left(j(m-j)+m\right)\right] = \frac{m^2-1}{6}+m .$$

The spectral route is independent and short. On functions constant within each fibre the
transition operator acts as the cycle operator, with eigenvalues $\cos(2\pi k/m)$; on
functions antisymmetric within every fibre it is zero. Those two orthogonal invariant
subspaces each have dimension $m$ and exhaust the space, so

$$\tau_2 = \frac1{1-\cos(2\pi/m)} \sim \frac{m^2}{2\pi^2},$$

and the fundamental-matrix trace
$\sum_{k=1}^{m-1}\left(1-\cos(2\pi k/m)\right)^{-1}+m$ equals $(m^2-1)/6+m$, agreeing with
the direct hitting-time sum. Since $n = 2m$, both $\tau^*$ and $\tau_2$ are of order $n^2$,
which defeats the proposed $n\log n$ and $n$ bounds; and

$$\frac{\tau^*}{2\tau_0} = \frac{\lfloor m^2/4\rfloor+m}{(m^2-1)/6+m} \longrightarrow \frac32 ,$$

which defeats the third. These are exact formulas, not estimates.

*My re-derivation.* I built the transition matrix at $m = 5,7,9,11,15,21$ and solved the
hitting-time system by linear algebra: the two recorded formulas are exact at every vertex
and every size, with $\tau^*$ equal to $22, 38, 58, 82, 142, 262$ against the predicted
$2\lfloor m^2/4\rfloor+2m$, $\tau_0$ equal to $9, 15, 22.3333, 31, 52.3333, 94.3333$ against
$(m^2-1)/6+m$, and the second eigenvalue of $P$ giving $\tau_2$ equal to
$1/\left(1-\cos(2\pi/m)\right)$ in every case. The ratio $\tau^*/(2\tau_0)$ reads
$1.2222, 1.2667, 1.2985, 1.3226, 1.3567, 1.3887$ -- climbing toward $3/2$ as it should,
which is worth stating because at small $m$ it is not yet close and a single size would be
unconvincing. Arc-transitivity I checked mechanically rather than by reading the argument:
at $m = 5, 7, 9$ the group generated by the rotation, one reflection and the $m$ single-fibre
swaps carries one arc onto all $4n = 8m$ arcs -- $40$ of $40$, $56$ of $56$, $72$ of $72$.
My re-derivation agreed with the record.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 22:32Z said
`candidate_complete_counterexample`), `verification:
author_checked_not_independently_reviewed`, `independent_review: none`, `novelty:
unverified`, with a scoped parent review receipt at SHA-256
`b968660dbd87588070d48502f0d93a2484ae90df2f368b02875c4694ec5ad409`. This is one of only two
problems in the whole campaign with a machine-checked arithmetic core: the 8 September
session formalised the hitting-time identities in Lean 4.33.1 with Mathlib at
`Prob1000/P0208.lean`, nine theorems, no `sorry` and no `native_decide`, with
`print axioms` showing only `propext`, `Classical.choice` and `Quot.sound`. The audit
records that Lean caught two of its own algebra slips in the process, a wrong ratio identity
and a wrong quadratic-growth identity, both in statements the reviewer had already convinced
himself of by reading. A Lean core for the hitting-time arithmetic is not a formalisation of
the counterexample, and the audit says so.

*Prior art as recorded.* This is the file's own weakest point and it volunteers it. The graph
is classical -- a lexicographic product with an empty graph, the wreath or necklace graph --
and the file cites Conder's 2013 Rogla summer-school notes, page 8, as an independent
description of the same graph and its arc-transitivity, calling that "evidence that the
construction is prior art". Focused searches on 6 September located the original question and
primary graph-theory descriptions but no verified later disposition of Problem 7.27. The 8
September audit's judgement is that a one-page answer to a 1994 question in a famous
unfinished manuscript should be assumed folklore until a literature search says otherwise,
and that this search is the only remaining work on the mathematics. The 10 September
comparison ranks P0208 and P0209 together as older source questions with elementary
counterexamples whose definition and prior-art risks make them weaker first publication
choices.

*Scope and what is open.* The three proposed bounds fail; nothing here says what the correct
bounds are for arc-transitive graphs, and the file makes no claim about them. The
counterexample is one infinite family at a single degree, and the reader who wants to know
how badly the conjecture fails -- whether $n^2$ is the worst case, for instance -- gets no
answer. The continuous-time versus discrete-time normalisation is the source's own
(page 115), and the arc-transitivity convention is the intended rather than the printed one.

### P0209. The relaxation time does not control the central limit theorem

*The problem as posed.* Aldous and Fill, Open Problem 4.30, PDF page 137; the chapter is
internally dated 11 October 1994. For a stationary finite reversible continuous-time chain
and a function $g$ with $E_\pi g = 0$, $E_\pi g^2 = 1$, the source asks for a universal bound

$$\sup_x\left|\mathbb P_\pi\left\{\frac{\int_0^tg(X_u)\,du}{\sigma\sqrt t}\le x\right\}-\Phi(x)\right| \ \le\ \psi\!\left(\|g\|_\infty,\ t/\tau_2\right), \qquad \psi(b,s)\to0 \ \text{ as } s\to\infty,$$

with $\psi$ not depending on the chain. Here $\sigma^2$ is the asymptotic variance rate of
the source's Proposition 4.29 and $\tau_2$ is the relaxation time. The ledger's
`statement_caveat` pins the three normalisations that a counterexample has to respect: "The
source uses asymptotic variance normalization, permits arbitrary continuous transition rates,
and starts in stationarity. The counterexample fixes $\|g\|_\infty$ exactly $2$ and also
survives uniformizing rates to at most $1$."

*What was found.* No such $\psi$ exists. A family of four-state reversible chains, with
$\|g\|_\infty$ pinned at exactly $2$ and $\tau_2$ pinned at exactly $1$, has Kolmogorov
distance to the normal bounded below by $1/2$ in the limit while $t/\tau_2 \to \infty$.

*How.* For an integer $s \ge 3$ put $\varepsilon = s^{-2}$ and $R = s^4$. Let $Y$ be the
stationary two-state chain on $\{0,1\}$ with rate $\varepsilon$ from $0$ to $1$ and rate
$1-\varepsilon$ from $1$ to $0$, so $\pi(Y=1) = \varepsilon$ and the nonzero generator
eigenvalue is exactly $-1$. Independently let $Z$ be a fair sign flipping at rate $R/2$, with
nonzero eigenvalue $-R$. The product $X = (Y,Z)$ has four states, is irreducible and
reversible, has generator eigenvalues $0,-1,-R,-(R+1)$, and therefore $\tau_2 = 1$. Set

$$A = 2\varepsilon+\sqrt{(1-\varepsilon)(1-4\varepsilon)}, \qquad B = \frac{2-A}{1-\varepsilon}, \qquad g(Y,Z) = AZ+B(Y-\varepsilon) .$$

The positive root $A$ solves $A^2-4\varepsilon A+5\varepsilon-1 = 0$, which rearranges to
$A^2+B^2\varepsilon(1-\varepsilon) = 1$; with independence and centring that is exactly
$E_\pi g = 0$ and $E_\pi g^2 = 1$. Also $A+B(1-\varepsilon) = 2$ by construction, and every
attainable $|g|$ is at most $\max\{A+B\varepsilon,\ A+B(1-\varepsilon)\} = 2$ because
$\varepsilon<1/2$, with the value $2$ attained at $Y=1,Z=1$. So $\|g\|_\infty = 2$ exactly,
for every $s$, and $A \to 1$, $B \to 1$.

The stationary autocovariance is read off the two nonconstant coordinate eigenfunctions,

$$E[g(X_0)g(X_u)] = A^2e^{-Ru}+B^2\varepsilon(1-\varepsilon)e^{-u}, \qquad \sigma^2 = 2\int_0^\infty E[g(X_0)g(X_u)]\,du = \frac{2A^2}{R}+2B^2\varepsilon(1-\varepsilon) > 0 .$$

Each fixed member of the family satisfies the ordinary central limit theorem; the point is
uniformity at a time depending on the member.

Take $t = s$ and split $\int_0^sg = F+H$ with $F = A\int_0^sZ_u\,du$ and
$H = B\int_0^s(Y_u-\varepsilon)\,du$. The probability that $Y$ is ever $1$ on $[0,s]$ is at
most $\mathbb P(Y_0=1)$ plus the expected number of $0\to1$ transitions, that is
$\varepsilon+s\varepsilon = s^{-2}+s^{-1} \to 0$. On the complement $H = -B\varepsilon s$, and

$$\left|\frac{H}{\sigma\sqrt s}\right| \ \le\ \sqrt{\frac{\varepsilon s}{2(1-\varepsilon)}} \ \longrightarrow\ 0,$$

using $\sigma \ge B\sqrt{2\varepsilon(1-\varepsilon)}$. The fast component is negligible in
$L^2$:

$$EF^2 = 2A^2\int_0^s(s-u)e^{-Ru}\,du \le \frac{2A^2s}{R}, \qquad E\left(\frac{F}{\sigma\sqrt s}\right)^2 \le \frac{A^2}{RB^2\varepsilon(1-\varepsilon)} \longrightarrow 0,$$

since $R\varepsilon = s^2$. Combining the rare-event bound with Chebyshev, the normalised
integral tends to zero in probability. For any fixed $x>0$ its distribution function
therefore tends to one, so the limiting inferior of the Kolmogorov distance is at least
$1-\Phi(x)$; letting $x \downarrow 0$ gives at least $1/2$. Yet $\|g\|_\infty = 2$ and
$t/\tau_2 = s \to \infty$.

The apparent conflict with variance convergence is worth spelling out, because it is the
part the 8 September audit initially misread. For a coordinate with covariance
$ce^{-\lambda u}$ the exact finite-time variance is
$2c\left[t/\lambda-(1-e^{-\lambda t})/\lambda^2\right]$, and substituting shows
$\mathrm{Var}\left(\int_0^sg\right)/(\sigma^2s)\to1$. The variance has converged. What has
not converged is the shape: the whole variance is carried by an excursion of vanishing
probability, so the normalised squares are not uniformly integrable, and variance
convergence alone cannot force a central limit theorem. The audit's measured numbers make
this concrete: at $s = 1000$ roughly $99.9$ per cent of the mass lies within $0.001$ of the
deterministic point $-0.022$ in normalised units, while $\Phi(-0.022) = 0.491$, giving a
Kolmogorov distance near $0.49$; measured distances were $0.478, 0.505, 0.509, 0.506$ at
$s = 30, 100, 300, 1000$, flat at about one half rather than decreasing.

Finally the rate normalisation. Page 26 of the source permits nonnegative transition rates
with no constraint on their sums, so the family is admissible as it stands; but even a
uniformisation to total jump rate at most one does not rescue the bound. Replace the
generator $Q$ by $Q/R$ and observe for time $Rs$: every outgoing rate is at most
$(R/2+1)/R \le 1$, the relaxation time becomes $R$, the variance rate becomes $R\sigma^2$,
and the time integral has the same law as $R$ times the old one, so both the standardised
law and the ratio $t/\tau_2 = s$ are unchanged.

*My re-derivation.* At $s = 10, 30, 100, 300, 1000$ I evaluated the algebra directly:
$\mathrm{Var}_\pi g = 1.000000000000$ and $\|g\|_\infty = 2.0000000000$ in every case, with
$A^2-4\varepsilon A+5\varepsilon-1$ vanishing to $2\times10^{-16}$; and the three bounds in
the collapse argument read, at $s=1000$, $0.001001$ for the rare-event probability,
$0.022361$ for the normalised slow part, and $1.0\times10^{-6}$ for the normalised fast
second moment, each decreasing in $s$ as the argument requires. My re-derivation agreed with
the record.

*Verification state as recorded.* `result_status: candidate_full_solution` (later record, 7
September 00:19Z; the earlier record at 6 September 22:32Z said
`candidate_complete_counterexample`), `verification:
author_checked_not_independently_reviewed`, `independent_review: none`, `novelty:
unverified`, with a scoped parent review receipt at SHA-256
`d0a58ea91383b4abcbff6b4d85c2515ce723250e2794cee4b76f2b7684d70f14`. No Lean development; the
8 September audit records that the content is a variance computation and a distributional
shape argument with no finite arithmetic core worth formalising, and that it verified the two
exact identities numerically to seven places instead.

One correction the audit made to its own reading, recorded neutrally because it changes the
statement of the mechanism rather than the conclusion: its first pass predicted that the
normalised functional would vanish in probability while its standard deviation also vanished.
The standard deviation stays near one. The functional does vanish in probability, and the
variance is carried by a compound-Poisson excursion of intensity about $1/s$; that is a
sharper statement, and it is the one in the file.

*Prior art as recorded.* Focused searches on 6 September found the original statement and the
author's chapter notes, which discuss fixed-chain Berry-Esseen constants, but no later
resolution of this precise uniform question. The ledger says search absence is not evidence
of current openness or novelty. The 8 September audit adds the same folklore caveat as for
P0208: a 1994 question in a well-known unfinished manuscript, answered by a four-state chain,
should be assumed known until a literature check says otherwise.

*Scope and what is open.* The file is explicit that it refutes the proposed form and proves
no replacement. What it identifies is the missing ingredient: a correct bound must involve a
third quantity beyond $\|g\|_\infty$ and $t/\tau_2$ -- something like the smallest stationary
probability, or a moment condition stronger than the sup norm -- because a spectral gap and a
bounded observable do not prevent the asymptotic variance from concentrating in rare
excursions. The file states that observation as explanatory and does not claim any modified
bound has been proved.

### P0266. The critical Allen-Cahn equation has no maximal second-moment bound

*The problem as posed.* Agresti and Veraar, *Nonlinear SPDEs and Maximal Regularity: An
Extended Survey*, NoDEA (2025), Problem 4, journal page 130 of 150, PDF page 131; the arXiv
version is arXiv:2501.18561 with the question on PDF page 92. The archived published PDF has
SHA-256 `a66ffa2c1d88f2b46d563a3e4d3963bbc0f8623492e7e1837b4ae089008ad091`, and the ledger
records that the published page was rendered and visually read. The ledger's statement: "Does
Theorem 6.4 imply $E\sup_{t\le T}\|u(t)\|_H^2 \le C_T(1+E\|u_0\|_H^2)$, including the source
critical Allen-Cahn model $\gamma^2 = 2$?" The model the survey names is the Ito equation on
the one-dimensional torus

$$du = \left(\Delta u+u-u^3\right)dt + \gamma u^2\,dW$$

with one scalar Brownian driver, and the survey singles out $\gamma^2 = 2$ as the case it
cannot settle: for $\gamma^2<2$ its Section 6.3.2 gives an $L^2(\Omega)$ bound.

*What was found.* No. For deterministic constant initial data $u_0 \equiv a>0$ on the torus,
$E\sup_{t\le T}\|u(t)\|_{L^2}^2 = \infty$ for every $T>0$, while $E\|u_0\|_H^2 = a^2$ is
finite and every fixed-time second moment is finite.

*How.* The construction is a reduction to a Bessel process. Normalise the torus volume to one
and take $u_0 \equiv a$. A spatially constant field has $\Delta u = 0$, and the noise is
one-dimensional, so the solution stays constant in space and solves the scalar equation

$$dU_t = \left(U_t-U_t^3\right)dt+\sqrt2\,U_t^2\,dW_t, \qquad U_0 = a .$$

Let $R_s$ be a four-dimensional Bessel process, $dR_s = dB_s+\tfrac3{2R_s}ds$, started at
$r = 1/(\sqrt2\,a)$, and set $s(t) = (e^{2t}-1)/2$ and

$$U_t = \frac{e^t}{\sqrt2\,R_{s(t)}} .$$

Ito's formula for $z(R) = 1/(\sqrt2 R)$ gives drift $-z^3$ and diffusion $-\sqrt2\,z^2$;
the deterministic time change followed by multiplication by $e^t$ turns those into drift
$U-U^3$ and diffusion $-\sqrt2 U^2$, and replacing the driver by its negative gives the
displayed SDE. A four-dimensional Bessel process never hits zero and has a positive minimum
on each compact interval, so the solution is positive and global; locally Lipschitz
coefficients give pathwise uniqueness, so this is the law of the unique global strong
solution for any prescribed scalar driver.

The tail comes from a finite-horizon hitting estimate for the Bessel process, and the file is
careful to keep it finite-horizon. For $0<b<r$ let
$\tau_b = \inf\{s\ge0 : R_s = b\}$ and fix $S>0$. The function $h(x) = |x|^{-2}$ is harmonic
away from the origin in dimension four, and the process stopped at $\tau_b$ is bounded by
$b^{-2}$, so optional stopping at $\tau_b\wedge S$ gives the exact identity

$$\frac{\mathbb P_r(\tau_b\le S)}{b^2} = \frac1{r^2}-\mathbb E_r\left[R_S^{-2};\ \tau_b>S\right] .$$

The remaining expectation is computed in closed form. Writing $|z|^{-2} = \int_0^\infty
e^{-\lambda|z|^2}d\lambda$ and using the four-dimensional Gaussian transform,

$$\mathbb E_r\left[R_S^{-2}\right] = \int_0^\infty (1+2S\lambda)^{-2}\exp\!\left(-\frac{\lambda r^2}{1+2S\lambda}\right)d\lambda = \frac1{2S}\int_0^1\exp\!\left(-\frac{r^2(1-w)}{2S}\right)dw = \frac{1-e^{-r^2/(2S)}}{r^2},$$

the middle step being the substitution $w = (1+2S\lambda)^{-1}$. Since $R$ never reaches
zero, $\mathbf1\{\tau_b>S\}\to1$ almost surely as $b\downarrow0$, and dominated convergence
against the integrable $R_S^{-2}$ gives

$$\lim_{b\downarrow0}\frac{\mathbb P_r(\tau_b\le S)}{b^2} = \frac1{r^2}-\frac{1-e^{-r^2/(2S)}}{r^2} = \frac{e^{-r^2/(2S)}}{r^2} > 0 \qquad\text{for every } S>0 .$$

Now put $M_S = \sup_{s\le S}(2R_s^2)^{-1}$ and substitute $b = (2x)^{-1/2}$: then
$x\,\mathbb P_r(M_S \ge x) \to e^{-r^2/(2S)}/(2r^2) > 0$, a tail of index one, so
$EM_S = \infty$. Since $U_t^2 = e^{2t}/(2R_{s(t)}^2) \ge (2R_{s(t)}^2)^{-1}$,

$$\sup_{0\le t\le T}U_t^2 \ \ge\ M_{s(T)}, \qquad \mathbb E\sup_{0\le t\le T}U_t^2 = \infty \quad (T>0) .$$

At each fixed time, by contrast, the same Gaussian formula gives
$EU_t^2 = e^{2t}a^2\left(1-\exp\left[-1/(4a^2s(t))\right]\right) < \infty$, consistent with
the existing pointwise second-moment bound. The rare finite-time maxima have a $1/x$ tail for
the squared amplitude, and the file names the place a careless argument would miss it:
replacing a localised stochastic integral by a mean-zero integrable martingale.

The abstract hypotheses are then checked in two settings, which is what makes the example a
counterexample to the theorem's setting rather than to an unrelated equation. In the scalar
Gelfand triple $V = H = V^* = \mathbb R$ with $A = I$, $B = 0$, $F(v) = 2v-v^3$,
$G(v) = \sqrt2 v^2$, the evolution equation is the scalar SDE above; linear coercivity holds
with $\theta = 1$, $M = 0$, and the nonlinear condition reads
$v\left(Av-F(v)\right)-\tfrac12|G(v)|^2 = -v^2 \ge |v|^2-2|v|^2-2$, so the theorem's
coercivity holds with $\theta' = 1$, $M' = 2$; the polynomial local Lipschitz bounds hold
with $\rho = 2$, $\beta = 2/3$, for which $(2\beta-1)(\rho+1) = 1$, the critical value. For
the torus model itself, with $V = H^1$, $H = L^2$, $A = I-\Delta$,

$$\langle v,Av-F(v)\rangle-\tfrac12\|G(v)\|_{L^2}^2 = \|\nabla v\|_2^2-\|v\|_2^2 = \|v\|_{H^1}^2-2\|v\|_2^2,$$

and the polynomial Lipschitz condition follows from
$(H^{-1},H^1)_{2/3,1}\hookrightarrow H^{1/3}\hookrightarrow L^6$ in one dimension, with
Holder for the cubic drift and the resulting $L^4$ embedding for the quadratic diffusion, at
the same critical indices.

*My re-derivation.* Four checks. The Ito reduction: symbolically,
$z(R) = 1/(\sqrt2 R)$ with $dR = dB+\tfrac3{2R}ds$ gives drift exactly $-z^3$ and diffusion
coefficient exactly $-\sqrt2 z^2$, so the reduction is right in the direction it is used. The
Gaussian expectation: the $\lambda$ integral evaluates in closed form to
$\left(1-e^{-r^2/(2S)}\right)/r^2$, and the difference from the claimed value is identically
zero; a Monte Carlo control with four hundred thousand four-dimensional Gaussians agreed to
three decimals at three parameter settings ($0.393762$ against $0.393469$; $0.245212$ against
$0.242348$; $0.245291$ against $0.245421$). The hitting scaling: simulating
$P(\tau_b \le S)/b^2$ at $r = S = 1$, where the claimed limit is
$e^{-1/2} = 0.60653$, gives $0.6281$ and $0.6489$ at $b = 0.30$ with two thousand and eight
thousand steps, $0.5681$ and $0.6312$ at $b = 0.20$, and $0.5069$ and $0.5677$ at
$b = 0.12$ -- in each case rising toward the limit as the step shrinks, which is the correct
signature. My re-derivation agreed with the record.

That last check is where the 8 September audit recorded an instrument failure whose cause I
reproduced. Its first pass showed $P/b^2$ falling with $b$ (1.53, 1.24, 0.84, 0.24), under a
print statement pre-labelled with the expected conclusion. The fall was the step size: at three
thousand steps over $S = 3.19$ a path moves $\sqrt{ds} = 0.033$ per step, and the balls probed
had radius $0.025$ and $0.0125$ -- smaller than one step, and a discrete path cannot enter a ball
it steps over. Before believing a small-ball hitting count, check that $\sqrt{ds}$ is well below
$b$.

*Verification state as recorded.* `result_status: candidate_full_solution` in both records (6
September 23:49Z and 7 September 00:19Z), `verification: author_checked_candidate`,
`independent_review: none` in the attempt, `novelty: not_claimed`. A scoped parent review
receipt is appended at SHA-256
`51bab8e934ed3092ab9849627b7eccf6bdabaedb6aeae7d30aeb6f6cbb53dada`, with the checked proof
hash `3afdb8adf2e2b58a7778f807a90283741394c8203e9541e160ca7cc6f55be870`. This pair was then
selected on 10 September as the campaign's best publication candidate and reviewed
independently, and that review is the most substantial verification any result in this chapter
has: it re-derived the reciprocal Ito equation and the reverse Bessel and time-change
construction, applied bounded optional stopping at the finite horizon, evaluated the Gaussian
inverse-square expectation, derived the maximum tail, then re-derived the conclusion by an
independent expectation-defect argument, and found no error in eight named ways of trying to
break it -- wrong Bessel dimension or time change, eventual hitting substituted for
finite-time hitting, expectation of an unjustified local martingale, dominated convergence
without a dominator, hypotheses violated, incompatible probability spaces, an overextended
moment statement, and the conclusion being already known. Only the last it left open.

A Lean file `EndpointCore.lean` exists from that review and compiles, and the review is
emphatic about what it does not mean: "A compiler success for the supplied conditional core
must not be described as a full Lean proof of the SPDE." The outstanding formal work it names
is the stochastic model itself. There is no verified Lean correspondence for this or any other
probability theorem in the campaign.

*Moment orders, exactly.* The 10 September review sharpens the tail into two-sided bounds: for
$Z = \sup_{t\le T}U_t^2$ and $y>a^2e^{2T}$,

$$\frac{a^2\exp\left[-1/(4a^2S_T)\right]}{y} \ \le\ \mathbb P(Z\ge y) \ \le\ \frac{a^2e^{2T}}{y}, \qquad S_T = \frac{e^{2T}-1}{2},$$

so maximal moments exist exactly for positive orders below $2$ and fixed-time moments exactly
for orders below $4$. The file's own clarification agrees: only the second fixed-time moment is
asserted finite, and the fourth is infinite because a nondegenerate four-dimensional Gaussian
has a strictly positive continuous density at the origin.

*Prior art as recorded.* `novelty: not_claimed`. A first search found Agresti's 2026 paper
*Fractal dimension of singular times for SPDEs*, arXiv:2602.21981, which does not resolve these
questions; its full text was searched for the relevant terms with no hit. The 10 September
review read Assumption 6.1, Theorem 6.4 and Problems 4 and 5 in the journal source, visually
checked the published question page, searched exact question phrases and author names with
endpoint, energy, counterexample and Bessel terms, and read the singular-times and Levy-noise
follow-ups; it found no prior resolution and states plainly that this is not a complete
citing-paper census. Its judgement of the remaining risk is the sharpest sentence available on
any result in this chapter: "This remains the strongest unresolved publication objection. The
Bessel mechanism is classical. Explicit source questions from 2025 help identify relevance,
not priority in September 2026."

*Scope and what is open.* Nothing here applies to $\gamma^2<2$, which the survey already
settles. The zero initial condition alone is not a counterexample. The file distinguishes
$a = 0$, $T = 0$, order $2$, order $4$, and fixed-time versus path-maximum statements, and
claims no failure of the narrower prose variants of the question that add mapping or growth
hypotheses.

### P0267. Continuity in the energy space fails for the same equation

*The problem as posed.* Agresti and Veraar, Problem 5, same page and same locators as P0266.
The ledger's statement: "Under Theorem 6.4, does $L^2$ convergence of initial conditions
imply $L^2\left(\Omega;L^2(0,T;V)\cap C([0,T];H)\right)$ convergence of solutions?" The two
problems are separate numbered questions -- one a bound, one a continuity statement -- and the
ledger counts them separately while one construction answers both.

*What was found.* No, under the same general hypotheses and on the same equation.

*How.* Use a common scalar Brownian driver and initial conditions
$u_0^{(n)} \equiv 1/n$, with limiting initial condition $u_0 = 0$. The solutions exist
strongly and can be constructed simultaneously on that one space for the countable family.
The initial conditions converge deterministically in $L^2$. The limiting solution is
identically zero, because both drift and diffusion vanish at zero. But the P0266 calculation
applied with $a = 1/n$ gives, for every $n$ and every $T>0$,

$$\mathbb E\left\|u^{(n)}-0\right\|_{C([0,T];H)}^2 = \infty ,$$

so convergence in the claimed space cannot hold. The point the file makes about what this
does not contradict is worth keeping: it does not contradict convergence in probability, nor
$L^p$ convergence for $p<2$, and in the two-sided tail bounds above the initial constants
$1/n$ do converge in every subquadratic maximal moment. It is exactly the second maximal
moment that is infinite, and tiny tail coefficients for small initial data do not make an
infinite second maximal moment finite.

*My re-derivation.* The construction is the P0266 reduction applied at $a = 1/n$ together
with the observation that $u \equiv 0$ solves the equation, so my P0266 checks cover it; the
only extra ingredient is that all the $u^{(n)}$ and the zero solution live on one probability
space, which follows from strong existence under locally Lipschitz coefficients for a
prescribed driver. My re-derivation agreed with the record.

*Verification state, prior art and scope as recorded.* Identical to P0266 in every field:
`candidate_full_solution` in both records, `author_checked_candidate`, `independent_review:
none`, `novelty: not_claimed`, with its own scoped review receipt at SHA-256
`23cf03ae222934032f483c2910676dcfe211d2490c2d62b642d28522b1d3b682`. The file's own scope
clarification restricts the claim to the numbered general Problem 5 and does not assert a
resolution of the narrower surrounding prose with additional mapping or growth hypotheses.
The 10 September review treats the pair as one paper.

### P0276. The product condition without cutoff on an unweighted Abelian Cayley graph

This entry is reported as history. On 10 September 2026 the owner retired the Cayley and
cutoff line, because a more general manuscript of his own -- *Sparse unweighted Cayley
realizations and instability of cutoff*, whose stated universal weighted-to-unweighted
realization and near-logarithmic-degree results cover this problem and the sparse-degree
follow-up -- supersedes it. The instruction recorded that day is to stop spending research
effort here and not to revive the older padding lemma's polylogarithmic-degree question as a
new open target. What follows is therefore a record of what the campaign's file contains and
how it was checked, not a live result of this report.

*The problem as posed.* Justin Salez, *Modern aspects of Markov chains: entropy, curvature and
the cutoff phenomenon*, arXiv:2508.21055, Problem 2.4, PDF page 27, with the definitions on
pages 25 to 26; archived SHA-256
`9b58f5e6c2b13103f9ca02ddd53b7890e259b2d93f632c25d3414dd87002e267`. The ledger's statement:
"Is total-variation cutoff equivalent to the spectral product condition for simple random
walks on finite Abelian Cayley graphs?" The two scope facts that decide the disposition are
recorded in the `statement_caveat`: "The source defines uniform choice from a generating set
and places weighted walks in a separate subsequent paragraph. Its statement does not impose a
bounded-degree hypothesis. A weighted reset example alone is insufficient."

*What was found.* For the literal unrestricted statement, no. There is a family of connected
simple undirected unweighted Abelian Cayley graphs satisfying the product condition whose
total-variation profile decays continuously, so cutoff fails. The degree is unbounded.

*How.* For $d \ge 8$ set $m_d = 1+\lceil 2^d\log d/4\rceil$ and
$G_d = (\mathbb Z/2\mathbb Z)^d\times(\mathbb Z/m_d\mathbb Z)$, writing $H_d$ for the cube
factor and $K_d$ for the cyclic factor. The generating set is the disjoint union

$$S_d = \left\{(e_i,k) : 1\le i\le d,\ k \in K_d\setminus\{0\}\right\} \ \cup\ \left\{(x,0) : x \in H_d\setminus\{0\}\right\} .$$

It excludes the identity, is inverse closed, and generates, since adding $(e_1,0)$ to
$(e_1,k)$ produces $(0,k)$. So the Cayley graph is simple, connected, undirected and vertex
transitive, and every edge carries the same weight. Its degree is
$D_d = d(m_d-1)+2^d-1$.

Take the rate-one continuisation and split the jumps by type. With

$$\alpha_d = \frac{d(m_d-1)}{D_d}, \qquad \theta_d = \frac{2^d-1}{D_d}, \qquad \beta_d = \frac{2^d}{D_d},$$

a local jump flips a uniformly chosen cube coordinate and gives the cyclic coordinate an
independent uniform nonzero increment, and a global jump gives the cube a uniform nonzero
increment and leaves the cyclic coordinate alone. The second family is a reset in disguise.
The transition operator for a uniform nonzero cube increment is
$Q_d = \left(2^d\Pi_d-I\right)/(2^d-1)$ with $\Pi_d$ the projection onto the uniform law, so

$$\theta_d\left(Q_d-I\right) = \theta_d\frac{2^d}{2^d-1}\left(\Pi_d-I\right) = \beta_d\left(\Pi_d-I\right),$$

and the cube projection has generator $\alpha_dL_d+\beta_d(\Pi_d-I)$. Since $\Pi_d$ commutes
with the cube semigroup, the projected total-variation distance satisfies the exact identity

$$q_d(t) = e^{-\beta_dt}\,c_d(\alpha_dt),$$

where $c_d$ is the distance for rate-one cube walk. No approximation of a nonzero increment
by a reset is involved.

The whole-space distance is then controlled rather than replaced by its projection. Let $N_t$
count local jumps, Poisson of mean $\alpha_dt$. Conditional on the jump types, their times
and all cube increments, the cyclic coordinate is a sum of $N_t$ independent uniform nonzero
increments, whose distance from uniform is at most $1/m_d$ once $N_t \ge 1$ -- the first
increment has exactly that distance and convolution contracts -- and at most one otherwise.
Coupling to an independent uniform coordinate,

$$0 \ \le\ v_d(t)-q_d(t) \ \le\ e^{-\alpha_dt}+\frac1{m_d} .$$

The cube's own cutoff is then self-contained. With $T_d = d\log d/(4\alpha_d)$, the rate-one
cube coordinates flip at rate $1/d$ and from the all-zero start have sign means $e^{-2t/d}$,
so $\chi^2 = \left(1+e^{-4t/d}\right)^d-1$; at $t = sd\log d/4$ this is
$\left(1+d^{-s}\right)^d-1$, which tends to zero for $s>1$. For $0<s<1$ the sum of
coordinate signs has mean $d^{1-s}$ and variance at most $d$ against stationary mean zero and
variance $d$, so Chebyshev at half the former mean gives
$c_d\left(sd\log d/4\right) \ge 1-8d^{s-1}\to1$. And $\beta_dT_d = 2^d\log d/\left(4(m_d-1)\right)\to1$
by the choice of $m_d$. Combining,

$$\lim_{d\to\infty}v_d(sT_d) = \begin{cases} e^{-s}, & 0<s<1,\\ 0, & s>1.\end{cases}$$

That is not cutoff: a nonvanishing fraction of the decay has already happened gradually over
a time proportional to $T_d$.

The product condition holds. Characters of $G_d$ are indexed by $A \subseteq \{1,\ldots,d\}$
with $a = |A|$ and a character $\psi$ of $K_d$, and the eigenvalues of the jump operator are
$\lambda_{A,\psi} = \left((d-2a)c_\psi+b_A\right)/D_d$ with $c_\psi = m_d-1$ or $-1$ according
as $\psi$ is trivial or not, and $b_A = 2^d-1$ or $-1$ according as $A$ is empty or not. The
three nonconstant sectors give gap candidates
$\left(2a(m_d-1)+2^d\right)/D_d$ for $a \ge 1$, $\psi$ trivial;
$dm_d/D_d$ for $A$ empty, $\psi$ nontrivial; and
$\left(D_d+d-2a+1\right)/D_d$ otherwise. For large $d$ the minimum is the first at $a = 1$:

$$\gamma_d = \frac{2(m_d-1)+2^d}{D_d} = \frac{2\alpha_d}{d}+\beta_d \sim \frac2d .$$

From the limiting profile, $t_d(1/4)/T_d \to 1$ because $e^{-s}>e^{-1}>1/4$ for $s<1$, and
$t_d(3/4)/T_d \to \log(4/3)$ because $e^{-s}$ crosses $3/4$ at that interior point. So
$\gamma_dt_d(1/4) \sim \tfrac12\log d \to \infty$, which is the product condition, while
$t_d(3/4)/t_d(1/4) \to \log(4/3) = 0.2877 < 1$, which is the failure of cutoff.

*My re-derivation.* The reset identity is an algebraic rearrangement and I checked it as
such. The quantitative claims I evaluated at $d = 8,10,12,14,16,20$: $\beta_dT_d$ reads
$0.99317$, $0.99909$, $0.99982$, $0.99996$, $0.99998$, $0.999999$, so the survival factor
really bites on the cube's mixing scale; $1/m_d$ falls from $7.4\times10^{-3}$ to
$1.3\times10^{-6}$; and $\gamma_dt_d(1/4)$ reads $2.03$ up to $2.50$ against
$\tfrac12\log d$ of $1.04$ up to $1.50$, the difference being exactly $\beta_dT_d \approx 1$,
so the file's leading-order claim is right and the correction is the additive constant one.
The $\chi^2$ identity behaves as stated but slowly near $s = 1$: at $d = 40$ it reads
$3.14$ at $s = 0.9$, $0.985$ at $s = 1.1$, and $0.0253$ at $s = 2$, consistent with
$\chi^2 \approx e^{d^{1-s}}-1$. My re-derivation agreed with the record. One honest
limitation of my own check: the Chebyshev lower bound $1-8d^{s-1}$ is vacuous at the
dimensions I could evaluate -- at $d = 40$, $s = 0.5$ it is $-0.26$ -- and becomes useful only
past $d = 64$, so I confirmed the algebra of that step rather than its bite.

*Verification state as recorded.* `result_status: candidate_full_solution` (record of 7
September 00:24Z, which replaced an `unsolved` record twenty minutes earlier when the weighted
reset was transferred to an unweighted graph), `verification: author_checked_candidate`,
`novelty: not_claimed`. This file carries the most detailed scoped review receipt in the
directory: a report at SHA-256
`ee332a2aa7f3ab31cb0ae91a0a745f84eb2b21e0c18f028869602cfdf1b90e7b` on the proof pinned at
`80633cef95af21172e4fc4f0f4c67c89845f5222e9806b74d8de721b4b64dbeb`, recording 8 graphs, 360
characters, 2,720 projection entries, 16 conditional convolutions, 10 product-mass cases and 18
rejected bad controls, plus the full coupling, spectrum and mixing-time brackets, with no gap
found in that scope. No Lean development within the campaign.

The 8 September audit also corrected its own earlier call here, and that correction is why the
proofs directory is described the way it is at the top of this chapter: it first published
P0276 as "not verified, not endorsed -- internal consistency only, the mixing profile is the
whole content and is unchecked", then found the written proof in the campaign tree, checked its
load-bearing algebra, and recorded the construction as sound.

*Prior art as recorded.* `novelty: not_claimed`, and the file volunteers the reason: "The reset
mechanism is classical prior art (often associated with Pak counterexamples); novelty, if any,
would concern this exact unweighted realization and its application to the literal source
statement." Searches found the literal Salez statement and related nilpotent-group conjecture
formulations but no verified prior disposition. The 10 September comparison ranks it as
potentially high interest with the decisive question being its relationship to the community's
intended conjecture, given the unbounded degree; and the owner's retirement supersedes the line.

*Scope and what is open.* The degree is about $2^dd\log d/4$ on a group of size about
$2^{2d}\log d/4$, so of order $\sqrt{|G|}$ times a logarithm. The file states plainly that
the construction says nothing against the bounded-degree transitive-expander problem or
almost-sure cutoff for uniformly random generating sets, and the 8 September audit adds the
question that decides the significance and was left unchecked: whether the workshop question
and the conjecture the survey cites carry a degree bound that the printed Problem 2.4 does
not.

### P0288. A rank-two transition asymptotic for a killed chain

*The problem as posed.* Phil Pollett, *Quasi-stationary distributions for queueing and other
models*, Queueing Systems 100 (2022) 241-243; arXiv:2202.05428, Section 2, PDF page 2. The
whole three-page preprint was read, including the discussion distinguishing lambda-null
recurrence from lambda-transience. The ledger's statement: "For a lambda-transient
irreducible countable transient class with almost-sure absorption, must every finite strictly
positive limit of $t^a e^{\lambda t}p_t(i,j)$ factor as $Ax_im_j$, with invariant or
subinvariant positive factors?" The `statement_caveat` restricts the target: "The question is
the factorization assertion (ii). Neighboring existence, common-exponent and survival claims
are not multiplied into extra entries or all declared resolved."

*What was found.* No. A nearest-neighbour continuous-time walk on $\mathbb Z$, killed
uniformly and at an extra rate at the origin, has a limiting kernel of rank two.

*How.* Take transient labels $C = \mathbb Z$ and a cemetery. From each $i$ jump to each
neighbour at rate one; kill at rate $\kappa>0$ everywhere and at an additional rate $v>0$
when $i = 0$. The generator on the transient class is $Q = \Delta-\kappa I-v|0\rangle\langle0|$
with $(\Delta f)(i) = f(i+1)+f(i-1)-2f(i)$. Exit rates are at most $2+\kappa+v$, so the chain
is stable and nonexplosive with a unique transition function; the class is irreducible because
every finite nearest-neighbour path has positive probability of being completed before
killing; and independent rate-$\kappa$ killing gives absorption almost surely. Relabelling
$\mathbb Z$ by the odd and even positive integers puts $C$ in bijection with a countably
infinite set as the source requires, with the cemetery distinguished from the lattice origin.
Put $K = -\Delta+v|0\rangle\langle0|$ on $\ell^2(\mathbb Z)$, a bounded nonnegative
self-adjoint operator, and $p_t(i,j) = e^{-\kappa t}\langle\delta_i,e^{-tK}\delta_j\rangle$.

The resolvent is explicit. For real $s>0$ put $D(s) = \sqrt{s(s+4)}$ and
$r(s) = \left(s+2-D(s)\right)/2 \in (0,1)$. The free resolvent is
$R_s^0(i,j) = r^{|i-j|}/D$: indeed $r+r^{-1} = s+2$ solves the homogeneous nearest-neighbour
resolvent recurrence, the jump of the first difference at $i = j$ is $D$, and decay at
infinity selects that root. The rank-one perturbation at the origin then gives

$$R_s(i,j) = \frac{r^{|i-j|}}{D}-\frac{v\,r^{|i|+|j|}}{D(D+v)} . \tag{1}$$

Write $a = |i-j|$, $b = |i|+|j|$, $q = \sqrt s$. As $q \to 0$,
$D = 2q+\tfrac14q^3+O(q^5)$ and $\log r = -q+\tfrac1{24}q^3+O(q^5)$, so

$$\frac{r^a}{D} = \frac1{2q}-\frac a2+\left(\frac{a^2}4-\frac1{16}\right)q+O(q^2), \qquad \frac{v}{D+v} = 1-\frac{2q}{v}+\frac{4q^2}{v^2}+O(q^3),$$

and subtracting the two terms of (1) cancels the pole:

$$R_s(i,j) = \frac{b-a}{2}+\frac1v-L_{ij}\sqrt s+O(s), \qquad L_{ij} = \frac{b^2-a^2}{4}+\frac bv+\frac2{v^2} . \tag{2}$$

A bare Laplace expansion is not a pointwise Tauberian theorem for an off-diagonal transition
probability, and the file says so; what makes the inversion legitimate is that the explicit
resolvent supplies the spectral measure. For $0<E<4$ set $s = -E+i0$: then
$D = i\sqrt{E(4-E)}$ and $r = 1-E/2-i\sqrt{E(4-E)}/2$, and on a small interval
$0<E<\varepsilon$ formula (1) has smooth boundary values with no denominator zero, so
Stieltjes inversion gives an absolutely continuous density there. The coefficients of the
convergent expansion in $q$ are real, so the $O(s)$ term of (2) is real on that interval and
the first possible further imaginary contribution is $O(E^{3/2})$:

$$\frac{d\mu_{ij}}{dE}(E) = -\frac1\pi\operatorname{Im}R_{-E+i0}(i,j) = \frac{L_{ij}}{\pi}E^{1/2}+O(E^{3/2}) . \tag{3}$$

There is no atom at zero, since $sR_s(i,j)\to0$; spectral mass outside $[0,\varepsilon)$
contributes $O(e^{-\varepsilon t})$, and the total variation of an off-diagonal spectral
measure is finite by Cauchy-Schwarz for spectral projections, so high-energy atoms are
harmless. Integrating (3) against $e^{-tE}$ with $u = tE$ and $\Gamma(3/2) = \sqrt\pi/2$,

$$\lim_{t\to\infty}t^{3/2}e^{\kappa t}p_t(i,j) = C_{ij} = \frac{\left(|i|+2/v\right)\left(|j|+2/v\right)+ij}{4\sqrt\pi}, \tag{4}$$

using $b^2-a^2 = 2(|i||j|+ij)$. Every $C_{ij}$ is finite and strictly positive, including for
$i$ and $j$ of opposite signs, because $\left(|i|+2/v\right)\left(|j|+2/v\right)>|ij|$; so
$\lambda = \kappa$ is the decay parameter, and the exponent $3/2$ is the unique one giving a
finite strictly positive limit for each pair, which is the source's smallest-exponent wording.
Monotone convergence in the resolvent integral, with (2), gives
$\int_0^\infty e^{\lambda t}p_t(i,j)\,dt = \left(|i|+|j|-|i-j|\right)/2+1/v<\infty$, so the
class is lambda-transient in exactly the source's sense.

The obstruction is then a two-by-two determinant. At $v = 2$ and lattice labels $i,j\in\{0,1\}$,

$$\left(C_{ij}\right) = \frac1{4\sqrt\pi}\begin{pmatrix}1&2\\2&5\end{pmatrix}, \qquad \det = \frac1{16\pi}>0 ,$$

and every matrix of the form $Ax_im_j$ has all its two-by-two minors zero. Allowing
subinvariant vectors cannot change that algebraic necessity.

The file adds a second, structural obstruction from the odd sector, which is worth having
because it does not rely on the numerical minor. Reflection about the origin commutes with
$K$, and on odd functions the killing potential vanishes, so for positive $i,j$ the defect
terms in (1) cancel and

$$H_t(i,j)-H_t(i,-j) = k_t(i-j)-k_t(i+j), \qquad k_t(n) = \frac1{2\pi}\int_{-\pi}^{\pi}e^{-2t(1-\cos\theta)}\cos(n\theta)\,d\theta ,$$

with $H_t(i,j) = e^{\kappa t}p_t(i,j)$. The difference of cosines is
$2\sin(i\theta)\sin(j\theta) = 2ij\theta^2+O(\theta^4)$, and Gaussian scaling around zero with
exponential suppression away from it gives
$t^{3/2}\left[H_t(i,j)-H_t(i,-j)\right]\to ij/(2\sqrt\pi)$, matching (4). A strictly positive
symmetric rank-one kernel invariant under simultaneous reflection would have an even positive
factor and hence satisfy $C_{ij} = C_{i,-j}$, so a nonzero odd-sector limit rules out rank one
independently of the minor.

*My re-derivation.* Four levels, all agreeing. The resolvent formula (1): I solved
$(s+K)x = \delta_j$ numerically on $\{-600,\ldots,600\}$ at $s = 0.5, 0.1, 0.02$ and compared
thirty entries against the formula, with maximum discrepancy $1.3\times10^{-15}$. The
expansion (2): symbolic series in $q$ for six index pairs reproduced both the constant
$(b-a)/2+1/v$ and the coefficient $L_{ij}$ exactly -- for instance $L_{11} = 5/2$,
$L_{1,-1} = 3/2$, $L_{23} = 9$, $L_{2,-3} = 3$ at $v = 2$, each matching
$(b^2-a^2)/4+b/v+2/v^2$. The limit (4): diagonalising $K$ and evaluating $t^{3/2}H_t$ at
$t = 100, 400, 1600$ on a lattice wide enough that the boundary is invisible gives, for
$(0,0)$, $0.138737$, $0.140457$, $0.140899$ against the claimed $0.141047$, and similarly for
$(0,1)$, $(1,1)$ and $(1,-1)$, each rising monotonically toward its claimed value. And the
minor formed from the measured entries reads $0.019532$, $0.019802$, $0.019871$ against
$1/(16\pi) = 0.01989437$. The 8 September audit carried the same computation out to
$t = 6400$ and recorded agreement to about $3\times10^{-4}$. My re-derivation agreed with the
record at every level.

*Verification state as recorded.* `result_status: candidate_full_solution` in the later record
(7 September 01:47Z), `verification: complete_author_checked_candidate` in the attempt,
`independent_review: scoped_original_packet_review_completed_no_originality_certificate` with
the report `P0288_killed_chain_candidate_review.md` at SHA-256
`94a89d6e5bbadef6026a0ff1644f33bbab4093f1736019bbe55f6439cd2bc150`, reviewing the packet
pinned at `08d929d170e30f914ffbfcd338b98b270aad706a9bdee819fba1c0ddd2654d46`. No gap was found
in the checked source hypotheses and spectral calculation. No Lean development.

*Prior art as recorded, and it is the decisive field here.* The later record adds
`originality: not_claimed_prior_art_obstruction_identified` and a `prior_art_status` naming
Foley and McDonald, *Yaglom limits can depend on the starting state*, arXiv:1709.07578,
equations (36), (45) and (46) -- a paper Pollett himself cites. The reduction, attributed in
the file to the reviewer rather than to Foley and McDonald, runs as follows. Let $J$ be their
substochastic nearest-neighbour hub chain with inward probability $a$, outward $b$, $a+b = 1$,
$0<b<1/2$, and absorption probability $a$ at the hub; put $B = J^2$ on the even sites,
$\mu = 4ab$, $r = \sqrt{a/b}$. Their ballot formulas give, for fixed even $x,y$ with
$y \ne 0$,

$$B^n(x,y) \sim D_{xy}\mu^nn^{-3/2}, \qquad D_{xy} = \frac{r^{|x|-|y|}}{2\sqrt\pi}\left[(1+|x|)(1+|y|)+xy\right] .$$

Rate-one Poissonisation with transient generator $B-I$ and the missing row rate sent to the
cemetery gives $p_t(x,y) = e^{-(1-\mu)t}E\left[a_N\right]$ with $a_n = B^n(x,y)/\mu^n$ and
$N \sim \mathrm{Poisson}(\mu t)$; the global bound $a_n \le C(1+n)^{-3/2}$ makes
$(\mu t)^{3/2}a_N$ uniformly bounded on $\{N \ge \mu t/2\}$ and convergent in probability to
$D_{xy}$, while on the complement a Poisson lower-tail bound dominates the polynomial
prefactor, so $t^{3/2}e^{(1-\mu)t}p_t(x,y) \to \mu^{-3/2}D_{xy}$. At sites $2$ and $4$ the
polynomial bracket matrix is $\begin{pmatrix}13&23\\23&41\end{pmatrix}$ with determinant $4$,
and the diagonal powers of $r$ cancel in that principal minor, so the continuous-time limiting
minor is $\mu^{-3}/\pi>0$: the same obstruction, from published discrete formulas plus a proved
Poissonisation step. The file concludes that this "does rule out treating the present packet as
a certified original discovery". The 10 September comparison says it in one line -- "A
rederivation should not be sold as a new answer" -- and the 8 September audit, having verified
the mathematics numerically, calls it "confirmed mathematics and probably known". I agree with
that reading and have nothing to add.

*Scope and what is open.* The packet addresses assertion (ii) only. It makes no claim to
characterise all limiting conditional distributions and does not refute the separate
survival-exponent assertion (iii), nor the rank-one theorem in the lambda-positive recurrent
setting. The file records one conditional observation on the common-exponent assertion -- if
finite strictly positive pure-power limits exist for every pair, then irreducibility and the
Chapman-Kolmogorov lower bound, applied in both directions at times differing by a fixed
constant, force the exponents equal -- and explicitly declines to count it as another result,
since it does not prove existence of all pairwise limits from one pair. Whether the exact
continuous-time corollary or the delta-killing realisation was previously published remains
unverified.

### P0340. The drawn length of a critical beta-splitting tree is linear, not $n\log^4n$

*The problem as posed.* Aldous and Janson, *The Critical Beta-splitting Random Tree II:
Overview and Open Problems*, arXiv:2303.02529v3, manuscript dated 17 April 2025; the source
PDF has SHA-256
`a93a520bc7e7f1579802bfb87ac8888712aadd5906c0980ca15d2efd4fa7735d`. Open Problem 14, PDF
pages 54 to 55, proposes that the expected drawn length of $\mathrm{DTCS}(n)$ grows roughly
like $n(\log n)^4$. The ledger's statement: "Determine the expected total vertical length in
the minimal integer-height drawing of DTCS(n); the source specifically proposes growth on the
scale $n(\log n)^4$," with the caveat that "The source drawing recursion is authoritative.
This is expected drawn length, not ordinary total edge count or the continuous-time total
length." The drawing convention is the source's own equations (72) and (73): for a finite full
rooted binary tree with children $A,B$,

$$h(T) = 1+\max\left(h(A),h(B)\right), \qquad \ell(T) = \ell(A)+\ell(B)+2+\left|h(A)-h(B)\right| ,$$

with both functionals zero on a single leaf. The source's own symbol $L$ is used both for
random-leaf depth and for expected drawn length, and the file distinguishes them throughout.

*What was found.* The proposed scale is wrong: $E\ell(T_n) = \Theta(n)$, and in fact
$E\ell(T_n)/n$ converges to an explicit finite constant, which is a convergent series of mean
heights of finite trees rather than a closed form.

*How.* The refutation is a deterministic inequality plus the authors' own theorem. Let $n(T)$
be the number of leaves, $h(T)$ the graph height with leaf height zero, $S(T)$ the sum of the
graph depths of the leaves, and $\ell(T)$ the drawn length. Then

$$2\left(n-1\right) \ \le\ \ell(T) \ \le\ S(T) . \tag{1}$$

The upper bound is an induction on the recursion: a full binary tree with $i$ leaves has
height at most $i-1$, so if the children have $i$ and $n-i$ leaves then
$2+|h(A)-h(B)| \le 2+\max(i-1,n-i-1) \le n$, which is exactly the increment
$S(T)-S(A)-S(B)$. An independent derivation by telescoping gives more:

$$\ell(T) = \sum_{v\ \mathrm{internal}}h(T_v)+h(T), \qquad S(T) = \sum_{v\ \mathrm{internal}}n(T_v),$$

because when the drawn edge differences are summed each child height is subtracted once and
each internal parent height added twice, and leaves contribute nothing; then
$h(T_v) \le n(T_v)-1$ over the $n-1$ internal vertices, together with $h(T)\le n-1$, gives
(1) again. The two routes are worth having separately: the comb attains the upper bound with
$\ell = S$, while the balanced four-leaf tree has $\ell = 6$ and $S = 8$, so neither an
inequality reversal nor a confusion with total edge count is hiding in (1).

Now let $D_n$ be the graph depth of a uniformly chosen leaf conditional on the realised tree,
so $ES(T_n) = nED_n$ by conditional averaging. The source's own Theorem 3, PDF page 12 -- an
established Aldous-Pittel and Aldous-Janson result -- gives
$ED_n \sim \tfrac3{\pi^2}(\log n)^2$. So

$$2(n-1) \ \le\ E\ell(T_n) \ \le\ \left(\tfrac3{\pi^2}+o(1)\right)n(\log n)^2, \qquad \frac{E\ell(T_n)}{n(\log n)^4} \longrightarrow 0, \tag{2}$$

which rules out both a positive-constant asymptotic and two-sided comparability with
$n(\log n)^4$, and by Markov's inequality gives $\ell(T_n)/\left[n(\log n)^4\right]\to0$ in
probability. The published random-leaf theorem is credited rather than claimed.

The file also supplies the upper order without that theorem, which matters if a reader does
not want to lean on it. Along a uniformly chosen leaf, the clade size $M$ has transition law
$\mathbb P(M_{t+1} = j\mid M_t = m) = 1/\left[H_{m-1}(m-j)\right]$ for $1\le j<m$, obtained by
multiplying the source split probability $m/\left[2H_{m-1}j(m-j)\right]$ by the size-bias
factor $2j/m$, with $H_k$ the harmonic number. The next clade is at most $m/2$ with
probability at least $1/(2H_{m-1})$, since there are $\lfloor m/2\rfloor$ such terms each at
least $1/\left[H_{m-1}(m-1)\right]$. Taking the potential $V(m) = (\log m)^2$, on that event
$V(m)-V(M_{t+1}) \ge 2\log2\log m-(\log2)^2 \ge \log2\log m$, the decrease is nonnegative
otherwise, and $H_{m-1}\le(1+1/\log2)\log m$ for $m \ge 2$, so the expected potential drop per
step before absorption is at least $c_0 = (\log2)^2/\left[2(1+\log2)\right]>0$; the chain
strictly decreases, so absorption happens by time $n-1$, and summing gives
$c_0ED_n \le (\log n)^2$. That avoids deriving an expectation bound from a probability-only
maximum-height bound.

The stronger conclusion is the linear limit. With $H_m = Eh(T_m)$ and $H_1 = 0$,

$$\frac{E\ell(T_n)}{n} \longrightarrow c_\ell := \sum_{m\ge2}\frac{a(m)H_m}{m} = \frac6{\pi^2}\sum_{m\ge2}\frac{H^{\mathrm{harm}}_{m-1}H_m}{m(m-1)}, \qquad 2 \le c_\ell<\infty, \tag{3}$$

where $a(j) = 6H^{\mathrm{harm}}_{j-1}/\left[\pi^2(j-1)\right]$ is the established fixed-$j$
limit of the tagged occupation probability $a(n,j)$, and the superscript distinguishes harmonic
numbers from mean heights. The proof has three steps. First, $H_m = O\left((\log m)^2\right)$:
at each unabsorbed step the conditional probability of halving is at least
$p_m = 1/\left(2H^{\mathrm{harm}}_{m-1}\right)$, and using fresh uniforms at successive
transitions couples successful halvings from below by independent Bernoulli variables, so the
absorption time is dominated by a sum of $b_m = \lceil\log_2m\rceil$ independent geometric
variables; from $e^{p/4}\le1+p/2$ one gets $Ee^{pG/4}\le3$, and a union bound over the $m$
leaves -- needing no independence among their depths -- gives
$\mathbb P\left(h(T_m)>t\right)\le\min\left\{1,m3^{b_m}e^{-p_mt/4}\right\}$, whose integral is
$H_m \le \frac4{p_m}\left(\log m+b_m\log3+1\right) = O\left((\log m)^2\right)$. Second, a
uniform dyadic-block bound on the occupation measure: once the decreasing chain enters
$(b,2b]$ it exits below $b$ at each step with conditional probability at least
$1/\left(2H^{\mathrm{harm}}_{2b-1}\right)$ and cannot return, so
$\sum_{j=b+1}^{2b}a(n,j) \le 2H^{\mathrm{harm}}_{2b-1}$ uniformly in $n$, whence
$\sum_{j=b+1}^{2b}a(n,j)H_j/j \le C(1+\log b)^3/b$ and the dyadic tail above any cutoff
vanishes uniformly in $n$ -- which is exactly the tail control a bare pointwise limit does not
supply. Third, the telescoping identity together with the branching property and the source's
own occupation formula $EN_n(j) = na(n,j)/j$ gives

$$E\ell(T_n) = n\sum_{j=2}^n\frac{a(n,j)H_j}{j}+H_n , \tag{4}$$

and $H_n/n \to 0$ finishes (3); the deterministic lower bound in (1) gives $c_\ell \ge 2$.

*Where the source's heuristic breaks.* The file locates it in one factor. The source's own
occupation identity on PDF page 29 is $EN_n(m) = na(n,m)/m$, so for an additive split toll
$b(m)$ the exact expected total divided by $n$ is $\sum_m a(n,m)b(m)/m$; the first heuristic
line of equation (75) on page 55 omits the factor $1/m$, using $n\,a(n,m)$ as the clade count
instead of $(n/m)a(n,m)$. The 8 September audit states the consequence arithmetically: with
the wrong count the sum behaves like $\sum\log^3m/m$, which diverges like $\log^4n$ and
reproduces the conjecture exactly, while with the right count it is
$\sum\log^3m/m^2$, which converges and gives $\Theta(n)$. The hard constraint that catches it
in one line is that $\sum_mN_n(m) = n-1$ exactly, so a clade count of order $n\log m/m$ is
impossible -- it would sum to $n\log^2n$. The file adds that inserting the missing factor alone
does not establish a corrected sharp asymptotic, because the heuristic's further approximations
of absolute height differences are also unproved; the linear limit (3) is proved by a separate
argument that does not replace an absolute difference by a difference of expectations.

*My re-derivation.* I enumerated all $2{,}056$ full binary trees with up to nine leaves and
checked three things on each: the deterministic sandwich $2(n-1)\le\ell(T)\le S(T)$, the
telescoping identity $\ell(T) = \sum_{v\,\mathrm{internal}}h(T_v)+h(T)$, and
$S(T) = \sum_{v\,\mathrm{internal}}n(T_v)$. Zero violations. The two four-leaf shapes the file
names came out as stated: $\ell = S = 9$ for the comb and $\ell = 6$, $S = 8$ for the balanced
tree, against $2(n-1) = 6$. My re-derivation of the deterministic step agreed with the record.
I did not re-derive the dyadic tail bound or the occupation-measure convergence beyond reading
them; those are the load-bearing steps of the stronger conclusion (3), and the refutation of
the proposed scale rests only on (1) and (2).

*Verification state as recorded.* `result_status: candidate_full_solution` in both records
(the later revised at 7 September 02:28Z), `verification: author_checked_candidate`,
`independent_review: none`, `novelty: not_claimed`. The attempt's `independent_check` field
records exact checks passed for 6,918 ordered binary trees and 23 rational height and
occupation systems, with five deliberately false identities rejected as controls, and it also
records that an initial float-contaminated checker failed -- the failure is retained rather
than deleted. This is the second of the two problems in the campaign with a machine-checked
arithmetic core: step (1) and the telescoping identity are formalised in Lean at
`Prob1000/P0340.lean`, four theorems, no `sorry` and no `native_decide`. A Lean core for a
tree induction is not a formalisation of the refutation, which also needs the source's
Theorem 3.

*The reading trap, recorded because it nearly reversed the result.* The PDF text extractor
renders $\log^2$ as "log2", so Theorem 3 reads "$3\pi^{-2}\log2\,n$" and looks like a base-2
logarithm. It is $\log$ squared, as the source's own heuristic on page 13 derives explicitly.
Read as base two the mean leaf depth becomes linear in $\log n$ and the refutation evaporates;
the 8 September audit caught it by simulating the leaf depth and finding $\log^2$ growth. That
audit also sampled $\mathrm{DTCS}(n)$ from $n = 10^3$ to $4\times10^5$ and found $E\ell/n$
reading $4.71, 4.78, 4.84, 4.83, 4.86$ -- flat over a four-hundred-fold range of $n$ while
$\log^4n$ grows twelvefold -- having first validated the sampler against the paper's own
formulas (clade counts matching $(n/m)a(m)$ to four figures, $0.3059$ against
$3/\pi^2 = 0.3040$ at $m = 2$).

*Prior art as recorded.* `novelty: not_claimed`. A bounded search on 7 September found no
correction. The one paper that could have pre-empted it was checked and cleared on 8 September:
Brandenberger, Chin and Mossel, arXiv:2505.24821, advertises that it answers several
Aldous-Janson-Pittel questions without naming them, and extracting its text locally shows it
answers Open Problems 5 and 6 and partially answers Open Problem 8, with the string "drawn" not
occurring anywhere in it. That paper does state, on PDF page 3, a weighted-convergence result
for all polynomially decreasing test functions which together with $H_m = O((\log m)^2)$ gives a
second literature-supported route to (3); the self-contained dyadic argument avoids assuming it.
The 8 September audit judges this the best novelty case of the results it checked, and the 10
September comparison calls P0340 and the partial P0341 "clear, useful corrections" whose
source-version and prior-art review remain necessary.

*Scope and what is open.* The result is an expectation asymptotic. There is no law of large
numbers for $\ell(T_n)/n$, no variance formula, no central limit theorem, and no closed form
for $c_\ell$ -- only the convergent series and the bound $c_\ell \ge 2$. The pointwise
occupation formula is established literature; the dyadic uniform-tail argument is
author-checked and unreviewed.

### P0289. Faster modulation can raise the mean workload

The mathematics of this one belongs to chapter 10, which re-derives it in full from a second
lane's work; this section records what it is and where it stands.

*The problem as posed.* Lasse Leskela, *Ross's second conjecture and supermodular stochastic
ordering*, Queueing Systems 100 (2022) 213-215, Problem 1, journal page 214. A single-server
queue with Cox arrivals of intensity $\lambda_c(t) = \lambda(ct)$, with $\lambda$ stationary
and ergodic, i.i.d. service, stable; $w(c)$ the mean stationary workload. Is $w$
nonincreasing in $c$, and if not, what simple condition on $\lambda$ makes it so? The ledger
groups the two clauses as one question and records that a counterexample to the first does not
finish the characterisation request.

*What was found.* The universal monotonicity clause is false. With intensity
$\varepsilon F(ct)$, $F(t) = 2+\cos\left(\theta X_t+\theta/4\right)$ where $X$ is the
clockwise-only continuous-time Markov chain on $\mathbb Z/1024$ at rate $1/\sin\theta$ with
$\theta = 2\pi/1024$, deterministic unit service and $\varepsilon = 10^{-4}$, one has
$w(3\pi)>w(2\pi)$. The mechanism is that a one-directional cyclic walk has complex character
eigenvalues, so the autocorrelation oscillates, $E[F(0)F(t)] = 4+\tfrac12e^{-\delta|t|}\cos t$
with $\delta = \tan(\pi/1024)$, and the second-order term in the traffic parameter picks up
the oscillation. A reversible environment has a completely monotone autocovariance and cannot
do this.

Chapter 10 re-derives from scratch the uniform second-order expansion the whole counterexample
rests on,

$$w(c) = \frac{\varepsilon a}{2}+\varepsilon^2\int_0^1(1-u)E\left[F(0)F(-cu)\right]du+R_c, \qquad 0 \le R_c \le \frac{\varepsilon^3M^3}{2(1-\varepsilon M)},$$

by a workload balance for $EV^2$, a shot-noise lower bound $V \ge S$, and the monotonicity of
$V-S$ under adding arrivals, with the remainder dominated by the un-thinned M/D/1 queue; it
confirms the expansion and finds the packet's rational bounds valid and in fact conservative
(true half-difference $0.01077$ against the claimed $137/46080 = 0.00297$). It also adds a
result the packet does not have: substituting $v = cu$ turns the second-order term into
$\tfrac12\mathrm{Var}\left(c^{-1}\int_0^cF\right)$, so to second order faster modulation lowers
the mean workload exactly when it lowers the variance of the environment's average over one
service time, and the low-traffic form of the monotonicity holds if and only if
$\int_0^c(2v-c)R(v)\,dv \le 0$ for every $c$. A nonincreasing autocovariance satisfies that,
and every reversible stationary Markov environment has
$R(v) = \sum_ka_k^2e^{-\lambda_kv}$, so a reversible environment can never produce a
second-order counterexample -- which explains why the counterexample had to be
non-reversible.

*Verification state as recorded.* `result_status: candidate_partial_counterexample`,
`verification: author_checked`, `independent_review: none`. This is the one file the 8
September audit left half-checked: it verified the mechanism and recorded the quantitative half
as unchecked, treating P0289 as "a promising candidate with a sound mechanism, not as settled".
The 12 September lane closed that half and reports the counterexample as author-checked by a
second reader, with the second-order criterion labelled author-checked, not independently
refereed, and no novelty claimed. No Lean development.

*Prior art and scope as recorded.* Initial targeted searches found the original author note and
older Ross-type literature including Miyoshi-Rolski 2004 and Heyman's older counterexample for
a nonstationary-arrival formulation; a full comparison was not made, and the light-traffic
literature on Cox queues -- where the variance criterion looks as though it should already sit
-- was not searched. The construction does not refute the doubly stochastically monotone case,
does not settle the source's Problem 2, and says nothing about three-state environments, since
it uses 1,024 distinct intensity values. The criterion is for the second-order term only: when
$\mathrm{Var}\left(c^{-1}\int_0^cF\right)$ is nonincreasing the third-order remainder is
bounded but not signed, so nothing follows about the exact statement. The requested
necessary-and-sufficient condition at fixed traffic remains open, and chapter 10 records that
the third-order term has no sign structure in $c$ that its author could see.

### P0001. Negative correlation in uniform forests, for cactus graphs only

*As posed.* Grimmett, *Selected problems in probability theory*, arXiv:2205.07318, Conjecture 4.2,
PDF page 8: for a finite simple graph, uniformly choose an acyclic edge subset; are distinct edge
indicators always negatively correlated? Tang and Zhang, arXiv:2603.10738v1 (March 2026), restate it
as their Conjecture 1.3, and their complete-graph results do not settle arbitrary graphs.
`result_status: partial_result`, `verification: author_checked_special_case_only`; the file's header
says the target remains unsolved.

*What was found.* Negative association -- stronger than pairwise negative correlation -- for cactus
graphs, where every edge lies in at most one simple cycle, with arbitrary positive edge weights; and
a refutation of a natural route to the general case.

*How.* Start from independent Bernoulli indicators with $p_e = w_e/(1+w_e)$; conditioning on
acyclicity gives exactly the weighted forest measure, since the product probability of an edge set is
a constant times its product weight. In a cactus the cycles occupy disjoint coordinate blocks, so
acyclicity is an intersection of events on disjoint blocks and conditioning preserves independence
between them. Inside one block, with $H$ the all-ones event of that cycle and $q = P(H) = \prod p_e$,
for disjoint increasing $f,g$ with $a = Ef$, $b = Eg$, $f_* = f(\mathbf1)$, $g_* = g(\mathbf1)$,
independence gives $E(fg) = ab$ and hence

$$\mathrm{Cov}\!\left(f,g\mid H^c\right) = \frac{ab-qf_*g_*}{1-q}-\frac{\left(a-qf_*\right)\left(b-qg_*\right)}{(1-q)^2} = -\frac{q\left(f_*-a\right)\left(g_*-b\right)}{(1-q)^2} \le 0,$$

the sign from monotonicity, $f_* \ge a$ and $g_* \ge b$. Negative association survives independent
products, so an induction over blocks and bridges finishes it. For two edges of one cycle the
covariance is $-q(1-p_e)(1-p_f)/(1-q)^2$, which on a uniform $m$-cycle is
$-2^{m-2}/\left(2^m-1\right)^2$.

The refuted route is the appealing principle that conditioning independent bits on a decreasing event
preserves negative association. Take three fair bits conditioned on neither $X_1X_2$ nor $X_2X_3$
being one: the allowed states are $000,100,010,001,101$, so $EX_1 = EX_3 = 2/5$ and
$E(X_1X_3) = 1/5$, giving $\mathrm{Cov}(X_1,X_3) = +1/25$. The event is decreasing and it creates
positive correlation. That kills the route, not the conjecture: the forbidden pairs are not the
circuits of a graphic matroid, and circuit elimination would need a third circuit that is absent.

*My re-derivation.* Enumerating the forests of the $m$-cycle for $m = 3,\ldots,7$ gives adjacent-edge
covariances $-2/49$, $-4/225$, $-8/961$, $-16/3969$, $-32/16129$, matching the formula exactly, and
the direct count $\left(2^{m-2}-1\right)\left(2^m-1\right)-\left(2^{m-1}-1\right)^2 = -2^{m-2}$ is an
identity; the three-bit example gives $1/25$ exactly. Agreed with the record.

*Prior art and what is open.* No novelty claimed. The general conjecture is open, and the file states
the exact obligation: an inequality controlling overlapping cycle constraints through graphic-matroid
structure, which arbitrary decreasing-event conditioning cannot supply.

### P0004. Root-independence of the quenched connective limsup

*As posed.* Same source, Question 2.3, PDF pages 3 to 4: on the infinite supercritical
bond-percolation cluster of $\mathbb Z^2$, does $c_n(v)^{1/n}$ converge almost surely, independently
of $v$? `result_status: partial_result`, `verification: author_checked_special_case_only`; the file
says the existence question is unsolved and its own conclusion already published.

*What was found.* On any infinite connected graph of maximum degree $\Delta<\infty$,
$M(v) = \limsup_nc_n(v)^{1/n}$ is independent of the root; and in the percolation setting
$\limsup\left(c_n^\omega\right)^{1/n} \le p\mu$ almost surely.

*How.* For adjacent $v,w$, partition the self-avoiding walks from $v$ by whether they visit $w$. One
avoiding $w$ becomes an $(n+1)$-step walk from $w$ by prepending the edge $wv$; one visiting $w$ does
so at a unique time $k$, and reversing the prefix while keeping the suffix gives a $k$-step and an
$(n-k)$-step walk from $w$, with disjointness forgotten only enlarging the count. So
$c_n(v) \le c_{n+1}(w)+\sum_{k=1}^nc_k(w)c_{n-k}(w)$. Local finiteness gives a ray from every vertex,
so $1 \le M(w) \le \Delta$, and with $c_m(w) \le C\left(M(w)+\varepsilon\right)^m$ the bound becomes
$\left[C\left(M(w)+\varepsilon\right)+nC^2\right]\left(M(w)+\varepsilon\right)^n$; $n$-th roots kill
the polynomial factor, so $M(v) \le M(w)$, and symmetry plus a connecting path finishes it.
Translation ergodicity and uniqueness of the infinite cluster make the common limsup deterministic.
For the annealed bound, every lattice walk uses $n$ distinct edges, so
$Ec_n^\omega = p^nc_n^{\mathrm{lattice}}$, and Markov plus Borel-Cantelli over a countable sequence of
$\varepsilon$ gives the claim.

*My re-derivation.* Both steps are injective counting and I checked them on paper; nothing is hidden.
Agreed with the record.

*Prior art and what is open.* The file names its own antecedent: the conclusion is in Lacoin,
arXiv:1203.6051, which also proves a strictly smaller bound than $p\mu$ in the planar supercritical
regime. Existence of the limit is untouched, and the file says why the obvious route fails: cutting at
time $m$ gives only $c_{m+n}^\omega(v) \le c_m^\omega(v)\max_uc_n^\omega(u)$ over reachable endpoints,
and that maximum is neither $c_n^\omega(v)$ nor a predetermined stationary translate, so Fekete does
not apply and no stationary subadditive process has been constructed.

### P0341. Aldous-Janson's Ansatz 20 fails in both parts

*As posed.* Aldous and Janson, arXiv:2303.02529v3, Open Problem 8 with the displayed Ansatz 20, PDF
pages 28 to 30 and 39 to 40. Open Problem 8 asks for explicit bounds on
$\left|a(n,m)-a(m)\right|$, then says "In particular, prove the following Ansatz." Ansatz 20: for
nonnegative $f$ with $f(j) = O(j^k)$, (i) if $\sum_ia(i)f(i)<\infty$ then
$\sum_{i=2}^na(n,i)f(i) \to \sum_ia(i)f(i)$; (ii) if the limiting series diverges then the finite sum
is asymptotic to $\sum_{i=2}^na(i)f(i)$. Here $a(n,j)$ is the probability that the tagged harmonic
descent chain from $n$ visits $j$ and $a(j) = 6H_{j-1}/\left[\pi^2(j-1)\right]$ its fixed-$j$ limit.
`result_status: candidate_partial_counterexample`.

*What was found.* Both parts are false, by one mechanism: $a(n,n) = 1$ exactly. The chain starts at
$n$, so it visits $n$ surely, and a test function charging $j = n$ along a subsequence sees a
contribution to which every fixed-$j$ limit is blind.

*How.* For (i) take $f(j) = \mathbf1\{j = 2^r,\ r \ge 1\}$, bounded and so of polynomial growth; since
$a(2^r) = O\!\left(r2^{-r}\right)$ the series $S = \sum_{r\ge1}a(2^r)$ converges. At $n = 2^K$,
nonnegativity and the certain root visit give
$\sum_ja(2^K,j)f(j) \ge 1+\sum_{r\le M}a(2^K,2^r)$ for every fixed $M<K$, so letting
$K \to \infty$ then $M \to \infty$ gives $\liminf \ge 1+S$ against the predicted $S$. For (ii) take
$g(j) = j\mathbf1\{j = 2^r\}$, so $g(j) \le j$; since $a(j)j \sim (6/\pi^2)\log j$ the term
$a(2^r)2^r$ is of order $r$ and the truncated limiting sum at $n = 2^K$ is of order $K^2$, while the
actual sum is at least its root contribution $a(2^K,2^K)2^K = 2^K$, and $2^K/K^2$ diverges.

*My re-derivation.* $S = 1.522117$, so the prediction is $1.522$ and the liminf at least $2.522$ --
wrong by a whole unit. For (ii) the truncated limiting sum reads $9.18$, $27.88$, $96.71$, $207.67$,
$360.77$ at $K = 5,10,20,30,40$, growing like $K^2$, against root terms $32$ up to
$1.1\times10^{12}$, so the ratio climbs from $3.5$ to $3.0\times10^9$. Agreed with the record; neither
part needs a rate of convergence.

*Why it matters beyond the Ansatz.* The authors invoke Ansatz 20 to pass from the fixed-$j$ limits to
balance-index asymptotics -- their text says "At this point we need to invoke Ansatz 20." That is not
a claim that those results are wrong, since the indices they treat use regular, non-sparse weights,
exactly the class the counterexample avoids; but the Ansatz cannot be used as stated, and any
application needs a hypothesis ruling out sparse root-charging test functions. The 8 September audit
records this as the one result in the directory it would put first for a specialist's attention.

*Prior art and what is open.* No priority claimed; Brandenberger, Chin and Mossel, arXiv:2505.24821,
supply fixed-state and growing-state error bounds and a decaying-test special case, credited in the
ledger. Open Problem 8 itself is not settled: useful two-parameter bounds remain open and the right
regularity class for a true version is undetermined.

### P0342. A bounded continuous functional that blocks an unrestricted fringe transfer

*As posed.* Same source, Open Problem 12, PDF pages 44 to 45: does a central limit theorem for a
functional along the stationary infinite fringe process necessarily give the same theorem for its sum
over the leaves of $\mathrm{DTCS}(n)$? The numbered question imposes no locality condition.
`result_status: candidate_partial_counterexample`, with the ledger's honest caveat: "The explicit
example below has a degenerate Gaussian limit; a strictly positive variance or fixed-neighborhood
interpretation is retained as an unresolved scope restriction."

*What was found.* Under bounded continuity and first-order convergence alone, no: one bounded,
locally continuous, deterministic functional has identically zero fringe sums and non-tight
finite-tree normalised sums.

*How.* For a finite full binary tree with $n \ge 2$ leaves the original root is the unique vertex of
degree two, so the original root split survives rerooting at a leaf. With $R_n$ the smaller original
root-clade size, $r_n = \lfloor\sqrt n\rfloor$, $B_n = \mathbf1\{R_n \le r_n\}$ and
$p_n = \mathbb P(B_n = 1)$, set $\Phi(T) = n^{-1/4}\left(B_n(T)-p_n\right)$ for $n \ge 9$ and
$\Phi = 0$ on infinite trees and smaller ones. This is one deterministic bounded function, since $n$
is a measurable statistic of the input. It is continuous in the local topology: a finite tree is
isolated once a large enough rooted ball with boundary degrees is specified, and finite trees
converging locally to an infinite tree must have $n \to \infty$ (a full binary tree with $n$ leaves
has $2n-1$ vertices), so $|\Phi| \le n^{-1/4} \to 0$ along any such sequence -- the prefactor, not the
indicator, is what makes the product continuous.

The stationary fringe tree and all its leaf rerootings are infinite, so every centred normalised
fringe sum is exactly zero. For the finite tree, rerooting changes neither $n$ nor the degree-two
vertex, so every leaf carries the same value and

$$\frac1{\sqrt n}\sum_{i=1}^n\Phi\!\left(T_i^{(n)}\right) = n^{1/4}\left(B_n-p_n\right),$$

with both centrings agreeing since each summand already has mean zero. The exact split law gives
$p_n = H_{n-1}^{-1}\left(H_{r_n}+\sum_{i=1}^{r_n}(n-i)^{-1}\right) \to 1/2$, because
$H_{r_n}/H_{n-1} \to 1/2$ and the second sum is at most $r_n/(n-r_n) = O(n^{-1/2})$. Eventually both
$p_n$ and $1-p_n$ exceed one third, so the displayed quantity exceeds $n^{1/4}/3$ in absolute value
with probability one: not tight. The unnormalised averages are at most $n^{-1/4}$ and vanish
deterministically, so first-order fringe convergence is untouched.

*My re-derivation.* $p_n$ exactly at $n = 9,16,100,400,2500,10000,250000$ reads $0.8344$, $0.7178$,
$0.5862$, $0.5556$, $0.5380$, $0.5310$, $0.5224$, with $H_{r_n}/H_{n-1}$ tracking from below and the
second term bounded by $r_n/(n-r_n)$ falling from $0.5$ to $0.002$. The convergence to $1/2$ is slow,
being a ratio of harmonic numbers, but the argument needs only that both $p_n$ and $1-p_n$ eventually
exceed one third, which happens by $n = 100$. Agreed with the record.

*Scope and what is open.* If a nondegenerate limiting variance is required this is not by itself a
counterexample, and the file says so. What survives is a structural implication: if an admissible
class contains some $\Psi$ with a nondegenerate fringe CLT and is closed under adding $\Phi$, then no
universal transfer theorem holds across it, since the fringe sums agree while the difference of the
finite-tree normalised sums is the non-tight quantity above. The useful open question is a transfer
theorem with quantitative locality, stabilisation, mixing, or a finite-to-infinite approximation error
negligible at square-root scale.

### P0355. A degenerate case the discounted-tree nonendogeny conjecture omits

*As posed.* Aldous and Bandyopadhyay, *A survey of max-type recursive distributional equations*,
Annals of Applied Probability 15 (2005) 1047-1110, Conjecture 34 with Corollary 33, journal page
1075, PDF page 29. The equation is $X \stackrel{d}{=} \eta+\max_i\xi_iX_i$ on $\mathbb R_+$;
Corollary 33 assumes the supremum of discounted ray sums is finite and that the homogeneous equation
has a nonzero solution $Y$, and its condition (39) adds independence of $\eta$ from the weights with
$0$ in the support of $\eta$. Conjecture 34 says the invariant recursive tree process with marginal
$\mu_a$, obtained by iterating from the law of $aY$, is nonendogenous for every $a>0$.
`result_status: candidate_partial_counterexample`, with the caveat that the counterexample is
restricted to the literal zero-mark and unit-weight boundary and that the intended strictly
discounted nondegenerate regime remains unsolved.

*What was found.* The literal hypotheses admit an endogenous case. Its value is in locating the two
boundary choices the conjecture needs to exclude.

*How.* On the deterministic binary tree take $N = 2$, $\eta = 0$, $\xi_1 = \xi_2 = 1$, $Y = 1$. Every
discounted ray sum is zero, so its supremum is the finite variable $X = 0$; the homogeneous equation
holds because $\max(1,1) = 1$; $\eta$ is independent of the deterministic weight vector with support
$\{0\}$, so (39) holds. For every $a \ge 0$ the operator fixes $\delta_a$, since
$T(\delta_a) = \delta_{\max(a,a)} = \delta_a$, so $\mu_a = \delta_a$, and these are distinct as $a$
varies. Setting every vertex variable equal to $a$ gives an invariant recursive tree process whose
root is a constant, hence measurable with respect to the innovations: endogenous. Equivalently, given
all innovations the conditional root law is $\delta_a$, so two conditionally independent copies agree
almost surely.

The two controls make the entry useful rather than a quibble. Positive constant marks make every ray
sum infinite, violating the finite-supremum hypothesis; deterministic weights $c<1$ make the constant
positive $Y$ fail the homogeneous equation, since $\max(cY,cY) = cY \ne Y$. And Corollary 33 does not
repeat the strict inequalities $\xi_i<1$ of the sufficient Theorem 32 -- its parenthetical says those
are one sufficient way to get a finite supremum, not that they are mandatory. That is the gap the
example occupies.

*My re-derivation.* The argument is finite and I checked it by reading: $T(\delta_a) = \delta_a$ is
immediate, each control is one line, and both endogeny formulations agree. Agreed with the record.

*Prior art and what is open.* A bounded search found no published correction, and the file says that
is not evidence of novelty; later work on bounded discounted tree sums usually assumes positive marks
explicitly, so this contradicts none of it. The substantive conjecture -- strict discounts, nonzero
marks, suitable nondegeneracy -- is untouched.

### P0389 and P0390. Fixed mass forces a window restriction in the ARW hyperuniformity questions

*As posed.* Levine and Silvestri, *Universality Conjectures for Activated Random Walk*,
arXiv:2306.01698v2, Conjecture 27 and Question 28, PDF pages 15 to 16, recorded as P0389 and P0390.
They ask for subcritical linear window variance and a critical or supercritical sub-volume saving,
for the free-chain torus configuration and for the stationary wake chain respectively. Both are
`candidate_partial_counterexample`, and the ledger's caveat is the content: "The literal source
permits every box with size-uniform constants. That lower bound fails for boxes filling almost the
whole torus. The intended mesoscopic or bounded-volume-fraction regime remains open."

*What was found.* A quantifier correction, not a resolution: under any law with a fixed total
particle count the claimed uniform linear lower bound cannot hold for every window.

*How.* Let $T$ have $N$ sites with occupation indicators summing to exactly $k$ almost surely. For
every $B$, $S_B = k-S_{T\setminus B}$, so
$\mathrm{Var}(S_B) = \mathrm{Var}\left(S_{T\setminus B}\right)$, and a variable confined to an
interval of length $a$ has variance at most $a^2/4$, giving
$\mathrm{Var}(S_B) \le \tfrac14\min\left\{|B|,N-|B|\right\}^2$. Only fixed mass is used, which holds
after every free-chain addition and throughout each fixed-particle-number wake chain. On the cycle
with $L$ vertices and $k = \lfloor\rho L\rfloor$, taking $B$ to be $L-1$ vertices gives
$S_B = k-I_x$, so the variance is exactly $\rho_L(1-\rho_L) \le 1/4$ and cannot be at least $c(L-1)$.
Uniform free driving is translation equivariant and the wake kernel commutes with translations, so
the single-site mean is $k/L$ in both ensembles. A proper subset is therefore not enough to repair
the statement; the whole torus is only the easiest exception.

The file then blocks the reading that this is about hyperuniformity. Under any fixed-mass law
$\sum_y\mathrm{Cov}(I_x,I_y) = \mathrm{Cov}(I_x,k) = 0$, and yet for a uniformly chosen $k$-subset,
offered only as a comparison model,
$\mathrm{Var}(S_B) = b\rho_N(1-\rho_N)(N-b)/(N-1)$ with $b = |B|$, which for $b \to \infty$ and
$b/N \to 0$ is asymptotically $b\rho(1-\rho)$: volume-order mesoscopic fluctuations coexisting with
exact finite-volume covariance cancellation. Passing the finite-torus zero sum to infinite volume
needs uniform tail control.

*My re-derivation.* The complement identity and the variance bound are one line each. The comparison
variance I checked by exhaustive enumeration of $k$-subsets at $(N,k,b) = (8,3,3)$, $(10,4,5)$,
$(12,5,7)$ and $(12,5,11)$: exact variances $0.5022321429$, $0.6666666667$, $0.7733585859$,
$0.2430555556$, each equal to the formula to ten places, the last showing the fall as $b$ approaches
$N$. Agreed with the record.

*Scope and what is open.* Nothing here shows that either ARW law is a uniform-subset law, negatively
associated, or hyperuniform, and the file says so. The natural next version restricts windows away
from full volume or takes the thermodynamic limit first, and the file does not assert that the source
prescribed either. Proving the transition and its exponent in such a regime is untouched.

### P0411. Hole monotonicity, the odd-dimensional polynomial, and a negative coefficient in the plane

*As posed.* D'Achille, Curien, Enriquez, Lyons and Unel, *Ideal Poisson-Voronoi tessellations on
hyperbolic spaces*, archived as `ideal_voronoi_2023`, Conjecture 7.5, PDF page 48, with Proposition
5.1 and equation (5.1) on PDF page 35: prove normalised hole monotonicity, a positive rational
polynomial form in odd dimension, a positive power-series form in even dimension, and a related
decreasing-density property. `result_status: candidate_partial_counterexample` in all three records;
the operative third record (7 September 07:11Z) carries `candidate_scope`: "All-dimensional
monotonicity, odd-dimensional polynomial and density/median proof, plus a $d=2$ counterexample to
positive Maclaurin coefficients; other even-dimensional density/median questions remain."

*What was found.* With $n = d-1$, $H_d(u)$ the probability that the ball of radius $u$ about the
origin lies inside its ideal cell, and $J_d = 1/H_d$: the map $u \mapsto e^{(d-1)u}H_d(u)$ is
strictly decreasing in every dimension; for $d = 2m+1$ one has
$H_d(u) = e^{-2mu}/p_m\!\left(e^{2u}\right)$ with $p_m$ of degree $m$ and strictly positive rational
coefficients, whence a decreasing density and a median below the mean; and in dimension two the sixth
Maclaurin coefficient of the conjectured $f$ is negative.

*How.* Monotonicity avoids differentiating under the integral. From
$J_d(u) = c_d^{-1}\int_{\mathbb R^n}\left(\sqrt{\cosh^2u+|x|^2}-\sinh u\right)^{-2n}dx$, put
$q = e^{2u}$ and $x = e^{-u}z$:

$$e^{-nu}J_d(u) = \frac1{c_d}\int_{\mathbb R^n}D_q(z)^{-2n}dz, \qquad D_q(z) = \sqrt{(q+1)^2/4+|z|^2}-\frac{q-1}2,$$

and $\partial D_q/\partial q = (q+1)\big/\!\left(4\sqrt{(q+1)^2/4+|z|^2}\right)-\tfrac12<0$ for
$z \ne 0$, so the integrand strictly increases in $q$ and a pointwise comparison of two values of $q$
suffices.

For odd $d$, with $a = e^{-u}$, $s = \sinh u$, the radial substitution
$y = \sqrt{\cosh^2u+r^2}-s$ has lower endpoint $a$ and gives $r^2 = (y-a)\left(y+a^{-1}\right)$,
$r\,dr = (y+s)\,dy$; setting $y = az$,

$$J_{2m+1}(u) = C_ma^{-4m}\int_1^\infty(z-1)^{m-1}\left(a^2z+1\right)^{m-1}\left[a^2(2z-1)+1\right]z^{-4m}dz, \qquad C_m = \frac{\Gamma(2m)}{\Gamma(m)^2}.$$

Expanding in $a^2$ leaves only strictly positive integrable coefficient functions on $z>1$ -- the one
apparent subtraction, $2z-1$, is positive there -- and
$\int_1^\infty(z-1)^{m-1}z^{j-4m}dz = B(3m-j,m)$ with positive integer arguments, so the coefficients
$b_{m,j} = \binom{m-1}{j}B(3m-j,m)+\binom{m-1}{j-1}\left[2B(3m-j,m)-B(3m-j+1,m)\right]$ are positive
because $B(A+1,m)<B(A,m)$. Normalisation gives $p_m(1) = 1$, with $p_1(q) = (q+2)/3$ -- the known
dimension-three formula, used as a control -- and $p_2(q) = q^2/7+16q/35+2/5$. The polynomial form
makes $J_d$ a positive combination of exponentials with rates in $[n,2n]$, so with $L = \log J_d$ the
quantity $L'$ is a mean rate and $L''$ a variance, giving $L' \ge n$, $L'' \le n^2/4$, hence
$f' = H_d\left(L''-(L')^2\right)<0$ for the density and, by convexity of the survival function, a
median below the mean.

The even-dimensional clause fails. The source's Remark 5.2 gives, credited to earlier work,
$H_2(u) = \pi/\left(4\arctan(e^u)\cosh^2u+2\sinh u\right)$, and the conjecture requires
$H_2(u) = e^{-u}/f(u)$ with $f$ having positive Maclaurin coefficients, so

$$f(u) = \frac{\left(e^u+2e^{-u}+e^{-3u}\right)A(u)+1-e^{-2u}}{\pi}, \qquad A(u) = \arctan(e^u) = \frac\pi4+\frac u2-\frac{u^3}{12}+\frac{u^5}{48}+O(u^7),$$

using $A'(u) = 1/(2\cosh u)$. With $E(u) = e^u+2e^{-u}+e^{-3u}$, whose relevant coefficients are
$[u^6] = 61/60$, $[u^5] = -61/30$, $[u^3] = -14/3$, $[u^1] = -4$,

$$[u^6]f = \frac{61}{240}+\frac1\pi\left(-\frac{61}{60}+\frac7{18}-\frac1{12}-\frac4{45}\right) = \frac{61\pi-192}{240\pi} < 0,$$

exactly, since $\pi<22/7$ gives $61\pi-192<-2/7$. Maclaurin coefficients of a function analytic at
zero are unique, so no positive-coefficient series in the same variable represents this $f$.

*My re-derivation.* Computing the series of $f$ to order seven in forty-digit arithmetic gives
$[u^6]f = -0.0004812422803658705635\ldots$, agreeing with $(61\pi-192)/(240\pi)$ to forty-three
digits and with the file's recorded value. I also verified $f = e^{-u}/H_2(u)$ at three values of $u$
to forty digits, the four coefficients of $E$, the Taylor coefficients of $A$ ($\pi/4$, $1/2$, $0$,
$-1/12$, $0$, $1/48$), the rational bound $61\pi-192 = -0.36285<-2/7$, and $p_1(1) = p_2(1) = 1$.
Agreed with the record.

*Scope and what is open.* The pieces should be kept apart: the dimension-three formula and the
odd-dimensional rationality observation are the source's; monotonicity in every dimension and the
positive odd-dimensional coefficients are the contribution; the negative coefficient refutes the
literal even-dimensional Maclaurin clause in the source's displayed distance variable and nothing
more. The file names the strongest alternative explanation itself -- that the authors may have
intended a series in another variable or normalisation, in which case a clarification would change the
disposition -- and other even-dimensional density and median claims remain unproved. No independent
referee has read the packet.

### P0429. Limited fork-join under exponential service

*As posed.* Recorded from a 2021 survey, Section 5, PDF page 16: how quickly can the number $k(n)$ of
tasks per uniformly routed job grow while the corresponding $k(n)$ stationary queues remain
asymptotically independent? The source credits $k = o\!\left(n^{1/4}\right)$. `result_status:
candidate_partial_counterexample` in the later record (7 September 07:11Z), which replaced `unsolved`
twenty minutes earlier, with `candidate_scope`: "Stationary collision/emptying bound;
exponential-service sufficient regime $k = o\!\left((n/\log n)^{1/3}\right)$; general service and
optimal threshold unresolved." The file credits the coupling method and its $k = o(n^{1/4})$ theorem
to Wang et al., *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, Sections 3 to 5, and
describes itself as sharpening the marginal emptying-time step.

*What was found.* A modular bound, and under exponential service a sufficient regime
$k = o\!\left((n/\log n)^{1/3}\right)$. With $r(T)$ the probability that a stationary marginal M/G/1
workload has not hit zero by time $T$,

$$d_{\mathrm{TV}}\left(\pi_{n,k},\nu_k\right) \le 2k\,r(T)+\frac{3\lambda Tk(k-1)^2}{2(n-1)} \quad\text{for every } T>0,$$

and for exponential service of rate $\mu$, with $\rho = \lambda/\mu$ and
$c = \left(\sqrt\mu-\sqrt\lambda\right)^2$, one has $r(T) \le (1+\sqrt\rho)e^{-cT}$.

*How.* Three steps. First the arrivals are decoupled with the marginal rates restored exactly rather
than lowered: for a tagged set of size $k$ one job selects $N$ tagged servers with
$E\left[N(N-1)\right] = k^2(k-1)^2/\left[n(n-1)\right]$; Poisson marking splits the stream by tagged
subset, singleton arrivals are kept, multi-hit arrivals discarded, and independent Poisson arrivals
added back at the removed marginal rate, so the $k$ streams are independent Poisson of rate exactly
$\lambda$. Over $[0,T]$ the discrepancy probability is at most
$\Lambda T\left(\mathbb P(N \ge 2)+E\left[N\mathbf1_{N\ge2}\right]\right) \le \tfrac32\Lambda T\,E\left[N(N-1)\right]$,
using $1 \le N(N-1)/2$ and $N \le N(N-1)$ on $\{N \ge 2\}$, and $\Lambda = n\lambda/k$ gives the
collision term. Second, stationary starts are coupled to empty starts monotonically: the stationary
workload dominates coordinatewise and the two agree forever at a coordinate once it hits zero, so a
union bound over $k$ coordinates costs $kr(T)$ -- independence of the stationary coordinates is
neither assumed nor needed, since each is a marginal M/G/1 queue with the same $\lambda$. Third, the
emptying tail: for the M/M/1 count, $h(q) = a^q$ with $a = \sqrt{\mu/\lambda}>1$ has
$\mathcal Lh(q)/h(q) = \lambda(a-1)+\mu\left(a^{-1}-1\right) = -\left(\sqrt\mu-\sqrt\lambda\right)^2 = -c$
for $q \ge 1$, so stopping at zero and at a finite upper level, then removing the upper level by
Fatou, gives $\mathbb P_q(\tau_0>T) \le a^qe^{-cT}$, and averaging over the stationary geometric count
gives $E\left[a^{Q(0)}\right] = (1-\rho)/(1-\rho a) = 1+\sqrt\rho$. Taking $T = 2\log n/c$ gives
$d_{\mathrm{TV}} \le 2k(1+\sqrt\rho)n^{-2}+3\lambda k(k-1)^2\log n/\left[c(n-1)\right]$.

*My re-derivation.* Three exact checks. $E[N(N-1)]$ by exhaustive enumeration at
$(n,k) = (10,3)$, $(20,5)$, $(24,6)$: $0.4$, $1.0526315789$, $1.6304347826$, each equal to the formula
to ten places. The generator identity at $\rho = 0.1, 0.5, 0.9$ with $\mu = 1$ gives
$-0.467544$, $-0.085786$, $-0.002633$, exactly $-\left(1-\sqrt\rho\right)^2$. And
$(1-\rho)/(1-\rho a)$ gives $1.3162277660$, $1.7071067812$, $1.9486832981$, exactly $1+\sqrt\rho$.
Agreed with the record.

*Scope and what is open.* A sufficient regime, not a threshold, saying nothing at
$k \asymp n^{1/3}$; correlated within-job service marks excluded; the tail constant degenerates as the
load approaches one, so no uniform heavy-traffic claim. The general form -- if $r(T) \le CT^{-p}$ then
balancing gives $k = o\!\left(n^{p/(3p+1)}\right)$, recovering the credited $1/4$ at $p = 1$ -- is
recorded as conditional on the emptying-tail bound, with no unproved implication from a service
moment. Exponential control of the stationary emptying time for general service laws is not proved,
and the file allows that the observation may be a known corollary of the credited paper.

### P0458 and P0459. Bilateral preference degrees: a non-Gaussian limit and a concentration regime

*As posed.* Dabirian and Subramanian, *Connectivity of a Family of Bilateral Preference Random
Graphs*, arXiv:2209.05677v3, 8 July 2025, the two additional questions on PDF page 3, recorded as
P0458 ("Determine the limiting law of $(D-E[D])/\sqrt{\mathrm{Var}(D)}$ for a typical $LK(n,k)$
degree as the preference budget grows") and P0459 ("Find growth conditions and quantitative bounds
for $LK(n,k)$ degrees to concentrate simultaneously around their mean"). Both
`candidate_partial_counterexample`. In the model, every edge of the complete graph on $n$ vertices
carries an independent uniform weight and survives when it is among the $k$ smallest incident weights
at both endpoints.

*What was found.* For P0458 a candidate limit in the regime $k \to \infty$ with
$k = o\!\left(n^{2/5}\right)$, which contains the source's $k = o\!\left(n^{1/3}\right)$
mean-asymptotic regime: with $Z$ standard normal, $g(z) = \varphi(z)+z\Phi(z)$ and
$v = \tfrac13+\left(\sqrt3-2\right)/(2\pi)$,

$$\frac{k-D}{\sqrt k} \Longrightarrow g(Z), \qquad \frac{\mathrm{Var}(D)}{k} \to v, \qquad \frac{D-ED}{\sqrt{\mathrm{Var}(D)}} \Longrightarrow \frac{1/\sqrt\pi-g(Z)}{\sqrt v} .$$

The limit is not normal: $g$ is strictly increasing and positive with range $(0,\infty)$, so the
standardised limit has a finite upper endpoint, consistent with the ceiling $D \le k$. For P0459, a
sufficient regime $k/\log n \to \infty$ with $k-2\sqrt{6k\log n} \le D_v \le k$ at every vertex.

*How.* For P0458 the argument is a finite-$n$ comparison, not a local limit. The root's $(k+1)$-st
smallest incident weight $X$ is $\mathrm{Beta}(k+1,n-k-1)$, and given $X$ and the selected label set
$S$ the $k$ root-to-$S$ weights are independent uniforms on $(0,X)$. Ignoring edges internal to $S$
gives a comparison degree $D^0 \ge D$; any change of acceptance must touch an internal $S$-edge of
weight below $X$, of which there are $J \mid X \sim \mathrm{Bin}\!\left(\binom k2,X\right)$, so
$0 \le D^0-D \le 2J$ and $E\left(D^0-D\right)^2/k = O\!\left(k^2/n+k^5/n^2\right) = o(1)$ -- which is
where $k = o\!\left(n^{2/5}\right)$ enters, and it is an $L^2$ comparison rather than a probability
bound because the variance conclusion needs it. Given $X$ and $S$, the outside-edge arrays at
different selected neighbours are disjoint sets of independent variables, so
$D^0 \mid X \sim \mathrm{Bin}\!\left(k,1-q_n(X)\right)$ with
$q_n(X) = E\left[(X-T)_+\mid X\right]/X$ and $T$ the $k$-th order statistic of $n-k-1$ uniforms,
since a root edge of weight $u$ is accepted exactly when $u<T$. Scaling
$U_n = (nX-k)/\sqrt k$ and $V_n = (nT-k)/\sqrt k$, both are asymptotically standard normal with
bounded fourth moments, and one-Lipschitz positive parts give
$\sup_u\left|E(u-V_n)_+-g(u)\right| \to 0$ with $g(u) = E(u-Z)_+ = \varphi(u)+u\Phi(u)$; so the
conditional scaled deficit $C_n = (k/nX)\,g_n(U_n) \Rightarrow g(Z)$, with moments controlled by
splitting on $\{nX \ge k/2\}$ and a Chernoff bound $\mathbb P(nX<k/2) \le e^{-(\log2-1/2)k}$, and the
residual binomial noise vanishing because $E\left[q_n(1-q_n)\right] \le EC_n/\sqrt k \to 0$. The
constants come from two Gaussian computations: $Eg(Z) = E(Z-Z_1)_+ = 1/\sqrt\pi$, and
$Eg(Z)^2 = E\left[(Z-Z_1)_+(Z-Z_2)_+\right] = \tfrac13+\sqrt3/(2\pi)$, by writing the two differences
-- variance two, correlation one half -- in polar coordinates and integrating the product of cosines
over the positive overlap $(-\pi/6,\pi/2)$.

For P0459 the route is the source's own sandwich. With $\delta = \sqrt{6k\log n}$ and
$t = (k-\delta)/(n-1)$, threshold every weight at $t$: each vertex's threshold degree is
$\mathrm{Bin}(n-1,t)$ with mean $k-\delta$, and Chernoff gives
$\mathbb P(B_v>k) \le n^{-3}$ and $\mathbb P(B_v<k-2\delta) \le n^{-3}$, so a union bound -- needing no
independence between vertex degrees -- puts all threshold degrees in $[k-2\delta,k]$ with probability
at least $1-2/n^2$. On that event every threshold edge is among the $k$ preferred at both endpoints,
so the threshold graph is a subgraph of $LK(n,k)$.

*My re-derivation.* $v = \tfrac13+(\sqrt3-2)/(2\pi) = 0.29068789486043867$, matching the file's
recorded seventeen digits exactly; $1/\sqrt\pi = 0.5641895835$ and
$\tfrac13+\sqrt3/(2\pi) = 0.6089977810$; and a two-million-sample Monte Carlo of
$g(Z) = \varphi(Z)+Z\Phi(Z)$ gives mean $0.563643$, second moment $0.607964$ and variance $0.290270$,
agreeing with all three within Monte Carlo error. Agreed with the record. I did not re-derive the
beta-moment and $L^2$ comparison steps; the file's own list of fragile points is the root's
$(k+1)$-st order statistic, the outside beta parameter $n-2k$, the use of $L^2$ rather than
probability, and moment convergence before standardisation.

*Verification, prior art and what is open.* Both are private author-checked candidates with no
independent review and no novelty certification, and the file says the concentration estimate is
sufficient rather than optimal. The finite controls are an exhaustive rank enumeration of all $720$
edge orders on four vertices for $k = 1,2$, finding no violation of $D \le D^0 \le D+2J$, with degree
histograms $(288,432,0,0)$ and $(48,192,480,0)$ giving means $3/5$ and $8/5$ -- means that also follow
from direct two-endpoint ranking probabilities, which is what makes the control worth having. The 2025
connectivity theorem is credited. Bounded-degree regimes, growth beyond $k = o\!\left(n^{2/5}\right)$,
optimal tails and the critical logarithmic regime are unresolved, and below the connectivity threshold
isolated vertices already obstruct simultaneous concentration near $k$. A separate consistency lane
through the fixed-$k$ Erlang weighted tree gives the same $g(Z)$ limit, and the file is explicit that
a sequential local limit does not replace the triangular-array argument.

### P0096. The four-edge-minimum bound for the time constant, already refuted

*As posed.* Auffinger, Damron and Hanson, *50 years of first-passage percolation*,
arXiv:1511.03262, manuscript 26 September 2016, Question 12, PDF page 33 and repeated on page 146:
for i.i.d. nonnegative edge passage times on $\mathbb Z^2$ with $F(0) = 0$, is
$\mu(e_1) \ge E\min\left(\tau_1,\tau_2,\tau_3,\tau_4\right)$? The ledger records the notation trap
-- "$E_4$ is expectation of a minimum, not a fourth moment" -- and that the target is the survey's
universal formulation, not a theorem attributed to the Alm-Deijfen simulation paper that motivates it.

*Status.* `admitted: false`, `current_status: resolved_in_literature`, `result_status:
literature_counterexample_rederived`. The file's header, timestamped 19:18Z on 6 September, says
"ALREADY REFUTED IN THE LITERATURE" and declines novelty and solved-open credit -- four minutes after
the earlier `candidate_counterexample` record at 19:13Z. The resolving paper is Ahlberg, *Tertiles and
the time constant*, arXiv:1911.09949 (2019; v2 May 2020), Journal of Applied Probability 57(2)
407-408, DOI 10.1017/jpr.2020.9, whose Theorem 1 gives $\mu \le 2t_{2/3}$ and whose final paragraph
explicitly refutes both Alm-Deijfen and this survey question. The two-page paper was read in full.

*The retained argument.* Take $\eta_e \in \{0,1\}$ with $P(\eta_e = 0) = 3/4$, an independent uniform
$U_e$, and $\tau_e^{(\varepsilon)} = \eta_e+\varepsilon U_e$ for $0<\varepsilon \le 1$: the law is
bounded and absolutely continuous, density $3/(4\varepsilon)$ on $(0,\varepsilon)$ and
$1/(4\varepsilon)$ on $(1,1+\varepsilon)$, no atoms, $F_\varepsilon(0) = 0$, support infimum zero.
All four $\eta$ equal one with probability $(1/4)^4 = 1/256$, and on that event the minimum is at
least one, so $E\min_{i\le4}\tau_i^{(\varepsilon)} \ge 1/256$. On the other side the $\eta$-only model
has zero mass $3/4>p_c(\mathbb Z^2) = 1/2$, so $\mu_0 = 0$; coupling all $\varepsilon$ on the same
$(\eta,U)$ gives $T_\varepsilon \ge T_0$, and choosing for each $n$ and $\delta$ a finite path of
$\eta$-cost at most $T_0(0,ne_1)+\delta$ -- an approximate minimiser, not a geodesic -- gives
$T_\varepsilon(0,ne_1) \le T_0(0,ne_1)+\delta+\varepsilon|\gamma|$. Sending $\varepsilon$ then
$\delta$ to zero, with $0 \le T_\varepsilon \le 2n$ for dominated convergence, and using
$\mu(e_1) = \inf_nET(0,ne_1)/n$, gives $\mu_\varepsilon \to 0$. So every small enough $\varepsilon$
reverses the inequality. The file then takes an explicit parameter from Ahlberg's theorem rather than
from its own limit: the family's two-thirds quantile is $8\varepsilon/9$, so $\varepsilon = 1/1024$
gives $\mu \le 1/576<1/256$.

*My re-derivation.* $(1/4)^4 = 1/256$, and $3/4>1/2 = p_c$ forces $\mu_0 = 0$ by the positivity
criterion the file cites. Agreed with the record and with its own exclusion. The mechanism is worth
keeping: a local entrance cost stays positive even when long travel can exploit a supercritical
cheap-edge network, and dividing one entrance cost by distance is what makes the bound fail.

### P0140. The random critical drift in the thinned Levy exploration

*As posed.* van der Hofstad, *Stochastic processes on random graphs*, 12 July 2017, Open Problem 4.1
with equations 4.5.5 and 4.5.20, PDF pages 206 and 210. The ledger's statement is "Explain directly
how mixing the heavy-tailed degree weights yields the independent-increment iid-degree exploration
limit", with the caveat: "The deterministic drift in the short 2017 formulation must be replaced by
the random critical shift $\Lambda_0$. Dhara et al 2019 equation 2.22 and Remark 11 already identify
the corrected law indirectly."

*Status.* `admitted: false`, `current_status: resolved_in_literature`, `result_status:
literature_result_rederived_with_scope_correction`, single record. The file says so in its header and
keeps the candidate filename only as a record of the workflow.

*The retained argument.* With $3<\tau<4$ and $\theta_i = (c/\Gamma_i)^{1/(\tau-1)}$ from a rate-one
Poisson process, the $\theta_i$ form a Poisson process of intensity
$\rho(dx) = (\tau-1)cx^{-\tau}dx$; give each an independent exponential clock of rate $\theta_i/\mu$
and define
$Z = \lim_{\epsilon\downarrow0}\left[\sum_{\theta_i>\epsilon}\theta_i^2-\int_\epsilon^\infty x^2\rho\right]$,
$\Lambda_0 = Z/\mu$. The small-point part converges in $L^2$ and almost surely because
$\int_0^1x^4\rho<\infty$, and the large-point part is finite with finite first moment because
$\int_1^\infty x^2\rho<\infty$, though its second moment need not be; telescoping the integrals over
$[\Gamma_{i-1},\Gamma_i]$ identifies $Z/\mu$ with the later paper's equation 2.22 exactly, which is a
check against the source rather than an analogy. The positive content is one line of Poisson marking.
For every $\epsilon$ the cancellation

$$S_{0,\epsilon}(t)+\frac t\mu Z_\epsilon = \sum_{\theta_i>\epsilon}\theta_i\mathbf1\{T_i \le t\}-\frac t\mu\int_\epsilon^\infty x^2\rho(dx)$$

is an identity; the pairs $(\theta_i,T_i)$ form a Poisson random measure with deterministic intensity
$\nu(dx,ds) = \rho(dx)(x/\mu)e^{-xs/\mu}ds$; and disjoint time intervals select disjoint sets of that
measure, so the jump sum has independent increments -- generally nonstationary, because the intensity
carries $e^{-xs/\mu}$. The deterministic drift evaluates to
$D(t) = -(\tau-1)c\,\Gamma(4-\tau)\left[(\tau-2)(\tau-3)\right]^{-1}(t/\mu)^{\tau-2}<0$ by
substituting $u = xt/\mu$ and integrating by parts twice, consistent with depletion of previously
discovered vertices.

The other half is what makes the scope correction precise: a deterministic $\lambda$ does not give
independent increments. With $A = S_0(\mu)$, $B = S_0(2\mu)-S_0(\mu)$ and $K(a,b) = \log Ee^{aA+bB}$,
the compensated Poisson formula gives
$K(a,a)-K(a,0)-K(0,a) = \int\rho(dx)\,E_T\left[\left(e^{aF_1}-1\right)\left(e^{aF_2}-1\right)\right]$,
nonnegative for $x \ge 1$; on $x \in \left[a^{-1/2},2a^{-1/2}\right]$ with $0<a \le 1/4$ both
exponents are at most $-x^2/2$, so the integrand is at least $\left(1-e^{-1/2}\right)^2$ on a region
of $\rho$-mass $c\left(1-2^{1-\tau}\right)a^{(\tau-1)/2}$, while on $0<x<1$ the disjointness of the
indicators and $\left|e^{au}-1\right| \le a|u|e^{a|u|}$ bound the contribution by $Ca^2e^{4a}$. Since
$(\tau-1)/2<2$ on the stated range, the mixed difference is positive for small $a$, so $A$ and $B$ are
dependent and a deterministic $\lambda$ changes only their means. Covariances would not settle it,
because the random slope can have infinite variance.

*My re-derivation.* The two structural steps are Poisson marking and a Laplace-transform sign, and I
checked them by reading; the exponent comparison $(\tau-1)/2<2$ is the whole content of the second and
is immediate for $3<\tau<4$. Agreed with the record. The file declines original-solution credit and
notes that the novelty of the marking calculation itself is unsearched.

### P0248. The diameter-squared relaxation bound on Cayley graphs, resolved by Pak

*As posed.* Aldous and Fill, Open Problem 7.18 with Theorem 7.16, PDF page 253, chapter dated 31
January 1994: given a finite group with a symmetric generating set of Cayley diameter $D$, can a
symmetric step law supported on that set always have relaxation time at most a universal constant
times $D^2$? The caveat notes that the question is about optimising the step law, not the uniform
generating-set walk, and not the absolute eigenvalue gap.

*Status.* `admitted: false`, `result_status: excluded_prior_resolution`, revised at 23:37Z on 6
September from a `candidate_full_solution` record earlier the same evening. The resolving reference is
Igor Pak, *Using stopping times to bound mixing times*, SODA 1999, Theorem 3.1, which explicitly
states that it resolves this question; the author-hosted PDF is internally dated 31 October 2004, and
the file distinguishes that from the publication date.

*The retained argument.* For each $x$ choose a geodesic word $w_x$ of length $\ell_x$ and randomise
between it and the reversed inverted word chosen for $x^{-1}$, which represents the same element with
the same length. With $N_s(x)$ the number of occurrences of $s$ in the randomised word,

$$a_s = \frac1{|G|}\sum_x\ell_x\,EN_s(x), \qquad A = \sum_sa_s = \frac1{|G|}\sum_x\ell_x^2 \le D^2 .$$

Word inversion gives $a_s = a_{s^{-1}}$, and $a_s>0$ because the word for $s$ has length one, so
$\mu(s) = a_s/A$ is a symmetric probability measure supported exactly on the generating set. Using
$\mathrm{Var}_\pi f = \frac1{2|G|^2}\sum_{z,x}\left(f(zx)-f(z)\right)^2$, telescoping along the chosen
word for $x$ and applying Cauchy-Schwarz, and noting that for each occurrence of $s$ translating the
summation variable by the preceding prefix leaves the uniform sum unchanged,

$$\mathrm{Var}_\pi f \le \tfrac12\sum_sa_s\,E_{z\sim\pi}\left(f(zs)-f(z)\right)^2 = A\,\mathcal E_\mu(f,f),$$

so the variational characterisation gives $\tau_2 \le A \le D^2$. The randomisation is what makes the
counts symmetric in a noncommutative group; a deterministic word table need not. The source's own
comparison Theorem 7.16 with uniform comparison increments reproduces the same bound.

*My re-derivation.* The load-bearing step is that translating by a prefix preserves the uniform sum,
which is left invariance on a finite group; the rest is the standard variance representation and
telescoping. Agreed with the record. The file says the rest plainly: "This derivation was written
before the Pak source was found in the campaign's later-literature check. Discovery order does not
imply novelty." The convention matters and the file states it: this is the continuous-time
$\tau_2 = (1-\lambda_2)^{-1}$, not a claim about absolute discrete-time eigenvalues on a bipartite
graph, where half-holding costs a factor two.

### P0249. The reversibilisation trace inequality, implied by a later theorem

*As posed.* Aldous and Fill, Conjecture 9.22 with Corollary 9.24, PDF pages 327 to 329, dated 21
April 1995: for an irreducible finite transition matrix $P$ with adjoint $P^*$ in $L^2(\pi)$ and
centred fundamental matrix $Z$, prove or refute
$\mathrm{tr}\left[Z^2\left(P^*-P\right)\right] \ge 0$. The centred convention is $Z\mathbf1 = 0$ with
$Z = (I-P)^{-1}$ on $L^2_0(\pi)$; adding the constant projection would not change the product.

*Status.* `admitted: false`, `result_status: excluded_prior_resolution`, revised at 23:37Z on 6
September. The implying reference is Huang and Mao, *Variational formulas of asymptotic variance for
general discrete-time Markov chains*, arXiv:2012.13895, Theorem 4.3, which proves that the asymptotic
variance for a reversible kernel plus an antisymmetric perturbation is even in the perturbation
parameter and decreasing in its absolute value -- an observable-by-observable statement stronger than
the required trace monotonicity. The file notes that the source does not name Conjecture 9.22 in the
checked passage; the implication is what forces the exclusion.

*The retained argument, which is a real one-page proof.* On $L^2_0(\pi)$ put $A = I-P = H+K$ with $H$
symmetric and $K$ antisymmetric, so $K^* = -K$ and $P^*-P = 2K$; $H$ is positive definite because the
underlying undirected chain is connected and its only zero-energy functions on the full space are
constants. Let $Q = H^{-1/2}KH^{-1/2}$, $B = -Q^2 = Q^*Q \succeq 0$ and
$F(t) = \mathrm{tr}(H+tK)^{-1}$. Averaging the inverses at $t$ and $-t$ through
$(I+tQ)^{-1}+(I-tQ)^{-1} = 2\left(I-t^2Q^2\right)^{-1}$, with transpose invariance of the trace,

$$F(t) = \mathrm{tr}\!\left[H^{-1}\left(I+t^2B\right)^{-1}\right], \qquad F'(t) = -2t\,\mathrm{tr}\!\left[H^{-1}B\left(I+t^2B\right)^{-2}\right] \le 0 \quad (t \ge 0),$$

the trace being nonnegative not because the product is symmetric -- it need not be -- but because
$C = B\left(I+t^2B\right)^{-2}$ is positive semidefinite and
$\mathrm{tr}\left(H^{-1}C\right) = \mathrm{tr}\left(C^{1/2}H^{-1}C^{1/2}\right) \ge 0$. That is the
step where an invalid commuting assumption would hide, and the file names it. Differentiating the
original inverse gives $F'(1) = -\mathrm{tr}\left(A^{-2}K\right)$, so

$$\mathrm{tr}\left[Z^2\left(P^*-P\right)\right] = -2F'(1) = 4\,\mathrm{tr}\!\left[H^{-1}B(I+B)^{-2}\right] \ge 0,$$

with equality if and only if $B = 0$, that is $K = 0$, that is $P$ reversible, since $H^{-1}$ is
positive definite and $b \mapsto b/(1+b)^2$ keeps positive eigenvalues positive.

*My re-derivation.* The resolvent-averaging identity and the similarity trick for the nonsymmetric
trace both check line by line. Agreed with the record. The file also records the reduction from
Huang-Mao in full -- add one-half holding $R = (I+P)/2$ so every convex mixture of $R$ and $R^*$ is
irreducible and aperiodic, apply the theorem to $R_t = (R+R^*)/2+t(R-R^*)/2$, sum the Poisson-equation
formula over an orthonormal basis of $L^2_0(\pi)$ to get
$\sum_j\tilde\sigma^2(R_t,e_j) = 2\,\mathrm{tr}(I-R_t)^{-1}-(n-1)$, and differentiate from the left at
$t = 1$, using $Z_R = 2Z_P$ and $R^*-R = (P^*-P)/2$ -- and notes that earlier finite-state
antisymmetric-perturbation work cited there may contain the result earlier still.

### Summary

"Verification" below is copied from the operative ledger record and the file's own header, never
upgraded. Every scoped-review receipt in this chapter disclaims human certification, novelty and
present openness, so that qualification is stated once here rather than in each row. No row is
independently certified.

| Id | Result type | Verification | Prior art state | Remaining gap |
|---|---|---|---|---|
| P0032 | Positive answer, Burdzy-Scheutzow 7.5 | candidate full solution, author and literature checks, no independent review | Leads named in the file: Chacon-Ornstein, Rost, Thorisson; Pitman-Tang Thm 5.7; Holroyd-Peres Thm 17; Last-Morters-Thorisson. Judged strong risk of being a classical shift-coupling consequence | Whether the source's prefix is unrestricted; no bound on $EN$, no finite-lookahead rule, no stopping-time version |
| P0033 | Counterexample, Lyons-Peres 17.18 | candidate full solution, author and literature checks, novelty unassessed | Johnson-Podder-Skerman endogeny criteria named, not assumed; tree-automaton literature unsearched | Nothing on strictly positive weights or intermediate hypotheses; which offspring laws admit such a colour |
| P0174 | Positive answer, $C = 1$, Hasebe-Ueda 3.3 | candidate full solution, author-checked, scoped review | Bounded search found nothing; the citation check on ALEA 15 (2018) 353-374 is owed | The source prints $2 \le C \le 4$ while its own example gives $C \ge 1$; if the printed bound is right under some reading of $D_\mu$, one of the two is wrong |
| P0189 | Counterexample to the literal general statement, van Handel 6.9 | candidate full solution, author-checked limited argument; the scoped reviewer contributed two steps and is disqualified for the amended proof | Novelty not claimed; the Brown measure of $u+v$, simplicity and unique trace are literature inputs | Says nothing about independent-entry ensembles, free limits or holomorphic Ginibre polynomials; no restoring hypothesis identified |
| P0193 | Counterexample, Hasebe-Ueda-Wang 4.7 | candidate full solution, author-checked, scoped review | Bounded search found no resolution; a two-atom measure is the first thing anyone would try | Failure proved only for $t \ge 5\pi$; no weaker hypothesis restoring eventual log-unimodality |
| P0208 | Counterexample to all three clauses, Aldous-Fill 7.27 | candidate full solution, author-checked, scoped review, Lean core for the hitting-time arithmetic (9 theorems, no sorry) | The graph is classical prior art, cited to Conder's notes by the file itself; no later disposition found | Prior art is the whole remaining work; correct bounds for arc-transitive graphs unknown |
| P0209 | Counterexample, Aldous-Fill 4.30 | candidate full solution, author-checked, scoped review, no Lean core | Bounded search found nothing; a 1994 question answered by a four-state chain should be assumed folklore | No replacement bound; the missing third quantity is identified but unproved |
| P0266 | Counterexample, Agresti-Veraar Problem 4 | candidate full solution, author-checked, scoped review, plus a full independent review on 10 September that attacked the argument in eight ways and found no error; conditional Lean core only | Novelty not claimed; the Bessel mechanism is classical, and the reviewer calls priority "the strongest unresolved publication objection" | Prior art; a complete stochastic formalisation; nothing for $\gamma^2<2$ |
| P0267 | Counterexample, Agresti-Veraar Problem 5 | as P0266, with its own receipt | as P0266 | as P0266; the narrower prose variants are untouched |
| P0276 | Counterexample to the literal statement, Salez 2.4 | candidate full solution, author-checked, the directory's most detailed scoped review (8 graphs, 360 characters, 2,720 projection entries, 18 rejected controls) | Reset mechanism classical, associated with Pak counterexamples; novelty claimed only for the unweighted realisation | Retired by the owner on 10 September, a more general manuscript of his own covering it; reported as history. Unbounded degree; whether the intended conjecture carries a degree bound was never checked |
| P0288 | Counterexample to assertion (ii), Pollett | candidate full solution, complete author-checked, scoped review of the original packet | Antecedent identified: Foley-McDonald arXiv:1709.07578, from which the same obstruction follows by a reviewer-derived Poissonisation; originality not claimed | Whether the continuous-time corollary was ever published; assertions (iii) and the common-exponent claim untouched |
| P0340 | Refutation of the proposed scale plus a linear limit, Aldous-Janson OP14 | candidate full solution, author-checked with exact controls on 6,918 trees and five rejected false identities, Lean core for the tree inequality (4 theorems, no sorry) | Novelty not claimed, but the one paper that could pre-empt it was checked and cleared (arXiv:2505.24821 never mentions drawn length); best novelty case of the batch | No law of large numbers, variance or CLT for $\ell(T_n)/n$; no closed form for $c_\ell$ |
| P0289 | Counterexample to the monotonicity clause, Leskela Problem 1 | candidate partial counterexample, author-checked; the expansion re-derived from scratch on 12 September and confirmed, with a second-order criterion added | Novelty not claimed; Heyman, Miyoshi-Rolski 2004 and the light-traffic literature not compared in full | The necessary-and-sufficient condition at fixed traffic; the third-order term has no sign structure in $c$ |
| P0001 | Partial: negative association for cactus graphs; a proof route refuted | partial result, author-checked special case only | No novelty claimed; Tang-Zhang restate the general conjecture in March 2026 | The general conjecture; an inequality for overlapping cycle constraints through graphic-matroid structure |
| P0004 | Partial: root-independence of the limsup, plus an annealed bound | partial result, author-checked special case only | The conclusion is already in Lacoin arXiv:1203.6051, which the file names and credits | Existence of the limit; the liminf's rate. No stationary subadditive process exists |
| P0341 | Counterexample to both parts of Ansatz 20 | candidate partial counterexample, author-checked | No priority claimed; Brandenberger-Chin-Mossel bounds credited | Open Problem 8 itself: explicit two-parameter bounds and the right regularity class |
| P0342 | Scope counterexample to an unrestricted fringe CLT transfer | candidate partial counterexample, author-checked | No novelty claimed | The limit is a degenerate Gaussian; a positive-variance or fixed-neighbourhood reading is untouched |
| P0355 | Literal-scope counterexample to Conjecture 34 | candidate partial counterexample, author-checked | Bounded search found no correction; later work usually assumes positive marks | The intended strictly discounted nondegenerate regime |
| P0389, P0390 | Window-quantifier correction to the ARW hyperuniformity questions | candidate partial counterexample, author-checked with exact finite controls | No novelty claimed | The ARW transition and its exponent in a mesoscopic or bounded-volume-fraction regime |
| P0411 | Partial: monotonicity in all dimensions, the odd-dimensional polynomial, and a negative sixth coefficient in $d = 2$ | candidate partial counterexample, author-checked, three independent coefficient lanes | No novelty established; the $d = 3$ formula and odd-dimensional rationality are the source's own | Other even-dimensional density and median claims; whether the authors intended a different variable, which would change the disposition |
| P0429 | Partial: a modular bound and an exponential-service regime $k = o((n/\log n)^{1/3})$ | candidate partial counterexample, author-checked, private packet | Method credited to Wang et al. including its $k = o(n^{1/4})$ theorem; may be a known corollary | General service laws; the optimal threshold; nothing at $k \asymp n^{1/3}$ |
| P0458, P0459 | Partial: a non-Gaussian degree limit for $k = o(n^{2/5})$, and concentration for $k/\log n \to \infty$ | candidate partial counterexample, author-checked, private packet, finite controls on all 720 four-vertex orders | 2025 connectivity theorem credited; no novelty claimed | Other growth regimes, optimal tails, the critical logarithmic regime, bounded $k$ |
| P0096 | Known: literature counterexample rederived | admitted false, resolved in literature | Ahlberg arXiv:1911.09949, JAP 57(2) 407-408 (2020), explicitly refutes this survey question | None as a problem; retained as an explanation |
| P0140 | Known: literature result rederived with a scope correction | admitted false, resolved in literature | Dhara, van der Hofstad, van Leeuwaarden and Sen, eq. 2.22 and Remark 11, already identify the corrected law | None as a problem; the novelty of the direct marking calculation is unsearched |
| P0248 | Known: rederivation of a resolved question | admitted false, excluded prior resolution | Pak, SODA 1999, Theorem 3.1, explicitly resolves Aldous-Fill 7.18 | None as a problem; the derivation predates the discovery of the source, which does not imply novelty |
| P0249 | Known: consequence of a later theorem, with a direct matrix proof | admitted false, excluded prior resolution | Huang-Mao arXiv:2012.13895 Theorem 4.3 implies the trace monotonicity; earlier work may contain it | None as a problem; the equality case, reversibility, is a clean by-product |

Two counts, for a reader who wants one number. The ledger carries twelve
`candidate_full_solution` rows, and every one survived the re-derivations above at every step I was
able to check. The number of independently certified full solutions in this chapter is zero, and that
is the number to quote.
