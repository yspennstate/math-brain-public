# QFORM-SCHUR-SIGNED-COUNT-SHARP-v1

Let
    A = [[B,C],[C^T,D]]
be real symmetric, with B an invertible k by k principal block, and let
    S=D-C^T B^(-1) C.
If inertia(B)=(p,q), then for every t>0,
    N_S^+(t) >= N_A^+(t)-p,
    N_S^-(t) >= N_A^-(t)-q,
and consequently N_S(t)>=N_A(t)-k.

Proof. With U=(I ; C^T B^(-1)),
    A=U B U^T+diag(0,S).
Write UBU^T=R_+-R_- with R_+,R_- positive semidefinite, ranks p,q. Starting from H=diag(0,S), subtracting R_- cannot increase the number of positive eigenvalues >=t, and then adding the rank-p positive semidefinite R_+ can increase that count by at most p. This proves the positive count. Apply the same argument to -A for the negative count. The absolute count follows by addition. No invertibility of A or S is required.

Singular compatible extension. If B is singular but range(C) is contained in range(B), put X=B^dagger C. Then
    A=(I ; X^T) B (I, X)+diag(0,D-C^T B^dagger C).
Therefore the same statements hold with absolute loss rank(B) and signed losses n_+(B), n_-(B). Without the range condition this is false: A=[[0,I_k],[I_k,0]], B=0 has pseudoinverse Schur complement zero but k positive and k negative unit eigenvalues.

Sharpness under arbitrary pivot thresholds.

1. Scalar. For any d in (0,1), choose N>d^(-1)-1 and a^2=(d^(-1)-1)/N<1. For u=(1,a,...,a), A=d u u^T has unique scalar pivot A_11=d, every other diagonal below d, all principal 2x2 determinants zero, spectrum {1,0,...}, and zero Schur complement at that pivot. Thus the loss one is exact even when no alternate pivot exists.

2. Indefinite pair. For any p0 in (0,1), set eps=sqrt(p0), choose m>eps^(-1)-1 and a^2=(eps^(-1)-1)/m<1. Let B=eps[[0,1],[1,0]], let U have rows e1,e2 followed by m copies of a e1 and m copies of a e2, and set A=UBU^T. Every diagonal is zero. The first pair is the unique pair with determinant modulus at least p0; all other pair determinants have modulus 0, p0 a^2, or p0 a^4. Since U^T U=eps^(-1)I, the nonzero spectrum is exactly {1,-1}. The selected pair Schur complement is zero. Hence the signed losses one positive and one negative are exact even for an arbitrarily small unique indefinite pivot.

At the current nine/400 thresholds these specialize to d=3/40 with N=111,a=1/3 and p0=1/400 with eps=1/20,m=76,a=1/2.

Impact. Schur bookkeeping cannot by itself lower the present fixed-multiplicity threshold. Any further reduction must improve the no-pivot/shared-anchor analytic receiver; pivot norm, near-singularity, threshold inertia, or alternative pivot selection cannot recover the charged directions.
