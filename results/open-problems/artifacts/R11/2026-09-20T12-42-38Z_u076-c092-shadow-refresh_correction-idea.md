Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and I do not claim otherwise.**

# R11 / I0054 correction note — replace same-stream memory by an independent shadow harmonic refresh, before revised checker

This correction is written **before the revised checker**. It preserves rather than edits the earlier idea/checker attempt.

## Why the first same-stream memory route is not promoted

The first idea tried to use the last ordinary inactive split-proposal mark as the next active compact-logit phase. That has a conditioning problem: an ordinary inactive proposal can split a carrier, and the law of the inherited mark conditional on the visible child that survives is biased by the split outcome. Therefore the claim that the stored inactive mark is always an unconditional sample from the inactive harmonic law at the next active proposal is not justified. The finite calculation in the first checker remains a correct calculation for that finite two-state model, but it does **not** certify the asymptotic coupling claimed in the first idea note. It will not be used to support U076/C092.

## Corrected route: an independent shadow harmonic refresh stream

Retain the ordinary harmonic split proposal clocks

`lambda_{N,s}=N/(2s(N-s))`, `1<=s<=N-1`.

Let the compact-logit active set be `A_N={s: 1/2 <= s/N < 4/5}`. Write

`W_N=sum_{s in A_N} lambda_{N,s} -> log 2`,

`R_N=sum_{s notin A_N} lambda_{N,s}=H_{N-1}-W_N ~ log N`.

Ordinary proposals remain tree proposals:

- inactive ordinary mark `s`: use the source Bernoulli bias `s/N`;
- active ordinary mark `s`: use the compact-logit bias determined by the current phase `J`.

Add a **shadow refresh stream** that never splits the tree. For every inactive index `s`, each current clade has an independent shadow clock of rate `lambda_{N,s}`. When it rings, it only sets

`J <- h_N(s)`

and makes no coloring and no partition change. Children inherit the current `J`; all ordinary and shadow clocks then restart independently. The root may start at any deterministic phase, say `J=0`.

This removes the conditioning problem completely. Shadow marks are independent of all tree colors and split outcomes. Conditional on a shadow event, its mark law is exactly

`pi_{N,s}=lambda_{N,s}/R_N`, `s notin A_N`.

Between two successive **active ordinary** proposals on any visible-carrier lineage, the active ordinary hazard is `W_N` and the shadow-refresh hazard is `R_N`. Ordinary inactive proposals may occur, including invisible or visible splits, but they are independent of `J`; phase and the active/shadow competition are inherited through them. Consequently the probability that the next active ordinary proposal arrives before any shadow refresh is exactly

`q_N = W_N/(W_N+R_N)=W_N/H_{N-1}=O(1/log N)`.

On the complementary event, the last shadow mark before that active proposal is a fresh sample from `pi_N`, independent of the active mark and of the partition/color history after that refresh. If `h_N(pi_N)` is within `epsilon_N` in TV of uniform on `Z/d_N`, the phase used at each active proposal can therefore be coupled to U073's fresh uniform dither with failure probability at most `q_N+epsilon_N`.

On a fixed visible restriction `[k]`, at most `k` visible carriers are present and each has active ordinary proposal rate `W_N`. Thus on `[0,T]`

`TV(C092^[k], U073^[k]) <= k T W_N (q_N+epsilon_N)`.

Combining with U073's `O_{k,T}(1/d_N+1/N)` path-TV error proves the full finite-restriction path limit once `d_N->infinity` and `epsilon_N->0`.

## U076 survives unchanged: one-shadow-mark deterministic extraction

The extraction theorem concerns only the finite inactive mark law `pi_N`, so the correction does not alter it.

For `d>=2`, set

`E_N(d)=sum_s (pi_{N,s}-1/d)_+`.

For every deterministic hash `h`, `TV(h(pi_N),U_d)>=E_N(d)`. Conversely, isolate atoms above `delta=1/(d sqrt(R_N))`, assign them separate bins, and greedily pack the remaining `<=delta` atoms against equal residual target masses. Since `pi_{N,s}<=1/(R_N min(s,N-s))`, the number of heavy atoms is `O(d/sqrt(R_N))`, and

`TV(h_N(pi_N),U_d) <= E_N(d)+O(R_N^{-1/2}+d^{-1})`.

Moreover

`E_N(d) <= (2/R_N)(1+log(1+d/R_N))`.

Hence `log d_N=o(R_N)` and `d_N->infinity` imply `epsilon_N->0`. The dual lower bound from oversized atoms still shows that for `d_N=floor(N^alpha)`, `0<alpha<=1`, every deterministic one-mark hash has `liminf TV >= alpha`, while `alpha>1` is ruled out by support size. Thus the one-mark extraction threshold is genuinely nontrivial.

For C092 use the exact integer sequence

`d_N=2^{max(1,r_N)}`, where `r_N=max{r>=0: 2^{r^2}<=N}`,

so `log d_N=Theta(sqrt(log N))=o(R_N)`. Retain arbitrary branch counts `b_N`; concretely use `b_N=1` for `N<=4` and `b_N=2^{2^{N-4}-1}` for `N>=5`.

## Revised #16 finite witness at N=4

At `N=4`, ordinary harmonic rates are `(2/3,1/2,2/3)`. The only inactive shadow mark is `s=1`, so set `d_4=2`, `h_4(1)=1`, and root phase `J=0`. The shadow refresh rate is `2/3`.

Before the first shadow refresh (phase 0), ordinary biases are `(1/4,1/2,3/4)`. After refresh (phase 1), active biases become `(2/3,3/5)` while the inactive ordinary bias stays `1/4`. Direct 16-mask enumeration gives ordinary split rates

phase 0: balanced `15/32`, unbalanced `7/8`;

phase 1: balanced `560707/1080000`, unbalanced `722693/810000`.

Let `B_1` be the eventual balanced-root probability after refresh and `B_0` the root-start value. Null ordinary proposals do nothing to the state, so

`B_1 = a_1/(a_1+u_1)=1682121/4572893`,

`B_0 = (a_0+(2/3)B_1)/(a_0+u_0+2/3)`.

The revised checker should obtain

`B_0=313435929/882568349 ≈0.3551406861`.

This differs exactly from CTCS(4) `3/11`, from C091 `357573111/981185971`, from C090 `3200871/8926643`, and from C084 `1682121/4572893`. This scale-free root-topology statistic is invariant under deterministic leaf relabeling and common positive time rescaling.

Only this corrected shadow-refresh model and its revised checker will support the final U076/C092 claims.