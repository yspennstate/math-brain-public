# The discrepancy of Sylvester-Hadamard matrices in odd dimension

Yitzchak Shmalo

For the 2^k x 2^k Sylvester-Hadamard matrix H_k, disc(H_k) = 2^k - 2 rho(1,k), where rho(1,k) is the covering radius
of the first-order Reed-Muller code RM(1,k). With the known values and bounds for that covering radius, this settles
Conjecture 13 of Randomstrasse101, *Open problems of 2024* (arXiv:2504.20539): disc(H_k) = 2^((k+1)/2) holds for
k = 1, 3, 5, 7 and fails for every odd k >= 9, where disc(H_k) <= (7/8) 2^((k+1)/2); disc(H_9) <= 28 < 32.

- `paper.tex`, `paper.pdf`: the paper.
- `check.py`: exhaustive check of disc(H_k) = 2^k - 2 rho(1,k) for k <= 4, the direct-sum identity on random
  functions, and the arithmetic of the corollary. Plain Python 3, no packages: `python check.py`.
