# A single core query: exact activation correction and full terminal bank

All logarithms are base two. Write phi(x)=-x log_2 x, with phi(0)=0.
Let A be ANY {0,1}-valued activation on independent control coordinates,
pi=EA, and g an independent Boolean sign. Set F=1+A(g-1), a=1-Eg,
and L_A=sum_T phi(Ahat(T)^2). Define, continuously at endpoints,

Psi_pi(a)=phi((1-a*pi)^2)-pi*phi((1-a)^2)
          -a^2*phi(pi^2)-(pi-pi^2)*a^2*log_2(a^2).

Then the exact identity is

    H(F)=pi H(g)+2a L_A+Psi_pi(a).                    (1)

Indeed, for nonempty core masks V, Fhat(T,V)=Ahat(T)ghat(V),
while the empty-core row is 1-a*pi at T=empty and -a*Ahat(T)
elsewhere. The nonempty-core mass is v=1-(Eg)^2=2a-a^2.
Its entropy is pi[H(g)-phi((1-a)^2)]+v L_A. The empty-core
nonconstant part is a^2[L_A-phi(pi^2)]
-(pi-pi^2)a^2 log_2(a^2). Add the remaining constant coefficient.
This uses A^2=A and independence at exactly these steps. No spectral
flatness, balance, FEI assumption, or interchange of infinite sums occurs.
For pi=0,1 and a=0,2 continuity agrees with the original functions.

For any actual fair core query i, with a_b=1-Eg_b,
(a_0+a_1)/2=a, so the linear term in (1) cancels:

    D_i F-pi D_i g=Psi_pi(a)-[Psi_pi(a_0)+Psi_pi(a_1)]/2. (2)

Equation (2) is an elementary specialization of exact composition
bookkeeping, with no novelty claim. It identifies the entire entropy
correction independently of the rest of the core spectrum.

## The same controller and same owned separator reserve

Use A=WUV OR S(U OR V) with each block a single fair bit. Then
eta=1/8,e=5/8,pi=7/16,JB=3/8,JC=1/2,JD=7/8. At j=1,
U(g)=[a JD+e I(g)]/2. Across core query i, the reserve release
is (5/16)Inf_i(g). It has already been booked and is never counted
as an independent new bank. Define

    R=D_i F-pi D_i g-[U(g)-mean U(g_b)].               (3)

Both actual restricted F_b, including constant children, are retained.

## Complete original reference and one explicit reset

Let P be the squared Fourier law of the actual root F. Set Q to its
product of Bernoulli spectral marginals, once at the root. Erase i from
P and Q to get q and q^Q. On each remaining mask T use the SAME actual
kernel k(b|T)=P_b(T)/(2q(T)), with k=1/2 if q(T)=0. Set
z_b=sum_T q^Q(T)k(b|T), Q_b=q^Q k/z_b. These are full normalized
laws; no source-zero reference row is deleted. For the fixtures the
normalizers are strictly positive and recorded exactly.

Put A0=D(P||Q), E=conditional-erasure KL,
O=D((1/2,1/2)||(z_0,z_1)), K=mean D(P_b||Q_b).
Two exact chain rules give A0=E+O+K. Let R_b be each actual child
product projection, TC=mean D(P_b||R_b), and sigma=TC-K.
The reset changes the actual mean terminal CROSS-ENTROPY by exactly
sigma. The root-based net reset debit is sigma-E=O+TC-A0; retain
both quantities rather than confusing a negative net debit with a
sufficient terminal bank. E is not spent as an extra credit below.

At fixed rate FOUR define the unused child banks AFTER retaining all
complete terminal cross-entropies and the STILL LIVE inherited reserve:

    B_old=mean[4 I(F_b)-H(F_b)-D(P_b||Q_b)-U(g_b)],
    B_new=mean[4 I(F_b)-H(F_b)-D(P_b||R_b)-U(g_b)].    (4)

Thus B_new=B_old-sigma. This is an exact signed release from ONE
explicit reset, not installation of fresh surplus. No other prior
withdrawal from these scoped finite banks is made. Full child entropy,
reference KL, physical influence and U are serialized in the certificate.

## Six-bit payment, with the full terminal bill

g=(-1,+1,+1,+1), query i=0. Direct truth-table Walsh computation gives

    R in (3429/100000,7/200),
    B_old in (1/40,13/500),
    B_new>19/100,
    sigma< -1/6,
    sigma-E<0.

In particular B_old<R: keeping the inherited references frozen fails.
One reset releases K-TC and gives R<B_new/5 and B_new-R>31/200.
These strict rational inequalities prove the finite payment of the
actual positive remainder while retaining BOTH complete product-reference
terminal laws and every remaining U. No negative net reset debit is
reused to pay R, and E remains unspent in this transaction.
The entropy-only account was B_H=mean(4I-H-U)>8/25, yielding an
entropy-only R/B_H<7/64<1/8. It is explicitly NOT B_old or B_new;
the final full-reference withdrawal bound is ONE FIFTH.

Root query Inf=7/32, pi Dg=7/8, reserve release=5/32.
Child influences are 19/16 and 0; mean remaining U=3/8.
Exact reference normalizers are 26573339/44171264 and
17597925/44171264. Mean terminal KL K is about .302923,
TC about .135385. These decimals are illustrative; rational intervals
in PILOT.json certify every sign. The constant child has H=I=TC=U=0;
its inherited KL is included in K rather than discarded.

## Failure of the first both-nonconstant non-flat extension

Take the three-bit non-flat core g=(-1,-1,-1,+1,+1,+1,+1,+1),
query i=0. Its children are (-1,-1,+1,+1) and (-1,+1,+1,+1),
both nonconstant. With the SAME controller, rate, reserve, root-product
reference and common-kernel/reset construction, exact certificates give

    R>41/1000,  B_old<-7/1000,  B_new<-67/1000,
    sigma>3/50, sigma-E<-47/1000.                     (5)

Both full child-reference accounts are insufficient even before R.
The favorable net reset debit sigma-E does NOT imply bank eligibility.
This directly refutes an extension claiming the sole child bank (4)
pays (3) for all non-flat cores at this fixed inherited U and rate4.
It does not refute a transfer from unused controller/source accounts,
a different justified reserve allocation, another policy, or FEI.
The exact first unpaid line is B_new>=R (or B_old>=R) for this
code7 core; both fail with separated rational intervals.

A dictator boundary g=(-1,+1) also has R>8/5 but B_new<43/50;
this separate fixture prevents claiming that the six-bit payment is a
general data-query law. No constant-terminal or non-flat exclusion can
rescue (5), whose children are both nonconstant.

## Verification and rung

The all-activation formula follows by the finite Fourier calculation
above; 800 actual queries over all labelled two-/three-bit cores check
its scalar correction against direct integer Walsh spectra. The A046
reserve has 9,216 exact rational parameter rows. Separate physical
separator checks cover 80 actual nodes, including j=4 and rare e regimes.
Finite payment and failures are exact rational interval certificates.

The log helper uses 36 positive atanh terms on [1,2], with tail
2 z^73/[73(1-z^2)], outward-rounded to 2^-120. Integer range reduction
handles all positive rational arguments, and division by the positive
ln2 enclosure uses the correct endpoint ordering. Floating values decide
no sign. The initial unrounded version failed serialization and produced
no certificate; the repaired fixed-domain run is the result used here.

Lean source formalizes ONLY the rational polynomial reserve release,
not the entropy theorem. Fresh memok passed; the pinned Lean checker
returned RUNTIME_UNVERIFIED after 69.636s with no compiler result.
There is no Lean-checked claim. Rung: analytic proof / exact finite
certificate, locally independently reviewed A046 v3, external review pending.
