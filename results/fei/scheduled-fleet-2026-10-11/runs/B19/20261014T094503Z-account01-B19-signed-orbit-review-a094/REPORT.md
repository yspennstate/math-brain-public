# B19 / A094 — independent review of B05 signed orbit ownership

**Target:** `B05-A023-SIGNED-ORBIT-OWNERSHIP-v1`  
**Producer:** account01/B05, canonical commit
`e1a663f08e373c8911cdfc7272985932777dbbe4`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED WITHOUT MATHEMATICAL REPAIR AT DECLARED SCOPE**  
**Universal GU / full FEI:** **OPEN**

## Audited candidate and implication

The candidate replaces the prior address-count term by

\[
\Theta_X(f)=\sum_{x\in X}q(Inf_x(f))
+\sum_{i\notin X}q(E_X^f(\{i\})).
\]

It claims shared-product transport, a first-reveal contraction, and an exact
signed telescope under arbitrary block changes. Together with the separate
unproved nodewise inequality

\[
\Delta_xU\le KInf_x+\lambda(R-O), \tag{D}
\]

these results would imply

\[
U\le(K+2\lambda/\ln2)I,
\quad H\le(2+2K+4\lambda/\ln2)I.
\]

## Independent verdict

All three proved components check.

- Product transport follows from conditional Cauchy--Schwarz on private
  singleton coefficients, the pivotal union bound on shared coordinates,
  and the exact scalar inequality
  `q(min(1,a+b))<=q(a)+q(b)`.
- First revelation follows from average preservation of the remaining
  physical influences and orbit energies, followed by concavity of `q`.
  The queried packet contributes the explicit drop `q(Inf_x)`.
- The changing-block identity is an exact signed cancellation. Root opening,
  branch-dependent block choice, coordinate re-entry, and terminal reserves
  are all retained; no credit is counted twice.

The endpoint derivation from (D) is also correct on a **complete** physical
tree. It uses `Phi<=2I/ln2` and the original Theorem G. It is an explicitly
sufficient U-drift route, not a proof of GU'.

## Mandatory scope corrections

1. “No `|X|` loss” means that no coarse multiplicative coefficient
   `|X|q(E_X(empty))` remains. The potential still contains one term for
   every shared coordinate. It is not uniformly `O(I)`.
2. The signed subtraction `-O_v` is indispensable. For the `r`-bit point
   defect,
   \[
   \Theta_{[r]}/I=r-1+2/\ln2,
   \]
   and the root opening has the same linear growth. Neither `R_v`,
   `Theta_X`, nor their positive parts are reusable influence credits.
3. Private blocks must remain disjoint in the product theorem. The result
   does not establish arbitrary shared-variable Boolean composition.
4. For a stopped tree, terminal `Theta` and terminal `U` must both be paid.
   Only a complete tree makes them vanish without a leaf hypothesis.
5. Criterion (D) remains the first unsupported line. In particular,
   `R_v-O_v` may have either sign, and an arbitrary active-block choice need
   not satisfy (D). Existence of a useful adapted choice is still open.

These are scope clarifications, not repairs to the stated theorem. The
reviewer-supplied point-defect opening obstruction is new and requires fresh
A085/A090 review before registry adoption.

## Independent verification

An independently written checker passed:

- 4,164 scalar subadditivity tests;
- 3,140 exhaustive physical-reveal cases through three variables;
- 12,256 independent shared-product tests, including 12,000 larger seeded
  factor pairs;
- 12,000 branch-dependent tree nodes with the root opening included; and
- the exact point-defect formulas through rank 128.

Maximum observed telescope error was `1.78e-15`. The acceptance rests on the
analytic reconstruction in `REVIEW_PROOF.md`.

## Status and next action

Accept `B05-A023-SIGNED-ORBIT-OWNERSHIP-v1` as a reusable signed accounting
bridge. Do **not** mark A023 complete and do not propagate a GU or FEI claim.
The next decisive test is the exact two-level overlap
`{x,y}->{y,z}`: substitute `Delta U=B-Gamma+KL` into (D), freeze `lambda`,
and determine whether some physical query/block choice survives all genuine
Boolean cores.

Model: Codex. Reasoning-effort metadata: UNKNOWN.

