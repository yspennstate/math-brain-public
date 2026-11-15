# T245 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Receipt: 15 November 2026, 05:11 Asia/Tbilisi.

## Orientation and restrictions

Read the startup memory, compute state, both earlier REPORT.md, LOG.md, PROOF.md and verify.py files. Earlier folders are read-only. The current folder-only instruction overrides global requests to write checklist, mesh, recall logs, or brain memories. No subagents, git, external messages, or outside-folder writes. Compute state was warn / owner_away_open, CPU saturated; calculations will be small, standard-library, one thread, OMP_NUM_THREADS=1, nice -n 15, under 1 GB and 20 minutes. The previous runs inherited nice priority 20; scripts will check priority directly.

## Bounded literature check, 05:11–05:13 Asia/Tbilisi

Used the web search tool for simultaneous depth/width NTK training limits, recent 2025–2026 work, and balanced deep-linear dynamics. Opened primary sources:

- Boris Hanin, Mihai Nica, *Finite Depth and Width Corrections to the Neural Tangent Kernel*, https://arxiv.org/abs/1909.05989.
- Jiaoyang Huang, Horng-Tzer Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, https://arxiv.org/abs/1909.08156.
- Qiyang Han, Masaaki Imaizumi, *Precise gradient descent training dynamics for finite-width multi-layer neural networks*, https://arxiv.org/abs/2505.04898. Width and depth remain bounded in its proportional regime.
- Blake Bordelon, Cengiz Pehlevan, *Deep Linear Network Training Dynamics from Random Initialization: Data, Width, Depth, and Hyperparameter Transfer*, ICML 2025, https://pehlevan.seas.harvard.edu/sites/g/files/omnuum6471/files/2025-06/Bordelon%26Pehlevan_ICML_2025.pdf. The abstract distinguishes its residual infinite-depth limit.
- Zihan Yao, Ruoyu Wu, Tianxiang Gao, *Feature Learning Dynamics in Infinite-Depth Neural Networks*, https://arxiv.org/abs/2512.21075; residual setting already distinguished by the previous worker.
- Andrea Combette, Nelly Pustelnik, Antoine Venaille, *Correlation flow governs learning at criticality*, https://arxiv.org/abs/2608.08350.
- Nadav Cohen, Govind Menon, Zsolt Veraszto, *Deep Linear Networks for Matrix Completion -- An Infinite Depth Limit*, https://arxiv.org/abs/2210.12497, and its full HTML https://arxiv.org/html/2210.12497v2.
- Armin Eftekhari, *Training Linear Neural Networks: Non-Local Convergence and Complexity Results*, https://proceedings.mlr.press/v119/eftekhari20a/eftekhari20a.pdf.

No solution of the original Gaussian ReLU joint training-law problem found. This bounded search is not evidence of absence. Balanced end-to-end deep-linear flows and their infinite-depth metric are existing mathematics, so the extension below will not claim novelty for those formulas. No SOLVED_ELSEWHERE.md: the whole-problem stop condition was not met. Literature search ends here, within five minutes.

## Earlier result independently re-derived, before extension

In Theta coordinates each layer contributes n^{-1} times the squared backward-vector norm times the forward-vector inner product. With W_l=s_l(D_l on E, identity on E-perp), D_l=I+C_l/n, prefixes Q and suffixes R, this gives exactly

M_n=(S_n^2/n) sum_l s_l^{-2} ||R_l^T e||^2 Q_{l-1}^T Q_{l-1},
B_n=(S_n^2/n) sum_l s_l^{-2} ||R_l^T e||^2.

The active update is C_l^+=C_l-eta S_n s_l^{-2} R_l^T e (Q_{l-1}g_n)^T. Thus the previous profile recursion and full kernel have the right order and normalization. For its nilpotent example C_1=(eta/2)e_1 e_2^T, direct integration of (1+eta^2(1-z)^2/4) times [[1,eta z/2],[eta z/2,1+eta^2 z^2/4]] gives exactly its M_1 polynomial. Its C_2,22=eta^2(1-eta)(1-z)/4 and endpoint commutator entry eta^6/32 also follow from the update. The earlier result holds at this algebraic recheck. Independent exact rational and numerical checks will be saved below.

## Extension chosen before calculation

Prove a finite-dimensional closure for the small-step limit of the earlier matrix profile, on finite training intervals. Balanced gradient flow is the concrete next step named by the previous report. The candidate state is the end-to-end active matrix P and the bias b; its operator is an integral of left/right matrix powers. The work needed is to connect that known balanced operator to the previous profile with unequal scalar gains, recover the full perpendicular test kernel, and quantify why discrete GD cannot use the closure exactly. Do not infer balancedness of discrete GD from conservation under gradient flow. The original Gaussian/ReLU question remains outside scope.

## Proof saved before numerical verification

Created PROOF.md. The key identity is D(C)=(C+C^T)_z-t[C,C^T], with D_tau=0 along the profile flow. It implies A_zz=A_z A^{-1}A_z for A=U^TU, hence U^TU=(U(1)^TU(1))^z and VV^T=(U(1)U(1)^T)^(1-z). The endpoint state P=S U(1) therefore satisfies the finite-dimensional balanced operator equation. Both kernel coefficients, including the perpendicular coefficient, are functions of P and the fixed S.

A loss-dissipation argument gives global existence: D=g^TMg and ell_dot=-h^2-D. In an eigenbasis of H=P^TP, D>=t v_i^2 g_i^2, v=P^Te, and (log lambda_i)_dot=-2t v_i g_i. Cauchy--Schwarz gives |log(sigma_i(P)/S)|<=sqrt(t tau ell_0), with |b|<=sqrt(tau ell_0). This rules out finite-time explosion and loss of invertibility, including for data that do not span the active space. The profile itself then stays bounded in C^1 on finite intervals, so its Euler recursion converges there.

For discrete GD, direct expansion gives D(C+eta G)=D(C)-t eta^2[G,G^T], an exact identity. In the previous nilpotent example [M_1,P_1^TP_1]_(1,2)=eta^3/48+eta^5/640; the balanced formula always commutes with P^TP. Thus it is invalid as an exact discrete kernel formula, while its error goes to zero on fixed continuous training intervals. These statements are to be checked with exact rational arithmetic, direct finite-layer flow, and the previous profile code run read-only from this folder.

## First independent verification, 05:19 Asia/Tbilisi

Created verify.py. Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
```

Exit code 0; all checks passed. The old profile module was imported with bytecode disabled and its main function was not called; it reads from the previous folder and writes nothing there. Complete output is verification_output.txt and data are verification_data.json.

- Exact Fraction calculations at eta=1/5,2/5,7/8 reproduce M_1, C_2,22 and the earlier eta^6/32 commutator. They also verify the new eta^3/48+eta^5/640 kernel commutator and the exact first balance defect.
- Logarithmic-mean spectral evaluation versus separate depth quadrature: maximum error 2.241e-12. Initial rate from endpoint finite differences versus the preceding formula: 2.152e-10.
- The wrong discrete balanced prediction has M_22 discrepancy/eta^2 = 0.04166667535 and B discrepancy/eta^2 = 0.02083329210 at eta=.005, approaching 1/24 and 1/48 as independently derived.
- Direct finite-layer RK4 flow uses raw trainable 2 by 2 matrices and computes the kernel from all layer products, without the endpoint closure. At n=256, full-state errors versus (3)--(5) were .0013645, .00032594, .0021251 for (t,S)=(.5,.7),(1,1),(2,1.3). Factor-4 size refinement reduced errors by about four. Maximum balancedness drift was 3.27e-13.
- Unequal near-identity gains and their reversals approach the same endpoint law: maximum errors .0137633,.0034331,.0008580 at n=32,128,512. These are deterministic gain arrays, not iid Gaussian matrix experiments.
- Earlier discrete depth profile at training time .4 approaches the endpoint flow: errors .0034993,.0017230,.0008550,.0004259 at eta=.04,.02,.01,.005. Depth grids 64 and 128 differ by 4.609e-8 in the finest time-step case.
- Scalar invariant, scalar perpendicular kernel, zero-residual stationary state, zero-input bias-only state, positive and negative initial residuals passed. Loss dissipation versus a central derivative of the actual squared loss differs by 4.130e-12.
- Resources: .957 seconds, 24,625,152 bytes peak RSS, one thread, priority 20. The macOS `nice: setpriority: Operation not permitted` warning reflects inherited priority 20, checked directly by the script.

The finite-size and Euler errors are numerical diagnostics, not rigorous error constants. The proof gives convergence and a finite-time bound with constants depending on S, t, data and T.

## Attempt to break the proof

Rechecked the sign in the balancedness invariant by expanding A_zz: the commutator cancels exactly the extra C^T C term, leaving (C+C^T)^2. Re-derived the endpoint normalization from the finite-layer physical product: two scalar Gram powers cancel the factor S^2; the perpendicular forward factor instead leaves S^(2z). Re-derived the singular-value bound from log lambda_i (rather than log sigma_i) to check the factor two. Eigenvalue multiplicities are handled by diagonalizing H_dot within the repeated eigenspace, not by differentiating a chosen SVD basis. The loss argument does not require full-rank or affinely spanning data. The discrete first-step kernel commutator is positive for every eta>0, so no exceptional positive learning rate rescues the balanced formula in that example.

Next verification will compare the raw finite-layer kernels with the exact finite-depth balanced matrix-power sum, and check the finite-layer discrete balance defect by exact rational arithmetic. These are independent checks of the two main bridges in the argument.

## Second verification and final report

Extended verify.py with an exact rational check of adjacent finite-layer balance defects and a comparison of raw finite-layer kernels with the exact finite-depth matrix-power sum. Added the corresponding second derivation of the defect sign and scaling to PROOF.md. Reran the same command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
```

Exit code 0, all checks passed. Exact finite-layer balance change at eta=1/6, n=7 was
`[1259/6350400,4327/66679200,4327/66679200,-1156031/25204737600]`, identical to the independently expanded quadratic gradient expression. Raw finite-layer kernel versus its finite-depth balanced power sum differed by at most 1.126899e-10. All preceding mathematical outputs remained unchanged. Final resource measurements: 1.041064 seconds, 25,247,744 bytes peak RSS, OMP_NUM_THREADS=1, priority 20.

Saved REPORT.md with verdict PARTIAL, the full output/kernel closure, limit order, global singular-value bound, exact discrete obstruction, verification commands, failures and remaining questions. There is no assertion of a fixed-eta finite-dimensional reduction or an iid Gaussian/ReLU law. Existing balanced-operator literature is explicitly credited. No outside-folder edits, git commands, subagents, or external messages were used.

Final read-only audit: `OMP_NUM_THREADS=1 nice -n 15 python3 -` with a short inline script checked that all six artifacts exist, contain no control characters, that Markdown display delimiters balance, that REPORT.md starts with `VERDICT: PARTIAL`, and that verification_output.txt ends with successful checks. Output: `Artifact audit passed.` File sizes before this log append: REPORT.md 5739 bytes, PROOF.md 18036, LOG.md 10897, verify.py 16695, verification_data.json 5777, verification_output.txt 3955. `rg -n 'VERDICT|global|simultaneous|Gaussian|Task:|mathcal D|failed|Next worker' REPORT.md PROOF.md LOG.md` confirmed the verdict, explicit limit-order and scope qualifications, defect formulas, next step and task attribution. No computation rerun was needed after the final prose-only proof expansion.
