VERDICT: PROVED explicit determinant-weighted saddle law and exact residual-field level comparison

The round-4 crossing-stability bound holds. Its script passed again,
and an independent Fourier–Bessel derivation recovers its saddle
height intensity phi(t) exp(-t^2)/(4 pi). No solution of the Cardy/SLE(6)
conjecture was found in the five-minute literature check.

New beyond round 4: the full conditional field required by the
proposed pivotal Kac–Rice estimate is explicit. Under the normalized
saddle determinant weighting at height t,

    F_t(r,theta) = t J0(r)
        + 2 sqrt(t^2+G) J2(r) cos(2 theta-Theta)
        + independent Gaussian Fourier modes n>=3,

where G has Gamma(2,1) distribution and Theta is independent uniform.
In particular det Hess F_t(0)=-G/4. Ordinary first-jet Gaussian
conditioning would give the wrong second-mode law.

Put H_t=F_t-t J0. On every centered annulus of positive width,

    TV(Law(H_t), Law(H_s)) = delta(|t^2-s^2|),
    delta(a) = (1-exp(-a)) exp(-a/(exp(a)-1)) <= min(1,a/e),
    delta(0)=0.

Thus comparison with zero has exact error t^2/e+O(t^6). A shared-mode
coupling also has expected uniform field difference outside radius R
bounded by

    |t-s| M0(R) + (sqrt(pi)/2)|t^2-s^2| M2(R),

where Mj(R)=sup_(r>=R)|Jj(r)|=O(R^(-1/2)), j=0,2. PROOF.md proves
these statements and gives the interior threshold density with the
global pivotality mark retained. These are derived identities; no
literature priority is claimed.

Commands:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T064/check_local_threshold.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_saddle_palm.py
```

Both passed. The new audit used 13.34 MiB peak RSS and 0.038 seconds,
with actual niceness 20. Independent density quadrature and maximized
CDF differences checked the total variation formula; spectral-angle
integration checked the Fourier normalization; direct tilted moments,
circle statistics and near-degenerate saddles checked the other
constants. Full output is in LOG.md. The proof does not depend on
numerical quadrature.

What failed and remains unresolved: uncentered Palm laws at distinct
levels have total variation one, even on a distant annulus, because
their circle means reveal the conditioned height. More importantly,
saddle arms concern F_t-t=H_t-t(1-J0(r)); subtracting t J0 leaves a
radial threshold asymptotic to t. The residual-law comparison does
not remove that threshold. There is no new arm decay estimate, RSW
bound, enlargement of the o(R^(-2)) sufficient level window, or
conformal limit. Literature novelty was not established, and the
bounded search cannot certify absence of a later solution.

Sources actually opened: Stephen Muirhead, Alejandro Rivera and Hugo
Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), for threshold
genericity and measurability; Dmitry Beliaev, *Gaussian fields and
percolation*, [arXiv:2207.13448](https://arxiv.org/abs/2207.13448),
for the Fourier–Bessel representation. Bessel formulas were checked
in DLMF Sections 10.2, 10.17 and 10.23, linked in PROOF.md.

Next worker: use (2) of PROOF.md as the exact sampling or analytic law
for determinant-weighted four-arm probabilities. For a measurable
annular arm event, its probability under H_t differs from that under
F_0 by at most delta(t^2), even when the chosen event depends on t.
The remaining comparison is between zero arms and arms at the radial
level t(1-J0(r)); quantify that stability or obtain direct large-radius
arm decay under F_0. Boundary pivotal estimates remain separate.

Only this folder was changed; no git or external writes. The shell's
nice warning is documented; the scripts verified inherited niceness.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 07:53 Asia/Tbilisi (session launch; the
message receipt time was not separately recorded).
