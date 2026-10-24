# C0062: an infinite counterexample family for the naive top-corner move

2026-10-10. Label: proof awaiting w346 KEEP. This refutes a proof route; it does not refute uniqueness up to conjugation or solve the finite-n maximization problem.

The earlier memo found (6,5,1,1) -> (5,5,1,1,1), dimensions 5720 -> 5005. It also already enumerated n<=90 and cited prior exhaustive computations beyond that. Repeating n<=40 would add no result.

Let lambda=(a,a-1,1^b), a>=2, b>=0. Move the top-right box to a new bottom row, giving mu=(a-1,a-1,1^{b+1}). Both have 2a+b-1 boxes. Direct hook products are

    H(lambda)=(a+b+1)(a+b-1) a! (a-2)! b! / 2,
    H(mu)=(a+b+1)(a+b) (a-1)! (a-2)! (b+1)!.

The row-1 hooks outside column 1 in lambda contribute a!/2; row 2 contributes (a-2)!; the b singleton rows contribute b!. For mu the analogous factors are (a-1)!, (a-2)! and (b+1)!. The first two column-1 hooks are displayed above. The hook-length formula therefore yields

    dim(mu)/dim(lambda)=a(a+b-1)/(2(a+b)(b+1)).

Set a=b+4 and b>=2. The original diagram has width minus number of rows exactly 2, yet the ratio is

    (b+4)(2b+3)/(2(2b+4)(b+1)) < 1,

because denominator minus numerator is 2b^2+b-4>0. The ratio tends to 1/2. Thus there are infinitely many counterexamples to the proposed rule that moving the top-right corner to a new row increases dimension whenever width exceeds height by at least two. The first is the previously observed n=13 example; new family sizes are n=3b+7.

This says nothing about a different corner move, a sequence of moves, or whether lambda itself is a maximizer. The stronger rule 'some corner to some outer corner improves dimension' survives this example and stays a conjectural route.

Checks: compute each hook product independently from its cell definition, compare exact rational ratios for b=2..100, and check the n=13 dimensions against the old memo. Include small a=2 and b=0 boundary cases to detect missing singleton factors.
