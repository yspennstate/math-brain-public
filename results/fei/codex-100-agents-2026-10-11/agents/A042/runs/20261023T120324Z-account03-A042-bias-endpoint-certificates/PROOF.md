# Paid-sector dyadic activation: a seed singleton bill survives rare activation

Natural logarithms throughout. All functions are actual Boolean signs on finite
independent product cubes. Contract deterministic coordinates first. For each
occupied nonempty physical label T use P_T=v_T c_T^2 and choose j_T>=0 by
1/2<2^j_T|c_T|<=1. Set W_T=v_T4^-j_T. For an arbitrary seed g write

V=Var(g), a=(1-mean(g))/2, I=I(g), Delta_g=I-V,
A=sum_singletons P_T, M=sum_high P_T=V-A=Delta_g-R_g,
J_1=ln4 sum_singletons P_T j_T, J_hi=ln4 sum_high P_T j_T,
E_1=sum_singletons P_T ln(1/c_T^2), L_1=E_1-J_1,
L_hi=sum_high P_T ln(1/(2^j_T|c_T|)^2),
Z_1=sum_singletons W_T, Z_hi=sum_high W_T.

Here high means degree at least two and
R_g=sum_degree>=3(degree-2)P_T. At empty sectors use zero costs.
The new B09 reference Q_* freezes actual empty AND singleton masses and
normalizes W only on high labels: Q_*(T)=M W_T/Z_hi there. Its full ordinary
KL is K_*=M ln(Z_hi/M)-L_hi. All low likelihood ratios are exactly one.
This differs from the prior reference that rounded every nonempty coefficient.

## 1. Exact physical activation and the high-sector carry

Let X be independent Bernoulli e=2^-k, k>=1, and F=1-X+Xg. For nonempty T,

c_F(T)=e c_T, c_F(XT)=c_T/2, c_F(X)=-a,
P_F(T)=e^2 P_T, P_F(XT)=e(1-e)P_T,
P_F(X)=4e(1-e)a^2.

The original deficit split is Delta_F=e Delta_g+Delta_o,
Delta_o=e(1-e)V. All full dyadic composition carries are zero.
But freezing singleton masses changes the HIGH charge. Directly summing its
two disjoint sets (T high) and (XT with T nonempty) gives

J_hi(F)=e J_hi(g)+e(1-e)J_1(g)
             +ln4[e^2 k M+e(1-e)V].                    (1)

The actual outer binary gate has J_hi(o)=ln4 e(1-e)V. Therefore the
nonnegative paid-sector carry is

A_hi:=J_hi(F)-e J_hi(g)-J_hi(o)
     =e(1-e)J_1(g)+ln4 e^2 k M.                        (2)

It is not a full-rounding mantissa carry. Even with zero full carry, it can
transfer arbitrary seed SINGLETON scale into the final high sector.
The exact endpoint is

A_hi/Delta_o=J_1(g)/V+ln4 [k/(2^k-1)]M/V
 -> J_1(g)/V as k->infinity                            (3)

for every fixed nonconstant seed. Thus rare activation does not remove this
inherited singleton bill. Quantitatively the nonnegative remainder in (3)
is at most ln4 k/(2^k-1). Reflection of X covers a selected input probability
tending to one. Constant seeds and zero high sectors are handled below.

## 2. The original joint account, not a new seed reserve

Let h(t)=t^2 ln(1/t^2), h(0)=0. Direct coefficient substitution gives

E_1(F)=4e(1-e)h(a)+e^2 E_1(g)+ln4 e^2 k A,
L_hi(F)=e L_hi(g)+e(1-e)L_1(g),
E_1(o)=4e(1-e)h(a)+ln4 e^2 k V,
L_hi(o)=0.

Combining these with (2) proves the exact conservation law

A_hi+E_1(F)+L_hi(F)=E_1(o)+e[E_1(g)+L_hi(g)].             (4)

In particular the source account retains the entire final singleton entropy
and high mantissa. Dropping E_1(F) changes the ledger. The Boolean singleton
bound E_1(g)<=4Delta_g-2R_g and L_hi(g)<=ln4 M imply the original joint bank
bound in A041; these are payments from the same seed allocation, not new
capacity after old debit. One explicit bound on the transfer alone is

A_hi <= e(1-e)(4Delta_g-2R_g)+ln4 e^2 k M,

because J_1<=E_1. This upper bound does not authorize spending an already
booked singleton allocation twice. No universal payment of J_hi(g) follows.

## 3. Complete paid-sector references and signed ordinary-KL conversion

The final high mass and rounded high mass are exactly

H_F=e M+e(1-e)A,
Z_hi,F=e Z_hi+e(1-e)Z_1.                               (5)

These formulas contrast with the all-nonempty reference: freezing the seed
singleton sector makes its old rounded weights reappear inside the final
high sector. The complete flat Q_*,F freezes all actual low masses and uses
H_F W_F/Z_hi,F on high labels. The actual two-input outer gate has only
one high label, so Q_*,o=P_o and K_*,o=n_*,o=0, even though L_hi(o)=0
and its pair dyadic charge need not vanish. Compose that reference with
the COMPLETE seed Q_*,g via Q_tree(S)=P_o(B)Q_*,g(T)/V whenever the
outer label B contains the seed wire. The singleton X and empty masses
are exactly actual. This is a normalized complete law, preserves every
actual low mass and every occupied high atom, and has

K_tree=e K_*,g,
C_tree^+=E_o+e[E_1(g)+J_hi(g)+n_g],
n_g=M ln(Z_hi/M).                                     (6)

The zero-high convention is n_g=0. Full ordinary cross entropies append
the same actual empty entropy and physical-bias correction to both
corrected cross entropies. Using (4) gives the EXACT signed transfer

K_*,F-e K_*,g = C_flat^+-C_tree^+
             = n_F-e n_g-e(1-e)L_1(g),                 (7)
n_F=H_F ln(Z_hi,F/H_F).

This is a signed reference change, not a positive reserve. It replaces the
KL along with the reference and retains both full terminal laws. The scale
carry A_hi does not equal this normalizer/KL conversion; (4) is essential.
If either high sector vanishes, form its complete law first and omit the
undefined conditional ratios. All occupied labels still have positive Q.

## 4. Actual all-arity obstruction with a fixed fair selector

Take the balanced majority sign g_m on n=2m+1 fair inputs, m>=1. A coordinate
is pivotal exactly when the remaining 2m inputs tie. Hence every singleton
coefficient is p_m=binom(2m,m)/4^m, V=1,
A=(2m+1)p_m^2, and J_1=ln4 A j_m, where j_m is the dyadic cell of p_m.
These are actual Boolean derivatives and singleton Fourier coefficients.

Elementary induction, starting p_0=1 and
p_(m+1)/p_m=(2m+1)/(2m+2), proves

1/(4m+1)<=p_m^2<=1/(m+1).                              (8)

Indeed the lower comparison after clearing denominators has numerator
(2m+1)^2(4m+5)-(2m+2)^2(4m+1)=1. The upper comparison has positive
numerator4(m+1)^3-(2m+1)^2(m+2)=3m+2.
Therefore A>1/2. If m=4^r-1 for any integer r>=1, then p_m<=2^-r
and j_m>=r. For the FIXED selector e=1/2, (2) consequently gives

A_hi/Delta_o >= J_1/V > r ln2.                         (9)

Thus NO finite constant prices the paid-sector carry from only the fresh
outer activation deficit, even when the selector is fair/dyadic and all
full-rounding carries are exactly zero. The same unbounded lower bound
persists at the rare-selector endpoint (3). This is a counterexample to
that payment rule, NOT to FEI: the original inherited seed deficit is
Delta_g=(2m+1)p_m-1 and remains in the joint account (4).

This complements A044's arbitrary-selector, fixed-seed full-carry obstruction.
Here the selector is fixed fair, seed arity grows, and the obstructed charge
is the NEW high-sector carry after singletons are frozen. Neither result
refutes A042's previous zero-full-carry theorem or A041's joint-bank theorem.

## 5. Endpoints and exact remaining universal obligation

If g=1 then F is constant and all costs vanish. If g=-1, one selector gives
a signed literal with Delta=0, no high sector and complete Q=P; omit V=0
ratios. At e=0 contract X and F is constant. At e=1 contract X and F=g;
no positive-variance selector law is invented. If g is a signed literal,
its only nonempty normalized coefficient has magnitude one, J_1=0,M=0;
then A_hi=0 even though F can have a nonempty high atom. These cases
explicitly cover zero deficit, zero high mass and unit conditional atoms.

The first unsupported universal line remains payment of the arbitrary
inherited high-degree charge J_hi(g) from unused ORIGINAL capacity with
the exact singleton and mantissa refunds, ordinary KL and full terminal
laws retained. Equations(2)-(9) prohibit charging all inherited singleton
transfer to a fresh outer gate; equation(4) supplies the correct existing
owner. Full FEI remains OPEN. Independent review of this new obstruction
and ledger specialization is pending; finite certificates do not establish
the all-arity conclusion without induction(8).
