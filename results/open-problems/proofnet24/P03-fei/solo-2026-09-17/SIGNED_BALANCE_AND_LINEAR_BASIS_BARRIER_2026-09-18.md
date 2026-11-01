# Signed overlap balance is not scale-local, and fixed linear bases lose a logarithm

Status: proved below and self-checked; novelty UNVERIFIED. These results eliminate two proof shortcuts. They do not refute FEI and do not prove the live logarithmic inequality.

Throughout, a_S=fhat(S), p_S=a_S^2, and logarithms are base two unless ln is written.

## 1. Exact sign balance on every spectral translation

Booleanity is equivalent to

    sum_S a_S a_(S xor U)=1{U=empty}.                  (1)

For a fixed nonempty U, group the sum into unordered pairs {S,S xor U}. Equation (1) becomes

    sum_pairs a_S a_(S xor U)=0.                       (2)

Consequently

    sum_pairs: product>0 |a_S a_(S xor U)|
      =sum_pairs: product<0 |a_S a_(S xor U)|.          (3)

In particular, for every coordinate direction, exactly half of the adjacent absolute-amplitude overlap lies on same-sign coefficient edges and half on opposite-sign edges. Zero products do not matter.

This is stronger than a cancellation only after summing all coordinate directions, but it is unweighted. The logarithmic functional inserts a magnitude-ratio weight. If r=a_S^2>=s=a_T^2 and t=ln(|a_S|/|a_T|), then

    s log_2(r/s)=(2/ln2)|a_S a_T| t exp(-t).            (4)

Equation (3) controls the same expression with weight one, not with t exp(-t).

## 2. One-point defect: perfect sign balance, maximally separated log cost

Let N=2^n and define the Boolean function

    f_n(x)=-1 at x=0, and f_n(x)=+1 otherwise.          (5)

Its Fourier coefficients are

    a_empty=1-2/N=(N-2)/N,
    a_S=-2/N for every nonempty S.                      (6)

Fix a coordinate i. There is one opposite-sign spectral edge, {empty,{i}}, with amplitude product

    2(N-2)/N^2.

The other N/2-1 nonzero edges in direction i join two negative coefficients. Each has product 4/N^2, so their total is also

    (N/2-1)4/N^2=2(N-2)/N^2.                           (7)

This verifies (3) by an explicit exact cancellation. However every same-sign edge has equal endpoint masses, hence zero logarithmic cost. The unique opposite-sign edge has all of it:

    K_i(f_n)= [8/N^2] log_2[(N-2)/2].                  (8)

Thus 100 percent of K_i lies in the opposite-sign class although the unweighted overlaps of the two sign classes are exactly equal. No assertion that unweighted signed cancellation persists separately at magnitude-ratio scales can be used without an additional quantitative transport lemma.

This family is not an FEI or K/I obstruction. Its influence is

    I(f_n)=2n/N,

while K/I=4 log_2[(N-2)/2]/N tends to zero. It shows precisely that the missing step is not cancellation itself, but a non-reusing payment for where the cancellation mass moves across scales.

## 3. Generalized influences and arbitrary linear bases

For a nonzero direction U in F_2^n define

    alpha_U=Pr_x[f(x)!=f(x xor U)].                     (9)

Fourier expansion gives

    alpha_U=sum_S p_S 1{|S intersect U| is odd}.        (10)

Indeed E[f(x)f(x xor U)]=sum_S p_S(-1)^|S intersect U|, and alpha_U is half of one minus this correlation.

Let U_1,...,U_k span F_2^n. The linear measurements

    Y_j=|X intersect U_j| mod 2

of the spectral random subset X determine X injectively. Entropy subadditivity therefore proves the valid general inequality

    H(f)=H(X)<=H(Y_1,...,Y_k)<=sum_j h_2(alpha_(U_j)). (11)

For k=n this is precisely the usual marginal-entropy bound after an arbitrary invertible linear reparameterization of the cube. Allowing k>n gives a redundant fixed linear measurement system.

A tempting stronger route would be to choose the basis or spanning family so that the last sum is O(I(f)) in the original coordinates. The one-point family disproves this for every choice simultaneously.

For (5), translation by any nonzero U changes f at exactly the two points 0 and U. Hence

    alpha_U=2/N for every U!=0.                          (12)

Every spanning family has k>=n, so (11) costs at least

    n h_2(2/N).

Compared with I(f_n)=2n/N, the ratio is

    h_2(2/N)/(2/N)=log_2(N/2)
       -[(1-2/N)/(2/N)]log_2(1-2/N),                   (13)

which tends to n-1+1/ln2. Therefore no fixed invertible linear change of variables, nor any redundant fixed collection of parity queries followed by entropy subadditivity, removes the logarithmic loss.

The actual spectral entropy does not have this loss. From (6),

    H(f_n)=-[(N-2)/N]^2 log_2([(N-2)/N]^2)
       +(N-1)(4/N^2)(2n-2),                            (14)

and H(f_n)/I(f_n) tends to 4. Thus the gap in (11) is a proof-method artifact on a Boolean family, not evidence against FEI.

## 4. Why an adaptive parity code exits the Boolean class

The failure above concerns a fixed spanning collection and the step H(Y)<=sum H(Y_j). An adaptive or conditional parity decision tree could encode a rare spectral event at its correct small average cost: after a rare branch, additional bits are paid only on that branch. Entropy chain rule does this automatically.

There is an exact description after one query. Let T_U f(x)=f(x xor U) and put

    A=(f+T_U f)/2,     B=(f-T_U f)/2.                  (15)

Then A,B take values in {0,+1,-1}, have disjoint physical supports, and

    Ahat(S)=ahat(S)  if |S intersect U| is even, else 0,
    Bhat(S)=ahat(S)  if |S intersect U| is odd,  else 0. (16)

Their squared L2 masses are 1-alpha_U and alpha_U. Hence the two conditional laws of the spectral subset after the parity answer are exactly the normalized squared Fourier laws of A and B.

This suggests enlarging the induction class to partial Boolean functions g:{+1,-1}^m->{0,+1,-1}. Unfortunately that class is already FEI-hard. Let rho=E g^2 and define normalized spectral entropy and influence from p_S=ghat(S)^2/rho. Given any Boolean h on n bits, set

    g(x,z)=h(x) 1{z=+1}.                               (17)

Then rho=1/2, and the normalized squared spectrum is the product of hhat(S)^2 with a fair bit. Therefore

    H_norm(g)=H(h)+1,       I_norm(g)=I(h)+1/2.        (18)

If a universal H_norm<=C I_norm held for all partial Boolean functions, apply it to (17) with h replaced by its r-fold tensor power. Tensor additivity gives

    rH(h)+1 <= C[rI(h)+1/2].

Divide by r and let r tend to infinity to obtain full FEI with constant C. Thus the natural one-query closure class is not an independently easy substitute.

Nor is the full partial-Boolean class an artificial enlargement beyond the functions that projection can produce. Given an arbitrary g:{+1,-1}^m->{0,+1,-1}, add a bit w and define a Boolean parent F by

    F(x,+1)=F(x,-1)=g(x)          when g(x)!=0,
    F(x,+1)=+1, F(x,-1)=-1        when g(x)=0.            (19)

Then

    [F(x,w)+F(x,-w)]/2=g(x)                               (20)

for both values of w. Thus, after identifying functions constant in w with functions on the quotient cube, every partial Boolean function is exactly the even branch A of one Boolean parent and one parity query. Any inductive statement closed under all such branches must therefore handle the entire partial-Boolean class. Combined with (18), this closure is FEI-hard, not merely a convenient overapproximation.

After multiple parity queries, Fourier projection onto an affine subspace need not even remain {0,+1,-1}-valued pointwise. For an explicit example, take the two-bit one-point defect, whose mean is 1/2, and query both standard spectral parities. The branch on which both answers are zero projects onto the constant coefficient alone, so its physical-space representative is the constant function 1/2. Thus the signed convolution identities can disappear further. One cannot recursively invoke a Boolean spectral lemma at each information branch without proving a closure or replacement invariant.

This identifies a narrower live possibility: construct a variable-length multiscale code whose analysis uses the original signed convolution identities globally, rather than trying to prove the full inequality anew on every conditioned partial function. No such code or constant bound is constructed here.

## 5. Relation to the current logarithmic target

The previous positive-power obstruction showed that fixed exponential moments of the log ratio are too strong. The present one-point calculation shows that exact sign cancellation is too weak when left unweighted. Together they bracket the needed argument:

- it must retain the true linear logarithmic cost rather than a positive power;
- it must transport cancellation across magnitude scales rather than assert cancellation within each scale;
- it must allocate the transport cost without reusing the same influence;
- a fixed linear coordinate system and marginal entropy cannot supply that allocation.

`check_signed_basis_barrier.py` verifies all coefficient, influence, generalized-influence, sign-overlap and K formulas with exact rational arithmetic and outward rational logarithm intervals for n=2,...,10. It also checks the parity-projection identities (15)-(16) on every Boolean function through three variables, the partial-Boolean lift (17)-(18) on the same range, and the completion construction (19)-(20) for every partial Boolean function through three variables. Universal statements above are proved algebraically, not by enumeration. The check is not an independent audit.
