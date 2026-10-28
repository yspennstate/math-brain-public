# A prescribed tail reset through the signed tag collision

All entropy, KL and cross entropy are in bits. Inputs are original independent
uniform physical coordinates. References below are normalized probability laws,
not discarded subprobabilities. Let a(u) be A079's displayed four-bit ternary
row, b(u)=1-a(u)^2, and let h(x) be ANY Boolean seed on fresh coordinates.
At ANY physical u restriction the same notation denotes the actual restricted
rows. Thus a*b=0 pointwise, a^2+b^2=1 and b is an indicator. Set

    F(z,u,x)=a(u)+z b(u)h(x), A_U=ahat(U), B_U=bhat(U),
    alpha=E a^2, beta=E b^2, m=E h, r=m^2, p_T=hhat(T)^2.

F and the two tag children G_sigma=a+sigma*b*h are ACTUAL Boolean functions.
Parseval gives sum A_U B_U=0, alpha+beta=1. No phase admission or FEI
claim about an arbitrary normalized amplitude vector is substituted.

## 1. Complete incoming reference and actual collision

Supply ANY normalized source reference R with finite CE(p,R). Write t=R(empty).
The tagged incoming reference, with all reference-only atoms retained, is

    Q(0,U,T)=A_U^2 1{T=empty}, Q(1,U,T)=B_U^2 R(T).

It has total mass alpha+beta=1. Its true law substitutes p for R, and

    CE(F,Q)=H(F)+beta D(p||R).

The tag children have complete TRUE spectra

    P_sigma(U,empty)=(A_U+sigma*m B_U)^2,
    P_sigma(U,T)=B_U^2 p_T for T!=empty.

Their vacuum masses are alpha+beta*r, not alpha and not r. The coherent
vacuum entries must keep the SIGNED actual m and the Fourier signs of A,B.
Both children have unit total mass because sum A B=0. Biased seed phases
cannot be guessed from the source reference's vacuum probability t.

## 2. Explicit fresh references with an arbitrary prescribed tail target

For r<1, finite source CE implies t<1. Define the normalized nonempty seed
laws p^tail_T=p_T/(1-r), R^tail_T=R_T/(1-t). Let S be ANY prescribed
normalized law on nonempty seed frequencies, including reference-only labels.
Choose 0<=epsilon<1 and define M=(1-epsilon)R^tail+epsilon S. Prescribe
BOTH fresh child references by

    Q'_sigma(U,empty)=(A_U+sigma*m B_U)^2,
    Q'_sigma(U,T)=B_U^2(1-r) M_T for T!=empty.          (1)

This is not the full true child spectrum: the entire nonempty-frequency tail
is still the supplied mixture of the old reference and arbitrary target S.
Its vacuum mass is alpha+beta*r and tail mass beta(1-r), so it is normalized
exactly. Positivity of the old R on true seed atoms and the floor1-epsilon>0
guarantee finite child CE. All old nonempty reference-only labels remain
with their old positive component when r<1 and beta>0.

If r=1 the seed is constant. Set Q'_sigma=P_sigma on the vacuum and zero
on the nonempty tail. This is an explicit FRESH reset; the removal of old
reference-only tail atoms is accounted for by the binary KL below, not a
change to the inherited marginal. No tail normalization is formed.
If beta=0 there is no seed sector and the two fresh references are the true
a spectrum, independently of source quantities. No division by beta occurs.
The r=0,t=0 case uses the stated tail laws with denominator1. If t=1,
finite source CE forces r=1. Zero true terms always contribute zero.

## 3. Exact reset increment and the single conserved source bank

Let B_z(F) be spectral conditional erasure and J_z the Jensen--Shannon
divergence between the two complete child spectra. The exact physical
restriction identity is H(F)-mean H(G_sigma)=B_z(F)+J_z, with J_z>=0.
Because (1) matches each true vacuum atom and factors its entire tail,

    D(P_sigma||Q'_sigma)=beta(1-r) D(p^tail||M).

The source's full relative entropy decomposes as

    D(p||R)=d(r||t)+(1-r)D(p^tail||R^tail),

where d is binary KL. Therefore the ACTUAL erasure-plus-reset increment is

    B_z(F)+mean_sigma CE(P_sigma,Q'_sigma)-CE(F,Q)
      = -J_z - beta*d(r||t)
        +beta(1-r)[D(p^tail||M)-D(p^tail||R^tail)].     (2)

The formula keeps both different child terminal spectra, their signed
vacuum entries and all normalizers. The constant-seed endpoint reads
-J_z-beta*d(1||t), with no undefined tail law. For epsilon=0 this is a
nonpositive reset: the actual vacuum is recalibrated and the old conditional
tail is carried. No old controller debit, source debit or reference-only
mass is silently discarded.

For positive epsilon, the pointwise likelihood floor M>=(1-epsilon)R^tail
gives

    D(p^tail||M)-D(p^tail||R^tail)<=log2(1/(1-epsilon)).

It follows directly from (2) that the prescribed new tail component is paid
whenever

    (1-r)log2(1/(1-epsilon))<=d(r||t).                 (3)

This is an explicit eligibility condition, not an automatically renewed
source budget. If (3) fails, (2)'s actual signed excess must be paid from a
genuinely unused original account; a generic free fresh reset is NOT proved.

A079's paid mixed controller/source interface supplies incoming Q with its
already booked debits. Replace any eligible terminal by the actual z query
and BOTH references (1). Equation (2), or its bound using (3), makes this
replacement no more expensive than the terminal it replaces. Weighted
induction at an arbitrary selected stopping frontier preserves that SAME
original account. The unused source reserve is not reissued, and no new
influence rate is needed. Each fresh terminal may then admit arbitrary
ordinary physical queries carrying its CURRENT marginalized complete
reference: CE(parent,Q)-mean CE(children,Qbar)=B+D_cond>=B. This includes
further biased seed queries without declaring their later arbitrary resets
free. First-reset frontier nodes can be chosen adaptively; they form an
antichain, so no source is charged twice.

This theorem conditionally closes a prescribed signed-collision reference
transfer. Its scalar KL/floor comparisons are general probability facts;
it is not offered as a new Booleanity inequality or an admission theorem
that excludes all normalized non-Boolean vectors. Its application uses the
displayed actual Boolean phases, finite source CE and an already paid source.

## 4. A nontrivial fixed mixture with positive certified slack

At the original A079 root beta=3/8. For EVERY Boolean seed with mean m=+/-1/2,
take a supplied source reference with t=1/2 and epsilon=1/8. Then r=1/4 and

    d(r||t)=(3/4)log2(3)-1,
    d(r||t)-(1-r)log2(8/7)=(3/4)log2(21)-13/4 > 1/24.

The last strict inequality is equivalent to 21^18>2^79 and is checked
exactly as an integer inequality. Consequently (2) is STRICTLY below
-1/64, in addition to the nonnegative J_z refund, for ANY prescribed S.
The old tail keeps weight7/8 and an arbitrary new normalized tail gets
weight1/8. This is a useful prescribed nonflat reference change through
the actual biased tag collision; both children remain nonconstant for
this fixed four-bit a,b. On a restricted controller the same formula gives
slack greater than beta/24, including the zero-beta endpoint with zero slack.
No mean1/2 assumption is required for (1)--(3), only for this fixed example.

## 5. An exact support impossibility for the naive phase reset

Take the ACTUAL seed h=[-1,1,1,1], m=1/2, and source reference

    R=[1/9,8/27,8/27,8/27].

It is normalized and strictly positive, so incoming source and wrapper CE
are finite. A tempting normalized child reference replaces actual m by
sqrt(t)=1/3 at the vacuum and retains B_U^2 R_T on the nonempty tail.
It is normalized, because sum A B=0, but on the minus child at U=empty

    naive vacuum mass=(2/16-(1/3)*(6/16))^2=0,
    TRUE vacuum mass=(2/16-(1/2)*(6/16))^2=1/256>0.

Thus its child CE is INFINITE. The actual Boolean child truth table, direct
Walsh transform and entire normalized naive reference are saved. This is
an exact impossibility of finite-cost reference support, not an FEI
counterexample or an arbitrary normalized vector presented as Boolean.
The repair (1) uses actual signed m and avoids the occupied zero.

## First unsupported line

The incoming source interface must still be influence-priced and finite
on the actual seed spectrum. A079 already proves this is not free for an
arbitrary Boolean seed. This theorem supplies no universal such source.
After the funded1/8 tail mixture, a later prescribed reference with no
likelihood floor or fresh occupancy credit can increase CE, and a reset
back to an earlier source must not be called calibration of the CURRENT
reference. NEXT is an actual later active query and a prescribed new reset
using the remaining same source account, with old tag/reset debit and both
complete terminals retained. Arbitrary fixed-controller all-history seed
payment is ruled out by A033 and is not retried here.
