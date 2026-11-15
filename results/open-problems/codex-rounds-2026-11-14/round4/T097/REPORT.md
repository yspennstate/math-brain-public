VERDICT: PARTIAL a non-shell capacity bound and a larger relative crossover coefficient

The predecessor's shell optimization and coefficient (log 2)^2/32 hold
under independent verification. The brief web check found no lattice
resolution; the recent papers opened concern the cable system.

The new piece is a deterministic capacity estimate outside the predecessor's
restricted class. In SRW Green normalization, PROOF.md proves for R>=1

    cap(B_R) <= C_cube (R+1/2),
    C_cube = 2 pi delta/[3 log((3+delta)/(3-delta))],
    delta = sqrt(9-24/pi),
    C_cube <= 8/9+2 pi/3 < 3.

The proof averages continuum trial functions over unit cells to obtain
an exact upper bound on lattice energy. It then optimizes profiles depending
on Euclidean distance from the enlarged cube. This strictly improves the
earlier bound A_R>4R at every R>=2. At R=1 either bound can be used.
Optimality is asserted only within the specified continuum profile class,
not for actual cube capacity.

For exactly the same radius as before,

    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2},

the improved consequence is

    liminf_{t->0} t^2 log(1/t) L_rel(t)
        >= (log 2)^2/(8 C_cube) > (log 2)^2/24.

This improves the previous guaranteed coefficient by a factor 4/C_cube>4/3.
It uses the same existing density theorem of Stephen Muirhead,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10, without using its excluded endpoint. The power and logarithmic
loss are unchanged.

AUDIT.md rechecks the geometric factors through the volume of a parallel
body, the exact integral by completing the square, the variational profile
by its Euler equation, and the crossover coefficient with Gaussian tails
instead of Holder. It checks finite support, nonsmooth boundaries, all
smaller radii, and the half-cell enlargement. No numerical computation,
decimal evaluation, simulation, or mathematical script was needed or run.

Commands: predecessor files were read with
`OMP_NUM_THREADS=1 nice -n 15 cat <absolute paths>`; source files were
discovered with `rg --files`. Final verification uses
`OMP_NUM_THREADS=1 nice -n 15 sh -c '<file checks>'`, recorded verbatim
in LOG.md. The sandbox denied priority changes, so no numerical workload
was launched. All authored files are in this folder. Earlier folders
were read only; there were no subagents, git operations, or external writes.

What failed or remains uncertain: this does not give a connection-specific
score bound or remove the logarithm. It does not compare L_rel to a
conventional correlation length. No exact lattice exponent, exponent
existence, critical nonpercolation, or equality with cable exponents is
proved. The true leading cube capacity coefficient and novelty of the
elementary estimate are not established.

Next worker: use the exact unit-cell transfer in PROOF.md section 2 if
sharper geometric bounds are useful, but further constant improvements
alone will not remove the logarithm. The substantive missing estimate is
still a connection-specific bound on -d/dh log p_R(h), of order sqrt(R)
uniformly for h in [h_*,h_*+c/sqrt(R)], or a comparison with a specified
crossing or two-point length. Neither is supplied here.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first retained local clock reading 04:49:23 +04
(Asia/Tbilisi).
