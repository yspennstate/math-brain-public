# Third shared query: ancestor derivative energy replaces adjacent equality

Bits. Full FEI OPEN. This is an author proof of a supplied-source continuation theorem, pending independent review. For EVERY odd d>=5, take the actual central majority on d shared physical bits, positive at weight<= (d-1)/2, and replace vertices0,e0 by arbitrary correlated Boolean private profiles V,W. Every finite adaptive history may query at most THREE distinct shared NONSEPARATOR coordinates (other than0), with arbitrary private interleavings, early guard exposure and stopping. Every physical coordinate is queried at most once per path. Retain every sibling and full inherited core and wrapper terminal entropy. No hypothesis on profile means.

## 1. A reusable quadratic-energy replacement

Write r=d-2 odd, alpha=binom(r+1,(r+1)/2)/2^(r+1). The parent odd-majority coefficients A_k vanish at even cardinalities and satisfy

 A_(2l+1)=(-1)^l alpha binom((r+1)/2,l)/binom(r+1,2l),
 A_(k+2)=-k A_k/(r+1-k) for odd k.

This follows by differentiating majority: its derivative is the indicator of the tie slice on r+1 bits. The conditional product moments are the coefficients of (1-t^2)^((r+1)/2) divided by binom(r+1,2l). Parseval of that actual Boolean derivative gives sum_k binom(r+1,k) A_(k+1)^2=alpha.

After two fixed shared answers00, the carrier coefficients are beta_even(k)=2A_(k+1), beta_odd(k)=A_k+A_(k+2). For11 their even signs reverse, leaving all absolute paired products unchanged. After01 or10 the carrier is central odd-majority on r bits, so its paired products and true erasure are ZERO.

For00 define nonnegative quadratic energies, with out-of-range terms zero,

 X=sum_(k even) binom(r-1,k) A_(k+1)^2,
 Y=sum_(k even) binom(r-1,k) A_(k+3)^2,
 Z=sum_(k odd)  binom(r-1,k) A_(k+2)^2,
 P=sum_(k odd)  binom(r-1,k) |A_k A_(k+2)|.

Twice applying Pascal gives EXACTLY alpha=X+Y+2Z. The recurrence and binomial identity give

 binom(r-1,k)|A_k A_(k+2)|
 =binom(r-1,k-1)[(r-k)/(r+1-k)] A_k^2,

so P<=X. Cauchy-Schwarz on the even sector now proves

 L=2 sum_(k=0..r-1) binom(r-1,k)|beta_k beta_(k+1)|
 <=4X+4sqrt(XY)+4Z+4P
 <=10X+2Y+4Z <=10alpha.                         (1)

The second inequality uses 4sqrt(XY)<=2X+2Y. This is a quadratic-energy inequality, not a claim that the twice-conditioned coefficients retain adjacent equality. More generally the first two bounds hold for ANY coefficient sequence with the displayed recurrence and derivative-energy identity; no entropy estimate is inserted into (1).

For nonnegative u,v, Phi(u,v)=(u+v)h2(v/(u+v))<=2sqrt(uv), including zero endpoints. Here is a complete scalar verification. For f(t)=2sqrt(t(1-t))-h2(t), f''(t)=[sqrt(t(1-t))/ln2-1/2]/[t(1-t)]^(3/2). On(0,1/2) it changes sign exactly once, from negative to positive. Also f'(0+)=+infinity and f'(1/2)=0. Thus f' first decreases and then increases to zero, crossing zero once in its decreasing phase. Consequently f increases then decreases on[0,1/2]; its endpoint values are both zero. Symmetry proves f>=0 on[0,1]. Thus the unedited carrier's query erasure is <=L. Direct pivotal counting gives actual carrier influence

 q=alpha*(r-1)/r for answers00 or11,
 q=alpha*(r+1)/r for answers01 or10.              (2)

Since r>=3, (1) yields B_j(carrier)<=15q. This includes both nonconstant event-dead siblings, not just the surviving00 event.

## 2. Complete edited mean sector, including interference

Only answer00 retains the edited vertices. Put p=2^-r, mu=EV,nu=EW. They and their neighbors along any NONSEPARATOR queried bit are all +1 in the unedited carrier, even at r=3. Its complete empty-private coefficients are

 mhat(S)=beta_|S|-p[(1-mu)+(-1)^(0 in S)(1-nu)].

For such a query the translation t_S is identical on S,S+j and |t_S|<=4p. Phi<=2sqrt(uv), triangle inequality and full carrier Parseval give

 B_j(m)<=L+8p sum_all_S |beta_|S||+16p
       <=10alpha+8sqrt(p)+16p.                   (3)

The last16p is 2*(4p)^2 times the2^(r-1) Fourier pairs; no empty row or interference term is omitted. Put q_r=binom(r-1,(r+1)/2)/2^(r-1), the active carrier influence. Along odd r>=3,

 q_(r+2)/q_r = r(r+1)/[(r+3)(r-1)] >=1/2.

Therefore both sqrt(p)/q_r and p/q_r decrease. At r3, q_r=1/4 and 8sqrt(p)+16p=2sqrt(2)+2<=5=20q_r, by sqrt(2)<=3/2. Combining(2),(3) gives

 B_j(m)<=35q_r<=35 Inf_j(F).                    (4)

The LAST inequality is actual physical ownership: edited edges were nonpivotal in the original carrier and edits add p(2-mu-nu)>=0; hence Inf_j(F)=q_r+p(2-mu-nu). On event-dead branches there is no translation and B_j<=15Inf. Influences tend to zero with d; this is not a fixed positive influence-floor argument.

## 3. Full spectrum and SAME source telescope

At r remaining shared bits retain U=p sum_live H(profile), R=rp sum_live Var(profile); both are zero on event-dead carrier branches. At ANY shared query U is harmonic and the nonempty-private erasure is at most its squared mass p sum_live Var(profile)=R-E R_child. The original reserve R therefore pays that entire sector. The physical two-child JS bound is JS<=2Inf/ln2<=3Inf. Equations(3),(4) prove the THIRD-query price

 Delta H(F)<=release_R+38 Inf_query(F).          (5)

No extra bank is created for this transaction. First and second prices5 and15 are the exact A076 v9/A077 SECOND-MAJORITY v1 clauses. Their respective private histories, and every subsequent private suffix here, use the A078 v2 nonzero-mean inequality

 Delta_private H<=Delta U+release_R+12Inf_private+Delta Xi,
 Xi=p sum_nonempty k(Vhat,What), -4p<=Xi<=0.

Supply ONCE an unused original B>=4e_o AFTER all old bookings, where e_o=2^-d. Let C=(B-Xi_o)/e_o and K=pC+Xi while both adjacent events survive; K=0 after common-event death. Each nonseparator query doubles p,Xi,K on its surviving child and kills the edited event on its other child; EXPECTATION across both children is K. Retain the true carrier entropy on killed branches. Private queries satisfy Delta Xi+E K_child=K_parent. Nonnegativity follows from C>=4. The original event-mass martingale gives E K_leaf>=B-4e_o. Finite actual-reach telescoping now yields

 H(F_o)-E H(F_leaf)+E(R_leaf+K_leaf)
 <= U_o-E U_leaf+R_o+B
    +12P_private+5P_first+15P_second+38P_third.    (6)

This covers EVERY adaptive nonseparator choice and every finite private continuation at the declared three-query scope. Physical P is query influence times ORIGINAL reach. All inherited input entropy decrements and complete actual terminals remain. A separator and a fourth shared query are not silently paid.

## 4. Actual Boolean padding source and first unsupported line

Use the ORIGINAL donor V=y*bent_k(z), W=y[1-2*1{z=0,x1=...=xm=0}], even k>=4,m>=2. Guard influence is INCLUDED: I(V)=k/2+1,H(V)=k. Its single split is5e_o I(V)=e_o H(V)+S with S=e_o(3k/2+5). Preserve FIRST4e_o and every oldD0. After BOTH first x1 answers carry B=S-D0-4e_o, admitted if D0<=S-8e_o. Equation(6) leaves expected K>=S-D0-8e_o. The concrete d5,k4,m2,D0=e_o donor has S11/32,B6/32 and guaranteed2/32 remaining after all THREE shared transactions; every guard, bent and padding influence is counted physically.

The exact first unpaid continuation is a FOURTH nonseparator query of the already thrice-conditioned carrier. The quadratic recurrence still exists, but no depth-uniform payment or original-source bound for its increasing bias has been proved here. Arbitrary carrier queries, separator after biased restrictions, universal donor eligibility and arbitrary inherited core/terminal FEI also remain open. The reusable change is replacement of a lost coefficient equality by ancestor derivative energy; the universal next step is a depth-uniform version and its actual-reach cumulative payment, not another reset of the donor or a repeated finite census.
