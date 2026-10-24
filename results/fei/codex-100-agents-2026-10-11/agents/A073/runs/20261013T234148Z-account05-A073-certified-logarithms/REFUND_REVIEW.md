# Independent channel reconstruction of A096's terminal KL refund

Review target: A096-TERMINAL-KL-REFUND-AUDIT@1, source DERIVATION.md equations (2)-(6) and its sublinear-cutoff consequence. Verdict: HOLDS at the stated scope, subject to the executed checks recorded alongside this proof. No repair to the source is supplied. Every logarithm is base two. No finite refund constant or FEI theorem is inferred.

Write p(S)=fhat(S)^2, e_i=sum_{S containing i}p(S), and I=sum_i e_i. For e_i>0 let mu_i(T)=p(T+i)/e_i and r_i(T)=p(T)+p(T+i), T not containing i. Summing disjoint pairs shows sum r_i=1; the definition of e_i shows sum mu_i=1. The reference includes every residual atom, even where the derivative law is zero. Whenever mu_i(T)>0, r_i(T)>0, so KL is finite. Define

    P(i,T)=p(T+i)/I,     Q(i,T)=(e_i/I)r_i(T).

Both normalize to one and have the same coordinate marginal e_i/I. Their likelihood ratio on the support of P is mu_i/r_i. Hence the KL chain rule gives

    I D(P||Q)=sum_i e_i D(mu_i||r_i).

Define M_i=sum_T p(T+i)log2(r_i(T)/p(T+i)). Then algebra of the actual likelihood ratio yields M_i=e_i[log2(1/e_i)-D(mu_i||r_i)]. Summing gives M=sum e_i log2(1/e_i)-I D(P||Q). Constants are treated separately with I D=0 and M=0. Irrelevant coordinates are omitted from the joint laws.

For h=chi_Z product_{b=1}^m f_b, with ell>=2 fresh parity coordinates, its squared spectral law is the product of m seed laws and a deterministic parity set Z. Its influence is J=mI(f)+ell. For a seed coordinate, both mu_i(h) and r_i(h) tensor the corresponding seed law with identical normalized spectator laws. Consequently the likelihood ratio is unchanged: D_i(h)=D_i(f), M_i(h)=M_i(f). For a parity coordinate the residual derivative and reference laws agree, so D_i(h)=M_i(h)=0 and e_i(h)=1. Summing gives M(h)=mM(f) and J D_h=mI(f)D_f, where these are weighted divergence identities. Fresh parity makes hhat(empty)=hhat({i})=0 for every i; that exclusion is essential below.

Activate with independent uniform point controls A_k, q=2^-k, and F=1+A_k(h-1). A point indicator has Fourier coefficients of magnitude q. Thus p_F(empty)=(1-q)^2, p_F(C)=q^2 for nonempty pure-control C, and p_F(C union S)=q^2 p_h(S) for each occupied nonempty core S and every control subset C. These disjoint cases sum to one. The original signs can be recovered by the physical definition of F, so this spectrum is that of an actual Boolean function, not a normalized real relaxation.

For each relevant core coordinate, e_i(F)=q e_i(h). On derivative support, for a core residual T and any C,

    mu_i(F)(T,C)=q mu_i(h)(T),
    r_i(F)(T,C)=q^2 r_i(h)(T).

There are 2^k=1/q control subsets, so the first law is the original derivative law times a uniform control law. The complete reference also has pure-control atoms; they are outside derivative support because h has no singleton coefficients. They must remain in Q's normalization and cannot be silently conditioned away. On derivative support the ratio is q^-1 mu_i(h)/r_i(h), whence

    D_i(F)=D_i(h)+k,      M_i(F)=q M_i(h).

For a control coordinate e_c(F)=q. The exceptional residual atom T=empty has mu_c=q and r_c=d=(1-q)^2+q^2. Every other derivative atom has likelihood ratio 1/(2q); their total derivative probability is 1-q. The two-sector KL decomposition therefore gives

    D_c=(1-q)(k-1)+q log2(q/d),
    M_c=q(1-q)+q^2 log2(d/q^2).

Summing over coordinates with their actual physical influences gives exactly

    I(F)=q(J+k),
    I(F)D_F=q[mI(f)D_f+kJ+kD_c],
    M(F)=qmM(f)+k[q(1-q)+q^2 log2(d/q^2)].

The coefficient of the seed weighted divergence is exactly qm. Activation refunds the k rarity bits for its own data derivatives and preserves the complete seed divergence. This is the normalization and terminal-cost point requested by A001/A096.

For oriented edges starting at lower level at least ell, all positive-cost original data edges lie in the tail because their lower support contains Z. For each control coordinate, nonempty core residual sets contribute q/2; pure-control residual sets with |C|>=ell contribute q^2 sum_{r=ell}^{k-1} binom(k-1,r). Each such equal-mass edge contributes its upper mass to M. Thus the more explicit tail count is

    M_geell(F)=qmM(f)+k[q/2+q^2 sum_{r=ell}^{k-1} binom(k-1,r)].

For ell=2 this equals qmM(f)+kq(1-kq), the source formula. This general count is part of the independent reconstruction, not a new broad candidate.

To review the cutoff quantifiers, fix a nonconstant n-bit seed and ell>=2. Let s(N)>=0 be finite and s(N)=o(N). Put eta_m=sup_{N>=mn}s(N)/N, which is finite and tends to zero. Choose k_m=ceil[4(n+1)m sqrt(eta_m)+2sqrt(m)]. Then k_m=o(m), and eventually N_m=mn+ell+k_m<=(n+2)m. Eventually eta_m<1, so

    s(N_m)<=eta_m(n+2)m<=4(n+1)m sqrt(eta_m),
    k_m-s(N_m)>=2sqrt(m)>log2(mI(f)+ell+k_m).

Therefore the actual Boolean F_m has 0<I(F_m)=2^-k_m(mI(f)+ell+k_m)<=2^-s(N_m). Its tail ratio is at least mM(f)/(mI(f)+ell+k_m), tending to M(f)/I(f). This lower bound uses only nonnegative control costs. Conversely M_geell(F)<=M(F), so the cutoff supremum is at most the unrestricted K_M. Taking a separate sequence for every finite seed ratio proves equality of the two suprema, also when K_M is infinite; no interchange of an uncontrolled supremum and a limit is made. Constants are irrelevant to positive-influence ratios.

There is no gap in the reviewed formulas or cutoff argument. The first unpaid universal line remains

    D(P_f||Q_f) >= sum_i (e_i/I)log2(1/e_i) - K

for one finite dimension-independent K and every Boolean terminal seed. In particular, the known additive k refund does not establish this line. Since M<=B<=M+I/ln(2), a universal M payment would pay C018; the present result is an exact audit of that unpaid interface.

An explicit normalization mutation sharpens this audit. Write alpha_i=sum_{T:mu_i(h)(T)>0}r_i(h)(T). The complete activated reference has derivative-support mass q*alpha_i. If it is conditioned on that support, its KL is

    D_i_conditioned(F)=D_i(F)+log2(q alpha_i)
                      =D_i(h)+log2(alpha_i)=D_i_conditioned(h).

Thus support conditioning removes exactly the k-bit activation refund before any estimate. Substituting that conditioned divergence into the complete-reference formula for M is false. With a dictator seed, m=1, ell=2, k=1, the resulting actual four-bit sign F has four squared Fourier atoms of mass 1/4. A parity coordinate has influence 1/2, complete D_i=1, conditioned D_i=0 and actual M_i=0. The substituted formula would instead return 1/2 bit. The saved mutation certificate identifies both full probability laws. This is an adversarial check of the same source-normalization claim, not a new broad FEI candidate.
