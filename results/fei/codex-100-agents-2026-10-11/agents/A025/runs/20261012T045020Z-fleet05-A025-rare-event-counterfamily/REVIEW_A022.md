# A025 scoped independent reconstruction of A022 v1

Source: A022-ODDFACE-SURGERY-GAP-LEDGER v1, run
20261011T234607Z-fleet05-A022-one-point-surgery, ODDFACE_GAP.tex paragraph
"Constant-child control queries are uniformly good".

Verdict: HOLDS FOR THIS SUBCLAIM ONLY. For a fair actual Boolean split with
one constant child, B/d<=2+log2(e)/sqrt(e)<3 when d>0. All point-activation
controls queried before the core therefore have no threshold-4 bad-node
credit. The complete active core ledger is retained with its correct 2^-r
physical weight.

Independent reconstruction: use the parent sign spectrum directly, not a
model for packet means. At residual nonempty T, the constant child has
coefficient zero, so the two parent masses are both hhat(T)^2/4. Their
binary entropy contribution sums to (1-(Eh)^2)/2=2d(1-d). The remaining
empty pair has masses d^2,(1-d)^2. Bounding its entropy by
d^2 log2(e/d^2), then dividing by d, gives
2+d(log2(e)-2)+2d log2(1/d). Its derivative vanishes at 1/(2sqrt(e)), where
the nonconstant term is log2(e)/sqrt(e). The strict comparison with 1 follows
from ln2>2/3 and e>5/2, proved by their positive series. Endpoints are handled
directly. This reproduces the source bound without repairing it or changing
its hypotheses. No acceptance of its multiple-flip census, all-r descendant
limit, or full bundled claim is inferred from this subclaim review.

The all-depth tower proof in PROOF.md independently includes this argument;
the tower result itself remains pending review by A087/A094. This note is
saved for supervisor adoption only. A022 and shared registry files were not
changed; no receipt is claimed as downstream use.
