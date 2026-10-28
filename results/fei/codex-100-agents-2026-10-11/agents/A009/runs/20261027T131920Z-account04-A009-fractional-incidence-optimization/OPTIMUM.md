# An exact all-weight, all-mixture certificate on a physical cycle

This is an optimization theorem for one explicitly fixed reference class, not a new FEI class result. Its point is that public mixing is strictly useful, even after optimizing every physical gate weight. The same physical Boolean test has a different optimum in A006's explicitly different fifteen-run forest subreference.

Use the three physical supports {1,2},{1,3},{2,3}. The Boolean function is 2[(x1 OR x2)(x1 OR x3)(x2 OR x3)]-1, majority on the zero/one cube, interpreted as a sign function. Its squared Walsh law gives mass1/4 to each singleton and to {1,2,3}; the other masses vanish, and I=3/2. All costs are bits.

Choose activations a,b,c>=0, a+b<=1,a+c<=1,b+c<=1, rho=a+b+c>0. Draw an actual anchor with prior alpha_j/rho, force its local mask uniform among the three nonempty edge subsets, and draw every other support empty with probability1-alpha_j or each particular nonempty mask with probability alpha_j/3. Output their physical UNION. Its full normalized output law is

    Q_alpha(A)=rho^(-1) sum_(union u=A) K(u) mu_alpha(u).

All actual anchor and local-draw events are retained. Every reference and any public mixing distribution are fixed before the spectral output is sampled. The parameter domain includes zero activations when rho>0. If strictly positive activations are required, take closure; statements about infima persist.

## Exact optimum

Over ALL incidence-feasible weights and ALL fixed public probability mixtures of these references, the exact infimum is

    C_* = 3/2 + (3/4)log2 3.

It is attained by the fixed mixture: weight3/8 on alpha=(1/2,1/2,1/2), and weight5/24 on each of alpha=(1,0,0),(0,1,0),(0,0,1). The resulting FULL output law is

    Q_*(each singleton)=1/6,
    Q_*(each pair)=1/8,   Q_*(triple)=1/8.

The four public branch probabilities and the entire allocation posterior are included. The optimum is strictly larger than H(f)=2, by (3/4)log2 3-1/2>0. No single feasible activation vector attains this mixed optimum; in fact its single-reference infimum is strictly larger. No claim concerns other dictionaries or the original-prime queue.

## Full mass calculation

Put s1=a+b+c, s2=ab+ac+bc, s3=abc. Write S for the TOTAL singleton output mass and T for triple mass. For vertex1 with incident weights a,b and nonincident weight c, its occupation numerator is

    [(a+b)/3-4ab/9](1-c).

Sum over the three vertices to obtain

    S=2/3-10s2/(9s1)+4s3/(3s1).

For each two-vertex set, compute the occupation of tuples contained in it (not just exactly equal to it). Inclusion-exclusion over these three sets and the three singleton sets gives

    T=2s2/(3s1).

Both formulas sum the ENTIRE actual output events. They are not selected-witness lower bounds. The remaining pair probabilities remain in the normalized reference even though their target Fourier mass is zero.

## Exact score certificate on the continuous polytope

The logarithmic tangent inequality for any reference Q gives

    C(Q)-C(Q_*) >= [1-sum_A p(A)Q(A)/Q_*(A)]/ln2.

For the present full law the score is

    (3/2)S+2T = 1-(s2-6s3)/(3s1).

It is at most1 throughout the incidence polytope. Here is a proof retaining all denominators and equality cases. Adding the three pair caps yields s1<=3/2. The square identities give

    s2<=s1^2/3<=s1/2,
    s2^2-3s1s3 = [(ab-ac)^2+(ab-bc)^2+(ac-bc)^2]/2>=0.

Thus 3s1s3<=s2^2<=s1s2/2. Since s1>0, divide to get 6s3<=s2. Averaging the score inequality over ANY public probability law preserves it, because there are only seven output coordinates. The tangent lower bound therefore certifies Q_* globally optimal over that entire class, not just a sampled list of mixtures. Its cost is (3/4)log2 6+(1/4)log2 8, the displayed value.

If s2=0, at most one activation is nonzero, and Q_alpha is the uniform nonempty mask law on that edge. If s2>0, equality s2=6s3 in the above chain forces s2=s1/2, equality in s2<=s1^2/3, and s1=3/2, hence a=b=c=1/2. These are ALL score-equality references. The logarithmic tangent is strictly unequal unless Q agrees with Q_* on every positive-target output. A single axis reference misses a singleton and the triple, while the half-vector reference has S=2/9,T=1/3. Neither agrees with Q_*. Therefore no single reference attains C_*.

There is also a strict infimum gap for single references. If s1 tends to zero, T=2s2/(3s1)<=2s1/9 tends to zero, so the positive target triple forces cost to infinity. Otherwise any sequence in the bounded closed feasible polytope has a subsequence with s1 bounded away from zero and a valid parameter limit. Finite output probabilities are continuous there; -log is lower semicontinuous including output zeros. A sequence with costs tending to C_* would consequently yield a single attaining reference, already ruled out. This compactness argument does NOT claim an explicit numeric size for the single-reference gap.

For an optimal public mixture, zero expected score deficit requires it be supported on the axis laws and half-vector. Triple mass fixes the half-vector branch weight3/8. The three singleton equations then force each axis-law total weight5/24. Thus the optimal output law and branch totals are unique (activation magnitude along an axis has no effect). For a strict-positive-only parameter domain these endpoint branches are limits, so the same mixed infimum need not be attained inside that open domain.

## What this resolves and what it does not

The unconstrained full-output relaxation has optimum H=2. The best actual mixed anchor law has a certified positive gap, while mixing itself improves strictly over every single activation vector. Thus neither setting the feasible reference equal to the target Fourier law nor omitting public mixtures is a sound shortcut to this optimization problem. This is the same score certificate interface as A006's, applied to a DIFFERENT complete anchor generator; it does not contradict A006's different forest-subreference optimum.

The universal unpaid line is still an ORIGINAL influence-priced full reference for arbitrary growing-width, connected overlap. This finite cycle certifies the optimization and equality machinery and rules out two shortcuts. It is not a lower bound for other representations, an unbounded H/I family, or a full FEI proof.
