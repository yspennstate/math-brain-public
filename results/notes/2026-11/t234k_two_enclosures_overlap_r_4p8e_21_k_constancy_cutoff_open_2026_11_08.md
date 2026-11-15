---
name: t234k_two_enclosures_overlap_r_4p8e_21_k_constancy_cutoff_open_2026_11_08
description: "Is T234's outgoing excess constant, with a uniform alpha cutoff (T234k)? Not proved: two certified enclosures (r 4.8e-21) overlap; cutoff needs a relative passage bound"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:53:40+04:00
  status: verified
  evidence: "OPEN-T234k REPORT.md, phase_00/04_CERTIFICATE.json; t234k_check.py rerun; push 8d5fb5b369"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

Is the outgoing phase family's excess exactly constant, and is there a certified cutoff uniform in alpha (T234k)? Not proved on either count. Two rigorous enclosures now overlap. Fixed-point GD at 224 bits, run for 85000 updates, gives endpoint trace-excess enclosures for the phases near 1/16 and 9/16. Their radii are 4.815e-21 and 4.797e-21 and their centres are 1.0759e-28 apart. Both contain 0.349363264011796152953604842476. They are conditional on T234h's validated.py arithmetic model, and the proof is author-audited.

The cutoff needs a relative scaled origin-and-nonlinear-passage error bound, uniform in p = -log10(alpha) >= p0. An absolute origin ball cannot supply it: at p = 2150 the ball exceeds the transverse norm bound by more than 2e169.

My check (t234k_check.py, run on a copy with sibling folders linked):
- reproduce.py gave an identical REPRODUCTION.json, with exponent 0.002791375 against a spectral 0.002791290.
- The planted +1e-12 at 9/16 was caught (1 flag), with 0 flags on the clean control.
- The overlap was recomputed in 80-digit Decimal.
- The 85000-step certification itself was not rerun.

Next: a triangular interval model of z and the relative W in U = [z, exp(s) W]. Exact constancy needs an invariant or an embedding theorem; more phase samples cannot decide it.

The two 54 MB path files are not on GitHub; REPRODUCE.md regenerates them. Folder: frontier T234 open_t234k_agent_11_08, push 8d5fb5b369. Card claim_821cbbbb13f84762b54b551ac97fc171.

Related: [[t234j_capture_rate_alpha_0p0028_starts_near_1e_2125_k_constancy_open_2026_11_08]] - T234j's double-double phase agreement is what these enclosures make rigorous for two phases; [[t234i_full_width_capture_asymptotic_only_regime_below_float64_2026_11_08]] - the asymptotic capture claim this family comes from.
