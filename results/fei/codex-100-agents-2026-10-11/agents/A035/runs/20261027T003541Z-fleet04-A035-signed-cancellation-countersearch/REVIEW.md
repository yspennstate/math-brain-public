# A031 quantitative fine tariff: HOLDS at its stated scope

This independently reconstructs A031-QUANTITATIVE-FINE-COMPATIBILITY-TARIFF@1,
statement hash 16d20ef754c45209dbbb3faad9803f99fdadebe89f89fad0a50d640a2b2b0094.
No repair or new hypothesis is needed. The result is generic finite probability
geometry. It supplies neither Boolean admission nor a necessary reference policy.

Let p_tau be the two complete child laws, m a complete inherited mean, and
r_tau(z) the prescribed profiles on a finite partition, averaging to m(z).
Assume p_tau << m and finite coarse KL. Write a_tau=p_tau(z), and, only on
occupied blocks, k_tau=p_tau/a_tau. All logarithms in this proof are natural;
the source's M and L are in bits, accounting for its factor ln(2).

For a feasible pair R_tau of the given profiles and mean m, subtract the
coarse divergence by the conditional KL chain rule. The excess is exactly
(1/2) sum_(tau,z occupied) a_tau D(k_tau || R_tau/r_tau).
Finite coarse KL ensures r_tau>0 on each such term. A block of m-mass zero
has no actual mass and no contribution; no denominator is canceled there.

Pinsker in natural units bounds this excess below by
(1/4) sum a_tau ||E_tau||_1^2/r_tau^2, where
E_tau=R_tau-r_tau k_tau. One independent derivation of Pinsker groups the
positive part of k-q by log-sum. Binary divergence has second derivative
1/[t(1-t)] >=4; integrating twice from its minimum proves D>=2 TV^2.
Endpoints follow by continuity or infinite divergence. This applies to any
finite complete law, with no Boolean or strict-support hypothesis hidden.

On a doubly occupied block put e=r_+k_+ + r_-k_- -2m,
W=r_+^2/a_+ + r_-^2/a_-. Pointwise compatibility gives E_++E_-=-e.
Set X=||E_+||_1, Y=||E_-||_1, A=a_+/r_+^2, B=a_-/r_-^2.
The sign-safe triangle step is ||e||_1<=X+Y, taken AFTER forming the actual
signed children and the reference errors. Its weighted sequel is certified by

 (1/A+1/B)(A X^2+B Y^2)-(X+Y)^2
       =(sqrt(A/B)X-sqrt(B/A)Y)^2 >=0.

The implementation avoids square roots: its identical cleared rational
numerator is (a_+ r_-^2 X-a_- r_+^2 Y)^2, divided by the strictly positive
a_+ a_- r_+^2 r_-^2. Thus the block contributes at least ||e||_1^2/(4W).
Cancellation is used as a LOWER bound; no reverse triangle inequality is used.

On a singly occupied block, feasibility forces R_tau(i)<=2m(i), including
all reference-only atoms. Put o=sum_i(r_tau k_tau(i)-2m(i))_+.
At least o mass must be removed from the ideal occupied reference. Since
E_tau has zero block sum, its L1 norm is at least 2o. Its contribution is
therefore at least a_tau o^2/r_tau^2. Empty actual blocks contribute zero.
Summing proves A031's exact Phi. The bound holds for every feasible pair,
so it also holds for the infimum M; existence is not required for this step.

Existence and the equality-set statement also check: the pair
R_tau(i)=r_tau(z)m(i)/m(z) on positive-mass blocks is feasible and finite.
The feasible polytope is compact, and extended KL is lower semicontinuous.
When all tests vanish, occupied references can equal r_tau k_tau and ghost
references fill the nonnegative remainders. Otherwise a positive Phi gives
strict excess. Both occupied signs, a single occupied sign, both-empty
blocks, reference-only labels, and zero-mass inherited blocks are covered.

For sharpness, h on two bits with one negative truth value has four Fourier
squares 1/4, as direct character sums verify. For f=x h the physical children
have identical spectral law p=uniform4 and Inf_x=1. One block forces profiles
1. For m=((1+2s)/4,(1+2s)/4,(1-2s)/4,(1-2s)/4), 0<s<1/2,
convexity in the reference makes R_+=R_-=m a global optimizer. Directly,
M ln2=-ln(1-4s^2)/2 and Phi=2s^2. The integral bounds
z<=-ln(1-z)<=z/(1-z) prove the limiting ratio is 1. The claimed constant
is optimal under general inherited means, even for positive-influence Boolean
queries. This does not establish sharpness at the actual midpoint.

For the complete transaction, let P be the parent squared spectrum, Q its
incoming reference, a the actual collapsed marginal and m the Q marginal.
The entropy restriction identity and both KL chains give the EXACT identity

 B_i + mean CE(p_tau,R_tau)-CE(P,Q)
       =mean KL(p_tau||R_tau)-JS(p_+,p_-)-KL(P||Q)
       =mean KL(p_tau||R_tau)-JS-KL(a||m)-rho.

Here rho is the actual conditional queried-frequency KL. Substitution of the
tariff yields the source's necessary reached-tree test, with all negative
credits retained and every complete terminal charged. In the sharpness
witness, rho=JS=0 and KL(a||m)=M: the FULL increment is exactly zero.
Positive Phi alone is consequently not an unpaid physical query.

Checks that could fail were: a missing fair-averaging factor; invalid triangle
direction; a vanishing occupied denominator; loss of ghost capacity; changing
signs before taking child squares; and omission of old KL or JS. The rational
checker tests each of these where applicable. It enumerates all 256 labelled
three-bit functions, all 15 partitions, three explicit reference pairs and
checks prime-log transaction identities exactly. Additional point defects,
tensor defects and bent point surgery use direct character sums at fixed
dimensions up to six. Finite checks support the reconstruction; the argument
above establishes the stated finite-law theorem in every dimension.

Rung: independent mathematical proof reconstruction with exact finite
certificates; not Lean-checked. The core integer Cauchy formalization returned
RUNTIME_UNVERIFIED after 47.091 seconds with no verified target or axiom set.
The theorem's truth is not inferred from that attempt, and no retry is needed
for this review. The first unsupported universal step remains a useful
required admissible class and its same-original influence-priced supplier.
