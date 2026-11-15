# Uniform containment: proofs and obstructions

All logarithms in costs are base 2; ln denotes the natural logarithm. Constants are
absolute unless their dependence is displayed. General containment P <= C I remains OPEN.
Correction to FLOW section 3b: its read-once zero-cancellation assertion needs to exclude
the empty derivative for biased functions. AND_2 (truth table 0x8) has mu(empty)=1/4,
H=2, P=1/2, I=1, V=3/4, so H is not 2P+2(I-V)=3/2. Its missing empty entropy
is 1/2 bit. This does not invalidate the general FLOW identities that retain Gamma.

The proofs here establish statements about every equal-width tribes function, and several
general identities and implications. They do not prove FEI or general containment.

## 1. Definitions and transfer between P and A — PROVED

Write mu(S)=fhat(S)^2, up(S)=E(D_S f)^2, p(S)=Pr[D_S f != 0],
I=sum |S| mu(S), V=1-mu(empty), P=sum mu(S) log(1/p(S)), and
A=sum mu(S) log(1/up(S)). Zero-weight summands are omitted. For S=empty,
p(S)=up(S)=1, so its cost is zero.

For nonempty S, the nonzero values of D_S f have magnitude between 2^(1-|S|)
and 1. Consequently 2^(2-2|S|) p(S) <= up(S) <= p(S), and summing logs gives

    P <= A <= P + 2(I-V).                                      (1)

Thus P<=C I implies A<=(C+2)I-2V; A<=C I implies P<=C I. Also
|E D_S f| <= p(S), so mu(S)<=p(S)^2. These assertions require Boolean f.
The sparse split P<=K I+Sp_K follows by partitioning the summands according to
whether log(1/p(S)) <= K|S|.

## 2. A general thinning bound — PROVED

For any real function h on a cube, D_i h can be nonzero only if at least one endpoint
of its i-edge is in the support of h. Therefore Pr[D_i h!=0] <= 2 Pr[h!=0].
Iterating, if R subset S then p(S)<=2^|S-R| p(R). It follows that

    log(1/p(R)) <= log(1/p(S)) + |S-R|.

For S sampled from mu and independently t-thinned to R_t,

    T_t := E log(1/p(R_t)) <= P + (1-t) I <= A+(1-t)I.           (2)

In particular, containment implies Conjecture T at every fixed t. The converse and
the relative increment assertion are OPEN here. Applying a Boolean-root assertion
to an arbitrary real derivative is not justified: this is the missing step in a
putative iteration of T. Equation (2) was tested on all Boolean n=4 functions by
audit.py, independently of the NPN reduction.

### The noise-support inequality can be sharpened — PROVED

For 0<=u<1, Bonami hypercontractivity and Holder on the support give

    F_R(u)=||T_sqrt(u) g_R||_2^2 <= ||g_R||_(1+u)^2
          <= up(R) p(R)^((1-u)/(1+u)).

The second step is ||g||_q<=||g||_2 p^(1/q-1/2), q=1+u. At u=1/2 this gives
F_R(1/2)<=up(R)p(R)^(1/3), strengthening the exponent 1/10 and prefactor 2
mentioned in the brief. It still supplies no cross-level budget: section 5 proves
that the two untruncated candidates fail even on tribes. Neither P<=CI nor A<=CI
follows from this pointwise bound alone.

## 3. Tribes generating functions — PROVED

Partition mw bits into m blocks of width w. Let a_j be the 0/1 AND of block j,
q=2^-w, b=1-q, and take f=2 product_j(1-a_j)-1. For a nonempty set S write
r for the number of blocks hit and s=|S|. Differentiating the product shows that
D_S f has a fixed sign on its support and magnitude 2^(1-s). Its support requires
all unselected bits in every hit block to be 1, and every unhit block not to fire.
Therefore

    p(S)=q^r 2^s b^(m-r),
    up(S)=4 q^r 2^-s b^(m-r),
    mu(S)=4 q^(2r) b^(2(m-r)).                                (3)

There are binom(m,r) [z^s]((1+z)^w-1)^r such sets. These formulas also cover
w=1 (an AND up to sign) and m=1. The empty Fourier weight is (2b^m-1)^2.
Summing (3) yields

    V=4 b^m(1-b^m),    I=2mwq b^(m-1),
    E_mu r=4mq b^m,
    P=w E_mu r-I+(-log b)(mV-E_mu r),
    A=P+2(I-V),        H=2P+2(I-V)+h0,                        (4)
    h0=mu(empty) log(1/mu(empty)).

For nonempty S, |E D_S f|=E|D_S f|. The empty term has alpha(empty)=1
and must be retained separately in entropy.
One useful rearrangement is

    P/I=1-2q + [2b(-log b)/(wq)](b-b^m).                     (5)

This is also an exact formula for the cost in item 1 of the brief; the sparse part
is obtained by retaining those (r,s) with rw-s-(m-r)log b>K s in the sum above.
The computation uses a binomial law in r and convolutions of
Binomial(w,1/2) conditioned to be nonzero for s. It reports the omitted spectral mass.

### Uniform support bound for every m,w — PROVED

Since -ln(1-q)<=q/b, (5) gives

    P/I <= 1-2q + 2b/(w ln 2).

For w>=3 this is less than 2, because 2/(3 ln 2)<1. For w=2 the right side is
1/2+3/(4 ln 2)<2, using ln 2>1/2. For w=1, (5) gives P/I=1-2b^m<=1.
Consequently every equal-width tribes function satisfies

    P <= 2I,    A <= 4I-2V,    H <= 6I.                       (6)

Here h0<=V/ln 2, from -x ln x<=1-x. In fact
H<=6I-(2-1/ln 2)V, so the stated simpler entropy bound follows.

Every Sp_K<=P<=2I for this family, for every K>0. This does not establish a sparse
budget for arbitrary Boolean functions.

### Exact thinning formula and T for tribes — PROVED

Put d_t=b^2+q^2((2-t)^w-1)=1-2q+q(1-t/2)^w. Summing over supersets gives,
for a nonempty R hitting r blocks with |R|=s,

    tau_t(R)=4 t^s q^(2r)(2-t)^(rw-s) d_t^(m-r).              (7)

The mass of R!=empty and its mean number of hit blocks are respectively

    V_t=4(b^m-d_t^m),
    E_tau r=4mq[1-(1-t/2)^w] b^(m-1),   E_tau |R|=tI.

Consequently

    T_t=w E_tau r-tI+(-log b)(m V_t-E_tau r).                 (8)

Equations (2) and (6) imply T_t<=(3-t)I for all equal-width tribes, in particular
T_(1/2)<=2.5 I. For the balanced sequence m=floor((ln 2)/q), as w tends to infinity,

    V -> 1, I/(w ln 2) -> 1, P/I -> 1, A/I -> 3,
    T_t/I -> 2-t  for every fixed t>0.                        (9)

For example, in (8) the first term divided by I tends to 2, the second is -t,
and the remaining term is O(1/w). There is no conflict with T_0=0: these limits
do not commute as t tends to zero.

## 4. Conjecture W is false; the sharp tribes repair — PROVED

Let

    W_(theta,c)=sum_{S!=empty} mu(S)c^-|S| up(S)^-theta.

From (3) and the binomial theorem, with d=1+2^theta/c,

    W_(theta,c)=4^(1-theta) (a^m-b^((2-theta)m)),
    a=b^(2-theta)+q^(2-theta)(d^w-1).                        (10)

### Original W (theta=1) fails for every finite c,K

It suffices to consider c>=4: W is decreasing in c, so failure at a larger c
implies failure at every smaller c. Then 1<d=1+2/c<2 and a=1+q(d^w-2).
For the balanced sequence in (9), q d^w tends to zero and

    log2 W_(1,c)=(1+o(1)) d^w.

Indeed m ln a=(ln 2)(d^w-2)(1+o(1)), and subtracting b^m, which tends to 1/2,
does not change the leading logarithm. But log2(V K^(I/V))=O(w) for every fixed K.
Thus no absolute finite c,K can satisfy the original W. This is a counterexample
to W itself, not to P<=CI or A<=CI: (6) holds on the very same functions.

### All 0<theta<1: exact threshold for the tribes obstruction

Define

    c_theta=2^theta/(2^(1-theta)-1).

If c<c_theta, d/2^(1-theta)>1. The same calculation on balanced tribes gives
log2 W growing exponentially in w (or faster); it cannot be O(I). Hence this c
is impossible for any fixed K, even restricted to tribes.

If c>=c_theta, then d^w<=q^-(1-theta). Therefore

    a <= b^(2-theta)+q-q^(2-theta) <= b+q = 1,
    W_(theta,c) <= 4^(1-theta).                              (11)

We next convert the constant bound to the requested variance-normalized shape.
For every nonconstant Boolean function the cube Poincare inequality gives I>=V.
Also V log(1/V)<=2I: if epsilon<=1/2 is the smaller output probability,
edge isoperimetry gives I>=2 epsilon log(1/epsilon), while
V=4epsilon(1-epsilon)<=4epsilon and log(1/V)<=log(1/epsilon).
Combining these inequalities with (11),

    log2(W/V) <= 2(1-theta)+log(1/V)
               <= (4-2theta) I/V.

Thus for every equal-width tribes function, all 0<theta<1 and c>=c_theta,

    W_(theta,c) <= V K_theta^(I/V),
    K_theta=2^(4-2theta).                                    (12)

This completely identifies which degree discounts c admit some finite K for this
family at each theta. Sufficiency for all Boolean functions is OPEN. It would imply
containment; no general proof is claimed.

For clarity, the Jensen implication for any family satisfying such a moment bound is

    theta A-(log c) I <= (log K) I,
    A <= [(log c+log K)/theta] I,    P <= same constant * I.   (13)

This uses the conditional probability mu/V on nonempty sets. For theta=1/2,
c=2+sqrt(2), K=8, it gives A<=[6+2log(2+sqrt(2))]I; (6) is the stronger tribes bound.

## 5. Both proposed untruncated budgets fail — PROVED

### up-weighted count

Even theta=0 fails. For any t>0,

    sum_R t^|R| up(R)=E_mu(1+t)^|U|.

For tribes this equals

    (2b^m-1)^2 + 4(e^m-b^(2m)),
    e=b^2+q^2((2+t)^w-1)=1-2q+q(1+t/2)^w.

On the balanced sequence, log2 of this sum is (1+o(1))(1+t/2)^w,
which exceeds C I for every fixed C. Multiplying by p(R)^-theta only increases
the count. Thus the first proposed count cannot be uniformly <=2^(C I) with
no cutoff, or with a bound independent of the cutoff M: take M=n.

The numerical interpretation of the brief's cutoff is

    up_M(R)=sum_{U contains R, |U|<=M} mu(U),
    sum_R t^|R| up_M(R) p(R)^-theta.                          (14)

The cutoff is on U, not on R. The tables include M=ceil(2I), ceil(4I), and no cutoff
at t=1/2. A universal estimate when M=a I for fixed a is OPEN here. Bounds whose
constant is independent of arbitrary M are disproved above. The exponential-moment
obstruction comes from far larger U, so it does not settle this restricted question.

### tau-weighted count

Fix t in (0,1] and theta>0. For 0<theta<1, (3) and (7) give

    E_tau p(R)^-theta = tau_t(empty)+4(a^m-a0^m),
    a0=d_t b^-theta,
    a=a0+q^(2-theta)[(2-t+t 2^-theta)^w-(2-t)^w].             (15)

The empty probability is 1-4b^m+4d_t^m. Put

    D=(2-t+t 2^-theta)/2^(1-theta)
      =2^theta(1-t/2)+t/2 > 1.

For balanced tribes, a0=1+O(q), the positive increment in (15) is
(1+o(1))q D^w, and D<2. Hence

    log2 E_tau p(R)^-theta = (1+o(1))D^w,

which is not O(I). Every theta>=1 also fails by monotonicity in theta. Thus
no positive fixed theta works, even for t=1/2 and even on equal-width tribes.
This rules out the second proposed budget throughout the requested (0,1/2] range.
It coexists with the linear logarithmic mean in (8)-(9).

## 6. Reference measures across all levels — PROVED facts; general bound OPEN

For every rho in (0,1), tau_rho is a probability measure and

    rho^|S| mu(S) <= tau_rho(S) <= up(S).

The lower bound takes only U=S in the thinning sum; the upper bound drops the
probabilities of obtaining S from U. Therefore its cross entropy L_rho satisfies

    H <= L_rho := E_mu log(1/tau_rho(S))
       <= H+I log(1/rho).                                   (16)

The first inequality is Gibbs. Any fixed-rho reference cost O(I) is equivalent to
FEI, not an established shortcut to containment. Nonetheless the domination needed
in the brief is excellent: up(S)>=pi(S) without a degree loss.

The uniform mixture pi_mix=int_0^1 tau_rho d rho is a probability and satisfies

    pi_mix(S)=sum_{U contains S} mu(U)/[(|U|+1)binom(|U|,|S|)],
    mu(S)/(|S|+1) <= pi_mix(S) <= up(S),
    H <= E_mu log(1/pi_mix(S)) <= H+I.                       (17)

The last bound uses log(|S|+1)<=|S| for integer |S|. A three-point mixture of
rho=1/4,1/2,3/4 is also tested; its cost is <=H+I+log 3, since its rho=1/2
component has weight 1/3. For a uniform O(I) bound in the highly biased regime,
the additive constant in this particular estimate should not be used; (16) for
rho>=1/4 gives directly L_mix<=H+2I by concavity of -log.

If pi is any sub-probability with pi(S)>0 on the spectral support,
up(S)>=pi(S)2^-d|S|, and E_mu log(1/pi(S))<=C I, then

    A <= (C+d)I,    P <= (C+d)I.                             (18)

This is the exact sufficient form used here. The thinned references and their
mixtures have d=0. For tribes, (6), H<=6I and (16)-(17) prove L_(1/2),L_mix
<=7I. Their ratios are also evaluated on large majority and all other families.
No universal bound for these reference costs is proved here.

### The proposed Markov product is not a sub-probability

Let R={r_1,...,r_s} in any order, with R_j the first j elements. Then

    product_j Pr[U contains r_j | U contains R_(j-1)]
      = product_j up(R_j)/up(R_(j-1)) = up(R).

Order by decreasing influence has no effect. Summing these weights gives
Z=sum_R up(R)=E_mu 2^|U|, generally greater than 1. If normalized, the reference
cost is exactly A+log Z. Section 5 already proves log Z/I unbounded on balanced
tribes (take t=1). Thus this repair loses the desired bound even on tribes.
A genuine sequential stopping/absence law would need additional factors; those
are not in the product specified in the brief.

The independent-product reference tested for comparison uses coordinate odds
Inf_i: pi(S)=product_i Inf_i^1[i in S]/(1+Inf_i). Its exact cost is

    sum_i log(1+Inf_i)+sum_i Inf_i log(1/Inf_i).

For balanced tribes Inf_i=2q b^(m-1), this cost divided by I grows as w.
For majority its analogous cost also grows logarithmically with dimension. It does
not give the desired common reference bound. The thinned laws and their mixtures
have bounded ratios in all the tables, including tribes and majority together;
their unresolved universal cost remains equivalent to FEI.

## 7. AND and address functions — PROVED

For AND_n, (3)-(5) with m=1 give I=2nq, V=4q(1-q), q=2^-n, and

    P/I=1-2q,     A/I=3-2q-4(1-q)/n.

Thus P<=I and A<=3I. Its exact thinning ratio is

    T_t/I=2[1-(1-t/2)^n]-t.

In particular any universal T_(1/2) constant must be at least 3/2. These highly
biased functions show that looking only at balanced cases would miss a sharp
necessary lower bound for this particular T constant.

For the a-bit address function, there are 2^a independent data bits and the output
is the data bit selected by the address. Each nonzero Fourier set consists of one
data bit j and any subset of r address bits. Its weight is 2^-2a, and

    p(S)=2^-(a-r),   up(S)=2^-(a+r).

These follow by differentiating the selected-data indicator on the address cube.
The spectral distribution of r is Binomial(a,1/2), so

    I=1+a/2,   P=a/2<=I,    A=3a/2<=3I.

Summing its moment gives, for c>=1,

    W_(theta,c)=c^-1 [2^(theta-1)(1+2^theta/c)]^a.

Consequently W<=K^I with K=max(1,2^(theta-1)(1+2^theta/c))^2. In this family
the original theta=1 version is valid. Its failure on tribes is therefore a
structural issue that the address examples alone do not detect.

## 8. Coverage and limits of computation — CHECKED / OPEN

npn.cpp scans the truth tables with f(0)=+1 and marks the entire orbit under every
input permutation, every input negation, and output complementation. The first
unmarked truth table is a new representative. A bitset records all 2^(2^n-1)
output-complement classes. Thus no NPN class can be skipped, and none is repeated.
Every functional in the census is invariant under these transformations; the
derivative signs change but mu, up and p are merely permuted. Generation and counts
are saved in npn1.log through npn5.log. The direct all-functions n=4 audit confirms
the extrema without relying on this reduction.

The finite supremum of Sp_K/I is not a proof of a dimension-free bound. The same
qualification applies to T, the cutoff count (14), weakened W on arbitrary Boolean
functions, and the reference-cost ratios. These four general questions remain OPEN.
