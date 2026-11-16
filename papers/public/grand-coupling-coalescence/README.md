# Almost every finite Markov chain has only coalescing grand couplings

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

A grand coupling of a finite Markov chain with transition matrix P runs copies of the chain from every state by applying independent random maps with a common law; its coalescence number is the eventual number of distinct trajectories. Grimmett and Holmes (Coalescence in Markov chains, J. Theoret. Probab. 39 (2026), arXiv:2510.13572, Open problem 3.8) asked whether, for a random transition matrix with independent uniform weights, every grand coupling has coalescence number one almost surely. Paul answered this affirmatively in a preliminary note (2026, https://github.com/neophyte577/3.11-counterexample), from the equal stationary mass of the eventual classes. The paper gives a different proof. If some grand coupling of P has coalescence number k >= 2, then there are k states W and a partition {Z_w : w in W} of the state space with w in Z_w such that the k x k matrix (P(w, Z_w')) is doubly stochastic. For k equal to the number of states this is the Birkhoff-von Neumann condition. Each such condition is a non-trivial affine equation in P and there are finitely many of them, so the matrices with a non-coalescing grand coupling form a Lebesgue-null set.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_monoid.py`: for every set of at most three maps on three states, and for 100,000 random sets of one to four maps on four and on five states, computes the generated semigroup and its least rank and, when that rank is at least two, checks the pointwise identity behind Theorem 1.2 for an idempotent of least rank (the first counts in Section 4). Run `python3 check_monoid.py`; plain Python 3, about a minute.
- `code/check_dims.py`: for n = 3, 4, 5 enumerates every non-empty family of k-element subsets (k >= 2), computes the maps that send each member of the family onto a member, and finds the affine dimension of their transition matrices (the second counts in Section 4). Run `python3 check_dims.py 5`; needs numpy, a few seconds.
- `SHA256SUMS`: sha256 of each file above.
