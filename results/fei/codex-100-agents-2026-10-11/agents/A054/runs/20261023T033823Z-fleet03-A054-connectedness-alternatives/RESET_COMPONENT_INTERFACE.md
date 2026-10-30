# Inherited component labels after an input reset

All cubes are finite and uniform. Fourier and Shannon entropy use bits.
Let g=1_U, f=1-2g, p=|U|/2^n>0, n>=2. The labels L are the ACTUAL
connected components of U before a reset. Let T be an invertible affine
INPUT map, f'=f composed with T, g'=g composed with T. Labels are pulled
back by this same T. No output-character multiplication is allowed here:
it need not preserve the support or its mass.

Write d_i=Inf_i(f') and define the directed crossing probability

    gamma_i=P[g'(X)=g'(X+e_i)=1, L(TX)!=L(T(X+e_i))],
    gamma_A=sum_{i in A} gamma_i.

For a queried block A of width r, retain the old labels and define W_A
from their physical fiber masses exactly as in A054 stage17. The labels
need not be connected after the input map. Zero fibers contribute zero.

## 1. The exact crossing interface

For disjoint inherited indicators g'_l, direct counting gives

    sum_l 4 E_A(g'_l)=I_A(f')+2 gamma_A.                    (1)

A boundary edge of U changes one indicator and contributes equally to
both sides. An internal edge with different labels changes two indicators,
but does not change g'. Its two changed indicators give the extra factor2.
All probabilities are directed, using both endpoints with weight2^-n.

Equivalently, a singleton conditional fiber with two occupied vertices
has entropy one if they share a label and zero given L if their labels
differ. Thus

    H(X_i|X_-i,L,g'=1)=1-d_i/(2p)-gamma_i/p,
    W_{i}=d_i/2+gamma_i.                                 (2)

The chain rule and conditioning reduce entropy, so for every block

    2W_A<=I_A(f')+2gamma_A.                               (3)

Consequently the exact corrected admission maximum is

    max_{empty != A proper}(W_A-gamma_A)/(|A|p)
        =max_i d_i/(2p).                                 (4)

The upper bound follows from (3); singletons attain it by (2). This
extends the preceding stage's singleton ceiling through arbitrary input
charts. Original connectedness cannot be reused after a reset as if
gamma were still zero. Recomputing new actual labels would remove gamma,
but would also change the inherited component excess and its terminals.

The raw spectral terminal ledger is still exact for these disjoint labels:
Delta=F(g')-sum_l F(g'_l)=X_A+Z_A, where
X_A=Lambda_A(g')-sum_l Lambda_A(g'_l) and Z_A is the mean actual-child
labelled excess. No sign or separate free bound on Z_A is asserted.
The payment below controls the complete actual L_A, so Z_A remains
inside that ledger rather than being discarded when gamma is paid.

## 2. Influence release does not automatically pay the crossing flux

Let I^L(g)=sum_l 4E(g_l), and assume the input reset releases
rho=I(f)-I(f')>=0. Before the reset, labels are actual components and
I^L(g)=I(f). After it, (1) gives I^L(g')=I(f')+2gamma_all. Therefore

    rho_L:=I^L(g)-I^L(g')=rho-2gamma_all.                  (5)

rho_L is SIGNED. If it is negative, a free payment 2gamma<=rho is false.
This is a second interface, distinct from the raw Fourier terminal
component excess; neither can be discarded.

An explicit counterfamily uses bits a,b,c,d and
Q=(-1)^(ab+cd), q=2^-k, k>=2. Define

    F_k=1-A_k+A_k*(-Q),

where A_k is the event that k fresh controls are zero. Its negative set
has two actual components at control0: the nine vertices with ab=cd=0,
and the singleton1111. The first is a product of two three-vertex paths.
The negative mass is p=5q/8.

Apply the input shear T(a,b,c,d)=(a+c,b,c,d), controls fixed (mod2).
Both root and reset have data directional influences q/2 and control
influences5q/4. Every nonzero data translation costs q/2; any translation
using a control costs5q/4. Hence both are full-affine influence minima:
each parity costs at least the largest coordinate cost in its support,
and all costs are <=1/2 for k>=2. Finite cheapest-basis threshold counting
proves this last criterion; no numerical orbit search is used.
The squared Fourier law has full affine span: all nonzero data rows
and control-only rows are nonzero, since Q is bent with mean1/4.

In the reset chart, vertices10 and14 (a is the low bit) are adjacent
along c and lie in different inherited negative labels. This is the
only crossing edge. Thus

    rho=0, gamma_c=q/8, gamma_all=q/8, rho_L=-q/4,
    W_c=3q/8 >= p/2=5q/16,
    I_c=q/2 < p=5q/8.                                    (6)

Omitting gamma would falsely infer I_c>=p from this fiber threshold.
Correcting it gives W_c-gamma_c=q/4<p/2. This does not claim that the
actual signed query is unpaid; only the free inherited-label inference
and the putative bound2gamma<=rho are refuted. Total influence is
(2+5k/4)q and tends to zero. No FEI counterfamily is asserted.

## 3. A paid crossing interface, with the original debit retained

Set a0=2/ln2+4/(e ln2), C=4+a0<37/4. The prior universal raw/sign
row bound, which does not require component labels, states

    L_A(f')<=4rp+a0 I_A(f').                              (7)

Suppose rho>=0 and an amount u of this reset's release is already
booked, with 0<=u<=rho. Its UNUSED release is R=rho-u. If

    2gamma_A<=R  and  W_A>=rp/2,                          (8)

then (3) gives rp<=I_A+2gamma_A and (7) yields

    L_A<=C I_A+8gamma_A<=C I_A+4R<=C(I_A+R).              (9)

This pays the explicit crossing interface8gamma_A using at most4 per
unit of unused reset release. The booked u is not offered again. A
simple sufficient geometric condition is rho_L>=u, because (5) then
gives2gamma_A<=2gamma_all=rho-rho_L<=rho-u. This condition is about
TOTAL energy of the inherited labels, not merely influence reduction
of the Boolean union. The counterfamily violates it exactly.

This is a local theorem with complete actual terminals. Let h_x be the
actual child after resetting and querying. Entropy preservation and
the restriction identity give, for every K,

    D_K(f)+E_x[K I(h_x)-H(h_x)]
        = L_A(f')-K[I_A(f')+rho].                        (10)

No child entropy or component term is suppressed. For u=0 and K>=C,
conditions(8) imply the right side is nonpositive. In a least-essential-
dimension positive K-witness every proper actual child h_x is smaller,
so its reserve is nonnegative, contradicting(10). Thus this is an
explicit paid critical class with arbitrary overlap, inherited labels,
and no support-mass lower bound. It is not claimed universal or closed
under restriction. If a previous query already booked u>0, use only
R in (9) and retain the earlier debit in that tree's original ledger.

For a reset AFTER a preceding query, (9) can be used in its descendant
only if that release was not spent on the preceding query, or the
remaining R still satisfies(8). An affine optimum and a labelled
energy optimum are different optimization problems.

For a boundary example, shear a two-bit parity to a literal. Its two
negative singleton labels become adjacent: rho=1, gamma=1/2, rho_L=0.
The new dummy-coordinate query meets the uncorrected fiber threshold
and is harmless, while its label flux uses ALL release in(8). Booking
u=1/2 before that query leaves R=1/2<2gamma=1, so that same proof cannot
spend the full release again. This is an admission failure of the
budget hypothesis, not a claim that the zero-entropy query is unpaid.

## 4. An executable labelled rank reset

For a nonzero physical translation v define w(v)=P[f(X)!=f(X+v)] and
gamma(v)=P[X,X+v in U with different original labels]. Put
ell(v)=w(v)+2gamma(v). The mutually exclusive edge types imply
0<=ell(v)<=2. For a basis (v_1,...,v_n), the input map with these columns
has labelled influence sum_j ell(v_j). It does not center output signs.

Sort all nonzero directions by ell and greedily retain independent ones.
For r_ell(t)=rank{v:ell(v)<=t}, the minimum possible labelled influence is

    min_basis sum_j ell(v_j)=integral_0^2 [n-r_ell(t)]dt.   (11)

At every threshold the greedy selected vectors span all directions seen
so far; no other basis can have more cheap members. Integrating their
complement counts proves(11), including ties and zero costs. The original
coordinate basis is a competitor. Thus the minimizer has rho_L>=0,
rho>=2gamma_all, and automatically supplies condition(8)'s flux bound
when u=0. With an existing debit u, rho_L>=u is a sufficient test for
all blocks: it is exactly the condition2gamma_all<=rho-u. One can test
that criterion by the exact same rank sum; a particular block can pass
its weaker2gamma_A test even when the all-coordinate test fails.

This is a constructive flux payment, not a lower bound guaranteeing
W_A>=rp/2. It also does not supply nonzero funding at a canonical root:
if f already minimizes ordinary influence over all input bases, then
every basis has union influence at least I(f), and labelled influence
is at least union influence. The labelled minimum equals I(f) because
the identity achieves it. Hence rho_L=rho=gamma_all=0 there. Useful
new release must arise after an actual query or outside that canonical
case, and cannot have been spent on the preceding query already.

## 5. Remaining universal line

Rank-certified affine release by itself cannot control inherited-label
crossing flux, even on actual full-span affine-minimal sources with
arbitrarily weak total influence. To combine component credit with the
B11 rank ledger, select an original query/reset/next-query fragment
whose SAME remaining release covers its crossing flux and complete
signed row bill, or use a different proved bound on that flux. Universal
existence of such a fragment on a genuine high-K minimal source is the
first unsupported line. Conditions(8) and rho_L>=u are sufficient
hypotheses, not a claimed consequence of criticality.
