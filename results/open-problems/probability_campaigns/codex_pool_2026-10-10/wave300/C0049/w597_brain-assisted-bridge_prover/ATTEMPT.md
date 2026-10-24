# C0049: conditional martingale bridge

2026-10-10. Scope: mathematical bridge only. C0049 remains unproved here; current openness UNKNOWN. No novelty claim. Independent statement was prepared first in STATEMENT.md; delivery retry is pending because team_comm requires an explicit team.

## Prior attempt and correction of the reduction

The exact local intake row is problems.jsonl:49, source_id duminil_copin_ising_potts_2017, locator Conjecture 3, p.93. The prior attempt is attempts.jsonl:39, C0049-A001. It identifies the missing additional control on the general-q parafermionic observable. Its assertion that the problem is reduced *exactly* to one extra discrete relation is too strong without compactness, boundary identification, convergence in random explored domains, and martingale uniform integrability. Finding that relation might be one route, but is not a logically established equivalence.

The equivalent older primary-source formulation, Conjecture 4.20 in the IHES lecture PDF, is in STATEMENT.md. The original 2017 locator still needs its exact PDF checked. H/I exact-ID searches returned no C0049 attempt. The Lean campaign lists the candidate as attempted_un; no formal proof receipt was located. Team O holds the adjacent C0050 observable problem (w339) and duplicate P0124 interface problem (w341); our proposed lane is the stochastic passage/identification bridge.

## Lemma L1: recover the driver rather than assume it is a semimartingale

Fix 0<sigma<=1. Let W be a real continuous adapted process with W_0=0 on a filtration satisfying the usual conditions. Let g solve the capacity-normalized chordal Loewner ODE partial_t g_t(z)=2/(g_t(z)-W_t). Fix z in H and work strictly before its swallowing time, with compact stopping as needed. Set Z_t=g_t(z)-W_t and J_t=g'_t(z). Choose the continuous logarithm L_t=log(J_t/Z_t), starting at a fixed branch at time zero, and set M_t=exp(sigma L_t). Assume its real and imaginary parts are local martingales in this filtration.

Then W is a continuous semimartingale on this stochastic interval. In its locally canonical decomposition W=N+A, with N a real continuous local martingale starting at zero and A real continuous finite variation starting at zero, we have

dA_t=0, and d<N>_t=8/(1+sigma) dt.

Proof, awaiting independent review:

1. On compact stops, g_t(z) and J_t are continuous finite variation processes. Indeed dJ_t=-2 J_t/Z_t^2 dt. Neither J nor Z vanishes, and Im Z>0. The map M is a nonzero complex local martingale.
2. Locally along the continuous path of M, choose a smooth analytic inverse branch R(M)=M^(-1/sigma) consistent with L. Branches can be continued with stopping; their derivatives are locally bounded. Complex Itô calculus (equivalently two-dimensional real Itô calculus) makes R(M) a semimartingale. Its chosen branch equals Z/J. Therefore W=g-J R(M) is a real continuous semimartingale. This step avoids assuming precisely the regularity being identified.
3. Apply Itô after writing W=N+A. Direct differentiation of M=J^sigma Z^(-sigma) gives

dM/M=(sigma/Z)dN+(sigma/Z)dA+(sigma/Z^2)[(1+sigma)/2 d<N>-4dt].

4. The last two terms have finite variation. Uniqueness of the continuous semimartingale decomposition, since M is a local martingale, makes their sum zero. Multiply the zero complex measure by Z^2/sigma to obtain

Z dA+[(1+sigma)/2 d<N>-4dt]=0.

5. The bracket and dt measures are real. Taking imaginary parts gives (Im Z)dA=0. Im Z is continuous and strictly positive on every compact stop, so dA=0 even if A initially has singular variation. The real part then gives the displayed bracket. No independence or unjustified product of conditional estimates is used.

Only a conditional characterization is proved: this does not establish that an FK observable converges to M.

## Lemma L2: probes that survive a deterministic time horizon

For z=iy and any continuous real driver, write g_t(z)=X_t+iY_t. Until swallowing,

partial_t(Y_t^2)=-4Y_t^2/[(X_t-W_t)^2+Y_t^2]>=-4,
so Y_t^2>=y^2-4t.

Consequently any y>2 sqrt(T) survives the full interval [0,T]. If the hypothesis of L1 holds at each probe z_j=i*2^j, j=1,2,..., then for every T one of these probes survives past T. Continuous W is bounded on each finite horizon almost surely, and compact localizations exhaust that horizon. L1 yields W a local martingale with bracket kappa t there. Lévy's characterization gives W=sqrt(kappa) B globally. This identifies the Loewner law, assuming the Loewner/curve convergence gates. One probe that might be swallowed does not by itself establish a global law.

## Single hardest unresolved gap

Prove joint convergence of normalized discrete observable martingales with the driver, in the exploration's random slit domains and after compatible compact stopping, with uniform integrability. Tightness plus a formula valid only in fixed deterministic domains is insufficient. The pending brain hypothesis comparison will specify which retrieved source supplies which gate.

NEXT: Retrieve full math-brain hypotheses, finish the martingale passage lemma and counterexamples, then send the frozen packet to w599.
