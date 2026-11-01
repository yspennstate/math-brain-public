# Shared-core ownership and a four-cell repair

Let d>=2 be even, delta=2^-d, t=sqrt(delta), b the canonical d-bit quadratic bent sign, and Q_r the product of r disjoint two-bit gates negative only at 11. Put alpha=2^-r, w=4^(1-r), e=delta/2, and F=b+1_(y=0)(Q_r-1). Its zero-selector Fourier coefficients are sigma*t+delta(alpha-1); all other coefficients have magnitude delta*alpha. Every selector influence is e, and every core influence is 1/2+delta(1-alpha).

For a selector query, retain its partner V alone. Its laws are mu_V=(1/2,1/2), r_V=(1-e,e). Set A=1-delta+2delta alpha^2 and R_sigma=1+2sigma*t(alpha-1)+delta[(alpha-1)^2+alpha^2]. Let D_y=sum_sigma N_sigma delta log2(A/R_sigma). The full conditional divergence in partner-zero is

 D0=D((w,1-w)||(A/(1-e), e(1-w)/(1-e)))+w D_y.

The binary quotient loss is e D0/2. For r>=2, D0>=3d/4-1 by the binary entropy bound and e<=1/8. More precisely e<=1/8 holds even d>=2 (delta<=1/4), so (1-e)/e>=2^d; w<=1/4. Thus for r=2^d all 2r binary losses together are at least 3d/8-1/2. They cannot be charged at a fixed rate to one specified core influence <=3/4. This is not a refutation of A073's explicitly dedicated r=1 reserve.

Repair: retain both V and whether the other r-1 pair subsets are empty. The complete four-cell laws are

 mu=(w/2,(1-w)/2,w/2,(1-w)/2),
 r=(A,e(1-w),ew,e(1-w)).

Only partner-zero/empty-spectator cell has residual conditional KL, so its weighted loss is e*w*D_y/2. Summed over all 2r queries this is r*delta*w*D_y/2. Since 3R_+-A=2(1-t)(1-2t)+6t(1-t)alpha+4t^2 alpha^2>=0, all conditional likelihood ratios are <=3 and D_y<=log2 3<2. Also r*w<=1. Therefore the ENTIRE remaining four-cell loss is <delta<=Inf_(y1)/2 for every r, allocated once to half of ONE named core influence. No retained quotient price, core entropy or other debit is assigned to that same fraction.

Every Fourier atom is positive. A direct spectrum estimate gives H(F)<=d+2+2d delta+2r delta<=4I(F), I(F)=d/2+d delta(1-alpha)+r delta. This is a diagnostic and repaired partial refund on one family, not FEI. A universal retained row price and genuinely available recursive terminal slack remain open.

## Pay the retained selector price as well, without reusing the core owner

The four-cell retained price has an exact cancellation:

 M_i^4/e=1+(w/2)[d+2r-1+log2 A].

Let J=r delta be total selector influence. Then sum_selector M_i^4-J<=delta(d/2+1), using r w<=1 and r^2 w<=1. Adding ALL discarded four-cell losses gives extra debit <delta(d/2+2)<=3/4<=(3/2)Inf_(y1). This charges only ONE specified core coordinate, once. Each core row has B_j<=h2(Inf_j)<=2Inf_j because Inf_j>=1/2. The selector lower halves cost at most J/ln2. Hence even the enlarged audit bill

 2I_core+sum_selector M_i^4+sum_selector L_i^4+J/ln2

is at most (7/2)I_core+(5/2)J<=(7/2)I, using ln2>2/3. The marked owner takes its baseline 2Inf_(y1) plus at most (3/2)Inf_(y1); all other core coordinates take only baseline 2Inf, and all selector coordinates at most (5/2)Inf. This pays the retained quotient, discarded remainder and usual lower-edge half from one root influence partition. It does not assert hereditary availability of this row quota or a terminal-child entropy surplus after restrictions.
