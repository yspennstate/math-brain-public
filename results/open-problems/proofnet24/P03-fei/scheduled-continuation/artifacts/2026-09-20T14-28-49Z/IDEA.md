# PROB10-01 idea lock — hereditary hard-core localization

UTC label: `2026-09-20T14-28-49Z`. Full FEI remains the parent target.

Before writing a new checker, this run will test three materially different routes while preserving the current P03 corrections.

1. **Folded-influence pruning.** Use the exact restriction profile identity `Delta_i H = sum_T w_T Psi(t_T)` and its proved cap `Delta_i H <= Psi(j_i)`. For a fixed threshold `tau`, recursively query any physical coordinate with folded influence `j_i>=tau`. Since `Psi(t)/t` decreases, each such entropy decrement is paid by `kappa(tau) j_i <= kappa(tau) Inf_i`, while exact physical edge partitioning telescopes the queried influence. Goal: prove that any counterexample to a candidate FEI coefficient above `kappa(tau)` has a restriction descendant whose every folded influence is `<tau`.

2. **Dependency/profile stopping.** At a terminal state, multiply by the character that flips every influence above `1/2`. This preserves Fourier entropy and turns total influence into folded total influence. Then use the already-proved Huffman dependency-bank theorem `H <= (2/ln 2) I (H_2(w)+1)` for normalized influence weights `w_i=Inf_i/I`. Goal: prove that a surviving counterexample must also have large influence-profile entropy. This route is global/information-theoretic rather than the local restriction cap above.

3. **Aggregate true-allocation plus endpoint route.** Test, but do not assume, whether the sum over coordinates of the true conditional allocation plus the adaptive endpoint charge has a universal influence payment. The newly recovered exact-Booleanity report shows that finite-order square identities, dyadic amplitudes, bounded fourth moment, or uniform almost-Booleanity cannot justify a general real-valued erasure estimate; any successful proof here must use full Booleanity. I will use finite Boolean censuses only as stress tests, not as theorem evidence.

The target theorem if Routes 1–2 close is a hereditary localization/compiler: for `0<tau<=1/2` and `R>=0`, every Boolean counterexample above

`C0(tau,R)=max{Psi(tau)/tau, (2/ln 2)(R+1)}`

has a character-folded physical restriction descendant `g` with the same strict counterexample coefficient, all positive influences `<tau`, and normalized influence-profile entropy `>R`. This would be a full-scope reduction, not FEI closure: the low-influence diffuse core can still contain one-point, recursive-majority, or coded families.

Stress tests will include the archived one-point, addressing, bent/quadratic, coded `F_8`, tensor, majority-substitution, and fresh-control examples. The coded `F_8` truth table will not be enumerated; only source-level exact formulas may be used.
