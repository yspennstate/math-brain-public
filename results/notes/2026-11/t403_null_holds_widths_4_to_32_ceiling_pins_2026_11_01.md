---
name: t403_null_holds_widths_4_to_32_ceiling_pins_2026_11_01
description: [VERIFIED] T403 widths 4-32: late compression leaves test error in place (mean -0.0003 to -0.0015); from width 16 I(X;T) pinned at log 64, nothing to compress
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T11:51:25+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed f5f434c, card claim_8d3b5695431640f1bbe50bb2695dc178 export bc516ca, move 9065ac6a. Extends [[t403_64_seeds_compression_no_test_gain_2026_11_01]].

- 32 seeds per width.
- rho(dI, d test err) was +0.37 at width 16: over the single-test threshold of 0.35, but not over the Bonferroni threshold of about 0.44 for four widths.
- I also stated its sign backwards once to the author and corrected it. Positive rho here means more compression went with more improvement.

**Why:** this removes the one-width limit of the T403 null.

**How to apply:** with n = 64 sample points and sigma 0.3, information-plane compression is visible only at widths up to about 8. At larger widths I(X;T) is capped by log n. Check the ceiling before reading anything into a flat I(X;T).

Folder: research-repo research_pushes/2026-11-01-loop-T403-widths
