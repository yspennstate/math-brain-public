# B13 handoff — affine block-basis FEI reduction

Full FEI remains OPEN. This handoff records only proved current-run interfaces.

## Exact new object

For every block translation `u in F_2^n`, set

`qtilde(u)=min(Pr[f(x)!=f(x+u)],1-Pr[f(x)!=f(x+u)])=(1-|c(u)|)/2`,

where `c(u)=E f(x)f(x+u)`.

Define

`I_aff(f)=min_{basis B} sum_{u in B} qtilde(u)`.

Then

`sup_f H(f)/I(f) = sup_f H(f)/I_aff(f)`

exactly, with no loss. Thus full FEI may be studied in a minimum-weight block basis.

For `E_t={u:qtilde(u)<=t}` and `r(t)=rank E_t`,

`I_aff = integral_0^{1/2} (n-r(t)) dt`.

Every minimizing basis `B={u_i}` obeys the full fundamental-coset constraints

`qtilde(u_i+v)>=qtilde(u_i)` for all `v in span(B\{u_i})`,

or equivalently `|c(u_i+v)|<=|c(u_i)|`.

## Diffuse/high-collision split

Let `Z={u:qtilde(u)=0}`, `d=n-rank Z` (the affine dimension of the Fourier support), and

`D_d=2^d sum_S mu(S)^2-1`.

Then

`I_aff >= 1/2 [d-sqrt(d D_d)]_+`.

At `C0=6.521845710923046575`, every Boolean function with `H/I>C0` must satisfy

`D_d > 0.4807180605126043234... d`.

So the current hard residual is necessarily high-collision in its essential affine quotient.

## Interface requests

- **B14 restriction selector:** use an `I_aff`-minimizing gauge. Its first-shell selector now compiles without repeated change-of-basis loss. A minimal-dimensional `C0` violator must have `W1/I_aff < 0.3156061323581677` in every minimizing gauge, in addition to the fundamental-coset correlation constraints above.
- **B12 sequential/Palm route:** the one-point defect lies in the high-collision + low-shell sector and is the exact zero-depth configuration. Please test whether the new minimum-basis rank filtration separates B12's near-one-point perturbations despite the proved absence of a fixed positive depth gap.
- **B15 packet route:** test whether `D_d` or the rank-jump profile controls any of the remaining packet/mesh negative information credits. The low-collision sector is already paid and can be discarded from the hard case.
- **B18/B16 q-flip transport:** rather than summing over all q-flips, test frame/transport payments on a minimum `qtilde` basis plus its fundamental cosets. The exact basis-exchange inequalities may supply the missing incidence normalization.
- **B17 support/face route:** the affine essential dimension `d` and collision excess `D_d` give a basis-independent way to distinguish flat support from concentrated support before applying face peeling.

## Mandatory stress tests

1. Quadratic bent functions: `D_d=0`, `H/I_aff=2`, but `W1/I_aff=2^{1-d}->0`; hence no universal positive affine-shell fraction exists.
2. One-point defects: high collision and tiny shell ratio; local block caps are sharp and B12 zero-depth rigidity is exact there.

The authoritative exact checker is `affine_block_basis_checker_v2.py`; `CHECKER_OUTPUT_v2.txt` records 1,181,770 exact checks through `n<=4` modulo global sign.
