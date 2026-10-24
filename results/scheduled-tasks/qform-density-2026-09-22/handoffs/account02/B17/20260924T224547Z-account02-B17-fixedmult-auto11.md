SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T22:45:47Z.
attacking: fresh fixed-multiplicity source audit and the full-rank multiplicity-four rank-two-crossing obstruction.

Historical 790-line source commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, blob
183ccd294763214e6a707e8d4749ff9a8cf7006d, declared SHA-256
9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69: PASS on a fresh complete read.
Earlier B17 labels are corrected: the projection phrase “factors with b_i=0 are at most one” refers to factor values,
not the number of rows; and the historical hyperbolic “same way using w instead of u” repeats the coordinate choice.

Latest five-paper source at commit 5ba2a4d6b689721601cce7ec7e22ffea9fa98f90, paper blob
bbebd6f6c5a27e9f639186a305008ab43a481e70, manifest SHA-256
040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3: PASS. It now chooses i and i' explicitly.
The current theorem is s5 density <=270 K^2/s; s3 gives only the 77 K/sqrt(s) full negative-half-moment bound.
lean/QformFive3.lean now covers the finite-dimensional Proposition 6.4 random-sign/spectral route with recorded rc=0.

New B17 witness: for 0<tau<1/16 and even N>256(1+tau), choose a two-row C with
CC^T=(1+tau)I_2 and entries of squared magnitude (1+tau)/N, and set
A=[[0,C],[C^T,tau I_N]]. Then spec(A)={1+tau,1+tau,-1,-1,tau^(N-2)}, so s4=1 and A is full rank.
There is no five-paper pivot, and every coordinate crossing block has rank <=2, hence E3=0 for every cut.
Yet the original-coordinate two-hub receiver gives density <=e sqrt(pi) K^2/sqrt(1+tau) for arbitrary affine terms.
Thus full-rank/nonzero residual spectrum does not rescue the order-three-crossing route at multiplicity four.
This is a proof-mechanism counterexample, not QFORM.

General s4 density, general s3 density and unrestricted three-eigenvalue QFORM remain OPEN / NOT PROVED / NOT DISPROVED.

Canonical math-open-problems audit/improvement writes were attempted but blocked by the platform safety layer;
complete fallback conversation artifacts were produced.