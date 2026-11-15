# T305 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Orientation clock: 15 November 2026, approximately 09:06 Asia/Tbilisi.
Exact prompt receipt time is unavailable.

## Orientation and literature check (09:06–09:09 +04)

Read the three preceding sessions' reports, proofs, logs and audit scripts.
Earlier folders are read-only. Read the startup memory index and compute
snapshot: status ok, owner_away_open, but substantial shared CPU load.
All computations here will be small, one-thread, standard-library Python
under nice -n 15. No subagents or git. The current folder-only order
overrides global requests to mutate mesh, checklist and memory stores;
none of those external stores will be changed.

Web queries: Metropolized/operator/Hessian/2026; source 2304.04724;
Hamiltonian Monte Carlo d^(1/4) Hessian Lipschitz. Opened:

- Yuansi Chen, Khashayar Gatmiry, Minhui Jiang,
  *When does Metropolized Hamiltonian Monte Carlo provably outperform
  Metropolis-adjusted Langevin algorithm?*, arXiv:2304.04724v3,
  https://arxiv.org/html/2304.04724v3.
- Matthew S. Zhang, Jason M. Altschuler, Sinho Chewi,
  *Algorithmic warm starts for Hamiltonian Monte Carlo*,
  arXiv:2603.22741v1, https://arxiv.org/html/2603.22741v1.
- Fan Chen, Sinho Chewi, Jianfeng Lu, Matthew S Zhang,
  *Smoothed Picard Hamiltonian Monte Carlo*, arXiv:2609.06906v2,
  https://arxiv.org/abs/2609.06906.

The first two still explicitly require Frobenius-Lipschitz Hessians.
The third uses a different integrator and smoothing; its high-accuracy
result uses a proximal bouncy particle sampler. No settlement of the
specified leapfrog MHMC question was found. Search stopped within five
minutes; this is a bounded check, not an exhaustive priority search.

## Independent recheck of the preceding result

For F=J S, volume preservation and F²=I give
E f(Delta)=E[e^(-Delta) f(-Delta)]. Pairing the signs of Delta gives
E Delta=E[|Delta| tanh(|Delta|/2)] <= E Delta²/2. The nonnegative
mean is exactly KL(S#rho||rho), by changing variables through S.
Thus the main entropy reduction in round 4 holds.

Independently expanding the two kinetic squares with
v=p-hg(x)/2, q=x+hv gives the local identity

    Delta = V(q)-V(x)-(q-x)·(g(q)+g(x))/2
            + h²(|g(q)|²-|g(x)|²)/8.

Two integrations by parts in the segment parameter give the trapezoid
defect bound M|q-x|³/12; one gives L|q-x|²/4. These require only C2,1.
Summing with the linear growth bound gives the two deterministic estimates
used in the previous proof. Independence then gives the claimed block
entropy and moment-generating-function bounds. No mathematical error
found. A fresh exact-arithmetic audit will separately check this identity
and the Gaussian moment formulas used below.

## Chosen extension — recorded before implementation

Prove the proposed stationary second-moment estimate

    E Delta² <= C[dh^4+(dh^4)²]

for a coupled class V(x)=|x|²/2+U(x), with U supported in a ball of
fixed radius, uniformly bounded Hessian and operator-Lipschitz Hessian.
This is a narrower class than T305, but it genuinely includes families
with Frobenius-Lipschitz constants growing as sqrt(d), unlike all bounded
blocks in round 4. The mechanism is avoidance of the perturbation by
typical Gaussian numerical paths, controlled uniformly in the number
of steps using the smallest singular value of the two-column matrix
[x,p], rather than a union bound over n. On the exceptional set use the
round-4 deterministic bound and explicit Gaussian moments.

An explicit radial bump will certify the regularity gap. If the
second-moment argument succeeds, also derive its warm-start energy tail
as a corollary of the same avoidance argument. No mixing theorem is
being assumed or inferred from acceptance alone.

## Proof saved — main derivation

Wrote PROOF.md. For Gaussian leapfrog,

    x_j = cos(j theta)x + sin(j theta)p/sqrt(1-h²/4).

The coefficient vector has norm at least one. Thus every Gaussian mesh
position is outside the perturbation ball whenever sigma_min([x,p])>R.
On this event the perturbed leapfrog proposal and energy error coincide
exactly with the Gaussian ones. Gaussian Gram-matrix tails give

    P_Gamma(sigma_min([x,p])<=R) <= K_R exp(-c d),
    c=1/16+log(15/16)/2 > 0.

There is no n factor. On the exceptional event the deterministic estimate
|Delta|<=D h²(1+|x|²+|p|²)^(3/2), combined with Cauchy–Schwarz and
Gaussian twelfth moments, gives an O(d h^4) contribution to E Delta².
The Gaussian contribution is exactly 2d mu1+(d²+2d)mu1², mu1<=h^4/24.
This proves the proposed second-moment scale for the chosen subclass.

The same event comparison and a two-regime warm argument prove

    P_warm(|Delta| > d h^4/24 + C h²[sqrt(d s)+s^(3/2)]) <= delta,
    s=log(K M0/delta).

When s<cd, the rare event can be discarded after warm transfer. When
s>=cd, d<=s/c and the global deterministic estimate plus the radial
Gaussian tail handles the whole state space. Omitting the second regime
would incorrectly ignore warm starts concentrated near the origin.

The explicit family U_d=(1-|x|²)_+³/24 has 3I/4<=Hessian V<=5I/4,
operator-Lipschitz Hessian constant at most 2, but every Frobenius
constant is at least (3/8)sqrt(d-1). Thus the class genuinely extends
beyond dimension-independent Frobenius regularity. It remains narrow:
the nonlinearity is confined to a fixed-radius, rarely visited ball.

## First computation and self-audit

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The first run passed every check in 1.331 seconds, one Python thread,
maximum RSS 16,859,136 bytes, inherited nice 20. The wrapper warning
reflects the inherited lower priority. Exact rational checks independently
verify the local energy identity, reversal, Gaussian means and fourth
moments, the tensorized second-moment formula, and Chernoff substitution.
The Gaussian twelfth moments were checked by convolution of squared-normal
moments, independently of the rising-factorial derivation in the proof.

A fixed-seed streaming audit used 2,000 stationary position/momentum pairs
per dimension d=1,2,4,8,16,64, and T=1 with n=4,8,16. The exceptional
counts were 2000,1747,754,42,0,0 respectively. The observed
E Delta²/(d h^4) ranged from 0.04297 to 0.04695. This is only a Monte
Carlo audit, not a certified probability or moment bound. In particular,
the direct sample mean has large cancellation noise and is not used to
validate the entropy scale. Positive reflected means are also recorded.

The deterministic avoidance check includes a deliberately adverse case:
x=(2,0), p=(-1,0), T=1 starts outside the support and enters it. A
comparison using only the initial position would fail. Its singular-value
event does flag it. Outside the singular-value event, the perturbed and
Gaussian iterates were exactly equal in floating-point arithmetic in all
12 checked paths, including h=1 and long resonant paths.

Added an explicit C3 sibling U_d=(1-|x|²)_+^4/32. It has the same
spectral bounds, operator-Lipschitz constant at most 3, and Frobenius
constant at least (27/64)sqrt(d-1). This ensures the example's gap is not
explained by its C2,1 regularity. The derivative constants are also checked
by exact rational algebra; rerun the audit after this addition.

## Final audit run and independent mathematical checks

Re-ran the command above after adding the C3 sibling checks. Output:

```text
nice: setpriority: Operation not permitted
PASS: exact rational local energy identity and reversible involution
PASS: Gaussian second moments by two exact expansions
PASS: Gaussian moments, dot-product Chernoff constant, and tail substitution
PASS: operator regularity and growing Frobenius lower bound
PASS: pathwise avoidance, including an outside start that enters the ball
stream d=1 exceptional=2000/2000 second/(dh4)=0.0458302,0.04478,0.044741
stream d=2 exceptional=1747/2000 second/(dh4)=0.0443462,0.043042,0.0429687
stream d=4 exceptional=754/2000 second/(dh4)=0.0469453,0.0462171,0.0460425
stream d=8 exceptional=42/2000 second/(dh4)=0.0440597,0.0433797,0.0432122
stream d=16 exceptional=0/2000 second/(dh4)=0.044599,0.0439552,0.0438031
stream d=64 exceptional=0/2000 second/(dh4)=0.0439591,0.0432654,0.0431172
Resources: {"elapsed_seconds": 1.3197663750033826, "max_rss_bytes_macos": 16564224, "nice": 20, "python_threads": 1}
```

The command exited zero. Numerical work is complete.

Re-derived the load-bearing bounds a second way:

1. The Gaussian mean can be recovered from (||C^n||_F²-2)/2, independently
   of its preserved modified energy. Its variance follows by direct
   expansion using E X^4=3, E X²P²=1; this agrees exactly with
   2 mu1+2 mu1² and the proof's determinant calculation.
2. The dot-product mgf follows either by conditioning on X or by writing
   X·P=(|A|²-|B|²)/2 for independent Gaussian A=(X+P)/sqrt(2),
   B=(X-P)/sqrt(2). Both give (1-t²)^(-d/2). The resulting constant is
   c=0.03023073943121441, positive and smaller than c0=0.09657359027997264.
3. Chi-squared moments through order six agree exactly between convolution
   of 2d squared-normal moments and 2^k(d)_k. The exponential-polynomial
   maximizer is d=4/c; both derivative and value checks agree with
   16/(c² e²). This is what absorbs the exceptional event's d³ factor.
4. Radial Hessian eigenvalues were obtained both by differentiating the
   gradient radially and by differentiating U as a function of |x|².
   For the cubic bump, the full Frobenius derivative squared at e1/2 is
   (49+9(d-1))/64; for the C3 quartic bump it is
   (45²+27²(d-1))/64². Each independently confirms sqrt(d) growth.
5. In the global deterministic estimate, augmented norm W>=1 removes the
   quadratic term without any dimension-dependent shift of the minimizer.
   Neither numerical endpoint stationarity nor integrability of exp(cW³)
   is used.

Boundary and omitted-case checks: d=1 makes the singular-value event the
whole space and is still covered by the global moment bound; h=1 is in
the Gaussian stability range; arbitrary n introduces no union factor;
entry into and exit from the support satisfy the exact C2 local identity;
large M0 is covered by the s>=cd branch; M=0 and U=0 reduce to the
Gaussian formulas; the C3 example removes a possible lower-regularity
explanation for the Frobenius gap. The radial bump cannot split into
bounded orthogonal blocks, because any orthogonal change leaves it radial
and mixed Hessian entries between arbitrary nonzero coordinates persist.

The next-family suggestion in REPORT.md is also checked at the level
claimed there: for b cos(r), the radial and tangential Hessian eigenvalues
are -b cos(r) and -b sin(r)/r. Their absolute values are <=b. Writing
sin(r)/r=integral_0^1 cos(rt)dt shows that its derivative is bounded by
1/2, so the radial matrix derivative has a dimension-independent bound
(at most 3b by the directional Hessian formula). At r=pi/2 the tangential
derivative equals 4b/pi², yielding a growing Frobenius constant. This only
checks membership and the regularity gap, not a finite-step energy bound.

Saved REPORT.md with the required partial verdict, theorem, commands,
limitations, opened papers and next step. Corrected inline math delimiters
in PROOF.md and REPORT.md during the artifact review; this was formatting
only. No substantive checks failed and no claims beyond the compact
perturbation subclass are made. All writes stayed inside this folder.
