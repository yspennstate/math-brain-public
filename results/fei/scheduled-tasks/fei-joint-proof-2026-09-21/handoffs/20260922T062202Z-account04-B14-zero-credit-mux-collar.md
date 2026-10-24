# account04/B14 FEI handoff — uniform zero-credit MUX collar

Run: `B14-20260922T061206Z-fei`  
Classification: `ESSENTIAL_STEP_APPLIED`  
Full FEI: OPEN / NOT PROVED  
Execution: `WITHOUT_VERIFIED_BRAIN`

## Exact sources consumed

- account01/B18 `20260921T1856Z-curvature-refunded-crossing/REPORT.md`: exact physical block drift `J-E J_child = I_A+C_A` and curvature-refunded critical-core inequality. Source-to-next-arrow use: retain nonmodular information/crossing credit; do not replace it by prescribed-coordinate payment.
- account04/B18 `20260922T045533Z-mux-joint-credit-collapse/REPORT.md`: exact unequal-MUX selector credit, balanced-selector midpoint formula, and exact zero-credit lines.
- account01/B18 `20260922T052537Z-zero-credit-mux-line/REPORT.md`: proves the live candidate on both zero-credit lines and supplies uniform line floor `Z(s)>=0.0167628035` plus the pinned h96 source envelope.
- current live candidate: `C^dagger=6.521851214`, `a^dagger=0.268204856`.

## New theorem

For the one-bit MUX `M(A;D0,D1)` with selector bias `t` and data biases `q0,q1`, the current candidate is rigorously safe throughout

`|t-1/2| <= 1e-6`

and

`min(|q0-1/2|, |q1-1/2|) <= 1/4400`,

with the other data bias arbitrary in `[0,1]`. Quantitatively,

`D_{Gamma^dagger}(M;t,q0,q1) > 5.15e-5`.

Proof ingredients:

1. From the pinned h96 source envelope, `Gamma^dagger` is `66`-Lipschitz on all candidate arguments occurring in this collar, and `0<=B(u)=Gamma^dagger(u)+h2(V_u)<9` globally.
2. At balanced selector, the exact MUX midpoint formula retains the angular Boolean credit. Since `Phi>=-1`, this term is nonnegative. Perturbing either zero-credit line by `epsilon` therefore costs at most `(66+C^dagger)|epsilon|`; at `|epsilon|<=1/4400` the inherited line floor leaves defect `>0.0002805645`.
3. Releasing the selector by `sigma` changes the exact six spectral masses by L1 at most `6|sigma|+8sigma^2`. For `|sigma|<=1e-6`, Fannes--Audenaert costs `<88e-6`; candidate/data/output terms cost `<141e-6`; the leaf entropy term costs `<2e-10`. The final reserve is `>5.15e-5`.

## Scientific archive

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T062202Z-zero-credit-mux-collar/REPORT.md`

report commit: `0182dedf5f82bd0ee0cac8c5d9b691ba513ec456`

checker commit: `321844e456d6a861ca1f5c9fc62efb6b3902ee0e`

checker SHA-256: `610fc51be91a02ebd639ce61be32ab5e78898d6131b5805815c7f9bfafd2df44`

captured-output commit: `a3dbc9951ea1c6f1ecbe3c2381a8da882da4bec7`

## Next arrow

Intersect the remaining compact unequal-MUX region (outside the complementary-data tube and these two zero-credit collars) with the exact selector-credit lower bound and account04/B12's simultaneous negative data-pivot residual conditions. Either prove the remaining compact region safe or isolate a source-valid negative point. Do not reopen prescribed-coordinate erasure.
