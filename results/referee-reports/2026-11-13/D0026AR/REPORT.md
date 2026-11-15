ACCEPT

Theorem A is correct as a partial result. For every q>1/2, it proves local convergence from every deterministic configuration containing an infection, exponentially fast uniformly when one initial infection location is fixed. Bounded convergence then gives convergence for every initial probability law supported on nonempty infection configurations, without a moment hypothesis. I found no mathematical error or unresolved gap in the reduction in claim_files/REPORT.md, lines 13–59.

The critical distinction is that the true single-seed law never acquires a globally uniform exponential distance moment at any fixed finite time. The report does not assert that it does: it applies BCMRT to a different law obtained by filling the exterior of a growing interval with zeros. Its finite-propagation comparison correctly protects the observable from that modification. Thus the objection in the review brief identifies a real obstruction to a direct invocation of BCMRT, but does not break the submitted proof.

This establishes Conjecture 1 with its parameter range restricted to q>1/2. It does not establish the conjecture for all q. The proof is a short localization consequence of published estimates, and the submission explicitly disclaims novelty. The exact whole-range q>1/2 statement was not located as a printed theorem in the sources checked; the near-one part is already covered by Mountford–Valle. No priority claim follows from this audit.

Errors and gaps, with locations and disposition:

1. No substantive error or unfilled proof obligation was found in Theorem A. No correction is required for acceptance as the claimed PARTIAL result. The detailed checks below explain the potential failure points and their resolution. The supplied snapshot omits the source files referenced by the other run; I independently downloaded the required sources and do not rely on those missing artifacts.

The following audit uses line numbers in claim_files/REPORT.md.

1. Lines 15–19: the imported theorem is applicable in its stated restricted class. [BCMRT, arXiv:1205.4584](https://arxiv.org/abs/1205.4584), Theorem 2.1, PDF p. 4, assumes q>1/2, a graph of (k,D)-polynomial growth, a local function g with equilibrium mean zero, and an arbitrary initial law mu satisfying

   κ = sup_x E_mu[theta_0^{d_x}] < infinity for some theta_0>1.

   It gives |mu P_v g| <= c||g||_infinity exp(-v/c) for D=1 and v>=2; for D>1 its bound is c||g||_infinity exp(-(v/(c log v))^{1/D}). The printed dependence is c(q,k,D,κ,|supp g|). Dependence on the available exponent theta_0 is implicit and visible in the proof, PDF pp. 11–12. The submission explicitly keeps that exponent fixed. On Z take k=3,D=1. For a noncentred f, use g=f-pi(f) and ||g||_infinity<=2||f||_infinity; this factor is absorbed into C. Neither independence nor translation invariance of mu is required. Remark 2.3, p. 5, expressly says the deterministic hypothesis means uniformly bounded gaps, so a single seed cannot be inserted directly.

2. Lines 21–37: the distance Lyapunov estimate is correct. Write p=1-q, choose 1<theta<q/p, and put

   lambda=(theta-1)(q/theta-p)>0,
   c_* = q(theta-1)/theta,
   B=c_*/lambda=q/(q-p theta).

   If d_x=k>=1, a site one step closer to x than a nearest zero is healthy and can become infected at rate q. When k=1 and there are two nearest zeros, this is still one legal site of rate q, which suffices. Distance can increase only by healing a unique nearest zero, at rate at most p. A healing zero has an infected neighbour, so the increase is at most one. Two nearest zeros cannot both heal at the same event. Consequently

   L(theta^{d_x}) <= -lambda theta^{d_x} for d_x>=1.

   At d_x=0, a legal healing makes the distance exactly one, hence the generator is at most p(theta-1)=-lambda+c_*. Therefore globally

   L(theta^{d_x}) <= -lambda theta^{d_x}+c_*.

   Integration gives the slightly sharper bound e^{-lambda u}theta^{d_x(eta)}+B(1-e^{-lambda u}), and thus (A1). The printed BCMRT Proposition 4.1, PDF p. 10, has lambda=(theta²-1)/theta [q-theta/(theta+1)] and B=q/[q(theta+1)-theta]; these are exactly the same constants. The condition q>theta/(theta+1) is equivalent to theta<q/p. The finite-interval approximation with frozen exterior zeros preserves the generator bound. For fixed x its initial distance eventually equals the original distance; graphical convergence and Fatou justify passing to infinite volume. A zero lineage, whose transfer rate is at most p, also shows nonextinction at finite times. No attractiveness assumption is hidden here.

3. Lines 39–50: the burn-in and the treatment of unreached sites are correct. Let a=log theta, delta=lambda/[2(lambda+100a)], u=(1-delta)t, s=delta t, and I_t=[h-r-ceil(100s),h+r+ceil(100s)]. For any initial eta with eta_z=0 and x in I_t,

   d_x(eta) <= |x-z| <= |h-z|+r+1+100s.

   Retain eta(u) on I_t and set all exterior sites to zero, obtaining zeta with law mu_t. This static modification can only decrease distance to the nearest zero; it asserts no order comparison between evolving processes. Hence

   E_mu_t[theta^{d_x}] <= B + exp(a(|h-z|+r+1)+100as-lambda u)
                            = B + exp(a(|h-z|+r+1)-lambda t/2).

   The equality follows from (lambda+100a)delta=lambda/2. For x outside I_t the moment is exactly one. Thus K=B+1 works globally whenever t>=2a(|h-z|+r+1)/lambda. K and theta are independent of t and of the remaining initial spins. This handles the far-away, healthy, unvisited line: it is altered in the auxiliary law, rather than being incorrectly assumed already equilibrated.

   To make the distinction explicit, from a single seed at z the event of no infection-creating marks at z-1,z+1 before u has probability exp(-2qu). On that event the process is still the single seed. Thus for every fixed u,

   E_eta[theta^{d_x(eta(u))}] >= exp(-2qu)theta^{|x-z|},

   and the supremum over x is infinite. The submitted argument survives exactly because it applies BCMRT to mu_t, not to this true time-u law.

4. Lines 50–52: the BCMRT constants remain uniform. Invoke the theorem separately for each mu_t with the same q, theta and K=B+1, and the same fixed observable f. The theorem is an estimate over all laws satisfying those bounds; it is not merely a separate qualitative convergence assertion for each law. Use t sufficiently large that also s>=2, namely

   t >= max{2/delta, 2a(|h-z|+r+1)/lambda}.

   This is compatible with the submission's final extension over bounded initial times. No constant depending on t or the sampled intermediate configuration is introduced.

5. Lines 54–59: the graphical estimate is valid. Run zeta and eta(u) under the same fresh rate-one clocks and resampling coins. The exterior zeros of zeta are free to change. A disagreement reaching supp(f) during s requires a chronological nearest-neighbour path with at least m=ceil(100s) steps. There are at most |supp(f)|2^n paths of n steps ending at the support. For each spatial path, the expected number of correctly ordered clock tuples is s^n/n!, including paths revisiting a site. A union bound therefore gives the stated series. With rho=2e/100<1,

   sum_{n>=m}(2s)^n/n! <= sum_{n>=m}rho^n
                         <= (1-rho)^{-1}exp(-c_0 s),
   c_0=100 log(100/(2e))=291.2023005... .

   This is an influence bound, not a monotone coupling claim. Converting the probability bound to an expectation costs at most 2||f||_infinity, absorbed into the prefactor. The estimate applies uniformly to arbitrary initial disagreement outside I_t.

6. Lines 43 and 59: the Markov-property step is sound. Both u and s are deterministic once t is fixed. Precisely,

   P_t f(eta)=E_eta[P_s f(eta(u))],
   mu_t P_s f=E_eta[P_s f(F_{I_t}(eta(u)))],

   where F_{I_t} fills the exterior with zeros. Future clocks are independent of eta(u). Apply the comparison in item 5 inside this expectation. There is no conditioning on future successful spreading, and no stopping-time substitution. Combining the estimates gives A exp(-b t), uniformly over eta_z=0, for sufficiently large t, with b=delta min{1/C,c_0}>0. Increasing A covers earlier times. Its dependence on q, f and z is permitted by Theorem A.

7. Line 59 and lines 109–111: the arbitrary-law conclusion requires no moment hypothesis. Every deterministic configuration in {eta: some eta_z=0} satisfies the established pointwise limit. The measurable integrand P_t f(eta)-pi(f) is bounded in absolute value by 2||f||_infinity. Dominated convergence applies directly under nu. No measurable choice of a seed, integrable distance to a seed, or integrable eta-dependent exponential prefactor is used. This yields qualitative convergence for arbitrary nu; an exponential rate uniform over all such nu is not asserted and would be false for seeds arbitrarily far from the observable.

8. Lines 63–76: the additional infected-region drift check passes. For finite nonempty initial infection sets, graphical finite propagation keeps the set finite at finite times. The rightmost infection advances by one at rate q and retreats by one at rate p times the indicator that its left neighbour is infected. Its drift lies in [q-p,q]=[2q-1,q]; its compensated martingale has predictable quadratic variation at most t. Doob's inequality on dyadic intervals gives summable O(2^{-n}) deviation probabilities, so M(t)/t tends to zero almost surely. Reflection gives the left-front bounds. This validates Proposition B, but Theorem A does not require a separate front-speed theorem: its distance estimate already supplies the needed local information. For q<=1/2 no theta>1 makes lambda positive, so this proof stops there.

Independent numerical verification:

I wrote code/referee_sim.cpp before reading the supplied simulation source. It uses a binary tree of individual flip rates, rather than the submitted implementation's active-site lists. With infection represented by spin zero, each facilitated healthy site flips at rate q and each facilitated infected site heals at rate 1-q. One or two infected neighbours enable the same rate. Exact exponential waiting times omit only null heat-bath resamplings. Exterior spins are healthy; the origin is infected initially and thereafter evolves freely.

There are 10,000 independent trajectories at each q, on [-1024,1024], through t=100. Seeds are 260001 and 260002. The following estimates are E[1{eta_0=0}], with one empirical standard error in parentheses; the equilibrium values are 0.55 and 0.70.

| t | q=0.55 | q=0.70 |
|---:|---:|---:|
| 0 | 1.0000 (0) | 1.0000 (0) |
| 1 | 0.8843 (0.00320) | 0.9085 (0.00288) |
| 2 | 0.7550 (0.00430) | 0.8051 (0.00396) |
| 5 | 0.5981 (0.00490) | 0.7091 (0.00454) |
| 10 | 0.5450 (0.00498) | 0.6933 (0.00461) |
| 20 | 0.5287 (0.00499) | 0.6883 (0.00463) |
| 50 | 0.5525 (0.00497) | 0.6949 (0.00460) |
| 100 | 0.5527 (0.00497) | 0.6954 (0.00460) |

The final residuals are 0.54 and -1.00 standard errors. The trajectory averages need not decrease monotonically toward equilibrium: the q=0.55 estimate at t=20 is below equilibrium. These data support relaxation, and neither prove a limiting statement nor estimate a rigorous exponential rate. Observations at different times on the same trajectory are correlated.

Boundary influence on the origin by t=100 is bounded by the clock-path series with m=1024. Applying the same factorial estimate gives a log upper bound below -647.59. No simulated path infected either endpoint; maximum visited distances were 61 and 91. The analytic bound, rather than the absence of observed endpoint infections, controls the infinite-volume approximation.

For a separate implementation check, code/validate_sim.py enumerates the 31 nonempty states on five sites with healthy boundaries, constructs the generator directly, and computes transient laws by Poisson uniformization. At each q I ran 80,000 further trajectories with seeds 260003 and 260004. Across the 31 terminal cells, maximum deviations were 2.013 and 2.880 standard errors; the checked origin time-series deviations were at most 1.863 standard errors. Generator row sums vanish within 2.23e-16, detailed balance within 6.94e-18, and stationary residuals within 2.78e-17. Details are in data/validation.json and the check CSV files. The invariant law here is product equilibrium conditioned on nonemptiness, as used in that validation.

I also independently enumerated every nonempty nine-site configuration and every observation site, at q=.5001,.55,.7,.99: 4,599 generator-inequality checks per q, all passed. The symbolic constant identities above and numerical substitutions independently agree. These finite checks supplement the general argument; they are not its proof. Results are in data/algebra_audit.json. A later read of claim_files/code/simulate.cpp confirmed the submitted flip rates and clock convention. Recomputing the 24 terminal standardized differences in its summary.csv gives a maximum 2.093418, consistent with its reported 2.10 bound; I did not rerun its eight large experiments.

Literature result and value:

| Primary source checked | What is actually established | Does it contain Theorem A at its full stated range? |
|---|---|---|
| [BCMRT 2013, arXiv:1205.4584](https://arxiv.org/abs/1205.4584), Theorem 2.1, Remarks 2.2–2.4, Proposition 4.1 | q>1/2; initial laws with globally uniform exponential distance moments; exponential relaxation in dimension one. | Its theorem statement excludes the single seed. Its published estimates, plus the valid localization above, imply Theorem A. |
| [Mountford–Valle, arXiv:1609.01364](https://arxiv.org/abs/1609.01364), Theorem 1.1 p. 2, Remark 1.2 p. 3; published 2019 | Bounded-degree graphs with the specified subexponential growth bound; q sufficiently close to one; single seed, and an initial-law extension with an exponential tail for distance to an infection from one fixed centre. Their facilitating spin is 1. | Covers the near-one part. Every deterministic nonempty configuration satisfies Remark 1.2, and bounded convergence yields arbitrary nonempty initial laws qualitatively in that range. It does not specify q_0=1/2. |
| [Blondel–Deshayes–Toninelli, arXiv:1803.08761](https://arxiv.org/abs/1803.08761), Theorems 2.1–2.2 pp. 4–5, Propositions 3.1–3.2 pp. 7–8, Corollary 3.3 p. 9 | Front invariant law, LLN and CLT above a contact-process threshold; local relaxation from sufficiently infected intervals for q>1/2. | No identical arbitrary-seed q>1/2 theorem located. The front conclusions keep their stronger q restriction; the local propositions still require infections throughout the observation region. |
| [Ertul, arXiv:2103.00019](https://arxiv.org/abs/2103.00019), Theorems 2.1–2.2 pp. 3–4 and Section 4; published ALEA 2022 | Finite-interval mixing/cutoff with infected boundary, above the contact-process threshold. Proposition 4.1 has q>1/2 but requires distributed infections. | Does not state the whole Theorem A. A finite chain with a frozen infected boundary is not the original single-seed infinite process. |
| [Shapira, arXiv:2005.13327](https://arxiv.org/abs/2005.13327), Theorems 1.1–1.3 p. 2 | Equilibrium spectral-gap/persistence estimates and finite-graph bounds. | No: these stationary estimates do not themselves imply pointwise convergence from a singular initial configuration. |
| [Hartarsky–F. L. Toninelli, arXiv:2212.08437](https://arxiv.org/abs/2212.08437), Theorem 3.3 p. 9 and Section 4 | General update families, q sufficiently close to one, suitable product initial laws (with extensions described in a footnote). | No replacement for the single-seed q>1/2 argument. |
| [Hartarsky–C. Toninelli, Kinetically Constrained Models, 2025](https://www.normalesup.org/~hartarsky/files/research/publi/KCM_book.pdf), Chapter 7, particularly Theorems 7.19–7.21, printed p. 86/PDF p. 96 | High-density general-model convergence, finite-volume mixing, and FA-1f cutoff with restrictions retained. | No identical theorem located in the checked chapter. |
| [Martinelli–Shapira–Toninelli, arXiv:2510.20461](https://arxiv.org/abs/2510.20461), Conjecture 1 p. 2, Section 4 pp. 16–20, Section 6 pp. 25–27 | All-q arbitrary-nonempty-law convergence is conjectural. Section 4 concerns the small-delta West perturbation of East with restricted initial laws. Section 6 controls finite-seed extent and diameter at all q. | None of these statements already supplies all-q FA-1f local convergence. The delta-West generator is different; diameter growth does not control interior healthy gaps. |
| [Martinelli, ICM 2026 survey, DOI 10.1137/25M180425X](https://epubs.siam.org/doi/10.1137/25M180425X), Section 2.2.1, Conjecture 2.11 | Explicitly restates the all-q arbitrary-nonempty-law convergence conjecture; reference 48 cites 2510.20461. Publisher metadata dates publication to 13 July 2026. | Confirms that the full conjecture was still being posed in this 2026 publication. |

As an additional cross-check, Marêché's thesis, printed p. 33/PDF p. 55, Theorems 3.6 and 3.7, distinguishes Mountford–Valle's one-centre-tail, q-near-one theorem from BCMRT's uniform-moment, q>1/2 theorem. It does not identify these initial-law classes.

Exact-ID, author and topic searches through 13 November 2026 found no later primary paper resolving the full conjecture. Search queries and retrieval limitations are recorded in sources/search_records.txt. This is a finite literature search, not an exhaustive citation certificate. In particular, an open conjecture in a July survey does not rule out later work. I do not certify originality of the elementary extension to q>1/2; I certify the reduction and its scope.

What remains open in the audited claim is convergence from arbitrary nonempty configurations when 0<q<=1/2, including a single seed. The proof neither gives a counterexample nor closes that range. Positive equilibrium spectral gap, stationary-measure classification, and all-q diameter growth are insufficient substitutes for the missing local relaxation estimate. The full Conjecture 1 and its all-q quantitative companion therefore remain unresolved by this work.

All requested arXiv sources were independently downloaded and converted through pdftotext stdin, with PDF bytes held only in memory. Only plain text is retained in sources/, with retrieval timestamps and SHA-256 digests in manifest.txt. The simulation is serial, one thread, inherited nice 10; measured simulator peak RSS was under 2.5 MiB. No publication, push, commit, subagent, retained PDF, or source-page image was used. Reproduction commands and final artifact checks are in LOG.md.

Task: “You are an independent referee. … Break it if it is wrong.” — 13 November 2026, approximately 07:45 Asia/Tbilisi.
