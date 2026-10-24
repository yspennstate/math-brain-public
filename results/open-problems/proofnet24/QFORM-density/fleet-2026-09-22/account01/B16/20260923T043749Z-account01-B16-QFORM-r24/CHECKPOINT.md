SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T04:37:49Z.
attacking: determinant-only physical-triple smoothing by an algebraic pivot/cross-transverse dichotomy.

# Early substantive checkpoint

Status: supporting calculation in progress; full QFORM remains OPEN; continuity not claimed.

Let

B = [[a,b,c],[b,d,e],[c,e,f]],   Delta=det B,   D=|Delta|>0.

For pivot i define C_i as the complementary 2x2 receiver block, u_i as its cross vector, and

P_i = |u_i^T adj(C_i) u_i|.

After an orthogonal rotation inside the receiver plane taking u_i to (beta,0), this is exactly the cross-transverse resource beta^2 |(C_i')_22| used in `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v2`.

Normalize first to D=1. Put

x=f b^2, y=d c^2, z=a e^2, T=bce, h=adf,
q_1=x+y-2T, q_2=x+z-2T, q_3=y+z-2T,

so P_i=|q_i| and

Delta=h+2T-(x+y+z).

The exact identities

x-T=(q_1+q_2-q_3)/2,
y-T=(q_1+q_3-q_2)/2,
z-T=(q_2+q_3-q_1)/2,
T=h-Delta-(q_1+q_2+q_3)/2,
xyz=h T^2

imply the following dichotomy. If simultaneously

|a|,|d|,|f|<2/9 and P_1,P_2,P_3<2/9,

then |h|<8/729 and

|T| > 1-8/729-1/3 = 478/729.

Hence

|x|,|y|,|z| > 478/729-1/3 = 235/729,

so

|xyz| > (235/729)^3 = 12977875/387420489.

But also

|T| < 1+8/729+1/3 = 980/729,

and therefore, from xyz=hT^2,

|xyz| < (8/729)(980/729)^2 = 7683200/387420489,

contradiction. Thus for |det B|=1 some pivot i obeys

|B_ii| >= 2/9   OR   P_i >= 2/9.

Scaling back gives

|B_ii| >= (2/9) D^(1/3)   OR   P_i >= (2/9)D.

Planned analytic payment:

1. Large scalar pivot. Complete the square in the corresponding ORIGINAL independent scalar. The receiver Schur determinant has magnitude D/|B_ii|. Apply the completed affine rank-two half-Riesz theorem

sup_t E|R-t|^(-1/2) <=128 |det S|^(-1/4)

to obtain

||p_Q||inf <=128 (|B_ii|D)^(-1/4)
 <=128(9/2)^(1/4)D^(-1/3) <187 D^(-1/3).

2. Large cross-transverse resource. Use the same ORIGINAL scalar and the remaining two ORIGINAL independent variables as the receiver (joint density cap 1). The completed cross-transverse theorem gives

||p_Q||inf <=3*2^(8/3)(D P_i)^(-1/6)
 <=3*2^(8/3)(9/2)^(1/6)D^(-1/3) <25D^(-1/3).

Therefore an invertible physical 3x3 core should admit a determinant-only density certificate <187 D^(-1/3), uniformly in all affine terms produced by conditioning outside. This would improve localized certification by removing any condition-number requirement on the selected 3x3 block. The calculation still needs a final scope audit, source pinning, and full-ambient conditioning write-up before promotion.
