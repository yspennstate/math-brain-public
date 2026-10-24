# account04/B04 FEI handoff — all-bias closure from interior certificates

Run: `20260922T111423Z-account04-B04-fei-allbias-r1`  
Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Full FEI: `OPEN_NOT_PROVED`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Recipient: `account02/B01`

## Immutable source

Repository: `yspennstate/math-open-problems`  
Commit: `f67082daddbe87d682ddb808ec7bffa52bf05a7a`  
Report: `proofnet24/P03-fei/fleet-2026-09-22/account04/B04/20260922T111423Z-account04-B04-fei-allbias-r1/REPORT.md`  
Report blob: `e6c2c4e372f67e0cd51c8ec9af10bda80d149157`  
Claims blob: `7b773f180fd314cda28c68f53305fdbb9ddfe9c6`  
Checker output blob: `c43268a713afbeaa8d0b580eab37ef5517f49e12`

## Result

For any finite Boolean gate and any one continuous symmetric endpoint-normalized common potential, rewrite the gate defect exactly as
[
D_\Gamma(G;p)=\sum_i d_i(p_{-i})[\Gamma(p_i)+h_2(4p_i(1-p_i))]-\Gamma(q_G(p))-\widetilde H_G(p),
]
where (d_i) is the genuine original-coordinate disagreement probability. This removes the apparent (\operatorname{It}_i/V_{p_i}) singularity.

On every boundary face, the defect is exactly the defect of the contracted gate with the same potential. Constant zero-variance restrictions have defect zero. An explicit closed-cube modulus is proved using product coupling, the angle metric (\arcsin\sqrt p), and the finite-alphabet (x\log x) entropy bound. Therefore exact nonnegativity on any dense interior set (including rational biases) extends to every bias. A finite mesh is valid only when its certified margin pays the displayed modulus.

The assigned partner account01/B04 is applied to characterize tight faces. If (D_0=0), its exact cancellation expansion gives
[
D_\Gamma(G;t)=tF_0+o(t),
quad
F_0=(D_1-D_0)+J_\Gamma(q_0,q_1)+d\gamma_0+E_0(u,v).
]
Any valid dense interior certificate must have (F_0\ge0); (F_0<0) generates genuine negative interior biases. For a constant limiting child this becomes the explicit necessary condition
[
D_\Gamma(G_1)+\Gamma(d)+E_{\rm const}(d)\ge0.
]

## Fresh correction check

The post-proof inbox event `FEI-B01-FIXED-CREDIT-RESERVE-NOGO-v1` was consumed. It blocks a fixed positive (K_{occ}) reserve and is not a premise of this theorem. The safe-cone selector floor remains `NEEDS_REVALIDATION`.

## Next use

Use the report's modulus as the enclosure rule for exact Bellman/gate interior certificates. Enforce the contracted-face and (F_0/F_1) conditions before claiming all-bias coverage. This theorem closes only the continuum-extension step; no common potential is yet certified for all gates/arities.
