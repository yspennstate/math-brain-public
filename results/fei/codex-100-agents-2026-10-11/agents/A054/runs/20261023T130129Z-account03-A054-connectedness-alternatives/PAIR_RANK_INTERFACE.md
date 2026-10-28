# Rank-completed alignment on the ORIGINAL pair partition

All cubes are finite, uniform and binary. Fourier entropy H uses bits;
I is physical total influence. Fix an ORIGINAL proper pair A, its
outside translation space W, d=dim W=n-2, and V/W=F2^2. No terminal,
mixed Fourier row or earlier debit is removed. This strengthens the
existing A054 interface mechanism using A052's new signed phase test.

## 1. Exact cost of all partition-preserving input resets

For an actual Boolean sign F define c(v)=P[F(X)!=F(X+v)]. For each
nonzero quotient q define b(q)=min_{v+W=q} c(v). Put

    m_W=min_{B basis of W} sum_{v in B} c(v),
    m_Q=min_{Q basis of V/W} sum_{q in Q} b(q),
    J_A(F)=m_W+m_Q.                                           (1)

Then J_A(F) is EXACTLY the least influence of F after an invertible
affine INPUT map preserving the ORIGINAL A partition, up to bijective
renaming of the four query values. Such a basis consists of a basis of
W and lifts of a quotient basis. Its costs add. Conversely arbitrary
minimizing lifts plus a minimizing basis of W form a full basis and an
allowed map. There is no compatibility loss. Input shifts leave costs
unchanged. Output characters are not silently included in this minimum.

Writing E_W(t)={v in W\{0}:c(v)<=t} and E_Q(t)={q!=0:b(q)<=t},

    J_A(F)=int_0^1 [d-rank E_W(t)]dt
             +int_0^1 [2-rank E_Q(t)]dt.                     (2)

Finite weighted greedy basis exchange proves each integral: at every
threshold a minimum basis spans the whole threshold set. For a pair,
m_Q is simply the sum of the two smallest of the THREE quotient costs.
Every lift is an actual physical direction. Dependent parity gains are
not summed. Root influence I(F) is an available competitor, so the
partition-preserving release R_A(F)=I(F)-J_A(F) is nonnegative.

## 2. Rank-completed full mixed-row alignment

Let f have complete original cofactors g_u on W, u in F2^2. Replace
ONLY branch r by s chi_v g_r, giving the actual Boolean F. Keep both
signs s: entropy is sign-dependent for a pair. Write E=H(F), E0=H(f),
Delta=I(F)-I(f), R=I(F)-J_A(F). Physical edges give A052's exact

    Delta=[B_v+C_(1,0)+C_(2,0)-s(C_(1,v)+C_(2,v))]/4,           (3)

where B_v=sum_(j in v)(1-2 Inf_j(g_r)) and
C_(j,v)=E[g_(r+e_j) g_r chi_v]. Every signed Fourier coefficient is
(1/4)sum_u (-1)^(z dot u) b'_u(T), including ALL mixed T,z rows.

Assume the INITIAL source maximizes D_K=H-KI in its finite joint orbit
of affine input maps and cubic output phases, K>0. More weakly, assume
stationarity under these actual branch-rematch/partition-reset composites.
The rematch phase has degree<=3, and the reset preserves H. Comparing
with the actual minimizing input chart from (1) gives

    E-E0 <= K[J_A(F)-I(f)] = K[Delta-R].                    (4)

Thus the explicit interface KR must be subtracted from the physical
phase cost in A052's alignment test. Equivalently the compensated
phase price

    Omega=E0-E+K Delta

pays KR: Omega>=KR. This is a proved controlled-excess inequality in
the stated critical normal-form class. It is strictly stronger whenever
R>0; generic physical-phase stationarity alone is insufficient to
justify the additional input reset. No universal source is asserted
to exist. A hypothetical least-essential-dimensional positive witness
can be chosen in this finite joint orbit before any bank is spent:
degree<=3 is preserved by affine substitution, the group is finite,
and a positive maximizer with smaller essential dimension would
contradict least dimension. Descendants do not inherit stationarity.

## 3. The FULL terminal bank and the retained phase interface

Let a(h) be minimum influence in the complete affine-input/output-
character orbit of a smaller Boolean sign h, and define

    t=(1/4)sum_u a(g_u),
    S*=(1/4)sum_u[K a(g_u)-H(g_u)],
    L_F=E-(1/4)sum_u H(g_u),
    Pi=Omega-KR = D_K(f)-[E-K J_A(F)].

The four terminal entropies and a-values survive the rematch and the
partition-preserving input reset, since every complete child is merely
character-multiplied, affinely relabelled or translated. Hence exactly

    D_K(f)+S* = L_F-K[J_A(F)-t]+Pi.                         (5)

This identity holds without stationarity or criticality; Pi can then
be negative. Under (4), Pi>=0. Genuine least essential dimension also
gives S*>=0. This distinction is essential: small absolute error and
phase stationarity alone do not make a negative terminal bank eligible.

If u units of R have already been booked, 0<=u<=R, retain
Pi_u=Omega-K(R-u)=Pi+Ku. The SAME expression is

    D_K(f)+S*=L_F-K[(J_A(F)+u)-t]+Pi_u.                    (6)

Here J+u is the scalar cost when only R-u is offered as unused release;
no Boolean function with that exact influence is asserted. Omitting
Pi or Pi_u counts an actual entropy/influence change as new funding.
In particular, a paid rematched row L_F<=K(J-t) need not pay the
ORIGINAL source. Its correct test retains the additional Pi.

This is the nonlinear counterpart of A052's previous input-affine
no-free-preconditioning identity. The rank-completed constraint is useful
structure, but the price does not disappear when the rank is optimized.

## 4. Connection to the inherited-component crossing interface

A phase rematch changes the sign support: old component labels CANNOT
be carried through it as labels of the new support. For the actual
new F one may start its actual component labels, then transport those
labels through the minimizing INPUT chart. With directed crossing
flux gamma_B along a subsequent queried block, A054's earlier exact
label identity is I^L_B=I_B+2 gamma_B. If its fibre threshold holds
and 2 gamma_B<=R-u, then the explicit entropy interface8 gamma_B is
paid by4(R-u), at the same C=4+2/ln2+4/(e ln2). This is local payment
for the NEW function and the SAME unused R-u. To transfer it to the
ORIGINAL root one must still include Pi_u and every terminal in (6).
The present theorem gives Omega>=KR at an eligible initial critical
normal form; it does NOT authorize spending Omega and R separately.

## 5. Exact frontier and first unsupported line

An explicit genuine critical guard is already three-dimensional. Take
f negative only at000 and K=2. Then I0=3/4 and
H0=4-(9/8)log2(3), so D2=5/2-(9/8)log2(3)>0, with integer certificate
2^20>3^9. Exhaustive exact checks of all22 labelled smaller functions
give H<=2I; all256 labelled three-bit sources give D2<=D2(f). Thus
this is a genuine least-dimensional GLOBAL deficit maximizer, stronger
than just phase stationarity. Fix original A=(0,1); all four child
entropies and affine/character minima are zero, so S*=t=0.

Rematch branch r=1 (the previously constant branch) by the character
of outside bit2, sign+. The new negative set is {0,5}; I(F)=3/2,
H(F)=2. Columns(5,2,4) preserve the original pair partition and give
J=1: outside cost1/2, quotient costs0 and1/2. Hence R=1/2. Querying
the original pair after this reset has full L_F=2, so its complete
optimized-terminal bill is EXACTLY paid at K=2. Nevertheless
Pi=D2(f)>0 and Omega=Pi+1. Dropping Pi would falsely exclude the
actual critical source; retaining it gives(5) exactly. This is a
low-rate counterguard, not a counterexample to FEI or to any correctly
qualified sufficiently-high-K selection theorem.

Equations(1)--(4) turn the signed original-pair alignment into an exact
two-rank oracle: internal directions and quotient lifts are optimized
together, without changing the physical query partition. Equations
(5)--(6) keep the complete phase-interface price and old debit visible.
The frozen checks include the genuine low-rate four-bit point-defect
guard, with its positive deficit certified by2^144>7^49; least dimension
at K=3 is checked on all labelled smaller sources. Its full cubic-orbit
maximality is a source result, not re-proved from a sampled census here.
Local composite stationarity under EVERY tested original-pair rematch
and ALL allowed input bases is verified exactly, via the minimum(1).

FIRST UNSUPPORTED UNIVERSAL LINE: for sufficiently high absolute K,
combine rank-completed alignment(4), genuine nonnegative complete child
reserves and mixed-row Boolean constraints to select an ORIGINAL proper
pair whose full bill INCLUDING Pi and all old debits is paid. A large
R, an input chart change, or local component payment of the rematched
function alone does not establish this. Full FEI remains OPEN.
