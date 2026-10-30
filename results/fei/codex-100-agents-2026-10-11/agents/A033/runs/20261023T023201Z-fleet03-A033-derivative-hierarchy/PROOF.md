# One active seed query after the signed tag reset

All logarithms are base two. All coordinates are original uniform physical
coordinates; all child terminals and reference-only atoms are retained.
This is a conditional reference-transfer result, not a new Booleanity
admission inequality or an initially influence-priced source theorem.

## 1. Incoming state: consume A032 rather than repeat the tag reset

Let A,B be real functions on controller coordinates u with AB=0 and
A^2+B^2=1 pointwise; B may be signed. Let h be Boolean on independent
seed coordinates and G_sigma=A+sigma B h, sigma in {+1,-1}. These are
the actual children of the physical tag in F=A+zBh. Put a_U=Ahat(U),
b_U=Bhat(U), beta=E B^2, mu=E h and r=mu^2. The incoming reference at
each tag child is the ACTUAL A032 signed-vacuum reference

  Q_sigma(U,empty)=(a_U+sigma mu b_U)^2,
  Q_sigma(U,T)=b_U^2(1-r) M(T), T nonempty.                 (1)

Here M is any normalized nonempty-frequency reference positive on all
occupied nonempty seed atoms. In particular M can be A032's already-paid
mixture (7/8)R_tail+(1/8)S. Its actual target component is not removed.
All earlier source/tag/controller debits remain booked. No reserve is
renewed. Parseval and sum a_U b_U=E AB=0 normalize (1) to one.
Constants (r=1) have no active seed query and can be stopped.

## 2. Exact inherited reference after one physical seed query

Query seed coordinate i. On remaining seed subsets V define

  m1=M({i}), w=(1-r)(1-m1),
  L(V)=[M(V)+M(V union {i})]/(1-m1), V nonempty.            (2)

The terms M(empty) and M({i}) are handled separately; M(empty)=0 by
definition. Let nu_tau=E(h|x_i=tau), r_tau=nu_tau^2 and
t_tau=beta(1-r_tau). The ACTUAL child vacuum atoms are

  p_sigma,tau(U)=(a_U+sigma nu_tau b_U)^2.                 (3)

The inherited marginal of (1), BEFORE any reset, is

  q_sigma(U,empty)=(a_U+sigma mu b_U)^2
                         +b_U^2(1-r)m1,
  q_sigma(U,V)=b_U^2 w L(V), V nonempty.                  (4)

These are normalized complete references. In particular (4) is generally
not the reference obtained by inserting nu_tau into (1). That replacement
is a fresh reset and must be paid. Define c_sigma=sum_U q_sigma(U,empty)
=1-beta+beta[r+(1-r)m1]. Its value is independent of sigma, but its
individual controller atoms retain their signs and interference.

## 3. Exact refund, retaining the controller-vacuum profile

Coarsen only the NONEMPTY remaining seed sector to one symbol *. Keep
every controller-vacuum atom U separately. The two normalized coarse laws
are

  P^coarse_sigma,tau=( (p_sigma,tau(U))_U, t_tau ),
  Q^coarse_sigma=( (q_sigma(U,empty))_U, beta w ).

Let R_sigma,tau=D(P^coarse_sigma,tau || Q^coarse_sigma).
It is finite whenever the incoming CE is finite. Proof of support:
each physical child coefficient is a sum/difference of the two parent
coefficients in that spectral fiber; an occupied child therefore has at
least one occupied parent coefficient, whose reference mass survives in
the inherited marginal. In a nonempty fiber both actual and inherited
laws factor through b_U^2, so the conditional U law is the same. Thus
the coarse KL is exactly the refund for matching the vacuum atoms and
the total tail mass, while retaining the current conditional tail L.

Prescribe arbitrary normalized nonempty targets S_sigma,tau and
0<=epsilon_sigma,tau<1, and set

  N_sigma,tau=(1-epsilon_sigma,tau)L
                                  +epsilon_sigma,tau S_sigma,tau,
  Q'_sigma,tau(U,empty)=p_sigma,tau(U),
  Q'_sigma,tau(U,V)=b_U^2(1-r_tau)N_sigma,tau(V).           (5)

For t_tau=0 omit the tail and use only the true vacuum. If beta w=0,
finite incoming CE forces t_tau=0, so L and N are never formed.
For beta=0 there is no seed sector and every refund/reset cost is zero.

Write p_tau^tail for the normalized true nonempty seed spectrum when
r_tau<1. Direct expansion of the logarithms gives the EXACT reset cost

 CE(P_sigma,tau,Q'_sigma,tau)-CE(P_sigma,tau,Qbar_sigma)
   = -R_sigma,tau
     +t_tau[D(p_tau^tail||N_sigma,tau)
                         -D(p_tau^tail||L)].             (6)

The likelihood floor bounds the last bracket by
log(1/(1-epsilon_sigma,tau)). This includes reference-only atoms.

For the parent query put
rho_sigma=D(P_sigma||Q_sigma)-D(P_sigma^marg||Qbar_sigma).
This is conditional occupancy KL, not an invented new bank, and rho>=0.
The exact conditional-erasure/CE chain rule, followed by (6), yields

 B_i(G_sigma)+mean_tau CE(P_sigma,tau,Q'_sigma,tau)
                  -CE(P_sigma,Q_sigma)
 = -rho_sigma-mean_tau R_sigma,tau
   +mean_tau t_tau[D(p_tau^tail||N_sigma,tau)
                                      -D(p_tau^tail||L)]. (7)

Consequently a prescribed reset is paid from THIS SAME incoming terminal
whenever the mean likelihood-floor bill is at most
rho_sigma+mean_tau R_sigma,tau. No physical erasure is discarded:
B_i is the full spectral conditional erasure, not automatically <=K Inf_i.
It remains inside the previously paid source-history interface. Weighted
replacement at a selected frontier preserves all earlier debits and both
tag children and both seed children; a source is not charged twice.

The refund splits further, when its nonzero sectors are normalized, into

 R_sigma,tau=d(t_tau||beta w)
   +(1-t_tau)D(P_vac_normalized||Q_vac_normalized).         (8)

Thus scalar occupancy alone can miss an actual signed-vacuum refund.
Dropping the second term is a conservative bound; identifying it with
zero without checking the controller profile is incorrect.

## 4. Strict phase-only example and a genuinely changed tail

Let A=(1+c)/2, B=(1-c)/2 on one controller bit; beta=1/2.
Let k be the two-bit point defect [-1,1,1,1], mean 1/2, and
h=x_i k. Take the incoming tag source R=P_h. The first tag reset uses
epsilon=0 and is paid; h is balanced, so it has zero tag JS and zero
source calibration debit. Then query i. Here m1=1/4, w=3/4,
nu_tau=+/-1/2. At each of the FOUR actual tag/seed terminals,
the two true vacuum atoms are 9/16 and 1/16 (possibly swapped),
the inherited vacuum atoms are 5/16 and 5/16, and the tail mass is 3/8.
Scalar occupancy KL in (8) is EXACTLY zero, while

 R_sigma,tau=(9/8)log(3)-(5/8)log(5)>1/4,

since 3^9>4*5^5. The current tail L is uniform on the three nonempty
k-frequency labels. Prescribe S to be the atom on one such label and
epsilon=1/8. Then N=(5/12,7/24,7/24), genuinely different from L.
The floor bill is (3/8)log(8/7)<3/32 since 8^4<2*7^4.
Thus (7) is below -5/32 at EACH tag child, even discarding rho>=0.
This refunds the actual signed vacuum collision and retains all tails;
it is not a claim that arbitrary subsequent resets are free.

The finite checker also tests A032's biased source family with the
ACTUAL earlier 1/8 mixture present; (2)--(7) do not remove that component.
The example is an actual Boolean family satisfying the complete hierarchy.
The KL identity itself also applies beyond Booleanity and therefore is
NOT advertised as the missing B07 Booleanity-specific FEI inequality.

## 5. Continue the ACTUAL paid 1/8 mixture, with the same source owner

Use the original A079 four-controller mask, beta=3/8. Let h be the
three-seed truth table [1,1,1,-1,1,1,1,-1], with bit-weight-one coordinate
i queried next. Its two restrictions are 1 and a character on a remaining
seed bit; the third seed bit is a retained spectator. Its mean is 1/2 and
its three nonempty occupied Fourier atoms each have mass 1/4.
Supply R(empty)=1/2 and R_tail=p_tail (uniform on those three atoms).
Apply A032's paid tag reset with epsilon_tag=1/8 and S uniform on ALL
seven nonempty seed labels. This is its existing biased eligible case,
so its old tag debit is retained and its release exceeds 1/64. The
actual current M has mass 13/42 at each occupied label and 1/56 at each
of the other four labels. Do not replace M by its old pre-mixture value.

For the next query, M({i})=13/42, w=29/56, and beta*w=87/448.
The inherited vacuum mass is therefore 361/448, at BOTH tag children.
The constant-seed child has coarse true tail mass zero and hence refund
at least log(448/361); the nonconstant child has refund at least zero.
Its actual tail mass is 3/8; the constant child has tail mass zero.
The CURRENT nonempty conditional reference is

  L=(26/29,3/58,3/58)

on the three remaining nonempty seed labels. Prescribe another epsilon
of 1/8 and ANY normalized target S on those labels at the nonconstant
child. In particular S=delta_spectator gives

  N=(91/116,79/464,21/464),

which is genuinely changed and retains the old L component at 7/8.
At the constant child retain its complete actual controller spectrum.
At EACH tag parent, (7) bounds this complete query/reset increment by

  -(1/2)log(448/361)+(3/16)log(8/7) < -1/10.             (9)

The strict inequality has the exact integer certificate

  448^40 * 7^15 > 2^8 * 361^40 * 8^15.

Thus both tag children can take the next ACTUAL active seed query and
this prescribed second reset, retaining all four final terminals and
the first tag/reset mixture/debit, with more than 1/10 bit NEW release.
This is a selected continuation of the SAME originally supplied account;
it does not issue a new initial source bank. The all-target statement
uses only the stated likelihood floor and the exact displayed profile.
An initially influence-priced source for arbitrary seeds is still absent.

## First unsupported line and complete Booleanity hierarchy

The missing universal step is still an initially influence-priced source
reference, or an unconditional lower bound on unused refunds that pays
every required future reset and erasure. Neither (7) nor this example
supplies that. Full FEI remains OPEN. In particular a later target with
no likelihood floor can have infinite CE; no fixed controller reserve
pays every seed history (A033's previous all-C no-go).

For Fourier coefficients fhat(S), the complete hierarchy used is ALL
signed convolutions sum_S fhat(S)fhat(S xor U)=1{U=empty}; equivalently
f^2=1 on every input. Under every physical restriction the split
f=A+x_i B obeys AB=0 and A^2+B^2=1. For ALL derivative orders T,
D_T f is the alternating restriction average, with grid
2^(1-|T|)Z intersect [-1,1] for nonempty T; that grid alone is not
an admission test. Fixed signed-convolution prefixes, dyadic coefficients,
atom-cap prefixes, and small norm/square defects are imported no-go
directions, not retried here. The previous source audit still lacks the
original cyclic atom-cap construction/checker; its import remains summary
only, not a newly certified family. This stage prices a full signed
post-tag profile, without pretending that generic KL proves a new
Booleanity consequence or that more fixed-prefix equations suffice.
