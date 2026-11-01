SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T13:01:29Z.
attacking: general indefinite physical-pair curved kernel — interpolate the zero-diagonal and nonzero-diagonal hyperbola regimes without taking any fiber supremum.

# Early mathematical checkpoint

A direct product-coordinate calculation appears to remove the small-nonzero-diagonal discontinuity in the existing coordinate-hyperbola peel.

Let X,Y be independent with densities <=1 and

q(x,y)=a x^2+bxy+c y^2,

d:=sqrt(b^2-4ac)>0.

The target estimate is

p_q(u) <= 2^(7/4)*sqrt(3) * d^(-3/4) |u|^(-1/4),   u !=0.

The proof splits at max(|a|,|c|)=d/4.

1. If |c|>=d/4 (or symmetrically |a|>=d/4), condition on X=x. The two y-roots have derivative magnitude sqrt(d^2 x^2+4cu). Bathtub optimization of the resulting one-dimensional kernel gives either an asinh or arcosh expression, both <=sqrt(sqrt(d/|u|)); this yields constant 4 in the normalized d^(-3/4)|u|^(-1/4) scale.

2. If |a|,|c|<d/4, factor exactly

q=B(x+s y)(y+t x),
B=(b+sign(b)d)/2,
s=c/B,
t=a/B.

Then |s|,|t|<=2-sqrt(3), |B||1-st|=d. On the hyperbola zw=u/B with z=x+sy,w=y+tx, retain the original product density after the near-identity inverse map. Split |z|>=sqrt(|u/B|) and its complement, using z on the first piece and w=u/(Bz) on the second. Each inverse original coordinate is monotone and its Jacobian is bounded by (1+lambda)/(1-lambda)=sqrt(3), lambda=2-sqrt(3). Bathtub then gives

p_q(u) <= (4sqrt(3)/d) log(1+(1/sqrt(2))*sqrt(d/|u|)).

Since log(1+x)<=sqrt(x), this is <=2^(7/4)sqrt(3)d^(-3/4)|u|^(-1/4).

For an invertible indefinite symmetric physical pair B2, d=2sqrt(|det B2|), so after arbitrary affine completion the conditional pair density should satisfy

p(t) <= 2sqrt(3)|det B2|^(-3/8)|t-t0|^(-1/4).

Averaging this conditional bound against the Schur remainder R gives the weighted receiver

||p_Q||inf <=2sqrt(3)|det B2|^(-3/8) H_(1/4)(R),
H_(1/4)(R):=sup_t E|R-t|^(-1/4).

This would extend the exact zero-diagonal coordinate-hyperbola peel to every invertible indefinite physical pair, retaining curvature and probability weight before any supremum. Full proof and the exact-rank-three application are being written next. Full QFORM remains OPEN.
