## The attempts of 12 September, and what the interrupted lanes left

This chapter records the work of 12 September 2026, when several agents worked live problems with the
mathematical brain and a report was assembled from the six ledgers. Most of those agents were cut off
mid-task when the account's usage window ran out. Their partial work is recorded here rather than
discarded, because two of them had already produced mathematics and one of them produced a new result.
What follows separates what was finished from what was in flight, and says for each unfinished lane
exactly where it stopped.

The attempts are recorded in a seventh ledger,
`06_math_research/probability_1000_attempts_H_20260912/`, with the attempt rows, a log of every
question put to the mathematical brain and how the answer was judged, and the search scripts. The
memos are in the Downloads folder with the other campaign memos.

### P0289, Ross's second conjecture: the expansion re-derived, and a variance criterion

Source: Leskela, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100
(2022), 213-215, Problem 1. A single-server queue with Cox arrivals of intensity
$\lambda_c(t) = \lambda(ct)$, with $\lambda$ stationary and ergodic, independent and identically
distributed service, stable, and $w(c)$ the mean stationary workload. Is $w$ nonincreasing in $c$, and
if not, what condition on $\lambda$ makes it so?

The campaign's proof packet refutes the universal clause with the environment
$F(t) = 2 + \cos(\theta X_t + \theta/4)$, where $X$ is the clockwise-only continuous-time Markov chain
on $\mathbb{Z}/1024$ at rate $1/\sin\theta$, $\theta = 2\pi/1024$, with unit service and
$\varepsilon = 10^{-4}$. On 8 September the mechanism was verified and the numerical half closed, which
left one named obligation: the light-traffic expansion
$$w(c) = \frac{\varepsilon a}{2} + \varepsilon^2 \int_0^1 (1-u)\,\mathbb{E}[F(0)F(-cu)]\,du + R_c,
\qquad 0 \le R_c \le \frac{\varepsilon^3 M^3}{2(1-\varepsilon M)},$$
uniformly in $c$, had been taken from the packet as given. The whole counterexample rests on that step.

It was re-derived from scratch on 12 September. The route: a square-workload balance
($d(V^2) = -2V\,dt$ between arrivals, an arrival at $t$ adding $2V(t^-)+1$, with $V(t^-)$ predictable
and the moments controlled by the M/D/1 workload of the un-thinned rate-$\varepsilon M$ Poisson
process) gives $w = \varepsilon a/2 + \mathbb{E}[\lambda(0)V(0)]$. The shot lower bound
$V \ge S$, with $S(A) = \sum_{T \in A \cap (-1,0]} (1+T)$, follows from evaluating the Reich supremum
just after the first arrival in the window. The difference $D = V - S$ is nondecreasing under the
addition of an arrival, which under the thinning coupling bounds
$\mathbb{E}D \le \rho^2/(2(1-\rho))$ with $\rho = \varepsilon M$ and yields the uniform remainder. The
first term comes from Campbell's formula. The environment's autocorrelation works out to
$\mathbb{E}[F(0)F(t)] = 4 + \tfrac12 e^{-\delta|t|}\cos t$ with $\delta = \tan(\pi/1024)$, because the
uniform average kills the first harmonics and the second spatial harmonic, and
$\mathbb{E}\cos(\theta J)$ for $J$ Poisson of rate $r t$ is $e^{-\delta t}\cos t$ when $r\sin\theta = 1$.

Numerical checks at 30 digits reproduced the 8 September values, $J(2\pi) = 0.000972$,
$J(3\pi) = 0.022520$, and confirmed that the packet's rational bounds are valid lower bounds with room
to spare: the true half-difference is 0.01077 against a claimed $137/46080 = 0.00297$, and the true
margin $0.0094\varepsilon^2$ against a claimed $0.00154\varepsilon^2$. The packet is right at every
step the re-derivation could reach, so the counterexample now stands as author-checked by a second
reader. The remaining doubt is prior art, not the mathematics: Heyman's periodic-intensity
counterexample to the first conjecture, Miyoshi and Rolski 2004, and the light-traffic literature were
not compared in full.

**What the re-derivation added.** Substituting $v = cu$ turns the second-order coefficient into a
variance:
$$\int_0^1 (1-u) R(cu)\,du = \frac{1}{c^2}\int_0^c (c-v) R(v)\,dv = \tfrac12 \operatorname{Var}(\bar F_c),
\qquad \bar F_c = \frac1c\int_0^c F,$$
where $R$ is the autocovariance of $F$. So, exactly,
$$w(c) = \frac{\varepsilon a}{2} + \varepsilon^2\Big[\frac{a^2}{2} + \tfrac12\operatorname{Var}(\bar F_c)\Big] + R_c .$$
To second order in the traffic parameter, faster modulation lowers the mean workload exactly when it
lowers the variance of the environment's average over one service time. Differentiating,
$$\frac{d}{dc}\operatorname{Var}(\bar F_c) = \frac{2}{c^3}\int_0^c (2v - c) R(v)\,dv,$$
so the light-traffic form of the conjecture holds if and only if $\int_0^c (2v-c)R(v)\,dv \le 0$ for
every $c > 0$. Three consequences follow, all elementary.

First, if $R$ is nonincreasing on $[0,\infty)$ the condition holds, because the weight $2v-c$ is
antisymmetric about $c/2$ and $R$ is larger where that weight is negative. Every reversible stationary
continuous-time Markov chain has $R(v) = \sum_k a_k^2 e^{-\lambda_k v}$ for any observable, so a
reversible environment can never produce a second-order counterexample, whatever its monotonicity
properties. That is why the counterexample had to be non-reversible, and Leskela's own star-chain
example for his Problem 3, which is reversible, is consistent with it.

Second, the supermodular route of Bauerle and Rolski sits above this condition: the hypothesis in
Leskela's note implies $R(c_1 v) \ge R(c_2 v)$ for all $v$, that is $R$ nonincreasing, hence the first
consequence.

Third, if $\operatorname{Var}(\bar F_c)$ is strictly larger at some $c_2$ than at some $c_1 < c_2$, then
$w(c_1) < w(c_2)$ for every $\varepsilon$ with
$\varepsilon M^3/(2(1-\varepsilon M))$ below the variance gap. For the packet's environment the
derivative is positive on roughly $(2\pi, 9)$, and the deterministic random-phase environment
$2 + \cos(t+U)$ gives the undamped $R(v) = \tfrac12\cos v$ and the same conclusion with no Markov chain
at all, which is presumably where Heyman-type examples live.

This is a partial answer to the second clause of Problem 1, a necessary and sufficient condition for
the light-traffic version of the monotonicity, and it explains the non-reversibility of the
counterexample. It is not a condition for the conjecture at fixed traffic: when
$\operatorname{Var}(\bar F_c)$ is nonincreasing the third-order remainder is bounded but not signed, so
nothing follows about the conjecture itself. No novelty is claimed; this looks like something that
should be in the light-traffic literature on Cox queues, which was not searched beyond the brain.
Obligations left: the prior-art comparison for both the counterexample and the criterion, and whether
the exact condition can be characterised at all, since the third-order term
$\mathbb{E}[\lambda(0)D(0)]$ showed no sign structure in $c$.

### G0013, Catalano and Lavenant: the exhaustive search extended to nine atoms

The conjecture concerns the coupling farthest from independence in quadratic Wasserstein distance. The
reduction already on record: the objective is convex over the doubly stochastic set, so a maximiser is
an extreme point, and discretised to $n$ atoms that is a permutation. The earlier search covered
$n = 3$ to $7$ exhaustively, with the identity and the reversal the unique maximisers, and
transposition hill-climbs from random starts ending at one of those two at $n = 10$ and $n = 12$.

On 12 September the exhaustive search was extended two further values, working over canonical classes
under the symmetry group rather than raw permutations:

| $n$ | classes | permutations | best objective | maximisers | runner-up | time |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 5,282 | 40,320 | $W_2^2 = 0.102539$ | the identity alone, as a canonical representative | 0.098633 | 69 s |
| 9 | 46,066 | 362,880 | $W_2^2 = 0.101204$ | the identity alone | 0.098461 | 426 s |

The conjecture holds at both values. In both cases the runner-up is a single adjacent transposition
away from the maximiser, at the end of the permutation, which is the same local structure the smaller
cases showed. Note what the table does and does not say: the maximiser is reported as the identity
because the reversal is identified with it under the symmetry used to form canonical classes, so this
is consistent with the earlier finding of two maximisers rather than a change to it.

This is evidence and not a proof. The exchange argument for general $n$, showing that any permutation
other than the identity and the reversal admits a local move strictly increasing the objective, remains
the obligation. The search scripts and the per-$n$ value tables are in the ledger's `g0013`
subdirectory.

### P0189, and what the brain served

The lane that worked P0289 also read the sources for P0189, Brown-measure convergence from general
strong convergence, without writing its ledger row before it was cut off. What it established: van
Handel's Problem 6.9 states the tempting conjecture for arbitrary strongly convergent families, with
strong convergence in the sense of norm convergence with matrix coefficients; Theorem 11.1 of Fan, Jekel,
Liang and Xu gives that the spectrum of $u+v$ is the closed disk at $\lambda = 1$, and their Theorem
12.2 gives the Brown measure as Haar measure on the circle at $\lambda = 1$, by a separate proof. Both
norm-convergence routes and the determinant and $q$-binomial nilpotency computation were re-checked by
hand. The next steps recorded were the P0174 normalisation fork, where the Hasebe and Ueda text was
still open, and then D0039.

On the brain's contribution, the log is small but worth reading exactly. Four questions were put to the
retrieval hook across the two lanes. On P0289 the brain served the 8 September memory that closed the
numerical half, and that memory named the expansion and its uniform remainder as the unchecked step,
which is what the lane then re-derived: a case where retrieval supplied the agenda rather than the
mathematics. On G0013 the brain was asked twice and judged once as the right field with no step turning
on it, once silent, and once served a note that changed the lane's next move. Against four asks that is
too small a sample to support any rate, and the honest summary is one clear help, one change of course,
and two misses.

### The lanes that were cut off, and where each stopped

Six agents were working when the usage window closed. Their partial work was read and is recorded here
so that nothing has to be re-derived.

**The store lane** had authored a bundle of 13 result nodes for the mathematical brain, one per
campaign result, each carrying the problem, the result, the mechanism and the verification state
copied from the record. The bundle is written and was never integrated, not even into the copy of the
store. Its titles show the shape intended, for instance "Aldous-Fill Open Problem 7.27 (our id P0208):
REFUTED" and "Aldous-Janson Ansatz 20 (our id P0341): REFUTED in both its convergent and its divergent
case". Resuming means integrating that bundle on a copy, scoring an owner-voice bank against it, and
landing it only if the standing instruments hold.

**The retrieval lane** took its own baseline through the hook and then diagnosed two of the three
outstanding locate-bank misses precisely, which is the useful residue. One of them, an item whose
answering value sits 593 characters into a 1,446-character statement, is a genuine window defect: the
window's term pattern recognises words, decimals and runs of two or more digits, so a question whose
discriminating token is a single digit has no term to weigh at all, and the head of the note wins on
topic words that the answering sentence does not repeat. The other had been listed as a floor miss and
is not one: the node is served, three store nodes carry the value, and none of them is chosen, so the
defect is in ranking. It also found that another agent had edited the same retrieval file while its
write claim was live, with both new code paths defaulted off.

**The proof-sense lane** built a 103-item measurement set with frozen shards and three posture variants
recorded by content hash, and dumped the six items of interest with their fault classes before it died.
It also reported, on the shared message bus, the two reruns that no one had yet read: on the
hundred-item bank the no-notes arm read 91 and the notes arm 94, and on the harder thirty-five-item
bank 29 against 33, with the notes-and-posture slice moving 20 to 25. Its own caveat is the one to keep:
the prompts and keys were byte-identical between the two days, yet the no-notes arm moved from 87 to 91,
and the only change was the shard size, so the effect being measured is the same size as an unexplained
move. Nothing from that lane should be quoted except paired numbers at a fixed shard size.

**The coverage lane** had read the store and was building its bundles when it stopped. Its useful
finding is one it reported rather than wrote: another agent had already landed 249 curated analysis,
functional-analysis and partial-differential-equation nodes into the live store that afternoon, taking
it from 7,451 to 7,700 nodes, so the coverage that remained was the probability side rather than the
analysis side. That other agent also recorded a trap worth repeating: an unscoped integration sweep
pulled about a thousand entries of an undecided harvested corpus into the store and had to be reverted.

**The two results chapters** of this report, covering the written proofs of the Codex campaign and the
thirteen settled problems, were both in the middle of their re-derivations when they stopped. They are
the gap in this document, and the chapter list says so.
