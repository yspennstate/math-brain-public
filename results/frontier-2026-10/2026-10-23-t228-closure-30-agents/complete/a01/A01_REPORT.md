# A01: T228 source recovery, independent audit, and explicit contraction certificate

Date: 2026-10-23. Assignment: exact current T228 source and a serious closure route. No remote repository writes or external messages were made. This is a mathematical audit and local proof supplement, not a new-discovery claim.

## Principal finding

The current private dossier is `<private-repo>/06_math_research/frontier/rows/T228/DOSSIER.md`, blob `5d95a5f8a9d830ca673e75321d66f66d9dccad45`. Its last modifying commit is `6f58ab3ea6706e018db82f2dc905b12ec21f20a2`, dated 2026-10-22T04:22:56Z, message `T228: target 3 verified`.

This source is newer than the initial T2-only report: its final entry says ALL THREE repaired dossier targets are proved and reviewed. T1 is scalar smooth asymptotically linear SGD; T2 is scalar leaky ReLU; T3 is smooth asymptotically linear single-index SGD in every finite dimension. These are under explicit negative mean-log multiplier assumptions. The exact statement is in the byte-exact local `DOSSIER.md`.

The existing T1 proof explicitly disclaims global average Lipschitz contraction. If the original registry row requires a concrete nonlinear model with average contraction, the explicit certificate below supplies that missing condition on an open step-size interval. This builds on existing proofs and independently verifies the exact-tail and positivity arguments. It must not be described as a newly discovered general neural-network theorem.

## Source preservation and pins

Nineteen source files are saved under this directory. All were verified byte-for-byte by recomputing Git blob SHA-1. `SOURCE_MANIFEST.json` records repository paths and blob hashes, and `SOURCE_PAYLOADS.json` preserves the exact retrieved contents. Main pins:

| Relative path under T228 | Git blob SHA |
|---|---|
| `DOSSIER.md` | `5d95a5f8a9d830ca673e75321d66f66d9dccad45` |
| `moves.jsonl` | `005367810642d99b9cde2e327a8e8ded7c60bf38` |
| `w688_target1/proofs/T228_A_v1.md` | `6056b253ff1d4b9eb2411d6dec7d25c5ce8d7523` |
| `w688_target1/AUDITS_FROM_REVIEWER.tsv` | `0e98941b66685633143b2dd20f33f60e0ca70608` |
| `claude_4af6ff1a/T228_B_v2.md` | `b7b358985ff34a9ea3fa7b35339047f0fe793822` |
| `claude_4af6ff1a/REVIEW_POINT1_CHECK.md` | `2a3abd7151775dfeeb73eb721191d2b2d329dc92` |
| `claude_4af6ff1a/REVIEW.tsv` | `644b741f22ebdaabbc7cd89db470c8ad55efbc4c` |
| `claude_b1e26540/T3_CLAIM.md` | `b665c36d72d2f087c0ee11cb65628aa376dc3387` |
| `claude_b1e26540/T3_STEP1.md` | `c169b975cd3a5d8ed1f554214d010da1c587e96d` |
| `claude_b1e26540/T3_STEP2.md` | `04d08036877af25a6d083247fdbfbf834ae0206e` |
| `claude_b1e26540/T3_STEP3.md` | `a3adfc7537b6a8f51b796539c5063b07a23fca39` |
| `claude_b1e26540/REVIEW.tsv` | `0e580d2fa5b5cdfb9533d10fc42ccbc9db802782` |

Repository URLs can be formed as `https://github.com/<private-repo>/blob/main/06_math_research/frontier/rows/T228/<relative-path>`. The manifest contains the retrieved URLs. The three originally named math repositories were searched/read first; no T228 exact source was found there. A02 located the frontier registry in this repository, after which only the relevant math paths were accessed.

## Explicit nonlinear theorem with average contraction

Let delta=1/1000, sigma(z)=z+delta tanh(z), and use independent standard normal a,epsilon at each step. The label is y=epsilon, equivalently the teacher is x*=0 with unit Gaussian label noise. For every eta in [0.99,1.01], batch size one constant-step SGD for the squared loss is

    Psi_eta(x)=x-eta a sigma'(ax)[sigma(ax)-epsilon].

Then:

1. E Lip(Psi_eta)<1, hence also E log Lip(Psi_eta)<0 in the extended sense.
2. There is exactly one stationary probability pi_eta, with full support and finite first moment; the chain contracts in Wasserstein-1 geometrically.
3. There is a unique alpha_eta in (1,2) satisfying E|1-eta a^2|^alpha_eta=1.
4. For a finite strictly positive c_eta,

       lim_(t -> infinity) t^alpha_eta pi_eta(|x|>t)=c_eta.

   The stationary law is symmetric, so both one-sided limits equal c_eta/2>0.
5. Every moment of order p<alpha_eta is finite, whereas every moment of order p>=alpha_eta is infinite.

The model is nonlinear for every delta>0. It uses light-tailed Gaussian innovations, so the power law comes from multiplicative SGD dynamics, not prescribed heavy-tailed additive noise.

### A. A fully explicit Lipschitz bound

Write z=ax and

    H(z,epsilon)=sigma'(z)^2+[sigma(z)-epsilon]sigma''(z).

Then Psi_eta'(x)=1-eta a^2 H(z,epsilon), with

    sigma'(z)=1+delta sech^2(z),
    sigma''(z)=-2delta sech^2(z)tanh(z).

The elementary inequalities |tanh z|<=1, sech^2 z<=1 and |z|sech^2 z<=1 give

    |H(z,epsilon)-1| <= 4delta+3delta^2+2delta|epsilon|.

Thus a valid random global Lipschitz constant is

    L_eta=|1-eta a^2|+eta a^2(4delta+3delta^2+2delta|epsilon|).

Since E|epsilon|<=1 and Ea^2=1,

    E L_eta <= E|1-eta a^2|+eta(6delta+3delta^2).

Direct Gaussian integration gives E|1-a^2|=4 phi(1)=4/sqrt(2 pi e)<0.97. Moreover

    E|1-eta a^2| <= E|1-a^2|+|eta-1|Ea^2 <0.98.

Consequently uniformly over the whole interval,

    E Lip(Psi_eta) <= E L_eta
        <0.97+0.01+1.01(0.006003)
        =0.98606303<1.

The decimal bound is only elementary arithmetic applied to an exact analytical estimate; no quadrature or simulation is needed. A stronger available estimate is |H-1|<=3delta+(3/2)delta^2+2delta|epsilon|, using cosh^2 z>=1+z^2 and tanh^2 z sech^2 z<=1/4, but the coarser estimate already suffices.

### B. Asymptotic multiplier, root and invariant law

Expanding the gradient gives Psi_eta(x)=M_eta x+R_eta(x), M_eta=1-eta a^2, and

    sup_x |R_eta(x)| <= B_eta
       := eta |a|[delta/2+(1+delta)(delta+|epsilon|)].

Here |z|sech^2 z<=1/2 follows from cosh^2 z>=1+z^2. The random bound B_eta has all positive moments. Dependence between M_eta and B_eta is allowed.

Put h_eta(p)=E|M_eta|^p. We have h_eta(1)<0.98 and

    h_eta(2)=1-2eta+3eta^2 >=1.9603>1.

Strict log-convexity of h, nonconstant |M| and unbounded multiplier support show there is exactly one positive root alpha, and it lies in (1,2). The logarithmic multiplier is integrable, has a density, and E log|M_eta|<=log h_eta(1)<0. The density assertion follows because M_eta=1-eta a^2 has an absolutely continuous law, with no atom at zero.

The Markov map acts as a strict Wasserstein-1 contraction on probability measures with finite first moment: synchronous coupling gives W1(mu P,nu P)<=q W1(mu,nu), q=E L_eta<1, and E|Psi_eta(0)|<infinity. Completeness yields an invariant law pi with finite first moment. Uniqueness among ALL invariant probability laws follows by coupling arbitrary finite-valued initial random variables: conditional on their initial separation r, the expected truncated distance at time n is bounded by min(1,r q^n), which tends to zero, and dominated convergence then identifies any two invariant laws.

For every p in [1,alpha), Minkowski and h_eta(p)<1 give

    ||X_(n+1)||_p <= h_eta(p)^(1/p)||X_n||_p+||B_eta||_p.

Starting at zero gives uniformly bounded p-moments; convergence and lower semicontinuity imply E_pi|X|^p<infinity. The orders below one follow from the finite first moment.

Conditional on nonzero a, Psi_eta(x) is Gaussian with variance eta^2 a^2 sigma'(ax)^2>0. Therefore pi has full support. Restricting a to [1,2], and x and destination to arbitrary bounded intervals, gives a strictly positive uniform lower bound on the conditional Gaussian density. Hence every bounded interval minorizes Lebesgue measure on any prescribed bounded interval. This supplies the lower-bound argument below. No rank or Feller issue is present in this smooth scalar model.

### C. Existence of an exact radial limit

Use Jelenkovic--Olvera-Cravioto, `Implicit renewal theory and power tails on trees`, arXiv:1006.3295v5, Theorem 3.1, with N=1, C=|M_eta|, R=|X|. I independently opened the primary paper and read Theorem 3.1 on PDF page 5 (browser reference `turn32view0`). It allows arbitrary independent R and C satisfying the specified moment, nonarithmetic and tail-difference integrability hypotheses; it does not require R=CR+Q as an independent-affine identity. This is precisely the necessary interpretation here.

Stationarity permits coupling U=|Psi_eta(X)| and V=|M_eta X| with |U-V|<=B_eta. Since alpha is between one and two,

    E|U^alpha-V^alpha|
      <=alpha E[B_eta(V+B_eta)^(alpha-1)]<infinity.

Indeed the mixed step moments are finite and E_pi|X|^(alpha-1)<infinity. Therefore the tail-difference integral is at most E|U^alpha-V^alpha|/alpha and is finite. The theorem gives a nonnegative finite limit c, with

    c=E[|Psi_eta(X)|^alpha-|M_eta X|^alpha]
        /(alpha E[|M_eta|^alpha log|M_eta|]).

The numerator is an absolutely integrable difference; one must not separate it into two infinite expectations. Positivity requires an additional argument, supplied next rather than inferred from the renewal theorem.

### D. Strict positivity: full independent check of the forward argument

Write A_i=|M_eta,i|, B_i=B_eta,i and r_i=|X_i|. The iid coefficient PAIRS may have dependence internally. The pathwise inequality r_i>=A_i r_(i-1)-B_i iterates to

    r_n >= exp(S_n)(r_0-V_n),
    S_n=sum_(i<=n)log A_i,
    V_n=sum_(i<=n)exp(-S_i)B_i.

Tilt the law of each pair by A^alpha, obtaining a probability Q because E A^alpha=1. Under Q the increment log A has mean m=E[A^alpha log A]>0. Fix 0<theta<min(1,alpha). Then

    E_Q exp(-theta log A)=h(alpha-theta)<1,
    E_Q (sum_(i>=1)exp(-S_i)B_i)^theta
       <= E[A^(alpha-theta)B^theta]/(1-h(alpha-theta))<infinity.

Thus V_infinity is Q-almost surely finite. Also p+=Q(S_n>0 for every n>=1)>0: the positive-drift walk has an almost surely finite lower infimum, and a finite string of sufficiently positive increments first puts it beyond a fixed safety level.

For tau_u=inf{n:S_n>u}, the overshoot O_u=S_tau_u-u is uniformly tight in u>=0. Here is the relevant proof, since this is a nontrivial ingredient. Chernoff gives the potential bound

    U((minus infinity,1])=sum_n Q(S_n<=1)
        <=e^theta/(1-h(alpha-theta))=:C_U.

Strong Markov at the first visit to any interval [a,a+1] gives U([a,a+1])<=C_U. Dropping the first-crossing restriction and partitioning (-infinity,u] into unit intervals gives

    Q(O_u>z)<=C_U sum_(k>=0)Q(log A>z+k),

which tends uniformly to zero because E_Q(log A)^+<infinity.

Choose z and then K large enough that

    Q(V_infinity>K/2)+sup_u Q(O_u>z)<p+/2.

For every initial y with 2K<=|y|<=4K, set u=log(t/K), t>4K. On the event that S_j>0 up to tau_u, V_tau_u<=K/2 and O_u<=z, the chain remains outside [-K,K] up to tau_u and reaches |X|>t by that time. This event is measurable at tau_u. Its Q-probability is at least p+/2. Since the stopped likelihood ratio is exp(-alpha S_tau_u),

    P_y(hit {|X|>t} before returning to [-K,K])
        >=(p+/2)exp(-alpha z) K^alpha t^(-alpha).

The stopped change-of-measure identity follows by summing over finite stopping times, so no unjustified uniform-integrability assertion is used.

The compact Gaussian minorization gives a fixed positive lower bound, uniformly for |x|<=K, on the probability of jumping in one step into {2K<=|y|<=4K}. This transfers the preceding bound to excursions from [-K,K]. Finally, stationarity and decomposition according to the LAST visit to [-K,K] before a fixed observation time imply

    pi(|X|>t)>=integral_(|x|<=K) pi(dx)
       P_x(hit {|X|>t} before the first positive-time return to [-K,K]).

To verify the direction of this inequality, the disjoint last-visit events give a sum of expected numbers of visits to the distant set during an excursion; this is at least the probability of one such visit. Since pi([-K,K])>0, we obtain pi(|X|>t)>=c_*t^(-alpha) for a fixed c_*>0. Combined with the exact radial limit, this proves c>0.

This is the substantive T3_STEP3 mechanism, independently checked in full. It applies directly in the present scalar model; it needs no continuity extension of ABB and no assumption that the bounded error is independent of the multiplier.

Because sigma is odd, sigma' is even and epsilon is symmetric, reflecting x and epsilon reflects Psi. Uniqueness therefore makes pi symmetric. The two one-sided tails equal half the radial tail. Positive regular variation then gives the stated sharp moment cutoff.

## Audit of the existing T1--T3 claims

### T1: PASS for its explicitly stated conditional theorem

The gradient expansion, uniform random remainder, root argument, fractional drift, and conditional-Gaussian compact minorization are correct. The proof honestly adds E log|M|<0 and explicitly gives a large-step counterexample to the unqualified root claim. It establishes Harris/geometric ergodicity but does not claim average global Lipschitz contraction. The new explicit small nonlinear perturbation certificate above fills that additional obligation for a concrete family.

T1's ABB application uses genuinely continuous random maps, equal asymptotic slopes, a symmetric two-state Cramer matrix, continuous log increments on self-transitions and full stationary support. The algebra/hypotheses match the cited framework. I did not independently reread every page of ABB in this agent; A04 has that source-check task. The direct radial/JOC/positivity proof above is an independent alternative for the concrete model and avoids this remaining citation-audit dependence.

### T2: substantial proof passes; measurable ABB extension requires a source-level audit

The slope symmetry and state-independent selected multiplier are valid; the offset can remain state dependent. The Cramer matrix has identical diagonal entries and identical off-diagonal entries, hence Perron root E|A|^p and equal tail constants. Drift and Gaussian minorization are valid. The beta=0 atom at the old state and gamma=0 absorbing origin are correctly handled in version 2: there are two extremal invariant laws when gamma=0, so it would be false to claim uniqueness in that case. The row's original unqualified derivative-at-zero convention must not suppress this exception.

ABB assumes continuous sample maps, while these leaky-ReLU update maps jump at zero. Version 2 explicitly recognizes the mismatch and replaces Feller existence by Harris recurrence, asserting that ABB Sections 3--8 need only measurability, invariance and bounded asymptotic-linear error. Its review note enumerates every continuity occurrence. This is plausible and independently flagged for A04, but a mere word search is not by itself a proof of the extension. No new global solution claim should depend on skipping that source-level verification. The smooth model above has no such issue.

### T3: the central mathematical argument passes this independent audit

The rotational identity |Mu|^2=(1-cX)^2+c^2XY with independent chi-square X,Y is correct. A radial upper error bound depending only on |a_i| and |epsilon_i| ensures the PAIR (|Mu|,B) has the same law for every direction; therefore the selected pairs remain iid along the chain. This stronger joint invariance is necessary for positivity and is present in the proof.

The one-step minorization using Gaussian sample direction and independent Gaussian label noise is valid even when batch size is less than dimension. Keeping the positive radial sheet gives the stated polar-coordinate lower bound; a singularity at zero causes no problem for almost-everywhere density inequalities. Positive density on every ball follows by integrating stationarity over a sufficiently large input ball. The source prose could spell out absolute continuity of the whole transition kernel more directly, but the same polar calculation establishes it.

The JOC N=1 theorem is applicable to the radial variable because its selected multiplier is independent of the radius. The integrability estimate for the signed difference is correct; no false finite alpha-moment is assumed. The complete last-exit/tilted-walk positivity argument is validated above. It is especially important that the proof uses partial V_tau for the stopped measurable event, comparing to full V only under Q; the source does this correctly.

The stated nonempty alpha<2 interval follows from the exact second moment and strict Jensen at its crossing. A stable-step restriction is real, not a bookkeeping artifact. The source's claimed geometric bound should always be read as 0<p<alpha, as the detailed STEP1 states.

## Limitations and exact remaining checks

1. The original registry row wording should be quoted and matched by the coordinator before changing the solved count. I have read the full current repaired dossier; the parent reports that the original row asks for one concrete nonlinear model and average contraction. Under that criterion the theorem above is a serious full-closure candidate.
2. The stored T3 claim header reports a second audit by claude-fc67971c, commit `06966f6ae36`, but the fetched REVIEW.tsv contains the first review only, and the directory listing did not contain claude_fc67971c. The assertion of a second historic audit is therefore source-reported, not independently recovered here. This independent mathematical check does not invent the missing receipt.
3. Several source files retain draft/pending-review sections despite newer review receipts. Their old headers are superseded by the dossier and explicit review files, but both states should remain visible in an archive.
4. A literature novelty claim is separate from solving the user-defined registry problem. No first-in-literature claim is made. Existing T1--T3 authors and applicable renewal literature must be credited.
5. This is not a theorem for arbitrary neural networks, arbitrary activation growth, arbitrary data laws, or every step size. The explicit smooth scalar family proves the specific nonlinear example with a nonempty parameter interval. The unrestricted statement without stability is false.
6. No numerical tail fit, Monte Carlo check, or unverifiable model-routing claim is used as proof.

Recommended coordinator action: give the explicit contraction and positive-tail proof to fresh independent reviewers, verify the original row's quantifiers, and if those audits pass label it a completed T228 closure audit built on the prior proofs. Do not relabel the old partial status silently or attribute all existing mathematics to today's run.
