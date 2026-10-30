# The prime-boundary reserve is a pair-occupancy quantity

All logarithms are natural. Let m>=3, independent rare Bernoulli bits have
probabilities e_i>0, s=sum e_i<=1/8, and e2=sum_{i<j}e_i e_j,
e3=sum_{i<j<k}e_i e_j e_k. Two additional core bits are fair.
The Boolean sign F is positive exactly when 3b1+3b2+2 sum rare>=5.
Physical signs are x=2b-1; write P(S)=v_S c_S^2, v_i=4p_i(1-p_i).
Delta=sum (|S|-1)P(S), R=sum_{|S|>=3}(|S|-2)P(S).
Use 1/2<2^j|c|<=1, J1=ln4 sum_single Pj, Jhi=ln4 sum_high Pj,
L1=sum_single P ln(1/(2^j|c|)^2), and
Bstar=ln4(2Delta-R)-J1-ln2 L1. This is the SAME diminished original
account as A041/A045, with no renewal or change of reference.

## Exact uniform endpoint theorem

For every such m and unequal positive profile,

  (49/64)e2 <= Bstar/ln4 <= (2+s/6)e2,                       (1)
  |Bstar/ln4-2e2| <= 4s e2,                                (2)
  Jhi/ln4 >= 9/64.                                         (3)

In particular Bstar>0 and
Jhi/Bstar >= 9/[64(2+s/6)e2]. If all e_i=e, then
Bstar/ln4=m(m-1)e^2+O(m^3 e^3), with error bounded by (2).
Unlike a fixed-profile Taylor expansion, (1)-(2) allow arbitrary relative
rates and unbounded m whenever s<=1/8. As s tends to zero the relative
error in Bstar/(2 ln4 e2) is at most 2s.

## 1. Independent reconstruction of the admitted prime family

At rare counts 0,1,2,>=3 the core slices are respectively AND2, OR2,
OR2, constant positive. The gate is essential: a core is pivotal when
the other core is1 and all rare bits0; a rare bit is pivotal when exactly
one core is1 and all other rare bits0. It is nonsymmetric: two core bits
pass while two rare bits fail.

Any proper block A of size 2 through m+1 would have at most two cofactor
rows if it factored through one Boolean wire. Write k for its core count
and r for its rare count. For k=2 use inside core counts0,1,2 and outside
rare counts0,1; the rows are --,-+,++. For k=1 (so r>=1), use inside
assignments none, one rare, core plus one rare and outside core counts0,1;
the same three rows occur. For k=0,r<m use inside rare counts0,1,2 and
outside assignments one core, one rare; rows are --,+-,++. For k=0,r=m
use inside rare counts0,1,3 and outside core counts0,1, giving --,-+,++.
These cases exhaust every block. This proves disjoint physical-wire
primeness only; it says nothing about affine or overlapping primeness.

## 2. Reserve identity and its scalar bound

Let D_i=(F_+-F_-)/2, t_i=E D_i and d_i=E D_i^2. Monotonicity gives
d_i=t_i. For general Boolean signs the physical identity
2Delta-R=I-sum_single P=sum_i v_i(d_i-t_i^2) follows by grouping degrees.
Indeed I_i=v_i E D_i^2, by conditional Parseval on the other coordinates.
Here every t_i is in [7/16,1/2], so every singleton dyadic index is1.
Consequently

  Bstar/ln4 = sum_i v_i phi(t_i),
  phi(t)=t-2t^2+t^2 ln(2t).                               (4)

There is no omitted derivative sign credit because the gate is monotone.
For t in [3/8,1/2], set delta=1/2-t. Direct differentiation gives
phi(1/2)=0, phi'(1/2)=-1/2, phi''(t)=-1+2ln(2t).
The inequality ln x<=x-1 gives
phi'(t)<=1-5t+4t^2<=-5/16<-1/4 throughout this interval;
phi''<0 gives phi'(t)>=-1/2. Therefore

  delta/4 <= phi(t) <= delta/2.                            (5)

On the narrower interval [7/16,1/2], ln x>=1-1/x gives
|phi''(t)|<=9/7<2. Taylor's integral remainder therefore gives

  |phi(t)-delta/2|<=delta^2.                               (6)

Both logarithm inequalities follow by differentiating ln x-x+1 and
ln x-1+1/x, respectively; their equality point is x=1.

## 3. Exact pivotal probabilities and pair occupancy

Let K be the total rare count. Both core pivotal means equal
t_c=(1-Pr(K>=3))/2, so delta_c=Pr(K>=3)/2<=e3/2.
For rare bit i let q_r=Pr(K_other=r) and s_i=s-e_i. Then
t_i=q0/2+q2/4 and
delta_i=q1/2+q2/4+Pr(K_other>=3)/2.
Union bounds and the first Bonferroni inequality give

  (1-s)s_i/2 <= delta_i <= s_i/2,
  0 <= s_i/2-delta_i <= (3/4)e2_other.                     (7)

For the lower bound q1=sum_j e_j prod_{k!=i,j}(1-e_k)
is at least s_i(1-s). For the second bound,
s_i-Pr(K_other>=1)<=e2_other and q2<=e2_other.
These prove (7) without a common-bias assumption. They also show
t_i>=7/16, including the core coordinates since e3<=s^3/6<=s.

Apply (5) to (4). The core contribution is at most e3/2.
The rare contribution is at most sum_i e_i s_i=2e2, and at least
(1-s)^2 sum_i e_i s_i/2=(1-s)^2e2>=49e2/64.
Finally 3e3<=s e2 (expand s e2, retaining its nonnegative repeated-index
terms). This proves (1).

For (2), (6)-(7) give
|phi(t_i)-s_i/4| <= (3/8)e2_other+s_i^2/4.
After multiplying by 4e_i(1-e_i), comparison with e_i s_i costs at most
(3/2)e_i e2_other+e_i s_i^2+e_i^2 s_i.
Sum these: sum_i e_i e2_other=3e3 and
sum_i e_i(s_i^2+e_i s_i)=2s e2. The two core terms add at most e3/2.
Thus the total error is <=5e3+2s e2<=(11/3)s e2<=4s e2.
This is a finite inequality, with no exchange of a limit and an infinite sum.

The core pair coefficient is c12=(q0-q1-q2)/2 >=(1-2s)/2>=3/8
and <=1/2. Its dyadic index is1, its v12 is1, proving (3).

## 4. Degenerate controls and the unpaid original source

Allow zero rare probabilities only by deterministic contraction. With one
positive rare coordinate the contracted gate is Maj3 with two fair inputs:
every relevant pivotal mean equals1/2, so Bstar=0 exactly, while the high
bill is positive. With all rare probabilities zero the contracted gate is
fair AND2, with Jhi=ln4/4, Delta=1/4, Bstar=R=0. Formula (2) is consistent
with both cases; division by e2 is made only at the stated positive m-bit
interior profiles. Reflection of any rare sign moves its probability to
1-e_i without changing squared spectrum or reserve: the gate truth table
is reflected too, and monotone derivatives become one-sign derivatives.

For fixed m>=3 and e1=t, e2=...=em=t^L with L>1, (2) yields
Bstar/ln4=2(m-1)t^(L+1)(1+o(1)). The high-sector bill stays bounded below.
The diminished-source failure is therefore governed by pair occupancy,
not by total rarity. The core bill must be paid from an original account
which survives deterministic contraction. Neither this theorem nor the
reviewed prime obstruction supplies that account for arbitrary cores.
All existing imports, mantissas, genuine carries, S_tree, normalization,
ordinary KL and BOTH full terminal laws remain charged. Full FEI is OPEN.
