# General three-variable form of the small-hub coarea receiver

Status: PROVED GENERALIZATION of REPORT.md in this directory; full unrestricted QFORM still OPEN.

Let H have a cap-one probability density and let (L0,V0) have an arbitrary joint density bounded by M, independent of H. Let T be a real symmetric 3x3 matrix on (H,L0,V0), with s3(T)>=1 and |T_HH|<1/64. Then the quadratic (H,L0,V0)^T T (H,L0,V0) has density at most 1+32M. The same bound permits arbitrary deterministic affine terms.

Proof. Orthogonally rotate only the two light variables, leaving their joint density cap and independence from H intact, to make the hub row of T equal (a,t,0):
T=[[a,t,0],[t,b,gamma],[0,gamma,lambda]].
Since ||T e_H||>=1 and |a|<1, t>=sqrt(1-a^2)>0. Take z=(-gamma/t,0,1). Then Tz=(-a gamma/t,0,lambda). Since ||Tz||>=||z||,
lambda^2>=1+(1-a^2)gamma^2/t^2>=1.
Shear V=V0+(gamma/lambda)L0, L=L0. The shear has determinant one, so the joint light density stays <=M, and the quadratic becomes
a H^2+2tHL+(b-gamma^2/lambda)L^2+lambda V^2.
Its 2x2 block K=[[a,t],[t,b-gamma^2/lambda]] is the Schur complement of lambda in T. The leading 2x2 principal block of T^(-1) equals K^(-1), hence ||K^(-1)||<=||T^(-1)||<=1. All hypotheses of the four-region receiver in REPORT.md hold, with t>=sqrt(1-(1/64)^2), giving the claim. As T invertible, any deterministic affine term can be removed by separate translations of H and the light pair, preserving their density caps and independence.

The joint light source need not be a product law once its valid unconditional two-dimensional density cap is established. In the QFORM matroid survivor it is the orthonormal two-dimensional projection of the original product light coordinates, so M<=2. This generalization does not treat an exact-rank-three A whose light row span has dimension three, nor matrices with arbitrary additional spectrum.