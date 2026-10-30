# Uniform-kernel controls and scope

All analytic inequalities are in `UNIFORM_KERNEL_PAYMENT.tex`. The checker is development evidence only.

## Mandatory regimes

- **Balanced child (`mu=0`)**: the envelope retains exactly one `q psi(alpha)` term. It does not replace the singular cost by `O(alpha^2)`.
- **Fixed nonzero bias and exact collision**: the signed near-region inequality retains the negative term `-alpha^2 b_T^2 k(|mu|/|alpha|)`. The genuine `mu=1/2`, `Z=1/4` family remains a refund through `n=16`.
- **Simultaneous transition (`mu=c alpha`)**: the proof is scale exact and uses no fixed-bias Taylor expansion. Its constant is independent of `c`.
- **Near collision (`|a_T+mu b_T|<=c|alpha b_T|`)**: the entire near contribution is bounded by `alpha^2 b_T^2[k(c)-k(|mu|/|alpha|)]`; it is nonpositive once `|mu|>=c|alpha|`.
- **Parity-zero erasure**: `alpha=0` gives `R_mu(0)=0` exactly.
- **Rare-switch/adaptive chains**: the fixed-source theorem uses exact reach weights and the prior physical pivotal-event packing. No per-level payment is present.
- **Whole-set addressing**: adaptive query choice is allowed. The theorem requires only physical nonreuse on each path.
- **Actual prime Boolean gates**: the coefficient bound uses only that `a+b` and `a-b` are genuine Boolean signs. Every ordered Boolean two-variable branch pair was included in the finite controls.
- **Shared-variable interference**: no overlapping-input theorem is claimed. The child block is disjoint, and the outer pair is fixed in the proved hierarchy theorem.

## Newly isolated reserve

The only additional source term in the complete fixed-source bound is

`M(a,b)=2 sum_{b_T!=0} b_T^2 log_+(|a_T|/|b_T|)`.

It obeys `M(a,b)<=E_raw(b)`. A family with `M<=L q` has a depth-, bias-, and collision-uniform coherent-remainder constant `L+4+2 ln 2+2/e`. For a changing outer witness, the unpaid quantity is the single weighted reserve `sum_v w_v alpha_v^2 M(a_v,b_v)`.

