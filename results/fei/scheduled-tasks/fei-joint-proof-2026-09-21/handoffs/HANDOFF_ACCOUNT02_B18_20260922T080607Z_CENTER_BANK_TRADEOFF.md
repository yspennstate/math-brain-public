# account02/B18 source-bound FEI handoff — center/bank dual frontier

Source scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T080607Z-center-bank-dual-tradeoff/REPORT.md`

Consumed other-account input:
`account01/B16/20260922T0743Z-and-bank-exhaustion`, report blob `31753d0347049d78cdfa1e8a19e6cc858feaa219`, together with the exact account03/B12 biased composition-prime witness.

## New exact implication

The 35 positive rational AND multipliers from account01/B16, with the center coefficient retained rather than set to zero, satisfy

\[
\sum_j\lambda_j[-L_{p_j,q_j}(\psi)]
={57\over256}\psi(3/8)-\psi(967/2048)
+\beta\psi(1/2),
\]

\[
\beta={23156036957147\over44712962557360},\qquad
\sum_j\lambda_jM(p_j,q_j)=
\kappa={792001822391570453\over11721234856636579840}.
\]

For the actual Numaro prime witness the perturbation response is
\[
W_{wit}(\psi)={465\over256}\psi(1/2)+{57\over256}\psi(3/8)-\psi(967/2048).
\]
Hence any correction satisfying the charged AND bounds with bank `K` obeys
\[
W_{wit}(\psi)\le \kappa K+\gamma\psi(1/2),
\qquad
\gamma={928973883008923\over715407400917760}.
\]
Using only the guaranteed uniform bank `K<=A=0.258204856` and the certified witness deficit `>0.0176114` forces
\[
\psi(1/2)>0.000126714849610403362\ldots,
\]
so every repair in that architecture has center
\[
\Gamma_{new}(1/2)>6.521977928849610403\ldots .
\]
This is an architecture-specific center floor, **not** a universal FEI lower bound.

## Exact next target

Evaluate the *actual nonuniform certified AND slack* on these same 35 charged pairs. The same positive dual gives a scalar weighted-slack test. If that weighted real slack is below the biased-prime deficit, the corresponding same-base repair class is ruled out without a uniform-bank surrogate; if above, the excess is the exact available resource for a fixed-point/envelope construction.

Compatible parallel input: account02/B16 `20260922T072030Z-source-bias-finite-secant` reduces another genuine n=18 coherent-bias source test to two near-half base-potential secants. Do not return to center-zero bump tuning or the retired half-band positive-current route.

Full unrestricted FEI remains OPEN / NOT PROVED.
