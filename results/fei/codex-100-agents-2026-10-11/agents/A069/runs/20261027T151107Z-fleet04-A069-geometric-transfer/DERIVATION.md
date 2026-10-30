# An original nonquadratic source with a rate-four reserve

All inputs and physical restrictions are uniform. Functions f and g in this note are ACTUAL Boolean signs. Entropy and reference costs use base-two logarithms. No geometric estimate is assumed, and no reference is reset at a physical descendant.

## 1. An abstract source-admission lemma

Let g:{-1,1}^n->{-1,1}, n>=1, be supplied with a checked bound

 H(g)<=4I(g)-4.                                             (1)

Write J=I(g). Since entropy is nonnegative, (1) implies J>=1. Define the ORIGINAL complete normalized reference

 R(S)=[ghat(S)^2+2^(-n)]/2.

It has positive mass at every Fourier set. This is one root mixture, including its full normalization cost; all descendants use only its frequency marginals. If f differs from g at a set E of uniform measure rho, suppose

 1024 n J rho<=1.                                          (2)

Then, writing C(f,R)=sum fhat(S)^2 log(1/R(S)),

 C(f,R)<=4I(f)-271/128.                                    (3)

Here g and its source are constructed independently of f's edited coefficients. This is a conditional abstract lemma, not an assertion that (1) holds for arbitrary Boolean g.

Proof. Let L(S)=log(1/R(S)) and Lmax=n+1; indeed R(S)>=2^(-n-1). Also

 C(g,R)<=H(g)+1<=4J-3=:B0,

and B0>=1. The difference h=f-g has squared norm4rho, since f and g are Boolean and differ only by sign. Weighted Parseval and the ordinary Euclidean triangle inequality give

 sqrt(C(f,R))<=sqrt(C(g,R))+sqrt(sum hhat(S)^2 L(S))
              <=sqrt(B0)+2sqrt(rho(n+1)).

Squaring nonnegative quantities and using B0<=4J and n+1<=2n yields

 C(f,R)<=4J-3+8sqrt(2nJrho)+8n rho.                       (4)

Using Fourier weights |S| instead gives sqrt(I(f))>=sqrt(J)-2sqrt(nrho). Its right side is positive under (2): 2sqrt(nrho)<=1/(16sqrt(J))<sqrt(J), since J>=1. Squaring is therefore legitimate and implies

 4I(f)>=4J-16sqrt(nJrho).                                 (5)

Put t=sqrt(nJrho)<=1/32. Subtract (4) from (5). Because sqrt(2)<3/2 and n rho<=1/(1024J)<=1/1024,

 4I(f)-C(f,R)>=3-(16+8sqrt(2))t-8n rho
              >=3-28/32-1/128=271/128.

Every denominator and square root above is on its stated positive range. All sums are finite. The proof works also at rho=0 without dividing by rho.

## 2. A growing nonquadratic clean source, derived directly

Let g_0(x)=x and let g_d be ternary recursive majority of three disjoint copies of g_(d-1), for every d>=1. Its physical dimension is n=3^d. These gates are balanced. The outer majority Fourier expansion has three singleton coefficients +1/2 and one triple coefficient -1/2, so its squared spectral law is uniform on four nonempty sets and has mean size3/2.

Sample the outer Fourier set, then independent child Fourier sets in its occupied blocks. Balanced children have no empty atom, so the union uniquely identifies both the occupied blocks and their child sets. Thus this is a true entropy identity, with no mixture ambiguity or overlap assumption omitted:

 J_d=(3/2)J_(d-1)=(3/2)^d,
 H_d=2+(3/2)H_(d-1)=4[(3/2)^d-1]=4J_d-4.                (6)

This proves (1) directly for every depth; no full-FEI premise is used. The spectral law P_g is given by the same explicit recursive sampler. Hence R=(P_g+uniform)/2 is an explicitly constructed original complete source. The class is genuinely beyond quadratic phases, and J_d/n=2^(-d) tends to zero, so it is not the elementary high-influence uniform-code case.

For EVERY edit set E, arbitrary geometry and arbitrary signs already determined by the Boolean g, of cardinality

 |E|<=floor[2^n/(1024 n (3/2)^d)],

the edited ACTUAL Boolean f=g_d*(-1)^(1_E) satisfies (3). At d3,n27 the integer allowance is1438 edits, not just a single point; the analytic theorem is for every arrangement of those edits. Larger depths allow exponentially many edits. The finite certificate checks all individual point locations up to exact physical symmetry; it is not an exhaustive check of every1438-point edit set.

## 3. Every stopping tree, the SAME original owner and both full terminals

At every physical node inherit R by frequency marginalization. If a queried fiber has actual Fourier coefficients a,b, the mean squared child coefficient is a^2+b^2. The full parent-to-mean-child CE decrement is

 D_i=sum_T [a^2 log((R_T+R_Ti)/R_T)+b^2 log((R_T+R_Ti)/R_Ti)]>=0.

All reference masses are positive. For any adaptive physical stopping tree, including a full exposure or a stop immediately at the root, with original reach weights w,

 sum_nodes w D_i + E C(full actual leaf,inherited R)=C(f,R).

Consequently its positive rate4 invoice satisfies

 sum_nodes w(D_i-4Inf_i)_+ + E C(full actual leaf,inherited R)
 <= C(f,R) <=4I(f)-271/128.                              (7)

This keeps BOTH child and full terminal costs. Choices may depend on the physical history or an initially independent seed; condition on that seed and average its original law. Irrelevant or constant-output continuations are not erased. No negative excess is re-spent. The reference is never reinstalled, normalized again, or replaced by a favorable child spectrum.

An already booked original debit U with0<=U<=2 may be added to the left side of (7) only if it is a distinct actual charge of this SAME original owner. Then the remaining original rate4 capacity is at least15/128. This is an algebraic admission guard, not permission to count source CE and its own telescoped charges twice. In particular, separately adding four times all queried influence is not included in (7).

## 4. Exact point-orbit certificates without a 2^27 truth table

A point of a depth-d ternary tree is classified up to sibling permutations by an unordered triple of child point-orbits. Starting from two signed leaves, orbit counts are2,4,20,1540 at depths0,1,2,3. Every point occurs in exactly one orbit under the rooted tree automorphism group; g and the original R are invariant under these physical permutations. We retain both global signs, so no additional sign quotient is assumed.

At a point x record, for each exponent a and evaluated coefficient sign s, the number N_(a,s) of Fourier terms with ghat(S)chi_S(x)=s*2^(-a) and the sum K_(a,s) of their degrees. Singleton outer terms add1 to a; the triple outer term adds1 to the sum of the child exponents and negates the product of the signs. Counts multiply; degree sums obey K12=K1*N2+N1*K2. This computes the complete coefficient multiplicities exactly, not sampled spectral data.

For the point-edited function multiply the evaluated coefficient by g(x), and put delta=2^(1-n). Its squared amplitude is (s*g(x)*2^(-a)-delta)^2. Missing clean coefficients acquire mass delta^2. Their count is2^n-sum N and their total degree is n2^(n-1)-sum K. The reference at a clean atom is2^(-2a-1)+2^(-n-1), and at a missing atom it is2^(-n-1). These formulas give complete exact normalization, influence and CE, including the newly created full spectral support.

Independently, if p(x) is the number of pivotal physical coordinates at x, the edited influence is

 I(f)=J_d+2^(1-n)[n-2p(x)].                              (8)

The checker compares this physical-edge formula with the full multiplicity spectrum; it also compares all depth<=2 point orbits with direct truth-table Walsh transforms. Rational logarithm intervals certify all numerical CE inequalities. The all-depth/multi-edit theorem is the analytic proof in Sections1-3, not extrapolation from these point cases.

## 5. Honest universal boundary

This supplies a nonquadratic ORIGINAL source at unchanged rate4 for a broad growing edit neighborhood, not for an arbitrary indecomposable core. It consumes the earlier real-function guard rather than weakening Booleanity. The first unsupported universal line remains: find a noncircular clean original source with sufficient influence-paid slack for every Boolean core, or a genuinely decreasing decomposition that reaches such a source and pays its required conversion from the SAME depleted owner. Choosing R=P_f and assuming its entropy is paid would simply assume FEI. The clean recursive sampler here avoids that circularity only for its stated class.

The coefficient4 is class-specific. A universal original source, if constructed, may use a larger finite absolute rate K declared before booking its charges; no universal H<=4I or universal clean4J-4 hypothesis is asserted.
