# Active-cylinder controller continuation with the original reference

Author proof; external review pending. Entropies are bits. Full FEI remains OPEN.

## 1. Interface and exact original ownership

Use A022@7's paid fixed block-first uniform-depth data frontier of
F(x,z)=b(x)(1-2 1[x=v] A(z)), b=g tensor t, t>=2,
g=-1 only at000, delta=8^-t, a=1-2A. Its bank is
B=4 I_data,remaining+delta H(a)-C-U >=13t/576,
with old 0<=U<=t/64 and COMPLETE reference costs C. The frontier
has exactly one active data cylinder h*, reach w=2^-d, conditional
point density eta=delta/w. Keep every other cylinder and its reference
unchanged. On h* retain its already converted positive data reference q.
Before any controller query its controller reference is the ORIGINAL
R_delta,a=(1-delta) point_empty+delta P_a, NOT R_eta,a.

Execute any finite adaptive controller-only tree on h*, permitting stopping
and coordinate choices based on earlier controller outcomes. No controller
query is executed on any inactive data cylinder. At an active controller
leaf e explicitly convert the reference to q tensor R_delta,a_e. Original
delta, original data reaches, q, U, all inactive costs, and old data-query
signed account remain. This is a prescribed conversion, not a declaration
that physical inheritance produced that reference for free.

The original entropy earmark is allocated as eta H(a) conditionally on h*
and zero on inactive cylinders, giving the SAME unconditional delta H(a).
For controller reaches p_e within h*, its exact spend is
K=delta[H(a)-sum_leaf p_e H(a_e)]. It may be signed. Therefore
K+delta sum_leaf p_e H(a_e)=delta H(a); no entropy is resupplied.

## 2. Conditional cross overhead

For any controller mean s, set r_delta(s)=1-delta+delta s^2 and
G_delta(s)=H(R_delta,a)-delta H(a). As reconstructed from A025@4,
G=phi(r_delta)-delta phi(s^2)+delta(1-s^2)log2(1/delta),
phi(u)=-u log2 u with continuous zero convention.

Actual active-cylinder controller marginal is R_eta,a: the coefficient of
each nonempty controller frequency has total squared mass eta P_a(T).
The empty mass is 1-eta+eta s^2 by Parseval. This statement uses actual
conditional density, not a reference reset. Complete controller CE obeys

 CE(R_eta,a,R_delta,a)-eta H(a)
   =(eta/delta) G_delta(s)+(eta/delta-1) log2 r_delta(s).

Multiplication by the ORIGINAL physical reach w, using w eta=delta, yields

 J_delta,w(s)=G_delta(s)+(1-w)log2 r_delta(s).                 (1)

The conditional data spectral marginal is a mixture of the unedited and
edited seed spectra with weights 1-alpha,alpha; hence data CE against the
fixed positive q and every remaining physical data influence are affine in
alpha=(1-s)/2. For an actual controller split s=(s0+s1)/2 these affine
terms cancel. Inactive cylinders are untouched, so their complete costs
cancel exactly without being discarded. The gain of the GLOBAL original
bank is exactly

 B_after-B_before=J(s)-[J(s0)+J(s1)]/2.                       (2)

## 3. Uniform curvature proof, not finite extrapolation

This part holds for ANY 0<delta<=1/64 and ANY 0<w<=1; actual one-point
frontiers additionally have w>=delta. For s!=0 put
u=(1-delta)/(delta s^2), c=1/ln2. Direct differentiation gives

 G''(s)=-2delta c[ln(1+u)-2u/(1+u)],
 (log2 r_delta)''=2delta c (1-delta-delta s^2)/r_delta^2.

For |s|<=1, u>=63 and ln(1+u)>=ln64=6ln2>4.
The exact inequality ln2>2/3 follows from
ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1), whose tail is positive.
Also 2u/(1+u)<2. Thus G''<-4delta c. The other term has

 (log2 r_delta)'' <=2delta c/(1-delta)<=2delta c*64/63.

Since 0<=1-w<=1, J''<2delta c(-2+64/63)<0. Derivatives
extend continuously across zero (s ln(s^2) tends to zero); monotonicity
of J' on either side and continuity establish concavity on all [-1,1].
All endpoints and constant controllers follow by continuity. Therefore
the exact gain (2) is nonnegative for every physical split. The scalar
proof is uniform in both t and controller dimension and has no canceled
bias denominator or limit exchange.

For an arbitrary finite adaptive controller-only tree on h*, summing
the physical reaches p_e gives

 B_final=B_initial+J(s_root)-sum_leaf p_e J(s_e)
        =B_initial+sum_internal p_e JensenGap_e
        >=B_initial>=13t/576.                               (3)

Only Jensen gaps are spent; no extra root bank is introduced. Concavity
and J(+/-1)=0 also imply J>=0, but this supplies no independent admission.
An arbitrary source controller still owes its explicitly supplied entropy.

## 4. Both terminal KLs and actual signed conversion

At each active physical split let C,H,D=C-H denote COMPLETE conditional
target CE, entropy and KL; bars average BOTH children. Put
DeltaH_F=H_parent-Hbar and DeltaH_a=H(a_parent)-Hbar(a_child).
Equations (1)--(2) give exactly

 w(C_parent-Cbar)=delta DeltaH_a+JensenGap,
 w(Dbar-D_parent)=w DeltaH_F-delta DeltaH_a-JensenGap.       (4)

Thus the combined change, including source-controller entropy spend and
the signed query account, satisfies

 DeltaB+w(Dbar-D_parent)+delta DeltaH_a-w DeltaH_F=0.       (5)

Both full child KLs remain, and the old data-query account is unchanged.
For physical inherited phase references the ordinary KL chain rule has
D_parent=erasure+outcome+average D_inherited. If kappa is the signed
average target-minus-inherited child KL, its NET cost is
kappa-erasure-outcome=average D_target-D_parent, precisely (4).
No raw positive conversion charge is assumed free and no positive-part
bound on kappa is claimed. Zero controller reference rows have zero actual
mass; no division by an unsupported row is used. All data references stay
strictly positive.

## 5. Scope, source review and first unsupported line

A025@4's common-controller-tree theorem is consumed, not duplicated: its
G calculus is independently reconstructed here; the NEW term in (1) pays
the active-cylinder-only transaction which A025 explicitly left open.
A022@7's numerical data-prefix admission remains conditional on its stated
review status. The present continuation proof is independent of its value:
ANY inherited bank B is preserved by this transaction under the hypotheses.

First unsupported universal line: after this active-only controller history,
an additional DATA query changes the active cylinder, physical reach and
already converted data reference. Paying that conversion while preserving
the current J, original entropy spend, U, all inactive costs and BOTH full
terminal KLs is not proved here. Arbitrary data-dependent controller queries
on multiple inactive cylinders and arbitrary influence-priced controller
entropy/source admission are also not claimed. FEI remains OPEN.
