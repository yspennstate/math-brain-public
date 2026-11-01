# FEI continuation: universal affine one-step entropy bound

19 September 2026. **Full FEI remains OPEN.** Read `scheduled-continuation/runs/2026-09-19/2026-09-19T18-46-55Z__report.md` for the complete proof, consumed-source receipt, checks, and limitations.

## New proved statement

Let `Ifrak(f)` be minimum total influence over invertible binary linear changes of the input followed by multiplication by a character, equivalently the minimum-basis directional influence defined in the affine-variance work. Then every Boolean function satisfies

    D_cross(f) <= 6 Ifrak(f) <= 6 J(f) <= 6 I(f).

The proof chooses a basis/character attaining `Ifrak`, writes the spectral marginals as `q_i<=1/2`, uses the archived Walsh uncertainty bound `D_cross<=2H(S|S xor T)`, conditional-entropy subadditivity, and the scalar inequality

    2 h_2(q)-h_2(2q(1-q)) <= 3q,  0<=q<=1/2.

No independence among different spectral coordinates is assumed.

## Why this is not FEI closure

For the one-point defect `w_n`, the discounted derivative-chain sum of `Ifrak` divided by its initial `Ifrak` grows like `n/2`. Thus the one-step theorem cannot simply be summed along the derivative chain.

Two stronger potential inequalities survived the exact dimension-at-most-three tests but are **UNPROVED**:

    D_cross <= 4 [v + delta_Ifrak],
    Ifrak <= v + delta_Ifrak,

where `v=1-max_s fhat(s)^2` and `delta_Ifrak=2Ifrak-E_z Ifrak(f_z)`. Either is a high-priority proof/counterexample target; neither may be quoted as established.

## Preserved affine-variance results

The creator session immediately preceding this run proved and exactly checked the following positive statements before its GitHub write route became available here:

- the entire multiplicative-derivative variance cost satisfies `V(f)<=2I(f)`, with optimal constant two;
- `Ifrak` has a threshold-rank representation, tensorizes exactly on disjoint products, is invariant under surjective affine lifts, and has an explicit formula for monotone Boolean functions;
- a precisely specified class obtained from products of one-point clauses, quadratic phases, and arbitrary read-once ternary-majority formulas by jointly surjective affine parameter mixing satisfies `H<=4 Ifrak<=4I`; constant four is optimal for that class;
- the corresponding allocation chain on that class is at most `8 Ifrak`;
- variance alone cannot control arbitrary allocation entropy, and the exact shared-shift descendant pair law carries a nonzero covariance correction.

Those statements do not remove the class hypotheses and do not solve full FEI. The complete preserved package was re-executed in this run; its checker SHA256 was `bd8663f3c6e89464bba9c69280cd9209e5276eb724ea5540cc603ed1cbe02100`. The current immutable scheduled report records their scope and the new theorem; a future packaging pass may place the longer creator-session manuscript in the continuation folder without changing source status.

## Next action

Attack `Ifrak <= v+delta_Ifrak` first using exact Boolean signed-convolution constraints and the threshold-rank representation. Mandatory adversarial families: one-point defects, the coded scalar obstruction, balanced majority substitution, bent/quadratic phases, and rare-marker constructions. If it fails, preserve the smallest structural counterexample and identify the missing global resource. Full FEI source status remains OPEN.
