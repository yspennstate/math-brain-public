# A011: full-support terminal shock and a paid floor repair

All logarithms are base two. This is a narrow repair of A011-POINT-EDIT-REFERENCE-OWNERSHIP@1, not a universal FEI claim. Let h=chi_A on m>=1 data bits, 1<=k=|A|<=m; let t=2^-m, p=2^-r with r>=1 fresh selector bits, and F=h(1-2 1_x* 1_y*). Every point y* is allowed. Put rho=4pt<=1. One supplied full data subprobability R has positive entries, finite c=log(1/R(A)), and mass s<=1. It is an inherited reference; we do not assume a universal bound on c.

## Physical spectrum and signed influence

Write a_T=1_{T=A} and b_T=h(y*)chi_T(y*) in {+-1}. Direct Walsh expansion gives Fhat(empty,T)=a_T-2pt b_T and Fhat(U,T)=-2pt b_T chi_U(x*) for nonempty U. At T=A, b_T=1. Consequently the actual marginal of T is

    q=(1-rho) delta_A + rho U_m,

where U_m is uniform on all 2^m data subsets. The nonempty selector mass is V=4p(1-p)t. Its joint law is flat on the (2^r-1)2^m nonempty-selector atoms, and I_sel=2rpt. The exact created/erased physical data contributions are C=2pt(m-k), E=2pt k, and I(F)=k+C-E+I_sel. No spectral auxiliary variable is asserted to be a physical leaf.

For B=H(selector spectral set | data spectral set), revealing whether the selector is empty gives B<=h2(V)+V log(2^r-1). Since h2(z)<=z log(1/z)+z log e, one gets B<=mV+4 I_sel. Indeed log(1/V)=m+r-2-log(1-p) and log(2^r-1)<r. Apply -log(1-p)<=p/[(1-p)ln2]; after removing mV the bound divided by rho is at most (1-p)(2r-2+log e)+p log e=2r-2-2p(r-1)+log e<2r. Finally 2r rho=4I_sel. This proves the bound for every r, without dimension extrapolation.

## Fixed inherited reference can fail without any boundary deficit

Take m=4,k=2,r=1; then C=E=1/8, I_sel=1/16, I(F)=33/16. The edit is non-bent and changes entropy (the source spectrum is a point mass, while the root has positive mass at every joint atom). For each integer L>=1 choose epsilon=2^(-L-4), R_L(A)=1-15 epsilon and R_L(T)=epsilon for T!=A. R_L is normalized and strictly positive; c_L<1. The data marginal assigns total mass 15/128 off A. Thus the UNCHANGED lift Q_L(U,T)=R_L(T)P(U|T) has

    CE(P_F,Q_L)=CE(q,R_L)+B >= (15/128)(L+4).

The Boolean function, all influences, source slack K I(h)-c_L, and full reference mass remain bounded as L tends to infinity. Therefore no dimension-independent fixed K can pay this inherited-reference lift from that source slack and finite physical edge charges uniformly over all supplied positive references. At L=256 its CE is at least 975/32 > 8*(33/16)=33/2. This refutes a fixed-reference transport proposal, not FEI or existence of an adaptive reference. The previous bent neutral obstruction concerned true entropy and a positive-net-increment-only bank; this new obstruction isolates prescribed-reference shock on a fixed non-bent four-bit core.

## Repair and its complete cost

Replace the data reference by the explicitly paid floor

    R'=(1-rho)R+rho U_m; Q'(U,T)=R'(T)P(U|T).

Its mass is (1-rho)s+rho<=1. It is positive and retains the true physical conditional kernel. Introduce ONLY for analysis the mixture label J with prior (1-rho,rho), component spectra (delta_A,U_m) and component references (R,U_m). Let pi(j|T) be the actual posterior and pi_R(j|T) the normalized reference posterior. Define kappa=sum_T q(T) KL(pi(.|T)||pi_R(.|T))>=0. Log-sum expansion, with all reference masses retained, yields

    CE(P_F,Q')=(1-rho)c+rho m+h2(rho)-H(J|T)-kappa+B,
    CE(P_F,Q')-H(P_F)=(1-rho)c-kappa.

For rho=1 the zero-weight branch is omitted; both identities remain valid. In particular this exact repair preserves a scaled inherited terminal debt and does not get the reference change free.

Use h2(rho)<=rho(m+r-2+log e), B<=mV+4I_sel, and log e<2. Since V=(1-p)rho, the complete cost is bounded by

    CE(P_F,Q') <= c+rho[(3-p)m+r-2+log e]+4I_sel
                <= c+6(C+E)+6I_sel.

For any rate K and supplied source slack S_K=Kk-c this gives the one-use physical certificate

    K I(F)-CE(P_F,Q') >= S_K+(K-6)C-(K+6)E+(K-6)I_sel.

The same source slack is debited once. This repair prevents arbitrarily large nonuniform reference shock; it does not remove the erased-edge bill. Integer word length has its separate global +1; no rounded cost is claimed here.

For an arbitrary Boolean g on independent additional data, with complete prescribed reference R_g and cost c_g, the actual tensor gF has product spectrum and reference R_g times Q'. Hence its exact cost is c_g+CE(P_F,Q'), its influence is I(g)+I(F), and its debt is the sum of D(P_g||R_g) and (1-rho)c-kappa. This retains the entire non-flat terminal cost without treating g as a free point edit or spending the parity bank twice. The point mask acts on the parity block only; no arbitrary-core whole-point admission is inferred.

## Exact remaining universal line

For a general non-bent core the marginal q is not this positive mixture of its original spectrum and U_m: the cross term -4pt h(y*) hhat(T) chi_T(y*) has unequal signed amplitudes. The first unsupported line is an influence-paid replacement for R', with a nonnegative, explicitly costed mixture or another complete reference, such that the same unused source slack pays its full reference change AND the erased-edge charge through subsequent physical restrictions. A true-kernel lift alone does not prove that line.
