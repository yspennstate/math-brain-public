# Encoding Interface Lemma: reconstruction from first principles (referee item (a), executed)

Author: main session c53c1d50, 2026-08-19 ~01:2x-01:4x. Status: the framework of §1 and its verification in §2 are elementary and checked here; §3's identification of the error terms is a reconstruction, labelled; §4 states what remains UNRESOLVED and why the declared fail-stop does not trigger. This executes part (a) of the single next work item adopted from `attacks/referee_iter1.md` §6.

Context: the dossier's endpoint bookkeeping, tag (25) — for a rank-r, size-k component the ternary basis-mass encoding has exponent −(n−r)ℓ + O(d_cb·k + (k−r)log r + r + n) — is cited in S1 line 461 as "the EXISTING ternary basis-mass encoding", i.e. its derivation lives in the earlier packet tree, which is not reproduced in the dossier and (like `recursive_paired_block_tree_entropy.md`) exists on no machine we control. The transfer lane's entire ladder (W1/W2/W3, the slice-mass bound) is priced against this tag. The referee declared: reconstruct it from displayed usage, or record the ladder as permanently conditional. This note reconstructs it.

## 1. The component framework, stated concretely

A singular sign matrix has a linear dependency among its rows. Fix the row set carrying it.

**Definition (component, reconstructed).** A *component* of B_n is a set S of k rows together with the fibre
  A := { column-restrictions of B to S } ⊆ {±1}^k,
i.e. the set of distinct sign patterns that the n columns show on those k rows. If the rows of S carry a dependency Σ_{a∈S} c_a·row_a = 0 then every column restriction lies in the hyperplane c^⊥, so A is contained in a proper subspace: rank(A) = r < k, corank j := k − r ≥ 1. Write the fibre's ambient defect
  ℓ := k − log₂|A|   (defect against the cube {±1}^k the restrictions live in).

**Probability of a given component.** The n columns of B are iid uniform on {±1}^n, so their restrictions to S are iid uniform on {±1}^k. Hence
  Pr( all n column-restrictions lie in A ) = ( |A| / 2^k )^n = **2^{−nℓ}**.
This is exact, needs no anticoncentration input, and is the only probabilistic ingredient.

**The union bound.** Singularity implies some component exists, so
  Pr(det B_n = 0) ≤ Σ_{(k, A-class)} N(k, A-class) · 2^{−nℓ(A)},
where N counts the components of that class — the *description count*. Everything deterministic in the problem enters here and only here.

## 2. Verification: the framework reproduces the conjectured constant exactly

Take k = 2 and A = {(+,+), (−,−)} (rows equal): |A| = 2, ℓ = 2 − 1 = 1, so each such component has probability 2^{−n} — the exact probability that two specified rows are equal. ✓
Count: C(n,2) row pairs × 2 fibres per pair (equal: {(+,+),(−,−)}; opposite: {(+,−),(−,+)}) = n(n−1) ≈ n². Columns contribute an identical n² by transposition. Total
  **(1+o(1)) · 2n² · 2^{−n}** — the conjectured value, on the nose.
So the framework is not an analogy: at k = 2 it *is* the mechanism that decides the constant (cf. `problem/layer3_interface_note.md` §1, derived independently). Any reconstruction that failed this test would be the wrong framework.

## 3. Reconstruction of tag (25): every term is a naming cost

Write −nℓ = −(n−r)ℓ − rℓ. In the endpoint range (k = O(n/log n), ℓ = O(log log n)) we have rℓ ≤ kℓ = O(n·log log n / log n) = o(n), so
  2^{−nℓ} = 2^{−(n−r)ℓ + O(n)} — matching (25)'s leading term with its O(n) slack. ✓
The remaining terms of (25) are exactly the cost of *naming* the component, i.e. log₂N:
- **d_cb·k** — naming the fibre A. A coordinate basis from A's full dual plus a signed selector per coordinate, with all residuals inside one d_cb-dimensional space, names A with O(d_cb) bits per coordinate over k coordinates. This is the ONLY place the deterministic quantity enters, and it enters as a code length.
- **(k−r)·log r = j·log r** — naming the relation structure (j independent dependencies, each specified within the rank-r span).
- **r** — naming the rank-r basis itself.
- **n** — naming which rows carry the component (log₂C(n,k) = O(k log(n/k)) = O(n) in the endpoint range) plus the rℓ slack above.

**Interface Lemma (reconstructed).** For any injective, in-field-decodable description scheme D of components, a component described in |D| bits contributes at most 2^{−(n−r)ℓ + O(|D| + j log r + r + n)} to the union bound of §1; a family of components of log-cardinality Λ contributes at most 2^{Λ − (n−r)ℓ + O(j log r + r + n)}.
*Proof.* §1's probability is exact and independent of how the component is described; summing over an injectively-described family multiplies by the family's cardinality, whose logarithm is the description length. ∎ (This is a one-line union bound; its content is entirely in §1's framework being the right one, which §2 tests.)

**Consequences, as the transfer lane predicted:**
- **W2 CONFIRMED at framework level**: the deterministic input enters only through code length. A rank certificate d_cb ≤ γℓ is one code among many (length O(γℓ + log r) per row).
- **W3 CONFIRMED at framework level**: index codes into an enumerated subfamily are lawful descriptions, so "certify OR count" is a genuine disjunction, and counting routes carry no absorption obligation (nothing per-generation is being charged — a description is written once).
- The transfer lane's *risk 1* (that a centered-moment expansion might consume the deterministic input through something finer than length, via cancellation) is answered structurally: §1's bound is a one-sided union bound, and per `layer3_interface_note.md` §2 the hard direction of the sharp conjecture is precisely one-sided. Cancellation is not needed and buys nothing here.

## 4. What remains UNRESOLVED — and why the fail-stop does not trigger

The honest gap in the reconstruction is a *parametrization* question, not a structural one. The dossier defines ℓ(A) = r − log₂|A| for a **spanning** fibre A ⊆ {±1}^r, whereas my §1 fibre is non-spanning in {±1}^k by construction (it lies in the dependency hyperplane), with defect measured against the ambient k. The two agree after the packet's own reduction machinery (delete zero Gale columns, pass to the Gale/relation dual — the "relation corank j = k − r" and "Gale-flag layer" language says exactly that their bookkeeping is on the dual side), but I cannot *derive* that correspondence from the dossier text: the reduction lemmas are in the same missing tree as (25) itself.

Consequently:
- **The structural claim is discharged**: the endpoint sum is a union bound over described components, d_cb enters only as a naming cost, and index codes are lawful. That is the whole content W2/W3 need, and it is now supported by an independent reconstruction that reproduces the conjecture's constant exactly.
- **The constant-level correspondence stays UNRESOLVED**: whether the packet's ℓ in (25) is my ambient defect or its Gale-dual image, and hence whether their O(·) constants transfer verbatim to my framework, cannot be settled from available text. Named question that resolves it: *is the packet's fibre the column-restriction set of the row component, or its Gale dual?* One sentence of the missing tree would answer it.
- **Fail-stop disposition (per referee §6(c)):** the declared trigger was "if (25)'s derivation cannot be honestly reconstructed from available text". It CAN be, at the level that the ladder depends on. So the fail-stop does NOT fire, and W2/W3 are upgraded from CONDITIONAL to **RECONSTRUCTED (structural), constants unverified**. They are not "dossier-grade" — that phrase should not be used — and the demotion clause is not invoked.

## Strongest case this is wrong

1. **My framework may not be the packet's.** If their components are Gale-dual objects with a different probability model, then my §1 exactness does not transfer and my identification of d_cb·k as fibre-naming is a coincidence of shape. Against this: §2's exact reproduction of 2n²2^{−n}, and the fact that all four error terms in (25) have natural naming interpretations in my framework with none left over. The check that would decide it: any statement in the earlier tree defining the fibre of a component.
2. **The union bound may be lossy exactly where it matters.** §1 sums over ALL components, and a singular matrix has many (every dependency, every subset of a dependent row set). Overcounting inflates the sum by the number of components per singular matrix; at the endpoint this could be the difference between o(n²2^{−n}) and Θ(n²2^{−n}). The packet's centered-moment machinery may exist precisely to control that multiplicity. This does not damage the interface reading (multiplicity is still a counting question) but it means my §1 is a first-moment sketch, not the packet's actual argument.
3. **The F_p version.** §1 is stated over the reals. The packet requires uniformity over odd F_p (p > q); the same counting works verbatim over F_p for the fibre-membership probability, but "dependency ⇒ non-spanning fibre" needs the field's characteristic to be odd for +1 ≠ −1, which is assumed throughout — worth a referee's eye, not obviously a problem.
4. **Endpoint-range arithmetic.** rℓ = o(n) uses k = O(n/log n) and ℓ = O(log log n). At the class ceiling ℓ can be much larger (the basis-mass cap allows ℓ ≲ rj/n); there rℓ may exceed the O(n) slack and the rewriting −nℓ = −(n−r)ℓ + O(n) fails. So the reconstruction is verified in the *endpoint window*, which is where the ladder is used — but it is not universal, and any use outside that window must redo the arithmetic.
