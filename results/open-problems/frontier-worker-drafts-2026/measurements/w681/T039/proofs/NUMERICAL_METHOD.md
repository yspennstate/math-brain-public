The numerical object is the weighted mean-zero operator from Appendix A (145)–(152). Put dnu(t)=exp(-t)dt, E(t,s)=K_+(t,s)-ell_rho(sqrt(t))-ell_rho(sqrt(s)), and f=sqrt(J_+)z. The constraint integral z dnu=0 becomes f orthogonal to J_+^(-1/2). Thus the relevant self-adjoint compression is P [E/sqrt(J_+(t)J_+(s))] P in L2(nu); its largest absolute eigenvalue is estimated. The positive branch dominates all sampled cases.

With t=x^2, the unitary map from L2(nu) to L2(dx) gives the symmetric kernel 2 exp(-(x^2+y^2)/2) E(x^2,y^2)/sqrt(Jtilde(x)Jtilde(y)), where Jtilde(x)=J_+(x^2)/x. A finite Gauss–Legendre rule with nodes x_i and weights w_i gives A_ij=sqrt(w_i w_j) times this kernel. The normalized constraint vector is proportional to sqrt(2w_i) exp(-x_i^2/2)/sqrt(Jtilde(x_i)). The program forms P A P explicitly. The Frobenius norm of A estimates the literal h_+ in (151); the extreme eigenvalues of P A P estimate the true constrained operator norm. The two norms are different objects.

Large negative arguments of erfcx are avoided: with q=rho*x/sqrt(1-rho^2), the factor exp(-q^2)[-psi'(-q cos(pi v))] is evaluated as sqrt(pi)(1+2q^2 cos^2(pi v)) exp(-q^2 sin^2(pi v)) erfc(-q cos(pi v)) + 2q cos(pi v) exp(-q^2). The kernel angular integral similarly combines the damping and coupling exponents before exponentiation. There is no use of the published coarse tail envelope for rho>=1/2. The finite cutoff and its refinement are numerical, not certified tails.

For arcs the program uses the normalized Bessel Fourier series (136). The stronger scalar bound is checked on [0,1]^2, and the vector bounds (139),(142) on every pair of denominator-30 simplex vectors. It uses M=ceil(10 sqrt(max(a,1))+30) Fourier terms and repeats selected cases with 2M terms. These are floating-point tests, not a truncation proof or interval bound.

Commands from T039 (Python 3.14; NumPy 2.4.3; SciPy 1.17.1; python-flint 0.9.0):

```powershell
python -X utf8 -B scripts/reproduce.py
python -X utf8 -B scripts/measure_operator.py control
python -X utf8 -B scripts/measure_operator.py sweep
python -X utf8 -B scripts/measure_operator.py roots
python -X utf8 -B scripts/measure_operator.py refine --n 128 --angular-n 64 --rho 0.386875 0.4 0.43251274132 0.4410142192 0.5 0.7 0.9 0.95
python -X utf8 -B scripts/measure_operator.py refine --n 512 --angular-n 192 --rho 0.386875 0.4 0.43251274132 0.4410142192 0.5 0.7 0.9 0.95
python -X utf8 -B scripts/measure_operator.py refine --n 768 --cutoff 30 --angular-n 256 --rho 0.386875 0.4 0.43251274132 0.4410142192 0.5 0.7 0.9 0.95
python -X utf8 -B scripts/measure_operator.py roots --n 512 --angular-n 192
python -X utf8 -B scripts/measure_operator.py roots --n 768 --cutoff 30 --angular-n 256
python -X utf8 -B scripts/check_arcs.py
python -X utf8 -B scripts/independent_kernel_check.py
python -X utf8 -B scripts/measure_operator.py refine --n 512 --cutoff 30 --angular-n 192 --rho 0.4 0.95
python -X utf8 -B scripts/measure_operator.py refine --n 512 --cutoff 30 --angular-n 384 --rho 0.4 0.95
```

All computations use CPU affinity [2,3], with BLAS/OMP/MKL/Numexpr thread caps 1; no GPU, randomness or seed. The largest planned array budget is 108 MiB (768^2*8*24 bytes). Available memory was checked before each command. The baseline took 425 seconds; later scripts run in bounded foreground commands and checkpoint every result. No detached process is used. Numeric reproduction should agree to about 1e-8 in displayed norms and 1e-7 in displayed crossing locations on a compatible stack; observed refinement agreement is much tighter. Those tolerances describe reproducibility and do not bound the infinite-dimensional error. The published certificate has the separate 5e-10 printed-output tolerance recorded in its metadata.

The hardest unpaid mathematical step is an outward-rounded upper bound for the full weighted compression over an interval of rho, including the radial tail and finite discretization error. A stable numerical eigenvalue is not that bound. The experiment remains numerical evidence and has no reviewer PASS.

At the measured crossings rho<1/2, the lower bound (153) also ensures J_+^(-1/2) belongs to L2(nu): 1/J_+(t) is bounded by a constant times t^(-1/2) exp(kappa t), with kappa=rho^2/(1-rho^2)<1. For larger fixed rho<1, formula (148) gives J_+(t) of order sqrt(t) near zero, while the conditional Gaussian radial law (98)-(99), w(a)->1/2 and theta(a)->0 give J_+(t)->1/2 at infinity. This supplies the qualitative mean-constraint interpretation, while numerical error enclosures remain unpaid.
