# Credits: Gradient flow for deep factored scalar linear attention learns multi-step gradient descent

Who proved what this paper rests on, with the cite key, the result, and how the paper uses it.
Labels: known (cited, as published), adapted (cited, changed as stated), new.

| Key | People | Result | Use here |
|---|---|---|---|
| vonOswald | von Oswald, Niklasson, Randazzo, Sacramento, Mordvintsev, Zhmoginov, Vladymyrov | linear self-attention can implement gradient descent on the in-context loss | the reading of each layer as one gradient step (known) |
| Akyurek | Akyurek, Schuurmans, Andreas, Ma, Zhou | transformer constructions of gradient-based and closed-form regression | context in the introduction (known) |
| Ahn | Ahn, Cheng, Daneshmand, Sra | landscape of linear transformers on linear regression; critical points as L preconditioned steps | the multi-layer landscape the paper settles for scalar data (known) |
| ZFB | Zhang, Frei, Bartlett | gradient flow on one linear self-attention layer converges to a global minimizer | the one-layer case (known) |
| Gatmiry | Gatmiry, Saunshi, Reddi, Jegelka, Kumar | gradient flow on looped linear attention converges, by gradient dominance, to multi-step preconditioned GD | the value map and mask are taken from it; Theorem 2.1 is its counterpart for untied layers, where gradient dominance fails (adapted) |
| BLP | Bordelon, Letey, Pehlevan | dynamics of untied linear-attention layers in a high-dimensional limit | context: Theorem 2.1 is finite n, scalar data, almost every initialization (known) |
| PS, CGPSP | Pedregosa, Scieur; Cunha, Gidel, Pedregosa, Scieur, Paquette | Laguerre polynomials as optimal residual polynomials in average-case analysis | identification of the optimal polynomial (Lemma 4.1) (known) |
| Szego | Szego | zeros of Laguerre polynomials are real, positive and simple | positivity and simplicity of the optimal step sizes (known) |
| ACH, DHL | Arora, Cohen, Hazan; Du, Hu, Lee | balancedness is conserved under gradient flow of deep linear / homogeneous networks | the conserved imbalance k_i^2 - q_i^2 (known) |
| BRTW | Bah, Rauhut, Terstiege, Westdickenberg | gradient flow on the factors of a deep linear network is a Riemannian gradient flow of the product; it converges to a critical point, and from almost every initialization to a global minimum on a manifold of fixed rank | the flow of the products a_i as a gradient flow of F in the metric diag(h_i^{-1}) is the scalar case (Section 5) (known) |
| ColdingMinicozzi | Colding, Minicozzi | Lojasiewicz theorem (a bounded gradient trajectory of an analytic function has a unique limit) and the gradient inequality, form (0.2) | convergence of a bounded trajectory (Lemma 5.3) (known) |
| OSS | de Oliveira, Siami, Sontag | strict saddles, possibly a continuum of them, attract a Lebesgue null set (Appendix A, Theorem 3, Corollary 3) | almost-everywhere convergence (Theorem 2.1(iii)) (known) |

New in this paper: boundedness and convergence of every trajectory for untied factored scalar layers; every critical
point that is not a global minimizer is a strict saddle (Lemmas 4.2 and 5.2, via the coefficient map of prod(1 - a_i s));
almost-everywhere convergence to a global minimizer (Theorem 2.1); the exceptional initializations k_i = -q_i
(Remark 2.2); the flow of the products as a gradient flow of F in a metric set by the imbalances.

Codex (OpenAI, GPT-6.1) developed the proofs and the verification script; Claude Opus 5.5 (Anthropic) checked the proofs
and wrote the paper. The introduction and the AI declaration name the people above with these citations.
