# Rank-one planar cross receiver with arbitrary local phases

Date: 2026-09-23. **Proved scoped theorem.**

Let H have independent probability density at most one. Let A=(L_A,V_A) and B=(L_B,V_B) be independent planar random vectors with probability densities bounded by M_A,M_B. Let R_H,R_A,R_B be arbitrary real measurable functions of their indicated independent sources. Suppose C=[[a,b],[c,2]] has determinant zero. Then
\[
Q=2H(L_A+L_B)+A^T C B+R_H(H)+R_A(A)+R_B(B)
\]
has a bounded continuous density satisfying
\[
\|p_Q\|_\infty\le 3(M_A M_B)^{1/3},
\]
uniformly in C and all local phases.

**Proof.** Since det C=0, a=bc/2. The bankwise determinant-one shears
\(V_A'=V_A+(b/2)L_A\), \(V_B'=V_B+(c/2)L_B\)
preserve bank independence and density caps, and give \(A^TCB=2V_A'V_B'\). Write
\(2V_A'V_B'=(V_A'+V_B')^2-(V_A')^2-(V_B')^2\)
and absorb the last two terms into the local bank phases. We reduce to
\(Q=2HL+V^2+\widetilde R_H+\widetilde R_A+\widetilde R_B\),
with (L,V) the sum of the sheared banks.

At each t, the complex bank densities a_t,b_t incorporating the local phases satisfy |a_t|≤a, |b_t|≤b and L2 norms at most √M_A, √M_B. Their convolution F_t has
\[
\|\widehat F_t\|_1
\le\|\widehat a_t\|_2\|\widehat b_t\|_2
\le(2\pi)^2\sqrt{M_AM_B}
\]
by planar Plancherel. With \(\widehat g(\xi)=\int e^{-i\xi\cdot x}g(x)dx\), planar Fourier inversion, a Gaussian cutoff, the V-Fresnel integral and the physical capped H integral give
\[
|\phi_Q(t)|\le \|\widehat F_t\|_1(4\sqrt\pi)^{-1}|t|^{-3/2}
\le\pi^{3/2}\sqrt{M_AM_B}|t|^{-3/2}.
\]
The same estimate permits arbitrary R_H because its phase has modulus one. Integrating this bound against the trivial |φ_Q|≤1 yields exactly \(3(M_AM_B)^{1/3}\); φ_Q∈L1 gives a continuous density. Details of the Gaussian/Fresnel step are in the [finite-P Fourier receiver](https://github.com/yspennstate/math-open-problems/blob/44cd716d0814a830c27feeba380a03f62da38c6b/proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/REPORT.md).

The nonsingular case det C≠0 retains a cross term \(dL_A L_B\), \(d=a-bc/2\), after the shears. This proof does not handle it. Allowing an arbitrary hub quadratic phase there can [collapse the whole form to rank two](https://github.com/yspennstate/math-open-problems/blob/b46763cc9dc7f66a66f146795176bf4f774438f6/proofnet24/QFORM-density/interactive/20260923T211000Z-cross-local-phase-obstruction/REPORT.md), producing an unbounded density; the exactly linear hub case remains open. The rank-two construction does not challenge the original s3≥1 conjecture.
