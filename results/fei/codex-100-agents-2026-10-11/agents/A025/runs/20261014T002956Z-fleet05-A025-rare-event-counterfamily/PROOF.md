# A multi-bit separator: a failed unfiltered reserve and a paid actual tree

All entropies are in bits. I is ordinary total influence of an actual sign
function. J(A)=I(1-2A)/2 for an indicator on a uniform cube. Q is the
normalized odd-two-face count; a split spends c=I(f0 f1)/2. Physical reach
probabilities, not spectral weights, multiply every node cost.

## 1. Uniform good-node criterion for a rare point switching block

Let G,H be arbitrary Boolean signs on a common data cube, gamma=P(G!=H)>0.
With j fresh independent point-selector bits, set F=G+A_j(H-G), where A_j
is the indicator of their all-zero point. At a live selector query, write
rho=2^-(j-1). Its children are G and G+A_(j-1)(H-G); its disagreement is
d=rho gamma. The bound below is valid without balanced child means.

Set Delta=Hhat-Ghat. Parseval gives ||Delta||^2=4gamma. For each nonempty
residual-selector frequency the first child coefficient is zero and the
second is rho Delta_T. The parent sector masses are equal, and their
total binary entropy contribution is exactly 2(1-rho)d.

For the empty residual-selector row, the parent coefficients are
u_T=Ghat(T)+rho Delta_T/2 and v_T=-rho Delta_T/2. The sum of derivative
sector masses is rho^2 gamma=rho d. The sum of both masses in these rows
is 1-2rho(1-rho)gamma<=1. For positive row masses a,b,

    Psi(a,b)<=b log2(e(a+b)/b).

This is the usual binary entropy remainder inequality
-(1-t)ln(1-t)<=t. Log-sum/Jensen across the exceptional rows yields

    B_i(F)/d <= 2(1-rho)+rho log2(e/(rho^2 gamma))
              =2+rho[log2(e)-2+log2(1/gamma)+2log2(1/rho)].       (1)

No row is assumed to have the same coefficient or posterior as another.
Maximizing the final variable term over all positive real rho gives

    B_i(F)/d <= 2+log2(e)/sqrt(e gamma).                        (2)

The maximizer is rho=1/(2sqrt(e gamma)); enlarging the actual discrete
domain to all positive rho gives a valid upper bound. Thus every point-
selector query is strictly threshold-4 good whenever gamma>=1/4:
log2(e)<3/2 follows from ln2>2/3, and sqrt(e)>3/2 follows from e>5/2,
so 2+2log2(e)/sqrt(e)<4. Endpoints gamma=0 are irrelevant queries.
This criterion allows d to be arbitrarily small; it uses the shared source
and point-switch geometry, rather than a marginal entropy rarity bound.

## 2. Exact extension of the one-bit three-event separator

Let S,W,U,V be disjoint point indicators on s,L,R,T fresh control bits,
respectively. All literals are compatible, chosen active at zero. Let g
be an independent balanced Boolean core. Set

    B=WUV, C=U OR V, D=C-B,
    A=B+S D = WUV OR SU OR SV,
    F=1+A(g-1).

B is contained in C, so D is an actual indicator. Write

    alpha=2^-s, q=2^-R, r=2^-T, eta=2^-(L+R+T),
    beta=q+r-qr, e=beta-eta,
    J_B=(L+R+T)eta,
    J_C=R q(1-r)+T r(1-q), J_D=J_B+J_C.                     (3)

The cuts of B and C are disjoint: a U-coordinate cut of C has V inactive,
whereas a U-coordinate cut of B has V active; similarly for V. W cuts
only B. Hence J_D=J_B+J_C exactly, with no per-event overcounting.

The terminal probability and actual exclusive influence accounts are

    pi=eta+alpha e,
    I_sep=s alpha e,
    I_other=(1-alpha)J_B+alpha J_C,
    I_terminal=pi I(g),
    I(F)=I_sep+I_other+I_terminal.                           (4)

The first two terms are physical control contributions for a balanced
core. Their equality follows either by conditioning on S for the U,V,W
directions or directly by directed edge counts. The data contribution is
the actual activation probability pi times I(g); the entropy at the
stopping leaves is pi H(g), and remains part of the final ledger.

Query the s separator bits first. On the live all-active path at a node
with j separator bits left, rho=2^-(j-1), reach=2^-(s-j). The children
product is 1+A_(j-1)D(g-1), and therefore

    d_j=rho e/2,
    c_j=rho[J_D+(j-1)e+e I(g)]/2.                          (5)

The term (j-1)e is the odd-face price involving yet-unqueried separator
coordinates. It is precisely a term that cannot be repriced from an
unchanged remaining influence bank at every reached layer.

Summing ALL of these local face prices, without filtering for badness,
gives the exact full-price repeated-reserve request

    R_all=sum_j reach_j c_j
         =alpha[s J_D+e s(s-1)/2+s e I(g)].               (6)

At s=1 this agrees with A023's valid single-separator price:
c=J_D/2+e I(g)/2. Equations (3)-(6) independently reconstruct its boundary
and terminal partition; the original one-bit theorem is not refuted.

## 3. Actual Boolean counterfamily to unfiltered repeated reservation

Choose R=T=1, L=2s and g=z, one fair literal. Then dimension n=3s+3,
alpha=2^-s, eta=alpha^2/4, e=3/4-alpha^2/4, J_C=1/2 and
J_B=(2s+2)eta. Formula (4) is

    I_s=alpha[(s+1)e+1/2]+eta[(1-alpha)(2s+2)+1].

Formula (6) is

    R_all=alpha[s((2s+2)eta+1/2)+e s(s+1)/2].

Consequently, as s tends to infinity,

    R_all/I_s ~ s/2,
    R_all/(I_s-I_sep) ~ (3/10)s^2.                       (7)

These asymptotics have a direct all-integer sign bound. For s>=1,
e>=11/16, s alpha<=1/2, alpha<=1/2 and

    I_s/alpha <= (3/4)s+15/8 <= s+2,
    (I_s-I_sep)/alpha <=15/8,
    R_all/alpha >=(11/32)s(s+1).

Thus

    R_all/I_s >=11s/48,
    R_all/(I_s-I_sep) >=11s(s+1)/60.                     (8)

For every finite K>=0, any integer s>48K/11 refutes the rule
R_all<=K I_s. The stronger attempted price from a single final
nonseparator/terminal bank also fails quadratically. Each F_s is an actual
Boolean sign; I_s tends to zero and P(F_s=-1)=pi/2 tends to zero.

Scope: the false rule here reserves the COMPLETE local child-product face
price at EVERY reached separator layer, before testing whether that node
is bad. It is a conservative completion of a one-bit reserve, not A023's
stated one-bit theorem. This is not a refutation of the localized currency,
an optimal paid policy, a stopping theorem with actual terminal costs or
FEI. In particular it cannot be recorded as a failure of B05's EXISTS-tree
localized bridge; the next section proves the opposite on this family.

## 4. A paid actual localized stopping policy on the same family

Before separator exposure the two branch signs are G=1+B(g-1) and
H=1+C(g-1), with gamma=e/2. For R=T=1 and any L>=1,
eta<=1/8, e>=5/8 and gamma>=5/16>1/4. Lemma (2) makes every separator
query strictly 4-good, uniformly in s, L and the balanced core g.

After the first inactive separator bit, resolve B=WUV, a point conjunction;
after all separator bits are active, resolve C=U OR V. A point-conjunction
query has one constant child. Direct parent spectra give

    B/d=2(1-d)+Psi(d^2,(1-d)^2)/d
       <=2+log2(e)/sqrt(e)<3.

Indeed Psi(d^2,(1-d)^2)<=d^2 log2(e/d^2), because the two
exceptional masses sum to at most one. Maximizing
d[log2(e)-2+2log2(1/d)] over positive d gives log2(e)/sqrt(e),
as in the point-switch maximization above. The strict final inequality
follows from log2(e)<3/2 and sqrt(e)>3/2.

For C, U,V are each one bit here. Its first control query has d=1/4;
concavity gives B<=h2(1/4)<1=4d. When U fails, the remaining V split has
one constant child; when U succeeds, stop immediately at g. Every queried
control is therefore good, and the ACTUAL localized prefix charge is

    Q_bad,4(prefix)=0.                                  (9)

All histories are disjoint first revelations; the same core is reached at
most once on each history. The influence removed by this policy is exactly
I_sep+I_other, and terminal entropy is exactly pi H(g). Using the actual
physical entropy decrement Delta_i H=B_i+JS_i with JS_i<=2d_i/ln2 gives

    H(F)<=(4+2/ln2)(I_sep+I_other)+pi H(g).              (10)

The scalar JS bound is reconstructed in REPORT.md; it is not inferred
from this family. With g=z, H(g)=0, so H(F_s)<7I_s since ln2>2/3 implies
4+2/ln2<7. The full continuation querying the terminal literal has B=0,
so its complete-tree localized cost is also zero. This is an exact terminal
certificate, not a dropped arbitrary core entropy.

## 5. What remains unpaid

The saved finite grid also examines larger R,T, but zero signs there are
not an all-width theorem. Lemma (2) is sufficient when the two branch
disagreement gamma is moderate; it is inconclusive in the small-gamma
regime. The first unsupported universal line is a history-measurable
bad-node-only reservation rule for overlapping controllers with gamma<1/4,
which consumes each physical control and terminal-core account once. The
successful moderate-gap point-block policy supplies no universal terminal
entropy certificate. The explicit counterfamily only retires unfiltered
full-price repeated reservation, preserving all valid one-bit and localized
claims at their precise quantifiers.
