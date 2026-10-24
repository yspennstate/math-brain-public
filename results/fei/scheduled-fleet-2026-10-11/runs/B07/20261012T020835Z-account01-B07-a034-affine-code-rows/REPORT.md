# B07 / A034 — affine-code row payment for the full conditional term

**Status:** `PROVED RESTRICTED THEOREM / INDEPENDENT REVIEW PENDING / FULL FEI OPEN`

## Mathematical movement

The latest durable A034 result bounded every conditional spectral fiber by an anchored-tail complexity. It paid one-point defects but left the averaged anchored cost open. A separate unsaved granularity calculation was reconciled and found already present in that theorem's marginal term, so it was not counted as a new attempt.

This run changes mechanisms. It identifies a growing, exact Boolean row class on which the complete conditional term is paid by physical `Y`-influence with constant four.

For

`a_R(y)=E_x f(x,y) chi_R(x)` and `p_R=E_y a_R(y)^2`, assume every positive row has constant magnitude and normalized sign `sigma_R=a_R/sqrt(p_R)`. Require each nonconstant `sigma_R` to equal `1-2 1_A` for an affine-subspace coset `A` of the physical `Y` cube. Then the conditional spectral fiber is exactly `q_R=hat(sigma_R)^2`, and

`H(S_Y|S_X) <= 4 sum_R p_R I(sigma_R) = 4 I_Y(f)`.

Combining this with the existing Boolean-granularity marginal theorem gives

`H(f) <= (4+2/ln 2) I_Y(f) + 2(d-1) - E_y Gamma_d(f_y)`.

The full conditional entropy is retained and paid. No arbitrary spectral law and no correlated physical input distribution is introduced.

## Exact code calculation

If `A=z+V` has codimension `k`, density `delta=2^-k`, and dual code `W=V^perp`, then `sigma=1-2 1_A` has squared spectrum

- mass `(1-2 delta)^2` at the empty set;
- mass `4 delta^2` at every nonzero word of `W`;
- zero elsewhere.

Thus, for `epsilon=4 delta(1-delta)`,

`H(sigma)=h2(epsilon)+epsilon log2(2^k-1)`.

If `r` physical coordinates are active in `W`, each occurs in exactly half its codewords, so

`I(sigma)=2 r delta >= 2 k delta`.

The anchored-tail estimate yields `H(sigma)<=8 k delta` for `k>=3`, hence `H(sigma)<=4I(sigma)`. The cases `k=1,2` are exact. Dense codes only improve the payment because `r>=k`.

## Tensor and obstruction tests

- **Arbitrary tensors:** for `f(x,y)=u(x)g(y)`, every normalized positive row is `±g`; the condition rejects arbitrary `g` immediately.
- **Repeated admissible cores:** a positive-entropy affine defect has `k>=2`. The negative density of its square is `(2^k-1)/2^(2k-1)`, not a reciprocal power of two, so the square is not an affine-subspace defect. Characters (`k=1`) are the only repeatable case and have zero entropy.
- **Rare restrictions:** the theorem retains the rare density and pays it by the exact code boundary; no fixed Rényi charge remains.
- **Near tensors:** `u(X)sigma(Y)` is admitted for every Boolean `u` and every affine-code defect `sigma`; the conditional payment is exact at the row level.
- **Addressing and generic prime gates:** they can fail constant row magnitude and are explicitly outside the theorem.
- **Boolean realizability:** every admitted fiber comes from a physical Boolean row sign. This is stronger than specifying a probability law with correct normalization.

## Verification

`verify_affine_code_rows.py` exhausts every linear subspace of `F_2^n` for `1<=n<=5` and every affine coset. It checks the exact Walsh spectrum, support, Parseval identity, active-coordinate weight sum, influence formula, the constant-four entropy bound with outward rational logarithm intervals, and the tensor-density guard. It also checks named full Boolean tensors with distinct `X` factors and dense dual codes.

Command:

`python3 verify_affine_code_rows.py`

The all-dimensional theorem is the analytic proof in `CONDITIONAL_PHASE_THEOREM.tex`, not a finite extrapolation.

## Exact remaining obstacle

The row condition is strong. A universal result would need a Boolean-stable decomposition of arbitrary rows into affine-code-like packets, or a stopping rule that pays the residual packet entropy once. No such decomposition is proved here, so full FEI remains open.

## Provenance

- Source plan head read before this run: `807cae6b6bb0849a3328c95ef9278078e8d82894`.
- B07 compact contract blob: `2402180c94777484a0f41d5f13a9e01059107569`.
- Durable predecessor: `B07-A034-ANCHORED-TAIL-v1`, run `20261011T230712Z-account01-B07-a034-anchored-tail`.
- Reconciled local granularity report SHA256: `a6b8c50a21862388138eec7509ff57db53c3d65f561c2736d054f0594c230147`; it was treated as prior marginal input, not new movement.

No independent review or full-FEI resolution is claimed.

