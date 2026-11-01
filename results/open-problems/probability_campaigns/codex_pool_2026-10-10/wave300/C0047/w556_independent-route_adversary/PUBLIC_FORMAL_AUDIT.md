# C0047 public comparator audit

2026-10-10. This is a source-level audit, not a Lean compilation or an axiom receipt.

The public docs/214.md scope describes the full nonuniqueness result. Its linked ComparatorChallenges/BenjaminiSchramm.lean contains admitted bodies for full_main, critical_laws, and cayley_main. The linked ComparatorChallenges/CayleyPercolation.lean likewise ends arbitrary_cayley with an admitted body. The exact proof token in all four is `sorry`.

Verdict: REJECT these four comparator declarations as a formal-check receipt. Their statements do not prove their conclusions. A kernel-checked receipt must identify the actual implemented theorem, its full assumptions, and its axiom dependencies, and exclude sorryAx or equivalent placeholders. No Lean execution or trusted-axiom output has been obtained here.

Boundary: comparator challenges can intentionally be statement-only benchmarks. This observation does not refute the mathematical preprint or show that a separate implementation is absent. Current openness remains UNKNOWN until the full mathematical argument or an actual proof implementation is verified. Do not convert the docs scope or comparator hashes into solved/retired status.

Sources checked through public browsing:

- https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/BenjaminiSchramm.lean ; theorem blocks full_main, critical_laws, cayley_main.
- https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CayleyPercolation.lean ; theorem arbitrary_cayley.
- https://github.com/openai/math/blob/main/lean/docs/214.md ; Scope and comparator links.

NEXT: Save immutable source hashes; inspect the mathematical paper's critical operator estimate, and request the actual implemented theorem/axiom receipt if a formal proof is claimed.
