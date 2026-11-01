# Cutoff and an actual remaining reserve for a point separator

All entropy is bits; all inputs and influences here are uniform and physical.
The exact target is the existing A023/A025 multi-layer separator interface,
not an arbitrary controller or a new universal potential.

## 1. Independent reconstruction of the paired-row bound

Let G,H be actual Boolean signs on one data cube, with disagreement
gamma=Pr(G!=H)>0. Let F=G+A_j(H-G), where A_j is a fresh point
conjunction on j fair bits. At the next live selector query put
rho=2^{-(j-1)}, d=rho gamma, and Delta_T=Hhat(T)-Ghat(T).
Parseval gives sum Delta_T^2=4gamma. The first child is G; the other is
G+A_{j-1}(H-G). Nonempty residual-selector frequencies have coefficients
0 and rho Delta_T, up to a common sign. Thus their parent selector-sector
masses are equal, and their total erasure contribution is exactly
2(1-rho)d. This uses the actual 2^{j-1}-1 frequencies.

For empty residual-selector frequency the two parent coefficients are
u_T=Ghat(T)+rho Delta_T/2, v_T=-rho Delta_T/2. Let a_T=u_T^2,
b_T=v_T^2. Then sum b_T=rho^2 gamma=rho d and
sum(a_T+b_T)=1-2rho(1-rho)gamma<=1. The binary erasure kernel obeys
Psi(a,b)<=b log2(euler(a+b)/b), by -(1-t)ln(1-t)<=t.
The log-sum inequality therefore bounds its sum by
rho d log2(euler/(rho^2 gamma)). Consequently

    B_j/d <= 2(1-rho)+rho log2(euler/(rho^2 gamma))
           =2+2^{-k}[log2(euler)-2+log2(1/gamma)+2k], k=j-1.  (1)

Zero Delta rows contribute zero. No conditional posterior or baseline
coefficient is assumed constant across data rows. This independently
accepts exactly the paired-row criterion in A025 v1, PROOF section 1;
it does not independently accept its whole bundled no-go/census claim.

## 2. A certified finite cutoff, including small disagreement

Suppose gamma>=2^{-D} for some D>=0. Put

    h=ceil(log2(D+1)), m=h+2.

If j>m then k=j-1>=h+2. Hence 2^{-k}D<=1/4,
2k2^{-k}<=1 for k>=2, and log2(euler)-2<0. Equation (1) gives
B_j/d<=13/4<4. Thus possible strictly bad layers have j<=m.
The rational constant follows from ln2>2/3; indeed log2(euler)<3/2.
This is an all-dimensional proof, not an extrapolation of the finite grid.

For the overlapping controller below, write q=2^{-R},r=2^{-T},
eta=2^{-(L+R+T)}, beta=q+r-qr, e=beta-eta. Since L>=1 and
q,r<=1/2, e>=q+r-(3/2)qr>=max(q,r). Its two branch signs disagree
with probability gamma=e/2 because the independent core is balanced.
Therefore gamma>=2^{-(min(R,T)+1)}. We may take

    D=min(R,T)+1, m=ceil(log2(min(R,T)+2))+2.                (2)

Unlike a moderate-gap assumption, this applies when R,T are arbitrarily
large. The cost still depends on their smaller width; that dependence
is not a universal FEI constant.

## 3. Exclusive physical accounts, with arbitrary balanced terminal core

Let S,W,U,V be compatible point indicators on disjoint fresh blocks of
positive widths s,L,R,T, and g an independent balanced Boolean sign.
Set B=WUV, C=U OR V, Dset=C-B, A=B+S Dset, F=1+A(g-1).
Define alpha=2^{-s}, J_B=(L+R+T)eta,
J_C=R q(1-r)+T r(1-q), J_D=J_B+J_C, pi=eta+alpha e.
The cuts of B and C are disjoint, so J(Dset)=J_D. Direct conditioning
or edge counting gives the actual exclusive physical partition

    I_sep=s alpha e,
    I_other=(1-alpha)J_B+alpha J_C,
    I_terminal=pi I(g),
    I(F)=I_sep+I_other+I_terminal.                           (3)

These are not separate budgets for the three named events. The control
policy queries S until failure or completion, resolves B or C respectively,
and stops at a constant or the SAME g. Terminal entropy is exactly pi H(g).

At a live separator history with j remaining bits, rho=2^{-(j-1)},
reach=2^{-(s-j)}, and the actual queried influence and child-product face
price are

    d_j=rho e/2,
    c_j=rho[J_D+(j-1)e+e I(g)]/2.                           (4)

The child product is 1+A_{j-1}Dset(g-1); its controller boundary is
rho[J_D+(j-1)e]. Balance accounts for the factor 1/2 in (4).
This reconstructs A023's single-layer boundary partition and A025's
multi-layer accounts; no new claim of priority is made for (3)-(4).

## 4. A remaining reserve which is not restarted

Let M_j=min(j,m), alpha_j=2^{-j}. At a live separator history define

    V_j=alpha_j[M_j J_D+e M_j(M_j-1)/2+M_j e I(g)],
    V_0=0.

Set the reserve to zero after separator failure, even though the remaining
B-controller must still be resolved on its separately declared control
budget. The next fair bit has a failure child with V=0 and a success
child with V_{j-1}. Elementary subtraction gives

    V_j-(1/2)V_{j-1} = c_j if j<=m, and 0 if j>m.            (5)

By (2), j>m nodes are good. Thus the actual localized bad-layer price
1_{B_j>4d_j} c_j is at most this reserve drift, at every separator history.
Finite summation gives Q_bad,separator<=V_s, with no terminal reserve
left over. The successful branch may have a larger reserve; only expected
drift is required. In particular early good layers do not recreate a
remaining-influence account. Equation (5) is the requested layer transport.

Let M=min(s,m). From (3), alpha J_D<=I_other because alpha<=1/2,
alpha e I(g)<=pi I(g), and M<=s. Therefore

    V_s <= M I_other+(M-1)I_sep/2+M I_terminal <= M I(F).     (6)

For fixed R,T this removes all growth in s from the root allowance. It
does not bound the allowance uniformly as min(R,T) tends to infinity.
The filter in (5) is an analytic envelope: it may spend face price at
eligible but actually good layers. The finite tests have no actual bad
separator nodes; they do not prove zero badness for all widths.

## 5. Whole stopping ledger and signed conditional-bank price

After separator failure, B is a point conjunction, with constant-child
splits satisfying B_i/d_i<3 by the same paired-row maximization.
After success, C=U OR V is the two-event descendant policy. Its fresh
point bound B_i/d_i<=2(1-rho)+rho log2(euler/(rho d_i)) is strictly
below 4 when the residual other-event probability is <=1/2 (the sufficient
condition 1-q>euler/8 holds). This is the scope of A023 v2's descendant
proof; terminal g is not queried here. Thus all possible prefix bad costs
are the separator costs bounded above. Using B_i<=4d_i+c_i at bad nodes,
B_i<=4d_i at good nodes and JS_i<=2d_i/ln2, the retained terminal ledger is

    H(F)<=(4+2/ln2)(I_sep+I_other)+V_s+pi H(g).              (7)

No arbitrary-core FEI certificate has been supplied. If one independently
has H(g)<=C0 I(g), (7) gives a parameter-dependent bound with coefficient
at most max(4+2/ln2,C0)+M; it is not dimension-independent.

The output-bank substitution is kept in the same ledger. In the coherent
ROOT-spectral/physical coupling (not independently sampled descendant
reference laws), J_tree=sum w_v JS_v=I(S0;Pi). At this stopping partition,
H(Y)=h2(pi/2), E H(Y|Pi)=pi, so I(Y;Pi)=h2(pi/2)-pi. Consequently

    C_T=H(Pi|Y)-H(Pi|S0)=J_tree-[h2(pi/2)-pi],
    -I(Y;Pi)<=C_T<=2(I_sep+I_other)/ln2-I(Y;Pi).             (8)

This is A092's previously derived common-lift conversion, reconstructed
using its scalar JS bound and exact physical influence removal. It is
not an extra independent refund to be added to (7). Extra witness-side
conditioning or injecting actual descendant schedules is outside (8).
In the tested low-disagreement fixtures C_T is positive, so even a zero
localized face bill cannot justify dropping this conditional-bank cost.

First unsupported universal line: replace the width-dependent envelope
V_s by a universally influence-paid actual-bad-layer reserve, uniformly
as min(R,T) grows, while pricing prescribed witness/reset costs and
retaining all terminal entropy. Equations (5)-(6) solve layer reuse for
the current envelope but not that remaining universal payment.
