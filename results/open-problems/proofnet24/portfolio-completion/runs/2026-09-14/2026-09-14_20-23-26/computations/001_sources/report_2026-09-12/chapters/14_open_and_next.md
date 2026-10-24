## What remains, in priority order

### Prior art on the results, and nothing else first

This is the whole distance between the campaign's results and anything publishable, and almost none of
it has been done. What is needed is not more search-engine queries. It is a citation check, per result:
pull the papers that cite the source, search each for the problem number, and read what they claim.
Two facts are already on record and show what the outcome looks like in both directions. Result 8 of
the thirteen-settled memo has its nearest relative named already, Last, Morters and Thorisson,
*Unbiased shifts of Brownian motion*, arXiv:1112.5373. Result 2 is confirmed clear of the one paper
that could have pre-empted it. P0288 has a published antecedent, Foley and McDonald 2017, found the
same way.

Until that check is done for a given result, the correct description of it is the one the ledgers use:
the mathematics is settled and the prior art is not cleared.

### The audit backlog

- **The 88 unaudited intake-D problems.** Intake D's eight literature exclusions and six flagged
  partials were checked; the remaining 88 rows have been read by nobody since they were entered.
- **D0039 should be re-admitted as open.** Virag's question names the beta-Hermite measure and the paper
  cited to close it is about the circular ensemble, so the exclusion fails. The row still carries it.
  Record Chhaibi and Najnudel as the closest known relative and the first thing to try.
- **The other six unchecked exclusions in that ledger.** Of the eight, two have been checked: D0039 is
  wrong and D0022 is right. The remaining six are D0001, the three sorting-network conjectures
  D0013 to D0015, D0055 and D0096. Every wrong exclusion is a live problem silently deleted, which is a
  worse error than an overstated result, and the check is two steps and takes minutes per row.
- **F0057's source correction is undone.** The authorised changes are recorded: the $G_Y$ and
  $G_\xi$ good events with maximum below $B$, the first inclusion intersected with $G_Y$ and the second
  union intersected with $G_\xi$, finite-$L$ complement errors absorbed into $o(1)$, the truncated
  bad-interval count equality weakened to an inequality, the exact independent identity only on
  $G_\xi$, and size-biased changed to tilted. Both literal copies of the memo still carry the old text.
- **The E0065 quadratic stochastic operator memo** has a sign error in its contraction polynomial
  (finding P30H-F002: the displayed polynomial should be negative, not positive, with the witness
  $m=3$, $\alpha=3/20$) and a Lean header that claims all trajectories converge to the barycentre when
  the two simplex vertices do not (P30H-F003). Both are recorded, both are classified LOW, and neither
  is corrected in the live files. Each report names the exact replacement text and the witness a
  re-auditor should replay, so these are half-hour jobs, not investigations.
- **The four 9 September findings all require a different agent to close them.** Their own re-audit
  criterion is that someone other than the auditor read the changed bytes and replay the original
  control. Nobody has done that for any of the four, so all four sit at SENT rather than closed.

### The mathematics that is one step away

Chapter 5 has the full list with each obligation stated precisely. The six worth starting on:

1. **P0289, Ross's second conjecture.** The mechanism is verified; the quantitative half is unchecked.
   This is the closest thing in the corpus to a finishable result.
2. **F0056, sparse parity.** Exact tilt existence at mean $(2k+1)/k^4$, then the assembled
   independent-versus-conditioned limit. The finite controls cover 9,762 odd allocations and the tilt
   brackets; they are not evidence for the theorem.
3. **G0013, Catalano and Lavenant.** The discretised problem reduces to permutations; the identity and
   the reversal are the only maximisers for every $n$ from 3 to 7 by exhaustive search and survive
   hill-climbing at $n = 10$ and $12$. What is missing is the exchange argument for general $n$.
4. **P0189.** Does the clock-and-shift pair converge strongly, and to which limit's Brown measure.
5. **Result 11's normalisation fork**, between the two Hasebe and Ueda conventions.
6. **G0005, Kozma and Nitzan Conjecture 3**, in the many-contacts regime, where the FKG argument that
   settles the bounded-contact case runs out.

### The formal side

The Lean inventory is 22 files and 80 named declarations that the kernel accepts in an isolated
namespace bundle, with standard axioms only and no `sorry`. No full source probability theorem has a
complete verified Lean correspondence. The honest next step is not more declarations; it is one
theorem taken end to end, with a separate statement-fidelity review that asks whether the Lean
statement is the source's statement. The F0056 partial-mass-function support model is the natural
candidate, and its last whole-file compile timed out after 1,800 seconds, so the first job there is a
fresh bounded compile that passes.

### The corpus itself

The mandate was a thousand problems and the corpus holds 908 admitted records. Intake G showed that
new sources are still arriving faster than they are being read: eight arXiv postings from a
three-week window yielded 15 rows, and three of the twelve candidate sources examined in that window
resolved earlier rows instead of posing new ones. A seventh intake would add rows; a more useful
seventh pass would take the 687 rows labelled attempted and unsolved and ask which of them the later
literature has quietly closed since the ledger was written.

### The mathematical brain

The lane that answers a question about the campaign's own work was, as of the morning of 12 September,
answering it badly: of 32 results checked against the 7,451-node store, 26 had a node and most of those
nodes carried the problem statement or an attempt note rather than the result and its verification
state, and 6 had no node at all. Work on that is under way in a separate program; the measurement to
repeat afterwards is the one that matters here, namely whether an owner-voice question about a result
gets that result's node.

The general finding from the campaign is worth keeping in view when planning the next one. On
proof-audit work, where a strong solver can already judge the argument, retrieved statements do not
change verdicts and the measurable gain comes from the posture that tells a reader to test each step
and name the first one it cannot re-derive. On locate-the-fact work, where the answer is a value only
the store holds, retrieval moves a solver from 3 correct out of 60 to 57 with no wrong answers. Use the
store for what it remembers exactly. It does not supply judgment, and the campaign's results came from
reading sources carefully, not from retrieval.

