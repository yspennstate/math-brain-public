# B16 FEI signed-transport handoff

Status: **PARTIAL / NEW EXACT IDENTITIES / FULL FEI STILL OPEN**.

This run replaces an absolute-variation view of the signed compiler expenditure by an exact signed Fourier transport. For Boolean phases with product one, the canonical xor-zero signed measure has the genuine squared-Fourier laws as its one-coordinate marginals. For the four phases `sigma, f sigma, g sigma, fg sigma`, the entropy plaquette

`kappa_sigma(f,g)=H(f sigma)+H(g sigma)-H(sigma)-H(fg sigma)`

is exactly a signed log cross-ratio over Fourier tetrahedra. Averaging over a mask phase subgroup `P` gives an exact quotient first-separator payment `K_P(f,g)` with no-reentry: it depends only on `fP,gP` and vanishes if either direction is already in `P`.

For a physical degree-`d` monomial generator, multiplication is a flat Householder reflection on each Fourier fibre. The total reflected projection energy is always `2^-d`, and its normalized profile is exactly the squared spectrum of the physical section at the monomial's `-1` cell. A raw absolute reflected-energy payment is impossible: on the monomial phase itself, entropy divided by reflected projection energy grows like `8d`. Therefore the next step must exploit baseline cancellation in the plaquette, section-profile mismatch and signed frustration credits rather than paying each reflection separately.

Executed checker: `check_signed_transport_plaquette.py`. Final status `PASS`: 16,452 exhaustive three-phase transport checks through dimension 3; 762 four-phase checks; 632 quotient/group-chain checks; 564 Householder checks. It exhibits genuine negative signed mass (`5/16`) already in dimension 3. The first local run failed with a deterministic `NameError` in the random Householder sampler; that checker bug was fixed and the complete run was rerun successfully.

Artifact identities:
- `REPORT.md`: Git blob `88d9d9d43403c51157eb2010863d6e0236d28709`, SHA-256 `30d2fd32349853ba5d705cc0fb8dfbc04fbce3a13b994ab537391545d70f9a2d`.
- `check_signed_transport_plaquette.py`: Git blob `e430a43b9e4a59cee7425bd99590cf1ec4cc5f5c`, SHA-256 `42dd1d5a2d22094bc19e45ae9724859fecb1690e42347fc0c558045bd779f618`.
- `signed_transport_plaquette_output.json`: Git blob `58162cacf0bfab2e0c21e4d2f56c4b508a5f8464`, SHA-256 `d5a5de1653f3271759aaa041138495670648d05b9057b3636807e7f108b758de`.

Next target: prove a baseline-cancelled Householder inequality for a monomial generator that pays positive plaquette curvature by original-coordinate boundary plus divergence of the two physical-section spectral profiles, while retaining a negative/frustration rebate from negative transport atoms. Do not resurrect raw absolute reflection-energy payment or discard signs.
