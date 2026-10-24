# A093 B19: restriction priority and a GMP constant correction

## exact target, quantifiers, hypotheses and units

For every Boolean f:{-1,1}^n->{-1,1} under uniform measure, H is Shannon entropy of squared Walsh coefficients in bits, and I_i=sum_{S containing i} fhat(S)^2. Audit the prior occurrence of H(f)<=2|A|+E H(f restricted on A) and the arbitrary-child one-coordinate decrement identity; compare the local all-LTF Theorem A with corrected primary literature. A093 follows the B19 lead's named target. Full FEI remains OPEN; this stage establishes no priority superlative.

## sources actually read, revisions and theorem locators

See PRIMARY_SOURCE_OVERLAP.md for the nine named primary papers, URLs, exact statements, and locators. The core positive overlap is CKLS ECCC revision 2, Lemma 3.2 (PDF p. 9), and GMP26 v2, Appendix (32) (PDF p. 28). GMP stopping-tree Ansatz 1.2 is on pp. 16–17. The v1 appendix was also read to check whether v2 repaired the constant issue; it did not. PDF page 16 was rendered and visually inspected, confirming that the false binary-entropy inequality is printed, rather than a text-extraction error. Primary ECCC correction and Han/GMP arXiv version pages were checked. BOARD.md (supervisor stamp 2026-10-13 23:49 UTC), B19 STREAM_NOTES.md v2, own STATUS.md, and execution protocol revision 2026-10-11-execution-v2 were consumed. No external trees were modified. No artifacts survived from the interrupted 20261012 stage; earlier completed B09 work was not repeated.

## complete derivation or exact first unsupported line

Write a_T=fhat_plus(T), b_T=fhat_minus(T), q_T=(a_T^2+b_T^2)/2, and h=h2. The parent coefficients are (a_T+b_T)/2 and (a_T-b_T)/2. For q_T>0 set u_T=(a_T-b_T)^2/[2(a_T^2+b_T^2)] and t_T=a_T^2/(a_T^2+b_T^2). Direct entropy grouping gives

Delta_i H = sum_T q_T [h(u_T)+1-h(t_T)] = E_i+R_i,

where E_i=sum q_T h(u_T) is GMP's (22) quantity, and R_i=sum q_T[1-h(t_T)] >=0. Zero fibers contribute zero. This is its Appendix (32); it translates to C005/C006. Since sum q_T=1, both E_i and R_i are <=1, proving 0<=Delta_i H<=2. Applying this at each of |A| coordinates and averaging over earlier uniform restrictions yields the block +2|A| inequality. CKLS already states the singleton bound explicitly; the block extension is its elementary iteration.

The exact witness for the same-K replacement in GMP Corollary 4.2 is f(x,y)=-1 except f(1,1)=1. Its four coefficients are (-1/2,1/2,1/2,1/2), so H(f)=2. Split x: f_plus=y and f_minus=-1 both have entropy 0, and I_x=1/2. The two occupied child fibers have coefficient pairs (0,-1) and (1,0), hence E_x=1, R_x=1 and Delta_x=2. At K=2, (22) holds, while (21) fails. This is an actual Boolean witness to a source's same-constant substitution, not a counterexample to FEI: total influence is 1 and H/I=2.

A safe general repair is E_i<=K I_i implies Delta_i H<=(K+4)I_i. Here is a self-contained bound on the refund. For t=(1+e)/2, |e|<=1, the entropy series is

1-h(t) = (1/ln 2) sum_{k>=1} e^{2k}/[2k(2k-1)] <= e^2,

because all terms are nonnegative and their coefficients sum to ln 2, as follows at e=1 by continuity/monotone convergence. Therefore q(1-h(a^2/(a^2+b^2))) <= (a^2-b^2)^2/[2(a^2+b^2)] <= (a-b)^2. Summing gives R_i<=sum(a-b)^2=4I_i. Conversely Delta_i<=K I_i implies E_i<=K I_i. Existence of a dimension-independent bound is therefore equivalent after allowing a constant loss; exact same-K substitution is not.

The appendix's first unsupported implication is its assertion after (32) that a bounded discarded term gives an if-and-only-if with the asserted constants. It changes from individual influence to sum(a-b)^2 without preserving the factor 1/4. If E_i<=K' sum(a-b)^2 then this derivation gives Delta_i<=4(K'+1)I_i, not the printed K=K'+1 in the influence normalization. A separate printed error is equation (20): h(t)<=sqrt(t(1-t)) fails at t=1/2, where the sides are exactly 1 and 1/2. Consequently arguments using that displayed bound or Corollary 4.3 require their own constant reconstruction. This stage does not refute all claimed restricted-class theorems. The telescope using the true decrement in Ansatz 1.2 remains valid.

The all-LTF comparison is limited to read statements: CKLS corrected H=O(sqrt n), CKKLS random-weight and small-weight regular subclasses, Han's influence-entropy sum bound, Potapov's flat-spectrum classes, Chang's biased lower bound, and Fang–Wang's low-degree Fourier weight. None of these read statements asserts the local Theorem A. Their absence from this table does not certify global priority or best constants. Historical Han overlap acknowledgment and CKLS correction matter for citations; the old uncorrected all-LTF statement is not a valid established comparator.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the check. Ran `python -X utf8 code/check_witness.py`, one n=2 Boolean truth table, no symmetry reduction, Fraction arithmetic, logarithms only at powers of two. All 25 exact assertions PASS; out/EXACT_WITNESS.json records all coefficients, influences, entropies and the code hash. The final run took under 0.01 seconds inside Python; estimated memory 30 MB. No heavy search or >300 MB computation was started. Primary PDF downloads/text extraction ran via code/fetch_sources.py; two additional PDFs were fetched with commands recorded in out/ADDITIONAL_RECEIPTS.json. The page image was rendered using fitz for source verification; no image editing was performed.

## proof dependencies and changed downstream conclusions

The witness and repair depend only on Walsh linearity, Parseval, binary entropy algebra and its positive series. They use no unaccepted campaign theorem. Literature locators are primary-source evidence, not independent theorem proof acceptance. Claim A093-GMP26-CONSTANT-CORRECTION v1 is source-complete pending independent review. C005/C006 are comparison targets, not modified shared claims. Consumers A041/A069/A095/A099/A100 should retain the refund in any C019 stopping tree and avoid importing GMP's constant-preserving replacement. A090/A085 review should reproduce the truth table and source normalization. No shared index or downstream consumption was written or verified.

## one next mathematical action and independent reviewer

Reconstruct GMP's stopping-tree bound with the full E_i+R_i debit and retained terminal entropy, then compare its corrected budget to the campaign's signed C019 payment. A090 is the requested independent reviewer, A085 alternate; B19 lead and A095 are the immediate mathematical consumers. This is a source-bound handoff through artifacts, not a message sent to others. Further class proofs should not be adopted until every use of (20), (22), and (23) has its constants rebuilt.

## actual persistence receipts or precise save blocker

The four protocol files, overlap table, citation status, exact certificate, frozen spec, code, primary PDFs/text and source receipts are saved in this run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only in A093. out/ARTIFACT_RECEIPTS.json pins generated files and source bytes; validation verifies schemas, claim hashes, packet compatibility and file size <20 MB. Local persistence is complete. GitHub copying, brain ingestion, independent acceptance and downstream mathematical use are not claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment by locating its prior telescope and removing a constant-preserving substitution that fails on an exact two-bit Boolean example. The repaired uniform implication costs at most an additional 4I_i per node; no finite universal bound on E_i has been established here. The remaining universal obligation is to pay the true decrement with a single influence budget while retaining all terminal entropy. Reconstructing that source-normalized ledger is the shortest next route because it tests the existing universal bridge directly and prevents an unpaid refund from masquerading as full FEI progress.
