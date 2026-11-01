# Exact uniform phase admission

All Fourier labels are elements of F_2^n, encoded by integer masks. Physical x uses the same bit order and chi_s(x)=(-1)^(s dot x). Entropy is in bits; influence is expected label Hamming weight.

## General finite interface

For an exact rational law p on 2^n labelled atoms, Boolean realizability means there are real signs epsilon_s with f(x)=sum_s epsilon_s sqrt(p_s) chi_s(x) in {+1,-1} for every x. If f is Boolean, W_s=2^n fhat(s) is an integer. Thus N^2 p_s must be an integer square. For n>=1 every W_s is even. For n>=2 every W_s is congruent modulo4: write f=1-2 1_D, so W_s=N 1_{s=0}-2 sum_{x in D}chi_s(x), and the last sum has parity |D|. Absolute values preserve residues0 and2. The common-mod4 condition does NOT apply at n=1; the pilot caught and corrected this endpoint implementation error before the full run.

Given magnitudes a_s=|W_s|, every nonzero u requires sum_{s<t,s xor t=u} epsilon_s epsilon_t a_s a_t=0. A necessary condition is an exact partition of these positive pair products into two equal sums. A subset-sum failure is an impossibility certificate irrespective of other equations. Passing these separate partitions is not asserted sufficient: pair signs must come from one common vector epsilon.

Otherwise enumerate all 2^(k-1) phases, fixing the first supported coefficient positive. Global negation preserves realizability, so this loses no case. The unnormalized Walsh transform of the signed integers must have every value exactly +/-N. A successful certificate supplies the full truth table and integer forward transform. Failure after the complete domain is exact impossibility. If the declared support budget is exceeded, the interface returns INCONCLUSIVE. Rational probabilities with irrational square roots are rigorously impossible on a uniform finite cube, not numerically rejected. This interface does not apply to product-biased transforms, whose coefficients may be irrational even for Boolean functions.

## All-dimensional support at most four

For every n and law p with at most four positive labelled masses, p is Boolean-realizable iff either (i) it is a singleton of mass1, or (ii) its support is an affine plane {t,t+u,t+v,t+u+v}, with u,v independent, and all four masses are1/4.

Proof. Two or three distinct supported labels have a unique pair in at least one nonzero XOR equation, yielding a nonzero convolution coefficient of f^2, impossible. Four distinct labels not having total XOR zero have all pair differences unique: two pairs sharing a label cannot have equal difference, and equality of disjoint pair differences would give total XOR zero. Hence they too are impossible. If total XOR is zero, put the four nonzero signed coefficients a,b,c,d in affine-plane order. The three equations are ab+cd=0, ac+bd=0, ad+bc=0. Dividing the first two gives b/c=c/b, hence b^2=c^2; the other divisions give equality of all four squared magnitudes. Parseval forces each square to1/4, and abcd<0. Conversely any four signs with product-1 satisfy all three equations and Parseval, hence f^2=1 at every physical input. One explicit polynomial is chi_t(1+chi_u+chi_v-chi_{u+v})/2. The singleton case is a signed character. This proof is independent of arithmetic granularity.

## Uniform law on any affine subspace

Let A=t+V in F_2^n have affine dimension r, and set p_s=2^(-r) on A and0 elsewhere. This law is Boolean-realizable iff r is even, including r=0. For odd r the coefficient magnitude2^(-r/2) is irrational, contradicting rational Walsh coefficients. For r=2m choose a basis v_1,...,v_r of V and let y_j=v_j dot x. Define f(x)=chi_t(x)(-1)^(y_1 y_2+...+y_{r-1} y_r). The rank-r map x->y is surjective and uniform. For one pair, the transform of (-1)^(ab) is (1,1,1,-1)/2, verified by its four values. Tensoring the pairs gives all2^r coefficients of magnitude2^(-r/2) on V; multiplying by chi_t shifts to A. This is an actual truth-table formula in every dimension. No novelty is claimed for the bent-function construction or rationality obstruction.

For this class H=r<=2D<=2I. Indeed each physical-coordinate projection of V is either zero (a deterministic spectral bit) or nonzero (a fair bit). Let q be the number of nonzero projections. Then D=sum_i min(Inf_i,1-Inf_i)=q/2, and q>=r since an injective rank-r matrix needs at least r nonzero rows. Thus H=r<=q=2D. Equality occurs on a coordinate r-face. This extends the coordinate-face classification already recorded in sources/ERASURE_RIGIDITY.md; it is a class bound, not a universal payment theorem.

## Affine-dimension reduction

For arbitrary p supported on t+V, remove chi_t and identify V with F_2^r using a basis. The inverse polynomial becomes g(y), and surjectivity of x->y proves: a phase realizes p on the original cube iff it realizes the relabelled law on the r-cube. The requirement that every coefficient of a Boolean r-variable function is an integer multiple of2^(-r) follows as well, even if the ambient n is much larger. This permits finite certificates to cover every ambient embedding of a fixed labelled support geometry. Basis changes preserve realizability and entropy, but need not preserve physical influence; no such influence invariance is used.
