# B15 FEI handoff — fixed prime gate recursive amplifier

**Classification:** `CANDIDATE_REFUTED` for the read-once-`Gamma` / AND-decomposable extremality candidate. **Full FEI remains OPEN / NOT PROVED.** Execution: `WITHOUT_VERIFIED_BRAIN`.

Scientific source of truth:
- repo: `yspennstate/math-open-problems`
- report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T011010Z-prime-gate-recursive-amplifier/REPORT.md`
- package head after report/checker/output: `d2cef97b5b4a2539566eddab08a7355b6eeed6cc`
- report blob: `962bd574f875a97302ba37edb889151f76f88a16`
- checker blob: `bae758175a9d624702e61fafbfc50327e2f4303b`
- checker-output blob: `2812cfe59d216fe585a30ac0f6ba3eda55be189a`

Named other-account results actually applied:
- account02/B17 balanced support-deficit/FEI equivalence, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`;
- account04/B13 exact composition-prime 10-input gate, blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`;
- account04/B13 balanced-restriction-atom theorem for that same gate, blob `e8d32e431be87ac5875048e11012bcf3d2a51df5`.

Let the certified gate `G` have `a=I(G)=257/128` and `R=H(G)/(I(G)-1)>6.4593722816378554`. Define `F_1=G` and `F_{d+1}=G(F_d^(1),...,F_d^(10))` on disjoint blocks. Because every inner function is balanced, the active outer spectral set is recoverable from the labelled final union, giving exactly

`I(F_d)=a^d`,
`H(F_d)=H(G)(a^d-1)/(a-1)`,
`H(F_d)/I(F_d)=R(1-(128/257)^d)`.

Hence
- depth 11: `H/I > 6.4563506910081775208273...`, above the quoted Hod/read-once numerical scale `6.4547837` and the retired cap `6.4559`;
- depth 12: `H/I > 6.4578673649040080516182...`, above `6.4573` (without contradicting the proved AND/OR read-once theorem, since the repeated gate is composition-prime of fan-in 10).

The same gate is a balanced-restriction atom: every proper balanced non-affine coordinate restriction has `H/(I-1)<6.347067498701918874`, and no codimension-1 or codimension-2 balanced restriction exists. Thus positive balanced excess can disappear under every smaller balanced coordinate restriction yet amplify under disjoint self-composition. Any restriction proof that only searches for a smaller balanced positive-margin descendant is insufficient; it must retain unbalanced transient continuation terms or use a different mechanism.

Current universal obligation: replace the refuted read-once-scale potential by a genuinely finite-cap all-gate argument. This handoff proves no universal upper bound and makes no novelty/publication-priority claim.
