# A025 stage 3: point-separator reserve replay

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage extends A023's one-bit overlapping-event
controller to a point-selector block, separating the complete face price
from the actual bad-node price. Entropy is in bits, outputs are signs,
inputs are independent uniform bits, and histories have physical reach
probability. Bad means strictly B_i>4 Inf_i. J(A)=I(1-2A)/2.

Let S,W,U,V be compatible point indicators on disjoint blocks of widths
s,L,R,T, and let g be an independent balanced Boolean core. Set
A=WUV OR SU OR SV and F=1+A(g-1). All widths are positive integers.
For R=T=1 and every s,L>=1, the policy exposing S first and then the
appropriate WUV or U OR V branch has zero localized bad-node prefix
cost, and keeps terminal entropy pi H(g). This is a quantified class
result, not an all-controller theorem.

The actual Boolean rare-event family F_s has L=2s, R=T=1 and g=z.
For the explicitly defined unfiltered separator reservation
R_all=sum_reached_separator_nodes reach*I(child_product)/2, it satisfies
R_all/I(F_s)>=11s/48 and
R_all/(I(F_s)-I_separator)>=11s(s+1)/60. This refutes every finite constant
in that repeated COMPLETE-price rule. It refutes neither A023's one-bit
v2 theorem nor a bad-node-only rule, nor an existential stopping route,
nor FEI. Its actual complete-tree bad-node bill is zero, and H(F_s)<7I(F_s).

## sources actually read, revisions and theorem locators

- EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, read in full;
  field contract, dispatch, review and frozen-compute sections.
- BOARD.md at stage entry (supervisor 2026-10-14 00:29 UTC), with a later
  opening/B05 reread showing the supervisor's 00:50 UTC update.
- Claude B05 STREAM_NOTES.md v2, 2026-10-11 23:4xZ: localized odd-face
  reduction and rare-flip tower direction. The disjoint tower was paid in
  A025 stage 2; this stage follows its outstanding overlap ownership gap.
- A025 STATUS.md and LEARNED.md, plus the stage-2 proof/claim and ledger
  interface; their fixed-K=4 disjoint-tower scope is retained.
- A023 stage-3 REPORT.md/CLAIMS.json, claim
  A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v2: boundary partition,
  single-separator reserve, arbitrary balanced terminal core and explicit
  prohibition on recycling that reserve.
- A021 stage-3 REPORT.md: arbitrary-order fixed-K obstruction and chosen
  overlap orders. Neither arbitrary-order counterexamples nor its finite
  triple-controller search are repeated here.
- A087 stage-3 REPORT.md: good-cap/JS bank and still-open signed terminal
  ownership interface. It motivates preserving the terminal core here.

Exact source paths/hashes are in out/SOURCE_RECEIPTS.json. Earlier campaign
background and papers are inherited from the completed earlier stages;
no newly asserted theorem requires an unreviewed paper dependency.

## complete derivation or exact first unsupported line

PROOF.md is the complete self-contained derivation. Its new point-switch
criterion is valid for arbitrary Boolean branches G,H: if
gamma=P(G!=H)>0 and rho=2^-(j-1), then at a live point-selector query

    B_i/Inf_i <= 2+log2(e)/sqrt(e gamma).

Thus gamma>=1/4 implies every such query is strictly 4-good, even when
the actual coordinate influence tends to zero. This uses paired Fourier
rows, exact residual-selector multiplicities and a log-sum bound; it does
not substitute h2(d) for the actual spectral erasure entropy.

Write alpha=2^-s, eta=2^-(L+R+T), e=2^-R+2^-T-2^-(R+T)-eta,
JB=(L+R+T)eta and JC=R*2^-R*(1-2^-T)+T*2^-T*(1-2^-R).
The directional cuts of WUV and U OR V are disjoint, giving JD=JB+JC.
The exclusive physical accounts are

    pi=eta+alpha e,
    I=s alpha e+(1-alpha)JB+alpha JC+pi I(g),
    R_all=alpha[s JD+e s(s-1)/2+s e I(g)].

The residual-selector term e s(s-1)/2 causes repeated full-price failure.
For the counterfamily, eta=alpha^2/4, e>=11/16, s alpha<=1/2,
I/alpha<=(3/4)s+15/8<=s+2 and
(I-I_separator)/alpha<=15/8. Also
R_all/alpha>=11s(s+1)/32, proving the two stated all-s bounds exactly.
I tends to zero and P(F_s=-1)=pi/2 tends to zero; these are actual sign
functions in dimension 3s+3, with no relaxed spectra.

For R=T=1, the switched branches have gamma=e/2>=5/16. Their selector
nodes are good by the new criterion. The inactive branch is a conjunction
and has constant-child splits with B/d<3. The active OR branch first has
d=1/4 and B<=h2(1/4)<1; its remaining control split has a constant child.
Stopping at g keeps pi H(g) and removes exactly I_separator+I_other.

For completeness, the JS bank used to telescope entropy follows from
the scalar inequality

    [p ln(2p/(p+q))+q ln(2q/(p+q))]/2
      <= (sqrt(p)-sqrt(q))^2/2.

Put x=(p-q)/(p+q). Its proof reduces to
[(1+x)ln(1+x)+(1-x)ln(1-x)]/2<=1-sqrt(1-x^2);
differentiate and use artanh(x)<=x/sqrt(1-x^2), itself obtained by
comparing derivatives for 0<=x<1. Symmetry and limits cover the other
cases. For squared child Fourier coefficients, sum(|a|-|b|)^2 is at
most sum(a-b)^2=4d. Hence JS<=2d/ln2. The good policy gives

    H(F)<=(4+2/ln2)(I_separator+I_other)+pi H(g).

For g=z the terminal entropy is zero, and the terminal literal query has
B=0. This proves the full-tree zero bad-node bill and H(F_s)<7I(F_s).

First unsupported universal line: when the switched branch disagreement
gamma<1/4, no general history-measurable bad-node-only reservation has
been proved that debits each shared control/core account only once and
retains the complete terminal entropy. The sufficient good-node estimate
does not resolve that regime.

## executed validation with domain, arithmetic, commands and outputs

All jobs used python -X utf8, one computational job at a time, no GPU,
with a frozen 180 MB memory estimate; no job triggered the >300 MB gate.
There was no automatic dimension escalation. Before execution, the pilot,
full, direct reproduction and replay specifications were saved under out/.

Commands, relative to this run directory:

    python -X utf8 code/separator.py pilot
    python -X utf8 code/separator.py full
    python -X utf8 code/reproduce.py
    python -X utf8 code/reproduce.py --replay
    python -X utf8 code/finalize.py

The discovery pilot covered s=1..4, L=2s, R=T=1: four families, ten
separator nodes, 438 assertions, 0.0855 seconds. The frozen full run
covered s=1..6 and L,R,T=1..3 (162 cases), plus 24 counterfamily cases
s=1..24 (186 declared entries including one duplicate). It checked 867
separator-node occurrences and passed 28,019 assertions in 560.025 seconds;
maximum dimension was 75. It uses exact integer Fourier category
multiplicities, rational physical ledgers and outward 100-bit dyadic
logarithm intervals from a 40-term atanh series with proved tail.
out/full_RESULTS.json contains every expression, sign and interval.

The independent implementation uses explicit truth tables and integer
undirected edge counts, without importing separator.py. Its frozen 18
families through dimension 12 passed 90 exact checks in 0.1274 seconds:
total influence, separator full price, influence telescoping, actual core
reach probability and terminal influence. Replay recomputes every saved
sign with a different 35-term series and 104-bit outward intervals.
Replay passed all 431 distinct saved sign certificates, with 952 total
assertions including the repeated direct checks, in 148.122 seconds.
Final counts/status are recorded in out/REPLAY_RESULTS.json and
out/VALIDATION_SUMMARY.json. These are independent implementations by
the same author; independent agent review is still pending.

The finite larger-R,T grid is evidence only about its declared separator
nodes. No all-width theorem or all-order theorem is inferred from it.

## proof dependencies and changed downstream conclusions

There are no external mathematical proof dependencies: the boundary,
selector, entropy and influence identities are reconstructed here.
REVIEW_A023.md independently confirms the boundary partition and the
single-separator reserve of A023 v2 at that interface. It is deliberately
a partial source-bound review, not acceptance of every bundled assertion.
The proposed repeated unfiltered extension is false; no existing indexed
claim or its dependents are invalidated. The actual localized B05 bridge
survives and is paid on this overlapping controller family.

## one next mathematical action and independent reviewer

Next: derive a bad-node-only ownership reserve for the same point-switch
controller when gamma<1/4, preserving pi H(g), instead of renewing complete
face prices. A087 or A094 should reconstruct PROOF.md §§1–4, especially
the paired-row normalization and the all-s counterfamily bounds. A023 is
the source owner/consumer for the multi-bit extension; Claude B05 and B20
should preserve the explicit scope distinction.

## actual persistence receipts or precise save blocker

All required protocol files, proof, source-bound review, frozen specs,
scripts and exact outputs are saved in this A025 run directory. Rolling
STATUS.md, WORKLOG.md and LEARNED.md are updated locally. Hashes, schema
checks, observed counts and file-size checks are in out/ARTIFACT_CHECK.json
and out/VALIDATION_SUMMARY.json. Independent agent acceptance, supervisor
copy and downstream use are pending and are not represented as completed.

**Universal bridge:** This stage moves C019 stopping-tree payment by
retiring unfiltered repeated full-face reservation, with an actual
rare-event Boolean family and all-s lower bounds, while paying the same
family's actual localized bill by a moderate-disagreement point-switch
policy with complete terminal entropy retained. It does not falsify the
universal existential localized route. What remains is exclusive
bad-node ownership in the small-disagreement regime and a universal
terminal certificate. NEXT targets precisely that unpaid history transfer,
rather than enlarging an already-paid disjoint tower or accumulating
another isolated class benchmark; that is the shortest unresolved step
toward a general C019/C024 payment theorem and full FEI.
