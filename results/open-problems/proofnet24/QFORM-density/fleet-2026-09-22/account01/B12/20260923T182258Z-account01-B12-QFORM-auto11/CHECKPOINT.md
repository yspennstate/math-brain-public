SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T18:22:58Z.
attacking: commuting spectral-replacement square-defect stability — arbitrary same-eigendirection replacements of either sign are free unless they reduce squared eigenvalue magnitude; charge only the ordered destructive-square defect, then route the surviving six-mode carrier through account02/B12.

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN; execution `WITHOUT_VERIFIED_BRAIN`.

Early substantive calculation. Let A0 and C be real symmetric with [A0,C]=0, put B=A0+C, and choose a common orthonormal eigenbasis so A0 has eigenvalues lambda_j and B has eigenvalues mu_j. Define d_j=(lambda_j^2-mu_j^2)_+, sorted decreasing. Then

B^2 = A0^2 - N + P,

with N,P positive semidefinite, NP=0, and eigenvalues of N equal the d_j. Hence for every original-coordinate set H and every k,p with k+p<=|H|,

lambda_k((B^2)[H,H]) >= lambda_{k+p}((A0^2)[H,H]) - d_{p+1}.

Indeed compress N to H, use compression interlacing lambda_{p+1}(N[H,H])<=d_{p+1}, and apply Weyl to A0^2[H,H]=(A0^2[H,H]-N[H,H])+N[H,H]. If an additional arbitrary symmetric L has rank <=r and a dense symmetric T has ||T||op<=delta, then

sqrt(lambda_k(((B+L+T)^2)[H,H]))
>= [ max_p sqrt((lambda_{k+r+p}((A0^2)[H,H])-d_{p+1})_+) - delta ]_+.

This follows from rank-r singular-value interlacing on the full column restriction and then singular-value Weyl for T. Thus arbitrarily many commuting eigenvalue replacements with |mu_j|>=|lambda_j| cost exactly zero regardless sign or magnitude; only the ordered destructive square deficits are charged, plus rank of a hostile noncommuting packet and operator norm of a dense tail.
