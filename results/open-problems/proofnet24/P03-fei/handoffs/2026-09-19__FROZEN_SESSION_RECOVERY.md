# FEI frozen-session recovery — 19 September 2026

Status: **PARTIAL; full Friedgut–Kalai FEI is not proved in this handoff.**

This file was written at the owner's request after a ChatGPT research session froze. It consolidates the recoverable written state and links the actual existing proofs rather than inventing or duplicating unavailable work. The latest conversation recovery records that the earlier assistant reported GitHub writes unavailable and intended to prepare a patch. No completed additional September 19 FEI patch or hidden unfinished derivation was recovered. Do not count a promised patch as a saved result.

## Read first: an important correction

The authoritative correction is [FEI.md](../../../research_pushes/2026-09-18-sidorenko-fei-ising/FEI.md), blob `98e27d0b12e7b48805220a4fad413ad72e76090a`, already present on master when this recovery began.

The old `solo-2026-09-17/FINAL_HANDOFF_2026-09-18.md` asserted the pointwise inequality

    H(f) <= B(f) + (2/ln 2) I(f).

**This is false.** All entropy is in bits; B(f)=sum_i H(X_i | X_{-i}) for the spectral sample X. An explicit parity lift of the eight-selector addressing function has H=16, I=11/2, B=0. The correction contains a rational verification of 16>11/ln 2.

What survives is the universal implication

    [B(g) <= K I(g) for every Boolean g]
        => [H(f) <= (K+2/ln 2) I(f) for every Boolean f],

and the hereditary pointwise version using the maximum B(g)/I(g) over all physical coordinate restrictions g of f. Do not replace that maximum by B(f)/I(f). Physical restriction destroys spectral code isolation.

## Recoverable main arguments, already committed

1. [Full solo continuation index](../solo-2026-09-17/NEXT_STEPS.md), blob at recovery `ccd310f1f2b276f400f39520ebc6da795b9516a7`. It records the precise logarithmic target, failed power-moment and local-restriction routes, and the retained positive results.
2. [Interference patching theorem](../solo-2026-09-17/INTERFERENCE_PATCHING_THEOREM_2026-09-18.md), blob `79ab93e1cd3dbb16278f17bca337553e5520da6c`. For signed selector cells v_j=1_{C_j} sigma_j, masses delta_j, data parity labels D_j, normalized cell spectral entropies E_j, and maximum coherent/incoherent ratio Lambda,

       H(f) <= Lambda [H(J)+sum_j delta_j E_j].

   With boundary separation, sum_j D(v_j)<=I_x(f) and H(J)<=2 I_x(f). Local E_j<=C D(v_j)/delta_j therefore imply H(f)<=Lambda(C+2) I_x(f). This is conditional on the representation and local estimates; it is not a universal decomposition theorem.
3. [Subcube parity multiplexers](../solo-2026-09-17/SUBCUBE_PARITY_MULTIPLEXERS_2026-09-18.md) and [bounded collisions](../solo-2026-09-17/BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md). These are structured-class results, with interference explicitly accounted for.
4. [Systematic spectral coding and constant-preserving erasure obstruction](../../../research_pushes/2026-09-18-sidorenko-fei-ising/FEI.md). For every fixed k, the supremum H/I among Boolean functions with Fourier support minimum distance greater than k equals the unrestricted supremum. The existing proof also covers growing k_N=o(N/log N), with N the pre-encoding dimension. This obstruction does not refute FEI or the correct universal erasure implication.
5. [Exact coding checker](../../../research_pushes/2026-09-18-sidorenko-fei-ising/check_fei.py) and [archived output](../../../research_pushes/2026-09-18-sidorenko-fei-ising/fei_checks.json). Existing finite tests are not a proof of a universal inequality.

## Exact remaining full-scope targets

A. Establish, for every Boolean spectrum p_S=fhat(S)^2, a finite universal bound

    K(f) = sum_{cube edges {S,T}} min(p_S,p_T) |log_2(p_S/p_T)| <= C I(f),

with zero terms omitted. The prior reduction has K<=B<=K+(2/ln 2)I. A valid universal estimate for K would therefore imply FEI through the hereditary restriction argument. The direct pointwise entropy shortcut above must not be used.

B. Construct an interference-controlled physical decomposition with boundary separation and genuinely simpler leaves. One arbitrary cell merely restates FEI; point cells may have unbounded interference and unpaid artificial boundaries.

C. Seek an entropy-weighted or signed-cancellation replacement for the worst-case interference multiplier, rather than discarding the phases or using false power-moment bounds.

## Instructions for continuation

Read this recovery together with the latest P03 run and the original sources. Preserve the existing finite-dimension P03 metric and do not reset its atlas or claim a completed global proof. Record new arguments as immutable reports under `proofnet24/P03-fei/runs/2026-09-19/` and reusable notes/checkers under `proofnet24/P03-fei/continuations/2026-09-19-recovery/`.

No schedule was created, restarted, or verified merely by this commit. This is a research handoff on the actual master branch in the existing FEI track. The owner requested GitHub delivery, not email or public publication.
