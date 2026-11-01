# A bounded-variation coefficient process and its exact obstruction

All logs are natural. Use the physical product Fourier basis, v_T=prod 4p_i(1-p_i), P(U,T)=Fhat(U,T)^2 and Delta=I-Var. This is a scoped continuation of the mixed-sector target, not its solution.

## Physical coefficient profiles have bounded variation

For a two-weight gate F=2*1{w N_A+N_B>=t}-1 and a nonempty B-set T, extend its normalized physical coefficient profile to real z:

    h_T(z)=E_B[(2*1{w z+N_B>=t}-1)phi_T(B)]/sqrt(v_T).

It is constant on each interval between successive thresholds in z. As z passes (t-l)/w its jump is 2 E[1{N_B=l}phi_T]/sqrt(v_T). Therefore

    TV(h_T)<=2 E|phi_T|/sqrt(v_T)=2.                    (1)

Both exterior values are zero since T is nonempty. Here E|phi_i|=2sqrt(p_i(1-p_i))=sqrt(v_i), and independence gives the product equality. No spectral conditioning or Boolean marginal admission is used. Restricting z to the attained A-counts cannot increase variation.

Writing g_j(A)=2*1{N_A>=j}-1, the attained sequence h_T(N_A) is a constant plus a signed sum sum_j alpha_Tj g_j(A) with alpha_Tj one half of its jump at count j, and sum_j |alpha_Tj|<=1. Every g_j is a physical symmetric Boolean threshold. The constant affects only the empty A-coefficient. For U nonempty,

    Fhat(U,T)/sqrt(v_T)=sum_j alpha_Tj ghat_j(U).        (2)

Thus there is an arity-free signed physical-cofactor representation for every coefficient process. It does not itself bound entropy: replacing the alpha signs by mixture weights loses quadratic cancellation.

## The natural absolute-cofactor deficit budget fails exponentially

For a proposed Jensen mixture over the signed tails, define the source budget

    B_abs=sum_{T nonempty} v_T sum_j |alpha_Tj|Delta(g_j). (3)

This is the budget obtained by applying the symmetric-threshold entropy bound to those tails with absolute signed weights. Zero filler can make their total weight one. Formula (3) is an unregistered candidate mechanism, not a theorem previously claimed by another agent. A universal B_abs<=KDelta(F) is false even for actual two-weight thresholds with exactly TWO heavy inputs.

Let r>=1, n=4r+1, B have n fair inputs, A have two fair inputs, w=n+1 and t=w+(n+1)/2. Set g(B)=2*1{N_B>n/2}-1, the balanced odd-majority sign. The actual weighted gate is

    F=-1 at N_A=0; F=g at N_A=1; F=+1 at N_A=2.        (4)

All physical inputs are essential. For each nonempty T, h_T(N_A)=(0,ghat(T),0). Its canonical jumps are alpha_T,1=ghat(T)/2 and alpha_T,2=-ghat(T)/2. Both A-tails are OR2/AND2 and have Delta=1/4. Therefore

    B_abs=(1/4)sum_{T nonempty}|ghat(T)|.              (5)

Let s_i=2X_i-1. The exact signed physical formula is

    F=(s_1+s_2)/2 + (1-s_1 s_2)g(B)/2.               (6)

Hence pure-A singleton masses are 1/4 each, pure-B masses P_g(T)/4, and mixed masses P_g(T)/4 only at U=A. Since g is balanced,

    I(F)=1+I(g)/2, Var(F)=1, Delta(F)=I(g)/2<=n/2.    (7)

For odd majority on n=4r+1 bits, every set of size 2r+1 has coefficient magnitude binom(2r,r)/2^(4r). This formula follows from the exact finite-difference count integral in the checker, or analytically as follows. Differentiate majority in one selected bit: the derivative is the indicator that the remaining 4r bits have exactly 2r ones. For a subset of 2r remaining selected bits, its centered sign moment is 2^(-4r) times the coefficient of z^(2r) in (1-z)^(2r)(1+z)^(2r)=(1-z^2)^(2r), namely (-1)^r binom(2r,r). The sign-coordinate Fourier derivative identity equates this to the original majority coefficient. This proves the magnitude for all r.

Central binomial coefficients are maximal, so binom(4r+1,2r+1)>=2^(4r+1)/(4r+2) and binom(2r,r)>=2^(2r)/(2r+1). Thus

    sum_T |ghat(T)| >= 2^(2r)/(2r+1)^2,
    B_abs/Delta(F) >= 2^(2r)/[2(4r+1)(2r+1)^2] -> infinity. (8)

No floating search or inference from finitely many r is needed. This is a source-budget obstruction, not an FEI counterexample; the weights and threshold in (4) specify actual Boolean functions. It shows that bounded variation and Boolean admission of EVERY tail cofactor still do not license an absolute-mixture entropy payment. The failure already occurs at fixed heavy arity two, so a slice-count normalizer alone cannot repair it.

## The signed squared profile retains the right cost

The same exact family has

    M=1/4, Delta_mixed=(I(g)+1)/4,
    E_mixed=[E(g)+(ln4)Var(g)]/4=[E(g)+ln4]/4.         (9)

The coherent profile is one scalar amplitude times a fixed two-bit parity coefficient. Formula (9) depends quadratically on ghat(T), including its entropy, instead of linearly on |ghat(T)|. The symmetric baseline pays this family; in fact E(F)=E(g)/2+ln4 and Delta(F)=I(g)/2, so E(F)<=cDelta(F), c=460+80ln2. This last statement is a diagnostic control of the proposed reference, not a new class target. The exponentially large B_abs is an artifact of destroying the signed cancellation, while the actual mixed entropy remains paid.

## A045 degree-reference correction is retained

For general M>0, a(U)=sum_TP, b(T)=sum_UP, d=|U|+|T|, and Delta_m=sum(d-1)P. The complete product reference Q0=ab/M^2 has degree normalizer Delta_m/M. Its tilted reference Qd=(d-1)ab/(MDelta_m), with Rd=(d-1)P/Delta_m, obeys Rd/Qd=MP/(ab) pointwise. Ordinary spectral TC and the tilted KL are different averages. Exactly

    E_mixed/Delta_m=E_Rd[ln(v_U v_T/P)/(d-1)],
    M TC_spec=Delta_m E_Rd[ln(MP/(ab))/(d-1)].         (10)

No Boolean estimate is applied to a/M or b/M: they are spectral marginals, not necessarily Boolean laws at the physical biases. Physical conditional-input TC, the spectral TC in (10), and spectral coordinate erasure remain different quantities. The recovered pivotal-credit failure retains its coefficient-one scope.

## Exact first unsupported line and changed mechanism

The target remains an absolute bound on the first expectation in (10) for all actual two-weight thresholds. The bounded-variation physical representation (1)-(2) is now proved, but its absolute tail-deficit budget (3) is rigorously excluded by (8). The next reference must retain signed amplitudes to the point of squaring and account for the full coefficient entropy, as (9) does on the control family. A matrix or coefficient-process reference with quadratic weights is needed; normalizing an absolute tail mixture or importing FEI for conditional spectral marginals does not provide that step. This is the first substantive failure of this new absolute-cofactor mechanism; earlier mass-only and scalar-tax failures are distinct mechanisms, not repeated attempts renamed.
