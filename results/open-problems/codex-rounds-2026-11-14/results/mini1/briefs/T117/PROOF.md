# The three-bit optimum and its unique first-order Markov exception

All logarithms are base two unless written as ln. Put h(t)=-t log t-(1-t) log(1-t), with 0 log 0=0. For 0<d<1, let

    M_3(d) = max_{P on {0,1}^3} I(X;Y),

where Y is the output of independent deletions of the three input bits. M_3 is measured in bits per three-bit block. It is not the infinite-channel capacity C(d).

## Statement

Set s=1-d, k=d/s, h_0=h(1/3)=log 3-2/3, and

    R = 2^(1+2k),      r = R/(1+R),
    L = log(1+R)-3k log 3.

There is exactly one a in (0,1) satisfying

    G_k(a) := log((1-a)/a)
              + 2k log(2(1-a)/(1+2a))
              + 3k^2 h_0 + 3k log 3 - log(1+R) = 0.       (1)

The unique input attaining M_3(d) has probabilities

    P(000)=P(111)=a/2,
    P(001)=P(011)=P(100)=P(110)=(1-a)r/4,
    P(010)=P(101)=(1-a)(1-r)/2.                            (2)

Its mutual information is

    M_3(d) = 3d^2 s [1-(1-a)h_0]
             + 3d s^2 [1+h((1+2a)/3)]
             + s^3 [1+h(a)+(1-a)L].                    (3)

There is exactly one deletion probability d_* in (0,1) at which (2) is the three-bit marginal of a stationary binary first-order Markov chain. It lies in (1/2,2/3). More precisely, k_*=d_*/(1-d_*) is the unique positive zero of

    B(k) = -4 + 2 log(2(2z+1)/(3z^2+2z+1))
                 + 3k h_0 + 3 log 3,    z=2^(2k).       (4)

At d_*, the chain has stationary law (1/2,1/2) and flip probability

    theta_* = 1/(1+2^(2k_*)).                           (5)

At every other d in (0,1), every stationary binary first-order Markov input has strictly smaller three-bit mutual information than M_3(d).

The known complement/reversal reduction already gives an optimal run-count law for blocks of length three: see Hassan Khodaiemehr and Chen Feng, *Orbit Reduction and Learned Run Distributions for Finite-Blocklength Binary Deletion Channels*, arXiv:2609.24889v2, Proposition 1 and Proposition 2(c), https://arxiv.org/html/2609.24889v2. The proof below includes that reduction to make the explicit scalar calculation and the exceptional Markov parameter self-contained. No claim of literature priority is made.

## 1. Uniqueness and symmetry

Write W_x(y)=Pr(Y=y|X=x) and q_P(y)=sum_x P(x)W_x(y). Mutual information equals

    I(P)=H(q_P)-sum_x P(x)H(W_x).

The second term is linear in P. For a length-three output x,

    q_P(x)=s^3 P(x),

because such an output requires no deletions. Thus P -> q_P is injective. Entropy is strictly concave on the finite output simplex, so I(P) is strictly concave in P. Continuity on the compact input simplex gives a maximizer, and strict concavity gives uniqueness.

Let c complement every bit and let v reverse a word. For complementation, W_{cx}(cy)=W_x(y). For reversal, reversing the deletion mask is a probability-preserving bijection between masks, so W_{vx}(vy)=W_x(y). Either operation merely permutes input and output labels and therefore preserves I. Uniqueness implies that the maximizing P is invariant under both operations.

Their three orbits on length-three words are

    A={000,111},
    B={001,011,100,110},
    D={010,101}.

Let their total probabilities be a,b,c, respectively; hence a+b+c=1. Every invariant input is uniform within each orbit.

## 2. Conditional on the number of survivors

Let K=|Y|. Its law is Bin(3,s) and is independent of X. Since K is a function of Y,

    I(X;Y)=sum_{j=0}^3 Pr(K=j) I(X;Y|K=j).              (6)

For K=0, the conditional mutual information is zero.

For K=1, the surviving position is uniform among the three positions. By complement symmetry its bit is uniform, so H(Y|K=1)=1. A constant word has conditional output entropy zero. Every nonconstant word has one symbol once and the other twice, so its conditional output entropy is h_0. Therefore

    I(X;Y|K=1)=1-(1-a)h_0.                             (7)

For K=2, each of the three position pairs is equally likely. The following table lists the outputs of representative words, with repetitions retained:

    orbit      word       outputs       H(Y|X=x,K=2)
      A        000        00,00,00             0
      B        001        00,01,01             h_0
      D        010        01,00,10             log 3.

The entropy values for every other word in the same orbit agree by the channel symmetries. For A the output pair is constant with probability one; for B and D it is constant with probability 1/3. Thus

    t := Pr(Y is constant | K=2) = a+(1-a)/3=(1+2a)/3.

Complement symmetry gives probability t/2 to each of 00 and 11, and probability (1-t)/2 to each of 01 and 10. Consequently

    I(X;Y|K=2)=1+h(t)-b h_0-c log 3.                   (8)

For K=3 the output is exactly X, so

    I(X;Y|K=3)=H(X)=1+H(a,b,c)+b.                     (9)

Indeed the three orbit sizes are 2,4,2, and the entropy within the selected orbit is a+2b+c=1+b.

Combining (6)-(9) gives the exact objective

    J(a,b,c)=3d^2s[1-(1-a)h_0]
              +3ds^2[1+h(t)-b h_0-c log 3]
              +s^3[1+H(a,b,c)+b].                    (10)

## 3. Eliminate one orbit parameter

For 0<=a<1 write b=(1-a)u, c=(1-a)(1-u). Then

    H(a,b,c)=h(a)+(1-a)h(u).

The terms of (10) depending on u, divided by s^3(1-a), are

    h(u)+u-3k[u h_0+(1-u)log 3]
      = h(u)+(1+2k)u-3k log 3,                        (11)

where log 3-h_0=2/3 was used.

For any real A, differentiating h(u)+Au gives

    log((1-u)/u)+A.

It decreases strictly from +infinity to -infinity, so the unique maximum is at u=2^A/(1+2^A). Substitution gives the value log(1+2^A). Taking A=1+2k proves u=r and maximum value L in (11).

The resulting objective is exactly the right side F(a) of (3). On (0,1), using h'(x)=log((1-x)/x),

    F'(a)/s^3 = 3k^2 h_0 + 2k h'((1+2a)/3)
                 + h'(a)-L
               = G_k(a).                             (12)

Moreover h''(x)=-1/[ln(2)x(1-x)]<0, whence

    F''(a)=3ds^2(2/3)^2 h''((1+2a)/3)+s^3 h''(a)<0.

As a tends to zero, G_k(a) tends to +infinity. As a tends to one, both log terms in (1) tend to -infinity. Thus (1) has exactly one solution in (0,1), which globally maximizes F on [0,1]. Its associated r lies in (0,1), so all eight word probabilities are positive. Equations (2) and (3) follow.

## 4. The Markov constraint

Suppose a stationary binary first-order Markov chain attains M_3(d). Its three-bit marginal must equal the unique law (2). In particular its one-bit marginal is uniform, and its pair marginals are positive and invariant under complement. Dividing pair probabilities by the one-bit probabilities shows that its transition matrix must be

    [1-theta, theta; theta, 1-theta]

for some 0<theta<1. For this chain the orbit masses are

    a=(1-theta)^2,    b=2theta(1-theta),    c=theta^2.   (13)

Thus b^2=4ac is necessary. It is also sufficient for positive a,b,c summing to one: b=2sqrt(ac) implies (sqrt(a)+sqrt(c))^2=1, and theta=sqrt(c) then gives (13).

The already-established optimum satisfies b/c=R. Combining this with (13) gives

    2(1-theta)/theta = R=2z,
    theta=1/(z+1),    a_M=z^2/(z+1)^2.                (14)

At this candidate,

    (1-a_M)/a_M=(2z+1)/z^2,
    2(1-a_M)/(1+2a_M)=2(2z+1)/(3z^2+2z+1).

Substitution in (1), using log z=2k and 1+R=1+2z, cancels log(2z+1) and yields

    G_k(a_M)=k B(k).                                  (15)

Since k>0 and G_k has a unique zero, the optimum is Markov if and only if B(k)=0.

## 5. Exactly one positive zero of B

First,

    B(0)=3log 3-4=log(27/16)>0.                       (16)

For strict concavity, put f(z)=3z^2+2z+1 and let D=z(d/dz). Direct differentiation gives

    D^2 ln(2z+1)=2z/(2z+1)^2,
    D^2 ln f(z)=2z(3z^2+6z+1)/f(z)^2.

As d/dk=2ln(2)D, differentiating (4) twice gives

    B''(k)=8ln(2)[2z/(2z+1)^2
                   -2z(3z^2+6z+1)/f(z)^2].          (17)

The second term inside the brackets has larger magnitude because

    (3z^2+6z+1)(2z+1)^2-f(z)^2
      =3z^4+24z^3+21z^2+6z > 0                       (18)

for z>0. Hence B''(k)<0 for every k>=0.

As k tends to infinity,

    log(2(2z+1)/(3z^2+2z+1))
      = 2-log 3-2k+o(1),

and therefore

    B(k)=(3h_0-4)k+log 3+o(1).

The slope 3h_0-4=log(27/64) is negative, so B tends to -infinity. Continuity and (16) give a positive zero. For any positive zero t, the mean value theorem gives some xi in (0,t) with

    B'(xi)=(B(t)-B(0))/t<0.

Strict concavity implies B'(u)<B'(xi)<0 for u>=t. Thus no second zero can lie to the right of t. The positive zero is unique.

Its location can be checked without numerical logarithms. At k=1, z=4 and

    B(1)=log(26244/23104)>0.

At k=2, z=16 and

    B(2)=log(9526572/18249984)<0.

Both signs follow from the displayed integer comparisons. Thus 1<k_*<2, or equivalently 1/2<d_*<2/3. Equations (14)-(15) prove (5) and the claimed exceptional attainment. At every other d the unique optimum cannot be Markov, so each stationary first-order Markov law has strictly lower mutual information.

## 6. An algebraic special case at d=1/2

At d=1/2, k=1, r=8/9 and (1) becomes

    log(81(1-a)^3/[a(1+2a)^2])=0.

Equivalently, a is the unique root in (0,1) of

    85a^3-239a^2+244a-81=0.                           (19)

The uniqueness also follows from the strict decrease of G_1 proved above. The orbit masses are exactly

    a,    b=8(1-a)/9,    c=(1-a)/9.

A shorter expression for M_3(1/2) follows from an output-divergence calculation. For a full-support maximizing law P, differentiating I at P in direction delta_x-P gives

    d/d epsilon I((1-epsilon)P+epsilon delta_x)|_{epsilon=0}
      = D(W_x || q_P)-I(P).

To verify this identity, differentiate H(q_P)-sum_z P(z)H(W_z). The entropy derivative is -sum_y (W_x(y)-q_P(y))log q_P(y); the additional constant in the derivative of -t log t vanishes since sum_y(W_x(y)-q_P(y))=0. Combining the remaining terms gives the displayed identity. All output probabilities are positive because P has full support and 0<d<1. Both signs of a sufficiently small epsilon are feasible, so the derivative vanishes. Thus I(P)=D(W_x||q_P) for each x.

Take x=000. Conditional on K=1 its divergence is 1. Conditional on K=2 the output is 00, of marginal probability (1+2a)/6, so its divergence is log(6/(1+2a)). Conditional on K=3 the output is 000, of probability a/2, so its divergence is log(2/a). The K=0 divergence is zero. At d=1/2, weighting by the binomial probabilities yields

    M_3(1/2) = 3/8 + (3/8)log(6/(1+2a))
                    + (1/8)log(2/a),                 (20)

with a determined by (19).

A candidate Markov optimum at d=1/2 would have theta=1/5 and a=16/25. It is excluded exactly: (15) gives

    G_1(16/25)=B(1)=log(6561/5776)>0.

Thus increasing a at fixed b/c=8 improves its mutual information. This is a concrete finite-block obstruction, independent of numerical optimization.

## Scope

This is an exact finite-block result. It neither identifies C(d) nor rules out a first-order Markov process attaining its infinite-block information rate optimum. Finite-block optima need not be consistent as blocklength varies. In particular, the special parameter d_* is not asserted to have a known infinite-channel capacity.
