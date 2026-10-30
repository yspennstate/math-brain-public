# One changed stopping leaf: reference shock and actual data-edge ownership

All costs are bits; author derivation pending review. The common-magnitude admission is deliberately broken here. This continues A011's comb interface and consumes A086's independent acceptance of that interface. A097's growing-overlap obstruction is retained, not contradicted.

## Exact representation and complete terminal ledger

Let h be any Boolean sign on m>=1 uniform data bits, y* any physical point, and h* the Boolean sign obtained by flipping h at y*. Let A be a point cylinder on r>=1 fresh selectors with probability p=2^-r. Set t=2^-m and

    F(x,y)=h(y)[1-2 A(x) 1{y=y*}].

This is precisely a comb with all leaves h except one leaf h* whose depth is r; the cylinder literals may have any orientations. Any unqueried later selectors are erased as spectators. Both nonconstant child cores can use every data coordinate, and their magnitudes generally differ. No substitution of a formal fresh core is made.

Choose one fixed full subprobability reference R on all data subsets, positive on the support of BOTH actual cores, with finite c=CE(P_h,R) and c*=CE(P_h*,R). This admission is needed: a reference supported only on P_h may miss new frequencies after the edit. Let

    q(T)=(1-p)P_h(T)+p P_h*(T),
    K(U|T)=P_F(U,T)/q(T),
    Q(U,T)=R(T)K(U|T).

At zero true q choose a normalized empty-selector kernel. The full reference mass is sum R<=1, including reference-only fibers and any missing-mass penalty. Its exact cost is

    CE(P_F,Q)=(1-p)c+p c*+B,
    B=H(S_selectors|S_data).

In the previous general comb ledger CE=average c+B+JS-kappa, this SAME-reference choice has kappa=JS exactly. Its reference leaf posterior is the physical leaf prior; direct posterior expansion gives sum q KL(posterior true||prior)=JS. That cancellation is measured, not a discarded label cost. The complete terminal bill, including the shock p(c*-c), remains. Root KL is

    CE-H(F)=KL(q||R).

Signed coefficients can be reconstructed without using FEI. Put a_T=hhat(T), c_T=h(y*)chi_T(y*), and chi_U(x*) for the control-cylinder orientation. Then

    Fhat(empty,T)=a_T-2pt c_T,
    Fhat(U,T)=-2pt c_T chi_U(x*) for U nonempty.

Thus the total nonempty-selector mass is V=4p(1-p)t, regardless of h or y*. Given that sector, the selector set is uniform among 2^r-1 choices and independent of the data set. Consequently

    B=H(1{S_selectors!=empty}|S_data)+V log2(2^r-1)
     <=h2(V)+V log2(2^r-1)
     <=V[m+2r-2+log2(e)]
     <=m V+4 I_sel(F),
    I_sel(F)=2rpt.

The penultimate line uses h2(V)<=V log2(e/V), V=4p(1-p)t and 2^r-1=(1-p)/p. The final line uses log2(e)<2, so V(2r-2+log2(e))<=8rpt. All sectors, empty data frequencies and entire reference normalizers are present. This bounds the extra selector bill, not the arbitrary c or c*.

## New and erased data edges are distinct physical accounts

Let d be the number of data neighbors of y* at which h already changes sign. Each formerly unpivotal incident edge becomes pivotal, and each formerly pivotal incident edge is erased. Their actual weighted influence contributions are

    C=2pt(m-d), E=2pt d,
    Delta_data=I_data(F)-I(h)=C-E=2pt(m-2d),
    I(F)=I(h)+C-E+I_sel(F).

Every incident undirected edge contributes 2t to its original core influence and is edited on the actual cylinder of probability p. Thus C and E are physical edge counts, not derivative energy or a reset budget. Since mV=2(1-p)(C+E), the full magnitude-change payment is

    B<=2(1-p)Delta_data+4(1-p)E+4 I_sel(F).

This is a quantitative reference-transfer correction with one explicit missing source reserve. At a local extremum d=0, no original data edge is erased, and

    CE(P_F,Q)<=(1-p)c+p c*+2(1-p)Delta_data+4 I_sel.

The added data influence pays this bill once. If the supplied reference also has c<=K I(h) and c*<=c, then for K>=2 the ideal full cost is <=max(K,4)I(F). More generally the exact terminal shock p(c*-c) remains and must be paid explicitly; mere point rarity does not bound it for an arbitrary prescribed reference. This is a conditional cost-transport statement, not a universal construction of such an R.

For d>0 the positive added-edge account C is not the net source budget. Treating C+E as Delta_data double counts erased old edges. The extra 4(1-p)E is the precise account requiring a source-owned reserve. E itself records removed old influence, so it cannot automatically be spent again at the root.

## An exact neutral-increment guard, beyond the existing selector-only obstruction

Use the actual quadratic bent core

    h_m(y)=(-1)^(y1*y2+...+y_(m-1)*y_m), m even >=4,

and r=1. Choose y* with Hamming weight m/2. The point's original pivotal degree is d=m/2, so C=E and Delta_data=0 exactly. I(h_m)=m/2 and I_sel=t. The root data spectrum nevertheless changes magnitudes.

The two-bit base has Fourier coefficients (1,1,1,-1)/2; tensoring proves h_mhat(T)=epsilon_T sqrt(t). Multiplying by h_m(y*)chi_T(y*) makes the oriented signs epsilon'_T have sum 1/sqrt(t), by Fourier inversion at y*. Thus counts are N_+=(2^m+2^(m/2))/2 and N_-=(2^m-2^(m/2))/2 for EVERY edited point. At r=1,

    q_T=t(1-2 epsilon'_T sqrt(t)+2t),
    P_F(nonempty selector,T)=t^2.

For m>=4, q_T>=t/2. The nonempty-selector contribution alone gives

    B>=sum_T t^2 log2(q_T/t^2)>=t(m-1).

With the full uniform data reference R(T)=t, both terminal costs equal m. Also

    KL(q||uniform)<=chi_square(q,uniform)/ln2
                        =4t(1-t)/ln2<6t.

Here the chi-square equality follows from E_uniform epsilon'=sqrt(t). Hence the TRUE Boolean entropy obeys

    H(F)-m=B-KL(q||uniform)>t(m-7).

Therefore there are no fixed finite K,A such that every one-point leaf edit has a complete root reference of cost <=m+K I_sel+A max(Delta_data,0), even with a bent core and unchanged uniform terminal bill. Take even m>K+7 in this neutral family and apply Gibbs CE>=H. This strengthens the reserve diagnosis: an owner based solely on POSITIVE NET newly added data influence cannot repair the known unrestricted selector-only failure. This is not an FEI counterexample; I(F)=m/2+t and H/I remains bounded.

## Full-cost bent application, preserving the actual final influence

A supplied source slack S_K=K I(h)-c leads to an explicit signed bank certificate, including the terminal shock:

    K I(F)-CE >= S_K-p(c*-c)
                  +[K-2(1-p)]C-[K+2(1-p)]E+(K-4)I_sel.

This follows by subtracting the already proved B bound from the exact complete CE. If the right side is nonnegative, the root cost is paid. The source slack is consumed once; it is not renewed after changing the leaf. For K>=4 the last term is nonnegative, but the E and reference-shock terms remain obligations. This is a sufficient certificate with measured costs, not a circular assertion that root slack is nonnegative. At K=4, a neutral edit and c*=c, this sufficient certificate reads S_4>=4(1-p)E.

For every even m>=2, every point y*, and every r>=1, the SAME uniform-reference lift above satisfies CE<=4I(F). This is an application of the owned-edge ledger, not a novelty claim for the Boolean class. The root reference CE=m+B is not claimed optimal.

Since I(h_m)=m/2 and d<=m,

    4I(F)-[m+mV+4I_sel]
       =m+4mpt(1+p)-16pt d
       >=m[1-4pt(3-p)].

For m>=4 this bracket is positive because t<=1/16 and p<=1/2. For m=2,r>=2 it is positive because t=1/4,p<=1/4. For the remaining m=2,r=1, B<=1 (one selector bit), CE<=3 and I(F)>=3/4 by the exact influence identity. This proves all widths and all point orientations. At a local extremum the stronger bound CE<=2I_data+4I_sel follows because m=2I(h_m) and the extra data influence pays mV.

The analytic domain is separate from direct finite Walsh certificates. The uniform core bill m remains, and arbitrary low-influence cores may not satisfy m<=K I(h). Integer one-word prefix rounding retains +1. No original incidence-queue L+S+R estimate is claimed.

## First unsupported universal line

For a magnitude-changing shared-core representation, pay the exact terminal reference shock and 4(1-p)E (or a sharper measured conditional bill) from one unused seed reserve. It is invalid to pay them from positive net added influence alone, as the neutral example proves. Neither the fixed uniform reference, a universal influence-paid terminal reference, nor a rule selecting an unused shared-core reserve exists here for all Boolean functions. NEXT must identify a spectral/core reference slack correlated with E and transport it through the same physical history, without allocating erased source influence twice. Extending local-extremum or bent widths further would not resolve this universal gap.
