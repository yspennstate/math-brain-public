# T384 rotated two-input hybrid geometry

## Deterministic classification

Consider the proposed positive-time, absorbing hybrid law with fixed symmetric positive-definite `C=[[c11,c],[c,c22]]`, `c>0`, selected first-layer masses `A1,A2>0`, and strict initial residual `r0=(r10,r20)` with neither component zero. Initially

`K=C+diag(A1,A2)=[[a,c],[c,b]]`, `a,b>0`, `ab>c^2`,

`r(t)=e^(-Kt)r0`, `J(t)=int_0^t r(s)ds=K^(-1)(I-e^(-Kt))r0`.

An initial-sign population in coordinate `j` is retained until the **first positive return** of `J_j` to zero, if any, and is then removed irreversibly. This ideal law has **at most one later switch**. Any switch is unique and transversal, and after it no other population can switch. No finite-time grazing, simultaneous switch, or chattering is possible under the displayed hypotheses.

If `r10` and `r20` have opposite signs, there is no later switch. For example, if `r1>0>r2`, put `z=(r1,-r2)`. For every phase, even with time-dependent diagonal gate masses,

`z'=[[-d1,c],[c,-d2]]z`, `d1,d2>=0`.

This Metzler system leaves the positive orthant strictly invariant. Thus `r1(t)>0>r2(t)` and `J1(t)>0>J2(t)` for all `t>0`. The reversed sign pattern is identical.

For same-sign initial residuals, multiply by their common sign and write `u=|r10|>0`, `v=|r20|>0`. The hypothetical constant-first-phase integrated limit is

`K^(-1)(u,v)^T=((b u-c v),(a v-c u))^T/(ab-c^2)`.

Consequently the complete switch classification is

| Ratio `v/u` | Hybrid outcome |
|---|---|
| `v/u>b/c` | Coordinate 1 loses `A1` at one finite time. |
| `v/u<c/a` | Coordinate 2 loses `A2` at one finite time. |
| `c/a<=v/u<=b/c` | No finite gate loss after the initial layer. |

The thresholds are ordered, `c/a<b/c`, exactly because `c^2<ab`. Equality is a boundary case: one integrated component tends to zero only as `t->infinity`, never returns at finite time. In the actual rotated stable law, `c11>c` and `c22>c` almost surely, so `a>c,b>c`; the switch thresholds lie below and above 1 respectively. Sufficiently balanced same-sign residuals therefore have no later switch.

To prove the finite-return criterion and transversality, diagonalize `K`, whose eigenvalues `0<lambda_-<lambda_+` are distinct because `c>0`. Each residual component has the form

`r_j(t)=p_j e^(-lambda_- t)+q_j e^(-lambda_+ t)`.

Since `e^(lambda_- t)r_j(t)=p_j+q_j e^(-(lambda_+-lambda_-)t)` is monotone, `r_j` can change sign at most once. It starts with the positive common sign. Therefore `J_j` either increases forever or first increases and then decreases strictly. It has a finite positive return to zero **iff** its limit `(K^(-1)r0)_j` has the opposite sign. At that return `r_j(t_*)=J_j'(t_*)` is strictly opposite the initial sign; the crossing is transversal. The two integrated limits cannot both oppose the common initial sign, because that would require simultaneously `cv>bu` and `cu>av`, implying `c^2>ab`.

At the first residual sign crossing, the other residual retains its original sign; both cannot reach zero together because the linear flow is invertible. Thereafter the mixed-sign orthant is invariant by the same Metzler transform. Hence at the later **integrated** crossing `t_*`, the residuals have strict opposite signs. Removing `A_j` changes only a diagonal entry, so the mixed-sign orthant remains invariant under `K'=K-A_j e_je_j^T`, which is still positive definite. The switched coordinate's `J_j` moves strictly farther past zero and the other `J_k` remains on its original side. This rules out reactivation and a second switch. These conclusions do not depend on an explicit formula for `t_*`.

The switch time, when present, is locally smooth in `(r0,C,A)` by the implicit-function theorem applied to `J_j(t_*)=0`, because `r_j(t_*)!=0`. It tends to infinity as the ratio approaches the corresponding no-switch threshold; there is no finite-time grazing at that threshold.

## Almost-sure nondegeneracy for the rotated stable initialization

The joint-initialization law in the prior run has `C=[[S0+S1,S0],[S0,S0+S2]]/2` with independent positive stable `S` variables, so `c=S0/2>0` and `C` is SPD almost surely. The selected `A_j` are positive almost surely because each relevant marked Poisson cloud has infinitely many positive small atoms but finite summed squares. The initial residual `r0=y-F` has an everywhere-positive two-dimensional density and is independent of `(C,N)`, while `A` depends on `N` and the sign orthant of `r0`.

Condition on `(C,N)` and partition by the four possible strict sign orthants. In each orthant the selected `A` and hence `K` are fixed. The events `r10=0`, `r20=0`, `b|r10|=c|r20|`, or `a|r20|=c|r10|` lie on finitely many lines and have conditional probability zero under the density of `F`. Thus almost surely the hybrid law is in exactly one of the strict cases above. For any fixed deterministic `T>0`, the event `t_*=T` also has probability zero: for fixed `K`, `J_j(T)=e_j^T K^(-1)(I-e^(-KT))r0` is a nonzero linear equation in `r0`. The same applies to a fixed `delta`.

## Implications for a full finite-width theorem

The local-clock proposition in the prior `agents/c01.md` already controls the path uniformly up to `t_*-epsilon`, or on all `[0,T]` in a no-switch case. On a switch event localized so `t_*` is separated from `0,T` and `r_j(t_*)` is bounded away from zero, the interval `[t_*-epsilon,t_*+epsilon]` has length `2epsilon` and both the true and candidate residuals have uniformly bounded derivatives. Their residual discrepancy across that interval is `o_P(1)+O(epsilon)`; the **integrated** discrepancy is `o_P(1)+O(epsilon^2)`. Since the candidate `J_j(t_*+epsilon)=r_j(t_*)epsilon+O(epsilon^2)<-c_0 epsilon`, the actual accumulated displacement is negative there for small fixed `epsilon` and large `m`. An active large supporting `W` gate at that time would require its initial `V_ij(0)` to be of order `epsilon L_m`, whose unconditional probability is `O(1/log m)` after the usual `W`-extreme union bound. The other coordinate's accumulated displacement stays positive, so its supporting large gates survive. Small initial `W` mass and total moved squares are negligible. This gives `K_m(t)` close to `K'` for `t>=t_*+epsilon`, while variation of constants and the mixed-sign cone keep the second phase stable. Letting `epsilon->0` yields a plausible full uniform output limit and kernel convergence uniformly away from `0,t_*`; the stopping-time details and joint path-space proof still need to be written.

**Topology warning:** A shrinking gate-death window does **not** imply `J_1` convergence of the kernel to one aggregate jump. On a positive-probability event, two distinct supporting Poisson atoms have nonnegligible squared weights and die at distinct finite-width times both tending to `t_*`. The intermediate staircase level stays separated from the pre- and post-switch levels, so no Skorokhod `J_1` time change can merge those jumps into one. Scalar `M_1` for the changing diagonal, together with uniform convergence of the other entries, or simply uniform convergence away from the switch, is the natural formulation. The output remains continuous and can converge uniformly. This corrects the tentative `J1` suggestion in my previous `c03.md` note.
