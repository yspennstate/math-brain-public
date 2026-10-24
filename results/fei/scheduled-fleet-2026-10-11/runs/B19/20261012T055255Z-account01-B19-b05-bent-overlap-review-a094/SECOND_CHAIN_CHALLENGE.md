# Independent chain challenge: B05 bent-overlap payment

Target commit: `86af28f927222e626e9d852c9a1f47ccab82d46c`.

## Risks selected independently

1. Reconstruct the selector Fourier coefficients and upper masses when both
   children occupy the same frequencies.
2. Verify the empty-selector cap identity coefficientwise, not by an
   assumed mixture law.
3. Track every `k-|T|` logarithm and require signed atomwise cancellation.
4. Differentiate the residual scalar directly and certify its full Hessian
   box at the simultaneous endpoints `k=8,p=1/2`.
5. Close the numerical-looking inequality `97/ln2<140` by a rational lower
   bound for `ln2`.
6. Reconstruct physical selector influence from pivotal edges, including
   the factor two for both edge endpoints.
7. Test phase, flip-point, smallest-dimension, least-rare, and increasingly
   rare regimes without importing the author's checker.
8. Compare against disjoint composition/read-once results and the current
   plateaued-function theorem without transferring any hypothesis.
9. Locate the first hierarchy step not proved by the one-node estimate.

## Result

All proof steps through the single bent one-point-surgery node are valid.
The general shared-switch identity and the bound `J<=71 I_ctl` are accepted
at their stated quantifiers. The proof spends only physical fresh-selector
influence and retains both child `U` packets.

The first unpaid line is repeated coherent surgery: no argument bounds the
sum of changing shared-spectrum cap ratios down an arbitrary hierarchy, and
no nonreuse telescope is established there. The accepted theorem therefore
does not imply `U<=K I` or full FEI.
