SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T12:13:57Z.
attacking: product Fourier rearrangement via global compatibility-Hellinger couplings of third-volume row bases; test whether the preceding six-row local Hellinger currency can be forced or must be replaced by an aggregate mechanism.

# Early substantive checkpoint


## New mechanism under derivation

For a physical cross block M=A[I,J], write

  a_S = sum_{|T|=3} det(M[S,T])^2

for supported physical row triples S. Let E be any symmetric compatibility relation on supported row triples. Define

  B_E = sum_{(S,T) in E} sqrt(a_S a_T),
  Pi(S,T) = sqrt(a_S a_T)/B_E on E,

and let mu be either marginal of the symmetric pair law Pi. If

  beta_i = Pi(i in S intersect T),  beta_* = max_i beta_i,

then exact inclusion-exclusion gives

  alpha_i := mu(i in S) <= (1+beta_i)/2.

Hence beta_*<1/2 puts mu into the weighted third-volume Fourier gate with q=1+beta_*<3/2. Moreover

  H(Pi)=log B_E - sum_S mu(S) log a_S,

so chain rule H(Pi)=H(mu)+H(T|S) gives the exact determinant/entropy currency

  G(mu)=exp(H(mu)+sum mu log a_S)=B_E exp(-H_Pi(T|S)).

After the standard conditional column lift proportional to determinant squares, the full minor law has the same currency. Therefore the sharp weighted product-Fourier theorem should give

  ||p_Q||_inf <= [3e/((1-2 beta_*) sqrt(1+beta_*))]
                 [B_E exp(-H(T|S))]^(-1/6),

with continuous C_0 density in that theorem's scope. This strictly generalizes the prior six-row complement-Hellinger construction: a complement matching has beta_*=0 and H(T|S)=0.

## Essential obstruction found early

The hoped-for next step from the preceding run — force one six-row complement-Hellinger currency C_R >= c0 from the bare spectral target — is false as a local-extraction mechanism, even uniformly over all original-coordinate cuts.

For k>=2 let U_k have k copies of e_1/sqrt(k), k copies of e_2/sqrt(k), k copies of e_3/sqrt(k), let V=I_3-(2/3)11^T, and M_k=U_k V^T. Then M_k has singular values 1,1,1 and every physical cross coefficient is nonzero. For A_k=[[0,M_k],[M_k^T,0]], the spectrum is +1,-1 each three times, plus zeros: this is target-valid and genuinely non-diagonal/indefinite.

For the natural left-to-right cut, nonzero row-base volumes are exactly a_S=1/k^3 for triples choosing one row from each of the three groups. A six-row set has positive complement currency iff it contains exactly two rows from each group, in which case C_R=8/k^3. For every other six-row set C_R=0.

For an arbitrary original-coordinate cut, if r of the three right-bank coordinates lie on the row side and 0<r<3, the cross block is a rectangular direct sum of rank at most 3-r and rank at most r; every rank-three row basis must contain all r right-bank row coordinates, so there cannot be two disjoint row bases and every six-row complement currency is zero. If r=3 there are only three active right-bank rows, again currency zero. Thus the only possible positive six-row currency occurs in the r=0 orientation above, and

  sup over all cuts and all six-row R of C_R <= 8/k^3 -> 0.

So no universal single-six-row Hellinger lower bound can follow from the three-large-eigenvalue hypothesis. This is NOT a counterexample to QFORM.

The new global compatibility coupling repairs this family: take E to be all ordered disjoint row-base pairs. There are k^3 bases, every base has (k-1)^3 compatible bases, B_E=(k-1)^3, H(T|S)=3 log(k-1), beta_*=0, hence G=1 and the sharp q=1 theorem gives ||p_Q||_inf <=3e, uniformly in k. This is the intended replacement for local packet extraction.

Partner to apply in final report: fleet02/B04 run fleet02-B04-20260923T111930Z-qform, theorem QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1, source math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013. On the dense 4x4 Householder cross block M_4=I_4-(1/2)11^T, strict h<3/4 support is impossible and Z=E3=4, so the partner theorem gives the actual bound ||p_Q||_inf<=6. This is exactly the beta_*=1/2 endpoint of the overlap-coupling mechanism.

Status: supporting theorem/correction in derivation; full target OPEN; continuity only in completed Fourier branches. Execution memory status WITHOUT_VERIFIED_BRAIN.
