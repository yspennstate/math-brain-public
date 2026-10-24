# FEI handoff — account04/B17 character-cofactor threshold

Source-bound scientific artifact: `yspennstate/math-open-problems`, path `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T061604Z-character-cofactor-local-threshold/REPORT.md`; creation commit `1e576c13521e7886fc2582aec04f5b6abd190c5e`; current report blob on readback `865131123fbceeb0d41109308d531ace9e926af6`.

Result: for a uniform Shannon pivot with balanced Boolean restrictions and one restriction a character, the exact conditional-information cocycle reduces the local gluing requirement to one scalar `Q(d)`. A rigorous source-valid estimate proves `Q(d)<5.1` for every `0<d<=1/2`, improving the prior compatible B15 threshold `6.387646448685102...`. Therefore at any center `C>=5.1`, this gluing cannot create a new balanced-uniform record above a safe child: `R(parent)<=max(R(noncharacter child),5.1)`.

Boundary adversary: an actual 12-bit Boolean realization with disagreement `d=235/1024` has `Q(d)=4.872321043042354...`, so any universal zero-child-subsidy local threshold at `C<=4.8723` is false. This is a Boolean witness, not a non-Boolean spectral law.

Checker: `CHECKER.py` commit `03155c1c2542c107323ae50d0f60e32ba4af8bc5`, readback blob `52081b1f64ca71be553301e25e0498ba6b07bd8e`, executed SHA-256 `4e7287910fcef1f8eec72249a0d2ae46b56d2a9753f0b2ecf6ac9802c9f9df51`. PASS output commit `17400494df49c82546233c8a4f510aab79f25c0f`, readback blob `e545aded146d96e1a42b06800902ed1f5f84059b`, output SHA-256 `b39eca8799fd8197c1f218527c203ba95cc8bd878dff9da6ccdee9581024566f`.

Scope: current owner revision `2026-09-22.2` all-gate convergence target. Full FEI remains OPEN / NOT PROVED. Execution WITHOUT_VERIFIED_BRAIN. The older Interface-D packet branch was read but not extended because the later OWNER MESSAGE supersedes it.
