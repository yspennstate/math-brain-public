# account02/B15 handoff — bent near-isoclinic Boolean obstruction to high-posterior sector KL

**Status:** FULL FEI OPEN. This is a source-bound obstruction/bridge-change handoff, not a proof of the all-gate inequality.

Scientific source report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T060159Z-bent-nearisoclinic-sector-obstruction/REPORT.md`
created by scientific commit `6c80637addf4be75e75ca225b50b9b5823359c25`.
Checker: commit `636123a454f02518569858c065e46e6bec521f86`; saved output: `ecfabc214a1bee058faac45831d73aaf1c8adf77`.

## What changed

B15's preceding character-cofactor sector theorem paid a rare Shannon loss because a nonshared Fourier sector had posterior `theta=1/2`. The first missing Booleanity implication was that any dangerous balanced pivot should expose some high-posterior source-defined sector, or at least force the exact vertical KL to have the `d log(1/d)` scale.

That implication is false for genuine Boolean functions.

For even `m=2r`, take the quadratic bent sign `b(u,v)=(-1)^(u dot v)`, add a fresh unbiased character `chi_y`, and let

`f0(y,x)=chi_y b(x)`,
`f1(y,x)=f0(y,x) (1-2 1{x=0})`.

The restrictions are balanced and disagree with probability `d=2^-m`. Writing `s=sqrt(d)` and the bent Fourier sign as `sigma`, their paired coefficients are

`a=sigma s`, `b=sigma s-2d`.

At the unbiased pivot:

`T=d A_sigma`, `A_sigma=1-2 sigma s+2d`,
`theta=d/A_sigma`.

For `m>=4`, every spectral posterior lies in

`(8/13)d <= theta <= (8/5)d`,

and the entire exact vertical relative entropy satisfies

`I(S;J) <= 40 d^2`.

Thus no data-processed Fourier sector can recover a `d log(1/d)` payment on this family.

In account01/B16's balanced-pivot angular state,

`c=1-2 theta > 0`,
`E|c|-|rho|=0` exactly,
`Var(c) <= 64 d^3`.

So this is an actual Boolean near-isoclinic/sign-coherent family. It consumes account01/B16's completed joint-credit/dyadic-rigidity result and answers the compatible B17 existence question affirmatively: strict Boolean rigidity can become arbitrarily small. This is compatible with the strict no-equality theorem.

The exact local Shannon term at support-deficit center `C` is

`L_C = C d - 1 - h2(d) + H(B|S) + I(S;J)`.

Because `H(B|S)<=1`,

`L_C <= d [C-m+40d]`.

Hence for every fixed finite `C`, the local term is negative for all sufficiently large even `m`, even though *all* exact local branch/KL credits are retained. At `C=6.521851214`, the analytic upper bound is already negative at `m=8`.

This refines, rather than duplicates, account03/B13's earlier bent-swap proof that pointwise scalar local margin can fail: here the full posterior geometry is controlled and rules out the proposed high-posterior sector rescue.

## Child slack pays the same family

For the two children,

`H(f0)=m`, `I(f0)-1=r`, hence `D_C(f0)=r(C-2)`.

For `f1`, exact bent sign cancellation gives

`I(f1)-1=r(1+4d)`,

while its spectrum has at most `2^m` atoms, so `H(f1)<=m` and therefore

`D_C(f1)>=r(C-2)`.

Since `L_C>=-2`, the full exact two-child cocycle satisfies

`D_C(parent) >= r(C-2)-2`.

Thus the family is globally safe for every `C>=4`: the obstruction is specifically to credit-only/local payment, and it demonstrates quantitatively why the owner's instruction to retain child slack is essential.

## Next exact obligation

Retire any universal lemma asserting that a dangerous sparse balanced pivot must expose a high-posterior Fourier sector. The next payment must retain child/stopped-tree reserve, e.g. an aggregate form of

`(D_Gamma(f0)+D_Gamma(f1))/2 + H(B|S)+I(S;J) >= [-R_Gamma,j]_+`,

with exact source signs and negative KL credits preserved. Pointwise information credit alone cannot close the balanced rare-pivot case.
