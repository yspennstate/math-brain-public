SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T17:14:11Z.
attacking: receiver-driver localization under arbitrary translated fragments; keep the whole driver law through the moving-fold average and quantify mass homogeneity before any fragment normalization.

# Early substantive checkpoint: mixed-budget moving-fold localization

Full QFORM remains OPEN. This checkpoint records a new subprobability/mixed-budget extension of account02/B14 r39 and a strict target-valid application.

Let nu be a finite measure on driver space with mass m, let beta(z) be a scalar statistic whose pushforward beta_#nu has a Lebesgue density bounded by L, and let W have a probability density f<=1. For nu-a.e. z let T_z be independent of W, with density q_z, and set K(z)=||q_z||_3. Assume S3:=int K(z)^3 dnu(z)<infinity. For arbitrary a in R define the subprobability output

Q_z = T_z + a W^2 + beta(z) W.

Claim proved below:

||p_Q^(nu)||_infinity <= 2^(4/3) (m L S3)^(1/3).      (A)

For a!=0, account02/B14 r39 gives conditionally
||p_{aW^2+bW}||_{3/2} <= |a|^(-1/3) H_f(-b/(2a))^(2/3),
H_f(x)=int |w-x|^(-1/2)f(w)dw.
Hence
||p_Q^(nu)||inf <= |a|^(-1/3) int K(z) H_f(-beta(z)/(2a))^(2/3)dnu(z).
Holder (3,3/2) gives S3^(1/3)[int H_f dmu_X]^(2/3), where mu_X is the pushforward of nu by -beta/(2a). It has mass m and density cap M=2|a|L. Bathtub rearrangement for a mass-m density capped by M gives
sup_w int|x-w|^(-1/2)dmu_X(x) <= 2sqrt(2)(mM)^(1/2).
Since int f=1,
int H_f dmu_X <= 2sqrt(2)(mM)^(1/2).
Substitution yields
|a|^(-1/3) S3^(1/3) * [2sqrt(2)(mM)^(1/2)]^(2/3)
=2^(4/3)(mLS3)^(1/3).

For a=0, Young gives ||p_{beta(z)W}||_{3/2}<=|beta(z)|^(-1/3). Holder yields
int K|beta|^(-1/3)dnu <= S3^(1/3)[int|beta|^(-1/2)dnu]^(2/3).
The same bathtub estimate on beta_#nu gives int|beta|^(-1/2)dnu <=2sqrt(2)(mL)^(1/2), producing the smaller constant 2(mLS3)^(1/3), so (A) holds for all a.

Fragment ledger: if nu=sum_j nu_j, with masses m_j, projection caps L_j and S_j=int K^3 dnu_j, then
sum_j ||p_Q^(nu_j)||inf <=2^(4/3) sum_j(m_j L_j S_j)^(1/3).
If L_j<=m_j L0 for every j, Holder implies
sum_j(m_j L_j S_j)^(1/3) <= L0^(1/3)(sum_j m_j)^(2/3)(sum_j S_j)^(1/3).
Thus for total mass one, any finite/countable fragmentation whose unnormalized driver projection cap scales linearly with fragment mass has exactly zero localization tax. Arbitrary fragment translations, separation, support diameter and moments do not appear.

Strict target family to be written fully in REPORT.md: independent cap-one U1,U2, product driver Z, receiver W, and arbitrary outside product vector Y,
Q=U1^2+U2^2+Z^T H Z+aW^2+2(v^T Z)W
  +2(l1^T Y)U1+2(l2^T Y)U2+2Z^T RY+2(s^T Y)W+Y^T GY,
with H,G symmetric and arbitrary, R,l1,l2,s arbitrary. Conditioning on Y=y and then viewing z as the moving-fold driver gives K(z)<=pi^(2/3) uniformly after completing squares in U1,U2, while beta(z)=2v^Tz+2s^Ty has density cap <=1/(sqrt(2)||v||_2) by the product-projection theorem. Therefore account02/B14 r39 plus (A) yields
||p_Q||inf <=2^(7/6)pi^(2/3)||v||_2^(-1/3).
If ||v||_2>=1, the active principal block I_2 direct_sum [[H,v],[v^T,a]] has at least three eigenvalues of modulus >=1: I_2 contributes two +1 eigenvalues, and the symmetric second block has operator norm at least ||v||_2. If that large eigenvalue is positive it supplies a third >=1; if negative it supplies one <=-1 in addition to the two +1 values. Hence the family is inside the exact owner target. Arbitrary outside couplings preserve the threshold count by principal-submatrix interlacing.

Dependency actually used: account02/B14 r39, canonical report yspennstate/math-open-problems@6b6cd1c3be8a9c23a3424593a38b0450acb61cfa, path proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T155625Z-account02-B14-QFORM-r39/REPORT.md.

Execution: WITHOUT_VERIFIED_BRAIN. No claim of full QFORM closure.
