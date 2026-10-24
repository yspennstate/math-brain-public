# Exact-rank-three matroid cross-cut classification

Proof: https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T190200Z-rank3-matroid-crosscut/REPORT.md
Math commit: f3ce3b46bce7ff4ca6072f960167051a055d427a.

For exact-rank-three A=U Lambda U^T, a physical rank-three crossing exists iff the row matroid of U has two disjoint bases. Edmonds' dual matroid partition theorem says failure implies either at most five active rows, all but three rows in a rank-one flat, or all but one row in a rank-two flat. Under N3(1/64) no-pivot and s3(A)>=1, the first two options violate spectral norm bounds c+4 sqrt(c+c^2)<1 and c+2 sqrt(c+c^2)<1. Therefore a unique exceptional original physical hub h has light block B of rank at most two.

Since e_h lies in range(A), hub coupling norm t>=sqrt(1-c^2)>0.9998779. The zero-hub compression has transverse rank one with coefficient |lambda|>=1, and rank B<=2 forces perpendicular shear leakage to vanish. At a=A_hh=0, the existing pure-hub theorem pays density <5.361. At nonzero |a|<c, the remaining analytic endpoint is Q=a X_h^2+2t X_h L+lambda(V-v_c(L))^2+F(L), with L,V two orthonormal projections of the original product light source.

This theorem is only exact rank three and only for cuts whose cross rank never reaches three. It does not resolve quantitative rank-three crosscuts, arbitrary additional spectrum, or the small nonzero hub square for rough inputs.

Further spectral constraint in small-a endpoint: let beta'=beta-u_v^2/lambda and H=[[a,t],[t,beta']]. Its inverse is a principal 2x2 block of the inverse of the exact nonzero 3x3 quadratic matrix M, hence ||H^{-1}||<=1. Since |a|<1, H has one eigenvalue >=1 and another <=-1. Therefore t^2>=1+a beta'+|beta'+a|. This is a necessary matrix inequality, not a density receiver. Updated math commit: 82df0db13b506b8883a0f8874be1173258061fb8.
