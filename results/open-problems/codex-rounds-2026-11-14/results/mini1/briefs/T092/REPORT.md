VERDICT: PARTIAL located an exact claimed external solution; validity not independently verified

An OpenAI preprint dated September 23, 2026 claims the exact finite-probability
conclusion of T092. Reference, repository identifier, theorem scope, and
proof-artifact links are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).
No arXiv id was located. The search therefore triggered the external-result
branch; no new special case or construction was attempted.

What was checked: the primary introductory TeX, citation README, final
diagonal argument, Lean scope note, comparator configuration, and named
top-level solution source were opened. The claimed orthonormal-basis
statement was independently checked to imply the precise Koopman model:
the assignment Uⁿf ↦ zⁿ extends to a unitary intertwiner by completeness
and orthonormality. This confirms scope, not the construction's validity.

Search commands were web-tool queries, including:

```
Banach problem simple Lebesgue spectrum probability preserving 2025 2026
"simple Lebesgue spectrum" "2024" "2025"
"2210.15480"
"A smooth three-torus diffeomorphism with simple Lebesgue spectrum" arxiv
"A smooth three-torus" error OR gap OR review OR counterexample
"ThreeTorus.lean" "simple_lebesgue_spectrum"
```

Local commands were read-only startup, directory, clock, and compute-state
checks. Files were written with apply_patch. Full chronology and useful
outputs are in [LOG.md](LOG.md). No numerical computation was needed.
The sandbox denied `nice -n 15` on the final tiny file checks; no substantive
compute or build was launched.

What failed or remains uncertain: the raw PDF was not parsed by the web
tool, so manuscript inspection used its TeX. No independent review was
established. The actual Lean solution source was located, but neither its
dependency closure nor its compilation was checked. A top-level proof body
and a scope note do not certify a result. T092 must not be marked settled
solely on this report.

Next worker: validate the named solution theorem and its definitions using
the comparator configuration, then audit the finite-stage construction in
the manuscript. Check resources before attempting a Lean build; it was not
shown to fit this session's 1 GB limit. If validation fails, retain the
claim notice and resume the special-case/reduction branch.

Task: “push this problem forward by one checkable piece” — received by this
worker 2026-11-14 21:58 +04 (Asia/Tbilisi).
