# exact target, quantifiers, hypotheses and units

A049 / B10 minimal falsifier extraction. Full uniform-cube FEI remains OPEN. This stage is an extraction and verification of the already refuted B09-TAXFREE-BIASED-UNCERTAINTY helper, not a new search against that retired assertion. Its scope is: for every finite Boolean sign under an interior product bias and every singleton physical reveal X, claim J_X <= M_X, with M_X=H(S_X|S_res), and J_X=I(X;T) in the experiment that chooses the physical child with its actual probability and then samples its normalized squared Fourier spectrum. All entropies use bits, include the empty atom, and use the product-biased orthonormal basis. Zero atoms contribute zero.

The extraction gives the smallest total physical dimension, n=2, one fixed common bias p=q=1/4, a complete four-entry truth table, and one integer sign comparison. More restrictive minima are n=3 with all residual coordinates fair, and n=4 with fair residual coordinates and both physical children balanced. The latter minima hold for arbitrary interior selector bias, not just the displayed 1/4. The common dyadic bias has the smallest possible interior dyadic denominator: denominator 2 is the uniform case and fails to witness the assertion on every two-bit truth table; denominator 4 supplies the witness. No optimality over all rational denominators or gate representations is claimed.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and the campaign plan were consulted in the read-only report tree. BOARD.md at stage start was the supervisor snapshot 2026-10-11 22:37 UTC. The requested claude/B10/STREAM_NOTES.md was absent; no lead directive was inferred.

Original B09 REPORT.md sections 2-4, run 20261011T195500Z-account01-B09-biased-restriction-uncertainty, source pin adb671ffcda143fa68347806bb96e8c305621a7d, provides the original ledger and two-bit AND failure. A046 REPORT.md, run 20261011T214251Z-account05-A046-current-candidate-intake, provides the already established q=1/4 rare-selector lower bound and p=1/8 finite certificate. A047 REPORT.md, run 20261011T220210Z-account05-A047-boundary-search, supplies the existing arbitrary-child endpoint classification. A096 REPORT.md, run 20261011T215017Z-account05-A096-live-gap-ledger, supplies the existing uniform leading-coefficient upper bound. These are acknowledged sources of the mechanism, not proof premises needed by the finite certificate. B05's original sparse-activation no-go and B19's reconstruction were read for scope; neither is reopened.

The supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source-note collection were ingested; BLOCK_RESTRICTION_IDENTITY (equations 1-4) and ONE_BIT_ENDPOINT were inspected for the physical versus spectral distinction. Threshold 38-page text, introduction/Theorem A, Proposition 7.1 and Proposition 8.1, and the earlier 29-page text were inspected for normalization and composition scope. Percolation 30-page and other 31-page text introductions/Theorems 1.1-1.2 explicitly restrict their conclusions to geometric percolation classes. These supplied manuscripts are context, not mathematical dependencies, and this stage does not claim to audit every proof in them. The source manifest records local byte hashes and reading scope; those hashes do not themselves establish equivalence to cited repository commits. No priority or novelty claim is made.

# complete derivation or exact first unsupported line

## 1. Definitions and exact Boolean source

For independent bits X,Y in {0,1} with Pr(X=1)=p and Pr(Y=1)=q, take

    f(X,Y)=1-2XY.

Equivalently on the sign cube, X=(1+x)/2 and Y=(1+y)/2. The input bias here is not uniform; the corresponding sign-coordinate means are -1/2 when p=q=1/4.

| X | Y | f |
|---|---|---|
| 0 | 0 | +1 |
| 1 | 0 | +1 |
| 0 | 1 | +1 |
| 1 | 1 | -1 |

In the orthonormal centered basis phi_X=(X-p)/sqrt(p(1-p)), phi_Y=(Y-q)/sqrt(q(1-q)), the coefficients are

    1-2pq, -2q sqrt(p(1-p)), -2p sqrt(q(1-q)),
    -2 sqrt(p(1-p)q(1-q)).

At p=q=1/4 these become (7/8,-sqrt(3)/8,-sqrt(3)/8,-3/8). Their squared law, ordered empty,X,Y,XY, is

    P=(49,3,3,9)/64.

The retained Y-label marginal is Q=(13,3)/16. The X=0 child is constant with spectrum (1,0). The X=1 child is 1-2Y with spectrum R=(1,3)/4. Thus Q=(3/4)(1,0)+(1/4)R, proving that the channel is the actual normalized physical-child experiment.

The definitions give

    M=H(P)-H(Q),   J=H(Q)-(1/4)H(R),
    E:=J-M=2H(Q)-H(P)-(1/4)H(R).

These formulas also follow directly from the entropy chain rule, without using B09's pending uncertainty theorem.

## 2. One exact integer sign certificate

Expanding the entropy expressions and collecting prime logarithms gives

    32 E = 48 + 6 log2(3) + 49 log2(7) - 52 log2(13)
         = log2(L/R),
    L=2^48 * 3^6 * 7^49,
    R=13^52.

Exact integers:

    L=52719499781386523982199270969636322098232779259710399315968
    R= 8415003868347247618489696679505181495471801448798649088081
    L-R=44304495913039276363709574290131140602760977810911750227887.

Hence E>0 follows from one integer comparison. The stronger comparisons 4R<L<8R give the rigorous margin

    1/16 < J-M < 3/32 bits.

No approximation to a logarithm, interval library, transcendental error bound or floating-point entropy evaluation is needed. The generic checker independently clears all rational entropy weights: it obtains the rational product (L/R)^2 and scale 64, agreeing with the collected-prime expression.

## 3. Minimal number of variables, and the common bias

On n<=1, revealing a relevant nonempty block leaves no residual coordinate. The retained spectral label is deterministic, so J=0. If the revealed block is empty or irrelevant, J=M=0. Since conditional entropy M>=0, no smaller-dimensional violation exists. The displayed two-bit Boolean witness proves dimension minimality over all interior product biases.

For the common dyadic bias, the only interior choice of reduced denominator 2 is p=q=1/2. Every two-bit sign truth table is either a signed character (8 tables) or has exactly one sign different from the other three (8 tables). A signed character has a point-mass spectrum, and E=0. A one-defect table has flat squared spectrum on four labels, so H(P)=2, H(Q)=1; revealing a coordinate gives one constant child and one fair dictator child, whose average entropy is 1/2. Hence E=2-2-1/2=-1/2. This proves analytically, and exhaustive exact arithmetic confirms, that the coarsest common interior dyadic bias supplies no violation. The denominator-4 choice p=q=1/4 does.

This is a fixed finite simplification. Setting both p and q rare together is not a replacement for A046's sharp endpoint family, which fixes q=1/4 and takes only p to zero.

## 4. Fair residual coordinates: minimum n=3

Let g,h be the actual Boolean children on a fair m-bit residual cube, and let the independent selector choose h with probability p. With G_T,H_T their real Fourier coefficients, parent masses and the residual marginal are

    a_T=((1-p)G_T+pH_T)^2,
    b_T=p(1-p)(H_T-G_T)^2,
    q_T=(1-p)G_T^2+pH_T^2.

If g=h, then M=J=0. If g=-h, their squared spectra coincide, so J=0 and M=h2(4p(1-p))>=0. If their spectral supports are disjoint, the residual label determines the physical child and J=h2(p). Each occupied fiber has selector-label entropy h2(p), so M=h2(p) and E=0.

On m<=1, the Boolean children are signed characters, so every pair is equal, opposite or has disjoint spectral supports. Thus no selector bias can produce E>0 with fewer than two fair residual coordinates.

For m=2 choose g=1 and h=1-2UV, with U,V independent fair bits. The h coefficients are (1/2,1/2,1/2,-1/2), up to truth-table convention. At p=1/4 the parent squared masses consist of (49,3)/64 at the empty residual label and (1,3)/64 at each of its three nonempty residual labels. The residual marginal is (13,1,1,1)/16, and H(hat h^2)=2.

Aggregating those three identical nonempty fibers, or substituting in the entropy expression, gives exactly the same E as section 2. Refining a residual label into three equally weighted labels adds (3p/4)log2(3) to H(Q), the same amount to H(P), and (3/4)log2(3) to H(hat h^2); their coefficients 2,-1,-p cancel. The parent circuit is

    F(X,U,V)=1-2XUV,   Pr(X=1)=1/4, U,V fair.

Its truth table, indexed X+2U+4V, is [1,1,1,1,1,1,1,-1]. This supplies the n=3 witness, with the same integer certificate, and proves its minimum under fair residual inputs.

## 5. Balanced children with fair residual inputs: minimum n=4

A balanced Boolean function on a fair two-bit cube has two plus signs and two minus signs. The six such tables are exactly the signed nonempty characters. Balanced children on m<=2 therefore again fall into the equal, opposite or disjoint cases, which have E<=0 for every selector bias. On m=0 balanced sign children do not exist.

On three fair residual bits Z,U,V set

    g(Z,U,V)=(-1)^Z,
    h(Z,U,V)=(-1)^Z(1-2UV).

Both children are balanced. Multiplying both earlier children by a fresh fair character translates every Fourier label by the same fixed set. It preserves H(P), H(Q), both child entropies, M and J. The full circuit is

    F(X,Z,U,V)=(-1)^Z(1-2XUV),
    Pr(X=1)=1/4, Z,U,V fair.

The complete 16-entry truth table, spectra and both balanced child tables are in out/BALANCED_CERTIFICATE.json. The same positive E and integer comparison hold. Thus n=4 is minimal when residual coordinates must be fair and both actual physical children balanced. The checker verifies invariance by comparing the independently generated entropy-product ratios exactly, not by comparing decimal entropies.

## 6. Scope and first unsupported line

This package minimizes a known failed tax-free helper. It does not refute B09's J<=M+Delta(p), A096's sharper uniform upper tax, coefficient-1/2 taxed proposals, existential coordinate selection, an optimized stopping tree, or full FEI. In the original uniform cube the two-bit AND spectrum is flat and H/I=2, providing no conjecture violation. A positive finite biased helper debt is not an unbounded uniform H/I family.

First unsupported line toward the main target: bound the full conditional cost M plus a valid bias tax, and the terminal entropy, by a single nonreused physical influence budget. Neither finite minimality nor the known sharp endpoint coefficient proves that step.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the calculation. The domain is the single equal-bias witness, all 16 uniform two-bit truth tables, all 276 ordered fair-residual pairs on m=0,1,2, and one explicitly specified balanced three-residual-bit pair. No computational symmetry reduction or automatic dimension escalation occurred. The small enumeration validates the analytic classifications; it is not a broader all-dimensional search. Memory estimate was 30 MB, runtime cap 60 seconds, and no >300 MB or heavy job was started.

Command from the assigned A049 directory:

    python -X utf8 runs/20261011T224133Z-account05-A049-minimal-falsifier-extraction/code/check.py

Integer FWHT was checked against direct character sums; Parseval and physical correlations were exact. Product-biased squared spectra were reconstructed by direct weighted truth-table sums in an unnormalized centered basis, divided by rational basis norms. Rational entropy signs were reduced to integer-power products. out/VALIDATION.json records assertion count and measured calculation runtime. The final strengthened check passed 1,363 assertions in 0.022243 seconds, including the rational margin and exact invariant-debt comparisons. Runtime is the only floating-point output.

The extraction is reproducible from code/check.py, its frozen spec and complete truth tables. No numerical search or imported checker output establishes a proof here.

# proof dependencies and changed downstream conclusions

The certificate and minimum-dimension proofs use only actual truth tables, finite Parseval, the entropy chain rule, and log monotonicity. There are no external unreviewed mathematical proof dependencies. A046/A047/A096 are credited for the previously reported mechanism and endpoint bounds; no endpoint novelty is claimed.

The precise downstream change is a two-bit finite regression witness with one common fixed bias, no tunable parameter, no logarithm implementation and a certified margin exceeding 1/16 bit. Additional fair-residual and balanced-child versions prevent attempted repairs based only on those restrictions. This is not a new broad counterexample claim added on top of B10's pending-claim cap; it verifies and minimizes the existing refuted helper's source certificate. Independent acceptance of this extraction is pending. B20 alone owns changes to shared claim or packet registries.

# one next mathematical action and independent reviewer

Next: A050 should test its explicitly versioned repaired stopping/composition ledger on the balanced circuit above, retaining M, the valid bias tax, actual physical branch probabilities and terminal entropy. No replay of the tax-free inequality is needed. The general extraction packet resumes only upon a found violation of a new live helper or a concrete review objection.

Independent reviewer: A092 primary, A090 alternate. A085 may reconstruct the cleared-denominator sign directly from the truth table. Consumers are A050, A042, A057, A071, A084, B09 and B20.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in the assigned run directory, together with FROZEN_SPEC.json, code/check.py, source ingestion code, complete spectra and truth tables, exact finite enumeration outputs, validation, and SHA256 receipts. Rolling STATUS.md is two lines; WORKLOG.md and LEARNED.md retain the result and gap. The finalizer checks protocol field sets, statement hashes, progress-copy equality and the 20 MB file limit, then writes out/PERSISTENCE.json. Supervisor repository copying, mirror verification, independent acceptance and downstream mathematical use remain unperformed and are not claimed. All writes stayed inside A049; no git or Brain write was used.

**Universal bridge:** This stage supports C019 stopping-tree payment by supplying the minimal finite test that exposes an omitted bias tax, including a balanced-child version with fair residual inputs. It moves the verification burden from unequal biases and approximate logarithms to one fixed common bias and one integer comparison; it proves no new universal payment constant. What remains is to pay M plus a valid tax and all terminal entropy without reusing influence. Applying a concrete repaired A050 ledger to this certificate is the shortest next route because it checks the exact unpaid term in the proposed universal bridge, rather than opening another isolated function-class bound.
