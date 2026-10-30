# Point-edit-compatible partial rank return

All logarithms are base two. Cross entropy CE(P,Q) means the complete expectation of log(1/Q), including vacuum and every other actual atom. No restriction cost is omitted.

Let E=F_2^N label frequencies and let V be a specified linear subspace of dimension d. Let g:{0,1}^N -> {-1,1} have Fourier support contained in V. Change its value at one physical point a to obtain f. For every s,

    fhat(s)=ghat(s)-2^(1-N) g(a) (-1)^(s.a).

Therefore P_f(s)=2^(2-2N) for every s outside V. On V there is no uniformity assertion. The clean case with no edit has zero outside mass.

Define the group G_V={A in GL(E): Av=v for every v in V}. Each v in V is a singleton orbit; E\V, if nonempty, is one orbit. To see transitivity on the complement, extend a basis of V first by s and then to a basis of E. For any t outside V, extend the same V basis first by t. Sending the first extended basis to the second defines an invertible map fixing V pointwise and taking s to t. This argument requires s,t outside V; it makes no assertion when V=E.

For any normalized reference Q supporting P_f, average its pushforwards over G_V. Explicitly, with M=2^N-2^d and q*=Q(E\V),

    Qbar(v)=Q(v) (v in V),
    Qbar(s)=q*/M (s outside V, when M>0).                 (1)

This preserves every core reference atom, not just its total mass. It is the unique invariant reference with those core masses and that outside mass. If M=0, the return is identity. If the actual law has no outside mass and q*=0, outside zero reference entries are allowed and contribute no cost.

Since P_f is constant on the outside orbit, its conditional law there is uniform whenever that orbit has positive actual mass p*. The exact conversion invoice is

    CE(P_f,Qbar)-CE(P_f,Q)=-p* D(U_M || Q(.|E\V)) <=0.  (2)

If p*=0 the invoice is zero; if p*>0, support of P_f forces q*>0 and all outside Q entries positive. Equation (2) follows directly by expanding both complete sums. Equivalently apply the arithmetic-geometric mean inequality to the outside Q values; no independent-events argument is used. Thus the invoice can be negative and its actual refund is counted once, rather than replaced by an unsigned fee. The core and vacuum terms cancel exactly.

## Physical heredity, including non-coordinate cores

Fix ANY physical partial assignment alpha, leaving m coordinates. Let pi:E -> E_alpha=F_2^m erase the queried frequency coordinates, and put V_alpha=pi(V), with dimension r. The Fourier expansion of the clean restriction g_alpha is obtained by signed summation over the fibers of pi. Hence its support is contained in V_alpha. If alpha excludes a, then f_alpha=g_alpha. If alpha contains a, f_alpha is exactly one point edit of g_alpha in the remaining cube. Therefore at EVERY node of ANY adaptive physical restriction policy, the actual law is constant outside V_alpha (zero on a clean node, 2^(2-2m) on an edited node). At m=0, V_alpha=E_alpha and there is no outside orbit. The conclusion is pathwise and does not multiply conditional probabilities.

Furthermore, the ordinary frequency marginal pi_* Qbar has the same partial-orbit shape. Let t=N-m. The linear map pi restricted to V has kernel dimension d-r. Every u in V_alpha has 2^(d-r) preimages in V and every u outside V_alpha has none. A full pi fiber has 2^t elements; in particular d-r<=t. With M>0, the exact FULL inherited reference is

    (pi_*Qbar)(u)
      = sum_{v in V, pi(v)=u} Q(v)
        + (q*/M) [2^t - 1_{u in V_alpha} 2^(d-r)].       (3)

All coefficients in brackets are nonnegative integer counts. In particular every outside u has the same reference value q*2^t/M. Thus a second G_{V_alpha} averaging of the inherited marginal is EXACTLY identity, on every adaptive path. Formula (3) includes source mass from old outside atoms that now project into V_alpha, including the empty label; none is deleted, treated as payment, or silently renormalized. If V=E the source is arbitrary and this shape condition is vacuous. These boundary cases cover t=0, t=N, d=0, d=N and clean/edited leaves.

More generally, at any node alpha one can return ANY supporting CURRENT reference R_alpha by averaging under G_{V_alpha}. Equation (2), with the current actual law and current source, again makes the return free or a refund. This latter statement does not require that R_alpha came from (1). A previous non-averaging source operation can destroy inherited shape; its own invoice is not paid here.

## SAME original owner; all terminals and old bookings

Suppose an already specified history/frontier has original owner A, old signed query/conversion booking U, reaches w_alpha, and complete CURRENT terminal costs C_alpha. Its remaining balance is

    B=A-U-sum_alpha w_alpha C_alpha.

Replace only those current references by the partial returns above. Its balance becomes

    B'=B-sum_alpha w_alpha Delta_alpha >=B,               (4)

where Delta_alpha is the exact signed difference (2). All reaches, old bookings and complete terminal bills are retained. This holds also with negative initial B, but does not claim to make such a B solvent. A paid history stays paid at the SAME rate without a new influence owner. Already smoothed inherited sources have Delta_alpha=0; their earlier refund cannot be collected again. This is source conversion at a supplied history, not a theorem that physical query debits are universally paid.

For A066's actual guard h_n (a dictator edited at one point), choose V=span{the dictator label}. Its actual source P_h is already invariant under G_V, so its return is exactly unchanged and costs zero. For t*x*z*h_n, use the linear span of the three private labels and the original dictator label, or equivalently keep the private labels fixed and average the h-frequency source alone. After A066's t prefix the h reference is still P_h. It remains unchanged at every x/z terminal; the SAME literal owner's already established balance is exactly retained. This removes the full-GL obstruction by fixing the dominant core label; it does not recover full GL invariance or prove that a downstream consumer needs this weaker target.

## A two-edit boundary and the first unpaid step

On three physical bits let g(x)=(-1)^(x0) and flip its values at the two points 000 and 100 (bit0 is the low bit). Then f=(-1)^(x0) [1-2*1_{x1=x2=0}]. Its squared spectrum has four atoms of weight1/4, exactly at {x0}, {x0,x1}, {x0,x2}, {x0,x1,x2}. Take V=span{{x0}} and original Q=P_f. The outside orbit has six labels, three occupied. Its partial return has outside reference1/8 and core reference1/4. Each of the three occupied outside labels doubles its reciprocal reference, so the exact debit is3/4 bit. Thus (2) fails for arbitrary two-point edits with the SAME old V. No source positivity shortcut or approximate sign is needed.

The first unsupported universal step is supplying, for an arbitrary Boolean core, a useful proper V and an ORIGINAL influence-priced complete core profile that pays all subsequent actual query costs. Choosing V=E always makes the theorem true but gives no compression or payment. Even when a low-dimensional V is supplied, (3) does not bound or recalibrate its inside profile. A universally required downstream profile beyond this invariant class is also not supplied. This is a compatible partial-rank mechanism that survives the exact point-edit guard, not full FEI.
