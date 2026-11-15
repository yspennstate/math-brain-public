# Literature check, 2026-11-14

The search did not establish a solution to the whole stated problem. "Natural input distribution" is not defined in the prompt; here it is interpreted to require a regular distribution at polynomial input scale.

Itay Safran, *Every Layer Counts: An Exponential L2 Depth Hierarchy for ReLU Networks*, [arXiv:2608.23877v2](https://arxiv.org/abs/2608.23877v2), is a substantial update predating this session. Theorem 3.1 separates every adjacent pair, but puts the approximation distribution at exponential radius. Theorem 4.1 gives a depth-4 versus depth-3 exact separation on the cube. Neither supplies the requested regular-distribution approximation result with polynomial target weights. No bound on the target's individual parameters was verified here. See the [opened full paper](https://arxiv.org/pdf/2608.23877), Sections 3--5.

The prompt conflates two references. [arXiv:2006.00625](https://arxiv.org/abs/2006.00625) is *Neural Networks with Small Weights and Depth-Separation Barriers*, by Gal Vardi and Ohad Shamir. Its Theorems 3.3--3.4 assume the shallower depth is at least 4; the discussion after Remark 3.5 explicitly excludes separation of depth 3 from a larger constant depth from that circuit barrier. This is a qualification to the prompt's caveat, not a proof that no other barrier exists. [Full text opened](https://arxiv.org/html/2006.00625v4).

The four-author paper is *Size and Depth Separation in Approximating Benign Functions with Neural Networks*, by Gal Vardi, Daniel Reichman, Toniann Pitassi and Ohad Shamir, [arXiv:2102.00314](https://arxiv.org/abs/2102.00314), COLT 2021. Its [proceedings page](https://proceedings.mlr.press/v134/vardi21a.html) was also opened.

Neil Krishnan and Elchanan Mossel, *Depth Lower Bounds for ReLU Networks with Binary Inputs*, [arXiv:2606.18540v2](https://arxiv.org/abs/2606.18540v2), concerns growing depth and exact computation, according to the opened abstract. It does not settle this task.

The search found no qualifying later solution. This is a bounded search result, not a proof of absence. SOLVED_ELSEWHERE.md records the substantial related advance with an explicit warning that the whole task remains unsettled by that paper.
