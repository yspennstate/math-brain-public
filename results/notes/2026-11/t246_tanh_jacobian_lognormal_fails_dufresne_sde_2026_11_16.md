---
name: t246_tanh_jacobian_lognormal_fails_dufresne_sde_2026_11_16
description: "[PROVISIONAL] T246 Jacobian law for critical tanh at L/n->t: is log|Ju|^2 Gaussian like ReLU (Hanin-Nica)? Sketch says no: y=1/(nQ) is a linear SDE from 0 (Dufresne functional); variance 2t+Var(2I_t) matches chain (2.53 vs 2.56 at t=1, n=100); skew small (-0.06). Lead fillq_ctl/t246/LEAD_1116.md"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T16:41:42+02:00
  status: provisional
  evidence: ""
---

Status: provisional, by hand plus one quick numeric check (n=100, 1000 paths). Setting: critical tanh MLP, Gaussian weights N(0,1/n), u orthogonal to the input. Exact chain: Q_{l+1}=mean tanh(h_l)^2 with h_l iid N(0,Q_l); F_l=mean sech^4(h) g^2; log|J u|^2=sum log F_l. With z=nQ, s=l/n: dz=-2z^2 ds+sqrt2 z dB; y=1/z gives dy=(2+2y)ds-sqrt2 y dB, y(0)=0, so y is an exponential functional of Brownian motion (Dufresne/Yor). Prediction: log(L|J u|^2) -> sqrt2 W_t - 2[int ds/y - (1/2)log] with W independent of y. Measured (chain_check.py): variances 1.31/2.53 against SDE 1.32/2.56 at t=0.5/1; SDE skew -0.06 (3.5 se), chain skew within noise. Prior art: Li-Nica 2023 arXiv:2310.12079 do the correlation of unshaped MLPs (SDE singular at 0), not the norm or Jacobian; Li-Nica-Roy 2022 is the shaped case; Hanin-Nica 2020 ReLU log-normal. What would change it: a paper with the tanh Jacobian at proportional depth; a larger-n chain whose variance drifts away from the SDE. Next: n=200-400 on a Mac, exact Var(I_t), 90-day arXiv search.

Update 16 Nov 17:17 (a second machine GPU, MLX chain n=800 x 16000 paths vs exact-scheme SDE x 200000): variance matches to 1% at t=0.5..8
(1.29, 2.53, 4.88, 9.30, 17.63 against 2t = 1, 2, 4, 8, 16); excess 4Var(I_t) = 2t/3 - 0.15t^2 + ..., saturating ~1.6-1.8.
Skew real but tiny (SDE -0.053 +- 0.0055 at t=2, peak near t=2-4, decays), excess kurtosis ~0. An Euler SDE with a floor at
y=0 gave a spurious flat skew -0.06: use the exact scheme y' = r y + dt(1+r), r = exp(dt - sqrt2 dB). Lead file:
fillq_ctl/t246/LEAD_1116.md; scripts mlx_chain_t.py, sde_exact.py there.

Update 16 Nov 17:3x (closed form, checked): since y_s = Phi_s A_s with A_s = 2 int_0^s exp(sqrt2 B_r - r) dr, dlogA/ds = 2/y_s, so 2I_t = log(A_t/2t) exactly and the limit is sqrt2 W_t - log A_t (W independent). Dufresne: A_t -> 2/E with E ~ Exp(1), so for large t |Ju|^2 is log-normal times an independent exponential; Var = 2t + Var log A_t, which rises from 2t/3 to pi^2/6; limiting third cumulant -2 zeta(3). Matches chain to 1% at n=200, 400, 800 (a second machine GPU jobs 31-33) and a direct simulation of log A_t (fillq_ctl/t246/dufresne_check.py). Still provisional: the convergence theorem is a proof route, not a proof (LEAD_1116.md 17:3x).
