# fleet02/B12 r24 early checkpoint — collective-tail cross-core under dense tails and unbounded low-rank spectral additions

Status: supporting theorem in progress; full QFORM remains open.

Let `I,J` be disjoint ORIGINAL-coordinate sets and `M0=A0[I,J]`. Let `P` be an orthogonal projection on the I-row space with `max_i P_ii<=1/2`. Consider the final cross block

`M = M0 + L + E`,

where `rank(L)<=r`, `(I-P)L=0`, and `||E||op<=delta`. The intended application is `E=T[I,J]` for an arbitrary symmetric dense tail `T` with `||T||op<=delta`; no claim is made that `X^T T X` is probabilistically small. The term `L` may have arbitrary norm and either sign provenance; for a spectral update `sum_a tau_a v_a v_a^T`, it suffices that its cross compression has rank at most r and every `(v_a)_I` lies in `range(P)`.

Define

`a1=(s_{r+1}(M0)-delta)_+`,
`a2=(s_{r+2}(M0)-delta)_+`,
`B^2=sum_{k>=r+3}(s_k(M0)-delta)_+^2`,
`epsilon0=||(I-P)M0||op`.

Rank-r singular-value interlacing followed by Weyl gives, for every `j`,

`s_j(M)>= (s_{j+r}(M0)-delta)_+`.

Therefore `s1(M)>=a1`, `s2(M)>=a2`, and the final collective tail satisfies

`T2(M)=sum_{j>=3}s_j(M)^2 >= B^2`.

Also `(I-P)L=0`, so

`||(I-P)M||op <= epsilon0+delta`.

Consequently, if `a2>0`, `B>0`, and

`epsilon0+delta <= B/15`,

then the completed volume-tail theorem in `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `PEER_TAIL_EXTENSION.md`, applies to the ACTUAL final cross block and yields

`||p_Q||inf <= (9 sqrt(3) e / 2) (a1 a2 B)^(-1/3)`.

All self blocks, outside couplings and affine terms remain arbitrary in that theorem. Thus an arbitrarily large added spectral block can be free in magnitude when its physical cross-cut footprint is low rank and lies inside a protected low-leverage row subspace; the dense arbitrary-rank tail is paid only through `delta`.

Next step in this run: compose this terminal certificate with the designated fleet03/B12 r23 sharp scalar-Schur compiler, then record a concrete target-class family and the exact remaining structural implication.
