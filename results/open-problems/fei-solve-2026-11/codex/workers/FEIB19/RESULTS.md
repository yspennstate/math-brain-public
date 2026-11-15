# Results as they arrive

No conclusion about universal FWC yet. The section 12(b) definition and martingale representation agree algebraically. The identity in 12(g) is an identity for exact erasure entropy; it does not by itself prove that optimizing orders can be restricted to block orders.

Sources read: ~/fei_solve_agent/FLOW.md; ../FEIB16/FORMULAS.md and WITNESSES.md; ../FEIB17/REPORT.md. Numerical results will be attached to executable receipts.

PROVED: compositions admit an optimal order respecting all blocks, with the target block last. The exact recurrence and proof are in PROOFS.md. Its independent full-table check covers 400 live coordinates in composition.json; the maximum cost residual is 2.220446049250313e-16 bits.

PROVED: L*=E at every coordinate of a read-once AND/OR formula. Together with the cited read-once entropy theorem this proves FWC with coefficient 10 on that restriction-closed class. The same equality also survives disjoint XOR nodes, so the statement extends to AND/OR/XOR/NOT read-once formulas.

FALSE: the actual input-adaptive martingale energies grouped by depth need not bound erasure. Truth table b6a4, n=4, i=1 has E_i=1 bit but adaptive cost 0.7743974703476992 bits. The policy and rational energy bins are in audit.json.

CHECKED: cyclic DNF OR_j (x_j AND x_{j+1} AND x_{j+4}) on 16 cyclic coordinates has optimized witness/influence 4.070340466904954 and erasure/influence 3.0345823208206126. Transitivity makes one coordinate sufficient. families.json gives the truth table, all terms and a minimizing order. This is a finite record in this scan, not an unbounded family.

CHECKED: the Fano-plane DNF on seven variables has exact erasure zero but optimized filtration/influence 2.321323484155634. Its two-copy OR on fourteen variables inherits that normalized gap exactly. Sources: structured.json and families.json; inheritance is proved in PROOFS.md.

Final results: the optimized PM tower minimum is approximately 4.86317608849 bits per unit influence; pm.json gives the depth-20 value and a remaining analytic tail of 1.112823041741625e-11. The independent native implementation agrees, and its chosen path is evaluated from exact dyadic masses at 90 decimal digits in native_audit.json.

The recursive Fano tower strengthens the gap example to approximately 4.601671597979309, with exact erasure zero. final_checks.json evaluates the recurrence at 90 decimal digits through depth 40 and bounds the remaining analytic tail by 1.9338352573568567e-20. These numerical enclosures are not directed-rounding certificates.

PROVED: every composition admits an optimal block order; read-once AND/OR/XOR/NOT formulas have FWC coefficient 10; degree-d functions have coefficient d-1+log2(e); sensitivity-s functions have coefficient 2s-2+log2(e); linear thresholds have coefficient 20.95691937544493 at a largest-weight coordinate in every reveal order. PROOFS.md supplies the arguments and dependencies. All four-variable Boolean tables pass the core inequalities in final_checks.json. General FWC and the class extensions identified in REPORT.md remain open.
