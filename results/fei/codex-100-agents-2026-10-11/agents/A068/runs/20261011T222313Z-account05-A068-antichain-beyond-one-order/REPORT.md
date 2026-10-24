# A068 / B14: context-dependent antichains with quadratic spectral fibers

## exact target, quantifiers, hypotheses and units

Let h:{-1,1}^q -> {-1,1} be regular in the published sense: after fixed coordinate orientations it is monotone and has a total desirability order. Let z consist of m independent uniform bits, write z_j=(-1)^{u_j}, and let Q_1,...,Q_q be arbitrary polynomials of degree at most two over F_2 in u. They may share every control variable. Put a_i(z)=(-1)^{Q_i(u)} and

    F(x,z)=h(x_1 a_1(z),...,x_q a_q(z)).

The x_i are distinct private physical data coordinates, independent of z. For every finite q,m, with no bound on the number, degree of overlap, or rank of the quadratic controls,

    H(F) <= C_reg I_x(F)+2 I_z(F) <= C_reg I(F),
    C_reg=log_2(4+e)+2log_2(e*pi)<8.937.

Here I_x=sum_i Inf_{x_i}, I_z=sum_j Inf_{z_j}; entropy is in bits. The sharper consequence H(F)<=C_reg D_x(F)+2I_z(F), where D_x=sum_i min(Inf_{x_i},1-Inf_{x_i}), follows from the recovered centered regular theorem. The ordinary inequality above is reconstructed with a complete normalized reference below. This is a proper-class result, not full FEI. Its local proof and exact validation are complete; independent acceptance is pending. Novelty outside the read corpus is unverified.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (fei-execution-protocol/2, revision 2026-10-11-execution-v2), README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json, STREAM_NEXT_ACTIONS.json, and the B14/A068 portions of FEI_100_agent_research_plan.tex. Read the three earlier run REPORT.md files under B05, B09, and B19. BOARD.md snapshot 2026-10-11 22:16 UTC was read at stage start. B14 STREAM_NOTES.md did not exist at its prescribed location; no lead direction was inferred.

Read supplemental CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md, plus source excerpts ERASURE_REDUCTION.md, OVERLAPPING_PRODUCT_NOTE.md and ROUTE_MAP_CURATED.md. The last source's Section 2.1 already supplies signed physical-translation symmetry removal at zero entropy decrement. Accordingly the linear-control special case is a recovered-mechanism application, not a new mechanism claimed here. The nonlinear quadratic extension has a positive conditional entropy term which that reduction does not eliminate.

Mathematical dependencies are the current threshold source, SHA256 5d87f625fbadad4aa9841416712b8193a869fa9dffcb4e9c200d2f39a62e6a10, baseline/current-threshold-paper.tex: lem:pivotal-antichain, lem:antichain-density, lem:antichain-noise, lem:ranktail (mean 1+ln 2), lem:levelentropy, eq:euler-reference, eq:euler-cost, thm:A, and the ordinary combination coefficient eq:multiI. These passages were read directly. The 38-page and earlier threshold TXT introductions and rank/width locators were compared; both percolation TXT introductions/encoding locators were consulted, without importing their arm estimates or claiming their proofs were reconstructed. Exact hashes and read scope are saved in out/SOURCES.json. Non-UTF8 paper text was decoded with replacement/CP1252 as needed. No web or novelty search was performed.

## complete derivation or exact first unsupported line

### 1. The replacement pivotal geometry

Fix z and write y_i=x_i a_i(z), also incorporating any fixed orientations of h. The map x -> y is a coordinate orientation, preserving uniform measure. For data pivot x_i,

    d_{x_i} F(x_{-i},z)=a_i(z) d_i h(y_{-i}).

In the coordinates preceding i in h's desirability order, every fixed-z pivotal fiber is therefore an antichain in the orientation a_j(z). The orientation is allowed to depend on the exterior control assignment, but not on the resampled predecessor coordinates. For every resampling mask R, its restricted fiber is still an antichain. Thus the signed relative-noise estimate remains valid after averaging z. This is the precise sufficient condition replacing one globally fixed orientation. It does not imply that F is globally unate.

For rank i, U_i={1,...,i-1} after reordering, the normalized derivative spectrum of F satisfies

    E (1-t)^{|T intersect U_i|} <= E c_B,
    c_b=2^{-b} binom(b,floor(b/2)), B~Bin(i-1,t).

Indeed bound d(X)d(Y) by |d(X)||d(Y)| and, conditionally on X,z,R, bound the latter support probability by c_|R|. Since R is independent of X,z, the derivative mass factors out. Signs of derivatives are harmless. The Fourier partial-noise identity diagonalizes resampling exactly as in the baseline. The same harmonic integral then gives

    E ln[i/(|T intersect U_i|+1)] <= sum_{b=1}^{i-1} c_b/b <= 1+ln 2.

For completeness, E h_kappa = integral_0^1 [1-E(1-t)^kappa] dt/t is at least sum_{b=1}^{i-1}(1-c_b)/b. Also ln[i/(kappa+1)] <= h_{i-1}-h_kappa. Finally c_{2j-1}=c_{2j}=4^{-j}binom(2j,j), and the binomial series yields sum_{j>=1} c_{2j}/(2j-1)=1 and sum_{j>=1} c_{2j}/(2j)=ln 2. This is the recovered sharp rank mean, now applied to conditional orientations.

### 2. Exact data-indexed packets; no incoherent replacement

For S subset [q], let a_S=product_{i in S} a_i, Q_S=sum_{i in S} Q_i over F_2. Expanding h gives the exact identity

    F(x,z)=sum_S hhat(S) chi_S(x) a_S(z),
    Fhat(S,T)=hhat(S) ahat_S(T).

Distinct S have disjoint full Fourier indices because their physical data labels differ. Hence there is no coherent sum to discard. Define p_S=hhat(S)^2 and nu_S(T)=ahat_S(T)^2. Parseval gives sum_T nu_S(T)=1 even when hhat(S)=0. Then

    P_F(S,T)=p_S nu_S(T),
    H(F)=H(h)+sum_S p_S H(a_S),
    I_x(F)=I(h),
    I_z(F)=sum_S p_S I(a_S).

These identities require distinct private data bits. They are valid for arbitrary Boolean controls; the next step uses degree at most two.

### 3. Quadratic control packets are affine flats with a paid rank

Let a(u)=(-1)^{Q(u)} for a polynomial Q of degree at most two on F_2^m. Let B be its alternating polar matrix, so

    Q(u+v)+Q(u)+Q(v)+Q(0)=u^T B v,
    r=rank_F2(B), R=ker(B).

The spectral characteristic function is its physical autocorrelation:

    sum_T ahat(T)^2 (-1)^{T dot v}
       = E_u a(u)a(u+v)
       = 1_{v in R} (-1)^{Q(v)+Q(0)}.

On R, Q(v)+Q(0) is linear because its polarization vanishes. Choose t_0 extending this functional. Walsh inversion gives

    nu(T)=2^{-r} 1_{T in t_0+R_perp}.

Thus nu is uniform on an affine space of dimension r, and H(a)=r. Let J be the coordinate support of the linear space R_perp. Every coordinate in J is uniform on the affine space; the remaining coordinates are fixed. Since dim(R_perp)=r, |J|>=r. Therefore

    I(a)=E_nu |T| >= |J|/2 >= r/2,
    H(a)=r <= 2 I(a).

This includes r=0, affine-linear controls and constant controls: their spectra are single atoms and their entropy is zero. We do not treat a non-Boolean normalized vector as a quadratic phase. The displayed Boolean autocorrelation proves the affine-flat assertion.

For each data set S, write L_S=t_S+ker(B_S)_perp and r_S=rank B_S. The product a_S remains a quadratic phase, so its full entropy bill r_S is paid by twice its physical control influence. The geometry is a family of context-oriented pivotal cubes over the control cube, with affine spectral fibers of possibly different dimensions over data sets.

### 4. Complete normalized rank reference and all its costs

Ranks are relabeled i=1,...,q. On data sets of size k define

    E_k(S)=product_{i in S} i^{-2},
    Z_k=sum_{|S|=k} E_k(S),
    R_k(S)=E_k(S)/Z_k.

Z_k is finite and strictly positive for 0<=k<=q, including Z_0=1. Euler's product from the baseline bounds Z_k<=pi^{2k}/(2k+1)!. Thus, if S={i_1<...<i_k},

    -log_2 R_k(S)
      <= (2/ln 2) sum_{j=1}^k ln(i_j/j)+k log_2(pi^2/4).

The factorial comparison (2k+1)!>=4^k(k!)^2 follows by induction. Define the full conditional reference

    R_k^F(S,T)=R_k(S) 2^{-r_S} 1_{T in L_S}, |S|=k.

For each S, L_S has exactly 2^{r_S} points. Therefore sum_{S,T} R_k^F(S,T)=1. It covers all positive Fourier atoms. Let w_k=P_h(|S|=k) and R^F(S,T)=w_|S| R_|S|^F(S,T). This too is a normalized probability law. Zero w_k levels carry zero actual mass and contribute zero.

The full reference cost is

    log_2(1/w_k) -log_2 R_k(S) + r_S.

In particular, the control geometry is not discarded: its conditional affine rank is charged once per complete Fourier set. The fixed polynomial list and coordinate order are part of the reference instance known to the decoder. Given S, the decoder computes B_S and L_S and decodes an r_S-bit affine coordinate. No extra choice of geometry is made separately for each observed set. If an unknown representation is selected from several lists, a normalized prior and its selection cost would additionally be required; this theorem does not waive that cost.

Gibbs' inequality, the derivative law and Step 1 now give

    H(F) <= H(|S|)+(2/ln 2)(1+ln 2) I_x
                    +log_2(pi^2/4) I_x + E_p r_S.

The spectral-level entropy of h is at most log_2(4+e) I(h)=log_2(4+e) I_x by the recovered Boolean level lemma. Step 3 gives E_p r_S<=2I_z. Consequently

    H(F) <= [log_2(4+e)+2log_2(e*pi)] I_x+2I_z.

This proves the claimed complete rank-reference theorem. Alternatively Step 2 plus H(h)<=C_reg D(h) gives the stated D_x refinement directly. No unsupported line occurs in the class theorem. For arbitrary controls, the first unsupported universal line would instead be sum_S p_S H(a_S)<=K sum_S p_S I(a_S) with absolute K. Taking h to be a dictator reduces that proposed line to full FEI on an arbitrary control a_1; the quadratic hypothesis is essential to the current proof.

## executed validation with domain, arithmetic, commands and outputs

The specification was frozen in out/FROZEN_SPEC.json before computation. The v1 pilot passed 100 actual Boolean parity lifts and 1,005 assertions in 0.0071 seconds. The quadratic extension was then frozen as helper v2 before its bounded full run. No GPU, random sampling, large allocation or automatic dimension escalation was used. Estimated memory is at most 40 MB; no job over 300 MB was proposed. Full results: 448,684 assertions passed, 0 failed, in 108.928 seconds (within the frozen 180-second bound). A separate direct-character transform and F2 row-elimination implementation checked all 2,198 quadratic phases in dimensions 0 through 4: 13,188 assertions passed in 0.428 seconds. It verifies polar-matrix rank against exact affine spectral support size. This separate implementation is not independent human/agent review.

Commands:

    python -X utf8 runs/20261011T222313Z-account05-A068-antichain-beyond-one-order/code/check.py --pilot
    python -X utf8 runs/20261011T222313Z-account05-A068-antichain-beyond-one-order/code/check.py
    python -X utf8 runs/20261011T222313Z-account05-A068-antichain-beyond-one-order/code/quadratic_core.py

The checker uses independent integer FWHT on actual truth tables, direct edge-boundary counts, exact Fraction identities, exact affine closure, and exact normalization. It checks 16,658 linear-control lifts (all base Boolean functions on q<=3 and all q by 2 control matrices), 3,106 quadratic-control lifts (exhaustive q<=2, fixed declared q=3 subclass), and linear/quadratic cyclic controls at q=3,5,7 (physical dimension at most 14). Entropy factorization is verified by exact atom-probability multisets; no floating logarithmic comparison is asserted as a certificate. Regular-base antichains, rational noise bounds, harmonic rank bounds, non-unateness, and cyclic physical influence formulas are checked. The infinite-dimensional theorem comes from the analytic proof, not extrapolation of this census.

## proof dependencies and changed downstream conclusions

Dependencies are the baseline signed antichain/noise/rank mean, Euler reference and Boolean spectral-level lemma. Their hypotheses are preserved conditionally on z, and the new quadratic packet argument is self-contained. The effective-piece lemma from SEED_LEMMAS.md is not invoked or counted as new work. Neither incoherent shared-variable product subadditivity nor the refuted fixed-order Renyi helper is used.

B14 now has a complete candidate proper-class theorem on nonlinear systematic quadratic shears. B04/B12 can use its low-selector-energy closure and retain control rank cost. B02/B08 can use exact conditional packet cost rather than a worst-case control-label count. No universal claim C018, C019, C020 or C024 is marked solved. The linear subcase agrees with the recovered isospectral translation reduction; only the quadratic affine-fiber payment is proposed as this stage's mechanism advance.

## one next mathematical action and independent reviewer

Next: identify one pair of private data coordinates in this quadratic-shear representation and derive the resulting signed two-row Fourier collision/reference cost. Keep its normalization and phase cross terms, seeking a single paid influence bound rather than silently assuming the graph remains injective. This removes the exact sufficient hypothesis where the present proof uses private data labels. Independent reviewers: A088 and A094, with A070 as the B14 analytic scope consumer. Their acceptance has not yet been obtained.

## actual persistence receipts or precise save blocker

All writes are confined to the A068 workspace. REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, NEW_RANK_GEOMETRY.tex, WIDTH_SEPARATION_EXAMPLE.md, frozen specification, code and exact outputs are saved locally. out/RECEIPTS.json records SHA256 and sizes after validation. STATUS.md, WORKLOG.md and LEARNED.md are updated locally. No Git, brain mutation, another-agent write, publication or mirror verification is claimed. Supervisor adoption/copy and independent review remain external follow-up steps.

Universal bridge: this stage advances C020 whole-set witness cost on systematic quadratic-control gates by paying the complete reference at C_reg I_x+2I_z, including a conditional affine-rank bill rather than a selector-label count; the nonlinear cyclic family has vanishing selector influence per control but a constant complete cost. Universal FEI remains open because private data labels prevent coherent collisions, and arbitrary control packets already contain FEI at a dictator base. The shortest next step is one private-data identification: it isolates the first actual signed collision introduced when this exact encoding ceases to be injective, directly connecting the proved rank geometry to the unpaid universal witness cost rather than opening another unrelated structured class.
