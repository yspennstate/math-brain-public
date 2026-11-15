VERDICT: PARTIAL a polynomial ceiling for the direct local-hardness hyperplane-incidence certificate

PROOF.md proves a limitation of one concrete route to T301. Let a globally L-Lipschitz target be evaluated under a mixture of distributions supported in balls. Suppose the ball centers have projected span D in some unit direction. If each component has squared depth-2 approximation hardness at least epsilon^2, against width at most v with unrestricted parameters, the usual first-layer-collapse union bound can certify a depth-3 first-layer width threshold no larger than

    (1-eta^2/epsilon^2)(1+LD/(2epsilon)),

for target L2 approximation error eta < epsilon. This holds for arbitrary mixture weights, radii, overlapping balls, and number of components.

The extension allows different local hardness levels epsilon_i, including zero. With beta = sum_i p_i epsilon_i^2 > eta^2, its certified threshold is at most

    (1-eta^2/beta)(4/3)(1+LD/sqrt(beta)).

A depth-4 target with entry bound B and hidden widths n1,n2,n3 has Lipschitz constant at most B^4 sqrt(d)n1 n2 n3. Thus polynomial target weights, widths, center span, and inverse total hardness scale give a polynomial ceiling for this certificate. This is not a lower bound or upper approximation theorem for the unrestricted problem. No claim of priority for the lemma is made.

The argument combines two elementary facts: a ball carrying constant local hardness cannot have radius smaller than that error scale divided by L; parallel hyperplanes averaged over their offsets must meet a substantial fraction of balls. The weighted extension retains at least three quarters of the local hardness energy. Every proof step and the restrictions on layer collapse are in PROOF.md.

Verification command, run from this folder in PowerShell:

```powershell
$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; (Get-Process -Id $PID).PriorityClass='BelowNormal'; python -B verify.py
```

The script also sets its own Windows priority to BelowNormal. It uses only standard-library exact arithmetic and small bounded loops. Final output is PASS: 750 equal-radius incidence cases, 750 unequal-radius cases, 1,024 Lipschitz-coefficient cases, 35 variance identities, 41 explicit layer-collapse evaluations, 886 variable-hardness inequalities, and 20 checks of the 4/3 constant: 3,506 checks total. The final run took 10.113585 seconds, with peak working set 25,542,656 bytes and peak pagefile usage 16,998,400 bytes. Data: verification.json. These checks validate the formulas and edge cases; they do not exhaust high-dimensional network configurations.

Attempts to break the result included unequal hardness levels, vanishing local hardness on some components, repeated projected centers, touching endpoints, overlapping balls, and zero input weights. Independent derivations of the radius and Lipschitz bounds are included. LOG.md records the exact commands and outputs.

What failed: no qualifying full solution was found in the bounded literature search, and no depth-4 versus depth-3 approximation separation is proved here. Merely using more replicated balls, nonuniform weights, or nonuniform local hardness does not remove this certificate's scale obstruction.

Resource breach: the external math-recall helper, run with logging disabled and the slow recall profile, was observed at 2,451,382,272 bytes of working set, exceeding the 1 GB limit. It exited before a targeted stop took effect. No further recall was run. This was separate from verify.py; the final verification also records its own peak memory. The helper must not be reused under this resource budget without an enforced memory limit.

Literature correction: LITERATURE.md and SOLVED_ELSEWHERE.md record Itay Safran's arXiv:2608.23877v2, which provides an adjacent-depth approximation hierarchy at exponential input radius and an exact separation on the cube. The paper predates the supplied November status and corrects an incomplete baseline. LITERATURE.md also corrects the source conflation and the scope of the cited circuit barrier: Vardi--Shamir's stated barrier starts at shallower depth 4, not 3. SOLVED_ELSEWHERE.md explicitly says that the whole T301 specification was not verified as settled.

Uncertainty: "natural distribution" is unspecified in T301. The recent hierarchy is substantial progress if one allows an engineered distribution at exponential radius, but its theorem was not verified to provide polynomial individual target weights. The present ceiling concerns only the displayed weighted union-bound certificate and local hardness against unrestricted depth-2 parameters. It leaves open methods exploiting bounded collapsed weights, different patch geometry, or collective constraints on several hyperplanes.

Next worker: seek a way to use interactions between several first-layer activation hyperplanes, rather than only their maximum individual incidence, or quantify a bounded-parameter local obstruction that survives layer collapse. Specify the input distribution and depth convention before comparing any candidate with the literature. A direct rescaling of the copied-ball incidence argument is insufficient under the assumptions proved here.
