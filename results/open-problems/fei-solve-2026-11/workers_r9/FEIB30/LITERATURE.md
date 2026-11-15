# Literature check

Checked online during this worker run, 10 Nov 2026. These are primary papers, not evidence that the exact predictor conjecture is novel. No novelty claim is made.

Verdú and Weissman, [The Information Lost in Erasures](https://web.stanford.edu/~tsachy/pdf_files/The%20Information%20Lost%20in%20Erasures.pdf), IEEE Transactions on Information Theory (2008), define erasure entropy as the sum of conditional entropies of each coordinate given all the others. For the spectral indicator vector this is

    sum_(T,i) [a log2(1+b/a)+b log2(1+a/b)].

Our I L is precisely the second, presence-weighted half. The first half lies between zero and I/ln 2, by log(1+x)<=x. Thus interpreting the expression as a one-coordinate erasure loss is already within the classical erasure-entropy framework. The variational predictor inequality is a direct KL/log-loss inequality; it should not be presented as a new information inequality. Besag's [Statistical Analysis of Non-Lattice Data](https://doi.org/10.2307/2987782) (1975) is an original source for modeling a joint law through coordinate conditionals, the pseudolikelihood terminology relevant here.

Garban, Pete and Schramm, [The Fourier spectrum of critical percolation](https://arxiv.org/abs/0803.3750), study the Fourier-squared spectral sample, its lower tails, and noise/dynamical percolation applications. The spectral sample itself and its use to understand resampling are established objects. This paper concerns percolation crossing functions; its statements do not supply a uniform thinning-predictor overhead bound for arbitrary Boolean functions. A search of these sources did not locate Conjecture P in this exact form; that is a limited search result, not a priority claim.

Keller and Kindler, [Quantitative relation between noise sensitivity and influences](https://arxiv.org/abs/1003.1839), give quantitative bounds relating noise stability to sums of squared influences, including product measures. Noise operators and derivative norms are standard ingredients in that subject. Such estimates do not by themselves bound averages of logarithms of ratios of higher derivative norms. The distinction matters: the present cost uses the spectral law mu in its outer expectation, whereas the exact deleted-count identity averages under nu.

Kelman, Kindler, Lifshitz, Minzer and Safra, [Towards a Proof of the Fourier–Entropy Conjecture?](https://arxiv.org/html/1911.10579v2), explicitly define higher derivatives and their Fourier expansion in Definition 2.2. The equality up_lambda(T)=||T_sqrt(lambda) D_T f||_2^2 is then Parseval, not a new derivative identity. Their Theorems 1.1–1.3 establish spectral concentration/min-entropy and low-degree entropy bounds with an extra logarithmic factor. Their random restrictions and generalized influences are directly related tools, but those theorems do not imply P as stated.

Han, [A new bound for the Fourier-Entropy-Influence conjecture](https://arxiv.org/html/2312.08271v2), uses moments of Fourier coefficients under random restrictions and obtains H<=O(I+sum_i Inf_i log(1/Inf_i)). Its Lemma 2.2 is an explicit averaged restriction identity. Independently, the familiar restriction calculation gives

    E_z [ fhat_(restricted to R)(T)^2 ]
        = sum_{U: U intersect R=T} mu(U),  T subset R.

If each coordinate is kept in R with probability 1-lambda, averaging R gives exactly nu_lambda(T)=(1-lambda)^|T| up_lambda(T). Thus spectral thinning here is also the averaged spectral law of a random restriction. This makes the relationship to random-restriction FEI approaches precise.

O'Donnell and Tan, [A composition theorem for the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/1304.1347), already develop biased composition and prove FEI for read-once formulas over fixed bounded gates. The Taylor/biased Fourier factorization used by this worker belongs to that composition framework. Our finite recurrence tracks the particular predictor's K, cost and L, which are different quantities from an entropy/influence composition bound. Wan, Wright and Wu, [Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture](https://arxiv.org/abs/1312.3003), develop the spectral coding interpretation and another composition proof.

Hod, [Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions](https://arxiv.org/abs/1711.00762), supplies lexicographic constructions improving prior lower bounds through composition. A lexicographic function's own H/I and the amplified ratio H/(I-1) of a balanced gate are distinct. This worker evaluates finite lexicographic functions, threshold-of-ANDs, and the author's saved balanced PM(K33) lift; it does not claim that every construction or every optimization parameter in Hod's paper was reproduced.

What remains open here is a dimension- and function-independent bound on the specific mismatch D_KL(Q||R_lambda). The checked literature supplies the surrounding concepts and identities, but this search has not settled that bound. The balanced-tower and majority proofs in this folder are proved calculations for particular families, with no claim of literature priority.
