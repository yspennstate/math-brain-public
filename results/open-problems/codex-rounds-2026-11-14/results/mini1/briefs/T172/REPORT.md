VERDICT: PROVED a uniform bound with logarithmic losses for growing-depth batching under iid uniform Bernoulli traffic.

For every `n>=2` and `0<epsilon=1-rho<=exp(-128)`, the policy in `PROOF.md`
satisfies, both from an empty switch uniformly in time and in a stationary
version with random scheduling phase,

\[
 \mathbb E Q_\Sigma
 \leq 10^6\,\frac n\varepsilon\,
 \log\frac{144n}{\varepsilon}\,
 \bigl(1+\log(1/\varepsilon)\bigr)^9.
\]

Arrivals must be independent Bernoulli variables over slots and queues,
of common mean `(1-epsilon)/n`. The exact `O(n/epsilon)` conjecture remains
open. The result here allows the number of batching levels to grow with
the load, replacing the fixed positive power loss in epsilon by logarithmic
factors. It is a corollary derived from an existing construction; historical
novelty is not established.

The literature search took under four minutes and found no later full
solution. The construction is due to Taha Ameen and Weina Wang,
*Approaching Optimal Scaling of Queue Size for an Input-Queued Switch*,
[arXiv:2610.37521v1](https://arxiv.org/html/2610.37521v1), submitted
27 October 2026. Its stated theorem fixes the depth. `PROOF.md` verifies
the growing-depth choice directly, including the graph estimate, rounding,
failure accumulation, matching-queue drift, and packet count. No substitution
into a fixed-depth big-O theorem is used.

Use

```sh
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > AUDIT_OUTPUT.txt 2>&1
```

The saved output reports 276 exact rational exponent identities, 44 rounded
parameter cases, 8,904 pathwise port-count identities, and 297 comparisons
between chronological service and an independent offline batch construction.
Case data and seeds are in `AUDIT_DATA.json`. The small-switch computation
checks structural statements; it does not simulate the theorem's very small
epsilon or estimate its stationary mean.

The command exited with status zero, at about 18 MB peak RSS, below its
90-second CPU limit. The sandbox denied changing priority, so `nice` emitted
an error; the program verified its actual inherited nice value was 20,
lower priority than 15. It used one thread and the Python standard library.

The attempted shortcut of using the published fixed-depth theorem alone
does not prove this result. The failed goal is removing all logarithmic
losses. Nonuniform traffic and arrival processes specified only by rates
are outside the proof. No independent external referee has checked this
derivation; the supporting computation is finite and is not a substitute
for its uniform inequalities.

The next worker should first audit the uniform-depth argument, especially
the causal parent/child service timing and the independence of final batches.
Then improve the level-dependent block multipliers: the use of
`D=288^k` and the final conversion to a ninth power are deliberately coarse.
Removing that growth would sharpen the logarithmic loss; removing the
remaining concentration logarithm requires a further idea.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:18 Asia/Tbilisi.
