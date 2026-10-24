# Sharp lower bound within the oblivious polynomial solver class

A05, 2026-10-23. Classical Chebyshev minimax mathematics, included to delimit valid optimality claims for T336. No new general transformer lower bound is asserted.

Fix 0<a<b, kappa=b/a, and T>=1. Consider estimators of A^{-1}f of the form p_{T-1}(A)f, where p is a polynomial of degree at most T-1 whose coefficients can depend on a,b,T but not on the instance A,f. An oblivious linear solver whose output lies in span{f,Af,...,A^(T-1)f} has this form. Here T counts residual degree, matching T updates from zero in C002; if one instead counts T explicit matrix-vector queries starting with f already available, the degree index shifts by one. Across all positive-definite symmetric A with spectrum in [a,b] and all f, its worst relative operator error equals

    max_{lambda in [a,b]} |1-lambda p_{T-1}(lambda)|.

The exact minimax value is

    E_T = 1 / Cheb_T((b+a)/(b-a))
        = sech(T arcosh((b+a)/(b-a)))
        = 2 rho^T/(1+rho^(2T)),
    rho=(sqrt(kappa)-1)/(sqrt(kappa)+1).                    (1)

Proof. Residual polynomials r(lambda)=1-lambda p(lambda) have degree <=T and satisfy r(0)=1. The scaled Chebyshev polynomial

    r_*(lambda)=Cheb_T((a+b-2lambda)/(b-a))
                  /Cheb_T((a+b)/(b-a))

attains +/-E_T at T+1 alternating points of [a,b]. If a competing r had strict uniform norm below E_T, then r-r_* would have alternating signs at those points and hence at least T distinct roots in (a,b). It also vanishes at zero, outside that interval. A nonzero degree-T polynomial cannot have T+1 distinct roots, contradiction. The explicit formula for Cheb_T outside [-1,1] yields (1).

Thus uniform relative residual <=delta<1 in this class requires and is achieved at

    T >= arcosh(1/delta)/arcosh((b+a)/(b-a)),

rounded up. For large kappa and small delta this is asymptotic to

    (sqrt(kappa)/2) log(2/delta).

This matches the leading Chebyshev solver depth in C002, within this precisely defined algorithmic class. It is not a lower bound on absolute error of a particular scalar posterior readout: the query and right-hand side may avoid the difficult eigenspaces. It is also not a lower bound on adaptive Krylov methods, matrix-memory algorithms, or arbitrary transformers.

In particular, attention can implement matrix Newton/Schulz iteration, whose polynomial degree doubles at each stage. Existing primary constructions include:

- Giannou, Yang, Wang, Papailiopoulos and Lee, *How Well Can Transformers Emulate In-context Newton's Method?*, https://arxiv.org/html/2403.03183v1 . Theorem 4.2 gives a linear-regression transformer with 3+T layers, two heads and width 4d+3, based on T inverse-Newton iterations. The ridge extension is discussed in Remark 4.4.
- Fu, Chen, Jia and Sharan, *Transformers Learn to Achieve Second-Order Convergence Rates for In-Context Linear Regression*, NeurIPS 2024, https://arxiv.org/abs/2310.17086 . Gives a transformer construction for iterative Newton computation as well as empirical evidence.
- Gutknecht and Röllin, *The Chebyshev iteration revisited*, ETH report 2000-16 / Parallel Computing, https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2000/2000-16_fp.pdf . Primary numerical-analysis treatment of scaled residual Chebyshev polynomials and recurrences.

Any broad claim that all transformers must have sqrt(kappa) depth would require additional restrictions excluding these known constructions.
