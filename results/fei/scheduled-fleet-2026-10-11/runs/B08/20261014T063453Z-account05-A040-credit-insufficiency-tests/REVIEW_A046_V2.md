# Independent reconstruction of A046 v2

Target: A046-SEPARATOR-LAYER-CUTOFF-RESERVE@2, digest
bd27ee5a2c778775819779bfeceee08d76d1f3f64f9e9667a7dc13e941bf547f.
Reviewer A040. Verdict: **HOLDS**, at the full exact v2 claim scope,
without repair. Source's statement and hypotheses remain unchanged.
The additional biased-core lemma in BIAS_EXTENSION.md is separate and
does not repair or contribute to this source version.

## Balanced rare-row proof

At a live separator query put rho=2^{-(j-1)}, d=rho e/2. For the
underlying branches G=1+WUV(g-1), H=1+(U OR V)(g-1), their means are
1-eta and 1-eta-e, and mismatch probability e/2. Separating the empty
data frequency from Parseval gives the exact three moments

    sum_nonempty Ghat^2=2eta-eta^2,
    sum_nonempty Ghat(Hhat-Ghat)=-eta e,
    sum_nonempty (Hhat-Ghat)^2=2e-e^2.

The full constant row is u0=1-eta-d,v0=d. The nonconstant empty-
residual-selector rows therefore have total mass
q_star=2eta-eta^2-rho eta e+rho^2(e-e^2/2), derivative mass
b_star=rho^2 e(2-e)/4, and q_star<=2eta+rho^2e. These identities are
checked against direct integer Walsh amplitudes in the independent code.

The binary erasure remainder bound and log-sum imply

    B/d<=2+rho log2(euler/(2-e))
             +rho log2(1+2eta/(e rho^2))
             +d log2(euler/d^2).

Compatible events give eta<=8e^2/25. When e<=1/8, the three variable
terms are strictly below 2/3,9/20,19/32, respectively: euler<11/4,
ln2>2/3, ln(1+x^2)<=x, and monotonicity of x log2(euler/x^2) on
(0,1/16] suffice. Thus B/d<1781/480<4 at every separator length.
These constants and their sum are independently checked exactly.

Consequently min(R,T)>=4 has zero separator bill. In particular the
previous A040 old-envelope counterfamily has zero actual prefix bill
for h>=3, while its original V/I~log(width) obstruction stays valid.
There is no contradiction: actual good rows have now been deleted.

## Remaining widths and the complete stopped-core ledger

If min(R,T)<=3, the accepted v1 cutoff has at most five eligible layers.
Set m_star=0 for min(R,T)>=4, otherwise use that cutoff. Define the
potential as the actual reached suffix sum of face prices over eligible
layers, exactly as in A040's v1 review. It evaluates to the source W_j,
with physical drift c_j if j<=m_star and zero otherwise. It is never
renewed after failure or descent. The already accepted physical accounts
give, for M=min(s,m_star),

    Q_bad<=W_s
      <=M I_other+max(M-1,0)I_sep/2+M I_terminal
      <=5I_other+2I_sep+5I_terminal<=5I(F).

After separator failure/success, the balanced core is unchanged, so
the point/union descendants retain v1's strict K4 goodness. The entire
controller prefix is thus covered. The exact B+JS entropy telescope,
JS<=2d/ln2, and all terminal laws yield

    H(F)<=(4+2/ln2)(I_sep+I_other)+W_s+pi H(g).

With independently certified H(g)<=C0 I(g), this implies exactly the
source rate max(9+2/ln2,C0+5). No stopped-core bad nodes are counted in
the controller prefix. No arbitrary terminal FEI premise, reference
transfer or root-output refund is implicitly accepted.

## Review scope

This reconstructs every clause of the exact source v2 statement without
repair; the v1 dependency was independently accepted in the preceding
A040 stage. The finite checks have separate physical and formal-rational
domains; their final PASS records are in out/. Source code is not
executed or imported. The final validation readback supports HOLDS.
Validation is complete: 92 physical node occurrences across the source,
biased and interleaved tests; 4,200 formal moment rows; 1,296 formal
reserve cases; exactly 30,000 final nonpilot assertions, all PASS.
Source acceptance uses the balanced slice and the full reserve proof;
the additional biased checks are not attributed to the source theorem.
Independent review of A040's biased continuation remains a distinct
obligation, rather than self-acceptance.
