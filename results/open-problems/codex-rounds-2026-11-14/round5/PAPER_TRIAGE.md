# Round 5 paper triage (an agent, for

15 Nov 2026 (JST).

- T347: not a paper. Hopfield exclusion radius about 1.9e-8. It is not sharp, and the worker claims no improvement.
- T325: paper candidate. Almost-sure global convergence of population gradient flow for factored scalar linear attention at every depth L. The limit is L empirical GD steps, with risk 2^L L!/prod(N+2j). Literature checked by the worker: arXiv 2506.05249, 2410.08292 and 1605.00405. Still to check: Ahn et al. 2023 and Zhang-Frei-Bartlett 2023.
- T248: weak candidate for a short note only.
  - Result: TW1 with deterministic finite-size centering for the projected kernel Y(I-ee^T)Y^T/N, with spherical inputs, a Lipschitz activation with a0=a1=0, and any a2. This covers the quadratic-spike regimes that round 4 excluded.
  - The universality input is Chen-Lyu arXiv:2610.41416v2, Corollary 1.4, used as stated. The new parts are an edge lemma with a nonzero trace defect and the projection bookkeeping.
  - Before writing:
    - confirm that 2610.41416 exists, and its authors and title;
    - check that Corollary 1.4's hypotheses match;
    - check whether Fan-Montanari, Benigni-Peche or Wang-Zhu already cover the projected kernel.
  - The full T248 problem (the unprojected kernel) is still open.

T325 scope (read 15 Nov):
- Model: d=1 scalar attention with L untied layers. Only the 2L key/query factors are trained; values are fixed. This is not softmax.
- Result: gradient flow converges outside a Lebesgue-null set of initializations. Every nonglobal critical point is a strict saddle. The anti-balanced k=-q start is a genuine exception (it converges to the zero-product saddle, risk 1).
- Gatmiry-Saunshi-Reddi-Jegelka-Kumar (looped transformers) is already cited in PROOF.md.
- Size: a short note, not a full paper. The intro must say plainly that the setting is a scalar toy model.
- Asked an agent on the mesh (topic paper-lane/T325) at 08:2x JST. If there is no answer by 12:00 JST, I draft it myself.

T325 literature check (15 Nov, read from arXiv and JMLR listings, abstracts only):
- Ahn, Cheng, Daneshmand, Sra, arXiv 2306.00297 (NeurIPS 2023). A landscape result: for one layer the global minimum is one preconditioned GD step; for L layers, certain critical points are L steps. It proves no convergence of the training dynamics.
- Zhang, Frei, Bartlett, arXiv 2306.09927 (JMLR 25, 2024). One linear self-attention layer: gradient flow from a suitable random initialization reaches the global minimum. One layer only.
- Gatmiry et al., arXiv 2410.08292. Looped (weight-shared) multi-layer model: gradient flow converges via gradient dominance. The authors leave open whether the stationary point implements multi-step GD. This is the closest prior work, and T325 already cites it.
- Not yet read: the ICLR 2024 multi-layer LSA paper (prefix vs causal mask, multi-step GD). It must be read in full before posting.
- Verdict: T325's untied-layers, both-factors, almost-every-initialization result, with the exact limit, looks new. It is still a d=1 toy model. Write it as a short note, credit these four in the introduction and the AI declaration (C17-C26), and state the scalar restriction in the abstract.
