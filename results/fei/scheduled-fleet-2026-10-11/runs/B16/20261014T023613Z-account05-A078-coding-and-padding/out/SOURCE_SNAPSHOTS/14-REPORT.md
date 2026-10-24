# A027 stage 4: interleaved point-control projection

Full FEI remains OPEN. The existing partial-core transport candidate is extended to arbitrary physical interleaving of POINT controls and core coordinates; actual terminal entropy and one influence account are retained.

## exact target, quantifiers, hypotheses and units

For every uniform Boolean core u and r>=1 fresh disjoint point controls, F=1+A_r(u-1), p=2^-r, take any finite actual adaptive restriction tree T, and prune constant continuations after control failure. Conditioning original INPUTS on all controls passing and deleting deterministic control queries gives one actual core tree U. Active leaf weights are v_l=w_l*p_l/p, including remaining-control probabilities.

Let Q_core, Q_control denote ACTUAL queried influence by coordinate type, and Q_core_live the core part queried before the controls are exhausted. Then Q_core=p Pi_I(u;U), and E=Pi_H(F;T)-p Pi_H(u;U) obeys -kappa Q_core_live<=E<=kappa Q_core_live+C0 Q_control, kappa=4+12/ln2<22, C0=2+2/ln2+1/(sqrt(e)ln2)<6. All entropy is in bits. If U is proper, paid at K>=0, and actual activated terminals are certified at L>=0, the complete root bound is max(K+kappa,C0,L)I(F). This is a conditional selection transport theorem, not universal existence of U.

## sources actually read, revisions and theorem locators

Read BOARD snapshot2026-10-14 01:41UTC, B06 STREAM_NOTES v2, own STATUS, and the complete execution protocol. Own previous DERIVATION and scoped A028 reconstruction supply the quantitative interfaces. A028 stage3 REPORT was read to preserve its controller-first/priority ownership. A038 stage3 REPORT and PROOF already establish interleaved POSITIVE-CAP reserve; this stage instead treats the FULL signed entropy path cost and projected inner-core partition. SOURCE_READS records source hashes and exact scope.

The board's A048 descendant-reference injection objection is respected: this projection conditions a single physical INPUT event and does not assert a root-compatible spectral witness channel. No new external paper theorem or literature-priority assertion is made; earlier mandatory reads retain their recorded scope.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete all-dimensional proof. At active histories w_v*p_v/p is exactly conditional reach probability under the original point event. Projected entropy/influence costs therefore correspond to one actual core tree. The activation correction is retained ONCE as G_r(d_root)-E_active G_(r_leaf)(d_leaf), with G_0=0. Its core-node contribution is bounded by kappa Q_core_live using the locally proved version2 interface. A control node is a dictator activation of its ACTUAL passing child, so A028's reconstructed C0 correction pays that node by its own queried influence. The separate sums yield the two-sided transport without a rarity reset.

The exact physical partition is I(F)=Q_core+Q_control+E_leaf I(F_leaf). Adding assumed actual terminal allowance and projected core allowance proves the maximum constant. Queries made after all controls pass have zero activation surcharge. Control failure leaves are actual constants; they are not discarded from the leaf partition.

WEIGHT_WITNESS.md records an exact coreD2/r2 prefix where active weights1/2,1/4 must become projected weights1/2,1/2. Normalizing raw active weights predicts bias5/6 instead of actual3/4. The physical influence partition is1=1/8+1/8+3/4, and terminal entropy3/2 remains. This is an ownership/wrong-weight witness, not a disproof of FEI.

First unsupported universal line: choose a proper projected core partition with a dimension-independent payment K and uniformly certified ACTUAL terminal allowance L for every Boolean core, without assuming core FEI or treating terminals as free. Interleaving alone does not establish that line. Arbitrary-controller interleaving and shared physical support are not claimed.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before search. Domain: all16 two-bit and256 three-bit core truth tables, r1,2; six labeled orders (including coincidences) at every prefix depth, plus12 adaptive three-step policies per three-bit core/r. The helper stops inactive branches and before the final core coordinate. There are14,496 ordered policies and6,144 adaptive policies, total20,640. Maximum physical dimension5; no symmetry quotient or automatic escalation.

Commands: `python -X utf8 runs/20261014T015108Z-account05-A027-block-selection/code/setup.py`, then code/check.py with `--pilot`, then without it. The setup copies ONLY pinned exact helpers from own prior run; no old search executes. Original pilot passed 16,256 assertions on672 cases in0.285s. Refined pilot passed 5,360 assertions over the same672 labeled policies/192 distinct actual trees in0.108s. Full final passed 337,648 assertions over20,640 labeled policies/9,408 distinct actual trees in131.031s. Identical complete physical tree shapes with the SAME core truth table and control width reuse an exact successful certificate; all labeled policies remain counted and each reuse is checked. This is duplicate certificate reuse, not a symmetry quotient. Exact integer Walsh/prime-log vectors verify signed entropy identities and endpoint potentials; physical edge counts and actual restricted truth tables verify projection, full core/control/terminal ownership, and exhausted-controller endpoints. Rigorous rational24-term atanh intervals with explicit tail verify rational rates22 and6; the sharper constants follow from the written analytic proof. code/weight_witness.py independently checks the fixed ownership witness and exports exact out/WEIGHT_WITNESS.json.

The first full command reached its originally frozen60-second runtime cap, with no mathematical assertion failure. VALIDATION_AMENDMENT was saved BEFORE retry at240 seconds. That retry reached its cap after14,739 completed policies; out/timeout_checkpoint preserves exact counts. VALIDATION_REFINEMENT was then frozen BEFORE the final run, reusing identical complete actual-tree certificates and setting a600-second full ceiling. out/RUNTIME_FAILURE.md preserves both failures. Pilot remains60seconds, domain/arithmetic/dimensions unchanged. No partial count from the first helper is invented. Original memory estimate160MB/refined180MB, peak unmeasured; no >300MB job, GPU, background service or dimension escalation. All subprocesses are awaited to completion before stage finalization.

## proof dependencies and changed downstream conclusions

Version3 extends the SAME candidate, retaining old components and exact surcharge-four obstruction. No new broad candidate is opened at the stream review cap. Its new quantitative premises are A027 version2 local core correction, A028 version2 one-bit scalar correction (previously independently reconstructed at scope), and the recovered physical-tree conservation. The projection itself is proved here directly.

A038's positive-cap theorem is recognized but not used as a full entropy payment. A028 retains its selector-first and priority ownership. A029/A030/A064/A082 may now apply a signed inner-core/tree allowance through one interleaved point wrapper with all actual leaves present. They must not substitute a nominal controller budget or a descendant spectral channel, and cannot reset the endpoint correction after every query. No universal FEI constant changes.

## one next mathematical action and independent reviewer

Use the exact projected terminal-slack ledger at the first core split of a rare biased activation to derive a necessary/sufficient admission criterion from actual certified child slacks, preserving the remaining control reserve. Seek an eligible proper core split rather than another transport or isolated controller class; A029 supplies the signed-terminal interface. A087 is the independent reviewer of the projection and complete ledger; A094 challenges leaf conditioning and terminal admission. These are saved handoffs, not external messages or observed review acceptance.

## actual persistence receipts or precise save blocker

All four protocol files, proof checkpoint, weight witness, frozen/amended specs, pinned helpers, exact pilot/full outputs and runtime failure record are saved within A027. STATUS is two lines and WORKLOG/LEARNED updated. out/PERSISTENCE_RECEIPT checks exact protocol schemas, claim hashes, required report fields, byte-identical compatibility files, file sizes and artifact hashes. No mirror, supervisor-copy or independent acceptance receipt is claimed.

## Universal bridge

This stage moves C019 and its C024 physical-history interface by proving all-order point-control transport through one ACTUAL projected core partition, with signed correction bounded by kappa Q_core_live+C0 Q_control and exact retained terminal entropy. It removes the ordering restriction from the point-wrapper transport and identifies the necessary remaining-control weight factor; it does not supply universal paid core selection. What remains is a proper eligible core partition with actual child/terminal certificates. NEXT prices admission at the first rare-biased core split using one remaining-control reserve and certified signed child slack. That targets the unsolved selection step directly, whereas another disjoint activation transport or controller-class theorem would leave the same universal obligation unpaid.
