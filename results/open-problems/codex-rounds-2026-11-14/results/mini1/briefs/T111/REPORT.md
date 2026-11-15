VERDICT: PROVED rare midpoint contamination limit and stability for a three-point iid triangular array

For fixed p in (0,1) and lambda >= 0, put probabilities `(1-lambda/n)(1-p), lambda/n, (1-lambda/n)p` on `{0,1,2}`, then center and standardize each row of n iid summands. With q=1-p, the normalized Berry–Esseen error has the exact limit

\[
 \lim_{n\to\infty}\frac{\sqrt n\,\Delta_n}{\rho_n}
 =\frac{|q-p|/6+(1+e^{-2\lambda})/4}
        {\sqrt{2\pi}(p^2+q^2)}.
\]

The supremum of this limit over fixed p is

\[
 K(\lambda)=\frac{B+\sqrt{B^2+4}}{12\sqrt{2\pi}},
 \qquad B=3(1+e^{-2\lambda}).
\]

This equals Esseen's constant at lambda=0 and is strictly smaller for every lambda>0. The proof also gives a compact-parameter stability statement: if p stays away from 0 and 1, n times midpoint mass stays bounded, and the ratio tends to Esseen's constant, then n times midpoint mass must tend to zero and p must tend to one of Esseen's two reflected parameters. See PROOF.md for the binomial expansion, uniform remainder argument, both jump sides, optimization, and stability proof.

This treats a scale missed by fixed-law lattice asymptotics: a third atom of probability lambda/n leaves a surviving parity factor exp(-2lambda). It does not give a universal finite-n bound, and novelty over all existing literature is not asserted.

| lambda | optimized limiting ratio |
|---:|---:|
| 0 | 0.4097321837023964 |
| 0.1 | 0.3745865640296369 |
| 1 | 0.2445449773432545 |
| 4 | 0.2196641047910368 |

Reproduce the finite checks with:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_midpoint.py
```

The final run passed all assertions in 1.94 seconds with peak RSS 128,696,320 bytes and verified effective nice 20. It computed 80 finite laws through n=32768; 48 smaller rational cases were independently checked using exact integer polynomial multiplication and 90-digit arithmetic. The maximum independent ratio discrepancy was 7.61e-15. Full commands and stdout are in LOG.md; data are in midpoint_data.csv and midpoint_audit.json. AUDIT.md includes a separate Fourier derivation of the parity coefficient and the analytic failure-case checks. Finite floating computations illustrate the theorem; they are not certified finite-n enclosures.

What failed or needs care:

- macOS rejected an address-space hard limit. The script retains CPU/wall limits, bounds its array sizes, and reports peak RSS; actual memory was well below 1 GB. The external nice command warns because the inherited priority is already 20, which the script checks before computing.
- The limiting expression is not a finite-n upper bound: at lambda=4, its optimizing p, and n=32768, the actual computed ratio exceeds the limit by about 1.55e-6.
- The proof does not cover parameters approaching p=0 or 1, unbounded n times contamination, or other locations of the added atom. The remainder has no explicit numerical constant.

Literature check, finished within ten minutes: a full-solution claim was found in Bartosz Kołodziejek and Kacper Rodziewicz, *The sharp iid Berry–Esseen inequality: Analytic reductions and exact certificate proof*, Hexagon 2610.00590v1, posted 29 October 2026. The primary PDF was opened: https://hexagonmath.org/pdf/2610.00590v1. It claims the full conjecture. Its long analytic reductions and certificate suite were not verified here; the current constants list still describes the sharp value as conjectural. SOLVED_ELSEWHERE.md records the precise claim and distinguishes the Hexagon identifier from an arXiv id. No claim that the full problem is settled is made in this report. The already supplied eventual theorem was confirmed on Hengzhi He and Guang Cheng's arXiv page, https://arxiv.org/abs/2609.06358v3.

Next worker: extend the midpoint calculation to another point on a finer lattice, retaining the distribution of the contamination count modulo the lattice index. For a universal sharp bound, an effective remainder uniform over near-two-point perturbations is still required; the present compact-parameter asymptotic formula alone does not supply it. Separately, audit the analytic hypotheses linking the October full-solution claim to its finite certificates before treating it as a solution.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 21:17 Asia/Tbilisi (session start).
