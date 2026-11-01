# Density payment at the root: all geometries and high-influence seeds

Uniform signs, entropy in bits. Data cube has k>=1 bits, N=2^k,
delta=1/N. Let b be ANY Boolean seed. Distinct vertices v_j carry arbitrary
indicators A_j on a common uniform controller cube, independent of the data;
indicators may depend arbitrarily on each other. Set a_j=1-2A_j,
alpha_j=EA_j, mu_j=Ea_j, beta_j=1-mu_j^2=4alpha_j(1-alpha_j),

    F(x,z)=b(x)[1-2 sum_j point_(v_j)(x) A_j(z)],
    p=delta sum_j alpha_j, V=delta sum_j beta_j,
    L=delta sum_j H(a_j), c=log2(e), phi(t)=t log2(1/t).

p is the ACTUAL probability F differs from b, not the nominal support
density q/N. Unlisted vertices have alpha=beta=0. No cardinality guard.

## Exact signed coefficients, row law and controller ownership

Direct Fourier transformation gives

    Fhat(S,T)=bhat(S)1_(T=empty)
               -2delta sum_j b(v_j)chi_S(v_j) Ahat_j(T).       (1)

For T nonempty, orthogonality of distinct data characters gives

    R_T=sum_S Fhat(S,T)^2
       =4delta sum_j Ahat_j(T)^2
       =delta sum_j ahat_j(T)^2.                             (2)

Thus R_empty=1-V and the FULL controller-label marginal is exactly

    R=(1-qdelta) point_empty + delta sum_j P_j,
    P_j(T)=ahat_j(T)^2.                                     (3)

This is a spectral marginal identity, not conditional physical resetting.
All signed cross terms remain in the conditional data laws nu_T(S).

    H(F)=H(R)+(1-V)H(nu_empty)
                       +sum_(T nonempty) R_T H(nu_T).       (4)

Zero rows are ignored. Every conditional data law has at most N labels,
so its entropy is at most k. This is one whole-root data budget; it does
NOT assert a good paired access tree or individually paid dense leaves.

On a controller coordinate, changes of a_j occur only in the disjoint
physical data fiber v_j. Hence, coordinatewise and in total,

    I_ctrl(F)=delta sum_j I(a_j).                           (5)

No independence among indicators is required.

## The exact logarithmic bill and its paid upper bound

For nonnegative x_j, phi(sum_j x_j)<=sum_j phi(x_j), by the
log-sum identity; zero terms are continuous limits. Applying this to (2),
and keeping the empty marginal exactly, gives

    H(R)<=phi(1-V)+L-delta sum_j phi(mu_j^2)+k V.             (6)

The difference from the right side is exactly

    D_mix=sum_(T nonempty) R_T H(J|T),
    P(J=j|T)=delta ahat_j(T)^2/R_T,                         (7)

which is nonnegative. Thus (6) preserves the full inherited controller
entropy, with an explicit unused mixing refund. Combining (4)-(7):

    H(F)<=L+k(1+V)+phi(1-V)-delta sum_j phi(mu_j^2).         (8)

More exactly the right-side excess over H(F) is

    D_mix + sum_T R_T[k-H(nu_T)],                         (9)

so no conditional signed geometry has been discarded from the identity.
For V=0 all controllers are constant; L=0 and (8) simply says H(F)<=k.
The phi(1-V) term and all mu_j terms are included. Nothing is hidden in a
zero-entropy terminal or a free label code.

Because phi(1-V)<=cV on [0,1], and V<=4p, (8) gives

    H(F)<=L+k(1+4p)+4cp.                                 (10)

A sharper optional relation is V<=4p(1-p), by Jensen applied to all N
alpha values (zero at unlisted vertices). Only V<=4p is needed below.

## Actual data edge capacity, including adjacent cancellation

Each seed data edge can change its pivotal status only if an endpoint is
flipped. At each data coordinate, this endpoint union has probability at
most2p. Therefore

    I_data(F)>=I(b)-2kp.                                 (11)

This counts ACTUAL edges after cancellations, not a sum of point boundaries.
For completeness the exact coordinate formula is

Inf_i(F)=Inf_i(b)+2delta sum_j alpha_j b(v_j)b(v_j xor e_i)
  -4delta sum_(j<l:v_l=v_j xor e_i)
           b(v_j)b(v_l)E(A_j A_l).                       (12)

The adjacent term cannot be replaced by independent products.

For ANY supplied seed with I(b)>=gamma k and p<gamma/2, (10)-(11) give

 H(F)<=L+[(1+4p+4cp/k)/(gamma-2p)] I_data(F).              (13)

The unrounded version (8) may be substantially better. This is a proved
seed-capacity criterion; it does not give gamma uniformly for all seeds.

## Absolute-rate high-influence closure

If k>=4, I(b)>=k/2 and p<=1/8, then c<3/2 gives

    k(1+4p)+4cp <= k[1+(11/2)p] <= (27/16)k,
    I_data(F)>=k/4.

Consequently

    H(F)<=L+(27/4)I_data(F)<=L+7I_data(F).                (14)

The spare1/4 in the rate is not claimed optimal. This covers ALL bent
references, without requiring quadratic pairs, and all seeds satisfying
the high-influence condition, including tensor products of bent signs and
characters of at least the required total influence. q can equal N.
The expected activation density, not the number of nominal vertices, is
the admission condition. H(a_j)<=C I(a_j) implies
H(F)<=max(7,C)I(F), using the exact coefficient delta in (5).

Additional nominal-density refinements: if rho=q/N<=1/8 and k>=4, then
V<=rho and p<=rho. Thus

    H(F)<=L+k(1+rho)+c rho,
    I_data(F)>=k(1/2-2rho),

and the quotient is at most75/16<5. If rho<=1/16, the quotient is at
most139/48<3. Therefore rate5 and rate3, respectively, hold for the same
high-influence seeds. These are refinements, not new universal claims.

## Finite recursive closure and the honest universal frontier

Start with constants/characters, and repeatedly use fresh data blocks
k>=4, arbitrary supplied high-influence seeds I(b)>=k/2, and previously
certified shared-bit controllers a_j, admitting only p<=1/8. Equation(14)
and (5) prove H<=7I at every finite construction depth. Each output's new
data reserve pays its own root conditional-data and mixing bill once;
the old controller entropy is inherited at delta, without raising its rate.
The seed's entropy certificate is not assumed: H(data spectral label)<=k
is paid by its actual large influence. This does not certify a prescribed
later mixed history or renew a bank after a booked query.

First unsupported universal line: an arbitrary Boolean target admits a
high-influence seed at p<=1/8 with certified controllers, or a low-influence
seed has an analogous budget without the ambient k/I(b) loss. For example,
the dimension label budget k is arbitrarily loose for padded low-influence
functions. The p<gamma/2 denominator and the complete controller bills
cannot be removed by calling (3) a reset. Full FEI and universal mixed-
history payment remain OPEN.
