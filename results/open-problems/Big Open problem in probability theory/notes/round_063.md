# Round 063 log

## Goal

Make the JSON bridge-certificate format closer to the actual finite-state
certificate theorem.

## Boundary vectors

The theorem uses nonnegative boundary vectors \(a,b\) in the majorization
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb.
\]
The verifier now requires `left_vector` and `right_vector`, checks that both
have the same dimension as `matrix`, checks nonnegativity, and rejects all-zero
boundary vectors.  The regular-tree toy certificate now includes
`left_vector = right_vector = [1]`.

This still does not verify the graph-specific bridge majorization itself.  It
only prevents malformed finite-state algebra certificates from passing the
exact Collatz--Wielandt audit.
