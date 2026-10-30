# Scope clarification for the adaptive-tree Poincare telescope

This addendum preserves the immutable `REPORT.md` and clarifies one terminal-word ambiguity.

If `affine leaf` is used in the narrow gate-ledger sense `P=0` (constant/literal), then the report's displayed identity

`P(root) = E sum_r Q_r`

is exact.

If instead `affine` is read in the F_2 sense of an arbitrary parity character, a higher-degree character can have `P(leaf)>0`. The exact statement is then

`E sum_r Q_r = P(root) - E P(leaf) <= P(root)`.

Every parity character still has spectral entropy zero, so

`H(root) = E sum_r (B_r + JS_r)`

remains exact. Consequently the main theorem and all universal-facing conclusions are unchanged:

`E sum_r JS_r <= 16 E sum_r Q_r <= 16 P(root)`,

and for balanced roots

`H(root) <= E sum_r B_r + 4(I(root)-1)`.

Thus the sandwich `K_tree <= C_FEI <= K_tree+4` remains valid whether policies terminate at constants/literals or at arbitrary character leaves. No scientific claim is weakened; this file only removes the possible ambiguity in the word `affine`.
