# Pay a bounded interacting core once; expose the remaining dimension bill

Bits throughout. These are new fixed ROOT references, not a conversion from
an old spent reference. No branch entropy estimate is substituted for its
complete cross entropy. Core bits are physically shared, not cloned.

## Generic supplied-reference interface, including signed collisions

Let f(z,x) be any sign Boolean function, with s>=1 uniform core bits and
d>=1 remaining physical bits. Set f_z(x)=f(z,x). Every nonconstant slice
has a prescribed positive normalized reference q_z on nonempty x-subsets,
fixed before the spectral target. Constants have zero local cost. Let
k be the number of nonconstant slices, and if k>0 define qbar as their
UNIFORM mixture. If k=0 use the uniform nonempty x reference instead.
Define the following strictly positive normalized nonempty physical law Q:

    Q(empty,B)=1/[2(2^s-1)]                 for B!=empty core,
    Q(A,B)=qbar(A)/2^(s+1)                 for A!=empty, ANY B.
                                                               (1)

The first random bit selects core-only versus residual-present; the latter
draws A from the one fixed qbar and B uniformly. All core choices, sector
choices, branch-mixture priors and local subsets are included. Summing (1)
gives exactly1. qbar is selected from the representation before observing
the Fourier set; it is not a posterior or a free reset.

For A in the data cube put c_z(A)=f_z_hat(A). The ACTUAL physical coefficient
is the signed core Walsh transform

    fhat(A,B)=2^-s sum_z chi_B(z)c_z(A).                (2)

Orthogonality, not a positive pushforward of squares, gives

    P_A=sum_B fhat(A,B)^2=2^-s sum_z c_z(A)^2.

Define M=sum_(A!=empty) P_A=E_z Var(f_z),
N=sum_(B!=empty) fhat(empty,B)^2, and v=M+N=Var(f).
Also I_x=E_z I(f_z) exactly, M<=I_x and N<=I_z, where I_z is the actual
sum of influences of physical core coordinates. In particular I=I_x+I_z.
No independence across slices f_z is required; they may use identical data.

Let C_z=sum_(A!=empty)c_z(A)^2 log(1/q_z(A)), constants cost0, and

    Gamma=2^-s sum_(z,A!=empty)c_z(A)^2 log[q_z(A)/qbar(A)].

The sum includes only nonconstant slices. It is a SIGNED prior-mismatch
term; it need not be nonnegative. The EXACT complete nonempty cost is

    C_Q(f)=E C_z+Gamma+(s+1)M+[1+log(2^s-1)]N.        (3)

This follows by summing (1) against (2) and Parseval on each A. Since
qbar>=q_z/k pointwise, Gamma<=M log k<=sM (and Gamma=0 when k=0).
If C_z<=K I(f_z) for every nonconstant slice, K>=0, then

    C_Q(f)<=K I_x+(2s+1)M+(s+1)N
           <=(K+2s+1)I(f).                            (4)

Retaining log k gives the sharper M coefficient s+1+log k. This source is
paid once. Reconditioning recursively could charge it again, and is NOT
justified by (4). The O(s) dimension term is explicit, not suppressed.

## A dimension-independent local clause supplier for every residual

For arbitrary disjoint private OR clauses of widths d_j>=1 let
U=prod_j OR(X_j), a=EU, epsilon_j=2^-d_j, g=2U-1.
Prescribe rho_j=epsilon_j/2. Draw independent Bernoulli-rho_j clause masks
conditioned on a nonempty mask, and uniform nonempty coordinate subsets
inside active clauses. With t the set of active clauses, the exact law is

    q(A)=prod_active[rho_j/(2^d_j-1)]
         prod_inactive(1-rho_j) / [1-prod_j(1-rho_j)].  (5)

This reference is positive and normalized on every nonempty private subset.
It differs from the actual normalized spectrum; its activation probability
was halved. The negative log of the denominator contributes the NONPOSITIVE
term log[1-prod(1-rho)], which is retained in (5) before bounding.

For epsilon<=1/2, log2[1/(1-epsilon/2)]<=epsilon. To prove this, the concave
function ln(1-epsilon/2)+epsilon ln2 is zero at0 and positive at1/2, since
(3/4)sqrt2>1 (18>16 after squaring). It lies above its endpoint chord.
Also log2[(2^d-1)/rho]<2d+1<=3d. Thus

    -log q(A)<=S+3 sum_active d_j, S=sum_j epsilon_j.

Direct pivotal counting and the independent INDICATOR Fourier law give

    I(g)=2a sum_j d_j epsilon_j/(1-epsilon_j),
    sum_(A!=empty)ghat(A)^2 sum_active d_j=4a sum_j d_j epsilon_j<=2I(g).

Since Var(g)=4a(1-a), Var(g)S<=4aS<=2I(g). Therefore the ENTIRE local
nonempty cost satisfies C_g(q)<=8I(g), for every clause count and widths.
Inactive coordinates absent from a residual get an optional full-support
extension only if needed: in this application we use a fixed reference
supported on its relevant subset cube, then mix with a uniform data law
with weight1/2. This adds Var(g)<=I(g), yielding a strictly positive
reference on ALL nonempty data sets with C_g<=9I(g). If every slice uses
all private variables, no extension is necessary. The extension is paid
once per local code under the averaged physical I_x, not per output visit.

More economically, a slice with unused private coordinates can KEEP its
image-only q_z in (1), provided qbar covers every ACTUAL data spectral
support. Formula (3) and all inequalities still hold, with 0log0=0.
For the shared-core clauses below the all-zero core slice uses every
private variable, so qbar is strictly positive on ALL nonempty data sets.
Consequently the 8I supplier applies without the extra smoothing charge.

## All two-core interacting clause dictionaries

Let z1,z2 be physical Boolean core coordinates, and let private blocks X_j
be mutually disjoint of arbitrary widths d_j>=1. Fix ANY anchor subsets
T_j subset {1,2}, including empty and including all three nonempty types.
Put

    f=2 prod_j OR(z_(T_j),X_j)-1.                    (6)

For each core assignment, clauses whose anchors contain a1 disappear;
all remaining private OR clauses are disjoint. Constants have cost0 and
each other slice uses (5) on its surviving private blocks. Treat that law
as supported on the surviving coordinates in the common physical data cube.
Every actual nonempty slice coefficient is covered. The z=(0,0) slice
has ALL clauses present, so its q_z is positive on EVERY nonempty data
subset; thus qbar and Q in (1) are strictly positive everywhere.

Equations (3)-(4) with s=2,K=8 give the complete nonempty bound

    C_Q(f)<=8I_x+5M+3N<=13I(f).                      (7)

All local branch priors, clause identities, inactive masks, active subsets,
the four physical core Fourier choices and the sector are paid. The same
one reference handles arbitrary numbers of clauses of each nonnested type
{1},{2},{1,2}; no independent copy of either shared coordinate is used.
The actual empty/nonempty wrapper adds at most2I(f), so FULL cost<=15I(f).
With ONE common anchor k=1, the stronger form of (3) gives <=10I nonempty,
<=12I full. These use a DIFFERENT reference from A008's repaired law;
its29I/2 theorem remains correct and is independently reviewed here.

## Elementary full-wrapper bound used above

For any Boolean event of minority probability t<=1/2, edge isoperimetry
gives I>=2t log2(1/t). A short induction proves it: split event densities
t0,t1, use crossing influence>=|t0-t1| and
h2(u)>=1-|2u-1| to combine the inductive bounds. This induction holds at
all densities, so it applies inside the slices as well.
Let v=4t(1-t). For t<=1/4, h2(v)<=v log2(e/v)
<=4t log2[e/(4t)]<=4t log2(1/t)<=2I; the middle step uses that
x log(e/x) is increasing for0<x<=1. For t>=1/4, v>=3/4,
h2(v)<=1<=2v<=2I. Constants cost0. Thus the full wrapper h2(v)<=2I is
proved independently of FEI, and applies without a hidden lower bound I>=1.

## The growing-core uniform dictionary really has a dimension barrier

Take f=Maj_s(z) for odd s=2m+1, and add one unused data coordinate if the
interface requires d>=1. Every data slice is constant, M=0,N=1. The core
reference in (1) gives COMPLETE nonempty cost1+log2(2^s-1)>=s, whereas

    I(Maj_s)=s binom(2m,m)/4^m.

Induction gives binom(2m,m)/4^m<=1/sqrt(m+1): after squaring, the induction
step reduces to (2m+1)^2(m+2)<=4(m+1)^3, whose difference is3m+2>0.
Therefore C_Q/I>=sqrt(m+1) -> infinity. This is an ACTUAL Boolean family
refuting dimension-independent payment of this particular growing-core
reference. It is not an FEI counterexample. The full wrapper is zero here,
so it cannot repair the divergence. Removing the sector header still gives
the same divergence up to factor(s-1)/s.

The exact unpaid universal line is replacing the uniform core Fourier tag
and branch-mixture information in (3) by a single influence-paid JOINT core
reference for arbitrarily large interacting cores. No positive pushforward
of virtual squares is assumed. The signed Walsh step (2) is essential:
identifying two copies of OR2 gives actual I=1, not the disjoint3/2.
Bounded-core fusion is a source-complete explicit interface, not a universal
lemma or an unlimited-depth closure. Existing supplied-reference restriction
transport may be applied only with the SAME paid root Q and old debits;
this stage does not change references for free. Full FEI remains OPEN.

Taking the entire cube as a core is not a shortcut: then every data slice
is constant, and a universal influence-priced FULL core reference would
already imply FEI by Gibbs' inequality. Conversely the true spectral law
has full cost H. Thus arbitrary-core source pricing is FEI-equivalent.
The next useful lemma must exploit anchor-incidence geometry and signed
joint conditioning, rather than rename that universal source problem.
