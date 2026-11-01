# Exact infimum-over-flows characterization of relaxation time

## Source question

David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (2002 manuscript / 2014 recompilation), Chapter 3, Open Problem 3.44:

> Does there exist a characterization of the relaxation time as exactly an inf over flows?

Live source: https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html

## What is proved

For every finite irreducible reversible discrete-time Markov chain with stationary law `pi`, orient the non-loop physical edges once, let

- `C = diag(pi_x P(x,y))` be the conductance matrix,
- `B` be the oriented incidence matrix,
- `Pi = diag(pi)`,
- `L = B C B^T = Pi(I-P)`,
- `H_0 = {b : 1^T b = 0}`.

Then

```text
tau_2 = inf_{R : B R = I on H_0}
          sup_{b != 0}
          (R b)^T C^{-1} (R b) / (b^T Pi^{-1} b),
```

and the infimum is attained by the electrical routing

```text
R_* = C B^T L^+.
```

Equivalently, for centered state-to-stationarity flows `psi^x` satisfying

```text
B psi^x = e_x - pi,
sum_x pi_x psi^x = 0,
```

and energy Gram matrix `G(x,y)=<psi^x,psi^y>_{C^{-1}}`, one has

```text
tau_2 = inf_Psi lambda_max(Pi^{1/2} G_Psi Pi^{1/2}).
```

`main.tex` contains a self-contained proof by reducing the optimization to the minimum-operator-norm right inverse of the weighted divergence `D = Pi^{-1/2} B C^{1/2}` and reading its smallest positive singular value from reversibility.

The same argument gives the continuous-time analogue.

## Exact finite checks

`check.py` is the exact SymPy checker inherited from the R01 theorem package. It verifies:

1. `P4`: the natural path-congestion scalarization is `5/2` while `tau_2=2`;
2. `K3`: the stationary average of pairwise minimum Thomson energies is `4/3` while `tau_2=2/3`;
3. the exact electrical-flow formula on `P4`, `K3`, and a nonuniform reversible three-state chain with holding probabilities;
4. `L = Pi(I-P)`, divergence, and energy normalizations.

`check.out` is the archived passing output. These finite checks are certificates for the examples and normalization, not substitutes for the universal proof in `main.tex`.

## Independent audits and closure state

The mathematical source claim has two distinct end-to-end outside audits:

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

The latter is in `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_04-00-52__run-report.md` and independently proves the theorem via singular values rather than merely reusing R01's original Thomson/Rayleigh presentation.

Fleet status of the exact numbered source question: **PROVED / INTERNAL CLOSURE COMPLETE**. This is not a claim of public publication.

## Prior-art qualification

The abstract mechanism is classical in substance: Moore--Penrose inverses give minimum-norm solutions of incidence/divergence equations, and bounded right inverses of divergence are standard in inf-sup / Babuska-Aziz theory. A 2023 review of generalized inverses in graph theory explicitly describes the incidence pseudoinverse as the minimum-norm network-flow solution and traces the observation to Ijiri. Kook--Vempala, arXiv:2608.16878 (17 August 2026), also use dual certificates and a Babuska-Aziz constant in spectral-gap analysis.

A bounded source/current-literature search through 17 September 2026 did not locate a primary source explicitly stating the finite reversible-chain formula above with the stationary `Pi^{-1}` demand norm and identifying it as the resolution of Aldous--Fill Open Problem 3.44. A negative search is not a novelty certificate. **Publication novelty remains UNVERIFIED.**

## Repository evidence

Canonical claim: `operations/claims/I0024.md`.

Main R01 proof history begins at:

- `runs/R01/2026-09-16T1258Z_i0024_flow_duality_01.md`

and the six-run handoff/rotation is:

- `runs/R01/20260916T1901Z_62d7c9a4.md`.

Canonical original checker paths:

- `artifacts/R01/i0024_exact_flow_checker.py`
- `artifacts/R01/i0024_exact_flow_checker_output.txt`

## Build

```bash
pdflatex main.tex
pdflatex main.tex
```

No Lean file is included because the finite core is covered by the exact-arithmetic checker rather than a Lean formalization.
