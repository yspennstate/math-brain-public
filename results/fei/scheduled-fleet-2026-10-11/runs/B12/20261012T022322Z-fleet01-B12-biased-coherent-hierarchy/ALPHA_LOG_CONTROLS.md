# A057 alpha-log and biased-collision controls

Status: the adaptive nonreusing alpha-log payment and the biased-child identity are **PROVED**. The complete coherent-remainder hierarchy and full FEI remain **OPEN**.

All entropy expressions in this run use natural logarithms.

## Exact movement

The preceding run proved only the simultaneous first-layer bound

`sum_i alpha_i^2 ln(1/alpha_i^2) <= (2/e) I(h)`.

This run extends it to every deterministic adaptive restriction tree that never queries a physical coordinate twice on one path:

`sum_v w_v alpha_v^2 ln(1/alpha_v^2) <= (2/e) I(h)`.

Here `w_v` is the exact uniform probability of reaching node `v`, and `alpha_v` is the queried singleton Fourier coefficient of the restricted Boolean function. The proof groups nodewise pivotal events by the original physical coordinate. This removes any depth factor and allows the queried coordinate to depend on previous restriction outcomes.

## Biased-child correction

For `F=a+h b`, child mean `mu`, queried singleton `alpha`, and `q=||b||_2^2`, the exact split is

`D_i(F)=q D_i(h)+R_mu(alpha)`

with

`R_mu(alpha)=Eraw(a+mu b)+Eraw(alpha b)-[Eraw(a+(mu+alpha)b)+Eraw(a+(mu-alpha)b)]/2-q K(mu,alpha)`.

The scalar correction `K(mu,alpha)` is mandatory. Dropping it incorrectly treats a biased restriction as another balanced child.

If `t_T=a_T/b_T`, then

`R_mu(alpha)=sum_{b_T != 0} b_T^2 [K(t_T+mu,alpha)-K(mu,alpha)]`.

## Collision asymptotics

Let

`Z_mu=sum_{b_T != 0, a_T+mu b_T=0} b_T^2`.

For fixed nonzero `mu`,

`R_mu(alpha)/(alpha^2 ln(1/alpha^2)) -> -Z_mu`.

At exact balance,

`R_0(alpha)/(alpha^2 ln(1/alpha^2)) -> q-Z_0`.

Thus fixed bias cancels the positive leading rare logarithm; exact spectral collisions supply a negative refund. This is not uniform when `mu=O(alpha)` or a collision gap tends to zero with `alpha`. The identity `K(c alpha,alpha)=alpha^2 K(c,1)` isolates that transition.

## Counterexample and stress-test matrix

- **Parity-zero erasure:** zero singleton coefficients contribute zero in the tree theorem.
- **Rare restrictions:** exact node weights appear; no node is charged as though it had probability one.
- **Whole-set addressing:** adaptive coordinate selection is allowed, and payment is grouped by physical pivotal events.
- **Near tensors:** no tensor additivity of raw collision entropy is invoked.
- **Shared-variable interference:** no overlap closure is claimed; the composition corollary requires a fixed outer pair on a disjoint child block.
- **Activation equivalence:** the fixed factor `q` multiplies both the log payment and the exact child influence contribution.
- **Actual prime Boolean gates:** the theorem is stated for arbitrary Boolean truth tables without a formula decomposition.
- **Balanced logarithmic obstruction:** preserved. At `mu=0`, the positive coefficient is `q-Z_0`, so the reviewed AND2 control still rules out pointwise `O(alpha^2)` replacement.
- **Biased collision refund:** an explicit four-input Boolean outer gate and genuine biased children give `Z_{1/2}=1/4` and ratio tending to `-1/4`.

## Remaining exact obstruction

Stable gap `B12-A057-COHERENT-HIERARCHY` is now narrowed to a uniform two-parameter interference estimate. The unpaid object is the complete sum of `R_mu(alpha)` when:

1. `mu` can approach zero at the same scale as `alpha`;
2. spectral gaps `a_T+mu b_T` can approach zero with the restriction depth; and
3. the outer activation witness can itself change with the restricted variables.

The next attempt should partition coefficients into `|a_T+mu b_T| <= c|alpha b_T|` and its complement. The near-collision part has an exact signed refund candidate; the separated part admits Taylor control. Any proposed bound must be summed with the adaptive pivotal-event ledger, not once per level.

