VERDICT: PARTIAL proved transience for Bernoulli(q) sleepers at q<=41/100 on the 3-ary tree and q<=33/50 on the 4-ary tree

PROOF.md gives a complete weighted three-type upper comparison, including a
coupling and the reflecting root. It retains one remembered empty child and
collisions between two frogs in a packet. Exact rational supervectors yield
finite expected root visits. The sufficient q endpoints exceed those of the
elementary branching test, 1/3 and 9/16, by 23/300 and 39/400. These are bounds
for a diluted distribution; no claim of novelty or best published constants
is made.

For one initially active root frog, with no additional root sleeper, the
proved expected-visit bounds (including time zero) are 1640000/1239 and
273700/461. An additional root frog doubles these bounds.

Reproduce with:
```
OMP_NUM_THREADS=1 nice -n 15 python3 certificate.py > certificate_output.txt 2>&1
```
The saved run exits 0. Its exact output is in certificate_output.txt and
LOG.md; all matrix and boundary data are in certificate_data.json. The script
compares the derived matrix with exhaustive one-step enumeration and uses
rational arithmetic throughout. A separate audit computes the contraction
factor from normalized slacks and checks the expectation bounds. Peak memory
was 15,351,808 bytes and runtime was under one second. The sandbox rejected
priority changes and OS memory limits; the requested nice command was used,
the script measures RSS and has a 30-second alarm, and no heavy runs occurred.

What failed: these certificates have negative slack at q=1, so they do not
settle either original one-per-site case. A simpler exploratory d=3 vector
(1,39/20,19/20) at q=2/5,t=2 also failed its D-row inequality and was not used.

Literature: within the ten-minute search, an opened primary repository and
its release notes reported a complete solution by mt0-svg, with recurrence
for d=3 and transience for d=4. SOLVED_ELSEWHERE.md preserves the reference and
the limits of verification. The actual paper and formal sources could not be
retrieved, so the claimed full resolution was not certified here. No arXiv id
was found for it. The older papers actually opened were those of Christopher
Hoffman, Tobias Johnson and Matthew Junge (arXiv:1404.6238), Poly Mathews Jr
(arXiv:2309.14443), and Samyah Ahmed and Matthew Junge (arXiv:2510.18792).

Uncertainties: the validity of the reported full solution, whether stronger
Bernoulli bounds are already published, and how much further these packet
comparisons can be pushed. No optimized threshold or obstruction for every
possible supervector was proved.

Next worker: first obtain the reported full solution and inspect its model
definitions, theorem statements and proof dependencies. If valid, both cases
of T127 are settled elsewhere. Otherwise, an available exact starting point
is the three-type matrix here; retaining the empty child on a two-frog
backward move, or tracking more than two frogs, may give stronger bounds.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:17 Asia/Tbilisi.
