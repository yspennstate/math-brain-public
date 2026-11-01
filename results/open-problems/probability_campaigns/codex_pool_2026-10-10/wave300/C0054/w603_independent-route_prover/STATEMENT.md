# C0054 statement sent independently to the adversary

2026-10-10. Current openness: UNKNOWN; bounded primary-source checks found progress on delocalization, not a complete fixed-bandwidth localization-and-Poisson proof. This is not a novelty claim.

## Recovered source target

The intake's exact target is: for dimension two and fixed bandwidth W, localize all bulk eigenvectors on a periodic box of side n as n tends to infinity, with predicted localization length exponential in W squared, and prove Poisson local eigenvalue statistics. The primary source is P. Bourgade, Random band matrices, arXiv:1807.03031v2, equation (0.1), transition prediction (0.2), printed page 2, and section 2.2, printed page 7.

The survey takes a real symmetric matrix indexed by {1,...,n}^d, centered entries independent up to symmetry, zero entries beyond periodic l1 distance W, comparable nonzero variances normalized to sum to one in each row, and uniformly subgaussian scaled entries (section 2.2). It predicts a two-dimensional transition bandwidth of order sqrt(log n), with localization length exponential in W squared. The complex Hermitian analogue is explicitly mentioned. These statements are conjectural, and the survey does not supply a fully quantified definition of 'all bulk states'. It only asserts the semicircle limit when W tends to infinity. For fixed W, unfolding must use the ensemble's density of states when that density exists, rather than silently inserting the semicircle density.

The two limits differ: finiteness of a localization length for each fixed W is one obligation; its predicted growth as W tends to infinity is another. Poisson statistics require additional eigenvalue-count estimates and are a separate obligation.

## Precise working submodel and sufficient goal

To make the independent Gaussian-row calculation exact, restrict to the complex Gaussian block model in arXiv:2609.24426v2, equations (1.1)-(1.5). Write n=WL and matrix dimension V=n^2. Partition the periodic two-dimensional lattice into blocks of W^2 sites. For x in block a and y in block b, let S_xy=(5W^2)^(-1) if a=b or a and b are neighboring blocks, and zero otherwise. The diagonal is real N(0,S_xx); off-diagonal entries are independent proper complex N_C(0,S_xy), up to Hermitian symmetry. Take L even and at least 100 to match that source.

Fix W and kappa in (0,2), and I=[-2+kappa,2-kappa]. A concrete sufficient localization goal is a uniform-in-L eigenfunction-correlator estimate

    E sum_{lambda_k in I} |psi_k(x)| |psi_k(y)| <= C(W,kappa) exp(-dist(x,y)/ell(W,kappa)).

Eigenvalues are simple almost surely in this finite Gaussian model. This goal is a working sufficient criterion, not an asserted literal equivalent of every formulation of the survey conjecture. The predicted large-W scale is log ell=Theta(W^2). For a fixed energy E where the infinite-volume density nu_W(E) is positive and regular, the separate Poisson goal is convergence of sum_k delta_{V nu_W(E)(lambda_k-E)} to the unit-rate Poisson point process.

The full C0054 target is not proved by solving a Gaussian-row special case.

## Current primary-literature constraints

arXiv:2503.07606v1 proves bulk delocalization for its complex Gaussian block ensemble when W>=V^c for a fixed c>0. It does not prove the predicted sqrt(log V) threshold. The local intake's status-search sentence conflates a predicted threshold with that proved result.

arXiv:2609.24426v2 (revised 2026-10-06), Theorem 1.2, assumes W>=sqrt(m), where Lcal=10+log V, lcal=10+log Lcal, and m=Lcal^(27/2) lcal^26 (log lcal)^4. It bounds all normalized bulk eigenvectors by max |psi_k(x)|^2 <= 2 C m/V with probability at least 1-V^(-D) for every fixed D and sufficiently large V. The abstract's W>=(log V)^7 is an asymptotic sufficient simplification. The earlier v1 abstract used power 55. These delocalization results concern growing W and do not close the fixed-W localization target.

No proof attempt or peer proof is included in this statement-only artifact.
