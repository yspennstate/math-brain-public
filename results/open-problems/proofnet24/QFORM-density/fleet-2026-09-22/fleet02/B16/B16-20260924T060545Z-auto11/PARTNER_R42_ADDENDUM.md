# fleet02/B16 addendum — consume latest partner r42

Run: `B16-20260924T060545Z-auto11`  
Status: **LATEST PARTNER CONSUMED / MAIN REPORT CORRECTION UNCHANGED / FULL QFORM OPEN**

After the main report was committed, fleet03/B16 published r42:

`yspennstate/math-open-problems@210b93b7a190c6784523e9bf281b0529614b3334`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260924T055252Z-fleet03-B16-QFORM-r42/REPORT.md`.

This supersedes r41 as the latest compatible designated-partner result for this run. Its theorem `QFORM-HUB-STAR-PLANCHEREL-AVERAGE-v1` is independent of the fleet01 shear step challenged in the main report and remains usable.

## 1. r42 theorem applied to the strict target family from the main report

For

`Q=aH^2+2H b^T X+X^T C X`,

r42 proves

`|phi_Q(t)| <= sqrt(pi) 2^(1/4) ||b||^(-1/2) |t|^(-1/2)`          (1.1)

for arbitrary independent cap-one original sources, by exact Plancherel averaging in the physical-star frequency.

In the strict near-coloop target family of the main report,

`a=1/64`, `tau=1/512`, `rho^2=4095/4096`,

so

`||b||^2=rho^2+tau^2
       =4095/4096+1/262144
       =262081/262144`.                                           (1.2)

Therefore the completed partner theorem gives the actual target oscillatory inequality

`boxed:
 |phi_Q(t)|
 <= sqrt(pi) 2^(1/4) (262144/262081)^(1/4) |t|^(-1/2)
 < 2.108 |t|^(-1/2),   t!=0.
`                                                                    (1.3)

This is pivot-uniform and retains the physical-star information. It does not by itself imply a bounded density because `|t|^(-1/2)` is not integrable.

The same family is exact rank three with spectrum `{64,lambda_+,lambda_-}`, `lambda_+>1`, `lambda_-<-1`; the pinned ruled theorem separately gives `p_Q(s)<=pi*sqrt(2)` for a.e. `s>=0`.

## 2. r42 sharpens the unpaid implication

R42 introduces the complex physical-star fiber density

`G_t(z) dz = E[ exp(i t X^T C X); b^T X in dz ]`                  (2.1)

and proves

`|phi_Q(t)| <= sqrt(pi/|t|) ||G_t||_2`.                           (2.2)

Thus a correction-safe closure of the hard collar follows from

`integral_{|t|>=1} |t|^(-1/2) ||G_t||_2 dt <= C`.                 (2.3)

The mask counterexample in the main report shows that a leaf-dependent density-preserving shear cannot be used to prove (2.3) merely by capping the translated hub density and then reinstating the original leaf product characteristic functions. Any shear-based exit from r42's mixed norm has to retain the hub factor as an additional source datum, or use an equivalent phase-aware `TT*` argument.

Accordingly the first unpaid implication for fleet02/B16 is best stated as

`QFORM-R42-INTEGRATED-FIBER-L2-WITH-HUB-DATUM-v1`:

> Prove r42's mixed norm (2.3) in the punctured exact-rank-three collar by combining the rank-two Schur curvature with the original product law while retaining the literal hub factor through every leaf-dependent shear. Do not pay an isolated hub Wiener norm, a worst conditional projected-density cap, or post-rotation independence.

The r42 Plancherel theorem itself is not challenged by the main report's correction. The correction applies specifically to the later step that would discard the translated hub amplitude while still claiming leaf-product Fourier factorisation.
