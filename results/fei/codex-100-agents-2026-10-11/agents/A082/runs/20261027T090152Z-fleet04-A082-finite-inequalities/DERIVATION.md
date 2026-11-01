# Root certificate and the distinction between atoms and components

All entropies and complete cross-entropies use bits. Full FEI remains open.

## 1. Independent reconstruction of A096's specified family

Let n be even and at least 4, M=2^n, and let f be the product of n/2 disjoint AND2 signs. Each factor has four Walsh coefficients of magnitude 1/2, so P(S)=1/M, H(P)=n and I(f)=n/2. The supplied reference q=(P+delta_[n])/2 obeys q>=P/2 and hence CE(P,q)<=n+1<=(5/2)I. This is an explicitly supplied source for this family, not a universal supplier.

Vacuum calibration fixes mass 1/M at the empty set. The subsequent minimum-KL cardinality projection has, for its parameter x>0,

 Z(x)=(1+x)^n-1+M x^n,
 u(empty)=1/M,
 u(S)=(M-1)x^|S|/(M Z(x)) for 0<|S|<n,
 u([n])=(M-1)(M+1)x^n/(M Z(x)).

The required conditional mean is mu=nM/[2(M-1)]. The equation x Z'(x)/Z(x)=mu is equivalent to x F_n(x)=0, where the integer polynomial

 F_n(x)=sum_(j=1)^n binom(n,j) c_j [2(M-1)j-nM] x^(j-1),
 c_j=1 for j<n and c_n=M+1.

All denominators are positive at x>0. Differentiating the finite conditional mean with respect to log x gives its variance, strictly positive since levels 1 and n both have positive mass. Thus the conditional mean is strictly increasing; there is no sum/limit interchange. The integer coefficient signs are negative through j=n/2 and positive thereafter. This sign pattern is checked independently but no unproved root-count theorem is needed.

Here is a simpler exact bracket than the original 1/(M+1)<x<1. At x=1/2, Z=(3/2)^n and

 mu(1/2)/n=1/3+(2/3)^n.

For n=4, the target divided by n is 8/15, and 8/15-43/81=1/405>0. For every even n>=6, (2/3)^n<=64/729<1/6, whereas M/[2(M-1)]>1/2. At x=1 the mean divided by n is 3M/[2(2M-1)], larger than M/[2(M-1)] because M>2. Continuity and strict monotonicity give the UNIQUE root

                         1/2 < x < 1.                 (1)

This implies (M+1)x>1 immediately. For this x the minimum u(S)/P(S) over intermediate levels occurs exactly at |S|=n-1; the full-set ratio exceeds it by factor (M+1)x>1. The intermediate minimum is strictly below 1: otherwise all ratios, including the vacuum ratio 1 and a strictly larger full ratio, would be at least 1, contradicting normalization. Hence precisely n atoms attain the global minimum b*. Any representation u=bP+sum a_W delta_W with b>0 and a_W>=0 has b<=b*. If b<b*, every one of M residual atoms is positive. At b=b*, exactly M-n are positive. Thus k_min=M-n, independently confirming A096's count. At n=2 the root is 1/5 and u=P, so k_min=0; the strict n>=4 hypothesis is essential.

The free projection debit also reconstructs: log(u/q_vac) is affine in |S| on nonempty atoms and constant on the vacuum. Matching the two moments makes E_P log(u/q_vac)=E_u log(u/q_vac). Therefore CE(P,su)-CE(P,sq_vac)=-D(u||q_vac), with the SAME scalar -log s retained. At general finite-law boundary means, the support is restricted to the extreme cardinality carrying P, so the same finite sum identity holds. No root price is created.

## 2. A nonnegative three-component description

Define B^+_(n,x)(S)=x^|S|/((1+x)^n-1) on nonempty subsets and zero at the vacuum. For EVERY real x>0, not just the root, the displayed u satisfies

 u = a delta_empty + b B^+_(n,x) + c delta_[n],
 a=1/M,
 b=(M-1)((1+x)^n-1)/(M Z(x)),
 c=(M-1)x^n/Z(x).

All three coefficients are strictly positive and sum to one. Direct substitution checks every atom, including the full-set extra factor M+1. Thus exponential individual-atom count does not imply exponential number of components in this richer class. This is a narrow compression statement, not an entropy estimate.

Delete any k coordinates and let d=n-k>0. The pushforward of B^+_(n,x) is

 alpha delta_empty + beta B^+_(d,x),
 alpha=((1+x)^k-1)/((1+x)^n-1),
 beta=(1+x)^k((1+x)^d-1)/((1+x)^n-1).

Indeed the retained empty fiber excludes only the original all-empty configuration; each nonempty retained subset has the full deleted weight (1+x)^k. Both coefficients are nonnegative, beta>0, and alpha+beta=1 by the polynomial identity (A-1)+A(B-1)=AB-1. The complete u therefore pushes forward to (a+b alpha)delta_empty+(b beta)B^+_(d,x)+c delta_[d]. Deleting all coordinates gives delta_empty. The result holds for every chosen deleted coordinate set, by permutation invariance, and for every finite sequence of deletions by composition.

EXHAUSTIVENESS THEOREM. The binomial theorem reduces every member of this specified all-dimensional family to the exact one-variable polynomial and finite sums above. Equation (1) is proved for ALL even n>=4; the compression identity is atomwise for ALL real x>0 and ALL coordinate subsets. These analytic identities, not the finite n<=32 and rational-x tests, make the finite domain exhaustive for the intended family and deletion operation. Arbitrary Boolean cores or full physical branches are not in that finite exhaustive domain.

## 3. The first unsupported bridge is physical branch transport

Coordinate deletion of a spectral reference is not a full physical restriction. For a physical query, child amplitudes are fhat(T)+fhat(T+i) and fhat(T)-fhat(T+i); their squares depend on phase and cross terms. Already on AND2, P is uniform on four frequencies and its coordinate deletion is uniform on two frequencies. The actual two children have spectral laws delta_empty and delta_singleton, respectively. This exact Boolean negative control rules out replacing full physical transport by the deletion formula, even on the smallest tensor seed.

No claim is made that every branch-specific transport leaves the three-component class, or that a richer compressed class is impossible. Such a class must carry the actual outcome likelihoods, phase-sensitive true component, ghost mass, old debits and both full terminal bills. The present formulas price no new source, refresh no allowance and establish no required stopping condition.

## 4. Scope and verification rung

A096's free moment-projection and sharp atom-count arguments reconstruct at their stated supplied-source scope, without a mathematical repair. The stronger bracket (1) simplifies its root certificate. The three-component/deletion identities have an elementary proof and exact finite checks; independent review is pending. No Lean check of the complete mathematical theorem is claimed. An algebraic Lean target is saved separately, with admission status recorded. Universal FEI improvement is zero.
