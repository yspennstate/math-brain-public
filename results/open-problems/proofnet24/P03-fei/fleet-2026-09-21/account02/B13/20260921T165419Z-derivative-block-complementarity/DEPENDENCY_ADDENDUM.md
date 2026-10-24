# Fresh B12 dependency addendum — equality rows make the hybrid-basis target exact

After the main B13 report was committed, the fresh account02/B12 run `20260921T165622Z-depth-rigidity-obstruction` became visible. It proves that equality in B12's sharp derivative-Palm mean-depth bound forces the derivative to be a constant-sign indicator of a subcube. This sharpens the interpretation of the B13 mixed-basis bank `R` and gives an exact solvable endpoint for the next hybrid-basis step.

Let the derivative cube have `m` coordinates and suppose the B12 equality case holds:

\[
g=\sigma 1_E,
\]

where `E` is a subcube fixing a coordinate set `F` of size `r`; write `U` for the `m-r` free coordinates. After normalization, up to the fixed computational bits and a global sign,

\[
|\psi\rangle
=\bigotimes_{j\in F}|z_j\rangle_Z
\otimes
\bigotimes_{j\in U}|+\rangle_X.
\tag{A.1}
\]

Now take a block `J` and put

\[
a=|J\cap F|,\qquad b=|J\cap U|,\qquad q=a+b.
\]

Because (A.1) is a product state, the B13 entanglement bank vanishes:

\[
E_J=0.
\]

The all-physical (`Z`) projection is deterministic on the `a` fixed coordinates and uniform on the `b` free ones, so

\[
C^{\rm phys}_J=2^{-b}.
\]

The all-spectral (`X`) projection is uniform on the `a` fixed coordinates and deterministic on the `b` free ones, so

\[
C^{\rm spec}_J=2^{-a}.
\]

Substitution into the exact B13 conservation law gives

\[
\boxed{
R_J
=1+2^{-q}-2^{-a}-2^{-b}
=(1-2^{-a})(1-2^{-b}).
}
\tag{A.2}
\]

Thus `R_J` can be close to one **even at exact equality in B12's Boolean depth theorem** whenever the block mixes many fixed and many free coordinates. This is not hidden complexity or entanglement. It is purely an axis-mismatch cost caused by measuring the whole block in one basis.

But the coordinatewise hybrid measurement that uses `Z` on `F` and `X` on `U` is deterministic on the entire equality state. Its collision probability is exactly one. Hence the next B13 target is not merely aesthetically natural: the B12 equality classification identifies the exact orientation that removes the whole `R` bank at the rigid endpoint.

This yields a sharper stability programme. If B12's depth defect

\[
\Delta_i=\mathbb E[Z\mid X=i]-\tfrac12\log_2(1/j_i)
\]

is small, its new identity

\[
\operatorname{Slack}_{\rm sign}+\operatorname{Slack}_{\rm iso}=4j_i\Delta_i
\]

says the derivative support is nearly subcube-like and has little internal sign-change energy. The B13 question can therefore be formulated quantitatively:

> Does small `Delta_i` imply the existence of a coordinatewise `Z/X` orientation whose hybrid dephasing captures all but `O(Delta_i)` (or another dimension-free function of `Delta_i`) of the reduced-state Hilbert--Schmidt mass, uniformly across a suitable random-block hierarchy?

At `Delta_i=0`, (A.1)--(A.2) prove the answer is exactly yes. For large `Delta_i`, B12 hopes to spend depth itself. The missing bridge is a stable hybrid-axis theorem, not an all-`Z`/all-`X` collision estimate.

This addendum does **not** prove that stability theorem and does not change the status of FEI: full FEI remains OPEN. It records the exact compatibility between the fresh B12 equality-rigidity theorem and B13's new block complementarity identity, and it avoids treating a large `R` value as evidence against the near-subcube route.
