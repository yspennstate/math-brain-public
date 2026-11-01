# Small physical hub square: a uniform three-variable slab bound

Status: PROVED TARGET-LEVEL BRANCH. This closes the exact-rank-three no-pivot branch with no rank-three original-coordinate cross cut, using the companion matroid classification. Full QFORM remains OPEN for quantitative rank-three crossing and arbitrary additional spectrum.

## The analytic theorem

Let H be independent of a real pair (L,V), with density f_H<=1 and joint density g_(L,V)<=M. Let
Q=aH^2+2tHL+beta L^2+lambda V^2,
where c=1/64, |a|<c, t>=sqrt(1-c^2), |lambda|>=1, and the invertible matrix K=[[a,t],[t,beta]] satisfies ||K^(-1)||op<=1. Then, for every interval J of length delta,
P{Q in J} <= (1+32M) delta. In particular M<=2 implies ||p_Q||infinity<65. Arbitrary affine terms in H,L,V are allowed after a separate deterministic translation of H and (L,V), since K direct_sum [lambda] is invertible. No support or moment assumption is made and L,V need not be independent.

## Four-region proof

Put u=ah+t l, D=t^2-a beta. The inverse of K is -D^(-1)[[beta,-t],[-t,a]]. Because |a|<1 and ||K^(-1)||<=1, K has one eigenvalue >=1 and another <=-1. Thus D>0, D>=t, and D>=|beta|. Partition (h,l,v) by the following disjoint conditions.

1. |u|>=1. For fixed (l,v), |partial_h Q|=2|u|>=2. The quadratic h-map has at most two monotone branches; total h-length mapping to J is <=delta. Integrating f_H<=1 and int g=1 gives contribution <=delta.

2. |u|<1, |v|>=1. For fixed (h,l), |partial_v Q|=2|lambda v|>=2; at most two monotone branches map into J, of total length <=delta. For fixed h, |u|<1 restricts l to length 2/t. Since g<=M and int f_H=1, contribution <=2M delta/t.

3. |u|<1, |v|<1, |h|>=2. Solve l=(u-ah)/t. Then
|partial_l Q|/2 = |(D/t)h+(beta/t)u|
 >=(D/t)(|h|-|u|)>=1.
For fixed (h,v), the eligible l form an interval, the derivative has fixed sign, and its preimage of J has length <=delta/2 (we use <=delta). Integrate the v strip of length 2, the cap g<=M, and the probability density f_H: contribution <=2M delta.

4. Remaining region |h|<2, |v|<1, |u|<1. Here
|l|<(1+2c)/sqrt(1-c^2)<1.032,
so (h,l,v) lies in a Euclidean ball of radius R=2.47. The source joint density is <=M. Let Z be Gaussian N(0,R^2 I_3). Its density throughout this ball is at least (2 pi R^2)^(-3/2) exp(-1/2). The three eigenvalues of K direct_sum [lambda] all have absolute value >=1, hence the characteristic function of Z^T (K direct_sum [lambda]) Z is bounded by (1+4R^4 omega^2)^(-3/4). Fourier inversion gives Gaussian quadratic density at most
B(1/2,1/4)/(4 pi R^2)
 = Gamma(1/4)/(4 sqrt(pi) Gamma(3/4) R^2).
Gaussian domination thus bounds the Lebesgue volume of the ball intersected with Q^(-1)(J) by
(2 pi)^(3/2) exp(1/2) [Gamma(1/4)/(4 sqrt(pi) Gamma(3/4))] R delta
 <27 delta.
The fourth contribution is <27M delta.

Summing yields P{Q in J} <=[1+(2/t+29)M]delta <(1+32M)delta, since t>0.9998. This interval bound proves existence of an essentially bounded density.

## Application to the exact rank-three survivor

The companion matroid proof at
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T190200Z-rank3-matroid-crosscut/REPORT.md
shows that every exact-rank-three A with s3(A)>=1, no c-pivot, and no physical rank-three cross cut has a physical hub X_h and orthonormal light projections (L,V0) with
Q=aX_h^2+2tX_h L+beta' L^2+lambda (V0+(u_v/lambda)L)^2,
|a|<c, t>=sqrt(1-c^2), |lambda|>=1.
The light pair (L,V0) is a projection of the original product vector and has joint density <=2. The shear V=V0+(u_v/lambda)L has determinant one, so retains the cap. The nonzero 3x3 matrix M3 of A has all singular values >=1; the inverse of K=[[a,t],[t,beta']] is a principal 2x2 block of M3^(-1), so ||K^(-1)||<=1. The physical X_h is independent of the light pair. The theorem therefore gives ||p_Q||infinity<65, including the previously unpaid nonzero hub-square endpoint.

This proof keeps the source in original-coordinate product form up to a two-dimensional joint projection, which is used only through its valid unconditional density cap. It does not delete a small quadratic term or assert post-rotation independence.