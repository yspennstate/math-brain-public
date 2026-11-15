"""Assemble audit tables from independent numerical outputs."""
import json, datetime
from pathlib import Path

def read(name):return json.loads(Path(name).read_text())
def fmt(x):
    if x is None:return 'undefined'
    return f'{x:.11g}' if isinstance(x,float) else str(x)
out=[]
def put(text=''):out.append(text)
def table(headers,rows):
    put('| '+' | '.join(headers)+' |')
    put('| '+' | '.join(['---']*len(headers))+' |')
    for row in rows:put('| '+' | '.join(fmt(x) for x in row)+' |')
    put()

put('# Independent referee report')
put()
put('Overall verdict: **SOUND**.')
put()
put('I found no mathematical error or missing internal proof step in the supplied arguments. The main spectral results survive exact generator checks, symbolic rederivation, boundary checks, and independent numerical tests. The count cutoff and classical Ewens diagonalization use established external theorems whose quoted statements are appropriate; their exact source locations were not checked because browsing was forbidden and the articles were not supplied. This verdict does not certify historical novelty or bibliographic metadata.')
put()
put('All eleven requested parts were reached. `LOG.md` records the ordered argument-by-argument audit; it is part of this report. Every program used for computation is saved here: `audit.py`, `audit_algebra.py`, `audit_count_direct.py`, `audit_uniformization.py`, the rejected `audit_exponential.py` diagnostic, and this table assembler. No author program, external search, other agent, push, visible window, or write outside this folder was used. Numerical work ran with one BLAS thread and sparse/tridiagonal storage. The longest computation was 21.1 seconds; the measured extension runs used about 76–80 MB peak RSS. No computation approached the five-minute or 1 GB limits.')
put()
put('The four load-bearing points are: (i) the cut representation transfers stationary forms, with gamma_M >= gamma_B, rather than pathwise polymer lumping; (ii) cyclic invariance eliminates degree one, and the strict forward-ratio estimate puts every degree at least two strictly above gamma_Q; (iii) singleton count fibers plus reversibility give exact polymer endpoint TV identities; and (iv) the arbitrary-start mixing proof bounds the actual polymer density through instantaneous energies and positivity, without assuming that polymer lifts evolve under the cut semigroup.')
put()
put('## Verdict table')
put()
put('Proof-step details, including the arithmetic behind these reasons, are in `LOG.md`. “CORRECT” for an application of an external theorem means the quoted theorem implies the claim with the hypotheses and normalization given; see the source-verification limitations below.')
put()
verdicts=[
('introduction: fragmentation/coagulation rates','The unequal/equal split and pair factors match the verbal model.'),
('introduction: stationary law, irreducibility','Factorial detailed balance; all states connect through monomers.'),
('[thm:main], [cor:regimes]','Upper certificate and exhaustive lower-bound patching give the stated constants.'),
('[proof:prop:comparison]: multiplicity and pushforward','Distinguished-cut counting gives n(k-1)!/prod m_j!.'),
('[proof:prop:comparison]: averaged rates and form equality','Uniform cyclic multiset ordering gives the polymer conductances exactly.'),
('[proof:prop:comparison]: gap direction','Lifted functions form a subspace, so gamma_M >= gamma_B.'),
('[proof:lem:positive]','Positive ground state and extrema of v/h prove both signs correctly.'),
('Count chain, derivative intertwining, base bound','Discrete derivative identifies all nonzero Q eigenvalues with -A.'),
('[proof:prop:upper]','The reciprocal product trial has maximum <= beta+4max(sqrt(beta),1/n).'),
('[proof:lem:layers]: commutator/dimension','Adjoint injection/surjection gives binomial(n,ell)-binomial(n,ell-1).'),
('[proof:lem:layers]: lift norms/orthogonality/completeness','The U,D recursion proves norms, support, and the telescoping decomposition.'),
('[proof:lem:sectoraction]','Neighbor-lift sums give the exact birth, death and killing coefficients.'),
('[proof:prop:base]','Higher killing is large; the cyclic fixed degree-one coefficient vector vanishes.'),
('[proof:prop:squareroot]','Positive reciprocal quotients give sqrt(beta)/5 under the stated hypotheses.'),
('Completion of [thm:main], all exceptional parameter ranges','beta>=1/16, beta<=4/n^2, n<8 and the remaining region exhaust all cases.'),
('[lem:ground-ratio]','A minimum forward ratio <=1/2 contradicts adjacent eigenvalue equations.'),
('[prop:higher-exact]','The shifted ground-state certificate is strictly above gamma_Q.'),
('[thm:exact-gap]','Rotation-invariant lower bound and count-function upper bound agree.'),
('[thm:sharp-gap]: a>1 and endpoint brackets','a(a-1)=beta*n(n+a+1); the quotient increases in k.'),
('[thm:sharp-gap]: additive error','d+1/n<=c<=d+4/n and subtraction <=6/n give d-5/n and d+4/n.'),
('[cor:sharp-equivalents]','The additive error is negligible in the claimed regimes; a->1 at the small end.'),
('[prop:critical-operator]','Closed core form, compact embedding, positive simple minimizer.'),
('[lem:critical-ground-ratios]','Order coupling plus the h0 transform gives both ratios; nonexplosion is justified.'),
('[thm:critical-limit]','The finite correction to the restricted infinite ground state lies in [-b/n,b/n].'),
('[prop:critical-lipschitz]','Bounded cross-parameter ground states lie in the operator domain; pairing is valid.'),
('[prop:critical-truncation]','Only the last birth changes; its quotient error is <=2b/(R+3).'),
('Degree-one critical form construction','Killing j still gives compact tails; zero form energy is impossible.'),
('[prop:critical-degree-one]','The transformed ratio gives the signed finite error and the bounds on sigma.'),
('[cor:critical-end-asymptotics]','Reciprocal bounds squeeze sigma; sharp count bounds squeeze rho.'),
('[eq:critical-sigma-truncation]','The last-birth error is <=b/(R+2).'),
('[cor:critical-spatial-limit]','Minimum is 1-Lipschitz; both radial approximations have error <=b/n.'),
('Count cutoff definition and window','The claimed fixed-epsilon times imply standard cutoff and an upper window bound.'),
('Count strong lumping and polymer endpoint TV identity','Singleton fibers and reversible evolution keep endpoint densities count-measurable.'),
('Count stationary estimates','Ratio differentiation gives central Gaussian estimates and geometric outer tails.'),
('Count hitting means, both endpoints','Passage recurrences plus reciprocal drift sums give tn+O_b(sqrt(n)).'),
('Count hitting variances, both endpoints','Independent passages and cumulative-tail estimates give O_b(n).'),
('[thm:count-cutoff]: worst-case upper bound','The quoted birth-death theorem applies after the exact time rescaling.'),
('[thm:count-cutoff]: endpoint lower bounds','Central-target hitting times have controlled means/variances; Chebyshev suffices.'),
('Separation cutoff consequence','The quoted separation theorem uses the sum of endpoint hitting means; fibers transfer it.'),
('[thm:full-polymer-tv-upper-new]: degree bound','Rising-factorial trials give lambda_ell >= ell*sqrt(beta)/6.'),
('[thm:full-polymer-tv-upper-new]: count density','The logarithmic Lyapunov inequality yields M(t)<=C_b sqrt(bn).'),
('[thm:full-polymer-tv-upper-new]: low-degree positivity estimate','Permutation-invariant PSD projectors have uniformly bounded entries on a slice.'),
('[thm:full-polymer-tv-upper-new]: energy integration','The energy inequality first reduces log R, then the gap mixes a polynomial density.'),
('[thm:full-polymer-tv-upper-new]: every start','All density and count estimates are uniform over the initial partition.'),
('[eq:spatial-generator] and equilibrium','Nonempty-subset reactions and symmetric swaps preserve the stated weight.'),
('[thm:spatial-exact-gap]','Harmonic tensor sums; higher sectors already exceed the count gap.'),
('[prop:spatial-degree-one-sharp]','The exact reciprocal quotient is increasing, with positive denominators for all a>0.'),
('[cor:spatial-leading-constants]','Combine additive errors inside the minimum; nm>=n sqrt(beta).'),
('[prop:spatial-degree-one-scale]','Two trial upper bounds, auxiliary lower bounds, and parameter patching give u/8<=eta1<=u.'),
('[eq:spatial-degree-one-below-count]','Subtract the two operators and use inverse ground ratios <=2.'),
('[cor:spatial-uniform-gap] and rare/cycle/torus cases','Take the minimum of the proved count and degree-one scales.'),
('[cor:spatial-inhomogeneous] and the example','Compare undirected reaction conductances against a_- B and a_+ B.'),
('[thm:nonreversible]: invariance and asymptotic rate','Unitary permutation actions are dissipative; tensor spectral sums remain valid with Jordan blocks.'),
('[thm:nonreversible]: contraction exponent','The symmetric-part gap is sufficient by differentiation and necessary at time zero.'),
('Nonreversible three-coordinate example and product extension','Characteristic polynomials give the stated 5/2 and 2 rates.'),
('[lem:simple-polymer-gap]','Strict higher-sector separation and the simple derivative ground state force a simple count mode.'),
('[prop:polymer-circulation]: rates, invariance, symmetric part','A divergence-free antisymmetric stationary current preserves all three properties.'),
('[prop:polymer-circulation]: strictness','An eigenvector attaining the symmetric-part gap would have to be g, but Ag is nonzero and orthogonal to g.'),
('[eq:circulation-perturbation]','Simple-eigenvalue perturbation gives the positive quadratic coefficient; adjoint symmetry makes the branch even.'),
('[thm:kernel-comparison] and unbounded stationary representation','Both reaction directions share a multiplier; compare forms with the same variance.'),
('[prop:ewens-classical]','The quoted classical spectrum has its least nonzero value at (n-1,1), in the stated units.'),
('[prop:growing-kernel-upper]: product drift and covariance','Exact monomer drift plus stochastic ordering of conditional nonmonomer counts.'),
('[prop:growing-kernel-upper]: additive bounds','Use i+j>=2 and i+j<=2ij in the common equilibrium form.'),
('Coupling appendix: Stage I and Stage II marginals','All joint events have the cut-chain marginals, including r=0.'),
('Coupling appendix: certificates and survival','Both killed generators have positive supersolutions at rate sqrt(beta)/5.'),
('Coupling appendix: concatenation and gap deduction','Uniform exponential moments concatenate by strong Markov; eigenfunctions force the gap bound.'),
('[eq:L2-decay], [eq:cov-decay], point-mass TV bound','Standard finite reversible spectral calculus with the stated constants.')]
table(['Statement or proof step','Verdict','Reason'],[(x,'CORRECT',y) for x,y in verdicts])

put('## Independent numerical evidence')
put()
put('These are floating-point spectral and ODE calculations, except where exact Fraction/SymPy checks are specified. No floating-point output is presented as a rigorous interval certificate. The mathematical arguments, rather than these grids, establish the all-parameter claims.')
put()
put('### 1 and 3(a): full polymer generators')
put()
put('Command: `python3 audit.py step13`. Every row passed exact rational detailed balance and graph-connectivity checks, simplicity of the gap, and strict monotonicity of its count eigenfunction. The function is constant on each count fiber to numerical precision. For n=2 there is no second positive eigenvalue against which to measure separation. Raw per-case separations and residuals: `step1_3a.json`.')
put()
r13=read('step1_3a.json')
direct=read('count_direct_checks.json')
direct_small={(x['n'],x['beta']):x['gap_Q_direct'] for x in direct['small']}
table(['n','beta','states','gamma_M','gamma_Q (direct)','absolute difference'],[(x['n'],x['beta'],x['states'],x['gap_M'],direct_small[x['n'],x['beta']],abs(x['gap_M']-direct_small[x['n'],x['beta']])) for x in r13])
put(f"Maximum absolute polymer/direct-count gap difference: {max(abs(x['gap_M']-direct_small[x['n'],x['beta']]) for x in r13):.4g}. The minimum separation from the next positive eigenvalue, where present, is {min(x['simple_separation'] for x in r13 if x['simple_separation'] is not None):.6g}. Maximum absolute within-count eigenfunction residual: {max(x['count_residual'] for x in r13):.4g}.")
put()
put(f"Additional command: `python3 audit_count_direct.py`. This builds Q from its original birth/death rates and computes its first positive eigenvalue directly, as well as checking the derivative version. Maximum direct-Q/derivative discrepancy is {direct['max_small_error']:.3g} in the 36 small cases and {direct['max_large_error']:.3g} in the 56 large cases, both below 1e-9. Exact count lumping of the full polymer generator and the matrix equation derivative*Q=A*derivative pass in all 36 rational cases. Raw data: `count_direct_checks.json`.")
put()
put('### 3(b): large count grid and bound slacks')
put()
put('Same command. The symmetric derivative tridiagonal matrix has exactly the nonzero Q spectrum, avoids subtracting the stationary zero eigenvalue, and has dimension n-1. All requested values are included, including duplicate numerical parameters such as 1e-6=n^-2 when n=1000. `step3b.json` stores unrounded values.')
put()
r3=read('step3b.json')
table(['n','beta','gamma_Q','sharp lower','sharp upper','eta1 (used in 7)'],[(x['n'],x['beta'],x['gap_Q'],x['sharp_lower'],x['sharp_upper'],x['eta1']) for x in r3['rows']])
put('A slack is actual-minus-lower or upper-minus-actual. The worst (smallest) slacks are:')
put()
table(['Inequality','minimum slack','n','beta'],[(name,x['slack'],x['n'],x['beta']) for name,x in r3['minimum_slacks'].items()])
put('There is no failed inequality. The -1.14e-13 sharp-lower value and -1.11e-16 elementary-lower value occur at n=2, where the relevant formulas are exact equalities and gamma_Q=beta+1. Their signs are rounding artifacts, confirmed by that independent exact two-state calculation.')
put()
put('### 4: critical function and finite-size comparison')
put()
put('Command: `python3 audit.py step4`. To make the paper\'s truncation width less than 1e-6 requires the R below. A direct array at R=200,000,001 would exceed the resource limit. Instead, the program evaluates rho_R by bounding the omitted tail of J_R with a Schur complement and diagonalizing only 80 coordinates. For k>=M+1 the tail diagonal minus absolute off-diagonal row sum is at least (M+2)(M+1-2sqrt(b)), including the reflecting last row. If U=2+b/2, the last-coordinate Schur correction to the leading block lies in [0,bM(M+1)/(tail_lower-U)]. Smallest eigenvalues of the two leading-block endpoints bracket rho_R in exact arithmetic. The numerically evaluated endpoint differences are at most 5e-13, and sometimes round to zero. This also localizes the infinite eigenvalue; the width shown below is the paper\'s more conservative analytic truncation error. Rounding is not interval-certified. `step4.json` contains the endpoints.')
put()
r4=read('step4.json')
table(['b','R','rho_R approx.','2b/(R+3)','2+b/2'],[(x['b'],x['R'],x['rho_R'],x['truncation_width'],2+x['b']/2) for x in r4])
table(['b','n','n gamma_Q(n,b/n^2)','difference from rho approx.','allowed b/n'],[(x['b'],y['n'],y['n_gap'],y['error'],y['error_bound']) for x in r4 for y in x['finite']])
put('All computed values satisfy 2<rho<=2+b/2. Every ordered pair among these b values satisfies 0<=rho(b2)-rho(b1)<=(b2-b1)/2 (checking adjacent pairs already implies the others). All twelve finite-size comparisons pass with substantial slack.')
put()
put('### 5: endpoint count TV profiles')
put()
put('Commands: `python3 audit.py step5` and `python3 audit_uniformization.py`. The table below uses uniformization: a nonnegative Poisson series for tridiagonal transition matrices. Adaptive upper-state truncation uses killed subgenerators, so removed trajectories and omitted Poisson terms lose probability mass; the total mass defect is <=2.02e-13, apart from roundoff. An independent sparse BDF evaluation of q\'=Q^T q (rtol=2e-9, coordinate atol=2e-13) agrees in TV within 5.68e-9 over the entire grid. BDF mass error is <=7.2e-15, and a tighter-tolerance rerun at b=0.5,n=400 changes TV by <=1.88e-9. Uniformization took 1.43 seconds. Data: `step5_uniformization.json` and `step5.json`. All entries below are at tn+c sqrt(n). A dash means a negative time, for which TV is undefined; it does not mean zero or time zero.')
put()
r5=read('step5_uniformization.json')['rows'];groups=sorted({(x['b'],x['n'],x['start']) for x in r5})
table(['b','n','start','c=-4','-2','-1','0','1','2','4'],[(b,n,start)+tuple(next((f"{x['tv']:.8f}" if x['tv'] is not None else '—') for x in r5 if (x['b'],x['n'],x['start'],x['c'])==(b,n,start,c)) for c in (-4,-2,-1,0,1,2,4)) for b,n,start in groups])
put('The positive-time entries are consistent with an O(sqrt(n)) transition window around tn: the distance at c=0 remains of constant order while fixed positive shifts reduce it substantially, and the two endpoints have similar limiting behavior. These small-to-moderate n data cannot prove cutoff or an optimal window. The requested grid poorly samples the pre-cutoff side: c=-4,-2 always produce negative times here, and for b=2 even c=-1 is negative for all four n. Thus this table gives very limited evidence for the left tail; the hitting-time lower bound, rather than the table, supplies that part of the theorem.')
put()
put('Rejected numerical diagnostic: `audit_exponential.py` attempted contour inversion of the tridiagonal resolvent. It produced nonphysical values and catastrophic cancellation for sharply concentrated high-count initial data; an initial dense-exponential cross-check also produced nonfinite output. Those results were rejected and do not appear in the table. Positive uniformization and the independent BDF solver resolve the calculation without that unstable route. This is a failure of an exploratory numerical method, not evidence against the paper.')
put()
put('### 7: full spatial generators')
put()
put('Command: `python3 audit.py step7`. State space is the 2^n-1 nonempty subsets, not the full Boolean cube. Each row below represents four separately built full generators. The unequal graph is a path with edge weights 1/3,2/3,...,(n-1)/3. Each entry was compared with min(gamma_Q,eta1+D lambda_G), using an independently built graph Laplacian and the degree-one radial operator. All 160 comparisons pass; maximum absolute error is 1.67e-13. Full per-D data: `step7.json`.')
put()
r7=read('step7.json')
groups7=sorted({(x['n'],x['beta'],x['graph']) for x in r7['rows']})
tab=[]
for n,b,g in groups7:
    rs=[x for x in r7['rows'] if (x['n'],x['beta'],x['graph'])==(n,b,g)]
    tab.append((n,b,g,rs[0]['lambda_G'])+tuple(next(x['gap'] for x in rs if x['D']==D) for D in (0.,.1,1.,10.))+(max(x['error'] for x in rs),))
table(['n','beta','graph','lambda_G','gap D=0','D=0.1','D=1','D=10','max error'],tab)
put('The degree-one endpoint, additive, scale, auxiliary and below-count bounds were also tested on every one of the 56 cases of 3(b):')
put()
table(['eta1 inequality','minimum slack','n','beta'],[(name,x['slack'],x['n'],x['beta']) for name,x in r7['minimum_slacks'].items()])
put('The tiny negative slacks are rounding at n=2 exact equalities: eta1=beta and gamma_Q=beta+1. No inequality failure was found.')
put()
put('### 8: stationary polymer circulation')
put()
put('Command: `python3 audit.py step8`. In each case epsilon is half the smallest of the four normalized stationary conductances, strictly inside the allowed range. Nonnegativity, row sums, invariance, and equality of the symmetric part with L_M were checked exactly with fractions. “Spectral rate” means the smallest real part of a nonzero eigenvalue of -L_epsilon; equivalently the negative of the largest nonstationary real part for L_epsilon. All improvements are strict.')
put()
r8=read('step8.json')
table(['n','beta','epsilon','gamma_M','spectral rate','increase'],[(x['n'],x['beta'],x['epsilon'],x['gap'],x['spectral_rate'],x['improvement']) for x in r8])
put('The proof of strictness is complete for every admissible nonzero epsilon: equality in the symmetric-part Rayleigh inequality would force the eigenvector into the simple gap eigenspace, but A maps its generator out of that space. Perturbation theory is only needed for the later quadratic expansion, not for strictness itself.')
put()
put('### 9: Ewens and shared growing kernels')
put()
put('Command: `python3 audit.py step9`. Each row includes a directly constructed Ewens generator, a shared-product generator and a shared-additive generator. Exact detailed balance and product monomer drift pass. Every product/additive bound passes. Maximum Ewens gap/formula error is 2.49e-14; comparison of every eigenvalue against the quoted partition-indexed spectrum gives maximum error 1.85e-13. These are different equilibria: Ewens fragmentation uses beta(i+j); the shared-product fragmentation uses beta*ij.')
put()
r9=read('step9.json')
table(['n','beta','Ewens gap','2beta+2(n-1)/n','product gap','additive gap'],[(x['n'],x['beta'],x['ewens_gap'],x['formula'],x['product_gap'],x['additive_gap']) for x in r9])
put('### Second derivations and coupling checks')
put()
put('Command: `python3 audit_algebra.py`. The independent symbolic checks cover the upper, square-root, higher-sector, sharp count, sharp degree-one, critical finite-size, rising-factorial and coupling certificates, the tower recursion, and the Lyapunov fourth-power identity. The program also checks the stationary projected generator by enumerating cyclic cut sets, and constructs both coupling marginals event by event.')
put()
ra=read('algebra_checks.json')
table(['Check','coverage/result'],[
    ('Exact symbolic identities',len(ra['symbolic_identities'])),
    ('Exact stationary projection entries',ra['projection_entries']),
    ('Full cut spectrum vs radial union',f"{ra['spectral_cases']} cases through n=8; max error {ra['max_spectrum_error']:.3g}"),
    ('Exact Stage-I coupling marginals',f"{ra['coupling_pairs']['I']} pairs through n=7"),
    ('Exact Stage-II coupling marginals',f"{ra['coupling_pairs']['II']} pairs through n=7")])
put('The appendix is a complete proof independent of harmonic decomposition under n>=8 and 4/n^2<=beta<=1/16. Its finite constants may depend on n,beta, which is harmless for extracting the exponential spectral rate. It does not by itself cover all n,beta; the main proof supplies that parameter patching.')
put()
put('## Attribution and novelty: memory only')
put()
put('I remember Granovsky and Erlihson\'s solvable coagulation–fragmentation work, and Durrett, Granovsky and Gueron\'s reversible equilibrium work. Confidence is moderate for the former and moderate to high for the latter. I do not independently remember the exact location or wording of the announced gap equality; the manuscript itself credits it, and its present proof does not require that announcement. Equality of gaps alone therefore should not be advertised as a new discovery.')
put()
put('I remember Aldous\'s coagulation–fragmentation relaxation questions and cycle representation with moderate confidence. The exact webpage dates and precise original question have not been checked. The Ewens/Metropolis transposition spectrum is classical; Jiang is a plausible direct source and is explicitly credited. I do not claim, from memory, that Jiang was the earliest source of every version of that formula.')
put()
put('I do not recall an existing paper with this exact critical function or the stated b/n cutoff. That does not establish novelty. Granovsky–Zeifman\'s N-limit spectral-gap work in particular needs source examination before any priority claim about fixed-beta asymptotics. No literature priority claim was inferred from a failed recall.')
put()
put('The familiar DGG, Caputo–Liggett–Richthammer, Chafai–Joulin, Filmus, Hwang–Hwang-Ma–Sheu, Levin–Peres and Jiang bibliography entries look plausible in author/title/year/journal. I found no definite metadata error from memory. The 2026 research items, repository citations, URLs, precise pagination and quoted theorem/equation numbers remain unverified. I did not invent a replacement reference.')
put()
put('## Typos, unclear wording, and missing material')
put()
put('No demonstrated mathematical typo was found. These are the source and clarity issues noticed:')
put()
table(['Location','Quoted text','Issue / suggested clarification'],[
    ('introduction.tex; PAPER.tex:279',r'`\input{related_work}`','The referenced file is absent and not concatenated, so the literature section is missing from this audit copy.'),
    ('proof.tex; sector-action proof',r'“Both radial boundary coefficients ... are zero.”','Say “the outward coefficient at each endpoint is zero” to avoid suggesting that both birth and death vanish at each endpoint.'),
    ('critical_scaling.tex; [prop:critical-degree-one]',r'“It is increasing”','Specify whether this means nondecreasing or strictly increasing. The proof explicitly establishes monotonicity; strictness also follows by positive ground-state pairing because the ground state is nonconstant.'),
    ('count_cutoff.tex; opening paragraph',r'“The time-window statements below imply cutoff”','A brief explicit statement of the double-limit cutoff criterion would help readers. The fixed-epsilon mixing-time assertion is already sufficient.'),
    ('appendix_computations.tex',r'“The accompanying program” / “Source data ... accompany the paper”','Those programs, result files and the figure are absent from this folder. Their claimed historical output was not checked; independent replacements were written.'),
    ('main.bbl attachment; PAPER.tex:3626 onward',r'`\end{document}` before `BEGIN FILE main.bbl`','The compiled bibliography is appended for audit and would not be processed by TeX in this position. This is a packaging observation, not a mathematical defect.'),
    ('acknowledgments.tex',r'“The final manuscript was audited by Claude Opus 5.5”','A process declaration that cannot be independently verified from the supplied source; it supplies no mathematical evidence for this report.')])
put('The date, source line numbers and external-file packaging refer to the supplied concatenation, not an independently fetched public release. No source changes were made.')
put()
put('## What could not be checked')
put()
put('- The absent `related_work.tex`, public PDF/figure, author programs/data, funding statements, and earlier AI audit declarations.\n- The exact statements/numbering in Chen–Saloff-Coste (worst-case TV and separation cutoff) and Jiang (classical spectral formula). Their supplied quoted forms were audited for applicability; external source authentication was prohibited.\n- Comprehensive novelty, priority, URLs and recent bibliography metadata.\n- TV at negative times in the requested numerical grid: these quantities are undefined.\n- Rigorous floating-point rounding intervals. Exact rational and symbolic checks are rigorous arithmetic; numerical eigenvalues and the ODE solution are not certified interval calculations.\n- An optimal cutoff window or worst-case polymer cutoff, neither of which the manuscript claims.')
put()
put('No requested mathematical section was left unread. The internal mathematical verdict is SOUND, with the external-source and novelty qualifications above.')
put()
now=datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %z')
put(f'Task: “Be a hard, independent referee” of PAPER.tex — report completed {now}. The original request clock timestamp was not supplied.')
Path('REPORT.md').write_text('\n'.join(out)+'\n')
print('Wrote REPORT.md:',len(verdicts),'verdict rows;',len('\n'.join(out)),'characters')
