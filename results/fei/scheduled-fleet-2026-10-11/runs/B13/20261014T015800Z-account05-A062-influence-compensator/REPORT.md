# A062 stage 4: arbitrary-core reserve preservation

## exact target, quantifiers, hypotheses and units

Fix ANY Boolean core g on r bits, any vertex flip g^v, prescribed finite complete continuation trees for both cores, and a finite price C>=0. Append q dummy bits and flip only the selected padded vertex, forming G_q; query the dummies before the core continuations. Its complete minimal reserve converges to Q_C(g), with the explicit error below. For a fresh character product (-1)^z g, similarly edited at one vertex and queried first at z, the complete reserve converges to [Q_C(g)-C]_+. This retains arbitrary child/core reserves and spends one character influence account. Entropies are bits; influences are ordinary. Core dimension and continuation are fixed in these limits; no universal core bound is assumed. The result extends the existing pending reserve candidate to version 3 rather than opens another broad candidate.

## sources actually read, revisions and theorem locators

BOARD.md snapshot 2026-10-14 01:51 UTC, including current B13, A005, A038, A059, A064 and A087 directions; full B13 STREAM_NOTES.md v2; own stage-3 STATUS.md; EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. A061 stage-4 REVIEW_PROOF.md: physical-child and corrected-selection sections, which identify the terminal reserve obstruction without accepting the authored admission chain. A005 LEARNED.md, signed-child eligibility and corrected-price paragraphs. A064 latest DERIVATION.md, full prefix reserve and actual-controller-boundary argument; CLAIMS.json version 2. ERASURE_REDUCTION.md sections 1-2 reread, especially the symmetric scalar JS bound min(d,1-d). Prior own complete reserve proof and exact arithmetic kernel are reused with pinned source hashes in out/SOURCES.json. No new paper/literature priority claim is made.

## complete derivation or exact first unsupported line

DERIVATION.md proves the finite recurrence R_j=[D_j-Cd_j+(R_{j-1}+R(g))/2]_+, d_j=2^(1-r-j), with R_0=R(g^v). Positive-part contraction and the scalar erasure/JS bounds give

|R_q-R(g)|<=E_q=2^-q|R(g^v)-R(g)|+d_q q[r-1/2+C+3log2(e)+q/2].

For the edited character root delta=2^(-r-q), d_z=1-delta and

|R(F_q)-[R(g)-C]_+|<=E_q/2+h2(delta)+(C+2log2(e))delta.

Both errors vanish explicitly at fixed core. This proves convergence of the full recursive reserve, not just entropy continuity, root local ratios, or signed endpoint deficit. The general opposite-branch query also has the retained-child certificate [h2(epsilon)+2log2(e)epsilon-C(1-epsilon)+(R_g+R_h)/2]_+ as an upper bound. For epsilon<=1/2 it is locally paid at C>=6 while the child reserve remains.

First unsupported universal line: bounding the averaged child reserves from unused source slack or another exclusive physical account for a selected arbitrary-core continuation. No bound R(g)<=K I(g) or R(g)<=C is established. A fixed-core q limit does not justify a limit with unbounded changing cores. The proof uses explicit finite-tree contraction estimates; no optional-stopping or uniform-integrability exchange is assumed.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded computation. `python -X utf8 code/check_transfer.py --pilot` checked 32 padded/character roots, 332 assertions, zero failures in 0.030 seconds. The final command without `--pilot` checked 420 roots: all 16 two-bit cores at prices 1,2,6 and q=1..4, plus a three-bit point-defect core at those prices and q=1..6. It passed 3,041 exact assertions in 0.885 seconds. Ordered actual truth-table recursion checked full spent influence, exact edited and opposite clean children, retained clean-child reserve and both error bounds. At r=3,C=1,q=6 the character reserve exceeds 3/4 exactly; its limiting residual is about 0.717. This price-one example certifies that local character payment does not remove an arbitrary residual; it is not a proposed disproof of FEI.

Integer Walsh transforms, direct edge counts, Fraction arithmetic and rational positive log-series bounds with outward 120-bit dyadic rounding supply the certificates in out/EXACT_TRANSFER.json. Display decimals do not decide signs. A rerun strengthened the positive fixture from a nonnegative test to the strict rational margin >=3/4. Job memory was estimated at 120 MB and no admission above 300 MB was needed.

`python -X utf8 code/review_boundary.py` checked all 16 two-bit controllers plus the point-defect controller at three prices: 51 boundary cases and 315 exact assertions, zero failures. REVIEW_NOTE.md independently reconstructs only A064's actual two-dictator frontier identities. Runtime for this separate review was not instrumented. Primary plus review assertions total 3,356; pilot assertions are excluded.

## proof dependencies and changed downstream conclusions

The new transfer uses only the existing Bellman definition, the scalar B<=h2(d) bound and the source-complete JS bound J<=(2/ln2)min(d,1-d). It does not depend on the lead's pending J<=B uncertainty claim. Original scoped single/two-edit conclusions are retained at version 2's exact sources; the version-3 extension changes no earlier constants. A061/A005 endpoint and signed-child results are consumed as motivation, not as premises. A064-TERMINAL-CORRECTED-GLOBAL-DEBT v2 actual-boundary clause independently HOLDS: the two-dictator data frontier retains exactly H(h)/2, I(h)/2 and Q_C(h,T)/2, with the original controller edge account counted once. Full prefix-chain acceptance is withheld.

## one next mathematical action and independent reviewer

At A064's first controller reveal after nonconstant core exposure, compute the exact Bellman update using the inherited complete core reserves and the actual two physical child continuations. Test whether the unused character-type debit pays that one update; retain all child reserves if it fails. This moves from fixed padding to the live interleaving gap. A087/A094 should reconstruct the contraction error, fixed-core quantifiers and one-character account; A064/A038 can consume the explicit retained-reserve transfer. Independent review of prior scoped reserve versions remains pending.

## actual persistence receipts or precise save blocker

All four protocol files, DERIVATION.md, REVIEW_NOTE.md, frozen specification, executable scripts and exact outputs are saved in this stage directory. STATUS.md, WORKLOG.md and LEARNED.md are updated locally. out/RECEIPTS.json checks hashes, file sizes, schema fields and required report headings. Supervisor adoption, independent acceptance and remote mirrors are pending; no remote persistence is asserted.

**Universal bridge:** This stage moves C019 stopping-tree payment from a quadratic edit class to a quantitative arbitrary-core reserve transfer: point-edit padding preserves the complete reserve within O(q^2 2^-q), and a following character query leaves exactly [Q_C(g)-C]_+ in the fixed-core limit. The terminal account is now identified rather than deleted, with an exact positive-residual fixture and an independent A064 boundary review. Universal payment of inherited core reserves remains open. NEXT attacks the first actual controller reveal during unfinished core exposure with these same reserves, which addresses the outstanding physical ownership step rather than another isolated class census.
