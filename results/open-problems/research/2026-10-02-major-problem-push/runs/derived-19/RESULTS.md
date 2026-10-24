# Derived-19 research result: first non-cactus stable apex block

## Completed theorem

Let the degree-three-side vertices of `K_{2,3}` be `0,1`. Give the three
backbone edges incident with `0` activity `p>0` and the other three activity
`q>0`. After adjoining an apex with five independent spoke variables, the
full multivariate forest polynomial is real stable for every `p,q>0`.

Thus, for arbitrary nonnegative spoke profiles, the whole apex-spoke
marginal is strongly Rayleigh and negatively associated under spoke external
fields and positive-probability spoke cylinder conditioning. Every
one-profile specialization has only strictly negative real zeros. Combining
this with the already audited four-core transfer proves negative correlation
of the two disjoint external marked edges with four proportional spoke rows,
at every positive pair of marked activities. Strictness is exactly four
positive row scalars and at least two positive profile entries.

This is the first completed theorem in the campaign for a 2-connected block
with two independent cycles. It strictly exceeds the cactus class from
derived-18. It does not solve the full forest negative-correlation problem.

## Analytic certificate

The internal `S_3` symmetry leaves four spoke-pair orbits. For each orbit,
the Rayleigh difference is collected as a quadratic in one of the other
variables. After shifts by `p+q+1` for internal spoke variables and by
`3p+1,3q+1` for the endpoints, the leading coefficients and negative
discriminants reduce to four explicit positive-definite binary forms.

Two forms have displayed positive eigenvalues. The other two have positive
diagonals and determinants

    p^2 q^2 (p+q+1)(2pq+p+q+1)

and

    8p^2 q^2 (p+q+1)(3pq+p+q+1).

Every zero-leading-coefficient boundary is evaluated explicitly. The
multiaffine Rayleigh characterization then gives real stability at all real
specializations, not merely real-rootedness on profile rays.

## Exact verification and independent audit

The author checker enumerates all `2^11` augmented-edge subsets, retains 712
forests, reconstructs all 32 spoke monomials, and verifies 18 coefficient,
discriminant, boundary, and positive-form identities over `Q[p,q,z]`.

The fresh independent audit **PASSes**. Its implementation imports no author
code and instead enumerates the 54 backbone forests and expands the product
`product_C(1+sum_(i in C)z_i)` over their components. It independently
checks the same 18 symbolic certificates, 24 exact rational profile/root
cases, and six directly enumerated full marked graphs (four strict, two
equality), with zero counterexamples. The audit caught and repaired the
needed positivity qualification on marked activities and two stale wording
items; no analytic identity required correction.

## Routes that remain open

The cactus one-terminal determinant gluing does not immediately extend to
two-terminal parallel composition because the normalized two-terminal Gram
matrix is network-dependent. Six unrelated activities destroy the four-
orbit symmetry and remain unproved. A deterministic numerical countersearch
tested 120 such weight vectors, all ten spoke pairs and 30,000 real points
per pair (36,000,000 Rayleigh evaluations); it found no negative value. This
is explicitly archived as numerical evidence only, not a theorem.

Arbitrary theta subdivisions, general series-parallel backbones, backbone
cylinder conditioning, nonproportional rows, and negative association jointly
with backbone or marked edges remain open. Full forest negative dependence,
full Boolean FEI, unrestricted ML10 Sidorenko, and Kaplansky/direct
finiteness also remain open in this campaign.

## Prior-art status

Borcea--Branden--Liggett supply the Rayleigh stability criterion and
strong-Rayleigh implications. Huang and the current 2026 forest papers are
credited for the broader conjecture and established regimes. Targeted
primary-source searches did not locate this exact side-uniform `K_{2,3}`
apex-stability theorem. That bounded search is not a novelty certification;
historical priority and external specialist review remain unverified.
