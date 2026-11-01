# Independent donor-optimality reconstruction

The reviewed claim is A072-SATURATED-DONOR-OPTIMALITY@1, source statement-only hash
589d2d5a88ed46b641128b06077714c386d0ae3b166dbae2465fce0644657772.
The protocol statement-plus-hypotheses digest is
d3a415f515fe14c8d600b1303f62c49c65ff3c5f5ec1c1ae9cea9edcf63eb7b3.
The source persistence script line60 hashes only the statement; the local
review normalizes that metadata and pins both digests and the source bytes.
Statement, hypotheses, version and finite/conditional scope are unchanged.
This is not a substantive proof repair. Full FEI remains open.

## General allocation and the hypotheses it actually uses

Let V_c,W_c>=0, S_c=V_c+W_c, and give the two physical children weight1/2.
For 0<=T<=mean S choose 0<=d_c<=S_c with mean d=T. The donor cost is
mean max(d_c-V_c,0). Pointwise max(d_c-V_c,0)>=d_c-V_c, so this cost is at
least max(0,T-mean V). To attain it, if T<=mean V and mean V>0 set
d_c=T V_c/mean V. If mean V=0 this branch forces T=0 and d=0 suffices.
Otherwise mean W>0, and theta=(T-mean V)/mean W belongs to(0,1]; take
d_c=V_c+theta W_c. Every cap, mean and asserted cost follows directly.
These branches prove the claimed formula and justify every denominator.

For parent slack S, incoming debit D and full physical excess e, the physical
influence identity gives mean S_c=S+e. With outgoing mean T=D+e and R=S-D,

    T-mean V = mean W-R.

This is an accounting identity, not an entropy estimate. Nonnegativity of both
banks matters. The two rational weakened-hypothesis counterexamples in the
source are reconstructed by directly computing their feasible debits and
objective; neither is asserted to be a Boolean function.

For T>0, each old label L is sent to L*d_c/T and the new signed label to
e*d_c/T. Conditional means of old labels remain L, and the signed new mean
remains e. Their sum is d_c. Negative new labels are allowed. The allocation
lemma includes T=0, but this proportional formula does not; its T>0 hypothesis
is explicitly retained. All60 Boolean cases certify it. No assertion about
nonnegative individual labels is needed.

## Saturation is absorbing unless the incoming account changes

If D=S, then mean d=mean S_c. Each S_c-d_c is nonnegative and their mean is
zero, so both are zero. Thus d_c=S_c and all W_c is spent. Apply this argument
at every descendant: on ANY finite continuation tree satisfying the same
physical slack identity, feasible capacity caps, positive child reaches and
no external credit/reset, a saturated incoming account remains saturated at
every descendant. No strictly positive unused reserve can arise inside that
subtree. This induction is an immediate consequence of the reviewed theorem,
not a new FEI assumption. It is conditional on feasibility; it does not prove
positive full-child slacks for arbitrary Boolean cores.

Consequently, a positive unused-donor invariant on the saturated branch alone
is impossible. The remaining route must establish child eligibility without
new reserves, or explicitly transfer genuinely unused capacity from a stopped
sibling with its true reach and existing labels retained. Merely declaring
the already spent W unused would change the account.

## Independent Boolean spectrum and full physical account

Use the exact source truth tables: g negative on{0,1,2} in six bits;
h negative on{0,1,2,4,8,16,32,6,17,40}; J(x)=-h(x xor1). We reuse ONLY
A074's prior independent binary finite-difference/conditional-entropy helper,
setting K=4 before any capacity is computed. No peer executable is imported
or run. In particular this is not a rerun of A072's centered-Walsh engine.

If X_j indicates a negative core output and p_j=E X_j, expand
J(X)=sum_U D_U product X_j by inclusion-exclusion on its64 truth values.
Then b_T=sum_(U superset T)D_U product_(U\T)p_j, and the occupied physical
block law is mu_T=b_T^2 product_(j in T)p_j(1-p_j). Direct integer characters
give each inner spectrum. Given an occupied block its nonempty physical
spectrum is normalized by v_j=4p_j(1-p_j). Hence independently derive

    H(F)=H(mu)+sum_j v_j q_j H(normalized nonempty inner spectrum),
    I(F)=sum_j q_j I(g_j).

The q_j are separately evaluated from physical outer pivotal edges. Constant
inner cores have zero v and contribute no conditional entropy. Full H is
computed first; only then form C=H(F)-sum_j q_j H(g_j). Formal rational
log-linear profiles preserve the exact occupied entropy and every core term.
They verify mean S_child=S_parent+e, conservation of other raw banks, and
e-(mean U_child-U_parent)=C_parent-mean C_child by exact dictionary equality,
not by a floating or interval equality test. V,W signs and divisions are
certified separately with rational intervals.

Reconstruct the original prefix block0 original coordinates2,0,3 answered00b.
The first nonconstant child receives2e1. The second query allocates each old
label proportionally to q0 S4 of its two selected cores. At the third query
let T3=D_second0+e3, tau=T3-S_third0/2. The signs are checked, not assumed:
the first third-child corrected capacity equals its full S and is saturated;
the other receives2tau and retains positive full surplus. Labels are split
separately in proportion to these actual debits. Both earlier stopped
terminals are kept with reaches1/2 and1/4; each third child has reach1/8.

For each b=0,1, each block j=1..5 and original coordinate i=0..5, recompute
the two full children. There is no symmetry quotient or dimension escalation.
Use S=4I-H, U=q_j S(core_j), M=S-U, V=U-max(-M,0), W=max(M,0).
On the saturated parent allocate each child's complete S. On the other parent
use the proved optimal selected-only or selected-plus-donor branch. All caps,
all conditional label means and all source comparisons pass. Each alternative
has five complete terminals of reach1/2,1/4,1/8,1/16,1/16; their mean remaining
account equals the SAME original root S4, with no rate increase or renewed bank.
Every full terminal H and I is saved, including both new children and all
earlier stopped siblings. The60 alternatives are not simultaneous debits.

## The failed verifier branch and its exact repair

The first full attempt stopped after48 completed cases. A reused verifier
inferred identical inner children whenever physical influence d=0. That
inference omits the alternative q_j=0. The source claim was not refuted.
The partial journal is preserved as a failed diagnostic; it is not counted
as final accepted evidence.

The corrected checker distinguishes two proofs of a full dummy query:
if inner Inf_i=0, direct truth tables show identical inner restrictions;
otherwise q_j=0, and every positive-probability outer edge in direction j
is checked to have equal gate outputs. Since q_j is a sum of nonnegative
weighted pivotal indicators, this proves full-function independence of that
block on the actual output support. Its entropy decrement and influence
are exactly zero even if the inner children differ. The same frozen60 cases
were deliberately revalidated under this corrected proof; no rate, dimension
or precision changed. A unique V2 journal prevents replay of partial outputs.

## Exact arithmetic, hostile tests and scope

All signs and bounds use arbitrary integers/Fractions and A074's48-term
positive atanh expansion after dyadic log reduction, with a proved tail and
112-bit outward log2 rounding. Source192-bit endpoints are used only in780
final interval comparisons, after our independent accounts are computed.
Equalities use the exact physical definitions/algebra and rational log profiles;
interval overlaps serve as diagnostics. Inner characters, Parseval, spectral
influence, independent physical edge counts, gate inversion and transported
q weights precede capacity conclusions. Nine distinct core tables are used,
including the prefix and stopped cores; this count differs from the source's
seven because the audited helper domain includes those additional prefix cores.

For405 rational boundary allocations with V0,V1,W0,W1 in{0,1,2}, T=k/2 over
the entire feasible range, we exhaust ALL feasible integer d0 values:729
feasible vertices in total. All objective breakpoints and feasibility endpoints
are integers in this domain, so the objective is affine between consecutive
integers and this discrete minimization is the exact finite LP optimum. This
is a separate implementation from the source's targeted breakpoint list.
The tests include zero banks, T=0, full saturation and negative new signed
labels, plus the two hypothesis-breaking counterexamples. The written
attainment/lower-bound proof handles arbitrary real capacities.

Final validation passes60 Boolean alternatives and405 boundary allocations,
with5506 review predicates and1932 helper predicates (7438 total), in9.7866913s.
Pilot and failed partial attempts are not added to that count. Exact records
are saved as each case completes. General child positivity is never inferred
from this finite census.

Core Lean submissions contain the integer shortfall identity and saturation
from two nonnegative deficits. Compute admission returned SETUP_UNVERIFIED
before launching a compiler. Neither the integer targets nor the real theorem
are labelled Lean-checked. The plain algebraic proof and independent exact
certificate are the mathematical evidence; the source has not been repaired.

The first unsupported universal line remains a noncircular signed-component
criterion guaranteeing feasible full child capacities for arbitrary retained
cores at the unchanged inherited debit, or a quantified genuinely unused
off-branch bank covering any deficit without renewing labels or terminal bills.
