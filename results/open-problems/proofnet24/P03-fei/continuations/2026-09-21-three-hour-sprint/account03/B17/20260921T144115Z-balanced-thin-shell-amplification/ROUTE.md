# New Route 18 — balanced thin-shell tensor amplification

**Role:** account03/B17, FEI new proof mechanisms.  
**Status:** route opened; full FEI remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## Mechanism to test

Move the universal problem away from bias, isolated giant Fourier atoms, and broad level distributions by an exact Boolean tensor amplification.

For a Boolean base `f` on `n` variables and an independent auxiliary sign `z`, define

\[
F_m(z,x^{(1)},\ldots,x^{(m)})=z\prod_{j=1}^m f(x^{(j)}).
\]

The planned exact calculation is that the spectral law of `F_m` is a shifted product of `m` independent copies of the spectral law of `f`. If so, entropy tensorizes, influence is additive up to the single balancing coordinate, the largest spectral atom decays exponentially whenever `H(f)>0`, and spectral size becomes relatively concentrated by variance additivity. The central question is whether this gives an exact reduction of the sharp FEI constant to **balanced, Fourier-diffuse, thin-shell spectral samples**, with essentially all entropy lying *within* a narrow level band rather than in the level variable itself.

This is deliberately different from the preceding B17 face-channel, MUX, affine-orbit, support-deficit, Bellman and Han-deficit routes. It is an extremal reduction by Boolean tensor amplification, not another local restriction charge or finite sweep.

## Claims to prove or kill

1. **Balanced amplification:** `H(F_m)=mH(f)` and `I(F_m)=1+mI(f)` exactly.
2. **Diffuse/thin-shell amplification:** if `K=|S|` under the base spectral law, then `K_m=1+K_1+...+K_m`, so `Var(K_m)=m Var(K)` and the largest atom is `p_*^m`.
3. **Within-level reduction:** `H(S_m\mid K_m)=mH(f)-H(K_m)` and `H(K_m)=o(m)` for a fixed base, so the within-level entropy/influence ratio tends to `H(f)/I(f)`.
4. **Sharp-constant equivalence:** every strict violation `H(f)>C I(f)` amplifies to a balanced strict violation for large enough `m`. Therefore any valid universal proof may, without loss in the sharp constant, focus on balanced high-influence Fourier-diffuse thin-shell functions.

## Refutation / boundary plan

Stress the identities on exact admissible Boolean examples rather than arbitrary subset laws: constants and characters (degenerate entropy boundary), the two-bit one-point defect, and three-bit majority. If any tensor law, balancing statement, or level-entropy identity fails exactly, abandon the route. Do not infer full FEI from the reduction.
