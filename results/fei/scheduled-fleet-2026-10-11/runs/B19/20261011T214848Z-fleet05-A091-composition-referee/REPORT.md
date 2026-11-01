# exact target, quantifiers, hypotheses and units

Independently audit finite Boolean disjoint substitution and fresh-selector shared-data closure, for every finite arity/depth allowed by their hypotheses. Entropy is in bits; squared coefficients use the normalized product Fourier basis. Write I_mu for spectral expected cardinality, V_mu=Var_mu, delta_mu=I_mu-V_mu. Under nonuniform inputs I_mu differs from the unweighted physical pivotal sum. For coordinate probability p_j, sigma_j^2=4p_j(1-p_j), and

    Hplus_mu(f)=sum_{S nonempty} fhat_mu(S)^2 log2(prod_{j in S} sigma_j^2/fhat_mu(S)^2).

This is corrected entropy, not ordinary Shannon entropy H_mu or conditional nonempty entropy. Uniform-cube Hplus=H-h0, h0=(Ef)^2 log2(1/(Ef)^2). Full FEI remains OPEN.

Verdict: A056's disjoint coefficient, full entropy, influence, deficit and restriction-recentering results are accepted at their stated scope by independent reconstruction. Manuscript Proposition 7.1/Corollary 7.2 and Proposition 8.6/Corollaries 8.7-8.8 have no gap in the closure derivations. The underlying all-regular and all-biased-symmetric-threshold gate estimates are cited premises, not newly independently reproved here. B09 Section 5's broad composition/additivity wording requires narrowing to aligned disjoint tensor products; its core uncertainty theorem and endpoint sharpness claim are separate review obligations.

# sources actually read, revisions and theorem locators

Protocol read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, assignment A091 and campaign plan were inspected. Advisory CAMPAIGN, CLAIMS (C004,C010-C014,C026,C035), COUNTEREXAMPLES (X002,X004-X007,X011-X013), SEED_LEMMAS and NATIVE_MAPPING were consulted. The source notes are provenance and scope controls, not unverified new mathematical premises.

Primary source: advisory baseline/current-threshold-paper.tex, Sections 6.1, 7 and 8; corresponding 38-page text, Proposition 7.1 (67)-(70), Corollaries 7.2-7.4, Lemmas 7.5-7.6, Corollaries 7.7-7.8, Proposition 8.6 (75)-(79), Corollaries 8.7-8.8. The old 29-page threshold introduction has a different regular constant (<13.415); it is not used to compute the current constant. Both percolation text versions were inspected for normalization and scope, Section 1.1: their pivotal I and spectral J differ under bias. No geometric percolation theorem is used as a gate premise, and the two versions' singularity claims are not inputs to this audit.

Read original reductions/paper/biased.tex: biasfull:composition, biasfull:mixture, biasfull:weightedcounter, biasfull:localTC, biasfull:gatepotential and biasfull:balancedoptimal. It supplies complete proofs of the three weighted controls, not merely the obstruction-registry summaries. Earlier B09 REPORT.md Section 5 and prior B05/B19 run scopes were inspected. The previous shared-data delta independent audit was read after reconstructing the equations. A056's complete REPORT.md was read; its checker code was not reused. A016's spectrum/code discussion was inspected for calibration only; no verdict on its queue asymptotic theorem is issued here.

BOARD.md was read at the start (snapshot 2026-10-11 21:55 UTC). claude/B19/STREAM_NOTES.md was absent; no lead direction was overridden. Local source hashes and targeted excerpts are recorded in out/SOURCE_RECEIPTS.json and out/SOURCE_EXCERPTS.txt. A file receipt certifies bytes, not an audit of every theorem in that file.

# complete derivation or exact first unsupported line

## Disjoint coefficient reconstruction, all child biases

Let independent product physical blocks B_i carry Boolean f_i with mean m_i and variance v_i=1-m_i^2>0. Their sign outputs have probabilities q_i=(1+m_i)/2 and are independent. Expand outer Boolean g under this induced product law nu in psi_i(z)=(z_i-m_i)/sqrt(v_i). The normalized centered child has expansion

    (f_i-m_i)/sqrt(v_i)=sum_{T nonempty in B_i} fhat_i(T) phi_T/sqrt(v_i).

For a physical Fourier set S, its occupied block set A={i:S intersect B_i is nonempty} and the individual T_i=S intersect B_i are uniquely determined. Consequently

    Fhat_mu(S)=ghat_nu(A) prod_{i in A} fhat_i(T_i)/sqrt(v_i),
    Fhat_mu(empty)=ghat_nu(empty),       F=g(f_1,...,f_k).

There is one decomposition, so no coherent cross term is discarded. Sample A from ghat_nu^2; for each i in A sample a nonempty T_i from fhat_i^2/v_i; output their union. This experiment is bijective on its positive outcomes. Set w_i=I_i^nu(g), a_i=w_i/v_i. Then

    V_mu(F)=V_nu(g),
    I_mu(F)=sum_i a_i I_mu_i(f_i),
    H_mu(F)=H_nu(g)+sum_i a_i[H_mu_i(f_i)-h2(v_i)],
    Hplus_mu(F)=Hplus_nu(g)+sum_i a_i Hplus_mu_i(f_i),
    delta_mu(F)=delta_nu(g)+sum_i a_i delta_mu_i(f_i).

For full entropy the conditional child entropy is [H(f_i)-h2(v_i)]/v_i. For corrected entropy the log numerator splits into an outer product of v_i and the physical sigma factors. This is exactly the needed cancellation. Since all a_i and deficits are nonnegative, gate/child inequalities Hplus<=C_i delta imply Hplus(F)<=max_i C_i delta(F), including the outer constant C_0.

For balanced children v_i=1 and nu is uniform, hence H(F)=H(g)+sum_i Inf_i(g)H(f_i). Ordinary FEI estimates H<=CI alone do not cancel the outer entropy. Strong deficit estimates are sufficient. For unbalanced children, retaining the old uniform outer spectrum is unsupported.

Boundary cases are exact. If v_i=0, freeze that child output and delete its gate input BEFORE division; at product-bias endpoints delete deterministic physical inputs first. Functions differing only on zero-probability assignments are identified after that restriction. If all children are constant, F is constant and H=I=delta=0. If outer input i is irrelevant, w_i=0 and its child makes no contribution. For interior nonconstant children a_i=E[(D_i g)^2], where D_i is the sign derivative on other outputs, so 0<=a_i<=1: a tiny v_i introduces no intrinsic blowup of this physical multiplier. A biased literal has Hplus=delta=0 although ordinary spectral H=h2(v_i) has a divergent H/I endpoint ratio. A uniform balanced Boolean of I=1 is a signed dictator (spectral support only on singletons and Booleanity forces a single coefficient), so its entropy is zero; division by I-1 at this terminal is forbidden.

At any physical restriction cylinder, unrevealed inputs are still independent product inputs and blocks remain disjoint. Recompute m_i, v_i, the reduced gate and its induced nu. For one changed child, write g=A+z_i B before restriction. If its new mean is m, the new outer polynomial is A+mB+sqrt(1-m^2)psi_i B; coefficients not containing i are Ahat(T)+m Bhat(T), whose squared values contain 2m Ahat(T)Bhat(T). At m=+/-1 freeze the gate input. Conditioning on an OUTPUT event is not a physical cylinder and does not justify the same product premise. This reconstructs A056's principal claims without borrowing its implementation.

## Gate admission and prime reductions

The exact identity admits symmetric threshold gates under every induced product bias with C_T=80+460/ln2, and parity with 2/ln2, using the cited gate lemmas. Uniform regular gates have a strong bound 4C_reg; an arbitrary weighted LTF internal gate is admissible by that uniform theorem only when all remaining nonconstant children are balanced. Uniform-input LTF terminal blocks can be unbalanced outputs: their bound Hplus<=4C_reg delta is a physical-input statement, and the next gate must then accept those biases. Negations preserve corrected entropy/deficit when the corresponding input law is flipped.

Fixed finite gate bases may use their separately established all-bias constants. A prime decomposition gives a conditional reduction only if every prime gate in it has a valid bound at every induced bias and one constant uniform over unbounded prime arity. The identities neither establish that prime estimate nor justify overlap of physical child blocks. The dyadic gate-potential formulation in biased.tex is FEI-equivalent, not a solution: finite uniform encoders realize only dyadic q; extension of the infimum-defined potential to nondyadic q is an additional unproved step. For arbitrary product inputs, actual physical probabilities and the admitted gate inequalities must instead cover their real induced q directly.

## Shared-data collision reconstruction and constant preservation

Let x be a fresh uniform a-bit selector independent of a common uniform data cube y, N=2^a, with Boolean branches g_b(y), including biased or constant branches. Define

    c_b(T)=ghat_b(T), R_T=N^-1 sum_b c_b(T)^2,
    r_T(b)=c_b(T)^2/(N R_T),
    nu_T(S)=[N^-1 sum_b chi_S(b)c_b(T)]^2/R_T  (R_T>0).

The actual physical Fourier coefficient is Fhat(S,T)=N^-1 sum_b chi_S(b)c_b(T), retaining its sign. Parseval over x gives sum_S Fhat(S,T)^2=R_T, including T=empty. A comparison law P(B=b,T)=c_b(T)^2/N has entropy a+average_b H(g_b), marginal R and conditional B law r_T. The actual law has the same R and conditional selector law nu_T. Subtraction of the two chain rules proves

    H(F)=a+average_b H(g_b)+sum_T R_T[H(nu_T)-H(r_T)],
    H(F)<=2a+average_b H(g_b).

Physical conditioning proves I_data(F)=average_b I(g_b), and

    Inf_{x_j}(F)=N^-1 sum_b P_y[g_b!=g_{b^j}]
               =N^-1 sum_b (1-E_y[g_b g_{b^j}])/2.

If every neighboring correlation is zero, I_sel=a/2. If instead I_sel>=c a for a fixed c>0, 2a<=2 I_sel/c. Combining branch ordinary FEI H(g_b)<=C I(g_b) proves respectively max{4,C} and max{2/c,C}. This is existing baseline closure, not new research. The weaker sufficient hypothesis is the actual averaged energy; pairwise neighboring orthogonality is one way to supply it. Nonneighbor branches need not be orthogonal. Spectral supports may overlap: only the old partition-selector mixture identity requires their disjointness.

For recursion, apply this local result at each node on the union of its branch data coordinates. Irrelevant padding changes no branch quantity. Internal branches may reuse each other's data, including selectors introduced LOWER in the construction. The CURRENT node's selector coordinates must be absent from ALL its branches, and independent under the actual input law. Induction from regular leaves preserves C_reg>4 without accumulating depth or a worst-case data-read count. If a=0 the function is the one branch. At zero selector energy all branches agree on every neighboring pair, hence all are the same Boolean function and F is that branch; the loose 2a bound should be bypassed. Constants are permitted in the shared-data identity, but two constant neighboring branches cannot have zero correlation. A constant branch may be orthogonal to a balanced one.

Reusing the current selector invalidates the independence premise: g_+(x)=x and g_-(x)=-x produce F(x)=1 when selected by that same x. Treating the branch x as independent data instead produces xy, with I=2, a different physical function. Freshness cannot be inferred from a drawn tree alone.

## Explicit controls and first unsupported lines

Old disjoint-support partition-selector formulas fail for leaves y and -y: actual F=xy has H=0,I=2, whereas the label mixture predicts H=2,I=3/2. Conversely orthogonal shared branches may have common Fourier indices with signed cancellation, as the paper's majority pair shows. Arbitrary signed singleton leaves g_u(y)=s_u y give F=s_x y and encode arbitrary Boolean s, with H(F)=H(s), I(F)=I(s)+1. Thus declaring arbitrary shared-data leaves an easy terminal assumes an FEI-strength conclusion.

The bent-splice control is independently replayed at odd m=3,5,7. Its two Boolean branches have uniform spectra on the even and odd subset classes: H=m-1,I=m/2, and local spectral erasure zero. The fresh one-bit splice has flat spectrum on all m+1 bits: H=m+1,I=(m+1)/2, selector influence 1/2. Hence zero child erasure is not a terminal entropy certificate. Here total data influence remains large, so this does not refute ordinary max{4,C} closure.

All three weighted controls come from an actual increasing threshold event

    A={m X0+sum_{j=1}^m Xj>=m},
    q=P(Xj=1), a=q^m,
    b=P(X0=1)=(1-eta)a/[eta+(1-eta)a],
    alpha=a/[eta+(1-eta)a].

Conditionally on A, X0=0 with probability eta and all light bits are one; otherwise they are independent Bernoulli q. Thus, with natural binary entropy h,

    TC(Q)=m[h(eta+(1-eta)q)-(1-eta)h(q)],
    I_mu/(4alpha)=1-eta-b+m eta(1-q),
    rho0=1-a, rho_light=(1-b)q^(m-1).

For q=m^-2, eta=1/m, d=1+(m-1)a, alpha=ma/d, one has TC=ln m+1+O(ln m/m) and I/(4alpha)=2-1/m-q-b. This proves alpha TC/I=(ln m+1)/8+O(ln m/m). For V=4alpha(1-alpha), the credit arguments are (1-a)/[alpha(1-alpha)] and m/(1-alpha), both >1. Put L=ln(1/alpha)=2m ln m-ln m+ln d. The residual divided by 4alpha is exactly

    (1-alpha)[L-ln4-ln(1-alpha)]
    -(1-1/m-b)[L+ln(1-a)-ln(1-alpha)]
    -(1-q)[ln m-ln(1-alpha)].

As a=m^(-2m), terms of size alpha L and bL vanish; the expression equals ln m-ln4+O(ln m/m). Division by I/(4alpha) gives the second no-go, .5 ln m-ln2+O(ln m/m). It refutes coefficient ONE on the credits, not every larger coefficient. Corrected Hplus/delta still tends to 2: for the light AND child delta=4a[m(1-q)-1+a] and Hplus=2delta+8ma(q-a)log2(1/q); the outer two-input OR has both deficit and corrected entropy O(ma^2), and light multiplier 1-b. These are decomposable weighted thresholds with divergent proposed PHYSICAL TC payments and a harmless actual spectral ratio.

For eta=1/2 at fixed m and q->0, Q tends to the equal mixture of (1,0,...,0) and (0,1,...,1). Every pairwise physical mutual information tends to ln2, and I_j/alpha->2 for every j. Therefore alpha sum_{k!=j} I_Q(Xj;Xk)/I_j -> m ln2/2 simultaneously for all j. This refutes even existential payment of that physical conditional-TC recursion. It is not the spectral quantity M_A=H(S_A|S_B).

B09 Section 5: tensor additivity of M_A,J_A,Delta_A is correct for disjoint PRODUCTS f=prod_r f_r with aligned physical blocks. Spectra and physical-child/spectral experiments then factor, so chain rules add. It does not extend unchanged to arbitrary disjoint outer substitution. A simple counter to child-ledger-only additivity is sign AND of two fresh uniform literals. Standalone literals have M=J=0 under any one-bit/full or empty reveal. The composed sign AND has four spectral masses 1/4, M_{first bit}=1 and J_{first bit}=1: both restricted children have entropy zero and the residual spectral bit is fair. An outer residual must be accounted for. The precise unsupported sentence is B09 Section 5's inference from tensor orthogonality of the transform to additivity of all aligned ledgers for broader gate composition. This audit does not assert a counterexample to a separately specified weighted cocycle; no such general M,J cocycle was proved there.

The B09 core uncertainty upper bound is not refuted by this scope objection. Its Section 5(4) inference that EVERY O(p) tax is impossible does not follow from the displayed upper-bound tax asymptotic alone; a necessary-tax lower-bound family is required. No endpoint sharpness acceptance is issued here. Prime-gate/low-energy terminal FEI beyond the admitted families remains unproved at the first missing all-bias gate payment or signed collision payment, respectively.

# executed validation with domain, arithmetic, commands and outputs

All specs were frozen before their corresponding computations: out/FROZEN_SPEC.json, out/FROZEN_BATCH_REVISION.json, out/FROZEN_CONTROLS.json. Pilot: python -X utf8 code/check.py --pilot, 16 cases, 130 assertions, PASS. The initial combined main hit its 58-second watchdog and exited without a final certificate. This is a resource failure, not a mathematical failure or substantive stagnation count. The unchanged domain was split into three commands.

    python -X utf8 code/check.py --law 0
    python -X utf8 code/check.py --law 1
    python -X utf8 code/check.py --law 2
    python -X utf8 code/constants.py
    python -X utf8 code/controls.py
    python -X utf8 code/endpoints.py

Working directory is this run. Three completed composition outputs are out/checks-law0.json (4096 disjoint+512 shared, 34010 assertions), checks-law1.json and checks-law2.json (4096 disjoint, 27010 assertions each). Total main: 12,288 disjoint+512 shared, 88,030 exact assertions. No symmetry reduction, sampling or floating logarithm is used for equality checks: entropy is compared as a rational coefficient vector of prime logarithms. Shared tests include all 256 pairs of two-bit branches for one selector and the fixed four-branch tuple (u,v,uv,u) for each pair; 132 tested tuples satisfy neighboring orthogonality. Constants and weighted formula signs use rational series tails, not decimal evidence. See out/constants.json and out/controls.json for actual outcomes and timings. The constants program was optimized by widening intermediate series enclosures to a rational mesh; current source is the regenerating version.

The initial controls command completed in 61.155 seconds, exceeding its frozen 60-second target by 1.155 seconds. No dimension or case escalation occurred. Widening normalized rational log arguments to a proved fixed rational mesh reduced the same replay to 0.817 seconds; that output replaces the initial one. A negative-decimal display formatter was also corrected before final regeneration; the rational intervals themselves were unchanged. The three separately frozen endpoint fixtures replay the A056 restriction witness, the shared-data majority pair, and the AND ledger scope counter. All PASS. No heavy search or memory-gated job was launched.

Final output readback exposed an accuracy loss in the high-m credit enclosures: absolute mesh rounding before division by exponentially small influence gave valid but useless intervals. The checker now evaluates the exact normalized D_m formula above before interval rounding, yielding narrow enclosures without increasing precision or dimensions. This is a conditioning repair, not a change to the analytic claim.

Independently certified outward enclosures:

| Constant | Lower | Upper |
|---|---:|---:|
| C_reg | 8.936474657877582804 | 8.936474657877582805 |
| 4 C_reg | 35.745898631510331216 | 35.745898631510331217 |
| C_T | 743.639718808923167385 | 743.639718808923167386 |
| AND/OR | 7.770780163555853629 | 7.770780163555853630 |
| parity | 2.885390081777926814 | 2.885390081777926815 |

C_reg=log2(4+e)+2log2(e*pi). The empty-atom comparison has beta=sqrt(2/(1-ln2))<2.553; thus C_T+beta<747. With Hplus<=C delta under uniform physical inputs, H<=max(C,log2 e)I and H<=(C+beta)delta. These full-entropy conversions do not hold unchanged for arbitrary biased physical inputs: the corrected-entropy sigma term must be retained. Finite checks corroborate the analytic identities; they do not supply an all-dimensional theorem by enumeration.

# proof dependencies and changed downstream conclusions

Composition identities and scope objections use only Fourier expansion, Parseval, elementary finite entropy chain rules and the explicit Boolean tables. Ordinary/strong terminal constants are conditional on the cited leaf/gate estimates, especially Theorem A and Theorem 6.6. This run does not promote B09 core uncertainty or an arbitrary weighted all-bias FEI+ estimate to an accepted premise.

A056's identities are independently accepted; its output is baseline completion, not a new solution. A041/A043/A044/A045 must state every induced gate bias, deterministic input deletion and the correct Hplus normalization. A057 must keep recentered signed coefficients after restriction. A019/A058 must pay the complete low-energy collision term or prove a controlled reuse identity; max{2/c,C} alone is already baseline. B09 Section 5 needs the tensor-only wording above unless a separate composition cocycle is supplied. B20 may ingest this review and scope artifact; no shared index was edited and adoption is not inferred from local saving.

# one next mathematical action and independent reviewer

Next action: A058 derive an explicit signed collision payment for a fixed fresh-selector family with I_sel/a tending to zero, using the exact R_T, r_T and nu_T ledger and branch terminal entropy. Alternatively consume a source-complete A043 prime-gate theorem when one exists, testing its induced all-bias hypotheses. Independent reviewer of this audit: A090, with A085 as alternate. No review of newly unavailable artifacts is claimed.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, COMPOSITION_SCOPE.json, frozen specs, code and output are local to agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee. Rolling STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md record continuation. out/RECEIPTS.json records local bytes and SHA256 hashes. Supervisor copy, remote mirror verification and downstream adoption remain pending; there is no local persistence blocker. No other agent folder, shared report tree, brain or external service was modified.
