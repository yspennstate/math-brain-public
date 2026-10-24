# Independent reconstruction of A096-TERMINAL-KL-REFUND-AUDIT v1

Verdict: HOLDS at the full stated normalization, transport and cutoff-supremum scope. This supplies no repair and no universal payment. Original statement/hypotheses/contributors/hash are preserved in CLAIMS.json, with this review appended. All formulas below use nats; division by ln2 gives the source's bits.

For p_S=hat f(S)^2, e_i=Inf_i>0, let mu_i(T)=p_(T+i)/e_i, r_i(T)=p_T+p_(T+i). Orthogonality gives sum_T r_i=1 and sum_T mu_i=1. The common index marginal e_i/I defines actual joint probability laws P(i,T)=(e_i/I)mu_i(T), Q(i,T)=(e_i/I)r_i(T). Every positive mu has positive r. Thus I D(P||Q)=sum_i e_i D(mu_i||r_i). Direct expansion gives M_i=e_i ln(1/e_i)-e_i D_i. These are algebraic identities with complete normalizers, not a replacement reference.

For h=chi_Z product_{b=1}^m f_b on disjoint blocks, |Z|=ell>=2, its occupied Fourier indices all contain Z, so no empty or singleton coefficient is occupied. Product structure gives I(h)=J=mI(f)+ell. For each relevant seed coordinate, both derivative and residual laws are its seed law tensored with identical probability factors for every other block; therefore its D_i is the seed D_i and M_i is the seed M_i. For a parity coordinate the lower spectral endpoint is zero, so mu_i=r_i and D_i=M_i=0. Consequently M(h)=mM(f) and sum_i e_i(h)D_i(h)=mI(f)D_f. This remains true for constant seeds, since their seed influence is zero and h is still balanced.

Activate h on a fresh k-bit point indicator A_k: F=1+A_k(h-1), q=2^-k. The constant coefficient is 1-q, every nonempty pure-control coefficient has magnitude q, and all core coefficients are q times those of h, copied over all control subsets. Direct physical flips give data influence q e_i(h); each control influence is q because h is balanced. Thus I(F)=q(J+k).

For a data coordinate, the derivative law is mu_i(h) times the uniform control-subset law. On this occupied support the residual law is q r_i(h) times that same uniform law. The exceptional constant mass lies outside derivative support since h has no singleton coefficient. The likelihood ratio is exactly 1/q times its core value: D_i(F)=D_i(h)+k ln2 and M_i(F)=qM_i(h).

For a control coordinate the exceptional residual atom has derivative probability q and residual probability d0=(1-q)^2+q^2. All other positive derivative atoms have ratio 1/(2q), and their total probability is 1-q. Therefore

D_c=(1-q)(k-1)ln2+q ln(q/d0),
M_c=q(1-q)ln2+q^2 ln(d0/q^2).

The exceptional atom contributes q to the derivative normalization; the regular atoms contribute exactly 1-q. Summing the data and control divergences against their actual influences proves

I(F)D_F=q[mI(f)D_f+kJ ln2+kD_c],
M(F)=qmM(f)+k[q(1-q)ln2+q^2 ln(d0/q^2)].

For oriented tail M_ge2, every positive data oriented bill has residual containing all ell parity bits, so contributes qmM(f). A control coordinate's core-supported edges contribute q ln2/2. Pure-control lower sets with size>=2 number 2^(k-1)-k (zero for k=1,2), each contributing q^2 ln2. Adding gives M_ge2(F)=qmM(f)+kq(1-kq)ln2. For arbitrary fixed ell, every data bill is in M_geell; regular control charges are nonnegative. No claim about a selected coordinate follows from a bound on the total sum.

To check the full cutoff quantifier, fix a nonconstant seed on n bits, finite nonnegative s(N)=o(N), and fixed ell. Let eta_m=sup_{N>=mn} s(N)/N, a finite quantity tending to zero. Choose k_m=ceil(4(n+1)m sqrt(eta_m)+2sqrt(m)); then k_m=o(m), N_m=mn+ell+k_m<=(n+2)m eventually. For large m with eta_m<=1, s(N_m)<=eta_m(n+2)m<=4(n+1)m sqrt(eta_m), so k_m-s(N_m)>=2sqrt(m)>log2(mI(f)+ell+k_m). Actual I(F_m)=2^-k_m(mI(f)+ell+k_m) meets the cutoff. Its tail ratio is at least mM(f)/(mI(f)+ell+k_m), tending to M(f)/I(f). Conversely M_geell<=M, so the restricted supremum is <=K_M. Applying this to each finite seed ratio proves equality even if K_M is infinite; no limit-supremum exchange is used. Constant seeds satisfy the finite formulas and are irrelevant to ratio admission.

The reviewed theorem is source-complete and its universal residual is explicitly NOT closed: D_f>=sum_i(e_i/I)ln(1/e_i)-K remains unproved for a dimension-independent K. A066's heat route must use the same actual terminal-core refund or price its retained erasure, rather than claim that the known activation term supplies that missing seed payment.
