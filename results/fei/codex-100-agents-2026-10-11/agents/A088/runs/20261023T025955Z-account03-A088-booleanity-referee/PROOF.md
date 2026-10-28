# Independent review of A067 and the next positive debit

All logarithms are base two. A=2^-m, delta=A^2/2, m>=2. The source is the
canonical b_m=(-1)^(sum_j Y_(2j-1)Y_(2j)), c_m=b_m-2*1_origin, with a dummy
w in b_m. The root G has z terminals b_m,c_m of reach 1/2. Original D,S and
r=S-D are exactly those of A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1.
Nothing here replaces either original terminal reference or renews this bank.

## 1. Independent reconstruction of the edited-prefix theorem

Use Walsh coefficients (1,1,1,-1)/2 for a quadratic pair. If t first members
have been fixed physically to zero, let J be the t exposed partner labels,
W the w Fourier bit, sigma the sign of the remaining m-t quadratic pairs.
The actual restricted spectrum and the marginal of the ORIGINAL c_m spectrum are

    P_t(T)=[2^t A sigma 1{W=0,J=empty}-2^t A^2]^2,
    Q_t(T)=2^t[A^2 1{W=0}+A^4-2A^3 sigma 1{W=0,J=empty}].

This follows by summing the original two Fourier labels of each removed
coordinate, rather than restarting a child reference. Their ratio is 2^t
outside {W=0,J nonempty}, and 2^t A^2/(1+A^2) on that cell. These are positive
laws. A next intact-pair Fourier coordinate cannot change the cell, so P and Q
have equal conditionals on its two-element fibers, exactly as source Eq.(3).

The physical seed is constant +1 along every marked incident edge. Flipping
the marked point creates two directed pivotal edges per coordinate. For an
intact coordinate Inf=1/2+2delta_t, delta_t=2^t delta. Both actual physical
children average spectrally to the parent Fourier marginal (the two squares
of sum and difference). Thus the complete CE drop is the actual conditional
binary entropy B<=1, and its rate-two signed debit is <=-4delta_t.
Original reach 2^(-t-1) makes this <=-2delta per continued query.

An outcome-one exit has a character on its partner and m-t-1 intact pairs.
Its influence is m-t, and entropy 2(m-t-1): a character costs influence one
and entropy ZERO. On its support the inherited Q_(t+1) is constant
2^(t+1)(A^2+A^4), hence its complete CE is
2m-t-1-log2(1+A^2). This independently recovers the source's negative
exit banks at t>=2. No negative term is clipped.

Summing the exact influence and CE decompositions retains old D and gives
S_Q(h)=S+E_Q and S_Q(h)-(D+E_Q)=r. Replacing CE by H adds the SAME full
weighted terminal KL to the bank and the debit. This telescope is existing
background, not the new payment. The source-specific conditional formula and
debit sign are sound. Verdict: HOLDS at the precise canonical selected-history
scope, without a source repair; statement hash is unchanged.

## 2. Exact first exposed-partner profile

Query physical a=Y1 on c_m, keep outcome-one, and on outcome-zero query
physical b=Y2. Let R be the remaining m-1 quadratic pairs, sigma their
Fourier sign, with counts n_+=(4^(m-1)+2^(m-1))/2, n_- similarly with minus.
Q1 is the original reference marginalized over a; Q2 over a,b. For W=0:

    Q1(b=0,sigma)=2(A^2+A^4-2A^3 sigma),
    Q1(b=1,sigma)=2(A^2+A^4),
    Q2(sigma)=4(A^2+A^4-A^3 sigma),
    P1(b=0,sigma)=4(A sigma-A^2)^2,
    P1(b=1,sigma)=4A^4.

For W=1, Q1=2A^4, Q2=4A^4, P1=4A^4. Counts are n_sigma in each cell.
The actual partner influence is 2A^2. Its complete rate-two reference debit is

    e1 = sum_(W,b,sigma) n_sigma P1 log2(Q2/Q1) - 4A^2.

These cells already average BOTH actual child CE bills; no child is omitted.
The query changes the source's likelihood cells, so source conditional equality
does not apply. In particular, e1 is positive, not another negative credit.

## 3. A residual-only payment fails in every dimension of this family

Let e0 be the preceding intact-query reference debit on c_m. The root-weighted
new two-query debit is E=e0/2+e1/4. A concrete proposed extension would pay the
partner from the original residual and the preceding credit:

    e1/4 <= r - e0/2, equivalently E<=r.                    (FALSE)

This is an unregistered proposed extension, NOT the A067 claim. We refute it
with actual Boolean functions retaining all original references and reaches.

Every partner ratio Q2/Q1 lies between 2(1-A) and 2/(1-2A). Positivity and
normalization of P1 give e1>=1+log2(1-A)-4A^2. The integral bound
ln(1-A)>=-A/(1-A), with ln2>2/3, gives

    e1 >= 1 - 3A/[2(1-A)] - 4A^2.

For e0 the W=1 pairs and the W=0,b=0 pairs have binary conditional entropy
one. In W=0,b=1 the conditional bias has absolute value 2A/(1+A^2).
Concavity of binary entropy between its midpoint and endpoints gives
h((1+v)/2)>=1-|v|. Hence B0>=1-2A, and

    -2A-2A^2 <= e0 = B0-1-2A^2 <= -2A^2.

Therefore

    E >= 1/4 - A - 2A^2 - 3A/[8(1-A)].

For m>=4, A<=1/16; each subtracted term increases with A, so

    E >= 99/640 > 1/8 > 7/128 > r.

The bound r<delta(m-1/4)<=7/128 is proved in the previous A088 stage,
PROOF section 1 (its independent exact checks also cover m=2,3). For
completeness its entropy algebra writes r=delta(m-1)+L, where
L=E_sigma[(1-sigma t)^2 log2((1-sigma t)^2)], t=A/2 and E sigma=A=2t.
Using ln x<=x-1 gives L<delta/(2 ln2)<3delta/4. The sequence
delta(m-1/4) decreases for m>=2, proving the bound above.

For m=2, exact rational log intervals give E in (0.10888,0.10890) and
r in (0.00817,0.00819); for m=3 E in (0.21561,0.21563) and
r in (0.00995,0.00997). Thus E>r for EVERY m>=2, with infinite range
covered by the displayed analytic bound, not numerical extrapolation.
The ratio bounds and the bound on e0 also imply e1->1, e0->0, E->1/4,
whereas 0<r<delta(m-1/4)->0. Consequently E/r diverges. No fixed multiple
of this residual alone pays even this one additional coordinate uniformly.

This does NOT refute FEI, source A067, or the signed no-reset identity.
Indeed S_Q(final)=S+E, and S_Q(final)-(D+E)=r still holds. New terminal
banks and debits change together. A fixed-residual withdrawal rule cannot
silently use that change as independently available old capital.

## 4. Keep the complete terminal KL bill

At the partner parent put Kp=KL(P1||Q1), and let Ka,Kb be the two actual
child KL bills against the SAME Q2. The actual entropy debit eH satisfies

    e1 = eH + Kp - (Ka+Kb)/2.

This is a conversion formula, not a new payment. At m=2 these quantities
are approximately e1=.8621752092, eH=.4902229725, Kp=.7445335724,
(Ka+Kb)/2=.3725813358. Both terms on the right of the debit decomposition
are positive. At m=4 they are approximately .9927349476, .0480425825,
.9687280291, .0240356640. The checker certifies these statements with
exact rational enclosures. It would be false to pay the entire e1 by KL
release alone at these dimensions, or discard the actual entropy debit.

## 5. Booleanity and the strongest tested real relaxation

The canonical incident-edge signs and Walsh pair phase determine the exact
spectra and Inf used in section 1. Once those profiles and energies are fixed,
the conditional-law equality, CE sign, and accounting are algebraic/probabilistic;
they do not invoke the full Boolean phase-convolution constraints.

There is a concrete normalized real relaxation of this ENTIRE two-query
experiment, including the root, both z children, all physical queried children,
all full spectral laws, and every Dirichlet influence. On any untouched pair R,
apply the Fourier sign multiplier -1 to its empty label, +1 to its other labels,
uniformly over all other Fourier labels. This is the orthogonal real operator
T=Id-2 E_R, where E_R averages over that pair. It commutes with restrictions
outside R and preserves every squared Fourier coefficient of each restricted
function. Thus it preserves every law, CE, entropy, reference marginal, and
Dirichlet influence in the two-query experiment. In general it destroys
Booleanity: already T b_m takes values 0 or +/-2 on that pair. Every child
remains L2-normalized because restriction and T commute.

The separate exact guard instantiates m=2, retaining the SECOND pair untouched,
checks all root/z/a/partner nodes, and verifies failure of a nonempty Boolean
convolution equation. This is stronger than a mere probability-only relaxation:
it is a family of actual normalized real functions with actual normalized
restrictions and the SAME full ledgers. It covers prefixes avoiding that pair,
not the source's final step that queries every pair. At that final step the
commutation argument is unavailable; no all-history real extension is claimed.

## 6. Honest remaining bridge

The nearest unpaid line is an influence-priced conversion of occupancy-changing
CE and actual entropy debit with their terminal KL and signed banks, or a
specified reset whose FULL conversion bill is funded. The existing residual
plus preceding negative credit cannot supply a dimension-independent payment.
The shortest follow-up is to identify a genuinely additional source or an
allowed total-rate bound, keeping this exact original history. Repeating a
no-reset telescope or proclaiming e1 paid by KL release does not close this gap.
