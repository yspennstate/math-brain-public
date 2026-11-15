# F0119 literature audit

Checked 2026-11-13. Page numbers refer to the **saved PDF version**, not an
assumed correspondence with journal pagination. Plain-text sources include
page delimiters; matching metadata identifies the downloaded bytes.

OpenAI's September 25, 2026 public preprint, Theorem 1.1, PDF page 3,
covers every regular \(b\ge2\), both signs, including equality and colouring.
It states reconstruction iff \(b\lambda^2>1\), and activates the requested
literature-stop rule. Journal acceptance was not established. The
regular-tree certificate subset was replayed; see REPORT.md.

| Primary source | Exact location | Scope and implications |
|---|---|---|
| [Mossel, *Survey: information flow on trees* (2004), math/0406446](https://arxiv.org/abs/math/0406446) | Definition 2.1, pp. 2–3; Proposition 2.1, p. 3; Theorem 4.1, pp. 6–7; equation (8), p. 7; Problem 1, p. 8; bounds, pp. 8–9; subsections 5.1–5.2, p. 10 | Exact original problem. KS sufficiency; impossibility if \(b|\lambda|\le1\) or \(3b\lambda^2/(2+\lambda)\le1\). Page 7 also records census impossibility at equality for Potts channels. |
| [Mossel–Peres, *Information flow on trees*, Ann. Appl. Probab. 13 (2003), 817–844; math/0107033](https://arxiv.org/abs/math/0107033) | Proposition 1.3, pp. 4, 11; Theorem 1.4, pp. 4, 15; Theorems 1.5–1.6, p. 4 and Sections 6–7, pp. 16–22 | Revealing-colour criterion; KS sufficiency on general trees; census impossibility below KS and at equality for Potts/asymmetric Ising. Theorem 1.6 in this preprint omits “census” from its statement; its section title and proof concern census vectors. It must not be used as full impossibility for all Potts channels. |
| [Sly, *Reconstruction for the Potts model*, Ann. Probab. 39 (2011), 1365–1406; preprint *Reconstruction of symmetric Potts Models*, 0811.1208](https://arxiv.org/abs/0811.1208) | Theorems 1.1–1.2, p. 4; Section 1.5, equation (1.1), pp. 6–7 | Three-state KS exact for both signs, including equality, for sufficiently large \(b\ge d_{\min}\). No explicit small-degree cutoff. Non-sharpness for \(q\ge5\) is not a three-state counterexample. The question's 0905.3797 identifier is unrelated. |
| [Sly, *Reconstruction of Random Colourings*, CMP 288 (2009), 943–961; 0802.3487](https://arxiv.org/abs/0802.3487) | Theorem 1, p. 3 | Large-\(q\) colouring asymptotics: impossibility below \(q[\log q+\log\log q+1-\log2-o(1)]\), reconstruction above \(q[\log q+\log\log q+1+o(1)]\). Not an explicit fixed-three-colour theorem. |
| [Mézard–Montanari, *Reconstruction on trees and spin glass transition*, JSP 124 (2006), 1317–1350; cond-mat/0512295](https://arxiv.org/abs/cond-mat/0512295) | Sections IV–V, pp. 16–20; Conjecture 2 and following paragraph, p. 30 | Cavity evidence for KS sharpness for three states of either sign, and four-state ferromagnetic channels. Conjecture 2 has a branching cutoff; the next paragraph proposes all degrees. Predictions are distinct from impossibility proofs. |
| [Bhatnagar–Vera–Vigoda–Weitz, *Reconstruction for Colorings on Trees*, SIAM JDM 25 (2011), 809–826; 0711.3664](https://arxiv.org/abs/0711.3664) | Theorem 1.2, p. 2 | For fixed \(C>1\), sufficiently large \(\Delta\) and \(q>C\Delta/\log\Delta\), exponential non-reconstruction. Does not settle the three-colour, four-child endpoint. |
| [Bhatnagar–Maneva, *A Computational Method for Bounding the Probability of Reconstruction on Trees*, SIAM JDM 25 (2011), 854–871; 0903.4812](https://arxiv.org/abs/0903.4812) | Theorem 12 and proof, pp. 17–18; Table 1, p. 18 | Certified impossibility at \(b=2,0<\lambda\le0.69\), \(b=3,0<\lambda\le0.555\), and \(b=3,\lambda=-1/2\). Item 2 says “reconstruction” in v1; the surrounding text, proof and table establish non-reconstruction. The colouring conclusion extends to weaker negative channels by degradation. |
| [Martinelli–Sinclair–Weitz, *Fast mixing for independent sets, colorings and other models on trees*, RSA 31 (2007), 134–172](https://www.drorweitz.com/ac/pubs/fast_tree.pdf) | Theorem 9.3, p. 29; variants, p. 30; Theorem 9.8 and Lemma 9.9, pp. 33–34 | General \(b\kappa\gamma<1\) criterion. Theorem 9.8 improves the revealing-colour bound by a positive channel-dependent factor. No all-degree equality classification. Saved author manuscript is dated November 29, 2004. |
| [Borgs–Chayes–Mossel–Roch, *The Kesten-Stigum Reconstruction Bound Is Tight for Roughly Symmetric Binary Channels*, FOCS 2006; math/0604366](https://arxiv.org/abs/math/0604366) | Theorem 1, p. 3 | For each \(b\ge2\), sufficiently small binary asymmetry gives impossibility at \(b\theta^2\le1\). Addresses the external-field Ising comparison, not a three-state proof. |
| [Liu–Ning, *Reconstruction for the Asymmetric Ising Model on Regular Trees*, 1712.00395](https://arxiv.org/abs/1712.00395) | Theorems I.1–I.2, p. 2 | Binary asymmetry criterion \(\Delta^2\gtrless(1-\theta)^2/3\). The small-asymmetry KS-sharpness result assumes sufficiently large degree and includes equality. |
| [Liu–Ning, *Large Degree Asymptotics and the Reconstruction Threshold of the Asymmetric Binary Channels*, 1812.06039](https://arxiv.org/abs/1812.06039) | Theorems 1.1–1.3, p. 4 | Binary stationary weights \(\pi_1\pi_2<1/6\): KS not sharp; \(\pi_1\pi_2>1/6\): sharp for sufficiently large degree. These strict cases do not settle \(\pi_1\pi_2=1/6\) or all external fields at every degree. |
| [Formentin–Külske, *A symmetric entropy bound on the non-reconstruction regime of Markov chains on Galton-Watson trees*, ECP 14 (2009), 587–596](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1516/1516-5159-1-PB.pdf) | Theorem 2.1, PDF p. 4 = printed p. 590; Proposition 3.3, equation (15), PDF p. 7 = printed p. 593 | Impossibility when \(b c(M)<1\), using a variational symmetrized-entropy contraction coefficient. Exact entropy recursion used by the 2026 proof; not all small-degree equalities. |
| [Ricci-Tersenghi–Semerjian–Zdeborová, *Typology of phase transitions in Bayesian inference problems*, 1806.11013](https://arxiv.org/abs/1806.11013) | Section III.D.1, pp. 15–16; Section IV.D, pp. 22–26; IV.H, pp. 30–32; equation (100), p. 31 | Local cavity expansion with coefficient \(q(q-4)\); three states and borderline four states differ. Perturbative and numerical evidence does not exclude a distant informative fixed point. |
| [Gu–Polyanskiy, *Non-linear Log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems*, CMP (2023); 2005.05444](https://arxiv.org/abs/2005.05444) | Theorem 3 and equation (14), p. 7; Theorem 6, p. 9 | Explicit improved region \(b\eta_{\rm KL}(P_\lambda,\pi)<1\) for either sign. Here \(\eta_{\rm KL}=\sup_{x\in(1/3,1]}\psi(\lambda x+(1-\lambda)/3)/\psi(x)\), \(\psi(x)=\log3+x\log x+(1-x)\log((1-x)/2)\). Not full all-degree KS sharpness. |
| [Gu–Polyanskiy, *Uniqueness of BP fixed point for the Potts model and applications to community detection*, COLT 2023, PMLR 195, 837–884](https://proceedings.mlr.press/v195/gu23a.html) | Theorem 1, PDF p. 4; Theorem 2, p. 5 | BP uniqueness and boundary irrelevance under specified conditions, not unconditional all-degree non-reconstruction. |
| [Mossel–Sly–Sohn, *Exact phase transitions for stochastic block models and reconstruction on trees*, Ann. Probab. 53 (2025), 967–1018; 2212.03362](https://arxiv.org/abs/2212.03362) | Assumptions 1.10–1.11 and Theorem 1.12, p. 5 | Under offspring-tail/tightness hypotheses, three and four states have KS sharpness for sufficiently large mean degree, either sign, including equality. Includes Poisson and deterministic offspring; still a large-degree restriction. |
| [Galanis–Goldberg–Yang, *Uniqueness for the 3-State Antiferromagnetic Potts Model on the Tree*, EJP 23 (2018), paper 82; 1804.03514](https://arxiv.org/abs/1804.03514) | Theorem 2, p. 4 | Worst-boundary Gibbs uniqueness: edge weight \(w\ge(b-2)/(b+1)\) for \(b\ge3\), and \(w>0\) for \(b=2\). Since \(\lambda=(w-1)/(w+2)\), this boundary is \(b|\lambda|=1\), distinct from reconstruction KS. |
| [Chenlin Gu–Wu–Yang, *Power law decay at criticality for the q-state antiferromagnetic Potts model on regular trees*, 2112.00573](https://arxiv.org/abs/2112.00573) | Hypothesis 1.1, p. 2; Theorem 1.2, p. 3 | Critical decay exponent \(1/2\), conditional on uniqueness, at the Gibbs uniqueness threshold. Chenlin Gu is one author, distinct from Yuzhou Gu. Does not settle reconstruction at KS. |
| [Zongchen Chen–Galanis–Goldberg–Mifsud–Smolarova–Zhang, *Fast Mixing for Low-Temperature Potts Models via Poisson Trees*, 2607.29495](https://arxiv.org/abs/2607.29495) | Theorems 1–2, p. 3 | Large-\(q,d\) sampling/mixing with monochromatic boundary on Poisson trees; not the free-boundary three-state reconstruction classification. |
| [OpenAI, *The exact reconstruction threshold for the three-state symmetric channel*, September 25, 2026](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026) | Theorem 1.1, p. 3; proof, p. 33; verification programs, Appendix D, pp. 48–60 | All regular \(b\ge2\), both signs, including equality and colouring. Reconstruction iff \(b\lambda^2>1\). The reference activating the requested stop. |

The ambiguous “Chen–Gu–…” fragment was searched directly and through
related titles. No joint-author paper was inferred without an identifiable
reference. Specific relevant Gu and Chen works found are listed above.

The original revealing-colour interval is
\[
\left[\frac{1-\sqrt{1+24b}}{6b},
      \frac{1+\sqrt{1+24b}}{6b}\right]\cap[-1/2,1].
\]
For \(b=2\), it includes the entire negative side and the positive side
through \(2/3\). For \(b=3\), Bhatnagar–Maneva settles negative colouring
and hence all weaker negative channels. Sly's stated theorem cannot close
the small-degree positive gaps, and none of those three references covers
\(b=4,\lambda=-1/2\). The 2026 theorem covers them directly.

Searches combined “three-state/3-state Potts”, “binary/small-degree tree”,
“reconstruction”, “Kesten–Stigum”, “antiferromagnetic”, “Chen”, “Gu”, and
2011–2026 dates, besides the named authors and titles. Secondary trackers
were discovery leads only. The resolving claim was read in the primary
manuscript, not inferred from a tracker or a partial Lean statement.
Searches for corrections/counterexamples identified no primary correction
to that manuscript during this audit; this is not journal certification.
