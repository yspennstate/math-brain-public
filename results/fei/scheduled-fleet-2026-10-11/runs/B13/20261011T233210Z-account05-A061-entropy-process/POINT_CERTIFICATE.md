# Point-function one-coordinate certificate

Let f_{n,x0}(x)=1-2 1{x=x0}, n>=1, on a uniform sign cube. Set d=2^{1-n}. Translations change coefficient signs only; coordinate permutations preserve all quantities. The empty coefficient is 1-d, and each nonempty coefficient is -d chi_S(x0). Thus every coordinate has influence d, I=nd, and

    H_n=-2(1-d)^2 log2(1-d)-2d(2-d) log2 d.          (1)

At a physical query the child missing x0 is constant and the other is a translated point function on n-1 bits. Set H_0=0 (its sign is immaterial). Every coordinate therefore has the SAME entropy decrement and rate

    D_i=H_n-H_{n-1}/2,
    R_n=min_i D_i/Inf_i = (H_n-H_{n-1}/2)/d.        (2)

R_1=0, R_2=4. For n>=2, with boundary 0 log 0=0,

    R(d)=4-4d-2d log2 d
       +[(1-2d)^2 log2(1-2d)-2(1-d)^2 log2(1-d)]/d. (3)

In particular R_3=12-(9/2)log2 3, and R_4=32-(49/4)log2 7+(9/2)log2 3. (Formula R_4 is about 4.7422.)

## All-dimensional decrement-rate monotonicity

Put c=1/ln 2 and F(x)=(1-x)^2 ln(1-x). Taylor expansion on 0<=x<1 gives

    F(x)=-x+(3/2)x^2-sum_{k>=3} 2x^k/[k(k-1)(k-2)].

This follows by multiplying the absolutely convergent series ln(1-x)=-sum_{j>=1}x^j/j by 1-2x+x^2 and collecting coefficients. Hence for 0<d<=1/4,

    R(d)=4+d[-4-2log2 d+3c]-c sum_{k>=3}A_k d^{k-1},
    A_k=2(2^k-2)/[k(k-1)(k-2)].

Subtract the expression at d/2:

    R(d)-R(d/2)
      =d[-3-log2 d+(3/2)c]
       -c sum_{k>=3}A_k(1-2^{1-k})d^{k-1}.         (4)

The k=3 term is (3/2)d^2. For k>=4, k(k-1)(k-2)>=24 and A_k<=2^k/12; also 1-2^{1-k}<=1. Thus the sum in (4) is at most

    (3/2)d^2+(4/3)d^3/(1-2d)
      <= (13/24)d,                               (5)

because d<=1/4 implies (3/2)d<=3/8 and (4/3)d^2/(1-2d)<=1/6. Since -log2 d>=2,

    R(d)-R(d/2)>=d[-1+23/(24 ln 2)]>0.            (6)

For completeness ln2<3/4: using z=1/3, ln2=2 sum_{j>=0}z^{2j+1}/(2j+1), and the tail after j=0 is at most (2/3) z^3/(1-z^2)=1/36. Thus ln2<=25/36<3/4<23/24. This proves the sign without numerical logs.

The series also gives R(d)->4 as d->0, because d log d->0 and its summed remainder is O(d^2). Consequently R_n strictly decreases for n>=3, all those rates exceed 4, and the exact sharp all-dimensional maximum is

    sup_{n>=1} R_n=R_3=12-(9/2)log2 3 < 5.        (7)

The inequality R_3>4 follows from 3^9<2^16; R_3<5 follows from 3^9>2^14. Equality in the maximum occurs exactly at n=3 (up to unused coordinates, output sign and translated defect vertex).

## Exact KL and logarithmic-rate certificate

For a fixed query, the residual empty packet has q0=(1-d)^2+d^2; its queried mass is b0^2=d^2. The other 1/d-1 residual packets have q=2d^2 and queried mass d^2. Therefore

    lambda_i=d-d^2+d^2 log2(q0/d^2),
    L_n=lambda_i/d=1-d+d log2((1-2d+2d^2)/d^2).  (8)

For n=1 this gives L_1=0. For d>0 set q(d)=1-2d+2d^2. A direct subtraction gives

    L(d)-L(d/2)=(d/2)log2[q(d)^2/(8d^2 q(d/2))]. (9)

The polynomial identity

    q(d)^2-8d^2q(d/2)=1-4d                     (10)

settles its sign exactly. Thus L_2=1, L_3=L_4=(3+log2 10)/4, L_n strictly decreases for n>=4, and L_n->1. In particular

    sup_n min_i lambda_i/Inf_i=(3+log2 10)/4<8/5. (11)

The upper bound follows from 10^5<2^17, equivalently log2 10<17/5. If nu_i=b_T^2/d and q_i=q_T, the exact KL identity handed off by the lead gives

    KL_2(nu_i||q_i)=n-1-L_n
      >=n-1-(3+log2 10)/4 > n-1-8/5.             (12)

Thus these genuinely rare functions repay their entire growing n-1 rarity logarithm with posterior KL, up to a sharp constant. The KL statement can also be checked directly: nu_i is uniform with mass d on all 1/d packets, so substitute q0 and 2d^2 into its definition. No uncertainty theorem is needed.

## Consequence for the entropy process and Q*

Every actual nonconstant descendant is another point function. At every coordinate of every descendant, D_i<=R_3 Inf_i. Therefore R_3 I(g_t)-H(g_t) is a supermartingale for EVERY fair adaptive rule on this family, with constant boundary zero. This is the sharp drift price for this class: the dimension-three node forces C>=R_3. At any C>=R_3 the minimal nonnegative reserve Q*_v=max(0,D_v-Cd_v+avg Q*_children), with zero constant-leaf reserve, vanishes at every node by backwards induction. This conclusion requires no new tree enumeration. It says nothing about the stronger universal Q* target for arbitrary Boolean functions.

The first unsupported universal line is that every actual Boolean function, or a suitable proper restriction of it, has a coordinate paying its rarity logarithm by KL with an absolute residual constant. Point-function symmetry cannot justify that step for several signed defects, arbitrary cores, or overlapping controls.
