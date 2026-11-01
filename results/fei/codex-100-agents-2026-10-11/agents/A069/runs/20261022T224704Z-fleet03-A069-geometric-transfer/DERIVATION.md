# Stage7: retain the whole signed core bank

Working record. Certificate status is recorded separately; full FEI is OPEN.

## 1. Independent reconstruction of A070's single flag

Take arbitrary Boolean cores (a,b,-b,-a) indexed c+2u, m>=1,
rho=2^-m, t=rho^2, F=q2G with q2 negative on c=0,Z=0. Let
D=1{a(Y)!=b(Y)}. One independent E~Bernoulli(t), fixed for the whole
auxiliary experiment, gives W=ED. At an actual physical core transcript v,
Pr(W=1|v)=t d_v. For every finite adaptive core-only stopping tree,
the sum of physical node probabilities times the flag Jensen-Shannon
decrement equals I(W;L), with L the final transcript. Including E in the
observation gives I(W;L)<=I(E,ED;L)=t I(D;L)<=t h2(d_root).
The independence is of E from the whole physical input/transcript; the
physical transcript may adapt to its own revealed inputs. No new E is
sampled at a child, and no Fourier-dependent stopping is allowed.
All terminal flags remain in the chain rule. Thus A070's depth-free flag
statement is correct at its stated scope. Its fixed-core >9/4 corollary
also follows from the independently reconstructed source slack and >1
terminal bounds, without supplying a repair.

## 2. Same-constant complete reference transfer

Write A=(I(a)+I(b))/2, B=(C_R(a)+C_R(b))/2 for ONE positive normalized
common core reference R. The complete five-cell reference Q is unchanged:
singleton weights 1/4,1/4,1/16 and flat tail weights 7/20,7/80;
only the actual empty/nonempty flag prior changes under restriction.
Let L=log2(20/7) and beta=2rho(1-rho). Direct partial Parseval gives

 C_Q(F)=B+h2(td)+2+2(1-2d)rho+beta[m+log2(1-rho)+L],
 I(F)=A+1+(m+1-2d)rho,       d=Pr(a!=b).               (1)

Set s(d)=4[1+(m+1-2d)rho]-[C_Q(F)-B]. At d=0,1,
this is the actual complete terminal control surplus after all Y inputs
are fixed. Both endpoints exceed1 for every m>=1: m=1,2 by exact log
certificates and m>=3 by s(d)>=1+4rho/5>1. Since all nonflag terms are
affine in d,

 s(d)=(1-d)s(0)+d s(1)-[h2(td)-d h2(t)]
      >1-t h2(d)>=1-t>=3/4.                           (2)

Thus for arbitrary a,b and arbitrary supplied common R, with no depth bound,

 C_Q(F)<B+4 I_controls(F)-3/4.                         (3)

If the supplied core bank satisfies B<=K A, K>=0, then
 H(F)<=C_Q(F)<max(K,4) I(F)-3/4.                       (4)
The K+2 core tax of the arbitrary-four-core estimate is absent under this
paired zero-sum structure. This is a conditional reference-transfer theorem,
not an existence theorem for a universally paid common R. For a=b arbitrary,
the hypothesis can contain the original FEI problem; it cannot be dropped.

## 3. Exact stopped signed ledger, without a new child bank

At a physical core query set e_v=Delta B_v-K j_v, j_v=Inf_i(F_v),
and J_v=h2(t d_v)-E h2(t d_child). Let sigma_v=K A_v-B_v,
and s_v=4 I_controls(F_v)-(C_v-B_v), the two explicit accounts.
The core bank obeys sigma_v=E sigma_child-e_v. The control bank obeys
s_v=E s_child-J_v. Therefore, on every physical stopping tree,

 sigma_root+s_root=E(sigma_leaf+s_leaf)-sum_v p_v(e_v+J_v). (5)

All full actual terminal costs remain in B_leaf+C_leaf-B_leaf. A negative
sigma_leaf is retained as a signed debt; equation(4) does NOT assert every
inherited child is separately paid. Equation(5) alone is not universal
payment. A particular history must bound its positive core excess from
an explicitly unused original source/child/terminal bank, or use justified
signed cancellation. The nine-bit point-edit experiment below targets that
remaining cumulative positive term, rather than repeating the flag proof.

## 4. Boundary and hypothesis audit

m=0 is excluded because the five nonempty-Z cells collapse. For m>=1,
rho and 1-rho are nonzero. d=0 and1 use 0 log0=0, with no division by d.
The reference has support on every positive actual atom; zero flag priors
only occur on zero-mass flags. All sums are finite. Booleanity supplies
(a-b)^2/4=1{a!=b}; arbitrary normalized real cores do not satisfy this.
Arbitrary four Boolean cores do not have the paired zero-sum structure.
An arbitrary inherited reference need not satisfy B<=K A, even when
the individual core entropies satisfy separate FEI inequalities.

The universal first unsupported line is a dimension-independent, once-owned
payment of cumulative positive core-reference excess for arbitrary actual
cores/history under a justified supplied common reference. The all-depth
flag and conditional same-constant transfer do not establish that line.

## 5. Nine-bit unequal-amplitude history: one fixed actual child owner

Let a=Maj3(Maj3(Y0,Y1,Y2),Maj3(Y3,Y4,Y5),Maj3(Y6,Y7,Y8)) and let b
be a with only its all-zero truth-table value flipped. For every frequency
S, set L(S)=1+3[1{S nonempty}+sum_{j=0,3,6}1{S meets block j..j+2}].
The normalized all-set reference is R(S)=2^-L(S)/Z, Z=6959/8192.
Its cells form the original complete ternary refinement hierarchy, and
its Kraft sum is computed exactly over all512 frequencies. R is supplied
before any query, then only marginalized in frequency; no restricted core
gets a newly optimized law. Use K=4, fixed physical order Y0,...,Y8 and
all actual outcomes, hence1023 nodes and511 queries.

For each node v write e_v=Delta B_v-4j_v. The certificate must establish

  P_core=sum_v p_v (e_v)_+ <7/12,
  h2(d_root)=h2(1/512)<1/32,
  sigma_{Y0=0}>1/2, sigma_{Y0=1}>1/2.                 (6)

Every query and every positive/negative/zero sign is treated with exact
prime-log expressions and rational logarithm enclosures, not rounded
pilot scores. Both first children have nonconstant actual core pairs.
By(2), the first actual child0 has its ORIGINAL full surplus
4I_child-C_child=sigma_child+s_child>1/2+3/4=5/4,
uniformly in m. At original physical weight1/2 it therefore owns a
strictly larger than5/8 reserve. Choose that single5/8 bank at the first
split, before charging any query, and leave the complementary child and
its complete reference bill intact. No earlier campaign spending is
imported into this newly specified test; the first root debit itself is
included in this one bank's charges.

For every m>=1, (A070's flag proof and positive-part subadditivity) give

 sum_v p_v (Delta C_v-4j_v)_+
   <=P_core+rho^2 h2(d_root)
   <7/12+1/128<3/5.                                  (7)

Book each successive actual expected positive charge against the SAME
5/8 bank. Every prefix of the history has accumulated no more than the
full nonnegative sum, so at every prefix the remainder is greater than
5/8-3/5=1/40. Old debits stay booked; later positive query credits are not
needed to establish availability and are not separately re-spent. Both
full terminals at every split remain in the exact ledger(5). This is a
nonlocal expected-tree allocation from ONE actual child, not a claim
that every low-probability individual path has a5/8 pathwise bank.

The witness has relevant bad queries at the root, at depth2 prefix0, and
at depth5 prefix0. At the root and depth2, both actual child core pairs retain
positive core influence. The depth5 query has a constant child core pair;
its full output still has positive control influence. Thus the test goes beyond a free/irrelevant
padding exposure and beyond the original three-bit family. The finite
history is not a theorem for all query orders or arbitrary core widths;
the all-private-width conclusion follows from(2),(7), not extrapolation.
