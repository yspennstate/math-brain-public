## What is solved, by area and by mechanism

This chapter is the map. The arguments themselves are in chapters 3, 4 and 5; what follows is where
the results sit in probability, what kind of argument produced each one, and what the audits learned
about the way this work fails.

### Markov chains, mixing and hitting times

The richest vein, and the one where the campaign produced its cleanest refutations. The Aldous and
Fill manuscript, *Reversible Markov Chains and Random Walks on Graphs*, poses open problems in a form
that invites a counterexample: it asks whether a parameter is $O(n\log n)$ over a class of graphs
after excluding the obvious bad family, and it says in the sentence before the question that nobody
knows whether the excluded family has a member inside the class. Three results came out of reading
those sentences carefully.

Open Problem 7.27 asks whether, over arc-transitive graphs excluding the $n$-cycles,
$\tau^* = O(n\log n)$, $\tau_2 = O(n)$ and $\tau^*/(2\tau_0) = 1 + o(1)$. The answer is no, and the
counterexample is the lexicographic product $C_m[\bar K_2]$ for odd $m \ge 5$: the $m$-cycle with each
vertex split into two non-adjacent twins. It is 4-regular, connected, arc-transitive, and not a cycle,
and its relaxation time is quadratic in $n = 2m$. The mechanism is that splitting a vertex into
non-adjacent twins preserves arc-transitivity while leaving the cycle's slow mode intact; the
manuscript's own Example 7.14, the ladder $\mathbb{Z}_m \times \mathbb{Z}_2$, is only
vertex-transitive, which is why the question was posed at all.

Open Problem 4.30 and a second question adjacent to 7.27 fell to the same kind of construction, one of
them through a thickened cycle. P0208 in the ledger is the arc-transitive wreath graph family with
quadratic hitting and relaxation times, labelled a candidate full solution and author checked; P0209 is
the uniform stationary normal approximation question from gap and bounded observables, also a
candidate.

The 8 September session also found that the later literature had already resolved Aldous and Fill Open
Problem 6.14 (Zhu, 2609.06818) and all seven Haggstrom and Rosenthal central limit theorem problems
(Brown, Rosenthal and Zhou, 2609.07819). Recording that is worth as much to the campaign as a proof; it
is the difference between a live problem and a spent one.

The cutoff line, P0276 on the product condition for unweighted abelian Cayley graphs, was retired by
the owner on 10 September because a more general manuscript of his own covers it. It appears in
chapter 3 as history, not as a live result.

### Percolation and random graphs

F0090 is the campaign's most ambitious claim: Kalai's Conjecture 8, which is the first open problem of
Garban, Pete and Schramm's 2010 work, asking whether the entropy of a planar percolation crossing
event is $O$ of its total influence. The argument is author-checked with a first independent read and
no independent certification.

Closed on 13 September 2026: the author posted the write-up as a ResearchGate preprint, *Entropy and
singularity of spectral and pivotal sets in planar percolation*, publication 414266816. The posted
paper is wider than the ledger row. It states the entropy bound for both the spectral sample and the
pivotal set, on the square lattice and the triangular lattice, uniformly over a class of
inhomogeneous near-critical product measures, and it adds a second theorem that the two laws are
asymptotically mutually singular for critical triangular-site square crossings, detected by an
elementary triangular face that the pivotal set forbids and a large spectral sample contains with
positive density. That second theorem answers open problem 5 of the same section of Garban, Pete and
Schramm, which no ledger row asks. Publishing is not refereeing: the closure records the author's
decision, not a verification.

G0001, from Cerf's 708-page monograph, turned out on reading to be equivalent to $\theta(p_c) = 0$
given the source's own Theorem 1.2 and the Kesten and Zhang supercritical tail. That is not a
solution; it is a reformulation, and the right action was to merge it with the earlier row that
already asks the same question. Recognising an equivalence is the cheapest progress available in a
corpus this size, and it happened only because the attempt read both statements side by side.

G0008, two-point monotonicity on $\mathbb{Z}^2$, is eventually monotone in $n$ at every $p \ne p_c$ by
Ornstein and Zernike asymptotics; the first attempt's stronger claim, that it holds for all $n$ at
small $p$, was withdrawn in the same session because the ratio argument does not give uniformity in
$n$. Withdrawing a claim inside the session that made it is the behaviour the audits reward.

P0001, negative correlation in uniform forests, is proved for cactus graphs and open in general. P0096
is a rederivation of a known four-edge-minimum lower bound for the first-passage percolation time
constant.

### Random matrices and free probability

Three candidates here, all on the free-probability side: P0174, a sharp support-diameter threshold for
free Brownian unimodality; P0189, Brown-measure convergence from general strong convergence, with a
scope caveat recorded in its own row; P0193, eventual log-unimodality from arbitrary compact positive
initial laws. A sharp free-Brownian mode-curvature bound was written up separately on 10 September.

The open ends here are analytic rather than combinatorial. P0189 needs the strong convergence of the
clock-and-shift pair and an answer to which limit's Brown measure is the limit. Result 11 of the
thirteen-settled memo has an unresolved normalisation fork between two conventions of Hasebe and Ueda.
E0046, on the complex Ginibre ensemble's average singular value, is explicitly known and is recorded
that way.

### Gaussian processes, stochastic calculus and SPDE

P0032 asks whether adding a finite prefix to a path can produce an equivalent Brownian law, and what
is recorded is a construction. P0266 and P0267 are the two Agresti and Veraar problems on critical
variational SPDE: a maximal second-moment bound including the critical Allen-Cahn case
$\gamma^2 = 2$, and endpoint energy-space continuity. Both are labelled candidate full solutions, and
both are counterexample-shaped rather than positive results, which matters for how much of the
source's question they close.

The nearest relative of one of the thirteen settled results is already identified in the record: Last,
Morters and Thorisson, *Unbiased shifts of Brownian motion*, arXiv:1112.5373. That is the kind of note
that has to be written down before novelty is claimed anywhere.

### Combinatorial probability and trees

Intake F's Janson results are the two with the most machine support. F0055 proves that the largest box
is $o_p(\log n)$ when $m/n \to 0$ and carries a Lean-certified core. F0057 proves a total variation
approximation for every large box count by a rare-cloud Janossy and Bonferroni argument with an
adaptive threshold, and carries a source correction that is still pending: the count inclusions omit
the truncation good events, which is finding P30H-F001 in the audit registry.

P0340 settles the growth of the minimal drawn length of critical beta-splitting trees: it is linear,
not $n\log^4 n$ as the ansatz suggested. The Aldous and Janson ansatz 20 itself is false in both of
its parts, and that is the most consequential single result in the campaign, because the authors invoke
that ansatz elsewhere in their own programme.

F0056, the sparse parity counterexample, is at author stage. The construction is $w_0 = 1$, $w_1 = 0$,
$w_j = 1$ for $j \ge 2$, $n = k^4$, $m = 2k+1$; the conditioned odd sum forces a maximum of at least 3
while the corresponding tilted independent rare-event probability tends to zero, so the total variation
distance tends to 1. What remains is exact tilt existence at mean $(2k+1)/k^4$ and then the assembled
independent-versus-conditioned limit.

### Quadratic stochastic operators, queueing and applied models

Intake E's quadratic stochastic operator family produced the campaign's two clean "proved" labels
outside intake F: E0061, the sufficiency of the sign condition in Ulam's ergodic theorem for a
three-type operator, and E0063, whether partition-type operators inherit the F-QSO fixed point.
E0064, Rozikov's Problem 11, is a refutation: uniqueness of the fixed point fails for five types, with
two fixed points exhibited exactly. E0078 refutes a stochastic ordering between time-stationary and
event-stationary Markov-modulated Poisson process waiting times by an exact rational counterexample
whose roots were checked. E0077 was proved and then excluded, because He's 2021 result already covers
it, and the exclusion is the correct disposition.

E0104 and E0105 in the mobile Boolean model are settled in restricted cases, inertial balls and the
homogeneous case respectively, and the restriction is in the label for a reason: the general question
is open. P0288, on rank-one polynomial asymptotics for transient Markov chains, has a published
antecedent, Foley and McDonald 2017. P0289, Ross's second conjecture, has a verified mechanism and an
unchecked quantitative half.

P0291, Leskela's problem 3, produced a nonmonotone chain with a supermodular time ordering, with an
author-checked proof and an explicit example.

### The mechanisms that actually worked

Six kinds of argument produced everything above, and they are worth naming because they are the
campaign's transferable output.

**Twin splitting and thickening.** Replace a vertex by non-adjacent twins, or a cycle by a thickened
cycle, and a symmetry hypothesis survives while the slow mode the question hoped to exclude stays put.
This produced the Aldous and Fill counterexamples.

**Reading the sentence before the question.** Three results came from the source's own admission that
it did not know whether the excluded family intersects the class. The question was posed because the
author could not build the object; the object exists.

**Refuting an ansatz by exact computation.** The Aldous and Janson ansatz fell to a computation carried
through rather than to an asymptotic argument, and so did the drawn-length growth rate.

**Exact rational counterexamples.** E0078 and E0064 are finite objects with rational data whose roots
can be checked to the last digit, which is why they carry the strongest verification in the corpus
short of Lean.

**Correlation inequalities, mostly FKG.** G0004, G0005 and several intake rows advance exactly as far
as FKG takes them and stop where many-contact or non-monotone regimes begin. Where FKG stops is a
reliable predictor of where the remaining obligation sits.

**Exhaustive finite search followed by a structural reduction.** G0013 reduces to permutations by
convexity of the objective over the Birkhoff polytope, and then an exhaustive search over all
permutations up to $n=7$ and hill-climbing at $n=10$ and $n=12$ finds the identity and the reversal as
the only maximisers. The search does not prove the conjecture, and the record says so.

### How this work fails, from the audits

Two audits read the whole corpus, one on 8 September over the 25 written proofs and intake D's
exclusions, one on 9 September over all five ledgers. Between them they found no wrong calculation.
That is the surprising part and it should be said plainly: nine independent re-derivations and 25 proof
files produced no arithmetic error.

The failures were of two other kinds, and both are caught by reading rather than by computing.

The first is a conclusion phrased more strongly than its derivation supports. Three of intake D's six
flagged partials overstated their conclusions, and in every case the missing caveat was already written
in the row's own obstruction field. The fix is mechanical: read the result field against the
obstruction field before believing the result.

The second is a citation that matches a neighbouring object rather than the stated one. One of intake
D's eight literature exclusions was wrong for exactly this reason. Virag's question 1 asks whether the
beta-Hermite measure and the Gaussian multiplicative cascade measure of the same Hausdorff dimension
have the same fractal spectrum. The paper cited to close it identifies Gaussian multiplicative chaos on
the circle with the circular beta ensemble, which is the circular analogue of a different measure. So
the question names the beta-Hermite object and the cited theorem is about the circular one, the
exclusion fails, and D0039 should be re-admitted as open. The circular theorem is good evidence that the
analogous answer is positive and its methods may transfer, but transferring them is mathematics somebody
has to do rather than a citation. One exclusion in eight was wrong, and the check that caught it takes
minutes: read the source's own sentence stating the question, read what the cited paper claims, and
compare the objects by name. What produced the error is worth naming too, because it is not carelessness
but a near-miss in wording: the row's own search summary said the paper answers "a question raised by
Virag", which is not the same as the question Virag asked.

A third pattern appears in the 9 September findings rather than in the earlier audits: a step that needs
a derived structure and assumes it instead. Those four findings are worth stating individually, because
all four are classified LOW and in every case the thing that is wrong is a displayed sentence rather
than the result it sits inside. The reports are under
`12_cognitive_architecture/audits/reports/2026/09/09/`, each with its own evidence directory; the
F0057 report's recorded hash still matches the file on disk.

**P30H-F001, the truncated count inclusions.** The F0057 memorandum defines its intervals with an upper
cutoff and then displays its two count inclusions as exact events without intersecting the event that
the maximum stays below that cutoff. Both directions have exact counterexamples: for the upper
inclusion, the sample $[100,4]$ with $j=2$ on the interval $[3,5]$ puts the second-largest value in the
target set while the truncated count is zero; for the lower inclusion, $[100,99,4,3]$ satisfies the
truncated conditions while the second-largest value sits outside. A Lean file proves both corrected
implications, and an integer-only enumerator exercised 334,020 cases with ties and found no violation of
the corrected form. What this does not do is invalidate the asymptotic result: the source's own input
says the maximum exceeds the cutoff with probability $o(1)$, so intersecting with that good event and
subtracting the comparison tail repairs the bound. The correction to the two displayed lines is still
pending in both copies of the memo.

**P30H-F002, a reversed inequality in the quadratic-operator memo.** Section 3.2 of the E0065 memo
defines $\kappa = 2(1-\alpha)(1-m\alpha)$ and then equates $\kappa < 1$ with the polynomial
$2m\alpha^2 - 2(m+1)\alpha + 1$ being positive. Expanding gives
$\kappa - 1 = 2m\alpha^2 - 2(m+1)\alpha + 1$, so the sign is the other way; $m=3$, $\alpha = 3/20$ gives
$\kappa = 187/200 < 1$ with the polynomial at $-13/200$. The contraction argument before it and the
root threshold after it both use the correct direction, so this is a typographical slip that a reader or
a formalisation could copy out of context.

**P30H-F003, a scope claim in a Lean comment.** The header of a quadratic-operator file calls
$V(x,1-x) = (2x(1-x), x^2+(1-x)^2)$ an example all of whose trajectories converge to the barycentre.
The endpoints of the simplex are legitimate starting points and both stay at a vertex, so the universal
claim is false as written while the compiled theorem, which proves only a majorisation inequality, is
untouched. The repair is to say interior trajectories.

**P30H-F004, an assumed dependence structure.** An attempt asserted that conditioning a product law on a
fixed total makes the threshold events negatively dependent, for every total. Three coordinates
conditioned to sum to six with weights $w_0 = w_2 = 1$, $w_6 = 1/9$ and the rest zero leave only
$(2,2,2)$ and the permutations of $(6,0,0)$; the threshold indicators then have covariance $1/18 > 0$,
which defeats even pairwise negative correlation. The zeros are not essential, since replacing them by
one thousandth keeps the covariance positive, and a control with factorial weights recovers the familiar
multinomial behaviour. This rejects the premise of an attempt, not an asymptotic theorem, and keeping
that distinction straight is what this report tries to do throughout.
