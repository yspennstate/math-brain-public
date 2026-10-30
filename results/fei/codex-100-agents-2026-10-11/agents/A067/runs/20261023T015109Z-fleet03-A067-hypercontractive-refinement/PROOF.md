# Intact-pair data queries preserve the edited source conditionals

All functions are actual Boolean signs on finite uniform cubes. H, CE and KL use bits.
The root is exactly the canonical G_m and m>=2 of the independently accepted A067 v1.
Write b_m(Y)=(-1)^(sum_j Y_(2j-1)Y_(2j)), c_m=b_m-2*1{w=0,Y=0},
G_m=b_m+1{w=0,Y=0}(z-1), A=2^-m, delta=2^(-(2m+1)).
The old actual z decrement D and original bank S are retained unchanged:

    D=H(G_m)-[H(b_m)+H(c_m)]/2,
    S=[2I(b_m)-H(b_m)+2I(c_m)-H(c_m)]/2,
    r=S-D=2I_X(G_m)-H(G_m)>delta/4.

The source statement/hash is unchanged. A088 independently accepted it without repair.
Its clean-history theorem is background and is not re-enumerated here.

## 1. Actual edited restrictions and the ORIGINAL reference

Initially expose z; leave the entire z=+ clean terminal b_m unchanged. In z=-,
successively query one physical Y bit from any still-intact quadratic pair. Upon
an outcome 1, keep that complete clean exit terminal and stop querying it. Only
the all-zero edited path continues, for any chosen length h with 0<=h<=m.
The queried pair/member choices may depend on previous outcomes. Pair permutations
and within-pair swaps preserve the marked point, so formulas below cover every
labelled such history, including stopping on the edited path.

At depth t the active edited function is

    c_t=b_(m-t)(Y_free)-2*1{all remaining coordinates=0}.

There are k=m-t intact pairs and t+1 physical dummy bits (w and the t partners).
The point mass is delta_t=2^t delta, and its remaining dimension is n_t=2m+1-t.
All incident seed edges at the marked point remain nonpivotal. Therefore

    I(c_t)=k+2n_t delta_t,
    Inf_j(c_t)=1/2+2delta_t for every member j of an intact pair.       (1)

The outcome-1 terminal of that query is a character on the partner times b_(k-1),
with influence k and entropy 2(k-1). Irrelevant coordinates are retained in the
reference alphabet; none of the informative dummy occupancy is discarded.

Let Q_0 be the FULL original squared spectrum of c_m. Define Q_t ONLY by marginalizing
Q_0 over the t physically queried Fourier coordinates. No child reference is reset.
Every Q_t is normalized and strictly positive: the original amplitudes sigma A-2delta
and -2delta are nonzero because A>=4delta>0 at m>=2, and marginalization preserves
strict positivity. The actual P_t is the spectrum of the physical c_t.

## 2. The exact nonflat likelihood formula

Let W denote occupancy of w, J the set of the t exposed partners, and sigma the
quadratic Fourier sign on the k untouched pairs. Fourier summation of each removed
pair coordinate gives 2 if its partner label is zero and 0 otherwise. Consequently

    Q_t(T)=2^t [1{W=0} A^2 +4delta^2
                    -4delta A sigma*1{W=0,T_J=empty}],
    P_t(T)=[2^t A sigma*1{W=0,T_J=empty}-2delta_t]^2.

The bent sign assertion is proved by the two-bit coefficients (1,1,1,-1)/2 and
tensor multiplication. In particular, it concerns the actual canonical phase,
not arbitrary Boolean or real flat phases.

Since 2delta=A^2, their full likelihood ratio simplifies to

    P_t(T)/Q_t(T) = 2^t,                         if W=1 or T_J=empty,
                 = 2^t A^2/(1+A^2),             if W=0 and T_J nonempty. (2)

For any next intact-pair coordinate j, the two labels T and T+j have the SAME
W and J. Thus (2) is constant on the entire j Fourier pair. Equivalently,

    P_t(T)/(P_t(T)+P_t(T+j))
      = Q_t(T)/(Q_t(T)+Q_t(T+j)).                              (3)

All denominators are positive. This is the substantive source-specific step:
although Q_t generally differs from P_t, it has exactly the right conditional
law for every permissible next data query. It holds for every m,t and pair order.

## 3. Signed reference debit, including BOTH actual query children

Set C_t=CE(P_t,Q_t). At the next physical query let P_0,P_1 be its actual child
spectra and Q'=marginal_j Q_t, used as the SAME normalized reference in both.
The mean actual child spectrum is marginal_j P_t. Finite sums and (3) give

    C_t-[CE(P_0,Q')+CE(P_1,Q')]/2 = B_j(P_t)<=1.              (4)

The bound is the entropy of one binary Fourier coordinate conditioned on all
others. Both full child CE bills occur in (4). Combining it with (1), the signed
rate-2 debit is

    e_t=C_t-average child CE-2Inf_j(c_t)<=-4delta_t<0.         (5)

The inequality is in fact strict at its upper endpoint: an occupied new partner
in the W=0,J=empty cell has nonuniform actual conditional probabilities. No
extra logarithmic degree/dimension bill occurs for these selected data queries.
This is a structured exact conditional-likelihood improvement, not a claim for
arbitrary data queries, arbitrary flat phases or arbitrary real amplitudes.
The likelihood calculation is algebraic once these actual Boolean profiles are
supplied; it is not a new consequence of all Boolean convolution identities.

The active node has reach a_t=2^(-(t+1)) from G. Hence every such query contributes
at most -2delta to the original signed account. For h queries,

    E_Q=sum_(t<h) a_t e_t <= -2h delta.                      (6)

The t-th clean exit has the complete inherited CE

    CE_exit=2m-t-1-log2(1+A^2),
    2I_exit-CE_exit=1-t+log2(1+A^2).                         (7)

For t>=2 this terminal bank is negative and MUST remain signed. It is neither
dropped nor replaced by the terminal's actual spectrum. Formula (7) follows
because the clean spectrum is uniform on its support, where Q_(t+1) is the
constant 2^(t+1)(A^2+4delta^2). The actual exit entropy remains separately known.

## 4. SAME original bank, old debit, full CE and KL at every stopping cut

Let L range over the unchanged b_m terminal, all clean exits, and the current
edited terminal; use their ORIGINAL physical reaches and their marginalized
original references. Define

    S_Q(h)=sum_L reach_L [2I(f_L)-CE(P_L,Q_L)].

One exact influence/CE decomposition at each node yields

    S_Q(h)=S+E_Q,
    S_Q(h)-[D+E_Q]=r>delta/4.                               (8)

There is exactly one S, one old D, and one r throughout the history. The same
term appears in the newly exposed signed terminal bank and in the signed bill;
no ancestor quota is renewed. Negative exit and active terminal banks remain.
This algebraic no-reset telescope is campaign background. What is new is (2)--(6),
which give the permissible edited profiles and a strictly negative next-query
reference debit on all of them, including after earlier edited queries.

For the actual entropy ledger retain K_L=KL(P_L||Q_L)>=0 in full. If E_H denotes
the sum of actual entropy decrements minus 2Inf at the new nodes, then

    E_H=E_Q+sum_L reach_L K_L,
    S_H(h)=S_Q(h)+sum_L reach_L K_L,
    S_H(h)-[D+E_H]=r.                                     (9)

No KL refund is treated as spare bank and no full terminal entropy is omitted.
Unlike E_Q, E_H is NOT claimed nonpositive. A frozen numerical withdrawal rule
that charges E_H while ignoring the matching terminal change is invalid.

## 5. Checks, scope and the next unpaid line

Potential failures are the physical incident-edge sign, retained dummy labels,
normalization/positivity of Q_t, the actual child mean spectrum, the conditional
ratio (3), the sign of the CE debit, negative inherited terminal banks, and an
accidental reset/erasure of old D. The checker reconstructs literal truth tables,
integer Walsh spectra, physical edges, exact incoming marginals and both query
children. It checks (2) and (3) by rational cross multiplication, so equality
does not rest on numerical tolerances. Rational log intervals check (5),(8),
all full terminal CE bills and the positive source residual. The grouped lane
checks all stated m,t cases separately from the labelled literal lane.

The inherited bank may be negative at individual terminals and is not an
independent C=2 admission certificate for each descendant. Full FEI remains open.
The first unpaid extension is querying an already exposed partner or w, or a
specified fresh-reference conversion: these queries change the likelihood cells
in (2), so (3) is no longer supplied by this proof. Arbitrary Boolean cores also
remain outside the statement. NEXT must price that actual occupancy-changing
query from SAME S,r,old D and current references, not repeat intact-pair histories.

An independent direct-character guard at m=2,t=1 tests all three query types.
Both occupancy-changing queries have four mismatched Fourier pairs, two actual
nonconstant Boolean children, and strictly positive signed source debits. Their
debits are approximately 0.8621752 (exposed Y2) and 0.3311632 (w), certified by
rational intervals; the intact Y3 debit is approximately -0.3383124. These are
counterexamples to extending (3) or nonpositive (5) to every remaining coordinate,
not counterexamples to the generic signed no-reset identity (8), or to FEI.
The generic identity still transports their signed costs. What is unpaid is a
useful selected positive-debit/reserve or prescribed-reset inequality beyond it.

The named rational Lean target a067_pair_likelihood expresses: if p0=l*q0 and
p1=l*q1, then p0*(q0+q1)=q0*(p0+p1). This matches the cross multiplication in (3);
positivity and the actual spectral formulas are separate analytical premises.
The compiler attempt was RUNTIME_UNVERIFIED, so neither that algebraic statement
nor the full entropy theorem is called Lean-checked. The claimed rung is the
analytic proof with exact rational verification, pending independent review.
