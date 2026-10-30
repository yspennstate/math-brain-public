# Correction to Theorem 3.1 wording

The phrase **"exactly one of the following occurs"** in `REPORT.md`, Theorem 3.1, is stronger than the proof establishes and should be read as **"at least one of the following occurs"**.

The proof establishes the implication actually used by the campaign:

- if an internal saturated-chain vertex lies strictly between `b` and `a` in the strong-majority order, then there is a strictly shorter extreme incomparable pair;
- **if no such span descent occurs**, then there is a saturated-chain cover edge `l lessdot u` with
  `l prec_* b prec_* a prec_* u` and
  `Pr(l<b<u)>1/3`, `Pr(l<a<u)>1/3` under the original uniform full-extension law.

The alternatives need not be mutually exclusive, and no exclusivity is used anywhere in the deduction, verifier, handoff, or stated remaining obligation. The `ESSENTIAL_STEP_APPLIED` outcome and the common-cover conclusion in the no-span-descent branch are unchanged.
