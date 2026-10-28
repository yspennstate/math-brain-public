# A floor-reference handoff pays an unbounded nested canonical-reset chain

All logarithms and complete-reference costs are base 2. This is an explicit
family/history theorem. It does not prove universal FEI or fund new Boolean edits.

## 1. Actual source, actual initial model, and unchanged bank

Let h_j=1-2*1_(all j inputs zero), including h_0=-1. For every w>=4 and m>=2,
take g=h_w*h_2 on k=w+2 source bits, m padding bits and one fair selector.
Let n=k+m, delta=2^-n, and F be g except its value at the all-zero point of
all n+1 bits is reversed. In particular g(0)=+1. The source reference is
R=P_g, with its actual full cost c=H(g), and is never renewed.

Put q=2^(1-w). The exact source influence is I_g=1+w*q>=1. A095 stage16's
signed-profile calculation gives c<4<=4I_g. Alternatively the source entropy
formula is c=2-(1-q)^2 log2((1-q)^2)+(2q-q^2)(2w-2); its bound
c<2+(4w-1)q-(2w-2)q^2<4 follows from (4w-1)2^(1-w)<=15/8.
Fix C0=4 and K=4C0+15=31 ONCE.

The incoming model is NOT A095's old canonical model. It is exactly A011's
floor: on n data-frequency bits,

 M(S)=[P_g padded(S)+3delta*2^-n]/(1+3delta),

lifted by the TRUE conditional selector-frequency law of F. Every data
marginal is positive. The reference is normalized, including all true-zero
atoms. A011's general-envelope interface, reconstructed in A094 stage19
DERIVATION section2, gives the complete cost

CE(F,Qfloor)<=2c+15B,  B=delta(n+1).

For completeness this used envelope bound has a short independent derivation
in the present normalized-source/fair-selector case. Write a for the padded
source Fourier coefficient. The actual data marginal is
q_S=(a-delta)^2+delta^2<=2a^2+3delta^2. Every M(S)<=1, so all log losses are
nonnegative. Since M(S)>=(a^2)/(1+3delta) and
M(S)>=3delta^2/(1+3delta), data CE is at most

 2c+(2+3delta)log2(1+3delta)+3delta(2n-log2 3).

Here n>=8, delta<=1/256, log2(e)<3/2, and
(2+3delta)log2(1+3delta)<10delta. Thus data CE is below
2c+(6n+10)delta. The selector-frequency nonempty mass is exactly delta;
its conditional entropy is <=h2(delta)<=delta(n+3/2). The full lifted CE
is consequently below 2c+(7n+23/2)delta<2c+15B. This rederivation checks the
actual control kernel as well as the data floor, without importing an
arbitrary-source or padding-prefix payment theorem.

All k source edges at the edited point were pivotal. Set E=k delta and
G=(m+1)delta, so B=G+E and literal edge counting yields

 I(F)=I_g+G-E.

Since k*2^-k<=1/2 for k>=1 and m>=2, E<=1/8<=I_g/8. Hence the UNUSED
ORIGINAL bank, before external old bookings, obeys

 31I(F)-CE(F,Qfloor)
 >=31I_g-2c+16G-46E >=(69/4)I_g+16G.       (1)

This uses only the initial general-envelope cost, not A011's padding-first
policy or identification of a canonical reference with a floor reference.
Permit an existing nonnegative external debit U<=(69/8)I_g, equal numerically
to A094's enlarged allowance at C0=4. It is a real additional liability in
this ledger; no source cost or terminal is erased to admit it.

## 2. Physical inheritance and the complete ledger

Use actual normalized posterior transport at every physical query. For parent
law P and model Q, let r be Q's marginal after deleting queried membership,
and p=(P0+P1)/2 the actual marginal. Define raw_b=r*P_b/p on p>0, raw_b=r
on p=0, Z_b=sum raw_b, Q_b=raw_b/Z_b. Thus Z0+Z1=2, retaining reference
mass on true-zero fibers. Positive true support and finite cost imply Z_b>0.
Likelihood disintegration gives

 D(P||Q)-average_b D(P_b||Q_b)
 =conditional spectral KL-average_b log2 Z_b>=0.       (2)

For any finite adaptive query tree the full signed terminal ledger is

 L=H(F)+sum_terminal reach(v) D(P_v||Q_v)
  =sum_internal reach(v) DeltaH_v+sum_terminal reach(v) CE(P_v,Q_v).

Without model resets it is at most the starting complete CE by (2).
A reset at physical reach lambda changes it by exactly
e=lambda[CE(P,Qfresh)-CE(P,Qinherited)], with the actual CURRENT reference.
Both full sibling terminals stay in L. Since normalized reference costs are
nonnegative, e^+=max(e,0)<=lambda*CE(P,Qfresh). Consequently

L<=CE(F,Qfloor)+sum e^+                          (3)

at every intermediate frontier, even if no negative reset credits are reclaimed.
This is an upper bound, not an equality asserting that transport has zero loss.

There is also a STRONGER accounting statement retaining every complete query
release instead of reclaiming the physical divergence losses. At each query
charge its complete release CEparent-average CE_inherited_children, using the
current model before any child reset. This release is nonnegative because
both spectral entropy and complete divergence contract. Let B_full be the
sum of those reached complete releases PLUS all complete current terminal
CE. A query preserves this bill exactly; a reset adds its actual signed e.
Therefore B_full=CEroot+sum e, and

 L<=B_full<=CEroot+sum e^+.

The gap B_full-L is the nonnegative accumulated physical divergence release.
Thus (3) and the final reserve below hold even when every such release remains
booked and no physical divergence credit is reclaimed. The exact checker
reconstructs BOTH bills and their distinct identities; they are not equated.

## 3. Genuine handoff and two narrow resets

Execute ANY finite adaptive tree querying only wide coordinates. Its unique
all-zero path has depth d, residual width t=w-d and reach rho=2^-d. Every
other leaf retains its entire actual inherited model. Do not query padding or
selector before the reset chain is over.

At this leaf query the first narrow bit. Reset only its zero child, actual
reach rho/2, to (1-eta)Qcan(h_t*h_1)+eta Ufull for any eta in[0,1/4].
Then query the second narrow bit INSIDE that zero child, using its current
model. Reset only child00, reach rho/4, to Qcan(-h_t). These are references
for the ACTUAL residual Boolean functions, not surrogate spectra.

Here Qcan(a) means the exact A095 support completion for a source a with
a(0)=+1 and its selector/padding point edit: put (1-W)P_a on its true old
support, epsilon^2 on every other full frequency, epsilon=2^(-source bits-m),
W=2epsilon-|supp(P_a)|epsilon^2. Preserve zero atoms. At t=0 h_0=-1, so
h_0*h_1 and -h_0 are actual characters/constants with the indicated signs.

A095 stage17 DERIVATION sections2-3 proves, for EVERY integer t>=0,m>=0,

 CEcan(h_t*h_1)<4, CEcan(-h_t)<4;
 both costs are <2 when t>=4.                     (4)

The first mixture adds at most log2(4/3)<1/2 to its full cost. If d=0 then
t=w>=4; if d>=1 then rho<=1/2. Therefore its actual positive debit is <5/4,
and the second actual positive debit is <1/2. This argument is independent
of the incoming inherited reference. In particular it applies to the actual
floor-root posterior here, not only to the old canonical-root history.

## 4. Arbitrarily many subsequent remaining-wide resets

After both narrow bits are zero, query remaining wide coordinates on the
surviving all-zero path in any order. At any chosen subset of those t queries,
reset only the zero child to its exact canonical Qcan(-h_(t-j)). At the j-th
such query its ORIGINAL physical reach is rho*2^(-j-2), regardless of which
earlier resets were performed. Every one child stops with the FULL model
inherited from the current reference. Its complete terminal is retained.

By (4), the sum of all these positive reset debits is strictly less than

 sum_(j=1)^t 4*rho*2^(-j-2)
 =rho*(1-2^-t)<=1.                               (5)

For t=0 there are no such debits and the sum is zero. Thus the entire handoff,
two narrow resets, and an UNBOUNDED number (as w grows) of subsequent nested
canonical resets have sum e^+<11/4. Any further finite physical queries using
inheritance and no new reset preserve (3). Every intermediate frontier obeys
the same bound; no later negative credit funds an earlier debit.

Combining (1),(3),(5) and the old U gives, at ALL these frontiers,

 31I(F)-U-B_full >(69/8)I_g+16G-11/4
            >=(47/8)I_g+16G>0.                   (6)

The same bound holds with L in place of B_full. The second inequality uses
I_g>=1. Both complete terminal costs at every
query, all previous signed charges, and the external old booking remain.
An independent terminal tensor with its separately paid complete reference
is additive and does not finance this core bank. No rate, source model or
point edit is renewed. This statement neither claims nor requires an
individual terminal cost <=31 times its own residual influence.

## 5. Exact gap and finite verification boundary

The new conclusion is a compatible floor-to-canonical handoff followed by a
dimension-unbounded nested reset chain for this explicit family, at the SAME
original supplied K=31 and with nonvanishing old U. It does not transplant the
previous canonical-root charge value e1>1/10; that charge involved another
incoming model. The actual charges here must be reconstructed from Qfloor.

The analytic proof of the infinite width/padding, eta continuum and all adaptive
tree quantifiers is (1)-(6), together with the source-complete canonical cost
bounds (4). Finite checks verify implementation, not these quantifiers.
The first unsupported universal continuation is paying conversions on many
simultaneously active branches, or creating a new Boolean point edit, without
geometrically decaying ORIGINAL reach or a new influence-priced source.
The fixed original source reference hypothesis also remains essential.

NEXT should test aggregation where disjoint reset paths have large total reach,
retaining actual inherited floors, old debits and both full terminals. That
removes the sole structural payment mechanism used in (5) and directly tests
the C020/C024 universal transfer gap. Full FEI remains OPEN.
