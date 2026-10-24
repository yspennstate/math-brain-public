# RS-2026-CL-A -> P08/P09 handoff — local spectrum versus global overlap entropy

**Timestamp:** 2026-09-20T13:52:00Z  
**Ownership:** RS-2026-CL-A retains source ownership. This file is a reusable lemma/obstruction handoff only.

## 1. Finite-type replica-pressure lemma

Let `nu` be a full-support law on a fixed finite state space `Y`, and let `K:Y x Y -> R` be symmetric with `K nu=0`. For a probability law `pi` on `Y`, define

`Q_K(pi)=sum_{y,y'} (pi-nu)(y)(pi-nu)(y')K(y,y')`.

If for some `kappa<infinity`

`Q_K(pi) <= 2 kappa D(pi||nu)` for every `pi`,

then for iid `Y_1,...,Y_n~nu` and any fixed `c` with `c kappa<1`,

`sup_n E exp[(c/n) sum_{i<j}K(Y_i,Y_j)] < infinity`.

Proof mechanism: write the pair sum in terms of the empirical type `hat_nu_n`, absorb the diagonal term into an `O(1)` factor, then use

`sup_n E exp[gamma n D(hat_nu_n||nu)] < infinity` for every `gamma<1`.

The last estimate is elementary from Stirling plus a local Gaussian lattice sum.

This is directly reusable whenever a Gaussian/tensor problem can be reduced to a finite empirical overlap type.

## 2. Local covariance is not automatically enough

If `K` is the replica kernel, the local Hessian at `nu` is its covariance-normalized operator. Low-degree cycle/contraction moments naturally control this local operator. But the all-test `chi^2` partition function depends on the global ratio

`sup_{pi != nu} Q_K(pi)/(2D(pi||nu))`.

These can differ.

Explicit warning example: for the `q`-state Potts kernel

`W_q(a,b)=q 1_{a=b}-1`,

the one-replica operator has spectral radius `1`, while the diagonal two-replica type `pi_diag(a,b)=q^{-1}1_{a=b}` gives

`Q_K(pi_diag)=q-1`,  `D(pi_diag||nu)=log q`.

Hence the global entropy-overlap ratio is at least

`(q-1)/(2 log q)`,

which exceeds the local spectral value for `q>=4`.

Interpretation: a first-order/nonlocal overlap state can defeat a proof based only on covariance or the Hessian at zero, even though every local spectral direction is subcritical.

## 3. Gaussian/tensor target

The exact Gaussian mean-mixture identity from the prior handoff remains

`1+chi^2(T_rho P||gamma_m)=E exp[rho^2 <b(Z),b(Z')>]`.

The new lesson is what kind of estimate should close it. Seek a sharp entropy-energy or sub-Gaussian inequality for the overlap random variable/state that controls the **whole exponential moment**, not just

`Var(<b(Z),b(Z')>)`

or the largest covariance eigenvalue.

Useful sufficient forms include:

- a log-Sobolev/transport inequality turning overlap energy into relative entropy;
- a global quadratic MGF bound matching the local covariance constant;
- a model-specific variational inequality ruling out nonzero overlap maximizers.

For tensor type-2 work, the analogous failure mode is a rare coherent tensor-overlap state whose entropy cost is lower than the gain predicted from local chaining/covariance calculations.

## 4. Scope warning

This handoff does not claim that P08 or P09 satisfies the required global entropy-energy inequality. It identifies the exact extra obligation created by moving from local/covariance control to an all-test replica-pressure conclusion. Preserve RS-2026-CL-A ownership of the low-degree source claim.
