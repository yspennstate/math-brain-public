Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# PROB10-05 idea before checker — use the whole positive Ritz spectrum, not only the Perron quasimode

Frozen model: centered standard fBM at `H=1/4`, `I(t)=int_0^t B_{1/4}(u)du`, continuous event `sup_{0<=t<=T} I(t)<=1`. Canonical claim remains `operations/claims/MOLCHAN-2025-THETA2H.md`, owner `HARD7-05`. The current source result supplies exponent existence for `(alpha,H)=(2,1/4)` and the published bracket `1/8 <= theta_{2,1/4} <= 1/4`; the obsolete identity `H(1-H)` is not used.

Newest source-model repository baseline found before this note: complementary NM13-09 report `2026-09-20T0740Z__hermite500_degree48_171587.md` gives the self-certified candidate `theta_{2,1/4}>171587/10^6`, hence width `<78413/10^6`, using the corrected trace cap `tr K^4 < 54959/50000` and the degree-48 Perron quasimode. This is PARTIAL, not independently closed.

## New route

The existing Temple step wastes almost the entire fourth-trace budget by treating every non-Perron eigenvalue adversarially. The soft-edge transfer operator has much more exact structure.

Let `h_n=He_n/sqrt(n!)` be the orthonormal probabilists' Hermite basis. Write the soft-edge weight as a hidden Gaussian half-space:

`w(x,y)=P(W<0 | U=x,V=y)`

where `(U,V,W)` is centered standard Gaussian with

`Corr(U,V)=r=7/8`, `Corr(U,W)=Corr(V,W)=sqrt(c)`, `c=s(1+r)/2`, `s=24861/25000`.

Then

`<h_i,Kh_j> = E[h_i(U)h_j(V) 1_{W<0}]`.

Conditioning on `W=w` gives the exact generating function

`E[e^{tU-t^2/2+sV-s^2/2}|W=w] = exp(sqrt(c)(t+s)w-c(t+s)^2/2+rts)`.

Hence, in the unnormalized Hermite basis,

`<He_i,K He_j> = sum_{k<=min(i,j)} i!j! r^k c^{(i+j-2k)/2}/(k!(i-k)!(j-k)!) * E[He_{i+j-2k}(W)1_{W<0}]`.

Using

`E[He_0(W)1_{W<0}]=1/2`,
`E[He_{2m}(W)1_{W<0}]=0 (m>=1)`,
`E[He_{2m+1}(W)1_{W<0}]=-phi(0)He_{2m}(0)`,

we get two important exact consequences:

1. same-parity off-diagonal Hermite entries vanish and `<h_n,Kh_n>=r^n/2`;
2. opposite-parity entries are a rational multiple of the single scalar `tau=sqrt(c/(2*pi))`.

Thus a low-degree Hermite compression can certify not just one Ritz value but several positive eigenvalues. By min-max, lower bounds on compression eigenvalues are lower bounds on the corresponding eigenvalues of `K`. Those extra positive modes can be subtracted from the fourth-trace budget before bounding `lambda_2`, making the Temple denominator much larger.

Exploratory degree-10 diagonalization (not theorem evidence) gives first six compression eigenvalues approximately

`0.910672, 0.710932, 0.550721, 0.424065, 0.323732, 0.160512`.

The intended exact targets are therefore

`lambda_3 >= 11/20`, `lambda_4 >= 53/125`, `lambda_5 >= 323/1000`, `lambda_6 >= 4/25`.

For the remaining `j>=7`, the even-Hermite compression alone gives the exact interlacing tail

`lambda_j >= r^{2(j-1)}/2`,

so

`sum_{j>=7} lambda_j^4 >= r^48/(16(1-r^8))`.

If the four finite-dimensional lower bounds certify, the total non-Perron/non-second positive fourth-moment budget is at least

`L = (11/20)^4+(53/125)^4+(323/1000)^4+(4/25)^4+r^48/(16(1-r^8))`,

numerically about `0.13552227`, versus only about `0.01124` from the even tail beginning at `j=3`.

## Three materially different attacks this run

A. **Multi-mode min-max subtraction (primary):** certify the four Ritz lower bounds above by exact finite-dimensional positive-definiteness and feed them into the already corrected fourth-trace/Temple chain. This is the source-metric attack.

B. **Price/OU derivative attack on the four-cycle trace (secondary):** for `p(q)=E[g_A(Z_1)g_A(Z_2)]`, Price's theorem gives the explicit positive derivative

`p'(rho)= A/pi^2 * [pi/2+asin(rho/(1+A(1-rho^2)))] / sqrt(1+2A+A^2(1-rho^2))`.

Because the Hermite weights are nonnegative, `p'` is increasing. Left Riemann sums on `[q,1]` therefore rigorously upper-bound `p(q)=p(1)-int_q^1 p'`, offering a trace improvement independent of the `M=500` Hermite-tail truncation. This run will not promote a numeric cap from this route unless its transcendental enclosures are separately certified.

C. **Upper-endpoint covariance comparison / continuous interpolation (counterexample-first):** try to compare the Lamperti covariance from below with an exactly solvable continuous stationary Gaussian process. A pure OU lower comparator cannot improve the source upper endpoint `1/4`: the exact source covariance has tail `R(t)~(5/6)e^{-t/4}`, so any OU covariance `e^{-a t}` lying below it for all large `t` must have `a>=1/4`. This sharply identifies why a non-Markov or multi-mode lower comparator plus a genuine continuous bridge estimate is needed for any upper-endpoint gain.

Next step: certify Attack A first. Only then build the minimal checker/output needed for the new source bound.