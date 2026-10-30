# Nonuniform thinning: keep the total mass and the multi-root correction apart

Natural logarithms are used until conversion to bits. For a finite nonempty vector x (dimension N>=1) of strictly positive root activities define A_x=sum_i x_i, D_x=prod_i(1+x_i)-1 and Delta(x)=ln(D_x/A_x). For 0<y_i<=x_i put L=sum_i(x_i-y_i). Both references are fixed before any Fourier set is sampled. These are the ORIGINAL conditioned nonempty-product root priors, not forest posteriors chosen after observing a set.

We prove the dimension-free inequalities

    -L <= ln(D_y/D_x)-ln(A_y/A_x) <=0,                 (1)
    |KL(Q_y||Q_x)-KL(r_y||r_x)| <=L,                  (2)

where Q_x(R)=prod_(i in R)x_i/D_x for nonempty R, and r_x(i)=x_i/A_x. KL in (2) is in nats. Dividing both sides by ln2 converts it to bits. Positive activities and finite vectors make every denominator and logarithm legitimate. The singleton N=1 endpoint has Delta=0 and both KLs equal zero.

## A rational derivative bound

For one coordinate write a=x_i, B=sum_(j!=i)x_j and E=prod_(j!=i)(1+x_j), so A=a+B, D=(1+a)E-1. Direct differentiation gives

    partial_i Delta=(AE-D)/(AD),
    AE-D=(B-1)E+1.

The numerator is nonnegative: the finite union bound gives 1-1/E<=sum_(j!=i)x_j/(1+x_j)<=B. This union bound follows inductively from 1-(1-u)(1-v)=u+v-uv<=u+v for u,v in [0,1]; no independence or limiting product is assumed. The numerator is also <=AD, because

    (A+1)D-AE=E[1+(A+1)a]-(A+1)>=0.

Indeed E>=1+B, and E[1+(A+1)a]>=1+B+a=1+A. Thus

    0<=partial_i Delta<=1.                            (3)

Integrate (3) on the line segment from y to x. It stays in the positive orthant; its coordinate increments are nonnegative and sum to L. This proves 0<=Delta(x)-Delta(y)<=L and hence (1). This proof retains the signed remainder: it does not replace it by an unsigned root refund. For common thinning y=t x, the exact formula becomes

    -(1-t)A_x <= ln[D_(t x)/(t D_x)] <=0.

At rare scale x=epsilon a, y=epsilon b, the error in (1) is at most epsilon sum(a-b), uniformly in the number of roots.

## The same conditioned root law, with the gate-name term still present

The exact root inclusion marginal under Q_y is

    mu_i(y)=y_i prod_(j!=i)(1+y_j)/D_y,
    mu_i(y)-r_y(i)=y_i partial_i Delta(y) in [0,y_i].   (4)

Since Q_y(R)/Q_x(R)=(D_x/D_y)prod_(i in R)(y_i/x_i),

    KL(Q_y||Q_x)=ln(D_x/D_y)+sum_i mu_i(y) ln(y_i/x_i),
    KL(r_y||r_x)=ln(A_x/A_y)+sum_i r_y(i) ln(y_i/x_i).

Subtracting shows that the difference in (2) is EXACTLY

    Delta(x)-Delta(y)
             +sum_i[mu_i(y)-r_y(i)] ln(y_i/x_i).       (5)

The first term is in [0,L]; the second is nonpositive and at least -L. To check the latter, set t_i=y_i/x_i in (0,1]. Then

    sum_i y_i ln(1/t_i)=sum_i x_i t_i ln(1/t_i)
                       <=sum_i x_i(1-t_i)=L,

using ln u<=u-1 at u=1/t_i. Equation (4) proves the lower estimate. Hence (5) lies in [-L,L], proving (2). Both signs of (5) occur on the frozen exact grid; neither contribution may be silently dropped. The bound controls only the multi-root remainder. It does NOT pay KL(r_y||r_x).

In particular, for positive fixed vectors 0<b<=a,

    |KL_bits(Q_(epsilon b)||Q_(epsilon a))
                    -KL_bits(b/sum b || a/sum a)|
          <=epsilon sum(a-b)/ln2.                    (6)

This is an explicit rare-root convergence certificate, not a passage of a limit through an unspecified witness posterior. All common log(epsilon) terms cancel in the exact formulas before any inequality. Gate-name mismatch survives in the singleton KL, which can be large.

## Pay the remainder from the physical implicant packing

Let f be any nonconstant uniform sign Boolean function, q=Pr(f=-1), v=4q(1-q), with a finite nonempty signed conjunction implicant table of f=+1, actual rarities pi_e=2^-w_e and w_e>=1. Fix positive packing-feasible old weights lambda_e and fixed thinned weights 0<lambda'_e<=lambda_e. Set x_e=lambda_e pi_e, y_e=lambda'_e pi_e. A008's local physical inequality, independently reconstructed in REVIEW_A008.md, gives

    pi_e <= a_(w_e)/(2q) sum_(i in R_e)Inf_i(f),
    a_w=(1-2^-w)/w.

Consequently the EXACT lost activity L satisfies

    v L <=2(1-q)sum_i Inf_i(f) d_i,
    d_i=sum_(e:i in R_e)(lambda_e-lambda'_e)a_(w_e).     (7)

For k=min w_e, d_i<=a_k by the SAME original packing rows. Equations (1),(2),(7) pay both signed-normalizer and root-KL multi-root errors by

    2(1-q)/ln2 sum_i Inf_i(f)d_i
             <=[2a_k(1-q)/ln2]I(f) bits.             (8)

No new weight vector is optimized after a Fourier set. No influence debit is reused: (8) gives alternative bounds on two related remainders; it does not authorize adding their budgets. The function, implicant widths/signs and reference gate table remain fixed. Only a specified coordinatewise thinning is compared.

Equation (8) is a universal root-component statement, not an FEI proof. The conditional prior Q_y differs from the actual Fourier-set forest posterior eta_T. Arbitrary posterior root/label costs are not controlled by (2). RETUNING_OBSTRUCTION.md gives actual overlapping prime references for which the unpaid singleton term diverges while the function stays fixed, every activity tends to zero, and all packing constraints hold. Thus the first unsupported line is a COMPLETE fixed-reference occupation/name payment, not another multi-root normalization bound.
