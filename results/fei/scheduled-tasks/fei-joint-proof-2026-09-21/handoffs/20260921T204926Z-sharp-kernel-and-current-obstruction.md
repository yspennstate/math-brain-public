# All-account FEI handoff: sharp kernel comparison and the actual half-band positive-current obstruction

21 September 2026. Owner-requested interactive account02 research under FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z. **Full FEI remains NOT PROVED.** New analytic results are self-checked, pending independent review; no publication-priority claim. This is mathematical input for every account, not a fabricated worker acknowledgment or native brain ingestion.

## 1. Complete source package and mandatory read order

Private scientific repository: `yspennstate/math-open-problems`, branch `master`.

Complete package commit: `dfb0dffbe472f19a15e3c3b22bc563d527a979ab`.

Directory:

    proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T204926Z-threshold-contraction/

Read `REPORT.md`, then `HALFBAND_COLLISION_EXTENSION.md`. The extension is the latest result: it strengthens the initial full-line and later-cutoff obstructions to an actual HALF-BAND finite-window obstruction. Do not continue from the earlier report's provisional scope without reading it.

Proof blobs:

    REPORT.md: 3a3c9f2c1b3d2cc759fb0fd390146ae7440f4ee0
    HALFBAND_COLLISION_EXTENSION.md: 2efc5dedf145a262700649c6e711c6a6fb91d622

The complete package also contains `verify_threshold_contraction.py`, `verification.json`, `verify_halfband_collision.py`, `halfband_collision_checks.json`, and `MANIFEST.json`. All six pre-manifest blob hashes and byte lengths were read back at scientific commit `54cb04ad96c06fbf04e773fb122f8a80497ed145` and matched the local executed artifacts. Both checkers were rerun separately with byte-identical output. This is reproducibility evidence, not independent mathematical review. The newly written scripts were accepted normally; no older denied upload was retried or bypassed.

## 2. Exact peer claims consumed, and what is superseded

This work directly consumes account02/B18 `20260921T200356Z-restriction-kernel-polarization/REPORT.md`, blob `f139911380f55a0dc715c4d00463b2e33a2ab947`; account01/B16 `20260921T195223Z-square-first-window-gram/REPORT.md`, blob `ebd532a214b9b4a293363578e0237fce636bab68`; account04/B16's authentic active-syndrome, ordered-min dual, and slice-clone source identities; and the newer account01/B16 `20260921T204046Z-terminal-shell-feature-projector/REPORT.md`, blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`. Complete immutable source paths are in REPORT Section 0.

The peer's PSD identities, square-first window domination, orthogonal retained-shell projector, and same-syndrome coefficient identities remain valid. The explicitly OPEN all-Boolean Brownian closing target in account02/B18 (9.1), equivalently account01/B16 (8.1), is now REFUTED by the source-valid construction below. This is stronger than the earlier peer counterexample to a diagonal surrogate: our example keeps the retained code, negative within-code terms, same-syndrome sums, and actual active orbit.

The subsequent attempt to restore exact current weights and then retain only the finite half-band window is also refuted at its ALL-BOOLEAN positive-budget scope. The original signed FEI inequality with its other reserved negative credits is NOT refuted. Nor is an independently justified restriction of the target to a narrower high-ratio critical class.

## 3. Positive result: sharp comparison for the ENTIRE entropy kernel

Let X,Y>=0. In natural logarithms define

    S(X,Y)=(X+Y)ln(X+Y)-XlnX-YlnY,
    P(X,Y)=(X+Y)D(2sqrt(XY)/(X+Y)),
    D(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2,
    G=S+P,    M(X,Y)=min(X,Y).

For every finite point family and every REAL coefficient vector, the exact optimal quadratic-form comparisons are

    S <= pi M,
    P <= (pi^2/2-pi) M,
    G <= (pi^2/2) M.

Divide constants by ln2 for the predecessor's bit-normalized kernels. These are sharp kernel constants, not universal FEI constants. They are not entrywise inequalities.

The proof computes mixed derivatives

    L_S(u,v)=1/(u+v),
    L_G(u,v)=ln((sqrt(u)+sqrt(v))/|sqrt(u)-sqrt(v)|)/(2sqrt(uv)),
    L_P=L_G-L_S>=0,

and applies an exact weighted Schur identity with weight u^-1/2. Their Schur masses are pi, pi^2/2, and pi^2/2-pi. Logarithmic coordinates turn them into positive convolution kernels, giving sharpness. For every signed threshold profile A the comparison retains the exact nonnegative deficit

    C integral A^2 - integral integral A L_K A
      =(1/2) integral integral L_K(u,v)/(sqrt(uv))
           [sqrt(u)A(u)-sqrt(v)A(v)]^2.

The Shannon part is classical Hilbert/Carleman machinery; its use is not a discovery claim for that classical theorem. The contribution here is the complete source-relevant comparison and its exact constants and deficit.

## 4. Actual Boolean construction: the proposed positive payment is false

Let D be the fine dimension, n=D-1, N=2^D. On the original n-cube let f=-1 at u=(1,...,1) and v=u+e2+e3 only, and +1 elsewhere. Append the source dummy coordinate. The negative set Q is now an affine two-plane of four points. All n ORIGINAL coordinates remain relevant, and

    J(f)=I(f)=8n/N,
    H(f)<4I(f).

With original coordinate1 first and the dummy last in the ordered-min basis, the original source has exactly two singleton parents, and the fine source has exactly their FOUR active singleton clones. The authentic h=g_S is therefore uniform over the sixteen subsets of Q. Every three-element active mode has q=3,k=1 and exact positive multiplier e=4/9, central multiplier epsilon=11/288. This is not an uncharged q=k example.

Use the actual retained measure alpha=Unif(RM(1,D))-Unif(RM(d,D)). For correlations U_r=c_r(h), V_r=c_r(fh), define

    A_h(u)=sum_r alpha_r[1{u<=V_r^2}-1{u<=U_r^2}],
    Q_M(h)=integral A_h^2.

At d=ceil(D/2), the initial theorem proves that N^2 E_S Q_M(g_S), its exact-current-weight version, and the full-line positive current each stay bounded below away from zero while J->0. Thus their ratios to J diverge.

The final extension is stronger. At the actual canonical live endpoint S_f=2sqrt(N/J), for every D>=128,

    integral_40^Sf E_cur(s)ds/s^3 >=7/[3145728 n^3],

and analytically

    integral_40^Sf E_cur(s)ds/s^3 ~4/(27n^3).

Thus the leading current/J ratio is 2^D/(54n^4), unbounded, even on the HALF-BAND finite window. The same obstruction applies to the exact central multiplier and survives the original anchor/order average with a fixed positive fraction at least 1/8. This is a lower bound on the actual positive current, not merely on an inefficient upper bound.

Do not mislabel this as FEI failure: the same functions satisfy H<4I. It shows that this positive-current closing estimate was stronger than the theorem we need and false at its stated generality.

## 5. New collision tool giving the half-band extension

For +/-1 variables matching independent signs through degree4m, let W be their sum, W' an independent copy, and let |Z|<=1 be arbitrarily dependent on W. The proved bound is

    integral_0^pi |E[Z exp(itW)]|^2 dt
       <=pi Pr(W=W') <=pi/K_(2M,m)<pi/sqrt(m),

where M is the number of signs and

    K_(N,m)=sum_(j=0)^m binom(N/2,j)^2/binom(N,2j)
            >=(2m+1)binom(2m,m)/4^m>sqrt(m).

The zero-atom estimate follows from a normalized Krawtchouk reproducing polynomial. The collision estimate applies it to the two-copy sum W-W'; exact Fourier orthogonality then handles the dependent multiplier Z. All needed arguments are in the package.

For the terminal code, remove the four active evaluation positions. Its remaining signs retain bounded independence. A triple's EXACT coefficient is

    b_R^(1)(Nt)=2N sin(t)^3 cos(t) E[Z_R sin(t W_out)].

Taking m=2^(d-1)-1 bounds its weighted energy on t<=T=(2n)^-1/2 by 4pi T^3/sqrt(m). The affine part has a complete explicit trigonometric formula and energy asymptotic (2/3)T^6 per triple. At the half-band cutoff the terminal term is negligible in the genuine weighted L2 norm. This yields the claimed finite-window asymptotic without enumerating huge Reed--Muller codes.

The result more generally holds when 2^d/n^3 tends to infinity. Merely moving to a later cutoff does not repair the positive-current target.

## 6. What the next run should actually attack

Primary source/interface-C recipients: account01/B16, account02/B16/B18, account03/B16/B18, account04/B16. Arithmetic/negative-credit partners, especially account02/B15 and their counterparts, should receive the exact remaining signed expression.

Do not spend another substantive run proving N^2 E Q_M<=CJ or integral_live E_cur<=CJ for ALL Boolean functions under these unchanged definitions: the complete counterfamily now rules both out. Preserve the valid peer identities and our sharp kernel theorem. Work instead with the original signed expression including the compensating R16/entropy/terminal terms, or derive a genuinely sufficient critical-core restriction that excludes these low-ratio examples and prove the narrower estimate there.

REPORT Section7 gives the exact cutoff-aware identity

    integral_W E_cur=(pi^2/2)Gamma_cur-D_cur-T_(outside W),

with nonnegative Schur and outside-window credits. It is correct, but the extension proves that even its full finite-window positive left side need not be O(J). Therefore the other signed credits or a justified narrower domain are essential. No universal compensation theorem is claimed in this run.

The independent adaptive restriction and joint derivative-stability routes remain available. The earlier paid subcube theorem retains its q/(16r) support-error hypothesis, and the fixed-relative one-row shortcut remains refuted. The scalar global phase/rank/l1 route and sign-free relaxations remain retired. Do not conflate any of these scopes.

## 7. Verification and operational scope

The executed checks include four small exhaustive Reed--Muller codes with 128/2048/32768/65536 words; exact moments, histograms and active-orbit coefficients; 124 Christoffel comparisons and 22 polynomial norm identities; explicit Boolean spectra through D12; exact Laurent-polynomial verification of the new terminal coefficient; and 385 rational checks of the large-D threshold. Kernel eigenvalues and high-precision quadrature are explicitly numerical diagnostics. The all-dimensional theorems have analytic proofs and do not rely on extrapolating small cases.

Both checker outputs were reproduced byte-for-byte in separate local processes. No independent end-to-end mathematical review or novelty clearance has occurred. Configured model/effort and provider thinking counters remain unexposed; model self-report is GPT-6 Astra Pro. Native brain packages were unavailable, so the work is WITHOUT_VERIFIED_BRAIN.

This handoff does not reassign brain or benchmark workers, modify any native schedule, activate production state, or claim any worker already read it. The existing eight-brain/five-benchmark/seven-FEI allocation per account remains unchanged. Both repositories were confirmed private; explicit new artifacts were checked for credentials and unrelated private content. There is no benchmark gold, private transcript, scheduler identifier or permission change in this package.
