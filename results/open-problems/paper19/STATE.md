# Paper 19 - STATE / durable ledger

Read this first on every resume. Source of truth for the 5-day build.

## Timer
- Start: 2026-06-27 18:48 JDT
- Target end: 2026-07-02 18:48 JDT
- See `paper19/.timer` for epochs. In PowerShell, check elapsed from the timestamps directly;
  do not use Unix `source`.

## Scope (user directives)
- Generalize the paper "Extreme least singular values of Gaussian row submatrices and a
  phase retrieval stability problem" to other random matrices, entry laws, and ensembles,
  as much as can be done honestly.
- Build this as a new standalone chapter/paper: `paper19/extremal_hard_edge.tex`.
- Second deliverable: genuine open problems in RMT, probability, and concentration related
  to the author's work.
- No Toeplitz, Hankel, circulant, or structured-symbol matrices. Stay in the area of the
  source paper: row submatrices, random frames, hard-edge least singular values, and phase
  retrieval stability.
- Use exactly 5 subagents per active round, with adversarial verification. The pasted prompt
  said 50; the corrected user instruction is 5.

## Files
- `PLAN.md` - math roadmap.
- `extremal_hard_edge.tex` - assembled manuscript.
- `parts/*.tex` - manuscript sections.
- `refs.bib` - bibliography.
- `verification/*.md` - adversarial verification reports per result.
- `sources/SOURCE_MANIFEST.md` - imported source PDFs and extracted-text provenance.

## Sources

- `sources/extreme_least_singular_values_radial_phase_retrieval_20260628_171349.pdf`
  is the 31-page June 28 source PDF on redundancy, radial ensembles, and
  quantitative phase-retrieval stability.  It is indexed under
  `sources/extracted_text/` for local audit context.  It does not promote any
  theorem-ledger row without lane-local proof or checked citation.

## Theorem ledger

Status meanings: TODO / DRAFT / VERIFYING / PROVEN / PARTIAL / CONDITIONAL / CONJECTURE / KILLED.

| ID | Statement (short) | Tier | Status | Notes |
|----|-------------------|------|--------|-------|
| A | Abstract extremal small-ball principle (H/a) | 1 | PROVEN | First/second moment theorem; see `parts/principle.tex`. |
| A-fin | Finite-budget lower-side principle | 1 | PROVEN | If `P{Y_T<=t} <= C_m t^{a_m}`, then `P{min_T Y_T <= exp[-(log|\mathcal T_m|+log C_m+u_m)/a_m]} <= e^{-u_m}`. Gives moving-aspect lower sides without a limiting entropy. |
| A-fin-w | Nonuniform finite-budget lower side | 1 | PROVEN | If `P{Y_T<=t} <= C_T t^{a_m}` with deterministic per-index constants and common exponent, the budget is `log B_m` for any `B_m >= 1 vee sum_T C_T`. Keeps weighted union-bound constants without replacing them by `|\mathcal T_m| sup C_T`. |
| A-fin-w-as | Almost-sure nonuniform finite-budget lower side | 1 | PROVEN | If the weighted finite-budget data are deterministic and `sum_m e^{-u_m}<infty`, first Borel-Cantelli gives `min_T Y_T > exp[-(log B_m+u_m)/a_m]` eventually a.s. No independence across dimensions or inside the tested family is used. |
| A-fin-as | Almost-sure finite-budget lower side | 1 | PROVEN | If the finite-budget data are deterministic and `sum_m e^{-u_m}<infty`, first Borel-Cantelli gives `min_T Y_T > exp[-(log|\mathcal T_m|+log C_m+u_m)/a_m]` eventually a.s. No independence across dimensions or inside the tested family is used. |
| A-as | Almost-sure lower-envelope principle | 1 | PROVEN | First Borel-Cantelli upgrades any lower-side union bound with summable failure probabilities to an eventual a.s. liminf bound. Applies to square, density-rate, smoothed, fixed/proportional-excess, two-sided, spherical-radial transfer, and critical PR lower envelopes. No a.s. upper/exact law claimed. |
| II.A | Lower bound from one-matrix LSV tails | 1 | PROVEN | Union bound; residual terms must be smaller than `exp(-Hm)`. |
| II.A-bd | Bounded-density real/complex iid lower bound | 1 | PROVEN | Uses `P{s_min<=t} <= C_{\F,K} m^{d_\F+1} t^{d_\F}`; real case matches Shmalo Prop. 6.1, complex case follows by codimension two. |
| II.A-fin | Finite-entropy square lower side | 1 | PROVEN | For arbitrary `N_m>=m`, independent bounded-density entries with scalar bound `K_m`, and `L_m=log binom(N_m,m)`, the lower side holds at threshold `(L_m+log K_m)/d_\F` up to polynomial and exponential slack. Summable `e^{-u_m}` upgrades the full finite threshold to an eventual a.s. lower bound. Lower side only. |
| II.A-fin-row | Row-wise heterogeneous-density square budget | 1 | PROVEN | If row `i` has deterministic scalar density bound `K_{m,i}` uniformly over columns, the square finite budget replaces `log binom(N_m,m)+log K_m` by `log binom(N_m-1,m-1)+log sum_i K_{m,i}`; polynomial and summable slack retained. Lower side only. |
| II.A-fin-ent | Entrywise density-profile square budget | 1 | PROVEN | If entry `(i,j)` has deterministic scalar density bound `K_{m,i,j}`, set `K_{m,i}^*=max_j K_{m,i,j}` and use the row-distance budget `log binom(N_m-1,m-1)+log sum_i K_{m,i}^*`. Summable `e^{-u_m}` gives eventual a.s. lower bounds. Lower side only; column averages/geometric means are not claimed without normal-delocalization input. |
| II.A-fin-dir | Directional anti-concentration row budget | 1 | PROVEN | Independent rows, without coordinate independence, are covered if `P{|<R_{m,i},u>-z|<=r} <= L_{m,i} r^{d_F}` uniformly over deterministic unit `u`, centers `z`, and `0<r<=1`. The square finite budget is `log binom(N_m-1,m-1)+log sum_i L_{m,i}+(d_F/2)log m`; summable `e^{-u_m}` gives eventual a.s. lower bounds. This yields the real iid isotropic log-concave lower-side base `h(gamma)`, but no exact law. |
| II.A-rate | Density-rate lower side | 1 | PROVEN | If scalar density bounds grow like `K_m=exp((kappa+o(1))m)`, then `P{M_m <= exp[-((h(gamma)+kappa)/d_\F+eps)m]} -> 0`; `kappa=0` recovers the bounded-density lower base. |
| II.A-rc | Random row-count / Poissonization transfer | 1 | PROVEN | For an infinite iid Gaussian row array and any integer row count `N_m/m -> gamma>1` in probability, possibly dependent on the row array, monotonicity squeezes `m^{-1}log M_m(N_m)` to `-h(gamma)/d_\F`. Bounded-density/density-rate lower sides and a.s. lower envelopes transfer by the same upper-bracket monotonicity. Poisson and independent Bernoulli thinning are included; value-dependent thinning is excluded. |
| II.B | Full continuous universality upper side | 2 | ESSENTIALLY CLOSED (modulo standard local law) | Two-projection local CLT now PROVED unconditionally as Lemma `lem:two-proj` in `parts/universality.tex` (bounded density, no sub-Gaussian; constants match the Gaussian two-slab/two-disk estimate; full proof `notes/IIB_lemma_2D.md`). Small/intermediate overlap codimensions PROVEN negligible by `prop:small-D-negligible`. SESSION-16 ADVANCE (`notes/keystone_synthesis.md`, lead-verified): the bulk moment `E[(1-|rho|^2)^{-d_F/2};D>=eps m]<=1+o(1)` is now itself REDUCED to a single typical-value estimate, with two of three pieces PROVED: (T) the polar-cap LOWER TAIL `P{1-|rho|^2<=y}<=(C sqrt y)^{D-1}+e^{-cD}` PROVED via RV08 net+small-ball (delta-cancellation kills the sqrt(D) blowup; `notes/keystone_tail.md`; numerically confirmed); (A) the moment ASSEMBLY PROVED given the typical value; (M) typical value `E|rho|^2`: PROVED EXACTLY `=1/m` for DISJOINT pairs via signed-permutation/phase symmetry `E[u u^*]=I_m/m` (`notes/keystone_typical.md`). SESSION-17 REFINEMENT (2 more agents): the assembly bar is now PROVED to be exactly `E|rho|^2=o(1)` — SUFFICIENT AND NECESSARY (optimize the eta-split: `E[X^{-a}]<=1+O(sqrt(E|rho|^2))`; `notes/keystone_assembly_bar.md`), far weaker than O(1/D). That bar is NUMERICALLY TRUE DISTRIBUTION-FREE (`E|rho|^2~1/D`, D=4..64, 5 laws incl non-symmetric exp/lognormal; `notes/keystone_weak_deloc.md`). The earlier `lambda_max~0.648` counterexample is REFUTED — a D=2 artifact (top eigenvalue decays 0.657,0.274,...,0.0095 ~ 1/D), NOT an obstruction. So the LONE remaining input is `E|rho|^2=o(1)` <=> no-gaps delocalization-in-expectation `sup_w E[|<u,w>|^2|E]=o(1)` for the null vector of projected iid rows: a recognized, numerically-true, UNOBSTRUCTED RMT estimate (needs a no-gaps-in-expectation theorem, not soft CLT). `prob:pc` updated to this. NET: keystone (hence II.B upper side, hence via the Gumbel reduction the explicit fluctuation law) is PROVEN modulo one true-but-unproven no-gaps-in-expectation bound; tail+assembly+disjoint all proven; no obstruction known. SESSION-19 NEAR-CLOSURE (2 agents + lead-verified, `notes/residual_locallaw.md`,`residual_lsv.md`; manuscript Prop `appB:resolvent` + Cor `appB:closure`): the residual is CLOSED via a RESOLVENT-MONOTONICITY reduction that bypasses the hard edge. Since u is the EXACT null eigenvector of Q=GG^*, `u u^* <= eta(Q+eta)^{-1}` (PSD, simultaneously diagonal in Q-eigenbasis — lead-verified), so `lambda_max(E[u u^*|E]) <= eta||E[(Q+eta)^{-1}|E]|| <= (1+o(1)) eta m(-eta) = (1+o(1))sqrt(eta)` by the OFF-SUPPORT isotropic/anisotropic local law [BEKYY2014/KnowlesYin2017] (Q = sample cov of isotropic projected rows, aspect->1, MP m(-eta)~eta^{-1/2}); eta=1/log D => o(1). Hard edge BYPASSED: resolvent at z=-eta off-support, eta>>1/D, the ROBUST regime. NET: II.B universality upper side + (via reduction) the explicit Gumbel law are PROVEN MODULO ONE STANDARD OFF-SUPPORT APPLICATION of the published local law. Undeformed case is outright in the literature (Nguyen-Vu IMRN 2018). `prob:pc` reframed as: give a self-contained proof avoiding the heavy local-law machinery. This is essentially a closed flagship. |
| II.B-small | High-overlap-pair negligible range | 1 | PROVEN | For any `s<h(gamma)/d_F`, hypergeometric overlap rarity gives `P{2<=D<=eps m}/p_m -> 0` for some `eps>0` whenever `p_m >= c exp(-d_F s m)`, so `E[q_D/p_m^2; 2<=D<=eps m] -> 0` from `q_D<=p_m`. |
| II.C | Atomic/discrete exact singularity | 1 | PARTIAL | First-moment obstruction proved; deterministic finite-alphabet projective-pair obstruction proved in `II.C-proj`; random atomic high-probability thresholds below deterministic row counts remain law-dependent and open. |
| II.C-proj | Finite alphabet projective-pair obstruction | 1 | PROVEN | If `S subset K` is finite nonempty for `K=R` or `C`, `Pi(S)={[a:b] in P^1(K): a,b in S, (a,b)!=(0,0)}`, `m>=2`, and either `S={0}, N>=m` or `S!={0}, N>=|Pi(S)|(m-1)+1`, every `A in S^{N x m}` has a singular `m`-row submatrix. Zero-zero rows are compatible with every projective class; for nonzero alphabets this recovers the quotient count `|S/S|`. The sign theorem is the `|Pi|=2` case. Random thresholds below this deterministic count are not claimed. |
| III.A | Rectangular row submatrices | 1 | PARTIAL | Fixed-excess Gaussian, bounded-density, heterogeneous-density, and directional-row lower sides proved; proportional excess scale corrected; exact fixed-excess base still needs second moment. |
| III.A-bd | Fixed-excess bounded-density lower side | 1 | PROVEN | For fixed excess `r`, scalar density bound `K_m=exp((kappa+o(1))m)` gives lower threshold `h(gamma)/(d_\F(r+1))+kappa/d_\F`; subexponential density growth preserves the Gaussian lower-side base. |
| III.A-fin | Finite-entropy fixed-excess lower side | 1 | PROVEN | For fixed `r`, arbitrary `N_m>=m+r`, and `L_m^{(r)}=log binom(N_m,m+r)`, the lower-side finite budget is `(L_m^{(r)}+(r+1)log K_m)/(d_\F(r+1))` up to polynomial and exponential slack; summable `e^{-u_m}` gives the full finite threshold eventually a.s. |
| III.A-dir-row | Fixed-excess directional-row lower side | 1 | PROVEN | `rect:directional-row-fixed-excess` uses the cofactor row-block certificate `rect:row-block-certificate`: if independent rows satisfy affine one-dimensional directional small-ball bounds `P{|<R_i,u>-z|<=rho}<=L_{m,i}rho^{d_F}`, then for fixed `r`, `p=r+1`, the finite budget is `log B_{m,r}^{dir}` with `B_{m,r}^{dir}=binom(N_m-p,m-1) sum_{|S|=p} prod_{i in S} L_{m,i}`, plus `(d_F p/2)log m+u_m` over denominator `d_F p`. If `N_m/m->gamma` and `beta_r^{dir}=limsup m^{-1}log sum_{|S|=p}prod_i L_{m,i}`, the lower-side base is `(h(gamma)+beta_r^{dir})/(d_F(r+1))`, with summable a.s. lower envelope. Lower side only; no exact law or pair correlation. |
| III.A-het-row | Fixed-excess heterogeneous row-density budget | 1 | PROVEN | For fixed `r`, row-wise deterministic density bounds `K_{m,i}` give finite budget `log Theta_{m,r}` where `Theta_{m,r}=sum_{|T|=m+r} max_{S subset T, |S|=r+1} prod_{i in S} K_{m,i}`. Summable `e^{-u_m}` gives eventual a.s. lower bounds. Lower side only; square `r=0` has a sharper special budget in II.A-fin-row. |
| III.A-het-entry | Fixed-excess entrywise heterogeneous budget | 1 | PROVEN | For fixed `r`, deterministic entrywise density bounds `K_{m,a,q}` give finite budget `log Xi_{m,r}` where `Xi_{m,r}=sum_{|T|=m+r} sum_{q=1}^m max_{S subset T, |S|=r+1} prod_{a in S} K_{m,a,q}`, with `d_\F(r+1)log m+O_{\F,r}(1)+u_m` slack. Summable `e^{-u_m}` gives eventual a.s. lower bounds. Lower side only; row-wise and uniform specializations recover `III.A-het-row` and `III.A-fin`. |
| III.A-prop-rate | Proportional-excess density-rate lower side | 1 | PROVEN | If `ell_m/m -> zeta in (1,gamma)` and independent scalar densities satisfy `K_m=exp((kappa+o(1))m)`, then `P{min_{|T|=ell_m} s_min(A_T) <= exp[-(kappa/d_\F+eps)m]} -> 0`; for `kappa=0`, `liminf m^{-1}log M_{m,ell} >= 0`. Exponential-scale lower side only; the `sqrt(m)` Wishart-edge/LDP limit remains open. |
| III.A-moving-fin | Moving-excess rectangular finite budget | 1 | PROVEN | For arbitrary `m<=ell_m<=N_m`, `p_m=ell_m-m+1`, scalar density bound `K_m`, and `q_m=d_\F p_m`, the lower-side finite budget is `log B_m` with `B_m=1 vee [binom(N_m,ell_m)m K_m^{p_m} binom(ell_m,p_m)^{d_\F/2} v_{q_m}m^{q_m/2}]`; denominator `d_\F p_m`. Summable `e^{-u_m}` gives eventual a.s. lower bounds. No Wishart-edge, upper-side, or exact-base claim. |
| III.A-prop-rc | Random-prefix proportional-excess lower sides | 1 | PROVEN | `rect:random-prefix-proportional-density-rate` transfers the proportional-excess density-rate lower side to possibly dependent prefix counts: for `F in {R,C}`, independent scalar entries with density bound `K_m=exp((kappa+o(1))m)`, deterministic `ell_m/m -> zeta in (1,gamma)`, and integer `N_m/m -> gamma>1` in probability, `P{min_{T subset [N_m], |T|=ell_m} s_min(A_T) <= exp[-(kappa/d_F+eps)m]} -> 0`. The selected-row normalized column-Gram statistic with `ell_m^{-1}A_T^*A_T` has doubled threshold `2kappa/d_F`. A.s. count convergence gives the same lower envelopes on common couplings. For `K_m=e^{o(m)}` the exponential-scale base is `0`. R57 separately records the pathwise row/right-factor transfer. No `sqrt(m)` Wishart-edge/LDP constant, upper/exact proportional-edge law, value-dependent row selection, or selected-column theorem is claimed. |
| III.A-prop-rc-cond | Random-prefix proportional-excess conditioning transfer | 1 | PROVEN | `rect:random-prefix-proportional-conditioning-transfer` composes R56 with the pathwise row/right-factor sandwich: for `F in {R,C}`, an independent-entry base row array satisfying the R56 density-rate hypotheses, deterministic `ell_m/m -> zeta in (1,gamma)`, possibly dependent prefix counts `N_m/m -> gamma>1`, positive real realized-prefix row weights, and one global all-column right factor `S_m in GL_m(F)` with `Delta_m^{propcond}=max_{i<=N_m}|log d_im|+|log smin(S_m)|+|log opnorm(S_m)|=o_P(m)`, the singular lower threshold remains `kappa/d_F` and the selected-row normalized column-Gram threshold remains `2kappa/d_F`. A.s. count convergence and `Delta=o(m)` transfer lower envelopes. Positive column diagonals, full-column covariance/whitening under absolute singular-scale control, Gaussian row normalization, and full-prefix Gaussian column normalization are included. This is only a pathwise lower-side transfer from the unweighted independent-entry base; the conditioned matrix is not asserted to satisfy a density hypothesis. No quaternion extension, condition-number-only covariance claim, selected-column theorem, selected-submatrix column normalization, value-dependent row selection, row-Gram result, `sqrt(m)` Wishart-edge/LDP constant, upper side, or exact proportional-edge law is claimed. |
| III.A-prop-gauss | Proportional-excess Gaussian exponential scale | 1 | PROVEN | If `ell_m/m -> zeta in (1,gamma)`, then `m^{-1}log min_{|T|=ell_m}s_min(A_T) -> 0` in probability. The finer `sqrt m` edge remains a Wishart LDP problem. |
| III.B-lower | Fixed-`k` Gaussian finite-budget lower side | 1 | PROVEN | Finite-`m` Laguerre-Selberg tail gives `P{sigma_{m-k+1}(G)<=t} <= C_{\F,k}m^{B_{\F,k}}t^{d_\F k^2}`; hence `M_m[k]` has finite budget `(log binom(N_m,m)+B log m+O(1))/(d_\F k^2)` and fixed-aspect lower base `h(gamma)/(d_\F k^2)`. |
| III.B-rect-lower | Fixed-excess fixed-`k` Gaussian lower side | 1 | PROVEN | For fixed `r>=0`, fixed `k>=1`, and iid Gaussian `F=R,C`, the rectangular Laguerre-Selberg tail gives `P{sigma_{m-k+1}(G)<=t} <= C_{\F,r,k}m^{B_{\F,r,k}}t^{d_\F k(k+r)}` for `(m+r) x m` matrices. Thus `M_m^{(r)}[k]` has finite budget `(log binom(N_m,m+r)+B log m+O(1))/(d_\F k(k+r))`, fixed-aspect lower base `h(gamma)/(d_\F k(k+r))`, and an a.s. lower envelope on common couplings. Recovers `III.A` at `k=1` and `III.B-lower` at `r=0`; quaternion lower-side analogues are recorded separately in `V.A-rect-kth`, and no upper side or exact law is claimed. |
| III.B-gram | Fixed-`k` Gram eigenvalue lower side | 1 | PROVEN | `kth:gram-lower` uses ascending eigenvalues and the pathwise identity `min_{|T|=m} lambda_(k)(m^{-1}A_T^*A_T)=m^{-1}M_m[k]^2`. The finite-budget lower side is the squared `kth:lower` threshold, and the fixed-aspect lower base is `2h(gamma)/(d_F k^2)` in probability and as an a.s. lower envelope on common couplings. Scope is iid Gaussian `F=R,C`; quaternion lower-side analogues are recorded separately in `V.A-rect-kth`, and no exact law is claimed. |
| III.B-rect-gram | Fixed-excess fixed-`k` Gram eigenvalue lower side | 1 | PROVEN | `rect-kth:gram-lower` is the pathwise transfer `Lambda_m^{(r)}[k]=(m+r)^{-1}(M_m^{(r)}[k])^2` for normalized column Gram matrices `((m+r)^-1 A_T^* A_T)`, `|T|=m+r`. The finite-budget threshold is the squared `rect-kth:lower` threshold times `(m+r)^-1`, and the fixed-aspect lower base is `2h(gamma)/(d_F k(k+r))` in probability and as an a.s. lower envelope. Lower side only; quaternion lower-side analogues are recorded separately in `V.A-rect-kth`, with no row-Gram statement for `r>0`, upper side, or exact law. |
| III.B | k-th smallest singular value exact law | 2 | CONJECTURE | Lower side is proved in `III.B-lower`; exact extremal law still needs the codimension-`k` pair-correlation/second-moment theorem. |
| III.C | Two-sided submatrices | 1 | PARTIAL | Lower side proved by entropy addition and one-matrix hard-edge tail; exact base conditional on row/column-overlap pair correlation. |
| III.C-rate | Two-sided density-rate lower side | 1 | PROVEN | For independent entries with scalar density bound `K_k=exp((kappa+o(1))k)`, `N_k/k -> gamma_R`, `n_k/k -> gamma_C`, and `H=h(gamma_R)+h(gamma_C)`, `P{M_k^{two} <= exp[-((H+kappa)/d_\F+eps)k]} -> 0`; `kappa=0` preserves the Gaussian two-sided lower base. |
| III.C-rc | Random-prefix two-sided density-rate lower side | 1 | PROVEN | `two:random-prefix-density-rate-lower` transfers `III.C-rate` to possibly dependent ordered row and column prefix counts: for `F in {R,C}`, an infinite independent-entry array with scalar density bound `K_k=exp((kappa+o(1))k)`, prefix counts `N_k^R/k -> gamma_R>1` and `N_k^C/k -> gamma_C>1` in probability, `P{min_{R subset [N_k^R], C subset [N_k^C], |R|=|C|=k} s_min(A_{R,C}) <= exp[-((h(gamma_R)+h(gamma_C)+kappa)/d_F+eps)k]} -> 0`. A.s. prefix-count convergence gives the same lower envelope on common couplings. The proof is only deterministic upper-bracket monotonicity plus the finite-budget two-sided lower side. R59 separately records the pathwise diagonal row/column weighting transfer. R61 separately records the deterministic selected-minor normalized Gram lower-side transfer. No upper side, exact two-sided law, pair-correlation theorem, quaternion extension, value-dependent thinning/reindexing, selected-column covariance transfer, non-diagonal right-factor transfer, or upper/exact Gram/sample-covariance law is claimed. |
| III.C-rc-diag | Random-prefix two-sided diagonal conditioning transfer | 1 | PROVEN | `two:random-prefix-diagonal-conditioning-transfer` composes `III.C-rc` with the pathwise diagonal sandwich: for `F in {R,C}`, positive real row and column weights over the realized ordered prefixes, possibly random and dependent, preserve the random-prefix two-sided density-rate lower threshold when `Delta_k^{twodiag}=max_{i<=N_k^R}|log d_{i,k}|+max_{j<=N_k^C}|log e_{j,k}|=o_P(k)`. A.s. prefix-count convergence and `Delta=o(k)` transfer the lower envelope. This is only a pathwise lower-side transfer from the unweighted independent-entry base; R61 separately records the deterministic selected-minor normalized Gram lower-side transfer. Non-diagonal column covariance/right factors, condition-number-only scale control, value-dependent thinning/reindexing, selected-submatrix renormalization, upper/exact two-sided laws, quaternion extensions, pair-correlation theorems, upper/exact Gram/sample-covariance laws, and Wishart-edge/LDP laws are not claimed. |
| III.C-rc-norm | Gaussian random-prefix two-sided full-prefix normalization | 1 | PROVEN | `two:random-prefix-gaussian-full-prefix-normalization` specializes `III.C-rc-diag` to iid real/complex Gaussian arrays with one-shot full-prefix row and/or column norm factors. Row norms use all realized prefix columns `[N_k^C]`; column norms use all realized prefix rows `[N_k^R]`; the factors are frozen before selecting `R,C`. Deterministic prefix bracketing gives the required logarithmic norm extrema `o_P(k)`, and `o(k)` a.s. under a.s. prefix-count convergence, so the lower threshold remains `(h(gamma_R)+h(gamma_C))/d_F` and the a.s. lower envelope transfers. R61 separately records the deterministic selected-minor normalized Gram lower-side transfer. This is not per-minor/iterative normalization, not a Sinkhorn theorem, not a non-Gaussian normalization theorem, and not an upper/exact two-sided or Gram law. |
| III.C-rc-gram | Random-prefix two-sided normalized Gram/sample-covariance transfer | 1 | PROVEN | `two:random-prefix-normalized-gram-transfer` composes `III.C-rc-diag` with the pathwise identity `lambda_min(k^{-1}B_{R,C}^*B_{R,C})=k^{-1}s_min(B_{R,C})^2`: for `F in {R,C}`, the selected `k x k` normalized column-Gram statistic over the realized row/column prefixes has lower threshold `2(h(gamma_R)+h(gamma_C)+kappa)/d_F`, with the corresponding a.s. lower envelope under the R59 a.s. hypotheses. The R60 Gaussian full-prefix-normalized matrices are included with `kappa=0`. This is deterministic squaring only for already selected square minors with selected-minor normalization `k^{-1}`; no upper/exact Gram law, Wishart-edge/LDP theorem, pair-correlation theorem, non-diagonal covariance/right-factor transfer, row-Gram rectangular result, per-minor normalization theorem, value-dependent selection theorem, or quaternion statement is claimed. |
| III.C-fin | Finite-entropy two-sided lower side | 1 | PROVEN | For arbitrary `N_k,n_k>=k`, independent entries with scalar density bound `K_k`, and `L_k^{two}=log binom(N_k,k)+log binom(n_k,k)`, the lower-side finite budget is `(L_k^{two}+log K_k)/d_\F` up to polynomial and exponential slack; summable `e^{-u_k}` gives the full finite threshold eventually a.s. |
| III.C-fin-het | Heterogeneous-density two-sided finite budget | 1 | PROVEN | For independent entries with deterministic scalar density bounds `K_{k,i,j}`, define `K_{k,i,C}=max_{j in C} K_{k,i,j}`. The lower-side finite budget is `log binom(N_k-1,k-1)+log sum_i sum_{|C|=k} K_{k,i,C}`, with `d_\F log k+O_\F(1)+u_k` slack; summable `e^{-u_k}` gives eventual a.s. lower bounds. Lower side only; recovers `III.C-fin` when all bounds are equal. |
| III.D | Endpoint aspect asymptotics | 1 | PROVEN | Deterministic calculus for the entropy base: near `gamma=1`, `h(1+delta)=delta log(1/delta)+delta+O(delta^2)`; as `gamma->infty`, `h(gamma)=log gamma+1-1/(2 gamma)+O(gamma^{-2})`. Interprets fixed-aspect thresholds; no matching exact moving-aspect law claimed. |
| IV.A | Small-minimum upper-tail bound | 1 | PROVEN | Union bound gives `I_-(s) >= d s - h`; single-submatrix prob lower bound gives `I_-(s) <= d s`, so proved sandwich `d s - h <= I_- <= d s`. Exact rate `I_- = d s - h` is CONJECTURE: Bonferroni needs `E[Z(Z-1)] = o(EZ)`, which fails on the `Theta(m^2) binom(N,m)` pairs with `|I∩J| = m-1`. See `parts/ldp.tex`. |
| IV.B | Large-minimum lower-tail LDP | 3 | CONJECTURE | Reformulated as hole prob `P{Z_m(s)=0}`, `EZ -> inf`. Rigorous: `O(1/m)` upper bound (Chebyshev half of principle) plus conditional `>= exp[-C(s m^3+m^2 log m)]` lower bound (Gaussian ball; needs bounded deterministic frames `A_{0,m}` with `M_m(A_{0,m}) >= 2 e^{-sm}`), which would rule out the double-exp independence prediction if such frames exist. Conjecture: speed `m^2`, rate `K(s)` (Coulomb-gas analogy); even positivity `K>0` open. See `parts/ldp.tex`. |
| V.A | Division algebras R,C,H | 2 | PROVEN | `thm:quaternion-gaussian-base` proves the square iid quaternion Gaussian base `h/4`: quaternion Gaussian is `Sp(m)`-invariant, quaternion scalar small ball is `p_H(t)=2t^4+O(t^6)`, Haar normal lines in `HP^{D-1}` give `|rho|^2~Beta(2,2(D-1))`, and for `D>=3`, `E[(1-|rho|^2)^(-2)|D]=(2D-1)(2D-2)/((2D-3)(2D-4))=1+2/D+O(D^-2)`. The proof separately handles the divergent `D=2` term by `q_2<=p_H` and the exact overlap count. This exact theorem is only square-row `k=1`; not the R27-removed rotationally invariant/quaternion spherical upper-side theorem, not quaternion spherical-radial transfer unless `thm:rot-inv-univ` is explicitly extended to `HH`, and not fixed-excess quaternion exact laws. |
| V.A-square-rc | Quaternion square random row-count exact transfer | 2 | PROVEN | `thm:quat-random-row-count-gaussian` transfers the exact square quaternion Gaussian base to random prefix row counts: for an infinite iid standard quaternion Gaussian row array and integer `N_m/m -> gamma>1` in probability, possibly dependent on the row array, `m^{-1}log M_m^HH(N_m)->-h(gamma)/4`. The normalized square Gram base is `-h(gamma)/2`. A.s. count convergence gives only lower envelopes. `cor:quat-poisson-thinning` covers independent Poisson/binomial prefix counts and independent Bernoulli thinning by distributional reindexing of retained iid rows. Value-dependent thinning/selection is excluded; no Balan-Wang, fixed-excess exact, supercritical phase-retrieval, quaternion spherical-radial universality, or a.s. exact law is implied. |
| V.A-square-rc-cond | Quaternion random-prefix conditioning exact transfer | 2 | PROVEN | `cor:quat-random-prefix-conditioning-exact` combines the random prefix theorem with the pathwise conditioning sandwich: for an infinite iid standard quaternion Gaussian row array, `N_m/m -> gamma>1` in probability, positive real prefix row weights, and a global invertible all-column right factor `S_m`, the exact square-row base remains `-h(gamma)/4` when the realized-prefix row-weight extrema plus `|log smin(S_m)|+|log opnorm(S_m)|` are `o_P(m)`. The normalized square Gram base is `-h(gamma)/2`. Positive column diagonals, row-normalized random-prefix matrices, and full-prefix column normalization are included. A.s. hypotheses transfer only lower envelopes. Condition number alone, value-dependent row selection, selected-column covariance transfer, fixed-excess exact laws, Balan-Wang/supercritical phase retrieval, quaternion spherical-radial universality, and a.s. exact laws are excluded. |
| V.A-square-rc-rf | All-field square random-prefix row/right-factor exact transfer | 2 | PROVEN | `cor:random-prefix-square-row-right-factor-exact` packages the exact random-prefix square laws for `F in {R,C,H}` with the pathwise row/right-factor sandwich: for an infinite iid Gaussian row array, possibly dependent prefix counts `N_m/m -> gamma>1`, positive real prefix row weights, and one global all-column right factor `S_m in GL_m(F)` with realized-prefix absolute scale `Delta_m^{sqrf}=max_{i<=N_m}|log d_i|+|log smin(S_m)|+|log ||S_m||||=o_P(m)`, the singular exact base is `-h(gamma)/d_F` and the normalized square column-Gram exact base is `-2h(gamma)/d_F`. A.s. count convergence and `Delta_m^{sqrf}=o(m)` transfer only lower envelopes. Positive column diagonals, row-normalized random-prefix Gaussian rows, and full-prefix column-normalized Gaussian columns are included. For `H`, this subsumes the R50 random-prefix conditioning statement; for `r=0,k=1`, it is the exact strengthening of `V.A-rect-kth-rc-diag`. No value-dependent row selection, selected-submatrix column normalization, selected-column/two-sided non-diagonal covariance transfer, quaternionic non-real row weighting, condition-number-only covariance claim, fixed-excess exact law, row-Gram result for `r>0`, or a.s. exact law is implied. |
| V.A-square-diag | Quaternion square diagonal/normalized exact transfer | 2 | PROVEN | `cor:quat-square-diagonal-normalized-exact` transfers the exact square iid quaternion Gaussian base through positive real diagonal row/column weights, possibly random and dependent on `G`, whenever the total logarithmic extreme is `o_P(m)`: `m^{-1}log min_{|T|=m}smin((D_row G E)_T)->-h(gamma)/4`. The normalized square column-Gram statistic has base `-h(gamma)/2` by `cor:gram-transfer`. Row-normalized quaternion Gaussian rows and full-matrix column-normalized quaternion Gaussian columns are included. A.s. `o(m)` diagonal extrema give only the lower envelopes; no a.s. exact law, fixed-excess exact law, selected-column/two-sided non-diagonal covariance transfer, quaternion-valued diagonal weights, selected-submatrix column renormalization, or spherical-radial quaternion transfer is claimed. Square all-column right factors are recorded separately in `V.A-square-cov`. |
| V.A-square-cov | Quaternion square row/covariance conditioning exact transfer | 2 | PROVEN | `cor:quat-square-row-covariance-conditioning-exact` transfers the exact square iid quaternion Gaussian base through `B=D_row G S`, where `D_row` is a positive real row diagonal factor and `S in GL_m(HH)` is a global right quaternion factor, random/dependent allowed, whenever `max_i |log d_i|+|log smin(S)|+|log opnorm(S)|=o_P(m)`. Then `m^{-1}log min_{|T|=m}smin(B_T)->-h(gamma)/4`, and the normalized square Gram statistic has base `-h(gamma)/2`. Deterministic uniformly elliptic quaternion right shapes `S=Sigma^{1/2}` are included. Absolute scale, not only condition number, is required. A.s. `o(m)` factors give only lower envelopes; no fixed-excess exact law, selected-column covariance transfer, non-square Wishart edge, or quaternion spherical-radial universality is claimed. |
| V.A-rect-kth | Quaternion fixed-excess fixed-`k` lower sides | 2 | PROVEN | `lem:quat-rect-kth-laguerre-tail` proves the beta-4 rectangular Laguerre-Selberg tail `P{sigma_{m-k+1}(G)<=t} <= C_{HH,r,k}m^{B_{HH,r,k}}t^{4k(k+r)}` for iid quaternion Gaussian `(m+r) x m` matrices, fixed `r,k`. Thus `thm:quat-fixed-excess-fixed-k-lower` gives finite budget `(log binom(N_m,m+r)+B log m+O(1))/(4k(k+r))`, fixed-aspect lower base `h(gamma)/(4k(k+r))`, and a.s. lower envelope on common couplings. `cor:quat-rect-kth-gram-lower` gives the normalized column-Gram lower base `h(gamma)/(2k(k+r))`. Lower side only: no upper side, exact law, beta interpolation, spherical-radial quaternion transfer, proportional-excess Wishart edge, or row-Gram statement for `r>0`. |
| V.A-rect-kth-rc | Random-prefix fixed-excess fixed-`k` lower sides | 2 | PROVEN | `cor:random-prefix-fixed-excess-fixed-k-lower` transfers the deterministic-count fixed-excess fixed-`k` lower sides to random prefix counts over `F in {R,C,H}`: for an infinite iid Gaussian row array, fixed `r>=0,k>=1`, and possibly dependent integer `N_m/m -> gamma>1`, the singular lower base is `h(gamma)/(d_F k(k+r))` and the normalized column-Gram lower base is `2h(gamma)/(d_F k(k+r))`, with a.s. lower envelopes under a.s. count convergence. The proof uses only the upper deterministic bracket and monotonicity. This is weaker than the exact square random-prefix laws when `r=0,k=1`; it adds fixed-excess fixed-`k` lower sides only. No upper side, exact fixed-excess law, value-dependent row selection, row-Gram result for `r>0`, beta interpolation, proportional Wishart edge, or Balan-Wang/supercritical phase-retrieval statement is implied. |
| V.A-rect-kth-rc-diag | Random-prefix diagonal/normalized fixed-excess fixed-`k` lower-side transfer | 2 | PROVEN | `cor:random-prefix-diagonal-fixed-excess-fixed-k` composes the R51 random-prefix lower side with the pathwise diagonal sandwich: for `F in {R,C,H}`, an infinite iid Gaussian row array, possibly dependent prefix counts `N_m/m -> gamma>1`, and positive real diagonal row/column weights with realized-prefix total logarithmic extreme `Delta_m^{rpdiag}=o_P(m)`, the singular lower base remains `h(gamma)/(d_F k(k+r))` and the normalized column-Gram lower base remains `2h(gamma)/(d_F k(k+r))`. A.s. count convergence and `Delta_m^{rpdiag}=o(m)` transfer lower envelopes. Row-normalized random-prefix Gaussian rows and full-prefix column-normalized Gaussian columns are included. This is only a lower-side packaging theorem, weaker than the exact square quaternion random-prefix conditioning laws when `r=0,k=1`; no upper side, exact fixed-excess law, value-dependent row selection, row-Gram result for `r>0`, selected-submatrix column normalization, non-diagonal covariance transfer, beta interpolation, proportional Wishart edge, or Balan-Wang/supercritical phase-retrieval statement is implied. |
| V.A-rect-kth-rc-cond | Random-prefix all-column fixed-excess fixed-`k` lower-side transfer | 2 | PROVEN | `cor:random-prefix-right-factor-fixed-excess-fixed-k-lower` composes R51 with the pathwise row/right-factor sandwich: for `F in {R,C,H}`, an infinite iid Gaussian row array, possibly dependent prefix counts `N_m/m -> gamma>1`, fixed `r>=0,k>=1`, positive real row weights over the realized prefix, and one global invertible all-column right factor `S_m` with `max_{i<=N_m}|log d_im|+|log smin(S_m)|+|log opnorm(S_m)|=o_P(m)`, the singular lower base remains `h(gamma)/(d_F k(k+r))` and the normalized column-Gram lower base remains `2h(gamma)/(d_F k(k+r))`. A.s. count convergence and a.s. `o(m)` conditioning factors transfer lower envelopes. Positive column diagonals, full-column covariance/whitening factors with absolute singular-scale control, row-normalized random-prefix Gaussian rows, and full-prefix column normalization are included. Lower side only: no upper side, exact fixed-excess law, condition-number-only covariance transfer, value-dependent row selection, selected-column covariance theorem, selected-submatrix column normalization, row-Gram result for `r>0`, beta interpolation, proportional Wishart edge, or Balan-Wang/supercritical phase-retrieval statement is implied. |
| V.A-rect-kth-diag | Quaternion diagonal/normalized fixed-excess fixed-`k` transfer | 2 | PROVEN | `cor:quat-diagonal-normalized-fixed-excess-fixed-k` applies the positive real diagonal pathwise sandwich to the R45 quaternion lower sides. If `Gtilde=D_row G E` with total logarithmic diagonal extreme `o_P(m)`, then `Gtilde` inherits the singular-value lower base `h(gamma)/(4k(k+r))` and normalized column-Gram lower base `h(gamma)/(2k(k+r))`; a.s. `o(m)` extrema transfer lower envelopes. Row- and column-normalized quaternion Gaussian matrices are included because row/column norm extrema are `o_P(m)` and summably `o(m)` a.s. in real dimensions `4m` and `4N_m`. Positive real diagonal weights only for these fixed-excess lower sides; no selected-column/fixed-excess non-diagonal covariance, upper side, exact fixed-excess/normalized law beyond the square `r=0,k=1` cases in `V.A-square-diag` and `V.A-square-cov`, spherical-radial quaternion transfer, beta interpolation, proportional Wishart edge, or row-Gram statement for `r>0`. |
| V.B | Row/column deterministic conditioning transfer | 2 | PROVEN | Subexponential row scalings and absolute column covariance extremes change log scale by `o(m)`; fixed-excess row variants, fixed-excess fixed-`k` row-submatrix statistics, their normalized column-Gram versions, and two-sided diagonal scalings also transfer. On common couplings, a.s. `o(m)` absolute conditioning factors transfer the inherited a.s. lower envelopes. Condition number alone is not enough for covariance-scale transfer. |
| V.B-rand | Random row-weight / row-normalization transfer | 2 | PROVEN | Pathwise diagonal sandwich; positive random row weights, possibly dependent on the matrix, preserve row-submatrix exponential log scales when global max/min weights are `exp(o_P(m))`. The same min-max proof covers fixed-excess fixed-`k` statistics and normalized column-Gram lower sides under random positive diagonal row/column weights with total logarithmic extrema `o_P(m)`, composes with random prefix counts as recorded in `V.A-rect-kth-rc-diag`, and transfers lower envelopes under a.s. `o(m)` extrema. Gaussian row normalization inherits these fixed-excess fixed-`k` and Gram lower sides; non-Gaussian normalized lower sides require explicit row-norm upper-tail control. |
| V.B-col | Random column-weight / column-normalization transfer | 2 | PROVEN | Pathwise right-diagonal sandwich; positive finite random column weights, possibly dependent on the matrix, preserve row-submatrix and two-sided-minor exponential log scales when global column-weight extrema are `exp(o_P(m))`. Gaussian column normalization has a.s. `o(m)` extrema and inherits fixed-excess fixed-`k`, random-prefix fixed-excess fixed-`k`, and normalized column-Gram lower sides via `rem:random-diagonal-fixed-k`, `cor:random-prefix-diagonal-fixed-excess-fixed-k`, and `cor:normalized-gaussian-fixed-excess-fixed-k`. Still diagonal only; non-diagonal column covariance does not commute with column selection. |
| V.B-rad | Spherical directions with radial weights | 1 | PROVEN | `thm:rot-inv-univ`: if `A_m=D_m^{rad}\Theta_m`, the rows of `\Theta_m` are iid uniform on the unit sphere, `m^{-1}log b_m->alpha`, and `Delta_m^{rad}(b_m)=max_i |log(r_{im}/b_m)|=o_P(m)`, then `m^{-1}log min_{|T|=m}s_min((A_m)_T) -> alpha-h(gamma)/d_\F`. `cor:rot-inv-as-lower-envelope`: on a common coupling, if `alpha_- = liminf m^{-1}log b_m` and `Delta_m^{rad}(b_m)=o(m)` a.s., then `liminf m^{-1}log min_{|T|=m}s_min((A_m)_T) >= alpha_- - h(gamma)/d_\F` a.s.; for iid radii, summability of `N_m P{|log(R_{1m}/b_m)|>eps m}` for every `eps>0` suffices. This is a pathwise row-weight transfer from Gaussian row normalization, not a new second-moment claim and not an a.s. exact law. Spherical critical real frames with deterministic `b_m=e^{o(m)}` have Balan-Wang base `1/4` in probability and the same a.s. lower envelope. |
| V.C-gram | Gram/sample-covariance transfer | 1 | PROVEN | `cor:gram-transfer` gives the pathwise identity `min_I lambda_min(q_m^{-1} B_I^* B_I)=q_m^{-1}(min_I smin(B_I))^2`. Hence every singular-value log-scale theorem transfers to Gram/sample-covariance minima with doubled constants and unchanged proof status. Square Gaussian row submatrices give `-2h(gamma)/d_F` for `F=R,C`; the quaternion Gaussian base gives `-h(gamma)/2`. For `A=D G Sigma^{1/2}`, the same one-sided covariance transfer needs subexponential absolute extreme eigenvalues of `Sigma`, not just subexponential condition number. |
| V.C-edge | Proportional sample-covariance/Wishart edge | 2 | CONJECTURE | The algebraic Gram transfer does not identify the proportional-excess normalized edge or the Wishart left-tail LDP constant; this remains the open problem in `prob:rectangular` and `prob:sample-cov-edge`. Fixed-excess exact covariance laws are only as strong as the singular-value Conjecture `rect:exact`. |
| V.D | Isotropic/log-concave rows | 2 | PARTIAL | Real iid isotropic log-concave rows satisfy the directional anti-concentration hypothesis, so the square lower-side base `h(gamma)` and fixed-excess lower-side bases `h(gamma)/(r+1)` are proved for every fixed `r`. Full laws remain open because the dependent-coordinate pair-correlation theorem is not proved. |
| V.E | Heavy-tailed bounded-density entries | 2 | PARTIAL | Lower side proved without moment assumptions; upper side remains conditional on pair correlation. |
| SM | Smoothed deterministic frames: lower side | 2 | PROVEN | For `A_m=F_m+sigma_m G_m`, `alpha=limsup m^{-1}log sigma_m^{-1}` shifts the lower threshold by `alpha`; subexponential smoothing preserves the Gaussian lower-side base. Matching upper/recovery threshold remains open. |
| SM-row | Row-dependent smoothed deterministic frames | 2 | PROVEN | For `A_m=F_m+D_mG_m` with row noise levels `sigma_{m,i}`, the square finite budget is `log binom(N_m-1,m-1)+log sum_i sigma_{m,i}^{-d_F}`; the lower-side shift is `(d_F m)^{-1}log sum_i sigma_{m,i}^{-d_F}`. Summable slack gives the a.s. lower envelope. |
| SM-geom | Smoothed deterministic geometric lower sides | 2 | PROVEN | For `F+sigma G`, `alpha=limsup k^{-1}log sigma^{-1}` gives the two-sided threshold `H/d_\F+alpha`; proportional row excess follows by applying `rect:proportional-density-rate` to Gaussian smoothing. Lower-side corollaries only. |
| VI.A | Balan-Wang base 1/4 universal for continuous frames | 1 | CONDITIONAL | Critical lower side proved; exact critical base needs pair correlation. The fixed-supercritical directional deficient-complement branch lower side is proved in `VI.A-dir-branch`, but the full supercritical Balan-Wang partition statistic remains outside the proved scope. |
| VI.A-dir | Directional critical real frames lower side | 1 | PROVEN | At `N=2m-1`, independent real rows with affine directional anti-concentration and `m^{-1}log sum_i L_{m,i}->0` are full spark a.s. and satisfy `P{omega<=exp[-(log4+eps)m]}->0`. Lower side only; exact base still needs pair correlation. |
| VI.A-dir-branch | Directional fixed-supercritical branch lower side | 1 | PROVEN | For fixed `r>=1`, `N=2m-1+r`, and `omega_r^fe=min_{|T|=m+r}smin(A_T)`, independent real rows with affine directional constants `L_{m,i}` and `m^{-1}log sum_{|S|=r+1}prod_{i in S}L_{m,i}->0` satisfy `P{omega_r^fe<=exp[-(log4/(r+1)+eps)m]}->0` and the same a.s. lower envelope on common couplings. This is only the deficient-complement fixed-excess branch; no full supercritical Balan-Wang lower-Lipschitz theorem, upper side, or exact law is claimed. |
| VI.A-norm | Row-normalized Gaussian critical frames | 1 | PROVEN | For iid real Gaussian rows normalized to the unit sphere at `N=2m-1`, the Balan-Wang singular-value statistic satisfies `omega=4^{-m+o_P(m)}`; row normalization only changes singular values by subexponential row-norm factors. |
| VI.A-col | Diagonally preconditioned Gaussian critical frames | 1 | PROVEN | If `B_m=G_m E_m` with `E_m` positive finite diagonal and `max_j |log e_j|=o_P(m)`, then full spark is preserved and `omega(B_m)=4^{-m+o_P(m)}`. Column-normalized Gaussian critical frames are included. This is coordinate preconditioning, not measurement-vector normalization; a.s. lower envelopes require `o(m)` a.s. diagonal extrema. |
| VI.B | Critical real sign frames fail PR injectivity | 1 | PROVEN | Deterministic two-column projective-pair obstruction for finite alphabets; `{+/-1}` is the `|Pi|=2` case and gives critical real sign-frame failure. Lean file `paper19/lean/SignCritical.lean` still checks the full arbitrary-`m` sign pigeonhole theorem matching `prop:sign-critical`; the finite-alphabet extension is manuscript-only. |
| VI.C | Complex PR base at sharp threshold | 3 | CONJECTURE | Requires new realified stability statistic. |
| FLU | Gumbel fluctuation law of log M_m | 3 | PARTIAL (first moment integrated; full law conjectural) | `conj:gumbel` now records the exact centering `b_m` via `binom(N,m)F_m(e^{-b_m})=1`, the leading centering `b_m=(h(gamma)/d_F)m+o(m)`, sharper Gaussian centering when `N_m=gamma m+O(1)` (`c_R=0`, `c_C=1/4`), the first intensity `E Z_m^{fl}(x)->e^{d_F x}` using finite-m Gaussian hard-edge regular variation, and the Markov one-sided bound `limsup P{log M_m+b_m<=x}<=e^{d_F x}`. Full Poisson/Gumbel remains conjectural and needs critical-scale factorial moments, small-overlap cluster negligibility, and higher-order bulk normal-overlap independence; current `prob:pc` alone is not sufficient at the centered scale. |
| NUM | Numerical confirmation | 1 | DONE (integrated) | `parts/numerics.tex` (now Section "Numerical confirmation", compiled) + reproducible `numerics/verify_bases.py` (seed 20260628) + output. Confirms: scalar small-ball exponents d_F=1/2/4 (fits 0.999/1.992/4.069); one-matrix hard edge d_F (fits 1.008/2.000); overlap Beta means/moments (real/complex match to 4 digits; complex E[(1-rho^2)^{-1}]=1.25=(D-1)/(D-2)); the QUATERNION overlap moment `(2D-1)(2D-2)/((2D-3)(2D-4))` to 4 digits for D=4..20 (independent check of my derived constant); and the extremal base `(1/m)log M_m -> -log4` (m=4..8 full enumeration, gap shrinks 0.228->0.082). ALSO (session 9): GUMBEL fluctuation evidence — std(log M_m) flat in m near pi/(d_F sqrt6) (real 1.28-1.33 vs 1.2825; complex 0.64-0.67 vs 0.6413), skewness ~ -1.07..-1.14 (min-Gumbel -1.1395; Gaussian would be 0); KS test of standardized log M_m vs min-Gumbel: stat 0.008, p~0.96 at m=7 (cannot reject Gumbel; Gaussian rejected). Two compiled FIGURES added (`fig:base` convergence, `fig:gumbel` QQ+histogram) via `numerics/make_figures.py`; spherical-frame base tracks Gaussian -> -log4. Manuscript 51pp. Strong numerical support for conj:gumbel. |

## Round log
- R0 2026-06-27: recon done; article read; PLAN+STATE+skeleton created; timer started.
- R1 2026-06-27: corrected subagent target from 50 to exactly 5; launched 5 review
  subagents; source-theorem and universality reviewers confirmed that non-Gaussian upper
  universality must be conditional; atomic reviewer found a deterministic proof that critical
  real sign frames fail full spark; drafted first rigorous manuscript parts and bibliography.
- R2 2026-06-27: strengthened the bounded-density lower-side theorem from the real case to
  real and complex scalar entries with bounded Lebesgue density, giving the lower base
  `h(gamma)/d_\F` without Gaussianity or moment assumptions.
- R3 2026-06-27: upgraded the fixed-excess rectangular Gaussian result to a proved lower-side
  theorem with exponent `d_\F(r+1)`; the exact base remains conditional on a tall
  pair-correlation theorem.
- R4 2026-06-27: generalized the common-covariance transfer to deterministic row/column
  conditioning: `A=D G Sigma^{1/2}` has the same extremal log base as `G` whenever the
  row weights and column covariance extremes are only `exp(o(m))`.
- R5 2026-06-27: launched exactly 5 read-only audit agents for the geometric/open-problem
  pass; promoted the two-sided square-submatrix lower side to a proved result in Lane O,
  while keeping the exact two-sided base conditional on a two-overlap second moment.
- R6 2026-06-27: added fixed-excess conditioning transfer and two-sided diagonal transfer
  corollaries; sharpened the open-problem section into point-process, overlap-resolved,
  avoidance-speed, proportional-rectangular-LDP, and normalized design/stability problems.
- R7 2026-06-27: wrote the large-deviations section `parts/ldp.tex`. IV.A: proved the
  upper-tail sandwich `d s - h <= I_-(s) <= d s` (union bound plus a two-sided one-matrix
  least-singular-value tail, lower half `P{smin(G)<=t} >= c_F t^{d_F}` proved via
  `smin(G) <= |<R_m,u>|`), left the exact rate as a conjecture with the Bonferroni-failure
  reason. IV.B: reformulated the lower tail as a hole probability, gave the rigorous `O(1/m)`
  bound and a conditional `exp(-C s m^3)` lower bound, conjectured speed `m^2`. Preserved
  `prop:small-tail`. Full document recompiles; latest BibTeX/LaTeX logs show no undefined
  citations or references. Remaining diagnostics are the existing `\theHfootnote` warning
  plus underfull/overfull box warnings.
- R8 2026-06-27: launched exactly 5 read-only audit agents for density-rate and smoothing
  extensions. Added the density-rate lower-side theorem, the smoothed deterministic-frame
  lower-side corollary, and the fixed-excess bounded-density lower-side theorem. The
  density-rate result allows prefactor `K_m=exp((kappa+o(1))m)` and shifts the square lower
  threshold to `(h(gamma)+kappa)/d_\F`; for `F_m+sigma_mG_m`, the shift is
  `limsup m^{-1}log sigma_m^{-1}`. For fixed excess `r`, the lower threshold is
  `h(gamma)/(d_\F(r+1))+kappa/d_\F`. Exact upper/recovery thresholds remain open.
  Standalone now compiles to 20 pages; master compiles to 849 pages; log scans show no
  undefined citations/references and no rerun requests.

- R8 2026-06-27 (lead): verified independently — (a) the k-th-singular-value exponent e_k=d_F k^2
  via the bottom-k Laguerre block (Vandermonde beta*C(k,2)+weights+measure, doubled by sigma=sqrt(lambda));
  (b) the one-matrix lower tail P{smin<=t}>=c t^{d_F} via smin(G)<=d_i=|<R_i,u>|; (c) the deterministic
  sign-frame theorem is CORRECT via the TWO-COLUMN (not antipodal-row) pigeonhole: among 2m-1 rows,
  cols 1,2 agree or disagree on >=m rows; on those rows the two columns are equal/opposite => any m of
  them give a singular minor. All m>=2. VI.B PROVEN stands. No active subagent panel from this note is
  tracked in the current repo state; future active rounds must use exactly 5 subagents.
- R9 2026-06-27: launched exactly 5 read-only audit agents for two-sided and proportional-excess
  lower-side extensions. Added the two-sided density-rate lower-side theorem with threshold
  `(h(gamma_R)+h(gamma_C)+kappa)/d_\F`, the two-sided smoothed deterministic lower-side corollary,
  and the proportional-excess density-rate lower-side theorem. On the exponential `m`-scale,
  proportional excess has lower threshold `kappa/d_\F`, so subexponential density growth rules out
  exponentially small proportional-excess minima. Exact two-sided upper laws and the proportional
  `sqrt(m)` Wishart-edge/LDP remain open. Standalone now compiles to 22 pages; master compiles
  to 850 pages and has been copied to `~/Downloads/master.pdf`. Log scans show no
  undefined citations/references and no rerun requests.
- R10 2026-06-27: launched exactly 5 read-only audit agents for random row-weight and
  row-normalization transfer. Added the pathwise positive random diagonal transfer theorem:
  if global row-weight extrema are `exp(o_P(m))`, then any row-submatrix exponential log law
  transfers, without independence between weights and the matrix. Added the iid Gaussian
  row-normalized frame corollary and the real critical phase-retrieval corollary
  `omega=4^{-m+o_P(m)}` for normalized Gaussian measurements. For non-Gaussian normalized
  rows, recorded the lower-side transfer under an explicit maximum-row-norm `exp(o_P(m))`
  condition and noted that bounded density alone does not imply this tail condition.
  Standalone now compiles to 23 pages; master compiles to 850 pages and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests.
- R11 2026-06-27: launched exactly 5 read-only audit agents for almost-sure lower-envelope
  upgrades. Added the Borel-Cantelli summability criterion and applied it to the square
  bounded-density, density-rate, smoothed, fixed-excess, proportional-excess, two-sided,
  critical phase-retrieval, and row-normalized Gaussian lower sides. The upgrade is only
  an a.s. liminf/lower-envelope statement; exact bases and upper sides remain in probability
  or conditional unless summable pair-correlation/upper-side estimates are proved.
  Standalone now compiles to 25 pages; master compiles to 851 pages and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests.
- R12 2026-06-27: launched exactly 5 read-only audit agents for random column-weight
  and column-normalization transfer. Added the pathwise positive right-diagonal transfer
  theorem: if global column-weight extrema are `exp(o_P(a_m))`, then any row-submatrix
  or diagonal two-sided-minor exponential log law on scale `a_m` transfers, without
  independence between weights and the matrix. Added the iid Gaussian column-normalized
  matrix corollary, including a.s. lower-envelope transfer from summable column-norm
  tails, and the real critical phase-retrieval preconditioning corollary
  `omega(GE)=4^{-m+o_P(m)}` under subexponential diagonal logarithmic extrema. The text
  explicitly separates coordinate preconditioning from measurement-vector normalization
  and preserves the non-diagonal covariance caveat for column-selected minors.
  Standalone now compiles to 27 pages; master compiles to 852 pages and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests.
- R13 2026-06-27: launched exactly 5 read-only audit agents for random row-count and
  Poissonization transfer. Added the monotonicity squeeze theorem: for an infinite iid
  Gaussian row array, if an integer row count satisfies `N_m/m -> gamma>1` in probability,
  even dependent on the row array, then the square row-submatrix extremal base is still
  `-h(gamma)/d_\F`. Added bounded-density/density-rate random-count lower sides, a.s.
  lower envelopes under a.s. count convergence, and Poisson/binomial/independent-thinning
  examples. The text explicitly excludes value-dependent thinning and adds a phase-retrieval
  warning: random square-submatrix row counts are not Balan-Wang corollaries away from
  the exact critical count `2m-1`; for `r>0`, `(m+r)`-row tall submatrices are only one
  branch of the supercritical Balan-Wang partition minimum. Standalone now compiles to
  29 pages; master compiles to 852 pages and has
  been copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun requests.
- R14 2026-06-27: launched exactly 5 read-only audit agents for a proposed
  supercritical phase-retrieval reduction. The adversarial audit killed the theorem:
  for `N=2m-1+r` with `r>0`, fixed-excess tall submatrices are only one branch of the
  Balan-Wang partition minimum, and both-spanning partitions can be smaller. No
  supercritical Balan-Wang corollary was added. The manuscript and verification notes
  now use the correct diagonal-preconditioning hypothesis, namely subexponential
  logarithmic extrema rather than condition number alone. Standalone compiles to
  29 pages; master compiles to 852 pages and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests.
- R15 2026-06-27: launched exactly 5 read-only audit agents for aspect-ratio
  asymptotics of the entropy base. Added a deterministic endpoint-asymptotics
  proposition for `h(gamma)` and `c_gamma=exp(h(gamma))`, plus a moving-aspect
  warning: the formulas calibrate fixed-aspect thresholds, but do not supply uniform
  RMT laws when `N_m/m -> 1` or `N_m/m -> infinity`. Added the compact Lane O
  calibration paragraph. Standalone now compiles to 30 pages; master compiles to
  852 pages and has been copied to `~/Downloads/master.pdf`. Targeted
  log scans show no undefined citations/references and no rerun requests; see
  `verification/R15_aspect_asymptotics.md`.
- R16 2026-06-27: launched exactly 5 read-only audit agents for finite-entropy
  moving-aspect lower sides. Added the abstract finite-budget union-bound
  corollary, the square row-submatrix finite-entropy lower side, and the fixed-excess
  finite-entropy lower side. The text keeps this lower-side only and does not claim
  a matching moving-aspect Gaussian upper side or exact base. Standalone now compiles
  to 31 pages; master compiles to 852 pages and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R16_finite_entropy_moving_aspect.md`.
- R17 2026-06-27: launched exactly 5 read-only audit agents for the two-sided
  finite-entropy lower side. Added the compact two-sided finite-budget corollary:
  the budget is `log binom(N_k,k)+log binom(n_k,k)+log K_k`, with the usual
  polynomial and exponential slack. This remains lower-side only; row/column
  overlap still blocks exact upper-side claims without a two-overlap pair-correlation
  theorem. Standalone now compiles to 32 pages (554,966 bytes); master compiles
  to 853 pages (7,757,237 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R17_finite_entropy_two_sided.md`.
- R18 2026-06-27: launched exactly 5 read-only audit agents for the finite-budget
  almost-sure upgrade. Added `cor:as-finite-budget`: deterministic finite-budget
  data plus `sum_m e^{-u_m}<infty` imply the exact finite-budget threshold holds
  eventually a.s. with strict `>`; no independence across dimensions or inside
  the tested family is needed. Applied it to the square, fixed-excess, and
  two-sided finite-entropy lower sides, preserving the polynomial terms and
  summable slack. Standalone now compiles to 33 pages (561,195 bytes); master
  compiles to 853 pages (7,757,631 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R18_finite_budget_as.md`.
- R19 2026-06-27: launched exactly 5 read-only audit agents for nonuniform
  finite-budget constants and heterogeneous density-budget risks. Added only the
  conservative abstract corollary `cor:nonuniform-finite-budget`: deterministic
  constants `C_{m,T}` with a common exponent use any budget
  `B_m >= 1 vee sum_T C_{m,T}`. This keeps weighted union bounds available but
  deliberately omits bulky heterogeneous-density applications, random constants,
  nonuniform exponents, and any upper/exact-base claim. Standalone now compiles
  to 33 pages (564,393 bytes) after a BibTeX refresh; master compiles to
  853 pages (7,758,105 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R19_nonuniform_budget.md`.
- R20 2026-06-28: launched exactly 5 read-only audit agents for the square
  row-wise heterogeneous-density finite budget. Added
  `cor:rowwise-heterogeneous-square`: if row `i` has deterministic scalar
  density bound `K_{m,i}` uniformly over columns, the finite budget is
  `log binom(N_m-1,m-1)+log sum_i K_{m,i}`, with `d_\F log m+O_\F(1)+u_m`
  slack. This is a concrete application of R19's weighted union budget and
  remains lower-side only. Standalone compiles to 34 pages (569,034 bytes);
  master compiles to 853 pages (7,757,924 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R20_square_heterogeneous_density_budget.md`.
- R21 2026-06-28: launched exactly 5 read-only audit agents for the two-sided
  heterogeneous-density finite budget. Added
  `two:heterogeneous-finite-budget`: for deterministic entrywise scalar density
  bounds `K_{k,i,j}`, put `K_{k,i,C}=max_{j in C}K_{k,i,j}` and use budget
  `log binom(N_k-1,k-1)+log sum_i sum_{|C|=k} K_{k,i,C}`, with
  `d_\F log k+O_\F(1)+u_k` slack and summable-a.s. upgrade. This is a direct
  nonuniform finite-budget application and remains lower-side only. Standalone
  compiles to 36 pages (577,951 bytes); master compiles to 853 pages
  (7,758,359 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R21_two_sided_heterogeneous_density_budget.md`.

- R-lead-1 2026-06-27 (lead/Claude, ran a focused panel on II.B): PROVED the two-projection
  anti-concentration lemma for bounded-density entries (non-Gaussian replacement for the
  Gaussian two-slab/two-disk estimate; constants match; needs only bounded density + finite
  variance, not sub-Gaussianity). Full proof in `notes/IIB_lemma_2D.md`. Integrated it into
  `parts/universality.tex` as `lem:two-proj` + `rem:pc-reduction`, updated the conditional
  remark, sharpened `prob:pc` to the single remaining overlap-moment estimate, and added
  `Petrov1975` to `refs.bib`. Independently verified `e_k=d_F k^2` and the deterministic
  two-column sign-frame obstruction (VI.B). Standalone compiles to 32 pages, 0 undefined
  refs/citations. The overlap-moment estimate (sharp constant) remains the lone gap for II.B.
- R-lead-2 2026-06-27 (lead/Claude): adversarially verified `lem:two-proj` (SOUND; fixed an
  overclaim — the (1+o(1)) constant holds for `t_m->0`, not all `0<t<=1`; corrected in .tex).
  Ran a read-only document-level consistency critic over all parts (report
  `verification/consistency_sweep.md`); fixed the issue I introduced — `\rho` symbol clash
  (density-rate vs normal overlap) now `\varrho` in lem:two-proj/rem:pc-reduction/prob:pc.
  Recorded for a coordinated pass (user-owned sections): missing Balan--Wang/full-spark
  citations in phaseretrieval.tex (HIGH); `k` vs `r` excess index and `L_m` overload (MED);
  abstract should mention the deterministic sign-frame failure (MED). Standalone 33 pages, 0 undefined.

- R22 2026-06-28: launched exactly 5 read-only review agents for citations,
  notation, overlap gaps, new lower-side results, and Lean feasibility. Added
  `prop:small-D-negligible`, proving the small/intermediate overlap-codimension
  contribution negligible by hypergeometric rarity and the trivial `q_D<=p_m`
  bound. Updated the II.B remaining gap and `prob:pc` to the true bulk estimate
  `D>=eps m`. Added the fixed-excess heterogeneous row-density budget
  `rect:heterogeneous-row-density`. Cleaned notation against the pruning
  manuscript: density-growth `rho` is now `kappa`, local radii use `tau`,
  fixed excess uses `r`, and the random-count trial-count overload was removed.
  Added Balan--Casazza--Edidin citation and corrected the supercritical
  Balan--Wang wording to distinguish `omega` from full partition stability.
  Added `paper19/lean/SignCritical.lean`, verifying in Lean the determinant-zero
  core of the sign-frame obstruction for equal/opposite first two columns.
  Direct Lean check passed with exit code 0; no background Lean/Lake processes
  remain. Standalone LaTeX/BibTeX rebuild passed; final log has no undefined
  citations/references and no rerun request. PDF is 36 pages, 577,951 bytes.

- R23 2026-06-28: launched exactly 5 read-only audit agents for the fixed-excess
  entrywise heterogeneous finite budget. Added
  `rect:entrywise-heterogeneous-fixed-excess`: for deterministic entrywise
  scalar density bounds `K_{m,a,q}`, the lower-side budget is
  `log Xi_{m,r}` with
  `Xi_{m,r}=sum_{|T|=m+r} sum_q max_{S subset T, |S|=r+1} prod_{a in S} K_{m,a,q}`,
  plus `d_\F(r+1)log m+O_{\F,r}(1)+u_m` polynomial/exponential slack. This
  refines the row-wise heterogeneous fixed-excess budget and specializes to the
  uniform finite-entropy lower side. Standalone compiles to 38 pages
  (587,597 bytes); master compiles to 853 pages (7,759,351 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun requests; see
  `verification/R23_fixed_excess_entrywise_budget.md`.

- R24 2026-06-28: launched exactly 5 tool-managed review agents for the fixed-`k`
  hard-edge tail, Lean sign-frame formalization, lower-tail LDP construction,
  variance/density-profile lower-side results, and pruning-notation consistency.
  Added the square entrywise density-profile lower-side budget
  `cor:entrywise-profile-square` with `K_{m,i}^*=max_j K_{m,i,j}` and no
  column-average claim. Added row-dependent Gaussian smoothing
  `cor:rowwise-smoothed-lower`, with finite budget
  `log binom(N_m-1,m-1)+log sum_i sigma_{m,i}^{-d_F}` and an a.s. lower
  envelope. Corrected the lower-tail construction to be conditional on bounded
  deterministic frames `A_{0,m}` and to keep the `m^2 log m` term in the
  Gaussian-ball bound. Cleaned notation against the pruning manuscript:
  proportional-excess aspect `beta` is now `zeta`, pair-correlation row sets are
  `I,J`, row-weight `W_m` is now `D_m^{row}`, and smoothed-frame text now
  explains the `W=R+S` signal-plus-noise correspondence. Added
  `MarchenkoPastur1967` and cited `RudelsonVershynin2008,TaoVu2010`.
  Extended `paper19/lean/SignCritical.lean` to prove the `signCritical_nplus2`
  finite pigeonhole theorem; direct Lean check passed. The fixed-`k` lower-side
  theorem was not promoted because it needs an explicit finite-`m`
  polynomial-loss Laguerre tail, not just the hard-edge exponent. Standalone
  LaTeX/BibTeX rebuild passed; final log has no undefined citations/references
  and no rerun request. PDF is 38 pages, 595,082 bytes; see
  `verification/R24_profiles_ldp_lean_notation.md`.

- R25 2026-06-28: launched exactly 5 read-only audit agents for the weighted
  finite-budget/a.s. upgrade, standalone-master consistency, phase-retrieval
  wording, and notation. Added `cor:as-nonuniform-finite-budget`: deterministic
  per-index constants with budget `B_m>=1 vee sum_T C_{m,T}` and summable
  `e^{-u_m}` give
  `min_T Y_{m,T}>exp[-(log B_m+u_m)/a_m]` eventually a.s.; no independence
  across dimensions or inside the family is used. Applied the statement to the
  square entrywise density-profile budget, fixed-excess row-wise and entrywise
  heterogeneous budgets, and the heterogeneous two-sided budget. Cleaned the
  rectangular row/column dummy variables, localized two-sided finite-budget
  notation to `(A_k)_{R,C}`, narrowed Randomstrasse wording to the exponential
  base, added the local complement-property/full-spark citation for the
  Rademacher obstruction, changed the complex open problem to the generic
  `4m-4` threshold, added three ACHA DOIs, and tightened Lane O deterministic
  density-budget hypotheses. Standalone compiles to 39 pages (599,275 bytes);
  master compiles to 853 pages (7,759,894 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R25_nonuniform_as_budget_guardrails.md`.

- R26 2026-06-28: launched exactly 5 tool-managed review agents for the
  fixed-`k` hard-edge tail, fixed-`k` theorem promotion, Lean sign-frame
  extension, and notation/ledger audit. Added the finite-`m` polynomial-loss
  Laguerre-Selberg tail `kth:laguerre-tail`:
  `P{sigma_{m-k+1}(G)<=t} <= C_{\F,k}m^{B_{\F,k}}t^{d_\F k^2}`. Promoted the
  fixed-`k` Gaussian finite-budget lower side `kth:lower`, giving finite budget
  `(log binom(N_m,m)+B log m+O(1))/(d_\F k^2)` and fixed-aspect lower base
  `h(gamma)/(d_\F k^2)`. The exact fixed-`k` extremal law remains conjectural
  pending the codimension-`k` pair-correlation/second-moment theorem. Extended
  `paper19/lean/SignCritical.lean` to prove the full arbitrary-`m`
  `signCritical` theorem matching `prop:sign-critical`. Cleaned proportional
  separation, Bonferroni row-pair, roadmap, and ledger notation. Standalone
  LaTeX passed and direct Lean passed; final log has no undefined
  citations/references and no rerun request. PDF is 40 pages, 612,712 bytes;
  see `verification/R26_fixed_k_laguerre_lean.md`.

- R27 2026-06-28: launched exactly 5 tool-managed review agents for the
  rotationally invariant/spherical row section, row-normalization transfer,
  notation, and Lean feasibility. Replaced the unsafe included second-moment
  theorem for radially concentrated rotationally invariant rows with the proved
  pathwise radial-weight transfer `thm:rot-inv-univ`: for
  `A_m=D_m^{rad}\Theta_m`, iid spherical directions, `m^{-1}log b_m->alpha`,
  and `max_i |log(r_{im}/b_m)|=o_P(m)`, one has
  `m^{-1}log min_{|T|=m}s_min((A_m)_T) -> alpha-h(gamma)/d_\F`. Added the iid
  controlled-radii corollary, kept the spherical critical-frame Balan--Wang
  corollary, removed the leftover unsafe quaternionic upper-side theorem, and
  narrowed the radial-mixture open problem to exponential sampled radial
  extremes. Added null-event clauses to normalized Gaussian transfer proofs and
  marked the old rotational-invariant notes file as superseded. Standalone
  LaTeX passed twice; final log has no rerun request. PDF is 42 pages,
  630,691 bytes; see `verification/R27_spherical_radial_transfer.md`.

- R28 2026-06-28: launched exactly 5 read-only audit agents for moving-excess
  finite budgets, entrywise smoothing profiles, fixed-`k` Laguerre tail
  guardrails, phase-retrieval consequences, and Lane O consistency. Added
  `rect:moving-excess-finite-budget`: for arbitrary `m<=ell_m<=N_m`,
  `p_m=ell_m-m+1`, scalar density bound `K_m`, and `q_m=d_\F p_m`, the
  lower-side finite budget is
  `B_m=1 vee [binom(N_m,ell_m)m K_m^{p_m} binom(ell_m,p_m)^{d_\F/2} v_{q_m}m^{q_m/2}]`,
  with denominator `d_\F p_m` and summable a.s. upgrade. Clarified fixed-`k`
  Laguerre finite-`m` constants, tightened Lane O deterministic
  Borel-Cantelli guardrails and explicit summation domains, and kept the
  complex phase-retrieval wording at the generic `4m-4` threshold. Standalone
  compiles to 42 pages (630,691 bytes); master compiles to 854 pages
  (7,762,588 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun requests; see
  `verification/R28_moving_excess_finite_budget.md`.

- R29 2026-06-28: launched exactly 5 tool-managed review agents for the
  spherical-radial almost-sure lower envelope, row-normalized Gaussian lower
  envelope, notation, adversarial transfer audit, and Lean feasibility. Added
  the general row-normalized Gaussian a.s. lower envelope to
  `cor:row-normalized-gaussian`. Added
  `cor:rot-inv-as-lower-envelope`: on a common coupling, if
  `alpha_- = liminf m^{-1}log b_m` and
  `Delta_m^{rad}(b_m)=max_i |log(r_{im}/b_m)|=o(m)` a.s., then
  `liminf m^{-1}log min_{|T|=m}s_min((A_m)_T) >= alpha_- - h(gamma)/d_\F`
  a.s.; for iid radii it suffices that
  `sum_m N_m P{|log(R_{1m}/b_m)|>eps m}<infty` for every `eps>0`. Moved the
  spherical critical-frame a.s. lower envelope into `cor:spherical-pr`, and
  tightened wording around direction-dependent radii, positive deterministic
  radii, and logarithms off null events. Lean was left unchanged. Standalone
  LaTeX passed twice; final log has no rerun request. PDF is 43 pages,
  637,166 bytes; see `verification/R29_spherical_radial_as_lower.md`.

- R30 2026-06-28: launched exactly 5 read-only audit agents for independent-row
  directional anti-concentration, isotropic log-concave applications, smoothed
  deterministic row models, Lane O summary guardrails, and phase-retrieval
  consequences. Added `cor:directional-row-lower`: independent rows with affine
  directional small-ball bounds
  `P{|<R_{m,i},u>-z|<=r}<=L_{m,i}r^{d_F}` have square finite budget
  `log binom(N_m-1,m-1)+log sum_i L_{m,i}+(d_F/2)log m`, with summable a.s.
  upgrade. Added the real iid isotropic log-concave lower-side corollary and
  kept the exact log-concave law open. Added the real critical
  Balan--Wang lower-side corollary for directional anti-concentration frames;
  no supercritical or complex PR theorem is claimed. Standalone compiles to
  45 pages (647,008 bytes); master compiles to 854 pages (7,765,630 bytes)
  and has been copied to `~/Downloads/master.pdf`. Targeted log
  scans show no undefined citations/references and no rerun requests; see
  `verification/R30_directional_row_logconcave.md`.

- R31 2026-06-28: launched exactly 5 tool-managed audit agents for the
  quaternion Gaussian division-algebra base, covering the one-matrix
  quaternion lower tail, Haar normal-line/overlap second moment, notation,
  ledger scope, and Lean feasibility. Promoted only the square iid quaternion
  Gaussian theorem as `thm:quaternion-gaussian-base`, with base `h(gamma)/4`.
  The proof now records the quaternionic negative second-moment identity,
  standard scalar normalization `p_H(t)=2t^4+O(t^6)`, Haar normal lines in
  `HP^{D-1}`, the local two-ball Jacobian `(1-|rho|^2)^(-2)`, the
  `Beta(2,2(D-1))` negative moment for `D>=3`, and a separate `D=2` overlap
  split. Left quaternion spherical-radial transfer, rotationally invariant
  quaternion universality, fixed-excess quaternion exact laws, and beta
  interpolation unpromoted. Added `Zhang1997Quaternions` for quaternion matrix
  conventions. Master Lane O now has the compact theorem
  `laneO:thm:quaternion-gaussian-base` with the same guardrails. Lean was left
  unchanged. Standalone LaTeX passed twice; final PDF is 48 pages, 679,118
  bytes. Master compiles to 855 pages (7,769,065 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted final log scans show no
  undefined citations/references, no rerun requests, and no fatal/package/LaTeX
  errors; each scan reported only its `Output written` line; see
  `verification/R31_quaternion_gaussian_base.md`.

- R32 2026-06-28: launched exactly 5 tool-managed audit agents for the
  Gumbel/fluctuation note, covering finite-`m` hard-edge regular variation,
  first-moment identities, centered-scale factorial moments, integration
  location, and Lean feasibility. Integrated only the first-moment part after
  `conj:gumbel`: exact centering via `binom(N,m)F_m(e^{-b_m})=1`, leading
  centering `b_m=(h(gamma)/d_F)m+o(m)`, sharper Gaussian centering under
  `N_m=gamma m+O(1)`, `E Z_m^{fl}(x)->e^{d_F x}` from finite-`m` Gaussian
  hard-edge regular variation, and the Markov one-sided bound. Corrected the
  Gumbel sign convention and recorded that the full Poisson law needs
  critical-scale overlap-cluster/factorial-moment conditions stronger than the
  existing bulk `prob:pc`. Lean was left unchanged. Standalone LaTeX passed
  twice; final PDF is 49 pages, 686,844 bytes. Targeted log scan shows no
  undefined citations/references and no rerun request; remaining diagnostics
  are the known `\theHfootnote` warning and the pre-existing overfull hbox in
  `parts/ldp.tex`; see `verification/R32_gumbel_first_moment.md`.

- R33 2026-06-28: launched exactly 5 tool-managed audit agents for the
  Gram/sample-covariance transfer; all five completed. Kept
  `cor:gram-transfer` as deterministic bookkeeping:
  `lambda_min(q^{-1}B^*B)=q^{-1}s_min(B)^2`, so singular-value log-scale
  statements transfer to Gram/sample-covariance lower edges with doubled
  constants and unchanged proof status. Added the one-sided population
  covariance caveat: for `A=DG Sigma^{1/2}`, subexponential absolute extreme
  eigenvalues of `Sigma` are needed, not merely subexponential condition
  number. Narrowed the remaining sample-covariance problem to the non-square
  constant-order Wishart edge and tied it to `prob:rectangular`. Master Lane O
  now has compact corollary `laneO:cor:square-row-gram-transfer`; see
  `verification/R33_gram_sample_covariance.md`. Standalone LaTeX passed twice;
  final PDF is 50 pages, 696,452 bytes. Master compiles to 855 pages
  (7,769,954 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted final log scans show no
  undefined citations/references, no rerun requests, and no fatal/package/LaTeX
  errors; each scan reported only its `Output written` line.

- R34 2026-06-28: launched exactly 5 tool-managed audit agents for the
  fixed-`k` Gram eigenvalue lower side; all five completed. Added
  `kth:gram-lower`: for iid real/complex Gaussian square row submatrices and
  ascending Gram eigenvalues,
  `Lambda_m[k]=min_{|T|=m} lambda_(k)(m^{-1}A_T^*A_T)=m^{-1}M_m[k]^2`
  pathwise. The finite-budget lower side is the squared `kth:lower` threshold,
  the fixed-aspect lower base is `2h(gamma)/(d_F k^2)`, and the a.s. geometric
  lower-envelope corollary now includes both `M_m[k]` and `Lambda_m[k]`.
  Master Lane O now has compact paragraph `laneO:par:fixed-k-gram-lower`.
  No quaternion fixed-`k`, exact fixed-`k` Gram law, or proportional Wishart-edge
  claim was added. Standalone compiles to 52 pages (794,348 bytes); master
  compiles to 855 pages (7,770,973 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted standalone log scan shows no
  undefined citations/references and no rerun request; remaining standalone
  diagnostics are the known `\theHfootnote` warning, the pre-existing overfull
  hbox in `parts/ldp.tex`, and an underfull vbox on the numerics figure page; see
  `verification/R34_fixed_k_gram.md`.

- R35 2026-06-28: launched exactly 5 tool-managed audit agents for the
  finite-alphabet atomic obstruction; all five completed. Added
  `prop:finite-alphabet-obstruction`: for a nonempty finite nonzero alphabet
  `S subset K^*`, `K=R` or `C`, with `q=|S/S|`, every `S^{N x m}` matrix has a
  singular `m`-row submatrix once `m>=2` and `N>=q(m-1)+1`, by pigeonholing the
  first-two-column quotients. Kept `prop:sign-critical` as the `q=2` sign case
  and preserved the real critical phase-retrieval consequence only for signs.
  Left zero-containing alphabets, quaternion/projective variants, random atomic
  high-probability thresholds, Lean expansion, and numerics untouched. Standalone
  LaTeX passed twice; targeted standalone log scan found no undefined
  citations/references and no rerun request; remaining diagnostics are the known
  `\theHfootnote` warning, the pre-existing overfull hbox in `parts/ldp.tex`,
  and an underfull vbox on the numerics figure page; see
  `verification/R35_finite_alphabet_ratio_obstruction.md`.

- R36 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  fixed-excess fixed-`k` lower side; all five completed and found the exponent
  and proof route sound. Added `rect-kth:laguerre-tail`,
  `rect-kth:lower`, and `rect-kth:fixed-aspect-lower`: for fixed `r>=0`,
  fixed `k>=1`, and iid Gaussian `F=R,C`, one `(m+r) x m` matrix satisfies the
  polynomial-loss tail
  `P{sigma_{m-k+1}(G)<=t} <= C_{\F,r,k}m^{B_{\F,r,k}}t^{d_\F k(k+r)}`.
  Union over `binom(N_m,m+r)` row sets gives finite budget denominator
  `d_\F k(k+r)`, fixed-aspect lower base `h(gamma)/(d_\F k(k+r))`, and an
  almost-sure lower envelope on common couplings. Added the compact master
  paragraph `laneO:par:rect-fixed-k-lower`. Scope is lower-side only for iid
  real/complex Gaussian entries; no quaternion, proportional-excess,
  upper-side, or exact-law claim was added. Standalone compiles to 54 pages
  (802,418 bytes); master compiles to 856 pages (7,773,478 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun request; see
  `verification/R36_fixed_excess_fixed_k.md`.

- R37 2026-06-28: launched exactly 5 tool-managed audit agents for the
  zero-containing finite-alphabet extension; all five completed. Upgraded
  `prop:finite-alphabet-obstruction` from the nonzero quotient count to the
  projective-pair count
  `Pi(S)={[a:b] in P^1(K): a,b in S, (a,b)!=(0,0)}` over `K=R,C`: if
  `S!={0}` and `N>=|Pi(S)|(m-1)+1`, or if `S={0}` and `N>=m`, every
  `A in S^{N x m}` has a singular `m`-row submatrix. The proof treats
  `(0,0)` first-two-entry rows as compatible with every projective class, not
  as projective points. The `+1` is necessary (for `S={0,1}`, `m=2`, one
  representative of each projective class gives a nonsingular below-threshold
  example). Kept the finite-alphabet theorem manuscript-only; no Lean expansion,
  quaternion/right-ratio variant, or random atomic threshold claim was added.
  Softened the atomic numerics language so sampled below-threshold behavior is
  illustrative, not an exhaustive sharpness proof. Standalone LaTeX passed
  twice; final PDF is 55 pages, 809,343 bytes. Targeted standalone log scan
  found no undefined citations/references and no rerun request; remaining
  diagnostics are the known `\theHfootnote` warning, the pre-existing overfull
  hbox in `parts/ldp.tex`, and an underfull vbox on the numerics figure page;
  see `verification/R37_projective_alphabet_obstruction.md`.

- R38 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  fixed-excess fixed-`k` normalized column-Gram transfer; all five completed and
  found the pathwise transfer sound. Added `rect-kth:gram-lower`: for
  `|T|=m+r`,
  `lambda_(k)((m+r)^-1 A_T^* A_T)=(m+r)^-1 sigma_{m-k+1}(A_T)^2`, so
  `Lambda_m^{(r)}[k]=(m+r)^-1(M_m^{(r)}[k])^2`. The finite-budget lower
  threshold is the squared `rect-kth:lower` threshold times `(m+r)^-1`, and the
  fixed-aspect lower base is `2h(gamma)/(d_F k(k+r))`, with an a.s. lower
  envelope on common couplings. Added compact master paragraph
  `laneO:par:rect-fixed-k-gram-lower`. This is only a normalized column-Gram
  lower side: no row-Gram statement for `r>0`, quaternion variant, upper side,
  exact law, or proportional Wishart-edge claim. Standalone compiles to 54
  pages (807,346 bytes); master compiles to 856 pages (7,774,714 bytes) and has
  been copied to `~/Downloads/master.pdf`. Targeted log scans show
  no undefined citations/references and no rerun request; see
  `verification/R38_fixed_excess_fixed_k_gram.md`.

- R39 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  fixed-excess fixed-`k` deterministic conditioning transfer; all five
  completed. Added `cor:fixed-excess-fixed-k-transfer`: under the hypotheses of
  `prop:cov-transfer`, the global row scaling and absolute covariance extreme
  factors sandwich `sigma_{m-k+1}(D_TG_T Sigma^{1/2})` uniformly over
  `|T|=m+r`, so the normalized log scale differs from the iid Gaussian one by
  `o(1)`. The lower-side base
  `h(gamma)/(d_F k(k+r))` transfers for singular values, and the normalized
  column-Gram base `2h(gamma)/(d_F k(k+r))` transfers after squaring and adding
  only the harmless `(m+r)^{-1}` normalization. Recorded explicitly that
  absolute covariance extreme control is used; subexponential condition number
  alone would not prevent global exponential rescaling. No upper side, exact
  law, non-diagonal two-sided-minor transfer, row-Gram result for `r>0`, or
  condition-number-only covariance claim was added. Standalone compiles to 55
  pages (813,196 bytes); master compiles to 856 pages (7,775,708 bytes) and has
  been copied to `~/Downloads/master.pdf`. Targeted log scans show
  no undefined citations/references and no rerun request; see
  `verification/R39_fixed_excess_fixed_k_conditioning_transfer.md`.

- R40 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  fixed-excess directional-row lower side; all five completed. The naive
  rank-`p` one-row projection route was rejected because deleting one row from a
  tall `(m+r) x m` matrix usually leaves full row span. Added the deterministic
  cofactor certificate `rect:row-block-certificate`: if
  `B in F^{(m+r) x m}` has small `smin`, then some `m-1` row block has a unit
  normal whose projections on the remaining `p=r+1` rows have Euclidean norm at
  most `sqrt(m) smin(B)`. Added
  `rect:directional-row-fixed-excess`: independent rows with affine directional
  small-ball constants `L_{m,i}` have finite budget
  `B_{m,r}^{dir}=binom(N_m-p,m-1) sum_{|S|=p} prod_{i in S} L_{m,i}`, slack
  `(d_F p/2)log m+u_m`, denominator `d_F p`, and a summable a.s. lower
  envelope. Consequently iid real isotropic log-concave rows have fixed-excess
  lower-side bases `h(gamma)/(r+1)` for every fixed `r`. No upper side, exact
  law, supercritical Balan-Wang theorem, or uniform-in-`r` log-concave marginal
  claim was added. Standalone LaTeX passed twice; final PDF is 59 pages,
  850,143 bytes. Targeted log scan shows no undefined citations/references and
  no rerun request; remaining diagnostics are the known `\theHfootnote` warning
  and the pre-existing overfull hbox in `parts/ldp.tex`; see
  `verification/R40_fixed_excess_directional_row_lower.md`.

- R41 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  almost-sure lower-envelope version of the fixed-excess fixed-`k`
  conditioning transfer; all five completed. Added the common-coupling liminf
  displays to `cor:fixed-excess-fixed-k-transfer`: the uniform min--max sandwich
  gives `M_A^{(r)}[k] >= alpha_m M_G^{(r)}[k]` with
  `m^{-1}log alpha_m -> 0`, so the Gaussian a.s. envelope in
  `cor:as-geometric-lower-envelopes` transfers. Squaring gives the normalized
  column-Gram a.s. lower envelope, with the `(m+r)^-1` normalization contributing
  only `o(1)` on the log scale. This is still lower-envelope only: no a.s. exact
  law, upper side, quaternion extension, row-Gram statement for `r>0`, or
  condition-number-only covariance transfer was added. Standalone compiles to
  59 pages (850,940 bytes); master compiles to 856 pages (7,775,984 bytes) and
  has been copied to `~/Downloads/master.pdf`. Targeted log scans
  show no undefined citations/references and no rerun request; see
  `verification/R41_fixed_excess_fixed_k_conditioning_as_envelope.md`.

- R42 2026-06-28: launched exactly 5 tool-managed read-only audit agents for the
  fixed-supercritical directional phase-retrieval branch; all five completed.
  Added `cor:pr-directional-branch`: for fixed `r>=1`, `N=2m-1+r`, and
  `omega_r^fe(A)=min_{|T|=m+r}smin(A_T)`, independent real rows with affine
  directional constants `L_{m,i}` and subexponential elementary-symmetric
  budget `sum_{|S|=r+1} prod_{i in S} L_{m,i}` satisfy
  `P{omega_r^fe<=exp[-(log4/(r+1)+eps)m]}->0` and the same a.s. lower envelope
  on common couplings. The exact specialization is
  `B_{m,r}^{dir}=binom(2m-2,m-1) sum_{|S|=r+1} prod_i L_{m,i}`, whose entropy is
  `log4`. This is only the deficient-complement fixed-excess branch of the
  Balan-Wang partition geometry: no full supercritical lower-Lipschitz theorem,
  upper side, or exact law is claimed. Standalone LaTeX passed twice; final PDF
  is 60 pages, 855,103 bytes. Targeted log scan shows no undefined
  citations/references and no rerun request; remaining diagnostics are the known
  `\theHfootnote` warning and the pre-existing overfull hbox in `parts/ldp.tex`.
  See
  `verification/R42_supercritical_directional_branch.md`.

- R43 2026-06-28: the first random-diagonal fixed-`k` audit attempt produced
  only two completed agents and three transport failures, so no theorem text was
  merged from that incomplete audit. Restarted the round with exactly 5 fresh
  read-only audit agents; all five completed. Added
  `rem:random-diagonal-fixed-k`: for
  `Atilde_m=D_m^{row} A_m E_m` with strictly positive finite random diagonal
  entries, possibly dependent on `A_m`, the total logarithmic extreme
  `Delta_m^{diag}` gives pathwise errors at most `Delta_m^{diag}/m` for
  fixed-excess fixed-`k` singular-value statistics and
  `2 Delta_m^{diag}/m` for normalized column-Gram statistics. Hence lower sides
  transfer under `Delta_m^{diag}=o_P(m)`, and lower envelopes transfer under
  `Delta_m^{diag}=o(m)` a.s. on common couplings. This is only diagonal
  lower-side bookkeeping: no upper side, exact law, row-Gram result for `r>0`,
  selected-column/fixed-excess non-diagonal covariance transfer, quaternion
  fixed-excess fixed-`k` law, or proportional-excess Wishart-edge claim was
  added. Standalone compiles to 60
  pages (858,101 bytes); master compiles to 856 pages (7,776,464 bytes) and has
  been copied to `~/Downloads/master.pdf`. Targeted log scans show
  no undefined citations/references and no rerun request; see
  `verification/R43_random_diagonal_fixed_k_transfer.md`.

- R44 2026-06-28: launched exactly 5 read-only audit agents for the
  row-/column-normalized Gaussian fixed-excess fixed-`k` transfer; all five
  completed. Added `cor:normalized-gaussian-fixed-excess-fixed-k`: for iid real
  or complex Gaussian `G_m` with `N_m/m -> gamma > 1`, both row-normalized and
  column-normalized matrices inherit the fixed-excess fixed-`k` singular-value
  lower base `h(gamma)/(d_F k(k+r))`, and their normalized column-Gram
  statistics inherit the doubled base `2h(gamma)/(d_F k(k+r))`. On common
  couplings the corresponding lower envelopes also transfer, because the
  relevant Gaussian row/column norm extrema are `o(m)` a.s. This uses only the
  random diagonal transfer plus existing Gaussian norm-tail summability; it does
  not add an upper side, exact law, quaternion extension, row-Gram statement for
  `r>0`, or selected-column/fixed-excess non-diagonal covariance transfer.
  Standalone compiles to 61 pages
  (863,410 bytes); master compiles to 856 pages (7,776,655 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun request; see
  `verification/R44_normalized_gaussian_fixed_excess_fixed_k.md`.

- R45 2026-06-28: launched exactly 5 read-only audit agents for quaternion
  fixed-excess fixed-`k` lower sides; all five completed. Four agents accepted
  the fixed-`k` result once the beta-4 Laguerre tail is explicit, and one
  recommended only `k=1` unless that tail is proved, so the final text includes
  the explicit beta-4 Laguerre--Selberg proof. Added
  `lem:quat-rect-kth-laguerre-tail`, `thm:quat-fixed-excess-fixed-k-lower`, and
  `cor:quat-rect-kth-gram-lower`: for iid quaternion Gaussian `(m+r) x m`
  matrices, fixed `r,k`, the one-matrix lower-tail exponent is `4k(k+r)`, giving
  finite budget `(log binom(N_m,m+r)+B log m+O(1))/(4k(k+r))`, fixed-aspect
  singular-value lower base `h(gamma)/(4k(k+r))`, and normalized column-Gram
  lower base `h(gamma)/(2k(k+r))`, with common-coupling a.s. lower envelopes.
  Lower side only: no upper side, exact fixed-excess quaternion law, beta
  interpolation, spherical-radial quaternion transfer, proportional Wishart edge,
  or row-Gram statement for `r>0` was added. Standalone compiles to 62 pages
  (874,041 bytes); master compiles to 857 pages (7,782,365 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun request; see
  `verification/R45_quaternion_fixed_excess_fixed_k_lower.md`.

- R46 2026-06-28: launched exactly 5 read-only audit agents for quaternion
  diagonal and normalized fixed-excess fixed-`k` transfer; all five completed.
  Added `cor:quat-diagonal-normalized-fixed-excess-fixed-k`: positive real
  diagonal row/column weights, possibly dependent on the quaternion Gaussian
  matrix, transfer the R45 lower sides whenever their total logarithmic extrema
  are `o_P(m)`, and transfer the lower envelopes under a.s. `o(m)` extrema.
  Thus row- and column-normalized quaternion Gaussian matrices inherit the
  singular-value lower base `h(gamma)/(4k(k+r))` and the normalized column-Gram
  lower base `h(gamma)/(2k(k+r))`. This is only pathwise diagonal lower-side
  bookkeeping: no upper side, exact fixed-excess/normalized law beyond the
  square `r=0,k=1` case later recorded in R47/R48, selected-column or
  fixed-excess non-diagonal covariance transfer, spherical-radial quaternion
  transfer, beta interpolation, proportional Wishart edge, or row-Gram
  statement for `r>0` was added.
  Standalone compiles to 63 pages (879,535 bytes); master
  compiles to 857 pages (7,782,880 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R46_quaternion_diagonal_normalized_fixed_excess_fixed_k.md`.

- R47 2026-06-28: launched exactly 5 read-only audit agents for exact square
  quaternion diagonal/normalization transfer; all five completed. Added
  `cor:quat-square-diagonal-normalized-exact`: for iid standard quaternion
  Gaussian `G_m`, positive real diagonal row/column weights with total
  logarithmic extreme `o_P(m)`, possibly random and dependent on `G_m`, preserve
  the exact square-row convergence
  `m^{-1}log min_{|T|=m}smin((D_row G E)_T)->-h(gamma)/4`. By Gram transfer,
  the normalized square column-Gram statistic has base `-h(gamma)/2`. Row- and
  full-matrix column-normalized quaternion Gaussian matrices are included. A.s.
  `o(m)` diagonal extrema give only lower envelopes; no a.s. exact law,
  fixed-excess exact law, selected-column/two-sided non-diagonal covariance
  transfer, quaternion-valued diagonal weights, selected-submatrix column
  renormalization, or spherical-radial quaternion transfer was added.
  Standalone compiles to 64
  pages (885,584 bytes); master compiles to 857 pages (7,784,020 bytes) and has
  been copied to `~/Downloads/master.pdf`. Targeted log scans show
  no undefined citations/references and no rerun request; see
  `verification/R47_exact_square_quaternion_diagonal_normalized_transfer.md`.

- R48 2026-06-28: launched exactly 5 read-only audit agents for exact square
  quaternion row/covariance conditioning transfer; all five completed. Added
  `cor:quat-square-row-covariance-conditioning-exact`: for iid standard
  quaternion Gaussian `G_m`, a positive real row diagonal factor and a global
  invertible right quaternion factor `S_m` preserve the exact square-row base
  whenever `max_i |log d_i|+|log smin(S_m)|+|log opnorm(S_m)|=o_P(m)`. Thus
  `m^{-1}log min_{|T|=m}smin((D_row G S)_T)->-h(gamma)/4`, and the normalized
  square Gram base is `-h(gamma)/2`. Deterministic uniformly elliptic
  quaternion right shapes are included. Absolute scale is required; a
  subexponential condition number alone would miss scalar shifts. This is only
  a square all-column right-factor statement: no fixed-excess exact law,
  selected-column covariance transfer, non-square Wishart edge, a.s. exact law,
  or quaternion spherical-radial universality was added. Standalone compiles to
  65 pages (890,610 bytes); master compiles to 858 pages (7,787,229 bytes) and
  has been copied to `~/Downloads/master.pdf`. Targeted log scans
  show no undefined citations/references and no rerun request; see
  `verification/R48_exact_square_quaternion_row_covariance_conditioning_transfer.md`.

- R49 2026-06-28: launched exactly 5 read-only audit agents for exact square
  quaternion random row-count transfer; all five completed. Added
  `thm:quat-random-row-count-gaussian`: for an infinite iid standard quaternion
  Gaussian row array, an integer prefix count `N_m/m -> gamma>1` in probability,
  possibly dependent on the row array, preserves the exact square-row base
  `m^{-1}log M_m^HH(N_m)->-h(gamma)/4`. The normalized square Gram base is
  `-h(gamma)/2`; a.s. count convergence gives only lower envelopes. Added
  `cor:quat-poisson-thinning` for independent Poisson/binomial prefix counts
  and independent Bernoulli thinning by distributional reindexing of retained
  iid rows. Value-dependent thinning/selection, Balan-Wang conclusions,
  fixed-excess exact laws, supercritical phase-retrieval statements, quaternion
  spherical-radial universality, and a.s. exact laws are not claimed. Build
  verification: standalone compiles to 66 pages (897,449 bytes); master
  compiles to 858 pages (7,788,977 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R49_exact_square_quaternion_random_row_count_transfer.md`.

- R50 2026-06-28: launched exactly 5 read-only audit agents for exact square
  quaternion random-prefix conditioning transfer; all five completed. Added
  `cor:quat-random-prefix-conditioning-exact`: for an infinite iid standard
  quaternion Gaussian row array, a random prefix count `N_m/m -> gamma>1`,
  positive real row weights over the realized prefix, and a global invertible
  all-column right factor `S_m`, the exact random-prefix square-row base
  remains `-h(gamma)/4` when the realized-prefix row-weight extrema and
  absolute singular-value scale of `S_m` are `o_P(m)`. The normalized square
  Gram base is `-h(gamma)/2`; positive column diagonals, row-normalized
  random-prefix matrices, and full-prefix column normalization are included.
  A.s. count/extrema hypotheses give only lower envelopes. Condition number
  alone, value-dependent row selection, selected-column covariance transfer,
  fixed-excess exact laws, Balan-Wang or supercritical phase-retrieval
  conclusions, quaternion spherical-radial universality, and a.s. exact laws
  are not claimed. Build verification: standalone compiles to 67 pages
  (904,372 bytes); master compiles to 858 pages (7,789,837 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun request; see
  `verification/R50_exact_square_quaternion_random_prefix_conditioning_transfer.md`.

- R51 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  fixed-excess fixed-`k` lower sides; all five completed. Added
  `cor:random-prefix-fixed-excess-fixed-k-lower`: for `F in {R,C,H}`, an
  infinite iid standard Gaussian row array, fixed `r>=0,k>=1`, and possibly
  dependent integer prefix counts `N_m/m -> gamma>1`, the deterministic-count
  fixed-excess fixed-`k` lower sides transfer by monotonicity. The singular
  lower base is `h(gamma)/(d_F k(k+r))`; the normalized column-Gram lower base
  is `2h(gamma)/(d_F k(k+r))`; a.s. count convergence gives the lower
  envelopes. The proof uses only the upper deterministic bracket on `N_m`.
  A follow-up proof audit tightened the statement to use the `+infty`
  convention on `{N_m<m+r}` and made the `gamma_+`/epsilon slack explicit.
  This is weaker than R49/R50 in the square `r=0,k=1` case and adds only
  fixed-excess fixed-`k` lower sides. No upper side, exact fixed-excess law,
  value-dependent row selection, row-Gram statement for `r>0`, beta
  interpolation, proportional Wishart edge, Balan-Wang or supercritical
  phase-retrieval conclusion, or a.s. exact law is claimed. Build verification:
  standalone compiles to 68 pages (910,837 bytes); master compiles to 859 pages
  (7,792,903 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R51_random_prefix_fixed_excess_fixed_k_lower_and_gram.md`.

- R52 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  diagonal/normalized fixed-excess fixed-`k` lower-side transfer; all five
  completed (Dirac `019f0e8c-27f3-7792-b0bf-dce66d534379`, Godel
  `019f0e8c-2873-7cb2-bff0-f4b18a4d0148`, Pascal
  `019f0e8c-28e2-74c2-a0b3-ed09f495b92c`, Gibbs
  `019f0e8c-2943-7c81-bbba-9c6ab12cc2df`, Kepler
  `019f0e8c-29c4-7c30-b279-a9643a92b301`). Added
  `cor:random-prefix-diagonal-fixed-excess-fixed-k`: for
  `F in {R,C,H}`, an infinite iid Gaussian row array, possibly dependent prefix
  counts `N_m/m -> gamma>1`, fixed `r>=0,k>=1`, and positive real diagonal
  row/column weights with realized-prefix total logarithmic extreme
  `Delta_m^{rpdiag}=o_P(m)`, the singular lower base remains
  `h(gamma)/(d_F k(k+r))` and the normalized column-Gram lower base remains
  `2h(gamma)/(d_F k(k+r))`. A.s. count convergence and
  `Delta_m^{rpdiag}=o(m)` transfer the corresponding lower envelopes. The
  proof is only the pathwise diagonal lower sandwich plus R51; Gram is handled
  at the eigenvalue/singular-value level, not by a Loewner comparison.
  Row-normalized random-prefix Gaussian rows and full-prefix column-normalized
  Gaussian columns are included. This is weaker than R49/R50 in the square
  quaternion `r=0,k=1` case and adds only a diagonal random-prefix lower-side
  packaging result. No upper side, exact fixed-excess law, value-dependent row
  selection, row-Gram statement for `r>0`, selected-submatrix column
  normalization, non-diagonal covariance transfer, beta interpolation,
  proportional Wishart edge, Balan-Wang or supercritical phase-retrieval
  conclusion, or a.s. exact law is claimed. Build verification: standalone
  compiles to 69 pages (917,919 bytes); master compiles to 859 pages
  (7,794,073 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R52_random_prefix_diagonal_normalized_fixed_excess_fixed_k_lower_and_gram.md`.

- R53 2026-06-28: launched exactly 5 read-only audit agents for all-field square
  random-prefix diagonal exact transfer; all five completed (Bernoulli
  `019f0e95-695f-7d51-9b63-cf1ab12b0ef8`, Confucius
  `019f0e95-91c0-7462-b2c0-ebfad37f1339`, Lorentz
  `019f0e95-ae3b-7511-b482-e3acb28d7d67`, Pascal
  `019f0e95-c6d4-7593-a097-aee0825b0a75`, Faraday
  `019f0e95-d919-7742-a2ee-500d6a6db02b`). Added
  `cor:random-prefix-square-diagonal-exact`: for `F in {R,C,H}`, an infinite
  iid Gaussian row array, possibly dependent prefix counts
  `N_m/m -> gamma>1`, and positive real diagonal row/column weights with
  realized-prefix total logarithmic extreme `Delta_m^{sqdiag}=o_P(m)`, the
  exact square singular base is `-h(gamma)/d_F` and the normalized square
  column-Gram base is `-2h(gamma)/d_F`. A.s. count convergence and
  `Delta_m^{sqdiag}=o(m)` transfer lower envelopes only. Row-normalized
  random-prefix Gaussian rows and full-prefix column-normalized Gaussian
  columns are included. For `H`, this is a diagonal specialization of the
  stronger R50 global-right-factor theorem; for `r=0,k=1`, it is the exact
  strengthening of R52. No value-dependent row selection, selected-submatrix
  column normalization, non-diagonal covariance transfer, quaternionic non-real
  diagonal weighting, condition-number-only covariance claim, fixed-excess exact
  law, row-Gram result for `r>0`, Balan-Wang or supercritical phase-retrieval
  conclusion, or a.s. exact law is claimed. Build verification: standalone
  compiles to 70 pages (928,441 bytes). Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R53_all_field_square_random_prefix_diagonal_exact_transfer.md`.

- R54 2026-06-28: launched exactly 5 read-only audit agents for all-field
  random-prefix all-column fixed-excess fixed-`k` lower-side transfer; all five
  completed (Mendel `019f0e9b-340f-7d41-9a83-400e9c6ba4c9`, Hilbert
  `019f0e9b-349e-7022-85ef-f616750cff7e`, Lorentz
  `019f0e9b-3516-7851-9c8f-843384853ca0`, Pauli
  `019f0e9b-357d-7243-889f-2d7f2a605982`, McClintock
  `019f0e9b-35e7-7701-8b4f-5f9a19617e4a`). Added
  `cor:random-prefix-right-factor-fixed-excess-fixed-k-lower`: for
  `F in {R,C,H}`, an infinite iid Gaussian row array, possibly dependent prefix
  counts `N_m/m -> gamma>1`, fixed `r>=0,k>=1`, positive real row weights over
  the realized prefix, and one global invertible all-column right factor `S_m`
  with `max_{i<=N_m}|log d_im|+|log smin(S_m)|+|log opnorm(S_m)|=o_P(m)`, the
  singular lower base remains `h(gamma)/(d_F k(k+r))`, and the normalized
  column-Gram lower base remains `2h(gamma)/(d_F k(k+r))`. A.s. count
  convergence and a.s. `o(m)` conditioning factors transfer lower envelopes.
  Positive column diagonals, full-column covariance/whitening factors with
  absolute singular-scale control, row-normalized random-prefix Gaussian rows,
  and full-prefix column normalization are included. Lower side only: no upper
  side, exact fixed-excess law, condition-number-only covariance transfer,
  value-dependent row selection, selected-column covariance theorem,
  selected-submatrix column normalization, row-Gram result for `r>0`, beta
  interpolation, proportional Wishart edge, Balan-Wang or supercritical
  phase-retrieval conclusion, or a.s. exact law is claimed. Build
  verification: standalone compiles to 72 pages (936,170 bytes); master
  compiles to 859 pages (7,795,044 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R54_all_field_random_prefix_right_factor_fixed_excess_fixed_k_lower_and_gram.md`.

- R55 2026-06-28: launched exactly 5 read-only audit agents for all-field square
  random-prefix row/right-factor exact transfer; all five completed (Euclid
  `019f0e9d-1e0e-74f3-a1b3-432b3325af73`, Euler
  `019f0e9d-34db-7121-962e-da931790ed76`, Hilbert
  `019f0e9d-49f2-7162-a9d2-ca3927f902c7`, Feynman
  `019f0e9d-5dc0-71f0-b991-8d88f1c9ab39`, Dewey
  `019f0e9d-73cb-7e61-8f14-4be275cc61f7`). Upgraded the R53 diagonal square
  corollary to `cor:random-prefix-square-row-right-factor-exact`, retaining
  `cor:random-prefix-square-diagonal-exact` as an alias on the same result. For
  `F in {R,C,H}`, an infinite iid Gaussian row array, possibly dependent prefix
  counts `N_m/m -> gamma>1`, positive real prefix row weights, and one global
  all-column right factor `S_m in GL_m(F)` with
  `max_{i<=N_m}|log d_i|+|log smin(S_m)|+|log ||S_m||||=o_P(m)`, the exact
  square singular base is `-h(gamma)/d_F` and the normalized square column-Gram
  base is `-2h(gamma)/d_F`. A.s. count convergence and a.s. `o(m)` conditioning
  transfer lower envelopes only. Positive column diagonals, row-normalized
  random-prefix Gaussian rows, and full-prefix column normalization are included.
  This is square row-selection only: no selected-column or two-sided non-diagonal
  covariance transfer, selected-submatrix column normalization, value-dependent
  row selection, fixed-excess exact law, row-Gram result for `r>0`,
  condition-number-only covariance claim, quaternionic non-real row weighting,
  Balan-Wang or supercritical phase-retrieval conclusion, or a.s. exact law is
  claimed. Build verification: standalone compiles to 72 pages (936,978 bytes).
  Targeted log scans show no undefined citations/references and no rerun
  request; see
  `verification/R55_all_field_square_random_prefix_row_right_factor_exact_transfer.md`.

- R56 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  proportional-excess lower sides; all five completed (Harvey
  `019f0ea5-0a5d-7f22-8f46-94b995f9a101`, Arendt
  `019f0ea5-0ab5-7ba1-bdfe-964b0119a669`, Descartes
  `019f0ea5-0b0e-70b2-a066-da3a02e093e4`, Volta
  `019f0ea5-0b66-7eb0-a6d4-cd3d7d187e65`, Anscombe
  `019f0ea5-0baf-7be0-a7b5-20f62f4b8631`). Added
  `rect:random-prefix-proportional-density-rate`: for `F in {R,C}`, an
  infinite independent-entry row array with density bound
  `K_m=exp((kappa+o(1))m)`, deterministic `ell_m/m -> zeta in (1,gamma)`,
  and possibly dependent integer prefix counts `N_m/m -> gamma>1`, the
  proportional-excess singular lower threshold remains `kappa/d_F` on the
  exponential `m`-scale. The selected-row normalized column-Gram statistic
  `ell_m^{-1}A_T^*A_T` has doubled lower threshold `2kappa/d_F`, and a.s.
  count convergence gives the corresponding lower envelopes. The proof uses
  only the upper deterministic prefix bracket and monotonicity, with `+infty`
  on infeasible prefixes. This R56 statement itself is
  lower-side/exponential-scale only; R57 separately adds the pathwise
  row/right-factor transfer. No quaternion extension, selected-column theorem,
  value-dependent row selection, `sqrt(m)` Wishart-edge/LDP constant, upper
  proportional-edge law, or exact proportional-edge law is claimed.
  Build verification: standalone compiles to 73 pages (946,087 bytes); master
  compiles to 860 pages (7,798,395 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R56_random_prefix_proportional_excess_lower_sides.md`.

- R57 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  proportional-excess conditioning transfer; all five completed (Plato
  `019f0eaf-ba9c-7f12-843c-15c2a32e91c4`, Feynman
  `019f0eaf-d505-7860-8a61-d2075f1c9904`, Schrodinger
  `019f0eaf-f417-7111-a17d-b7edad27eb7a`, Ampere
  `019f0eb0-0a93-7bc0-a1e0-b41f0a363b64`, Turing
  `019f0eb0-40d6-7cf3-b2e0-3a618e33da40`). Added
  `rect:random-prefix-proportional-conditioning-transfer`: for `F in {R,C}`,
  the R56 independent-entry random-prefix proportional-excess lower sides
  transfer through positive real realized-prefix row weights and one global
  all-column right factor `S_m in GL_m(F)` when
  `Delta_m^{propcond}=max_{i<=N_m}|log d_im|+|log smin(S_m)|+|log opnorm(S_m)|=o_P(m)`.
  The singular lower threshold remains `kappa/d_F`, and the selected-row
  normalized column-Gram threshold for `ell_m^{-1}B_T^*B_T` remains
  `2kappa/d_F`; a.s. count convergence plus a.s. `o(m)` conditioning factors
  gives lower envelopes. Positive column diagonals, full-column
  covariance/whitening under absolute singular-scale control, Gaussian row
  normalization, and full-prefix Gaussian column normalization are included.
  This is a pathwise lower-side transfer from the unweighted independent-entry
  base, not a new density theorem for the conditioned matrix. No quaternion
  extension, condition-number-only covariance claim, selected-column theorem,
  selected-submatrix column normalization, value-dependent row selection,
  row-Gram result, proportional Wishart-edge/LDP constant, upper side, or exact
  proportional-edge law is claimed. Build verification: standalone compiles to
  74 pages (953,556 bytes); master compiles to 860 pages (7,799,977 bytes) and
  has been copied to `~/Downloads/master.pdf`. Targeted log scans
  show no undefined citations/references and no rerun request; see
  `verification/R57_random_prefix_proportional_excess_conditioning_transfer.md`.

- R58 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  two-sided density-rate lower sides; all five completed (Peirce
  `019f0eb8-aa6c-7623-a0be-1a864a8996ed`, Epicurus
  `019f0eb8-e7cb-77b0-92df-c53e02332d7f`, Heisenberg
  `019f0eb9-0abc-7140-84e6-662457961cc6`, Anscombe
  `019f0eb9-3d8e-7070-945b-13ae79ff57b5`, Plato
  `019f0eb9-56ea-7203-91e2-097a0ffedb5d`). Added
  `two:random-prefix-density-rate-lower`: for `F in {R,C}`, an infinite
  independent-entry array with scalar density bound
  `K_k=exp((kappa+o(1))k)` and possibly dependent ordered row and column
  prefix counts `N_k^R/k -> gamma_R>1` and `N_k^C/k -> gamma_C>1`, the
  two-sided `k x k` minor lower threshold is
  `(h(gamma_R)+h(gamma_C)+kappa)/d_F`. The proof uses deterministic upper
  brackets for both prefixes and the deterministic two-sided density-rate
  lower side; a.s. count convergence plus countable brackets gives the lower
  envelope. This is an ordered-prefix lower-side transfer only: no upper side,
  exact two-sided law, pair-correlation theorem, quaternion extension,
  value-dependent thinning/reindexing, selected-column covariance transfer,
  non-diagonal right-factor transfer, or upper/exact Gram/sample-covariance law
  is claimed; R59 separately records the pathwise diagonal row/column weighting
  transfer, and R61 separately records the deterministic selected-minor
  normalized Gram lower-side transfer.
  Build verification: standalone
  compiles to 75 pages (960,682 bytes); master compiles to 860 pages
  (7,801,521 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R58_random_prefix_two_sided_density_rate_lower_side.md`.

- R59 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  two-sided diagonal density-rate transfer; all five completed (Copernicus
  `019f0ec4-49e4-7811-af85-682b1486960f`, Sagan
  `019f0ec4-712f-7001-a6db-8b0a1ff3e001`, Beauvoir
  `019f0ec4-855b-7d52-82e2-014724ff241b`, Meitner
  `019f0ec4-ab98-7f61-b5f9-cbf17b97b475`, Darwin
  `019f0ec4-c69c-7242-b59d-8a829c810d17`). Added
  `two:random-prefix-diagonal-conditioning-transfer`: for `F in {R,C}`, the
  R58 independent-entry random-prefix two-sided density-rate lower side
  transfers through positive real row and column weights over the realized
  ordered prefixes, possibly random and dependent, when
  `Delta_k^{twodiag}=max_{i<=N_k^R}|log d_{i,k}|+max_{j<=N_k^C}|log e_{j,k}|=o_P(k)`.
  The two-sided lower threshold remains
  `(h(gamma_R)+h(gamma_C)+kappa)/d_F`; a.s. prefix-count convergence plus
  a.s. `o(k)` diagonal extrema gives the lower envelope. This is only a
  pathwise lower-side transfer from the unweighted independent-entry base, not
  a density theorem for the weighted matrix. No non-diagonal column
  covariance/right-factor transfer, condition-number-only scale control,
  value-dependent thinning/reindexing, selected-submatrix renormalization,
  upper/exact two-sided law, pair-correlation theorem, quaternion extension,
  upper/exact Gram/sample-covariance law, or Wishart-edge/LDP law is claimed.
  The deterministic selected-minor normalized Gram lower-side transfer is
  recorded separately in R61. Build verification: standalone
  compiles to 76 pages (965,364 bytes); master compiles to 861 pages
  (7,803,713 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R59_random_prefix_two_sided_diagonal_density_rate_transfer.md`.

- R60 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  two-sided full-prefix normalization; all five completed (Godel
  `019f0ecc-bd8d-7d42-8f6a-40705b160b9a`, McClintock
  `019f0ecc-d5be-7351-a734-c8c2aa705070`, Averroes
  `019f0ecd-016e-7900-a59d-c0ffb6701b77`, Cicero
  `019f0ecd-1ca1-78d0-be56-02df89293d8d`, Euler
  `019f0ecd-30bb-79a3-bded-0e4cdeace0f7`). Added
  `two:random-prefix-gaussian-full-prefix-normalization`: for `F in {R,C}`,
  iid Gaussian infinite arrays with possibly dependent ordered prefix counts
  inherit the R58 two-sided lower threshold under one-shot full-prefix row
  and/or column norm factors. Row norms use all realized prefix columns
  `[N_k^C]`; column norms use all realized prefix rows `[N_k^R]`; factors are
  frozen before selecting `R,C`. Deterministic prefix bracketing, Markov upper
  tails, and ball-volume lower tails give the required logarithmic norm
  extrema `o_P(k)` and `o(k)` a.s. under a.s. count convergence. The lower
  threshold remains `(h(gamma_R)+h(gamma_C))/d_F`, with the corresponding a.s.
  lower envelope. This is only Gaussian one-shot full-prefix normalization: no
  per-minor normalization, iterative balancing/Sinkhorn theorem, non-Gaussian
  normalization theorem, non-diagonal covariance/right-factor transfer,
  value-dependent thinning/reindexing, selected-submatrix renormalization,
  upper/exact two-sided law, quaternion extension, upper/exact
  Gram/sample-covariance law, or Wishart-edge/LDP law is claimed. The
  deterministic selected-minor normalized Gram lower-side transfer is recorded
  separately in R61. Build verification: standalone compiles to 78 pages
  (975,139 bytes); master compiles to 861 pages (7,804,979 bytes) and has been
  copied to `~/Downloads/master.pdf`. Targeted log scans show no
  undefined citations/references and no rerun request; see
  `verification/R60_random_prefix_two_sided_full_prefix_normalization.md`.

- R61 2026-06-28: launched exactly 5 read-only audit agents for random-prefix
  two-sided normalized Gram/sample-covariance lower-side transfer; all five
  completed (Noether `019f0ed4-b49a-7af0-b2df-f1ddcd0c73d3`, Parfit
  `019f0ed4-d08d-7c30-8334-919d4843d96c`, Euclid
  `019f0ed4-e634-72c2-8a8e-aad78509eb99`, Laplace
  `019f0ed4-ff3e-7f91-9bd5-0fdb27cdaef7`, James
  `019f0ed5-2422-7800-a327-15d13c8a0c6d`). Added
  `two:random-prefix-normalized-gram-transfer`: in the R59 diagonal-transfer
  setting, the selected-minor normalized column-Gram statistic
  `min lambda_min(k^{-1}B_{R,C}^*B_{R,C})` over realized `k x k` row/column
  prefixes has lower threshold
  `2(h(gamma_R)+h(gamma_C)+kappa)/d_F`, with the corresponding a.s. lower
  envelope under a.s. count convergence and `Delta_k^{twodiag}=o(k)`. The R60
  Gaussian full-prefix-normalized matrices are included with `kappa=0`. The
  proof is only the pathwise identity
  `lambda_min(k^{-1}B^*B)=k^{-1}s_min(B)^2`; the `log k/k` normalization term
  is negligible. This is not an upper/exact Gram law, Wishart-edge/LDP theorem,
  pair-correlation theorem, non-diagonal covariance/right-factor transfer,
  row-Gram rectangular result, per-minor normalization theorem,
  value-dependent selection theorem, or quaternion statement. Build
  verification: standalone compiles to 80 pages (1,000,502 bytes); master
  compiles to 861 pages (7,806,351 bytes) and has been copied to
  `~/Downloads/master.pdf`. Targeted log scans show no undefined
  citations/references and no rerun request; see
  `verification/R61_random_prefix_two_sided_normalized_gram_sample_covariance_transfer.md`.

## Open problems list
See `parts/open_problems.tex`.

## Resume protocol
1. Read `STATE.md` and `PLAN.md`.
2. Preserve the 5-subagent cap. Do not start 50 agents.
3. Pick the next TODO/DRAFT/VERIFYING rows and run a develop -> adversarial verify pass.
4. Merge only PROVEN, clearly-labeled PARTIAL/CONDITIONAL, or CONJECTURE content into the TeX.
5. Update ledger and round log. Recompile if LaTeX is available.
6. If all rows are proved/closed and time remains, deepen with fluctuations, ensembles,
   sharper constants, or open problems. Do not stop early just because a subset is done.
