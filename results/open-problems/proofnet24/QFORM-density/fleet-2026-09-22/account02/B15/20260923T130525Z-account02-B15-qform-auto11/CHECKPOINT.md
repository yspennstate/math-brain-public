SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T13:05:25Z.
attacking: independently verify the moving-sheet rough-input closure, then combine it with a new quantitative truncation/compactness obstruction that keeps essential height separate from continuity.

# Early substantive checkpoint: weak trace is not normalized small-ball trace

The full QFORM theorem remains open. This checkpoint records a target-valid obstruction to strengthening the latest account03/B15 weak-limit trace theorem.

Use the completed account03/B15 phase-aligned family at math-open-problems@a5094ce57d028af28c2c114f92ca26ac277d4cec. For every s>=2 there is a smooth compactly supported cap-one density f_s on (1,10) such that, for three iid coordinates and the fixed target A=I_3,

Q_s=X_{s,1}^2+X_{s,2}^2+X_{s,3}^2

has a smooth density p_s supported in (3,300), ||p_s||_infinity<=1/2, and

|hat p_s(s)|>=27/64.

Choose s_j->infinity and then a subsequence, still denoted s_j, for which the one-dimensional source laws converge weakly to a law mu on [1,10]. Cap-one laws are weakly closed, so mu has a density f<=1. The triple products converge weakly and hence the Q_s laws converge weakly to the law rho of Q=X_1^2+X_2^2+X_3^2 with iid X_i~mu. By the latest completed partner trace theorem at math-open-problems@be22adf9f67e9fa02063418c000bc5ee2d2d0c43, rho is atomless and

sup_{a<=b}|rho_j((a,b])-rho((a,b])| ->0.

Let p be the density of rho. Because f is supported in [1,10], the density h of X^2 lies in L^1 cap L^infinity, has support [1,100], and ||h||_infinity<=1/2. Hence p=h*h*h is a bounded continuous compactly supported density, with ||p||_infinity<=1/2. Riemann-Lebesgue gives hat p(s_j)->0. Therefore

liminf_j ||p_{s_j}-p||_1 >= liminf_j |hat p_{s_j}(s_j)-hat p(s_j)| >=27/64,

and, since both densities are supported in [3,300],

liminf_j ||p_{s_j}-p||_infinity >=27/(64*297).

More sharply, let r_j=pi/(2s_j) and beta_r=(2r)^(-1) 1_{[-r,r]}. Then hat beta_{r_j}(s_j)=2/pi and

((p_{s_j}-p)*beta_{r_j})(y)
=[rho_j([y-r_j,y+r_j])-rho([y-r_j,y+r_j])]/(2r_j).

Its Fourier coefficient at s_j has asymptotic magnitude at least (2/pi)(27/64), while its support length is at most 297+2r_j. Consequently

liminf_j sup_y |rho_j([y-r_j,y+r_j])-rho([y-r_j,y+r_j])|/(2r_j)
>=27/(9504*pi)>9.0e-4.

Thus the partner theorem's uniform UNNORMALIZED interval-profile convergence is essentially the correct weak-limit statement: even inside the exact target, with fixed A=I_3, common compact support, smooth approximants, a continuous bounded limit density, and a common height cap 1/2, normalized shrinking-interval profiles need not converge. A common estimate rho_j(I)<=C|I| still passes to the limit exactly; what fails is any attempt to obtain that estimate from weak convergence plus continuity or density convergence.

Next in this run: verify the ruled one-sheet rough-input/moving-sheet bridge at its exact source scope, then write the combined final report and explicit remaining implication.