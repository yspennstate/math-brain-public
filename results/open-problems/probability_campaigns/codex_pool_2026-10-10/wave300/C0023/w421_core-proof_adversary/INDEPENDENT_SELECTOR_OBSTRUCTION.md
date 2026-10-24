Independent derivation, saved before reading w420's proof (2026-10-10).

The primary bond-percolation source is Kozma--Nitzan, arXiv:2401.12397v1, Conjecture 1:
P(o connects to b) >= P(o connects to A) min_{a in A} P(a connects to b),
for every finite graph with independent, arbitrary edge probabilities. This is a conjecture, not a proven inequality for general A.

A tempting proof selects the first connected member of A and applies FKG after selection. That conditional step is false, even on a path with all probabilities strictly between zero and one.

Take the four-vertex path o--a2--b--a1. Each of its three edges is independently open with probability 1/2. Order A=(a1,a2). Let F2 be the event that a2 is the first member of A connected to o. In edge notation X=o--a2, Y=a2--b, Z=b--a1,
F2={X=1 and not(Y=Z=1)}.
Then P(F2)=3/8 and P(F2 and a2 connects to b)=1/8. Thus
P(a2 connects to b | F2)=1/3 < 1/2=min_{a in A}P(a connects to b).

The selected-event condition contains a decreasing exclusion, so it is not an increasing event and FKG does not apply. Revealing the origin cluster likewise reveals closed boundary edges; unrevealed edges remain independent but the resulting connection probability is in a graph with those boundary edges removed.

The conjectured global inequality is nevertheless an equality here: P(o connects to A)=1/2 and P(o connects to b)=1/4. The first-selection event F1 has probability 1/8 and conditional connection probability 1; the second has probability 3/8 and conditional probability 1/3. Their weighted average gives 1/4. Failure of a pointwise conditional premise is not a refutation of Conjecture 1.

For a general ordering A=(a1,...,am), write Fi={o connects to ai and o is not connected to any earlier aj}. Exactly,
sum_i P(Fi)P(ai connects to b | Fi)=P(o connects to b and o connects to A).
Terms with P(Fi)=0 are defined as zero and need no conditional probability. A sufficient missing premise for this selection route is the WEIGHTED lower bound
sum_i P(Fi)P(ai connects to b | Fi) >= P(o connects to A) min_i P(ai connects to b).
No proof of that weighted premise is claimed. Replacing it by a pointwise bound loses precisely the compensation present in this path example.

NEXT: Ask w422 to check the eight edge configurations; read and test w420's actual central premise.
