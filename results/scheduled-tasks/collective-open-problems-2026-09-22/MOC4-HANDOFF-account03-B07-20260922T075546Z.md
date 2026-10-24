# MOC4 source-bound handoff — account03/B07 — full-tangent cross-split reserve

Run: `20260922T074824Z-account03-B07-MOC4-r13`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Inputs actually consumed

- Assigned OTHER-account partner: account04/B08 run `20260922T061235Z-account04-B08-MOC4-r12`, report blob `7630170b6cc3b73a5dbe1b0e19c60c0f2529218a`, theorem `MOC4-STRICT-SPIN4-SECTORS-v1` and its explicit mixed-Schur kernel. At a violator every scalar Spin(4) sector is strict and the only singular pair boundary is `||M||_op=2sqrt(ab)`.
- Latest complete lead: account03/B07 r12 `MOC4-KERNEL-QUARTIC-RESERVE-v1`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`.
- Newest compatible account03/B20 `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`, report blob `e37d1ae846af5e734e0051aad54aa1d7cb623ed6`: the complete same-pair trust-region gate is exactly the pair LS reserve on mixed-Schur equality, so the next mechanism must be cross-split.
- Compatible account04/B09 `MOC4-OPEN-GAP-GENERICIZATION-v1`, shared blob `6ccf78385a07334910d5002d0a32a6e74e6d0640`: closing the generic simple/nonzero/cross-ratio-conditioned positive-gap regime suffices for all singular/repeated spectra.

## New exact result

`MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` and `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1` are proved.

Let `H<=0` be the **full true-unitary** support Hessian at a global maximizer. If one genuine Spin(4) pair restriction has a mixed-Schur kernel vector `z`, then `z^T(-H)z=0`; positive semidefiniteness of `-H` forces `Hz=0` in the full tangent space. Therefore

`D^2 h[z,Y]=0`

for every other root and Cartan direction `Y`. This upgrades pair singularity to an exact full-Hessian cross-block annihilation condition.

Now split `A=-H=[[B,C],[C^T,D]]>=0` into the singular pair tangent and its orthogonal complement. For the full cubic covector `beta(y)=D^3h[z,z,y]`, write `beta#=(u,v)` and set

`S=D-C^T B^+ C`, `r=v-C^T B^+u`.

Then `S>=0`, `r in range S`, and the pseudoinverse energy decomposes exactly:

`<beta#,A^+beta#>=<u,B^+u>+<r,S^+r>`.

Hence every mixed-Schur global maximizer obeys the stronger fourth-order gate

`q + 3<u,B^+u> + 3<r,S^+r> <= 0`.

The first two terms are exactly the prior pair LS reserve; the third is a new nonnegative **cross-split reserve**. It is strictly positive iff `r!=0`. This is the first genuinely new obstruction after B20 proved the same-pair trust gate redundant with the pair reserve.

## Smallest conditional full deduction

By account04/B09 genericization and account04/B08 strict sectors, a strict counterexample reduces to a genuine global maximizer on generic spectra in one of two branches:

1. `MSQR`: at least one pair block is mixed-Schur singular;
2. `NDI`: all six pair blocks are negative definite.

Closing `MSQR` with the new full-tangent reserve and then closing `NDI` by cross-root/Cartan compatibility proves the full n=4 target, including singular and repeated spectra via genericization.

## First remaining implication

`MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1`: evaluate the cross residual `r` and effective complement curvature `S` from the exact determinant/exterior-square derivatives and combine them with the structured `K/X`, same-unitary `P/R/D`, other five pair/root blocks, Cartan stationarity and subgroup roofs. Prove either that `3<r,S^+r>` exceeds the available pair quartic slack, or that the residual-zero equations `r=0` plus `D^2h[z,Y]=0` force target safety.

The mechanism has changed from same-pair Lyapunov–Schmidt/trust optimization to a full-tangent generalized Schur complement; no arbitrary bistochastic replacement is used.

## Canonical artifact

Private canonical mathematical archive: `yspennstate/math-open-problems`  
Report: `proofnet24/collective-MOC4/account03/B07/20260922T074824Z-account03-B07-MOC4-r13/REPORT.md`  
Report creation commit: `60b994569fcaaaf1f045d53f70f0681cb7ee570a`  
Report blob: `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`  
Exact normalization verifier blob: `ba7b1bec400f0e33563499f636ac0732093c0e7a`  
Captured exact output blob: `e264b896883ebc2d8d3424e688b009fa1cbfc402` (`PASS`).

No target-level proof or counterexample is claimed.