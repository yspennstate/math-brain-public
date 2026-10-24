# account02/B16 repeated line audit — 20260925T083258Z-account02-B16-fiveaudit-P11

Objective: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925 (AUDIT ONLY).

## Source pin
- math-open-problems commit: ec211ba2d77a4a9850168c6af1574ea651feaa7c
- short.tex blob: c4f2a997cf336ee974e15409b5bccdd8cca039d8; 58,136 bytes; 675 physical lines
- short.pdf blob: 8be3aae36ecad7a9dc9b7c95978aad09499f32d0; 484,310 bytes; 14 PDF /Type /Page objects
- manifest PDF SHA-256: 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423
- direct visual PDF screenshot comparison: UNCHECKED in this run because the private GitHub PDF could not be opened by the screenshot-capable web PDF route.

## Reconstruction order
Fresh derivation began at Section 6 (L513-L580), then checked the dependency chain backward and forward through L1-L675. Peer evidence was consulted only after the derivation.

## Verdict
No fatal defect found in the theorem chain after the explicit local repairs. Literal manuscript is not gap-free. The normalized proof closes below 269, hence the stated 270 bound.

### Literal exceptions
- L41 / PDF p1: FALSE abstract clause. Random-sign conversion needs the no-pivot hypothesis. Counterexample A=I_5. Repair C04.
- L62 / p1: UNCHECKED only for the current-literature claim that the three-eigenvalue question is open. The scaling and one/two-eigenvalue counterexamples on the same line check.
- L65 / p1: FALSE presentation clause. The proof supplies a square-root/logarithmic upper envelope, not a necessary singularity. Repair C05.
- L74 / p2: UNCHECKED as a complete external-attribution bundle; internal claim that Section 4 tolerates same-bank quadratic terms checks.
- L148 / p3: GAP wording: “Both follow” introduces three assertions. All three singular-value assertions check. Repair C06.
- L222 / p5: FALSE local clause: zero beta rows need not be at most one. Example U=(e1,e2), W=(e3,e4) gives beta1=beta2=0. Drop all zero-beta factors; frame identity and e^{d/2} bound are unchanged.
- L319-L321 / p7: GAP local. Insert |E F|^2 <= E|F|^2 before (4.5). Repair C02.
- L398 / p9: GAP local. Square-profile density formula should be stated for z != v / a.e.; assign arbitrary representative at z=v.
- L412 / p9: GAP local. Half-open angular chart is not a global diffeomorphism. Remove one null ray/use an open angular interval. Repair C01.
- L441 / p10: GAP local closure. Explicitly note {q=v} is two affine lines, hence null under the joint density. Repair C03.
- Bibliographic metadata L651,653,655,657,659,661,663,665,667,669,671 / p14: UNCHECKED metadata; no proof dependency.

## Section 6 adversarial reconstruction
No-pivot gives |a_ii|<1/12 and |a_ij|<5/48. For C=(0 M; M^T 0), SVD gives eigenvalues ±sigma_j(M) and the remaining zeros, so s_{2m-1}(C)=s_{2m}(C)=s_m(M), including zero padding.

For Q_eps=sum_{i!=j} eps_i eps_j o_ij phi_i phi_j^T, expanding the Frobenius square leaves exactly the two ordered pairings (p,q)=(i,j),(j,i):
E||Q_eps||_F^2 = sum_{i!=j} o_ij^2 (|phi_i|^2|phi_j|^2+(phi_i.phi_j)^2)
<= 2 a^2 (sum_i |phi_i|^2)^2.
No missing factor two was found.

With k=2m-1 and Phi the selected eigenvector matrix,
2 Phi^T C Phi = Lambda - Phi^T Delta Phi - Q_eps.
The diagonal compression is <eta, some sign has ||Q_eps|| <= ||Q_eps||_F < sqrt(2) a0 k, singular-value perturbation gives s_k(2 Phi^T C Phi)>2 gamma_m, compression gives s_k(C)>=s_k(Phi^T C Phi), and duplication yields s_m(A_{I,J})>gamma_m. Gram/Cauchy-Binet then gives E_m>gamma_m^{2m}. No rank-index or sign loss found.

## Projection/product interaction
Only literal original-coordinate banks are copied. D=X_J-X'_J has independent physical coordinates with densities <=1. The phase-weighted hub measure is dominated by the ordinary joint projected law before Plancherel. After mollification, Step 4 applies one joint projection-density estimate to (M_H D,(<c_i,D>)_i), then scalar Fourier-power estimates. No independence of rotated/projected coordinates is asserted or needed.

## Constants recomputed
C3=14.818337662843<15.
C2=12.095072570796486<12.2.
gamma1=0.3846763769597346; gamma2=0.23736246421253723; gamma3=0.09004855146533981.
Gaussian small-ball coefficient=18.25531919676703<19.
C3/gamma3=164.55942290805933<167.
C2/sqrt(gamma2)=24.82575456311178<26.
Diagonal half-moment total=76.14307501039998<77.
sqrt(12)*77=266.7358243656071<267.
16*pi=50.26548245743669<51.
Indefinite-pair branch=266.95134633033405<269.

## Independent comparison after derivation
Account03/B19 run 20260925T070048Z-account03-B19-fiveaudit-P2-r17 independently reproduces the C02 Jensen omission and the repaired complex-measure/Plancherel step on L286-L345. Account03/B16 run 20260925T065141Z-account03-B16-FIVE270-audit-r62 independently reports a complete source pass with no fatal defect. These peer reports were not used as proof premises.

## Remaining UNCHECKED
Fresh visual source-versus-render inspection of all 14 PDF pages; fresh Lean compilation; exhaustive current-literature verification of L62 and all bibliography metadata/attributions. None is used as a mathematical premise for the theorem derivation.

Execution label: WITHOUT_VERIFIED_BRAIN. No lower-threshold research, schedule/state changes, notifications, email, permissions, public release, paid calls, or cross-account authentication.
