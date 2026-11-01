# A unique-intermediate rule for composing projection channels

Root creative construction, 2026-09-15. This note proves the composition identity below. C034 and C035 are now complete, so the composition consequences below apply to their proved coupling formulas. It does not settle arbitrary projection flags or Lyons concavity.

Let Q1,Q2 be unitaries supported on coordinate sets A,B respectively, and suppose |A intersection B|<=1. Thus each acts as the identity outside its support. Define the occupation channel W_Q(S,T)=|det Q[S,T]|^2 for |S|=|T| and zero otherwise. Then

    W_(Q2 Q1) = W_Q2 W_Q1.

Proof: Cauchy-Binet expands det(Q2Q1)[S,T] as sum_R detQ2[S,R] detQ1[R,T]. A nonzero first factor forces R outside B to equal S outside B. A nonzero second factor forces R outside A to equal T outside A. These determine every coordinate of R except possibly the unique coordinate in A intersection B. The constraint |R|=|T| determines that last coordinate as well. There is consequently at most one nonzero intermediate term. Squaring its absolute value produces exactly the classical channel composition. Inconsistent boundary coordinates or cardinality produce zero on both sides.

By induction the rule applies to a sequence of coordinate-supported unitaries whenever each new support meets the UNION of preceding supports in at most one coordinate. These form a tree of overlapping coordinate sets. General products with larger overlaps have interference terms and are not covered.

Consequences:

1. If each factor has a common random-permutation realization W_Qj(S,T)=Pr(pi_j(T)=S) for ALL subsets T, their product has the realization pi_m ... pi_1. Applying that one random permutation to a coordinate Boolean diamond supplies a simultaneous labeled projection diamond for every coordinate flag.
2. More generally, suppose each factor has an unlabeled diamond transport for every coordinate diamond (X,X+i,X+j,X+i+j). Apply a factor's transport conditionally to each current elementary diamond. Bottom and top distributions are pushed by W_Qj; the sum of the two middle marginals is pushed by that SAME linear channel. Hence iteration preserves the correct unlabeled aggregate. The unique-intermediate identity identifies the result with physical projection marginals for the product unitary. No common labeling of the two middle marginals is needed for this unlabeled consequence.

C034 proves the stronger simultaneous permutation realization for single rank-one phase rotations with gamma<=3. C035 proves unlabeled transports for all gamma<=4, including Householder reflections. Their explicit formulas and this rule extend those constructions to arbitrarily large overlapping-support unitary products. A useful follow-up is an explicit genuinely complex multiphase example, complete coupling probabilities, and exact certificates showing scope beyond a single rank-one unitary perturbation.
