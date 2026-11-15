VERDICT: PARTIAL proved transience for Bernoulli(q) sleepers at q<=419/1000 on the 3-ary tree and q<=337/500 on the 4-ary tree

The earlier result holds. independent_audit.py recovers its exact slacks,
root inequalities, contraction factors and expected-visit bounds without
importing its code or reading its certificate data.

The new result retains the empty child when both frogs in a pair step toward
the root. This adds one packet type to the earlier three-type comparison.
PROOF.md gives the full domination coupling, four-type mean matrix,
reflecting-root argument and rational certificates. The certified sleeper
probabilities increase from 0.41 to 0.419 for d=3 and from 0.66 to 0.674 for
d=4, gains of 9/1000 and 7/500. No optimality or priority over published
Bernoulli bounds is asserted.

For one initially active root frog, with no additional root sleeper, the
expected total root visits, including time zero, are bounded by
155982888000/2349271 for d=3 and 32481964500/2275273 for d=4. These large
bounds reflect the small strict contraction margins at the new endpoints.
An additional root frog doubles the bounds. Finite expectation proves
almost-sure transience throughout the respective smaller-q intervals.

Reproduce from this folder:
```
OMP_NUM_THREADS=1 nice -n 15 python3 independent_audit.py > independent_audit_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 four_type.py > four_type_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 audit_saved.py > audit_saved_output.txt 2>&1
```
All three saved runs exit 0. four_type_data.json contains the exact matrices
and certificate fractions. The matrix agrees with two independent event
enumerations. audit_saved.py then checks the saved data by scalar enumeration
of all full child-mark configurations and walk choices, independently of
the matrix code. It recovers every slack and root boundary value, both
contraction factors, both expectation bounds and the printed proof fractions.
LOG.md records the commands, outputs and case-by-case coupling audit.

The optional candidate search is reproducible with
`OMP_NUM_THREADS=1 nice -n 15 python3 four_type.py --search`.
It suggested thresholds near 0.41904 and 0.67426 on its finite t grid;
these are exploratory numbers, not certified thresholds. A normal run uses
only exact fractions in its mathematical checks. Every mathematical run
took under one second and measured below 20 MB RSS. The sandbox denied the
requested nice priority change; the denial is retained in the output files.
No parallel workers, GPU or numerical libraries were used.

What failed: at q=1 all four slacks of both displayed certificates are
negative. Neither original one-sleeper-per-site case is settled by this
comparison. The first exact run also caught an accidental float in the
additional slot-count audit; replacing integer division with Fraction fixed
it. The exact matrices themselves agreed before that correction.

The literature check took under five minutes. The same
[mt0-svg repository](https://github.com/mt0-svg/frog-model-tree) and
[release page](https://github.com/mt0-svg/frog-model-tree/releases) still claim
recurrence for d=3 and transience for d=4, but the paper, statement map,
formal definitions and Zenodo deposit could not be retrieved. No new arXiv
identifier or accessible proof was obtained. This repeats the earlier
unverified lead; it does not establish a complete solution here.

The primary papers actually opened were Christopher Hoffman, Tobias Johnson
and Matthew Junge, [Recurrence and transience for the frog model on trees](https://arxiv.org/abs/1404.6238),
and Poly Mathews Jr, [Improved critical drift estimates for the frog model
on trees](https://arxiv.org/html/2309.14443v2). Their stated results do not
settle the two cases. The inaccessible later claim remains a separate
uncertainty.

Next worker: first try to obtain and inspect the reported outside paper and
its model definitions. If it cannot be verified, the four-type matrix is an
exact starting point. The next distinct refinement is to retain the
three-frog packet after two frogs hit the same sleeping child, rather than
split it into D+F. It may improve the bound; no estimate or claim at q=1
has been established for that refinement.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 01:32 Asia/Tbilisi.
