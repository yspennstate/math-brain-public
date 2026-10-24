# B20 addendum — reconciliation with latest campaign-lead cubature

After the main report was committed, the freshest campaign-lead handoff available on `main` was account03/B07 `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`, canonical report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`. It proves valid true-unitary transposition-subgroup roofs and updates the global first missing implication to `MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`.

This is compatible with `MOC4-STANDARD-PR-LOCKING-v1`: the two estimates constrain the same hypothetical support gap by independent genuine-unitary mechanisms, so on the unique-standard-maximizer branch one may take the minimum of the subgroup-cubature ceiling and the standard-P–R-locking ceiling.

For the lead's hard simple-complex datum

`a=(-4+4i,-i,-3+2i,-4-4i)`, `b=(-4-4i,2-i,2-4i,4-i)`, `eta=1`,

exact endpoint/channel arithmetic gives

- `M=256`, `Q=245/2`, `Delta=267/2`;
- unique standard maximizer `sigma_*=3142`;
- `K=855/2`, second standard value `723/2`, hence `delta=66` and `r=294`;
- `H_{sigma_*}=94`, hence `d_*=162`;
- `L_P=0`, `L_R=456`, `L=912`;
- `MOC4-STANDARD-PR-LOCKING-v1` gives `gamma <= 42906/163`.

The campaign lead's subgroup cubature gives the much stronger `gamma <= 289/3` on this same datum. Therefore the new locking theorem does **not** close or materially sharpen that particular hard residual. Its value is a different branch-local structural payment: when the standard-channel ceiling is already tight enough to force a large unique-endpoint Birkhoff mass, the exact `P -> D -> R` relation locks the pair quotient toward the compatible endpoint.

Accordingly the global first unpaid implication is the lead's `MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`; `MOC4-STANDARD-FACE-LOCK-v2` remains a useful branch-local subproblem inside the wider residual analysis. Full MOC4 remains OPEN / NOT PROVED / NOT DISPROVED.
