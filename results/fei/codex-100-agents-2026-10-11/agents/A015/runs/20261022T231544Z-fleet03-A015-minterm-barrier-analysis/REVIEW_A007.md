# Scoped reconstruction of A007's new payment and scale cancellation

Source: A007-COMBINED-LEAFLESS-PAYMENT-AND-SCALE-CANCELLATION@1,
statement hash 6c440f3bd293bf492f08c7dde45fab6e47eaf236c13922acc9de1abe07af5d0e,
20261021T211258Z-fleet03-A007-root-normalization.
Read KMM_PAYMENT.md, SCALE_CANCELLATION.md and CLAIMS.json. Result:
SCOPED HOLDS for the new numerical combination conditional on its stated
upstream transfer, and for the finite positive-record scale identity.
This is not independent acceptance of that compound claim's full chain.

I reconstructed the payment: the I_g coefficient from (3)--(5) is
log(m)+4+(3/5)log(e); all terms retain their signs and the physical controller
has influence b, not I_g. Using log(e)<3/2 and I_g<=4m2^-m gives
m2^-m[4log(m)+211/10]+(63/40)b. Then m2^-m<=1/2,
m^2 2^-m<=9/8 and b>=9/16 give exactly10199/360<29. The inductive m^2 bound
starts at m=3 and uses (m+1)^2<=2m^2 thereafter; m=2 is checked separately.
The bound pays source R_F, leaving the explicitly named K_ref and entropy
interface outside it. It does not claim an upper bound on the actual queue
cost from the source surrogate.

For scale cancellation, I independently exponentiated the identity, avoiding
numerical logarithms. For each T, S_t J_U=N_alpha,U termwise. Raising the
combined cost per unit spectral mass to exponent1/p^2 yields

    [(D_t/S_t)(D'/(pD_t))]^(1/p) / prod_U J_U
      = (D'/p)^(1/p) / prod_U N_alpha,U,

since there are exactly1/p control subsets INCLUDING the empty subset.
Thus old D_t and S_t cancel while the posterior itself can change. Positive
masses make each operation legitimate. Omitting empty controls invalidates
the cancellation. Exact fixtures in check_frontier_review.py test this
reconstruction with changing posteriors and fixed final scale; these are
abstract algebra fixtures, not Boolean witnesses.

Conflict disclosure: A015 authored the upstream one-control inequality used
by A007. I do not independently accept that part, the full inherited
distributed transfer, or the sharp asymptotic via this review. The new
rare-core actual-queue theorem in this run does not assume any of them:
it reconstructs original queue event probabilities directly. A007's new
rare-core target is consumed rather than duplicating its solved K_m,m case.
