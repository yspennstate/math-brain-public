# Independent reconstruction: A059 whole-subformula obstruction

Source: A059 run 20261011T224320Z-account05-A059-decomposition-depth,
PROOF.md sections 3--4 and REPORT.md, read-only. Review applies to the
rare-switch counterfamily and its exact H/I formulas; it does not claim
independent acceptance of every subclaim in A059's bundle.

Verdict: HOLDS at stated scope. I reconstructed the actual spectrum by
partitioning Fourier sets into the old-data and fresh-y sectors, rather
than relying on a generic tree identity. The independently written checker
uses direct truth tables followed by integer FWHT and Fraction probabilities.
For six (r,d) tables it checks exact H, I, singleton coefficients and the
additional aggregate B formula as rational prime-log identities. Formula
dimensions stay at most 7. No floating entropy arithmetic is used.

For all k>=2, d=2^(2k), p=2^-3k, the dominant singleton contributes
2tp q^(2t), and its ancestor weight q^(d-t) yields at least 2tp q^(2d).
Sum t=1,...,d-1 and use Bernoulli q^(2d)>=1-2dp>=1/2 to get
D>=2^(k-1)(1-2^-2k). Independently I<=1+3k2^-k<=5/2;
3k2^-k decreases for k>=2 because its successive ratio is (k+1)/(2k)<1.
This establishes the divergent bank/I on genuine Boolean functions for
all k, independently of finite enumeration. Q_r<=6rp verifies the
depth-uniform actual entropy payment and excludes interpreting the bank
as an FEI disproof. These steps coincide with A059's conclusion and need
no substantive repair to its claim. No contribution to A059's version
is made by this review.

The informal lead's use of the same epsilon for p and rp is clarified in
my own PROOF.md; A059's explicit p,r,d formulas already distinguish them.
Independent new-script output: out/validation.json, 792 assertions PASS,
1.7083 seconds across the full frozen domain, including selector tests.
The present review is local; no shared claim registry was edited.
