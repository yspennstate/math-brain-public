# C26 v1: the absorbing-parent extinction atom

Status: proof (unaudited). Kind: special. Target 1.
This observation corrects a screening criterion; it does not classify T3.

Let0<=p<1/2. A fresh recursive root has one original resident and one incoming
ordinary frog, with no other awake frogs. Each of their first independent
steps goes to the parent with probability p. A frog that hits that parent
stops. All other frogs start asleep and can wake only through an awake visit.
After the first incoming seed, close all permitted activity before adding
another seed. Let V be the resulting parent-return count, possibly infinite.

Then

    P(V=2)>=p^2,
    E[s^V]>=p^2*s^2  for0<s<1,
    P(V=infinity)<=1-p^2.

Here s^infinity means0. In particular, at p=1/4 and s=1/2 the PGF is at least
1/64. A PGF that remains positive cannot by itself rule out a positive
probability of infinite lower-model returns.

Proof. Let E be the event that the two initial ordinary steps both go to the
parent. Their independence gives P(E)=p^2. On E both frogs stop immediately.
Neither visits a child, so no other frog can wake. Thus V=2 on E, regardless
of awakening depth or child-entry cap. All three conclusions follow from this
event and nonnegativity; no limit interchange is involved.

The hypotheses matter. Root reflection does not stop the two returning frogs.
The non-backtracking incoming frog cannot reverse its entrance edge. An
already active third frog can continue after the two initial returns. The
argument asserts no positive extinction atom in those different situations.
At p=0 the stated lower bound is0 and gives no obstruction. The PGF parameter
is restricted to0<s<1 to avoid conventions at0 and at1 for infinite counts.

The full ordinary model has a separate0-1 law (HJJ1404.6238, Theorem4).
Consequently a valid lower comparison with positive probability of infinite
returns is sufficient for full recurrence; the lower model need not itself
have probability-one infinite returns. The model comparison is supplied by
C27, subject to its own independent audit.

Checks: Python Fraction verifies (1/4)^2*(1/2)^2=1/64. The first
Mathlib attempt returned RUNTIME_UNVERIFIED; no Lean verification of this
arithmetic or of the probability argument is claimed. Source protocol:
simulate_joint_ordinary_excursions.py, sample_joint, initial two pending frogs
and parent-step Binomial(2,p). C25's independent direct finite-tree controls
are numerical agreement checks, not a proof of the probability argument.

This elementary observation is submitted for correctness and screening use;
novelty is not claimed. C28 now gives a stronger, uniform finite-mean
obstruction for every fixed ordinary entry cap at p=1/4; C26 alone does not.
