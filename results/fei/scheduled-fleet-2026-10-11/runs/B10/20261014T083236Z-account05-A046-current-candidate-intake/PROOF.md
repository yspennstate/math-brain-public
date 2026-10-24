# Mixed separator/core histories: a reserve carried from the root

All inputs are fair physical bits, entropy is in bits, and face price means
I(F_0 F_1)/2. Controls are compatible point events on disjoint blocks.
This proves separator payment only. It does not pay core-query entropy.

## 1. Frozen family and conditional moments

Let S,W,U,V have positive widths j,L,R,T and let g be ANY independent
Boolean sign. Define B=WUV, C=U OR V, A=B+S(C-B), F=1+A(g-1),
q=2^-R, r=2^-T, eta=2^{-(L+R+T)}, beta=q+r-qr, e=beta-eta,
a=1-Eg, alpha=2^-j, rho=2^{-(j-1)}, p=a e, d=rho p/2.
Throughout the mixed history W,U,V remain entirely unexposed. Conditional
cores may have arbitrary bias. A failed S stops separator accounting;
it does not make F constant, nor remove its terminal entropy.

For G=1+B(g-1), H=1+C(g-1), Delta=Hhat-Ghat, Boolean Parseval gives
the nonconstant DATA-label moments

    sum Ghat^2 = 2a eta-a^2 eta^2,
    sum Ghat Delta = -a^2 eta e,
    sum Delta^2 = 2a e-a^2 e^2.

Indeed EG=1-a eta, Delta_empty=-a e, E[G(H-G)]=-a e,
and E[(H-G)^2]=2a e. This reconstructs A040's bias replacement;
using the balanced moments after a data restriction would be wrong.

At the next S query the empty remaining-S label has paired parent
amplitudes u=Ghat+rho Delta/2 and v=-rho Delta/2. The FULL constant
data label is u=1-a eta-d, v=d. The other data rows have total mass

    q*=2a eta-a^2 eta^2-rho a^2 eta e
          +rho^2(a e-a^2 e^2/2) <=2a eta+rho^2 a e,
    b*=sum v^2=rho^2 a e(2-a e)/4.

All nonempty remaining-S labels contribute exactly 2(1-rho)d to
erasure, since their two parent-sector masses coincide.
For nonnegative x,y, Psi(x,y)<=y log2(euler(x+y)/y), with zero rows
interpreted by continuity. This follows from -(1-t)ln(1-t)<=t.
Log-sum on the nonconstant rows and total mass <=1 on the constant row
therefore imply, for d>0 and theta=eta/e,

    B_S/d <=2+rho log2(euler/(2-p))
               +rho log2(1+2theta/rho^2)
               +d log2(euler/d^2).                       (1)

The exact nonconstant coefficient is rho(1-p/2); replacing it by rho
enlarges the positive logarithm, and replacing 2(1-rho) by 2 enlarges
the other part. Here e<1 and p<2, so denominators stay positive.
If a=0 then g is identically +1 and B_S=d=0.

## 2. Only the last three separator layers can be bad

Geometry gives eta<=qr/2 and beta>=3qr, because q+r>=4qr for
q,r<=1/2. Consequently theta<=1/5, uniformly in every width.
Also eta<=8e^2/25: with t=sqrt(qr)<=1/2, eta<=t^2/2 and
e>=2t-3t^2/2>=5t/4.

First suppose p<=1/16. Since c=1/ln2<3/2 and euler<11/4,
euler/(2-p)<44/31<3/2<2^{3/5}. The inequality ln(1+x^2)<=x
follows by differentiating x-ln(1+x^2): its derivative is
(x-1)^2/(1+x^2)>=0. Thus the middle term in (1) is at most
c sqrt(2theta)<(3/2)sqrt(2/5)<19/20. Finally d<=1/32 and
x log2(euler/x^2) increases on (0,1/32]; its derivative is
2log2(1/x)-c>0. Its value there is <23/64. Hence for EVERY j,

    B_S/d <2+3/5+19/20+23/64=1251/320<4.                 (2)

For p>1/16, the disagreement gamma=p/2>1/32. To avoid any new
black-box spectral premise, here is the generic paired-row bound.
For arbitrary Boolean G,H, sum Delta^2=4gamma. Empty residual-S rows
have sum v^2=rho^2 gamma and total sum(u^2+v^2)<=1. Nonempty
residual-S rows contribute 2(1-rho)d. Applying the same log-sum gives

    B_S/d <=2+2^-k[c-2+log2(1/gamma)+2k], k=j-1.          (3)

This is the paired-row identity independently reconstructed in our
stage-4 PROOF section 1. For k>=3 the right side is strictly below
2+2^-k(9/2+2k), a decreasing sequence whose first value is 53/16<4.
Together (2)-(3) prove that EVERY j>=4 is strictly K4-good for any
core bias, all widths, and all core dimensions. Possible bad S queries
are restricted to j=1,2,3. This is not a claim about biased C descendants.

We also consume and independently reconstruct A040's stronger rare
geometry result. If e<=1/8 then p<=1/4, d<=1/8, theta<=1/25.
The elementary estimates c<13/9, euler<87/32,
(87/56)^20<2^13, and sqrt(2)<10/7 give the three terms in (1)
strict upper bounds 13/20, 26/63, and 67/72, respectively. For c,
ln2>2/3+2/81+2/1215=842/1215>9/13. For euler, its degree-six
sum 1957/720 plus tail <=1/4410 is <87/32 (subsequent term ratios
are <=1/8). The last-term monotonicity holds on (0,1/8]. Therefore

    B_S/d <2+13/20+26/63+67/72=10063/2520<4.             (4)

In particular min(R,T)>=4 implies e<=q+r<=1/8. No S layer can be bad
in that geometry even after arbitrary adaptive core restrictions.

## 3. A fixed root reserve and exact physical drift

Fix m*=0 if min(R,T)>=4 and m*=3 otherwise. This number is chosen
once from the unexposed control geometry, not from the changing bias.
Set JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC,
M_j=min(j,m*) and

    U_j(g)=2^-j[a M_j JD+a e M_j(M_j-1)/2+M_j e I(g)].    (5)

Set U=0 at S failure or completion. This is a nonnegative local
remaining reserve, never a refreshed root account. The physical
child-product at a live S query is 1+S_remaining(C-B)(g-1).
Since the boundary cuts of B and C are disjoint, I(C-B)=JD.
Direct edge counting gives

    c_j=I(F0 F1)/2=2^-j[a(JD+(j-1)e)+e I(g)].           (6)

Subtraction of (5) at successive layers yields U_j-U_(j-1)/2=c_j
when j<=m*, and zero when j>m*. By section 2 all potentially bad S
queries are included among these debit layers. Eligible but good
layers may be charged; actual bad debit remains smaller.

At a physical core query i, let g0,g1 be its fair restrictions and
t_i=Inf_i(g). Fairness and the physical influence identity give

    (a0+a1)/2=a,
    (I(g0)+I(g1))/2=I(g)-t_i,
    U_j(g)-(U_j(g0)+U_j(g1))/2=2^-j M_j e t_i.           (7)

The actual queried influence is Inf_i(F)=pi_j t_i,
pi_j=eta+2^-j e. Thus the same owned release in (7) lies between zero
and 3 Inf_i(F). It is a decrease of U, not an additional independent
refund. No charge is reversed when bias becomes small. Formula (5)
may be selected at the original root; it is not installed afresh at
later descendants with a newly granted budget.

For ANY finite adaptive history exposing only fresh S and core bits,
multiply each drift by its original physical reach. Telescoping on the
actual tree gives the exact conservation identity

    sum eligible-S reach*c_j + sum core reach*release_i
          + E U_stopped = U_root.                       (8)

Consequently Q_bad,S+sum core reach*release_i+E U_stopped<=U_root.
This covers interleaving and early stops. Leaves after S failure or
completion retain their actual Fourier entropy even though U=0.

At the original root let alpha=2^-s and define exclusive accounts

    I_sep=s alpha a e,
    I_other=a[(1-alpha)JB+alpha JC],
    I_terminal=(eta+alpha e)I(g).

Their sum is exactly I(F). Because alpha<=1/2, alpha a JD<=I_other;
because alpha e<=pi, alpha e I(g)<=I_terminal; and M_s<=s.
Equation (5) gives

    U_root<=M_s I_other+max(M_s-1,0) I_sep/2+M_s I_terminal
          <=3 I_other+I_sep+3 I_terminal<=3 I(F).        (9)

For a balanced root this U is no larger than v2's W: in the wide
geometry both vanish, and otherwise its M is 3 rather than 4 or 5.
The previously accepted balanced controller-prefix theorem remains
valid. Equation (9) extends only the separator part to arbitrary bias
and mixed histories; it does not extend the whole prefix to biased
union descendants.

## 4. Actual data entropy: an exact unpaid residual

Let s=L=R=T=1 and g=(-1,1,1,1), query the first core coordinate.
Here eta=1/8, e=5/8, pi=7/16, a=1/2, I(g)=1. The query influence
is 7/32 and the owned U release is 5/32. The child core entropies
are both zero, while H(g)=2. Direct physical six-bit FWHT yields
the squared-mass multiplicities

    F: 44*(1/1024),12*(9/1024),4*(25/1024),
       3*(49/1024),1*(625/1024);
    F0:22*(1/256),6*(9/256),2*(25/256),1*(49/256),1*(81/256);
    F1:one mass 1,31 zero masses.

For D_F=H(F)-(H(F0)+H(F1))/2 and
D_g=H(g)-(H(g0)+H(g1))/2=2, rational log enclosures certify

    D_F-pi D_g-release >3429/100000>0.                  (10)

The residual interval is [0.034291680553963,0.034291680553964].
Actual erasure and JS terms are approximately 0.589229104430196 and
0.476312576123766 bits, respectively; their rational enclosures and
the exact spectra are in out/DIRECT.json. Both child core laws and
both child banks (3/4 and 0) are retained in out/CHECK.json. Actual
restricted F0 has positive controller entropy, already present in D_F;
it has not been replaced by a bare child-core entropy.

Thus the first unsupported line is the proposed inequality
D_F<=pi D_g+release_i, already FALSE for this actual Boolean root.
This falsifies this specific release-only local payment, not FEI or
the full bank identity (8). Payment with genuinely unused inherited
controller/core slack, and all prescribed reference/reset costs, stays
open. For a mixed stopped tree retain E H(F_leaf) and all signed
reference increments; a root pi H(g) cannot replace those conditional
terminal laws without a proved transfer identity.

## 5. Validation and independence

Frozen code/check.py domains: all 16 labelled two-bit cores, plus the
eight signed three-bit majority, point, parity and constant cores;
j in {1,2,4}; (L,R,T) in {(1,1,1),(1,2,2),(1,4,4)}. There are 216
separator nodes, 504 actual data queries and 720 ordered two-core-query
ledgers. Fraction arithmetic and rational outward log enclosures check
normalization, bank contraction, root accounts and exact conservation.
2,887 recorded assertions PASS in 3.103 seconds. Enumerated cores are
corroboration; sections 1-3 supply the arbitrary-core proof.

The separately frozen code/direct.py computes one root and both actual
restrictions from 128 truth-table evaluations and integer FWHT, without
using the grouped controller coefficient helper. It reproduces the
erasure/JS intervals and strictly positive sign in (10), PASS in 0.009
seconds. The arithmetic log helper is shared and has rational remainder
bounds; this representation check is not an independent agent review.

A046 independently reconstructs A040-BIASED-RARE-SEPARATOR-CORE-QUERY@1
unchanged: (1),(4),(6), and the M=1 instance of (7) give its full exact
scope without repair. The new cutoff and carried U require independent
review by A040/A087/A092. Neither claim supplies a universal FEI proof.
