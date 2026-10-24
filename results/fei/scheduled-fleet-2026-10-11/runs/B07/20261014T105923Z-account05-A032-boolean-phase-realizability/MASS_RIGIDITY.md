# Product frequency branches of an actual Boolean function are necessarily fair

For every Boolean g(z,y) on a uniform cube, suppose each positive law of S_Y
conditioned on S_z=b is a coordinate product (deterministic coordinates allowed,
arbitrary Fourier signs). Then each such law has ONLY fair varying marginals.
If both branches are positive their masses equal 1/2. Consequently H(g)<=2I(g),
sharply, in every dimension. This closes the nonfair/unequal-mass extension of
A079's fair-branch endpoint by an impossibility certificate, not an estimate.

## Primitive norm admission for a ternary physical row

Set u_b(y)=(g(+1,y)+(-1)^b g(-1,y))/2. These rows take values 0,+1,-1,
and u_0^2+u_1^2=1 pointwise. Their masses are w_b=E u_b^2.
Let u be any nonzero ternary row whose normalized squared spectrum is product.
Remove deterministic frequency characters and unused coordinates. This preserves
physical heights and w. On the reduced d-dimensional cube all raw Walsh entries
W_s are nonzero integers. Product magnitudes have the form

    |W_s|=c product_i a_i^(1-s_i) b_i^s_i,

where a_i,b_i are coprime positive integers. Ratios are rational because the W_s
are integers. Coprimality implies the tensor products have gcd1, so c is integer.
Any odd divisor of c divides every physical value after inverse Walsh division
by 2^d. A nonzero ternary row has a value +/-1, so c is a power of two.

Write k=sum_y u(y)^2, P=2^d. Parseval gives

    P k=c^2 product_i(a_i^2+b_i^2).

For an opposite-parity coprime pair, its sum of squares is odd and 1 modulo4.
For two odd entries, its sum of squares is 2 modulo8, so its odd part is 1
modulo4. Thus EVERY primitive sum has odd part 1 modulo4, and so

    oddpart(k)=product_i oddpart(a_i^2+b_i^2)=1 modulo4.       (1)

Since w=k/P, its reduced dyadic numerator is also 1 modulo4. A nonfair primitive
pair has odd part at least5: opposite parity gives sum>=5; two odd entries
give sum/2>=5 unless they are (1,1). Therefore oddpart(k)=1 forces every
varying marginal to be fair. Fixed-one frequency characters only add influence.

## Complementary-mass exact certificate

Suppose both rows are positive. Since w_0+w_1=1, write w_b=r_b/2^a_b with
r_b positive odd and r_b=1 modulo4; a_b>=1.
If a_0=a_1=a, then r_0+r_1=2^a. The left side is 2 modulo4, so a=1,
and positivity forces r_0=r_1=1.
If a_0>a_1, then a_0>=2 and

    r_0+2^(a_0-a_1) r_1=2^a_0.

The left side is 3 modulo4 when the exponent difference is1, and 1 modulo4
when it is at least2. The right side is0 modulo4. Contradiction. The other
ordering is symmetric. Hence w_0=w_1=1/2, their odd numerators are1, and
(1) forces both branches to be fair product laws. If only one row is positive
its mass is1, and the same odd-part argument forces a fair product law.
This proof rejects every possible phase assignment and works in arbitrary d.

## Full entropy and the original physical influence

For positive branches write m_b for the fair count and a_b for the mean physical
Y-frequency degree. Each a_b>=m_b/2. If both branches are positive,

    H(g)=1+(m_0+m_1)/2,
    I(g)=1/2+(a_0+a_1)/2 >= H(g)/2.

If one row is zero then H(g)=m and I(g)=b+a>=m/2. Thus H<=2I in every case.
All entropy terms are retained; no Renyi entropy bound or separate energy account
is substituted. The nonflat A079 four-bit fixture attains equality H=3,I=3/2.
Tensor admission with a fresh Boolean data seed forces that seed spectrum to be
product. Its height-one norm has w=1, so it too is fair product; its full entropy
and influence add and are paid at2. No closure under arbitrary seeds is asserted.

## Exact frontier

Standalone ternary product rows can be nonfair (the saved catalogue contains3584
examples on four bits, all with N=1,m=3 and mass5/8). Their complementary mass
is3/8, whose odd numerator is3 modulo4, so their physical complements CANNOT
also have product spectrum, irrespective of signs or added dimensions preserving
these masses. The out/ternary_obstruction.json witness checks an actual Boolean
five-bit assembly with one product branch and one nonproduct branch.

The first unsupported universal line is paying a Boolean split when at least one
conditional spectrum is nonproduct, or transferring this argument to general
height-two address rows: their half-integral frequency branches need not have
primitive scale a power of two, and the complementary mass congruence is not
proved there. In particular this theorem does not close C019 or full FEI.

## Booleanity and vacuous-embedding guards

The normalized non-Boolean vector psi=(sqrt255+y)/16, independent of z, has one
positive product frequency branch with marginal1/256, H=h2(1/256)>8/256 and
I=1/256. It violates H<=2I; its inverse values are not ternary or Boolean.
Thus the result is not a generic statement about normalized probability laws.
For a two-bit point defect each branch has just one data coordinate, so the
product hypothesis is vacuous; the actual table [-1,1,1,1] gives H=2,I=1 and
attains2. For the three-bit point defect, splitting off one frequency coordinate
gives a main ternary row [0,1,1,1], with Walsh[3,-1,-1,-1]; its squared two-bit
array[9,1,1,1] fails9*1=1*1. It is excluded by this one-frequency product-branch
hypothesis. It remains admitted and sharp under A034's DIFFERENT two-address
product-row hypothesis; no contradiction with that benchmark is asserted.
