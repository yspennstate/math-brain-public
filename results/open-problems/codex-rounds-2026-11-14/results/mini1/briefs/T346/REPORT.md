VERDICT: PROVED exact Gaussian minimax radius under a trace budget, allowing arbitrary input-dependent covariance

For p>2, including infinity, a in (1/2,1), and nominal smoothing noise with expected squared Euclidean norm at most d sigma^2, the optimal universal majority radius among kernels N(y,Sigma(y)) is exactly

    sigma Phi^{-1}(a) d^{1/p-1/2}.

Here a is the class probability at the nominal input, and the certificate must hold for every measurable base-classifier region with that probability. Sigma(y) may be any positive-definite matrix at each input; independence and continuity are not required. Constant isotropic covariance sigma^2 I attains the bound. Any attaining kernel must have that covariance at the nominal point.

The proof is in PROOF.md. Its key finite-radius obstruction is a halfspace: once the perturbed mean crosses the halfspace boundary, its probability becomes less than 1/2 under every Gaussian covariance chosen there. The boundary distance is derived independently by norm duality. Sign averaging and matrix Cauchy-Schwarz give the dimension factor by two routes. A further local theorem gives the sharp probability-loss constant phi(Phi^{-1}(a)) d^{1/2-1/p}/sigma for C1 covariance fields, also for a<=1/2.

This does not settle T346 for arbitrary smoothing distributions at fixed clean accuracy. Dataset accuracy and nominal class probability are different constraints. Fixed clean accuracy alone does not normalize distances or exclude constant-label tasks. The precise Gaussian result above uses an explicit local noise budget and universal class-region quantifiers. No claim of literature novelty is made for this special case or its elementary halfspace obstruction.

## Literature check

The search lasted less than five minutes. No located work settles the original question as worded. The brief's caveat needs qualification:

- Avrim Blum, Travis Dick, Naren Manoj, and Hongyang Zhang, *Random Smoothing Might be Unable to Certify l_infinity Robustness for High-Dimensional Images*, [arXiv:2002.03517](https://arxiv.org/abs/2002.03517), already give a moment barrier for arbitrary additive noise, including non-product distributions.
- Greg Yang, Tony Duan, J. Edward Hu, Hadi Salman, Ilya Razenshteyn, and Jerry Li, *Randomized Smoothing of All Shapes and Sizes*, [arXiv:2002.08118](https://arxiv.org/abs/2002.08118), [Theorem 7.3 and Corollary 7.4](https://proceedings.mlr.press/v119/yang20c/yang20c.pdf), cover general distribution families q_x under their universal useful-smoothing assumptions. These are stronger than empirical clean accuracy.
- Peter Súkeník, Aleksei Kuvshinov, and Stephan Günnemann, *Intriguing Properties of Input-dependent Randomized Smoothing*, [arXiv:2110.05365](https://arxiv.org/abs/2110.05365), analyze restrictions on input-dependent variance.
- Chenhao Sun, Yuhao Mao, and Martin Vechev, *Dual Randomized Smoothing: Beyond Global Noise Variance*, [arXiv:2512.01782](https://arxiv.org/abs/2512.01782), [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cd9664c7094d90e512ce27f2fd58198b-Abstract-Conference.html), certify adaptive variance selection through local constancy. This does not establish a better universal high-dimensional exponent. Its listed 31 October 2026 revision precedes the brief's November status.

All cited papers' arXiv or proceedings pages were opened; the Blum and Yang full PDFs were also opened. No SOLVED_ELSEWHERE.md was created because no full solution was verified. The search is not a proof of absence of other literature.

## Verification

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify.py
```

The final run exited 0 in approximately 0.16 seconds. It checked 21 covariance matrices, 420 halfspace derivative cases, and 1,008 finite-radius endpoint cases. Dimensions were 1 through 7, with isotropic, diagonal, and correlated covariances; p=2.01,3,4,infinity; and a=0.1,0.5,0.75,0.9,0.99. Maximum derivative discrepancy against exact-CDF finite differences was 4.95e-10; against numerical score integration it was 3.64e-11. Endpoint boundary probabilities agreed with 1/2 within 1.78e-14. Detailed data are in audit_data.json and complete output in LOG.md.

The sandbox reports that changing priority is not permitted; the script verified it already inherits nice level 20 and OMP_NUM_THREADS=1. It uses only the Python standard library, tiny matrices, one thread, and a 30-second CPU limit.

## What failed, limitations, and next work

A one-halfspace local derivative argument can fail: changing covariance can cancel that derivative exactly. The explicit cancellation test demonstrates this. The reflected halfspace repairs the local proof; the finite proof instead uses the sign of the projected threshold and needs no derivatives. The survey OpenReview PDF hit a browser challenge, and a newer Lipschitz-variance PDF returned 404; neither is used for technical claims.

The result does not cover arbitrary non-Gaussian nominal noise, singular kernels, kernels centered away from the input, classifier-specific information, or dataset-only accuracy constraints. The optimal distribution over all such schemes remains unresolved here.

The next worker should specify a nontrivial data/accuracy model and a scale constraint before optimizing all smoothing schemes. A focused extension is to identify non-Gaussian nominal distributions for which a comparable halfspace-quantile bound is sharp, and determine whether a second-moment constraint alone permits an exact matching constant. Existing arbitrary-noise barriers must be checked before claiming that non-product dependence escapes them.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 22:13 Asia/Tbilisi.
