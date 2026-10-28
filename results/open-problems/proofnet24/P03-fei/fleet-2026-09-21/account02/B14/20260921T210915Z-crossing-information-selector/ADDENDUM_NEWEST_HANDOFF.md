# B14 addendum — newest subcube-peeling handoff and the corrected residual


The handoff proves two facts that must be retained together:

1. if a maximum/average-controlled pivotality support is within absolute error `q/(16r)` of a codimension-`r` coordinate subcube, the defining **physical** block `Z` satisfies `Delta_Z H <= 12 I_Z`;
2. replacing `q/(16r)` by fixed relative error `q/16` is false even for a unique maximum-influence pivot and after the exact folded refund. Its explicit family has
   `Delta_Z H / D_Z > (log_2 r-1)/25 -> infinity` while the function itself still has bounded `H/I`.

This does not invalidate the crossing-information theorem in `REPORT.md`. It identifies exactly what that theorem does and does not buy.

## The obstruction has almost maximal posterior crossing

In the fixed-relative obstruction, write `q=2^-r`, `delta=q/16`. The pivot `x` is sensitive exactly on

    E_x = {z=0} union {w=0}.

Hence

    p_x = q+(1-q)delta.

Reveal the defining control block `Z`. On the atom `z=0`, the posterior pivotality is `1`. On every atom `z!=0`, it is `delta<1/2`. Therefore the posterior-majority crossing is exactly

    c_x(Z)=q,

and its crossing fraction is

    gamma_x(Z)=c_x(Z)/p_x
              =1/[1+(1-q)/16]
              =16/(17-q)
              >16/17.

Thus the bad defining block is **not** bad because it fails to create a crossing. It creates an almost maximal crossing.

Applying Theorem 4.2 of `REPORT.md` gives the rigorous physical payment

    h_2(p_x) <= 9/(2 gamma_x(Z)) I_Z
             < 153/32 I_Z
             = 4.78125 I_Z.

On the other hand the newest handoff gives

    Delta_Z H / D_Z > (log_2 r-1)/25,
    D_Z=I_Z+q >= I_Z.

Consequently

    Delta_Z H / h_2(p_x)
      >= [Delta_Z H / D_Z] [D_Z/I_Z] [I_Z/h_2(p_x)]
      > (log_2 r-1)/(25*(153/32)),

which diverges with `r`.

So **substantial posterior crossing plus the correct logarithmic physical cost is still insufficient to bound the uncorrected block entropy decrement by one survivor's marginal Shannon entropy.** This is an exact compatibility result with the newest obstruction, not a contradiction.

It also explains why the compiler in `REPORT.md` was deliberately formulated with the corrected decrement

    E_A = Delta_A F = B_A-Q_A,

rather than with `Delta_A H`: the new obstruction rigorously kills the stronger uncorrected version on the natural defining block. The obstruction does not by itself prove that `E_Z/h_2(p_x)` diverges, because the full potential/recombination rebate `Q_Z` may be non-negligible; no such claim is made.

## Updated exact residual

The current B14 target is therefore narrower than the initial report's generic wording. A universal proof from interface A needs one of the following on every high-ratio primitive core:

- a physical pair `(A,j)` with `c_j(A)>=gamma p_j` and **corrected** decrement `B_A-Q_A <= K h_2(p_j)` for fixed `gamma>0,K<infinity`; or
- the stronger already-paid codimension-sensitive stability branch from the newest handoff (`error <= q/(16r)` giving `Delta_A H<=12 I_A`); or
- a different physical/adaptive block that escapes the fixed-relative obstruction while charging its extra entropy to a nonreused joint-row / mixed-derivative credit.

A theorem asserting that the defining block of every fixed-relative near-subcube row works is now explicitly retired. The next derivation should study a **minimal corrected-crossing stopping block** (first block along an adaptive reveal order for which `c_j(A)>=gamma p_j`) and attempt to show that its *incremental corrected erasure* is controlled by `h_2(p_j)` plus a mixed-derivative credit that telescopes globally. If the fixed-relative obstruction can be adapted to this minimal-stopping formulation, preserve it as the decisive counterexample and switch mechanisms again.
