# Frozen validation specification
Helper: ledger_check.py v1, deterministic stdlib only.
Family/domain: all 256 Boolean truth tables on n=3; fixed adaptive tree reveals coordinate 0, then coordinate 1 if first physical bit is 0, otherwise coordinate 2, stopping after two reveals. All 4 leaves retained. Also all 16 n=2 Boolean functions, and 81 rational joint laws with 4 witness values and 2 child outcomes (weights 1,2,3 in four entries, remaining entries fixed), common and mismatched channels, one explicit reference reset, and one side-conditioned XOR law.
Case count: 256 physical lifts + 16 sign controls + 81 rational chain cases + 2 exact endpoint examples; no symmetry reduction.
Arithmetic: fractions.Fraction probabilities; logarithmic identities represented as formal sums of rational coefficients times log2(rational), checked exactly by prime factorization. Thus no numerical sign is used as proof. Nonnegativity follows analytically from Gibbs.
Memory estimate: <50 MB. Pilot and entire run limit 60 s. No automatic escalation, no GPU, no subprocess, no random seed.
