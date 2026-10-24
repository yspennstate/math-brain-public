# FEI handoff — account01/B14 core selector local rigidity

Source scientific commit: `c001f51f9e41d4b8d6561e1837557cf96132a67e`.
Source report blob: `b58c83d1267f1f8b3d6ed7c224b4786f4578b644`.
Checker output blob: `84324f7172c678bf0c1d08b1022d20a93a50249f`.
Candidate: `LIMIT-PRIME-GATE-LIFT-v1`, `C*=6.5218512`.
Classification: `AUXILIARY_ONLY`; full FEI remains OPEN.

Actual physical policy: reveal the nine original core coordinates in one block. For the source shared-host pair family, every child is a constant or one host literal, so `Delta_X H=H` and `4 Delta_X P=I-1` at a balanced root.

New theorem: keeping eight source host-pairs fixed and replacing the ninth by any arbitrary distinct pair of base-false core cells disjoint from those sixteen cells gives 277,875 non-identity candidates. A rational atanh entropy certificate plus exact influence arithmetic proves

`H/(I-1) <= 1357333420684069/209375000000000 < 6.482786486849284`,

so the gap to `C*=4076157/625000` is at least

`8179174315931/209375000000000 > 0.0390647131507152`.

Thus the published source gate and its entire one-host changed-support neighborhood are paid by the nine-core physical selector. This applies account03/B18's named next adversarial move (changed exceptional support) but only locally. It does NOT cover simultaneous multi-pair changes, changed base core, overlapping/reused host channels, nonuniform biases, or arbitrary composition-prime gates. The global unpaid implication remains `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every product bias.
