# POS3 handoff — account03/B10 — explicit uniform-rank variance residue

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3:** OPEN / NOT PROVED  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

Canonical immutable scientific report:
- repository: `yspennstate/math-open-problems`
- commit: `74c9f4506b5cdb47f0418c8ab8a3de0934abfa8b`
- path: `proofnet24/collective-POS3/account03/B10/20260922T0214Z-a03-b10-r11/REPORT.md`
- report blob on readback: `3e50b4d0adaa18c79a96079139d660b832418a2d`

## Exact assigned-partner result consumed

Assigned partner **account04/B11**: `B11-20260922T011236Z-pos3-r12/REPORT.md`, blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`. It proves the qualitative exceptional band `7<=pi(P)<=K_3` and constructs arbitrary-size width-three, connected, module-prime examples already at `pi=7`, with rank variance at most `49/4` and one-element insertion multiplicity at most `8`. Exact change here: do **not** attempt a finite kernel; instead make the high-variance exclusion numerically explicit under the actual uniform extension law.

Additional compatible peer inputs used:
- account04/B10 blob `a7713fd0ecac31104201ec2a381d55b045a3adc7`: every element of a hypothetical width-three counterexample occupies its exact strong-majority rank with probability `>1/81`, with one-sided cases `>4/9`.
- account02/B10 blob `cc0b07e71d1c01c7741fa83f0058962088511124`: first/last majority-block boundary probabilities are in `(2/3,7/9)` and both Hasse-blocker channels are active.
- account01/B19 blob `f1f0eacfcb9f4d908947b7b640944ed6d7b69b34`: the first majority block is an ideal chain, the exact projected law is weighted by `W_C`, and its prefix mass is `>4/9`.

## New exact results

1. Stanley log-concavity of the rank distribution plus Aravinda's sharp discrete log-concave inequality
   `q(x)^2(1+Var(rank(x)))<=1`
   turns the collective pinned atom `q(x)>1/81` into the actual-uniform-law bound
   **`Var(rank(x))<6560` for every element**.

2. The one-sided Shepp/XYZ argument applies to every element of the **entire first and last strong-majority chain blocks**, not merely the two global endpoints. Their pinned rank atom is `>4/9`; hence
   **`Var(rank(x))<65/16` on both endpoint blocks**.

3. Let `K_AK(mu,L)` be the threshold in Aires--Kahn Theorem 3.1. Taking `mu=1,L=6560`, a maximum-product incomparable set pair `(A,B)` with `|B|>=|A|` cannot have `|B|>=K_AK(1,6560)`, because Theorem 3.1 would force average rank variance at least `6560`, contradicting the strict cap above. Since the maximum product dominates `pi(P)`, every hypothetical width-three counterexample satisfies
   **`7 <= pi(P) < K_AK(1,6560)^2`**.
   The upper constant is source-parameterized, not numerically invented; Aires--Kahn state existence of the threshold rather than a closed numerical value.

4. For the first ideal majority block `C`, `Q=P\C`, and exact lift multiplicity `W_C`, write `alpha=e(Q)/e(P)`. The prefix-rank atom gives `alpha>4/9`, while the newest first-boundary cap gives `alpha<7/9`. Therefore under the genuine uniform base law on `L(Q)` used in the exact identity `e(P)=sum W_C`,
   **`9/7 < E W_C < 9/4`**,
   with non-prefix full-extension mass in `(2/9,5/9)`. The actual projected law remains proportional to `W_C`; no uniform surrogate is asserted.

## External source inserted

Heshan Aravinda, *Entropy-variance inequalities for discrete log-concave random variables via degree of freedom*, Discrete Mathematics 347 (2024), 113683, DOI `10.1016/j.disc.2023.113683`, Theorem 1.4: `M(X)^2(1+Var X)<=1` for integer-valued log-concave `X`.

Aires--Kahn source: arXiv:2510.26134v1, especially Stanley rank log-concavity as their Theorem 2.2 and their Theorem 3.1 average-variance threshold for maximal incomparable set pairs.

## Next exact obligation

The new scalar bounds cannot themselves compactify the problem: the assigned partner's `pi=7` family already has much smaller variance and arbitrary order. The next actual-uniform-law step remains the **ideal-block weighted balance transfer / two-fringe charge**: combine exact `W_C`, the first-boundary two active Hasse channels, no-balanced touching constraints, and nested-profile boundary charges to force either a balanced pair meeting `C` or a weighted `Q`-pair orientation ratio in `[1/2,2]`.

No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive content, paid API/Codex use, remote workflow, public release, or production-brain mutation is present.
