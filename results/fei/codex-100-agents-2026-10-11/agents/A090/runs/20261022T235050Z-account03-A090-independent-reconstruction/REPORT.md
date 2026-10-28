# A090 stage 7: reconstructing the paid reset and its exact limit

## exact target, quantifiers, hypotheses and units

**HOLDS at its stated scope:** A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER@1. Its general reset cap and specified one-frontier payment reconstruct directly from the theorem statement and the physical Fourier restriction identity. No producer derivation or checker is used. Full FEI remains **OPEN**.

There are two further conclusions. First, the same original quota pays any adaptive history on the specified nine-bit fixture with at most two 7/8-preserving reference resets per path, retaining all executed charges and full terminal cross-entropies. Second, replacing this controlled reset with an arbitrary independently prescribed full-support reference is false even for one positive-influence query with both children nonconstant and both squared spectra full-support and non-flat. The counterexample concerns reference costs, not Boolean H/I.

All functions are actual Boolean signs on finite uniform physical cubes. Entropy, cross-entropy C(P,R)=-sum P log2 R, divergence and all ideal costs are in bits. Influence is ordinary flip influence. P<<R means every occupied P atom has positive R mass. References are normalized; empty-set and reference-only mass remain. Trees are finite, may adapt to physical outcomes, query fresh coordinates, and retain both fair children. No unrelated old debit or integer-code rounding is included without its own accounting.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, is read in full. The current user extension controls the campaign endpoint. BOARD.md is the supervisor's 2026-10-22 23:50 UTC snapshot; B18 STREAM_NOTES.md remains v2 from 11 October. A090 STATUS.md and LEARNED.md preserve the stage-6 no-reset bridge. The productive saved reset gap takes dispatch priority over the old proposed five-variable census.

The source statement is A004/runs/20261022T220858Z-account03-A004-constant-and-unit-ledger/CLAIMS.json, claim A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER@1; its companion A001-NEUTRAL-CORE-ACTUAL-DATA-TRANSFER@2 gives the fixture. Statements from the latest A094, A096, A097 and the current A099 package were inspected to identify remaining canonical-reset obligations; those entire chains are not accepted by this report. In particular this audit does not reconstruct A094's h_w*h_2 canonical reference or A097's negative-cell floor.

Original physical restriction definitions are in the campaign supplement sources/ERASURE_REDUCTION.md, section 1. A090's previous stage, runs/20261021T175538Z-account03-A090-independent-reconstruction/REPORT.md, supplies its already independently reconstructed no-reset telescope and exact neutral root spectrum. The new proof below re-expands the reset identity and its quantifiers. SOURCE_RECEIPTS.json binds the exact local source bytes and marks inspection scope. A file hash is not a review of every theorem in that file. No producer DERIVATION.md or code is imported.

## complete derivation or exact first unsupported line

At a node, paired signed amplitudes u=a_T and v=a_(T+i) give actual child masses (u+v)^2 and (u-v)^2. Their fair average is p_T+p_(T+i). Let P_minus_i be that marginal, let r=R_minus_i, and write B_i=H(P)-H(P_minus_i). Finite CE ensures every conditional denominator needed below is positive. The full conditional occupancy divergence is

c_i = D(P||R)-D(P_minus_i||r)
    = sum_T (p_T+p_(T+i)) D(P(i in S | T)||R(i in S | T)) >= 0.

For zero true marginal mass the summand is zero; reference-only mass is retained in r. Nonnegativity follows from the ordinary finite KL inequality, not independence. Linearity of CE in the true law then gives

B_i + avg_s C(P_s,r) = C(P,R)-c_i.                                      (1)

If the node or child reference is replaced by Q, its exact signed extra cost is

e(P;r,Q)=C(P,Q)-C(P,r)=sum_(T:P(T)>0) P(T) log2(r(T)/Q(T)).                (2)

Summing (1) over a finite tree, with (2) booked once at every reset, proves

W + E C(P_leaf,R_leaf) = C(P_root,R_root) + sum_resets w e - sum_queries w c_i.  (3)

Here W is every actual executed erasure, including the entire old prefix within this account. Both complementary terminals keep their complete CE. Negative resets are credits; they are not silently replaced by positive charges. Nothing in (3) creates a new descendant bank.

If Q(T)>=alpha*r(T) on the true support, 0<alpha<=1, each logarithm in (2) is at most log2(1/alpha), so e<=log2(1/alpha). More sharply, for fixed normalized r,Q,

sup_(Boolean characters chi_T, r(T)>0) e
 = sup_(Boolean P<<r) e
 = log2 max_(T:r(T)>0) r(T)/Q(T),                                       (4)

with infinity if Q vanishes at a positive r atom. The upper bound is a weighted-average bound. Equality is attained by the actual character chi_T, whose squared spectrum is a point mass at the maximizing T. This verifies the quantifier in the source: r and Q are fixed while the Boolean test function varies. It does not claim that the particular fixture's law can be chosen to attain every worst-case atom. Consequently a uniform cap c over all these Boolean test laws is equivalent to Q>=2^-c r on the entire positive-r support. A cap just for the actual law may instead use its weighted signed cost.

For the neutral fixture put b(y)=+1 iff y&7=0 on six bits and F=b+1_origin(Maj3-1) on three fresh majority bits. Its exact incoming reference is P_F, and its original core quota is 3=4I0 with I0=3/4. The previously reconstructed root entropy is

H0=385/32-(2401/1024)log2(7)-(1575/2048)log2(15)
  =2.444203601658... .

For a reset Q=(7/8)r+(1/8)U, U uniform on all residual Fourier masks, the reference is normalized and full-support, and Q>=(7/8)r. Put c=log2(8/7). If every path encounters at most k reset nodes, then sum_resets w<=k. Equations (2)-(3) give

W + E C_terminal <= H0 + k c.                                         (5)

This holds for arbitrary finite adaptive choices and stopping, not only the tested query orders. It also allows any other reset satisfying the same 7/8 domination. Later no-reset continuation keeps (5). Reference-only mass, phases in actual restrictions, and all conditional normalizers remain present.

For k=1 the original margin is 3-H0-c>363150/10^6, reproducing A004. For k=2,

3-H0-2c>170505/10^6.                                                   (6)

The margin is smaller than the stage-6 no-reset margin because one or two explicit worst-case reset costs c are now subtracted from the same original bank; no numerical constant has changed silently. In the executed two-query policies both fair children are reset at each query frontier. The second reset is priced against its actual already-reset incoming reference, not against a newly supplied copy of the original one. The analytic proof covers unequal path depths and arbitrary later marginal-reference continuation.

The first unsupported extension is: **replace the prescribed smoothed Q in (5) by an independently prescribed canonical Q_can while retaining the cap c, without proving domination or paying the actual signed cost (2).** A004 expressly excludes this extension. The following exact witness shows why it cannot be inferred just from full support, non-flatness and Booleanity.

Let f=Maj5, positive when at most two of five 0/1 labels equal one. Its nonzero Fourier coefficients are 3/8 on singletons, -1/8 on triples and 3/8 on the five-set. Thus every coordinate influence is 3/8 and I(f)=15/8. Start with the exactly matching reference R=P_f, and physically query coordinate0. Fourier parity makes B_0=0; c_0=0 since the initial reference matches. Both actual children are nonconstant and have the same squared spectrum r on all sixteen residual masks: six atoms of mass 9/64 (including the empty set) and ten of mass 1/64. These spectra are normalized, full-support and non-flat. Their inherited reference is exactly r, so no previous reference debt is hidden.

Reset only one fair child to the reference fixed by

Q_m(empty)=2^-m; Q_m(T)=(1-2^-m)/15 for each of the other fifteen masks.

Every Q_m is normalized, full-support, non-flat, and specified before the spectral sample. Keep the complementary child's inherited r unchanged. Its full ledger is

L_m=(C(r,Q_m)+H(r))/2 >= 9m/128.                                       (7)

The lower bound is just the empty atom's positive cost; all other CE terms and the other terminal's entropy are nonnegative. For m=128, L_m>=9>15/2=4I(f). The exact certificate gives L_128=12.341429942817... . More generally L_m/I(f)>=3m/80, so no finite universal rate pays arbitrary prescribed reference resets even on this fixed five-bit function. This is not a Boolean counterfamily to FEI: the Boolean function, its actual entropy and its influence stay fixed; only an imposed reference changes. Nor does it refute an existence theorem for good canonical references. It rejects an unjustified arbitrary-reference substitution and retains the complementary full terminal.

No unsupported implication is found within A004's actual stated theorem. The unpaid canonical-reference substitution above is the precise universal gap. A001 v2 no longer uses the undefined shadow-reservation comparison flagged in the previous review; that old clause is not needed or accepted here.

## executed validation with domain, arithmetic, commands and outputs

Specification: out/FROZEN_SPEC.json, saved before execution. Command from A090: `python -X utf8 runs/20261022T235050Z-account03-A090-independent-reconstruction/code/check.py`. The successful bounded pilot takes approximately 9.5 seconds, uses a 60 MB memory estimate, and performs **5,731 exact assertions**. There is no symmetry reduction, automatic dimension increase, GPU work or heavy job.

The checker reconstructs the actual fixture and Maj5 truth tables, integer Walsh spectra and physical influences. For each of all 9*8=72 labeled ordered two-query policies, it keeps every outcome, both complete reset references at each frontier, actual erasures, signed reset costs, conditional KL refunds and full terminal CE. It checks exact cancellation in (3), domination and the common original-budget bound. It tests the five fixed witness values m=8,16,32,64,128; at every one of sixteen residual masks an actual character checks the sharp fixed-reference expression (4). Maj5's two nonconstant children, full support, non-flat mass histogram, actual influence, matching inherited law and untouched sibling terminal are asserted explicitly.

Rational probabilities use Fraction. Equalities are exact rational linear forms in logarithms of positive integer atoms (large Mersenne atoms need not be factored into primes). Sign certificates use the forty-term atanh expansion after normalization to [1,2], with explicit positive remainder <=2t^81/[81(1-t^2)]. Positive certified ln2 bounds justify division. Floating intervals printed in out/CHECK.json summarize rigorous rational calculations and do not determine acceptance. The lower bound L_128>=9>15/2 also has a direct rational proof independent of logarithm approximation.

The fresh memok.py gate exited 0, but lean_check.py's additional compute-admission check held because of a hung window or less than 5500 MB free. It returned SETUP_UNVERIFIED and launched no compiler. out/LEAN.txt preserves this receipt. The intended core target was only the numerical certificate 8^10<2^2*7^10 and 489+80<600 (a coarse two-reset budget bound), not the entropy theorem. Neither target nor full theorem is labeled Lean-checked. FINAL_VALIDATION.json records the precise rung. The formal admission hold does not invalidate or formally verify the independently executed rational certificate.

## proof dependencies and changed downstream conclusions

A004's full abstract reset theorem and its numeric one-frontier fixture payment are independently accepted at their stated scope, without a repair. The two-reset result (5)-(6) is A090's direct corollary and awaits another reviewer; it does not receive an independent acceptance from its own contributor. The controlled-reset mechanism is elementary accounting, not a new universal entropy estimate. The generic telescope and neutral spectrum were already reconstructed in A090 stage6; no new independent acceptance of A094/A096/A097 canonical constructions is inferred from reading their statements.

A004/A001/A096 may now consume a second controlled reset on the fixture without renewing the original bank. The signed reset at every later node must use the actually inherited already-reset reference. A094/A097/A099 must keep the missing distinction visible: full support and a non-flat child alone do not pay a canonical reset. The Maj5 witness is a falsifier for that possible strengthening, not a refutation of any source theorem that keeps its domination or source-price hypothesis.

## one next mathematical action and independent reviewer

Next: obtain the actual prescribed canonical floor after one dummy-data or off-branch exposure in the current A097/A099 chain. Compute (2) against the actual remaining inherited reference, with its old active/control reset debits, both full terminals and the unchanged ancestor envelope. Prove sufficient domination or pay its actual weighted excess from the measured KL refund and genuinely unused reserve. A004/A094 review the two-reset corollary and the Maj5 guard; A086/A096 review any subsequent canonical-floor application. Testing one real canonical floor targets the missing universal interface more directly than another smoothing exercise.

## actual persistence receipts or precise save blocker

The requested REPORT.md, CLAIMS.json, PROGRESS.json and identical compatibility PACKET_DELTA.json are saved in this run, with code/ and out/. The three rolling notes are updated inside A090. SOURCE_RECEIPTS.json, out/CHECK.json, out/FROZEN_SPEC.json, out/LEAN.txt, FINAL_VALIDATION.json and out/ARTIFACT_RECEIPTS.json preserve source versions, exact execution and local readback hashes. Protocol field sets and file size limits are checked. Supervisor/GitHub/brain adoption is unverified; no shared research source, another agent folder or brain store is mutated. The initial task-checklist update encountered its shared lock; the final lifecycle receipt records the later outcome.

**Universal bridge:** This stage moves C019 stopping-tree payment and C024 history transfer by independently reconstructing A004's paid reset interface and extending the specified fixture to two controlled resets per adaptive path from the same original quota, leaving more than 170505/10^6 bits with all terminal KL retained. It adds no universal FEI constant. The exact fixed-Maj5 obstruction shows that merely declaring the next reference full-support and non-flat cannot close the chain; its signed cost or domination must be proved. Pricing one independently prescribed canonical floor after a real mixed-history exposure is therefore the next unpaid universal interface, rather than another isolated Boolean class calculation.
