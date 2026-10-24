STATE: DONE
NEXT: In a future attempt, improve the random-background truncation comparison from the proved n^(1-r) bound to o_P(n^(1/3)), and establish fixed-temperature KPZ/Airy universality for the capped model.
VERDICT: PARTIAL

2026-10-12: First attempt verified the source, searched later literature, proved isolated-spike/truncation reductions, and concluded PARTIAL. OpenAlex was rate-limited; no checked literature closure was identified.
2026-10-12: Reopened at the user's request. Read ATTEMPT.md and queried the brain for the confinement/Lindeberg gap and Berger-Torri entropy-controlled chains. Wrote two new approaches in SECOND_ATTEMPT.md and pursued the chain approach.
2026-10-12: Proved the lattice chain-count estimate, entropy coarsening, and a many-spike rare-reward theorem with quenched total-variation convergence to the bare walk. Proved its slowly growing-temperature version.
2026-10-12: Holder and finite path relative entropy yielded an unconditional original-polymer cap error bound (n log 2+exp(-n^(1/3)/4))/(1+n^r), for any 0<r<(alpha-5)/(3 alpha) with a suitable cutoff below n^(1/3). This is sublinear but much larger than the KPZ scale.
2026-10-12: Refuted deterministic transfer shortcuts and constructed an admissible infinite-third-moment law. Exact finite checks passed; additional Lean algebra passed. Sparse experiments used bounded memory and remained numerical evidence only.
2026-10-12: Additional attempt concluded PARTIAL, with all proofs and remaining gaps written in SECOND_ATTEMPT.md and audited in SECOND_REFEREE.md. No full KPZ/Airy theorem or iid counterexample to F0021 was obtained.
