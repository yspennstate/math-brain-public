Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Erratum / clarification to the finite-state Markov escape-resolvent artifact

Target: `C0130`.  
Corrected artifact: `research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T144900Z__C0130_finite_state_markov_potential_resolvent.md` @ creation commit `46535d3f4d3768fd8b34f7cb1a5a8619ef7941b0`.

The mathematical conclusions and formulas (3.1)--(8.14) are unchanged, but **Lemma 2.1 needs one domain qualification**.

The full true forward kernel and the auxiliary kernel also differ on population-zero rows: the true forward process has population `0` absorbing, whereas the algebraic auxiliary row at population `0` has pgf `B_s(z)`. Therefore the literal full-space sentence

> `R=Q-K has nonzero rows only in B`

is too strong.

The correct statement is:

> On the **positive-population killed state space** `E_+ = S x {1,2,...}`, before entrance into the zero set `Z=S x {0}`, the difference between the true killed kernel and the auxiliary killed kernel is supported only on
> \[
> B=\{(s,k):1\le k<M\}.
> \]
> In row `(s,k) in B`, the population-coordinate discrepancy is supported only at `0<=j<=M-k` (with the `j=0` part interpreted as killing at `Z`). On the full state space there are, in addition, discrepancy rows on `Z` itself.

This is exactly the form used later in the first-defect/Dirichlet argument: Section 8 treats

\[
Z=\{(s,0):s\in S\}
\]

as a separate boundary set and never uses equality of the true and auxiliary kernels after hitting `Z`. In Lemma 8.1, the two paths are asserted to coincide only **before first entrance into `A=B union Z`**, where the corrected killed-kernel statement is sufficient.

Consequently:

1. the transfer formula for the auxiliary kernel is unchanged;
2. the `n^{-bar(delta)}` potential estimate is unchanged;
3. the Green first-entrance identity on `A=B union Z` is unchanged;
4. the finite system `(I-M)s_B=a` and the exact escape formula (8.14) are unchanged.

This immutable clarification is added instead of modifying the prior artifact.