# HARD7-02 exact analytic checkpoint — PWIT tail-map lemma and cyclic-band zero forcing

This artifact contains only analytic derivations. No simulation or finite numerical checker was used in this run.

## A. Exact pushforward of one PWIT branch to the half-angle tail coordinates

Fix `0<alpha<2`. Let the radial PWIT marks have intensity

`m_alpha(dr)=alpha r^(-alpha-1) dr`,

so `m_alpha((R,infinity))=R^(-alpha)`. Let `theta` be a probability measure on the unit sphere in `C^2`. For `w=(w_1,w_2)` put `p(w)=w_1 w_2`. On `{p(w) != 0}` choose measurably one square root

`u(w)^2=p(w)/|p(w)|`, `|u(w)|=1`.

Attach an independent sign `sigma` uniform on `{+1,-1}` to each Poisson point and define

`s = r sqrt(|p(w)|)`, `d = sigma u(w)`.

Define the finite measure on `S^1`

`kappa_hat_theta(A) = integral |p(w)|^(alpha/2) * [1_A(u(w))+1_A(-u(w))]/2 theta(dw)`.

(The definition is independent of the measurable square-root choice.)

### Lemma A.1

The image of the marked PWIT Poisson process under `(r,w,sigma) -> (s,d)` is a Poisson point process on `(0,infinity) x S^1` with intensity

`alpha s^(-alpha-1) ds kappa_hat_theta(dd)`.

### Proof

For a nonnegative measurable test function `f`, the pushforward intensity equals

`integral theta(dw) (1/2) sum_{sigma=+-1} integral_0^infinity alpha r^(-alpha-1) f(r sqrt(|p|), sigma u(w)) dr`.

For `p != 0`, set `s=r sqrt(|p|)`. Then

`r=s/sqrt(|p|)`, `dr=ds/sqrt(|p|)`,

and hence

`alpha r^(-alpha-1) dr = alpha s^(-alpha-1) |p|^(alpha/2) ds`.

The set `p=0` maps to `s=0` and makes no contribution on `(0,infinity)`. Substitution gives exactly

`integral alpha s^(-alpha-1) ds integral kappa_hat_theta(dd) f(s,d)`.

The Poisson mapping/marking theorem completes the proof. `QED`

### Corollary A.2 — exact one-big-jump count

For every Borel `A subset S^1` and `R>0`, let

`N_R(A)=#{points: s>R, d in A}`.

Then

`N_R(A) ~ Poisson(lambda_R(A))`,

`lambda_R(A)=R^(-alpha) kappa_hat_theta(A)`.

Consequently

`P(N_R(A)>=1)=lambda_R(A)+O(lambda_R(A)^2)`

with the explicit inequality

`0 <= lambda_R(A)-P(N_R(A)>=1) <= lambda_R(A)^2/2`,

and

`P(N_R(A)>=2) <= lambda_R(A)^2/2`.

The latter follows because for a Poisson variable `N`, `E[N(N-1)]=lambda^2` and `1_{N>=2} <= N(N-1)/2`.

Moreover the intensity factorizes, so conditional on a selected point satisfying `s>R`, the overshoot `s/R` has Pareto tail `P(s/R>t | s>R)=t^(-alpha)` (`t>=1`) and its direction has the normalized restriction of `kappa_hat_theta`, independently of the overshoot.

### Scope

This proves exactly the *raw branch point-process* portion of the half-angle candidate from the preceding STUCK2 report. It does **not** prove that a raw branch produces a planar eigenvalue tail event. The unpaid steps remain the child-resolvent replacement, control of the truncated PWIT background under resonance conditioning, and the `eta downarrow 0`/Hermitization transfer.

---

## B. Deterministic zero forcing for a periodic hard-indicator band

Let `N>=1`, `0<=W<N/2`, and `L=2W+1`. Work on the cyclic index set `Z/NZ`. Let `A=(a_ij)` be any matrix satisfying

- `a_ij != 0` whenever `dist_N(i,j)<=W`;
- `a_ij = 0` otherwise.

No randomness is assumed.

### Lemma B.1

Every nonzero `v in ker(A)` satisfies

`|supp(v)| > N/L`.

Equivalently, no exact kernel vector can be supported on at most `floor(N/(2W+1))` coordinates.

### Proof

Assume to the contrary that `S=supp(v)` has size `k>=1` with `k<=N/L`. List the elements of `S` in cyclic order. Let `g_j` be the number of vertices strictly between the `j`-th support point and the next support point. Then

`sum_{j=1}^k g_j = N-k`.

Therefore some gap satisfies

`g_j >= (N-k)/k = N/k - 1 >= L-1`.

Let `s` be the support point immediately before such a gap. The cyclic interval

`I={s,s+1,...,s+L-1}`

contains no point of `S` except `s`. Since `L=2W+1`, `I` is exactly the support of the row indexed by `r=s+W` (mod `N`):

`I={j: dist_N(r,j)<=W}`.

Hence the `r`-th equation of `Av=0` reads

`0=(Av)_r=a_{r,s} v_s`.

Both factors on the right are nonzero by construction, a contradiction. `QED`

### Consequences for the frozen Rademacher band target

For the normalized periodic Rademacher hard-indicator band, all in-band entries are `+-1/sqrt(L)`, so the lemma holds deterministically on every realization. Thus a singularity/circular-law obstruction based on an exact localized null vector of support at most `N/(2W+1)` is impossible. For `W->infinity` this still leaves approximately-sparse vectors, and exact null vectors with support larger than `N/(2W+1)`, completely uncontrolled; the lemma is therefore auxiliary progress only, not a circular-law theorem.
