# T228 target 2: novelty rerun (scalar leaky-ReLU SGD, exact stationary tail)

agent AF, 22 Oct 2026 05:2x-05:4x. arXiv API through frontier/arxiv_q.py, newest first, ten wordings; this
reruns the 16 Oct search (agent A, lit.json) for the statement proved in T228_B_v2.md.

Statement searched: for constant-step minibatch SGD on the scalar single-index model with leaky-ReLU link (any slope
beta in [0,1)) and Gaussian data, under E log|A+| < 0, the stationary law has P(x > t) ~ C+ t^(-k) and
P(x < -t) ~ C- t^(-k) with C+ = C- > 0, k the root of E|1 - c sum w(a_i)^2 a_i^2|^k = 1.

Wordings: heavy tail + SGD + stationary; tail index + stochastic gradient (rerun in UTF-8 after an encoding crash);
Kesten + stochastic gradient; heavy-tailed + SGD + nonlinear; iterated random + stochastic gradient; leaky ReLU + heavy
tail; power law + stationary distribution + SGD; heavy-tailed + single-index; stochastic recurrence + neural network;
Gaussian approximation + constant step SGD.

What came back, none of which states it:
- Gurbuzbalaban, Simsekli, Zhu, 2006.04740: linear regression (quadratic loss) only.
- Hodgkinson, Mahoney, 2006.06293: "almost linear" recursions, two-sided bounds on the index, no exact constant.
- Jiao, Keller-Ressel, 2402.01382: homogenized SGD (an SDE surrogate), bounds on the index.
- Lehman Pavasovic, Durmus, Simsekli, 2310.18455: offline SGD, approximate tails, quadratic loss.
- Gurbuzbalaban, Hu, Simsekli, Yuan, 2205.06689: decentralized SGD, linear.
- Simsekli et al., 1912.00018 and 2006.09313: tails assumed or measured, not derived for a given model.
- Armacki et al., 2310.18784, 2410.13954, 2410.15637, 2507.09093, 2610.10527: nonlinear SGD (clipping, sign,
  normalization) under heavy-tailed NOISE; convergence rates, not stationary tails produced by light-tailed data.
- Keslin, Wu, 2610.14567: Gaussian approximation of constant-step SGD (the bulk, not the tail).
- Rhee, Ryu, Seo, 2503.05219: exit times for Kesten-type recurrences.
- Olsen et al., 2507.12709: spectra of weight dynamics, heuristic.
- The heavy-tailed-noise optimization papers (2412.19529, 2505.03736, 2605.06884, 2607.25492, 2405.17529) assume heavy
  noise; they do not derive a stationary index.
- The tool T228_B_v2 rests on, ABB 2102.02299 (sign-modulated random affine maps on the line), is prior art for the
  renewal step and is cited as such; it does not treat SGD or any activation.

Verdict: no prior statement found. An exact two-sided tail with a positive constant for SGD under a nonlinear
activation does not appear in what these ten wordings return. The search is title/abstract-level through the arXiv
API, not a full-text sweep, and it does not cover journals outside arXiv.

## Forward citations (05:4x, Semantic Scholar graph API)
All 199 papers citing 2006.04740 (GSZ) or 2006.06293 (Hodgkinson-Mahoney), titles screened for tail, Kesten,
stationary, renewal, ReLU, activation, power law, recursion. Read in abstract:
- 2403.13868, "Analysing heavy-tail properties of SGD by means of stochastic recurrence equations": answers GSZ's open
  questions for LINEAR regression through irreducible-proximal matrices (affine recursion, symmetric A_k).
- 2204.12554, "An Empirical Study of the Occurrence of Heavy-Tails in Training a ReLU Gate": the closest. It measures
  the tail index of SGD on a ReLU gate, reports that it behaves unlike the linear case, and proves nothing about the
  index. T228_B_v2 at beta = 0 is the scalar ReLU gate; its index equation (only samples with a_i x > 0 enter the
  multiplier) gives a different number from the linear one, the kind of gap that paper reports (the abstract does not say whether
  its runs include d = 1, so this is agreement in kind, not a check). Cite it as
  the empirical motivation; it is not prior art for the theorem.
- 2306.09624 (power-law SDE), 2610.05599 (Gaussian limits, least squares), 2602.05657 (large-deviation tail of the
  gradient norm, bounded or clipped noise): different objects.
Verdict after this check: no prior statement found; "open" stands, with 2204.12554 added to the related work.
