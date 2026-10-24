SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T14:49:50Z.
attacking: optimize the fresh third-volume projection/tail certificate, then test it on a dense rotated indefinite matrix whose top singular subspace is maximally localized.

# Early substantive checkpoint

Fresh source reviewed: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md`.

Independent check so far: the exact third-volume marginal matrix `W` satisfies `0<=W<=I` and, using account01/B20's `T2 E2<=3 E3`, also `W <= (3/T2) M M^T`, where `T2=sum_{j>=3}s_j(M)^2`. Therefore for every orthogonal projection `P`, with `l_i=P_ii` and `eps=||(I-P)M||op`,

`sqrt(alpha_i) <= sqrt(l_i) + sqrt(3)*eps/sqrt(T2)*sqrt(1-l_i)`.

No commutation of `P` with `MM^T` is needed. I also re-derived the source Fourier constant: if all row marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`, then

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`;

the coefficient follows exactly from `b=3/(2q)` and Fourier inversion of `min(1,K|t|^{-b})`. No defect found in the new matrix/tail certificate or its constant at this checkpoint.

New optimization step: define

`H(P)=max_i (sqrt(P_ii)+sqrt(3)*||(I-P)M||op/sqrt(T2)*sqrt(1-P_ii))^2`.

If `H(P)<3/4`, choose the smallest admissible `q=max(1,2H(P))`. Since `q -> 3e/((3-2q)sqrt(q))` is increasing for `q>=1`, this is the optimal q furnished by this certificate. Thus every such P directly yields a continuous `C_0` density bound. In particular `P=0` gives `H(0)=3s1(M)^2/T2`; hence `T2>4s1^2` alone is a leverage-free Fourier exit, and `T2>=6s1^2` gives the clean q=1 bound

`||p_Q||_inf <= 3e E3(M)^(-1/6) <= 3e [s1^2 s2^2 T2]^(-1/6)`.

Next: apply this to an explicit dense Hadamard-rotated indefinite target and compare with the newly completed six-row complement-Hellinger B04 compiler.