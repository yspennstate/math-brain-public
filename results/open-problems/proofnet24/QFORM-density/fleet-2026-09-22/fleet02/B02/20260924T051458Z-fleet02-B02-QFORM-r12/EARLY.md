# B02 early calculation — scalar-square L3 times exact-rank-two crossing L3/2

Programme: QFORM-DENSITY-3EIG-20260922. Full rough-product target remains open.

The first unpaid implication inherited from the latest B02 work is `QFORM-OVERLAP1-TWOPAIRS-TWOSIDED-CURVATURE-L1-v1`. I change mechanism from per-pair L2: combine one literal independent physical square in L3_t with the exact-rank-two crossing theorem in L3/2_t. This retains arbitrary same-bank curvature on both crossing banks.

## 1. Sharp-HY scalar chirp improvement

Let X have density f<=1 and let Y=(X+c)^2. Its density g on (0,infinity) satisfies int g=1 and g(y)<=y^(-1/2). Hence

    int g^(3/2) <= int g(y)y^(-1/4)dy <= 2sqrt(2).

The last inequality is the bathtub extremum under 0<=g<=y^(-1/2), int g=1: fill the cap on [0,1/4]. Therefore ||g||_(3/2)<=2. The reviewed sharp Hausdorff-Young inequality at p=3/2,q=3, with Fourier convention hat g(t)=int exp(ity)g(y)dy, gives

    ||hat g||_3 <= pi^(1/3) 3^(1/6) ||g||_(3/2),

so uniformly in c

    boxed: int_R |E exp(it(X+c)^2)|^3 dt <= 8 pi sqrt(3).

For coefficient a!=0 this becomes 8 pi sqrt(3)/|a|.

## 2. Exact rank-two crossing gives an L3/2 norm

Use the completed arbitrary-internal-function crossing theorem from `NEW_PROJECTED_CROSSING.md`. For independent original-coordinate banks X,Y, an exact-rank-two physical cross matrix B with nonzero singular values s1,s2, projected bank density caps M_X,M_Y, and arbitrary measurable internal phases F(X),G(Y),

    |phi_R(t)| <= min(1, K/|t|),
    K = pi (M_X M_Y)^(1/2) (s1 s2)^(-1/2).

Therefore

    ||phi_R||_(3/2)^(3/2) <= 6K,
    ||phi_R||_(3/2) <= (6K)^(2/3).

## 3. New receiver

If a literal original coordinate H is disjoint from the two crossing banks and, after conditioning all outside coordinates, has no quadratic cross coupling to either active bank, while its coefficient a is nonzero, then the conditional characteristic function factors as a shifted-square factor times the rank-two-crossing factor. Holder (3,3/2) gives

    boxed:
    int |phi_Q(t)|dt
    <= pi 2^(5/3) 3^(5/6)
       [ M_X M_Y / ( |a| s1 s2 ) ]^(1/3).

Hence

    boxed:
    ||p_Q||_infinity
    <= 2^(2/3) 3^(5/6)
       [ M_X M_Y / ( |a| s1 s2 ) ]^(1/3)
    < 3.965407 [ M_X M_Y / ( |a| s1 s2 ) ]^(1/3).

This is genuine unweighted Fourier L1 and permits arbitrary same-bank quadratic curvature on BOTH crossing banks. For two literal two-coordinate banks M_X=M_Y=1.

## 4. Exact-target two-sided-curvature stress family

On five original coordinates (h,u1,u2,v1,v2), take

    A_* = [1] direct_sum [[I2,I2],[I2,I2]].

Then spec(A_*)={2,2,1,0,0}, so the exact target is satisfied. The quadratic form is

    h^2 + (u1+v1)^2 + (u2+v2)^2.

All disjoint physical cross blocks have rank at most two, hence every E3 and E5 currency is exactly zero. Nevertheless the new receiver with a=1, B=I2 and M_X=M_Y=1 gives

    int |phi_Q| <= pi 2^(5/3)3^(5/6) <24.915384,
    ||p_Q||_infinity <3.965407.

This pays a genuine two-sided-curvature endpoint while giving an exact-target obstruction to D'/D5-only structural closure.

## 5. Designated-partner r45 equation

For the r45 partition L={h,u1,u2}, R={v1,v2}, the crossing has x1*x2=1 and top-two left carrier span{u1,u2}. The same-side block D=I3 has transverse part exactly the h diagonal, so r45's mixed 2+1 sum satisfies T>=1. Directly, the only nonzero determinant in that sum is

    det A[{h,u1,u2},{h,v1,v2}]=1,

hence T=1 and the entire certificate lies in the overlap-one branch. Thus this endpoint is not an artefact of a loose fork: overlap-one curvature is literally present while all disjoint E3/E5 currencies vanish.

Next: determine whether the same L3 x L3/2 mechanism can survive a carrier-aligned nonzero hub coupling without factoring the square from the crossing. The grouped-hub theorem pays transverse coupling; the remaining obstruction is precisely aligned coupling, where projection consumes one of the two crossing directions.
