# Independent review of the exact three-core surcharge identity

Source: A029 run 20261014T025327Z-fleet05-A029-child-deficit-transport,
DERIVATION.md, sections "Two physical children and one nested reserve"
and "What would need a refund". Source SHA256 is recorded in
out/source_inventory.json. This identity has no separate A029 claim ID
in that run's CLAIMS.json; its copied A023 claim is NOT accepted wholesale.

Verdict: HOLDS for the displayed reserve decomposition, surcharge identity,
and terminal capacity bound. No repair supplied. No acceptance of the
unproved replacement of R_data by R_star in a general entropy inequality.

Independent reconstruction uses one oriented data edge at a time. Let
d_j be the pivotal indicator of core j on this edge. The product core
g_i*g_j is pivotal exactly when d_i XOR d_j is one. Thus, for pi equal
to (1-a,a(1-b),ab), the symmetric reserve per edge is
2 sum_{i<j} pi_i*pi_j*(d_i XOR d_j). If q=sum pi_j*d_j, this is exactly
2q(1-q), at most 2q. Averaging gives R_star<=2 I_terminal without
discarding any terminal, its reach weight, or any destroyed edge.

The outer reserve's data part is
2a(1-a)[(1-b)(d0 XOR d1)+b(d0 XOR d2)]. The physically reached inner
reserve is 2ab(1-b)(d1 XOR d2). In R_star the first two coefficients
are identical, while the last is 2a^2*b(1-b). Their difference is
2a(1-a)b(1-b)(d1 XOR d2). Integration proves the source identity exactly.
On B controls g0 is constant, so the outer product g0*h has precisely
the same pivotal indicators as h. Its additional reserve is therefore
2a(1-a)I_B, which is not terminal data capacity.

The current exact checker also verifies the identity on all 288 scoped
two-point bent-edit instances, independently of its entropy enclosures.
That finite check supplements the per-edge all-core proof above.

The first unsupported universal line remains replacing R_data by R_star
in an actual entropy bill without proving a signed refund. The new A021
DERIVATION supplies such a refund only for the explicit common-flat-
reference family, with control rate 18 rather than the source rate 11/2.
