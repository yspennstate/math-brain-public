# Research log

Task: “prove one explicit spectral inequality on weighted graphs, or to find a counterexample, or failing both to prove the strongest rigorous partial result you can.” Received 2026-11-12; work began 23:12 Asia/Tbilisi.

## 1. Orientation and resource checks (23:13)

All four requested modules are installed in the specified Python 3.13: numpy, scipy, mpmath, sympy. The compute governor reports warning / CPU saturation. All experiments will use one thread, nice 15, small matrices, and a hard wall-time budget below five minutes per invocation. No agents, network, pushes, or visible windows.

The current task's explicit restriction to mutations inside this folder overrides the usual external checklist, mesh, and brain writes. This log is the local task record. Existing scripts have been read as leads; independent verification code will not import them. Initial reading confirms that the supplied trace script uses a tolerance to identify the top eigenspace; numerical conclusions must therefore record the actual relative gap.

No mathematical conclusion yet.

## 3. Algebraic reductions and immediate theorems

CHECKED algebra. The product p has zero sum, since u and v are orthogonal. The claimed projection norm is obtained by projecting the symmetric matrix (uv^T+vu^T)/sqrt(2) onto symmetric matrices with zero diagonal and zero row sums; details will be in RESULT.md. The trace identities in the source re-derive directly as S2=tr(Pi circ G), S3=tr(L(Pi circ G)), with circ denoting entrywise product.

Writing X1=D sum_e w_e gamma_e and Y=2 sum_e w_e tau_e gamma_e proves the claim whenever 2 tau_e <= D on every positive-weight edge. In particular this proves every D>=4 graph, and every graph with constant projector diagonal when n>=8: Pi_ii=D/n implies tau_e<=4D/n. These conclusions are exact, not numerical.

Next route: all circulants. Only n=5,6,7 remain after the constant-diagonal theorem. In a fixed Fourier top-eigenspace sector, lambda and G are linear in the distance-orbit masses, Pi is constant, and the target T is a quadratic polynomial. Thus a finite exact quadratic certificate over the spectral sector polygon may finish these cases.

Resource note: the sandbox denied nice/setpriority, although Python executed; numerical work still has all BLAS thread counts fixed at one, uses only tiny matrices, and has a 110-second internal deadline.

## Audit implementation correction

The first independent certificate audit stopped before checking any point: SymPy's algebraic-field from_sympy method requires a SymPy Integer, not a Python int. This is an audit harness type error, with no effect on the completed exact certificate calculation. Correcting it and rerunning.

## 6. Scope and remaining obstruction

The exact certificates prove all weighted circulants on n>=5 that lie on the stratum. For n>=8 the proof is the projector bound, and for n=5,6,7 the explicit sector certificates have nonnegative coefficients. Ties were included: n=6 needs the D=3 sectors {1,3} and {2,3}; D>=4 ties use the general theorem. The n=5 sector also gives the sharp ratio bound attained at the five-cycle.

The direct edge argument does not resolve arbitrary D=2 or D=3: it requires tau_e<=D/2, whereas every cycle edge at C5 has tau_e=2 lambda>1. Replacing gamma by its norm bound also fails to close even C5, as in the prompt. No unrestricted proof or counterexample has been obtained. The final result will state this limit explicitly.

## 2. Independent numerical reproduction

NUMERICAL. 18 records saved in numerical_reproduction.json; pair definitions and trace identities agree. No ratio above one. Runtime 0.39 seconds.

## 4. Exact small-circulant certificates

[True, True, True, True, True, True]; runtime 0.8911053329939023 seconds. Exact coefficients saved in circulant_certificate.txt.

## 4. Exact small-circulant certificates

[True, True, True, True, True, True]; runtime 0.7333242919994518 seconds. Exact coefficients saved in circulant_certificate.txt.

## 5. Independent certificate audit

NUMERICAL cross-check of exact identities at all 46 vertex pairs/midpoints, using real Fourier eigenvectors and the original P,Q definitions rather than the trace formula. Maximum absolute discrepancy 3.608224830031759e-16. Exact positivity itself uses rational interval lower bounds, not these floating-point checks.

## 7. Final proof audit and deliverable (23:22)

RESULT.md now contains the complete self-contained partial theorem and proof: all D>=4 graphs; constant-diagonal top projectors for n>=8; all weighted circulants for n>=5; and the sharp five-vertex circulant ratio. The n=6 eigenvalue inequalities and n=7 polygon inequalities were checked against the Fourier formulas. A separate exact SymPy calculation confirms Q(s)=(1-s)8sqrt(5)/25 in the five-vertex family. Direct rational evaluation confirms the stated bracket for the positive cubic root at n=7.

Repeated certificate output blocks from the independent audit were deduplicated; one exact record per sector remains. The log retains all attempts. Final numerical sample: 15 random points, maximum relative gap below 1.4e-14 and maximum ratio 0.8113380332. No counterexample candidate triggered the 50-digit verification condition.

Done within the requested partial-result alternative. Arbitrary D=2 and D=3 graphs are still unresolved; no unrestricted claim is made. No external writes, pushes, agents, browser, or visible windows.
