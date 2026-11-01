# A nonfair incoming kernel pays the third prescribed reset

Walsh coefficients are normalized on uniform finite cubes. Spectral entropy,
cross entropy CE and KL divergence use bits. M is oriented erasure, while B_i
is full conditional spectral entropy H(S_i|S_-i). All physical reaches below
are original reaches, never renormalized source influence.

## 1. Consume the closed next step and keep its entire account

The actual Boolean family is f_L=2 product_j(1-1_(input_Ej=0))-1, for every
integer L>=1, with E1={x,a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}, and two
disjoint L-bit private blocks X2,X3. All displayed singletons are distinct.
The original source owner is W=17 I_private(f_L), private={x} union X2 union X3.

The saved A031 NEXT is already closed by A035's second-reset theorem. Its
precise input here is the all-L joint account

    D_old + E_(s,t) CE(p_(s,t), Q_(s,t)) < W-1/32,        (1)
    D_old=M(f_L)+B_x(f_L)+E_s B_b(f_L|x=s),
    p_(s,t)=squared spectrum of f_L|x=s,b=t,
    Q_(s,t)=fair_a(marg_a p_(s,t)).

The four physical parents have reach1/4. The entire old M, x and b erasures,
the first and second prescribed reference histories, all normalizers and all
four terminal liabilities in (1) stay in the account. This stage does not
replace the ancestor quota with a new child-private influence bound.

The source version is A035-TRIANGLE-SECOND-PRESCRIBED-RESET v1 as identified in
its saved CLAIMS; exact author ID/version and bytes are copied to the local
review record. Its input A031 original joint-bank theorem was independently
accepted by A035 at its stated scope. The new second-bank step is independently
reconstructed here; neither review is a full-FEI acceptance.

## 2. The next actual query and the prescribed reference

Choose any physical y in X2. In EACH of the four parents, query y and KEEP BOTH
physical children p_(s,t,u), each of original reach1/8. Prescribe, with no
optimization or choice after inspecting the cost,

    Qnew_(s,t,u)=fair_c(marg_c p_(s,t,u)).                (2)

For a law p, fair_i(marg_i p) means Q(T)=Q(T+i)=[p(T)+p(T+i)]/2.
It is a complete normalized law, with p absolutely continuous with respect to Q.
All reference-only rows remain. The new target is

    D_old+E_(s,t) B_y(p_(s,t))
          +E_(s,t,u) CE(p_(s,t,u),Qnew_(s,t,u)) < W-1/32. (3)

The query is active in BOTH b=0 parents at every finite L: requiring a=0,c=1
and all other X2 bits zero toggles E2 with y, while E1 and E3 stay inactive.
Thus its physical influence is at least q/2>0, q=2^-L, regardless of x.
In b=1 parents y is a dummy; those parents and both their children remain.

## 3. Signed construction and the actual nonfair kernel

For U_J=union_(j in J)E_j the ENTIRE Fourier amplitude is

    a_S=2 sum_(J subset{1,2,3})(-1)^|J|2^-|U_J|1_(S subset U_J)
           -1_(S=empty).                               (4)

Include the empty union. Sum signed terms before squaring. Under any physical
history h, amplitudes are sums of the parent a_(S union V) with character signs.
For the y query specifically they are u+v and u-v. Therefore

    (p_child0(T)+p_child1(T))/2=p(T)+p(T+y).             (5)

Boolean f_L^2=1 supplies every signed convolution, not just a finite prefix;
each physical child also remains Boolean, hence its squared spectrum normalizes.
The finite implementation verifies (4), normalization, signed collapse and
physical influences against a separate direct-character implementation.

For the actual parent (x,b)=(1,0), the two remaining clauses involve disjoint
blocks {a}+X2 and {c}+X3. Put

    u=1-2q+q^2/2, v=-q+q^2/2.

The signed coefficients at empty and at a,y,a+y are u,v,v,v. In incoming
Q=fair_a(marg_a p), at the vacuum row of all OTHER frequencies, the y kernel is

    theta=Q(y=1|other frequencies)=2v^2/(u^2+3v^2).       (6)

It is nonfair for EVERY integer L>=1. At L1, theta=9/14. For L>=2, q<=1/4,
and u^2-v^2=(1-q)(1-3q+q^2)>0, so theta<1/2. All denominators are positive:
v!=0 for 0<q<=1/2. At L2 the kernel is exactly49/218.
The original source influence is not changed by these calculations.

## 4. The measured refund is a conditional mutual information

Fix one physical parent p and its incoming Q=fair_a(marg_a p). The queried
coordinate is y!=a,c, and the inherited complete reference is Qbar=marg_y Q.
Let p_u be the actual physical-child spectra. Define

    rho=sum_T pbar(T) D(p(S_y|T)||Q(S_y|T)),
    Delta=E_u[CE(p_u,Qnew_u)-CE(p_u,Qbar)],
    J_y=H(marg_y p)-E_u H(p_u).

Finite CE implies Qbar>0 wherever pbar>0, and (5) ensures every child has
finite CE against Qbar. Conditional rows of actual mass zero contribute zero,
even when their references have positive mass.

Q's y kernel is the ACTUAL kernel after marginalizing a, not a fair bit.
It follows by the conditional KL definition that

    rho=I_p(S_y;S_a|S_-(a,y)).                           (7)

The correct complete-reference conservation identity is

    CE(p,Q)=B_y(p)+E_u CE(p_u,Qbar)+rho.                 (8)

In particular rho is NOT 1-B_y. The next reset changes the booked bill by

    N=B_y+E_u CE(p_u,Qnew_u)-CE(p,Q)
      =Delta-rho
      =B_a(p)-J_y-E_u B_c(p_u).                        (9)

This exact identity keeps both y outcomes and the previous full reference.
The conversion Delta can be positive; only its DIFFERENCE from the genuinely
available conditional refund is relevant to the bank. No unused full bit is
invented at the nonfair query.

## 5. Why the actual Boolean parents pay this nonfair conversion

Each physical parent f_L|x=s,b=t is invariant under a<->c and X2<->X3, since
the private widths are EQUAL and E1 is symmetric in a,c. The Fourier law inherits
this actual coordinate-permutation symmetry. In particular

    B_a(p)=B_c(p).                                     (10)

This equality is established BEFORE exposing y, which breaks that symmetry in
the children. It is not assumed for the fresh child functions or references.

Write R=S_-(c,y). The full-entropy physical-query identity, once for p and
once for its c-marginal, gives

    B_c(p)-E_u B_c(p_u)
       =B_y(p)-B_y(marg_c p)+J_y-J_y^(minus c),
    B_y(marg_c p)-B_y(p)=I_p(S_y;S_c|R),
    J_y^(minus c)=H(marg_(c,y) p)-E_u H(marg_c p_u)>=0.

The last inequality is the mutual information of physical outcome u and the
retained spectral label with c removed. This argument needs the ACTUAL marginal
child laws, not independently chosen probability vectors. Equations (9)-(10)
therefore yield the exact net identity

    N=-I_p(S_y;S_c|R)-J_y^(minus c)<=0.                 (11)

This is a standard entropy/KL identity plus an explicitly supplied symmetry;
it is not advertised as a new generic Booleanity inequality. Its application
to this paid, signed Boolean source is the new inherited-bank result. In
particular

    Delta=I_p(S_y;S_a|S_-(a,y))-I_p(S_y;S_c|R)-J_y^(minus c)
          <=rho.                                      (12)

No matter how nonfair the kernel (6) becomes, the measured same-node rho pays
the prescribed third reset. In each of the four original parents (11) applies
separately, so averaging with the unchanged reach1/4 and applying (1) proves
(3), for ALL integer L>=1, at SAME rate17 and SAME >1/32 reserve. No new tail
estimate, child influence reserve or repeated fair-bit credit is used.

No positive Delta was found in the frozen checked widths. Consequently this
stage claims a nonincreasing paid extension, not a positive-price nonfair
reset witness. No sign outside the checked widths is extrapolated.
The all-L PAYMENT in (3) is analytic via (11), not a finite extrapolation.

## 6. Complete terminals, arbitrary spectators and the first unpaid line

At (x,b)=(1,1), the actual children are constant, but the fresh c-reference
still costs ONE bit in EACH y outcome. At (x,b)=(0,1), the actual child is the
two-bit defect on a,c, and both y outcomes retain its entire entropy/reference.
These costs are not dropped as inactive/dummy branches. All eight final CE
bills are in (3). Any further no-reset continuation preserves them using (8)
with the supplied current references, not a new conditional bank.

An independent untouched Boolean spectator g with supplied finite-cost Q_g
retains M(g)+CE(p_g,Q_g) with coefficient ONE on both sides, with every reference
explicitly tensored by Q_g. The triangle source owner pays none of that debt.

The normalized non-Boolean control uses equal singleton amplitudes on N=2L-1
private coordinates in X2 union X3 EXCLUDING y, with x,a,b,c,y all dummy. Choose
L=2^17, N=262143. All x,b,y physical restrictions STILL have norm one, all
queried erasures and old M vanish, but the full fresh-c CE is log2(N)+1>17,
while original private spectral energy is1. The source payment fails, and
nonempty convolution at any two active private labels is2/N>0. No high-dimensional
truth table is allocated. This excludes claiming that normalization, the generic
identity (11), or a phase-free relaxation supplied the paid original bank.

First unsupported universal line: after this PRIVATE y exposure the children
are no longer individually a/c symmetric. Price a NEXT prescribed reset at
that asymmetric frontier with incoming references, old M/x/b/y debits and all
complementary terminal bills retained, using SAME unused ancestor capacity.
Neither (10) nor a fair incoming kernel may be renewed by assertion. Arbitrary
signed-core initial source admission and full FEI also remain open.
