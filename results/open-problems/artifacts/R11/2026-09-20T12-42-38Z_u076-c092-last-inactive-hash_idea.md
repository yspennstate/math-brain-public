Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and I do not claim otherwise.**

# R11 / I0054 idea note — last-inactive harmonic-mark extractor, before code

Methods actually being used this run: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #11 DUALIZE; #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.**

This note freezes the mathematical route before any checker is written. The supported baseline is the immutable R11 report `runs/R11/2026-09-20T11-40-00Z_i0054-proposal-count-rotor-u075-c091-5e3a.md`, which moved the frozen I0054 metric `90 -> 91` using #10/#22/#28. The canonical claim `operations/claims/I0054.md` still says `PENDING_ADMISSION, not READY`. The old R11 planar-SAW route remains retired. The newest neighboring P13 work is on binary LCS, not Aldous--Janson Open Problem 18.

## Route

The preceding rotor U075 extracted an almost-uniform cyclic phase from the **number** of raw harmonic proposals between active compact-logit proposals. Its proof requires `d_N/H_{N-1}->0`. I will instead extract the phase from the **identity of the last inactive harmonic mark** before an active proposal. That raw mark has a very spread-out heavy-tail law and contains substantially more one-shot entropy.

Keep the compact-logit setup from U073:

- `L=log 4`, `I=[1/2,4/5)`;
- harmonic proposal rates `lambda_{N,s}=N/(2s(N-s))=(1/2)(1/s+1/(N-s))`;
- total rate `H_N^*=sum_s lambda_{N,s}=H_{N-1}`;
- active rate `W_N=sum_{s/N in I} lambda_{N,s}->log 2`;
- inactive rate `R_N=H_N^*-W_N~log N`;
- active raw-proposal probability `q_N=W_N/H_N^*=O(1/log N)`.

Conditional on an inactive mark, let

`pi_{N,s}=lambda_{N,s}/R_N`, `s/N notin I`.

For an integer alphabet size `d`, define the unavoidable oversized-atom excess

`E_N(d)=sum_s (pi_{N,s}-1/d)_+`.

### Proposed U076: one-mark harmonic extractor theorem

For any deterministic hash `h` from inactive marks to `Z/dZ`, if `Q=h(S)` for `S~pi_N`, then

`TV(L(Q),Unif_d) >= E_N(d)`.

Conversely, because `pi_{N,s} <= 1/(R_N min(s,N-s))`, a deterministic finite partition exists with

`TV(L(h_N(S)),Unif_d) <= E_N(d) + O(R_N^{-1/2})`

whenever the heavy atoms are isolated and the remaining atoms are greedily packed by cumulative mass. More explicitly, take `delta=1/(d sqrt(R_N))`; there are `O(d/sqrt(R_N))` atoms heavier than `delta`, assign each such atom its own bin, use equal residual target mass for the other bins, and greedily cut the `<=delta` tail. The target-vector deviation contributes at most `E_N(d)+O(R_N^{-1/2})`, and the greedy rounding contributes at most `d delta/2=O(R_N^{-1/2})`.

Also

`E_N(d) <= (2/R_N)(1+log_+(d/R_N))`,

so if `log d_N=o(R_N)` and `d_N->infinity`, then there is a deterministic `h_N` with output TV error `epsilon_N->0`.

The dual lower bound is close to sharp at the logarithmic scale: for `d_N=N^alpha`, `0<alpha<=1`, the two edge families `s=m` and `s=N-m`, `m<=d_N/(4R_N)`, are inactive and each have `pi >= 1/(2R_N m)`, giving

`liminf E_N(d_N) >= alpha`.

For `alpha>1`, support size alone forces TV to 1. Thus one **single** inactive harmonic mark supports deterministic near-uniform extraction for every `d_N=N^{o(1)}`, while no polynomial-size alphabet can be asymptotically uniform. This is the #4/#11 subproblem.

For the concrete model choose the exact integer sequence

`d_N = 2^{max(1,floor(sqrt(log_2 N)))}`,

so `d_N->infinity` and `log d_N=o(log N)`. To avoid irrelevant finite implementation choices, define `h_N` for all sufficiently large N by the explicit heavy-atom/greedy-tail construction above, and allow arbitrary deterministic hashes on finitely many small N; for the finite witness below fix `h_4(1)=1`. Equivalently one may define the lexicographically first TV-minimizing hash; the theorem proves that its error also tends to zero.

### Proposed C092: last-inactive-mark hash-dither hierarchy

Each current clade stores the previous raw harmonic mark `Z`. The root begins with `Z=1`.

At a proposal with current mark `s`:

1. if `s/N` is inactive, use the source Bernoulli bias `s/N`;
2. if `s/N` is active and stored `Z` is inactive, set `J=h_N(Z)` and use compact-logit bias
   `sigma(L { b_N alpha_{N,s} + J/d_N })`;
3. if `s/N` is active and stored `Z` is active, use fallback `J=0`;
4. after the proposal set `Z=s`; if a split occurs, both children inherit this updated mark, and their future proposal clocks are fresh.

Here `b_N` is **arbitrary**. For a concrete class retain the deliberately huge schedule used near C090: `b_N=1` through N=4 and `b_N=2^{2^{N-4}-1}` for N>=5.

Why this should have the complete path limit: between a clade birth/previous active mark and its next active mark, either no inactive raw proposal occurs (probability exactly `q_N`), or the **last** inactive mark before that active proposal is a fresh sample from `pi_N`, independent of the terminal active mark. On the good event the deterministic hash phase has law within `epsilon_N` of uniform. Hence each active proposal can be coupled to U073's fresh uniform dither with failure at most `q_N+epsilon_N`. On a fixed visible restriction `[k]`, there are at most k visible carrier blocks and their total active proposal intensity is at most `k W_N`, so on `[0,T]`

`TV(C092^[k], U073^[k]) <= k T W_N (q_N+epsilon_N) ->0`.

U073 already gives `TV(U073^[k], CTCS^[k]) <= C_{k,T}(1/d_N+1/N)`. Therefore C092 should converge in total variation on the **entire finite-restriction path**, hence in finite-state Skorokhod J1 and then in the same projective CTCS(infinity) topology used throughout R11.

Phase inheritance is important: an invisible hidden-only split updates the stored mark exactly once and gives the visible carrier child the same stored mark, so restriction consistency survives. If a visible child is born at a mark whose distribution is biased by the split, that inherited mark only matters when the next raw proposal is already active; this is included in the `q_N` bad-event allowance. After one inactive proposal, the last inactive mark has the unconditional inactive conditional law `pi_N`.

### #16 finite witness planned at N=4

Take `d_4=2`, `b_4=1`, root memory `Z=1`, `h_4(1)=1`. The embedded raw mark probabilities are `(4/11,3/11,4/11)` for marks `s=1,2,3`. Mark 1 is inactive. For incoming inactive memory the active biases are `2/3` at s=2 and `3/5` at s=3; for incoming active memory fallback gives `1/2` and `3/4`.

The two-state root absorption system should give

`P_C092(2|2)=563725059/1541504863 ≈ 0.3656978791`,

which differs from CTCS(4)'s `3/11`, from C091's `357573111/981185971`, and from C090's `3200871/8926643`. The checker will independently enumerate all 16 color masks for each bias and solve this two-state exact rational system. Only after this idea commit will checker code be written.

## Status intended if all proof/checks survive

If the extraction proof, restriction/coupling argument, and exact N=4 computation all survive checking, record `R11-I0054-U076 = PROVED_AUTHOR_SIDE`, `R11-I0054-C092 = PROVED_AUTHOR_SIDE`, and move the frozen metric `91 -> 92`. This would remain **PARTIAL** for the source because the present package still lacks the required P26 end-to-end PASS plus a second independent OTHER-track PASS, and current-literature nonresolution evidence is necessarily bounded.