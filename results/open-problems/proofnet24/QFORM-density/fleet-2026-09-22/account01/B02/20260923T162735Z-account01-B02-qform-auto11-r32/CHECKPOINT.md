SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T16:27:35Z.
attacking: the double-anchor small-E2 collar by replacing the physical residual E2 packet with either physical star-leg E2 packet, using the same cross-disjoint one-sided-Weyl compiler.

# Early substantive checkpoint

Let the live invertible second-anchor block be

B = [[P,R],[C,M]],  D=|det P|>0,  S=M-C P^{-1}R,
G=D^2||S||_F^2>Z/24.

Assume the surviving double-diffuse packet from the preceding B02 run:
max_i ||S_{i:}||^2/||S||_F^2<1/4 and max_j ||S_{:j}||^2/||S||_F^2<1/4.

New observation: the previous E1(S) x E2(M) determinant compiler has a left-leg analogue with E_C=E2(C)=det(C^T C). The two positive basis families in the one-sided-Weyl Brascamp--Lieb expansion are:

(1) anchored singleton family: det B[{two P rows}+i,{two P cols}+j]=det(P) S_ij, total squared mass G;
(2) left-leg pair family: det C[U,:], |U|=2, total squared mass E_C.

If (i,j) is sampled from |S_ij|^2/||S||_F^2 and U from det(C[U,:])^2/E_C, then the row-disjoint probability is

delta_C=P(i notin U)=1-sum_k a_k q_k >1-2(1/4)=1/2,

because sum q_k=2. Conditioning on disjointness gives residual row BL exponents <=1/2. The determinant/entropy calculation is no worse than the already proved E1(S) x E2(M) compiler, hence should yield

int |phi_Q(t)| dt <= 10 pi 2^(1/5)e^(4/5)(delta_C G E_C)^(-1/10).

The transpose gives the same with E2(R), using column diffusion of S. Therefore if either E2(C) or E2(R) is >=Z^(2/3)/64, the partner packet G>Z/24 gives the same universal-scale exit

int |phi_Q| <179.281 Z^(-1/6),   ||p_Q||inf<28.534 Z^(-1/6).

Failure forces E2(C),E2(R)<Z^(2/3)/64. Together with the preceding run's E2(M)<Z^(2/3)/64, every physical residual/star-leg block is either Frobenius-small at scale Z^(1/3) or has stable rank <32/31. Also for T=C P^{-1}R,

D^2 E2(T)=E2(C)E2(R)

by the rank-two compound identity. This creates a new triple-near-rank-one/small structural collar. Full proof and constant audit to follow in REPORT.md.
