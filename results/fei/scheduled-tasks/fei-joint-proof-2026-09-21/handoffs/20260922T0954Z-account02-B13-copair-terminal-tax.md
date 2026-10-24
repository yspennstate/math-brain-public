# Source-bound FEI handoff — account02/B13 co-pair terminal tax

Scientific source: `yspennstate/math-open-problems` report commit `85ffa60db26997421d980b1f86c03d82259504ca`, report
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`.
Checker source commit `eaec27488609f82279f47fef36dde45a762eae81`; executed output commit `e3ac12f362d8a5afeae21151f7a5ecb612ceb3f6`.

Status: `ESSENTIAL_STEP_APPLIED / JOINT_A-B_CONSTRAINT / MECHANISM_NO_GO / FULL_FEI_OPEN`.

Consumed completed other-account result: account04/B18 `20260922T081002Z-visible-hidden-curvature-split/REPORT.md`, in particular `kappa_ij=p_ij+4o_ij`, `omega_{i<-j}=p_ij-2c_{i<-j}+4o_ij`, and its explicitly unpaid raw hidden-curvature bank `U_4`. The latest account01/B18 MUX-newborn result was also read, but its universal use is incompatible with the corrected source state because it is tied to the fixed `Gamma^dagger`, which account01/B18's `CURRENT_OWNER_PIVOT_CORRECTED.md` refutes on the exact prime 18-input gate.

New exact co-pair theorem. For centered Boolean `f`, spectral sample `X`, pair `i!=j`, `r_ij=Pr(i,j in X)`, support disagreement `p_ij`, and opposite-sign overlap `o_ij`,

`kappa_ij=4 r_ij`, hence `r_ij=p_ij/4+o_ij`.

Physically reveal every coordinate except `i,j`. Every two-bit child is affine, with `H=P=J=F=0`, or non-affine, with `H=P=2,J=1,F=0`; the non-affine probability is exactly `p_ij`. Therefore

`E H(child)=2p_ij`, `E P(child)=2p_ij`, `E J(child)=p_ij`, `E F(child)=0`,

and the co-pair crossings are

`c_i=q_i-p_ij/2`, `c_j=q_j-p_ij/2`, `D_A=J-p_ij`.

This yields the exact physical/spectral constraints

`JS_A = H(X_i,X_j)-2p_ij >=0`,

and, with `a_i=j'(q_i)`,

`2p_ij+a_i(q_i-p_ij/2)+a_j(q_j-p_ij/2) <= j(q_i)+j(q_j)`,

as well as the global pair tax

`P >= H(X_i,X_j)+a_i(q_i-p_ij/2)+a_j(q_j-p_ij/2)`.

Thus the support-nonaffinity component of mixed curvature is locally phase-paid on an actual codimension-two physical restriction, while the opposite-sign orientation component is retained.

Tensor warning and genuine Boolean no-go. For a disjoint tensor cross-factor pair, `p=c=0` but `r=o=q_i q_j`, so raw hidden curvature already contains a quadratic tensor-orientation baseline. Qualitative tensor primitivity does not repair this. Let `phi` be the six-bit one-point defect (`phi(0^6)=-1`, otherwise +1), let `F_m=prod_{r=1}^m phi`, `N=6m`, and flip only `v=1^N` to obtain `G_m`.

For `phi`, every nonempty physical block has strict `K=4` all-block terminal margin `U_A-4D_A>0.075`. Tensor additivity gives the same for `F_m`. One-point surgery changes every block margin by less than `21 N 2^(1-N)<0.002884` for `m>=3`, hence every `G_m` remains all-block K=4 terminal.

Every `G_m` is tensor-primitive: for any nontrivial coordinate partition, a multiplicative 2x2 rectangle of product `-1` is explicit. If the partition is a union of whole six-bit factors, use the rectangle through the flipped point `v`; if it splits a factor, use the local rectangle around that factor's one-point defect, away from `v`.

Nevertheless, for every ordered cross-factor coordinate pair, `omega>=4(1/1024-2^(2-N))`. Hence

`U_4(G_m) >= 576 m(m-1)(1/1024-2^(2-6m))`,
`J(G_m) <= 6m(1/32+2^(1-6m))`,

so `U_4(G_m)/J(G_m) -> infinity` (asymptotically at least `(3-o(1))(m-1)`). Therefore

`all-block K=4 terminal + tensor-primitive => U_4=O(J)`

is FALSE with any dimension-independent constant. This does not refute FEI or a statement using full `rho>4` ratio-extremal criticality; the family is a low-ratio near-tensor family.

Next exact target: on a true `rho>4` minimum-dimensional F/J ratio core, use the co-pair identities plus criticality to control a tensor-centered orientation excess or build a nonreused selector. Do not attempt to pay raw `U_4` from terminality + qualitative primitivity alone.

Executed checker: 32,906 Boolean functions modulo global sign through n=4, 197,000 co-pair checks, zero identity error at executed precision and zero negative inequality slack; 131,071 nontrivial coordinate partitions of `G_3` each certified by a product-`-1` rectangle; infinite-family analytic perturbation bounds also checked numerically through m=10. Full FEI remains OPEN.
