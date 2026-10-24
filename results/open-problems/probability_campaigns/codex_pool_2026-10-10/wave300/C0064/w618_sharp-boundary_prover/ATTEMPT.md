# C0064 sharp-boundary packet (w618)

## Target recovery

Inherited target: infrared bound for nearest-neighbour percolation in every integer dimension d>6, particularly d=7,8,9,10. Exact primary-source formulation and current status are not yet verified. No solution or novelty claim is made.

## First saved result: C0064-w618-L1

Let D(x)=(2d)^(-1)1_{||x||_1=1}, so Dhat(k)=d^(-1) sum_j cos(k_j) on [-pi,pi]^d. Then the integral of (1-Dhat(k))^(-3) is finite exactly when d>6.

Proof. On [-pi,pi], 2t^2/pi^2 <= 1-cos(t) <= t^2/2. Summing gives 2|k|^2/(d*pi^2) <= 1-Dhat(k) <= |k|^2/(2d). Integrability at zero is equivalent to that of r^(d-7) dr. The denominator is strictly positive elsewhere on the torus. Thus the threshold is strictly d>6; d=6 diverges logarithmically. QED.

This is an elementary power-counting boundary check, not a percolation proof or a new theorem.

## Single hardest gap

An actual uniform critical Fourier bound for independent nearest-neighbour Bernoulli percolation in d=7,8,9,10. Finite triangle diagrams, source hashes, or estimates for arbitrary positive-definite kernels cannot close that gap alone.
