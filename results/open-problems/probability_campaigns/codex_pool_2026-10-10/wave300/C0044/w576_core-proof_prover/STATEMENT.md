# C0044 statement sent before proof-route development

Fix an integer d >= 3 and a deterministic nonzero vector l in R^d. Let E = {+/-e_i: 1 <= i <= d}. At each x in Z^d let omega_x = (omega(x,e): e in E) be a probability vector. The rows omega_x are independent and identically distributed under an environment law P. Strict ellipticity means P(omega(x,e) > 0 for every x,e) = 1. Given omega, X_0=0 and P_omega(X_{n+1}=x+e | X_n=x)=omega(x,e). The environment is sampled once and retained. The annealed law is P_0 = integral P_omega^0 dP.

Set A_l = {lim_n X_n dot l = +infinity}. Target: P_0(A_l) is either 0 or 1. The uniformly elliptic subtarget additionally assumes a deterministic kappa>0 with omega(x,e)>=kappa for every x,e almost surely. Proving only that subtarget does not prove the strict-ellipticity statement.

The weaker Kalikow law is P_0(A_l union A_-l) in {0,1}; it does not exclude both opposite escapes having positive probability. The standard target is therefore equivalent, using that weaker theorem, to excluding P_0(A_l)>0 and P_0(A_-l)>0 simultaneously.

Primary recovery: Zerner (2007), arXiv:0706.0745, introduction, recalls the all-dimensional union law and distinguishes the stronger directional law. The public OpenAI mathematical manuscript linked by https://raw.githubusercontent.com/openai/math/main/lean/docs/220.md claims the strict-elliptic target as of September 23, 2026. This claim has not yet been mathematically verified in this packet. CURRENT OPENNESS: UNKNOWN, recent primary proof claim found.

This file contains the statement and source-status warning only; no proposed proof route was included in the first adversary handoff.
