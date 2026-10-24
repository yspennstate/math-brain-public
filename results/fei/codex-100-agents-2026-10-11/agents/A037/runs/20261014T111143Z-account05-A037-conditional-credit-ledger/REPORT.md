# A037: one further non-flat data frontier under an inherited reference

Full FEI remains OPEN. This stage follows the live A038/A039 history rather than repeating the lead's completed B05 benchmark. One fixed non-flat core and sixteen next-data policies are exactly checked. A single reference remains inherited throughout, the final conversion is made only once, and every terminal entropy and reference KL is retained. The new scoped application awaits independent review.

## exact target, quantifiers, hypotheses and units

Use uniform physical bits (x,a,b,z0,z1,z2) and the actual reached priority root

    F=-1 if x=0,a=1; F=v(z) if x=1,b=1; F=+1 otherwise.

The core is truth-code 91 under A039's explicit convention v(j)=+1 when bit j of 91 is set, -1 otherwise, namely (+,+,-,+,+,-,+,-). It is the source's positive conditional-conversion witness. Its inherited root reference is the completed canonical nonempty entropy projection M, not the product of spectral marginals. The fixed physical history queries a, then z1 in both a children. At the next frontier, independently choose z0 or z2 in each of four reached branches: exactly sixteen policies, no symmetry reduction. These are eight-terminal-leaf trees, not a claim about all adaptive histories or all cores.

Information and code costs are in bits. At a query with actual parent spectrum P and inherited Q, spectral erasure releases E, outcome mismatch is O=D_2(fair||Q_Y), and the two Bayes children are Q_y. The remaining leaf KL is K_end. The final converted leaf reference is each actual leaf's product projection, with mean TC_end. Define A=D_2(P_root||M), sigma=TC_end-K_end and D_end=sigma-E_tot=O_tot+TC_end-A. No intermediate product reset is exercised. The earlier-frontier conversion below is a diagnostic, not an additional withdrawal.

## sources actually read, revisions and theorem locators

Read BOARD.md at the start (supervisor snapshot 2026-10-14 11:05 UTC), B08 STREAM_NOTES.md v2 dated 2026-10-11 23:35Z, and own STATUS.md. The lead B05 k=2 CF/SF target is complete in A037 run 20261014T043944Z; the board now routes A038/A039 to non-flat descendant ownership. Read A039 run 20261014T055326Z REPORT.md, PROOF.md Sections 1-3, out/SUMMARY.json and the source convention/root/step definitions in code/mixed.py. Read A038 run 20261014T051947Z REPORT.md for the certified parity child owner and its arbitrary-core gap. Read A039 run 20261014T025407Z REPORT.md and PROOF.md for the original root-occupancy transport and alternative-reset distinction. No peer checker is imported or executed. The protocol's exact required fields are checked from EXECUTION_PROTOCOL.json; its unchanged revision remains 2026-10-11-execution-v2.

The older campaign/paper reads retain their previous recorded scope; no external paper result is needed for this finite application or the reference-bracketing proof. Source hashes and precise local paths are in out/SOURCES_READ.json. Later claimed all-core/parity theorems are context, not unreviewed logical premises. The selected source witness is reconstructed independently from its raw Boolean truth table.

## complete derivation or exact first unsupported line

### 1. Canonical reference and a rigorous rational implementation

Let P be the raw squared Fourier law, v=1-P(empty), d_j=P(j in S) and r_j=d_j/v. The canonical entropy maximizer on nonempty sets has theta_j=c r_j, where the unique positive c satisfies

    1-c=product_j(1-c r_j).

Completing it by the original empty mass gives M(empty)=P(empty), M(S)=v product_j theta_j^(1[j in S])(1-theta_j)^(1[j not in S])/c for nonempty S. Log M on the nonempty support is affine in its indicators; matching marginals and Gibbs prove the entropy-projection property. The polynomial is strictly concave over the supported interior, vanishes at zero, has positive slope there and is negative at one, giving the unique positive crossing. The independent checker obtains a 48-step Fraction bracket [c_lo,c_hi] and verifies both endpoint signs.

The actual calculation uses a single EXACT RATIONAL reference M0. Set c0=(c_lo+c_hi)/2, theta0=c0*r, Z0=1-product_j(1-theta0_j), and normalize the nonempty product by Z0, not by c0. Preserve M0(empty)=P(empty). This avoids pretending that a rational approximation satisfies the canonical normalization equation. M0 is chosen once at the root and is retained without any descendant selection. Its normalized mass is checked exactly.

For every root atom the checker bounds the canonical M(S) by rational products at the two bracket endpoints, including the reciprocal c normalizer. It then certifies

    abs(log2(M(S)/M0(S))) < epsilon = 2^-36.

This supplies an explicit approximation error rather than silently substituting a different reference law.

### 2. Why the reference approximation is paid once, independently of depth

If two root references obey 2^-epsilon Q0<=Q<=2^epsilon Q0 atomwise, every common nonnegative stochastic kernel preserves that inequality on the JOINT terminal-history/output law. This follows by multiplying each root atom by the same kernel and summing; no KL or entropy estimate is assumed. Erasure of a spectral coordinate is such a marginal map. The function-specific physical kernel is likewise common to both references, including a declared fair extension on source-zero rows.

At a positive history l, each conditional reference divides the joint atom by its own history mass. The two masses obey the same epsilon ratio bound, hence posterior references satisfy a 2epsilon ratio bound. This depends on conditioning ONCE on the complete history, not on charging the error at each intermediate normalization. Therefore root KL A differs by at most epsilon, cumulative outcome KL O_tot (a KL to the complete transcript reference) by at most epsilon, and expected terminal KL by at most 2epsilon. In particular

    abs(D_end(M)-D_end(M0)) <= 2epsilon.

For the conditional-versus-quotient decomposition the error is at most 4epsilon because it subtracts full and quotient reference KLs. These bounds hold for any finite compatible tree length; they do not apply to newly reselected descendant models. This is the precise approximation/no-reuse interface used in the certificate.

### 3. Exact physical transitions and complete account

For queried i, q(T)=P(T)+P(T union i)=(P0(T)+P1(T))/2, with the children obtained from the signed raw Walsh transform. Erase i in Q as well. Apply k(y|T)=P_y(T)/(2q(T)) on positive fibers and k=1/2 otherwise to both actual and reference residual laws. This gives Q_Y and Bayes-normalized child Q_y. Exact likelihood-ratio factorization on every supported atom proves

    D(P||Q)=E_i+O_i+average_y D(P_y||Q_y).

Iterating with true physical weights gives A=E_tot+O_tot+K_end. The sole final reset to child products has sigma=TC_end-K_end and D_end=O_tot+TC_end-A. Thus D_end<0 means the original account pays the full final outcome and product-KL obligations; it does not discard the terminal spectral entropy, and it does not certify any upstream controller/core cost.

Let T=(x,b) at a final leaf and Z its remaining data coordinate(s). The code separately retains sigma_T=D(P_T||R_T)-D(P_T||Q_T) and sigma_Z=[D(P||R)-D(P_T||R_T)]-[D(P||Q)-D(P_T||Q_T)]. Their sum is sigma. A positive quotient component cannot be erased merely because the conditional component saves more. Neither component is spent separately from the complete reset.

### 4. The finite continuation result

At the earlier four-leaf frontier the independent canonical-reference sign certificates give

    D_end < -19/100,
    conditional sigma > 1/4.

Rounded diagnostics for M0 are D=-.190541152183, conditional sigma=.266316248293, quotient sigma=.011179585117, E_tot=.468036985593, O_tot=.051563434846 and K_end=.473111820764. This reconstructs precisely the source witness; no acceptance of A039's full 1,152-policy theorem is asserted from a single case.

For EACH of the sixteen further-data policies, with the canonical-reference errors included, the certified statements are

    D_end < -7/10,
    conditional sigma < -1/10,
    quotient sigma > 0,
    every actual leaf 4I-H >=0,
    mean actual leaf surplus 4I-H >9/5.

The M0 diagnostics agree across these policies at D=-.744561266480, conditional sigma=-.116669796957, quotient sigma=.009264817350, E_tot=.637156286873, O_tot=.085463084706, K_end=.270092869624, TC_end=.162687890017, H_end=1.662687890017 and mean 4I-H=1.837312109983. No exact equality across policies is inferred merely from matching displays; every policy is independently enclosed and passes the same strict signs.

The positive debit at the intermediate conditional component becomes a saving after the further actual data query. The total reset at the final frontier is negative; zero terminal-surplus withdrawal is required. All eight terminals, including the constant and character cases, keep their exact inherited references. Source-zero rows at the queried nodes happen to number zero for this fixture, a checked finite fact rather than a deleted-reference convention. If such rows occur elsewhere, they remain in the reference and use the declared kernel extension.

For the actual evaluated transaction there is no earlier intermediate reset or separately committed debit. More generally a previously justified reservation b against this SAME unchanged root account remains eligible if b<=7/10, because A-O_tot-TC_end>7/10. This is a conditional bookkeeping admission, not evidence that a particular upstream charge has been paid or that another reset can be exercised while retaining the old Q. The original total account is never restarted.

### 5. Exact first unsupported line

For arbitrary unfinished, non-flat cores, no theorem proves that a suitable next physical data query makes the complete conversion affordable from the SAME original account after all genuine incoming controller/source reservations, with both terminal bills retained. The free-conversion conclusion cannot extend to all dimensions (A038/A039 parity already rules that out). The length-independent approximation bound removes numerical/history accumulation, not this mathematical eligibility gap. No dimension-independent FEI constant or Boolean H/I counterfamily is claimed.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before execution. Command from A037:

    python -X utf8 -B runs\20261014T111143Z-account05-A037-conditional-credit-ledger\code\continuation.py

One six-bit raw truth table, one fixed first/second history, sixteen next-frontier policies; no symmetry quotient or automatic escalation. Integer Walsh transform and Fraction probability/influence calculations reconstruct actual spectra, normalization, physical branch likelihoods and per-atom likelihood-ratio identities. Every marginal influence is independently checked by raw physical edge counting. Exact factorization proves the equalities; interval overlap is only an additional consistency diagnostic and is not used as a proof of equality.

Directed fixed-point intervals on a 2^160 grid implement rational range reduction, positive/negative coefficient scaling, and multiplication/division extrema. Logarithms use forty terms of 2 sum_(j=0)^39 z^(2j+1)/(2j+1), with z in [0,1/3] and rigorous tail <=2*(1/3)^81/[81*(1-1/9)]. Zero logarithms are handled exactly. Canonical atomwise approximation, strict reset signs and every terminal-surplus claim use separated rational endpoints. CHECK.json stores all brackets, rational root-reference masses, complete leaf accounts and policy certificates.

Final pass: 2,750 counted exact/interval assertions, runtime 0.1716114 seconds. The first exploratory pass had no failed mathematical assertion; the final pass adds strict signs and exact log(1)=0 normalization. Memory estimate <50 MB, actual peak unmeasured; no >300 MB job, GPU, background process or memok-gated job was started. Floating displays in the report are explanatory only.

## proof dependencies and changed downstream conclusions

The selected fixture and canonical-reference convention are source-bound to A039, but the table, root bracket, exact normalization, physical transitions, numerical enclosures and next-query policies are independently implemented without importing a peer checker. The inherited account identity is independently reconstructed rather than assumed as an unreviewed premise. The length-independent approximation guarantee is proved by an elementary atomwise kernel/conditioning argument, not by repeated approximate KL computations.

This scoped continuation advances an existing application instead of opening another broad universal candidate while stream queues are substantial. A038/A039/A064/A087 now have the next actual frontier for the positive conditional-conversion witness, with no restarted root account and no terminal-bank spend. A083/A092 can use the ratio-bound convention when separately certifying a canonical root in a shared inherited history. New independent acceptance and shared registry adoption remain pending.

## one next mathematical action and independent reviewer

Next: repeat the same-reference calculation on the biased rare core v_n, carrying an explicitly booked incoming conversion and all nonconstant child terminals; identify whether a positive delayed debit can be paid by the remaining ORIGINAL certified owner rather than a renewed mean 4I-H bank. Use its compressed exact support to avoid large cubes. A088/A094 should review the new length-independent ratio proof and finite certificates; A039/A092 should audit final conditional/quotient ownership. No messages were sent.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/continuation.py, code/persist.py, out/FROZEN_SPEC.json, out/CHECK.json, out/SOURCES_READ.json and out/ARTIFACT_SHA256.json. Updated the three A037 rolling files. Schema, identical progress/delta and SHA256 receipts are checked locally; immutable old runs and other agents' folders are untouched. Mirrors, copying, brain ingestion, index adoption and downstream use are unverified.

Universal bridge: This stage moves C024 history transfer and its C019 ownership interface by carrying the positive non-flat conditional-debit witness through a further real data frontier under one inherited occupancy reference: all sixteen policies have total conversion below -7/10, retain all terminals, and spend no terminal surplus. The accompanying canonical-reference ratio certificate charges approximation once over the entire history, independently of depth. No universal constant changes; biased/high-dimensional positive-debit eligibility after genuine prior bookings remains open. NEXT tests that named remaining-owner condition on the existing rare-core obstruction, the shortest route to the universal induction gap rather than another generic chain rule or already closed finite-family entropy bound.
