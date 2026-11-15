# T097 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First retained local clock reading: 15 November 2026, 10:48:09 +0400
(Asia/Tbilisi).

## Orientation and predecessor reading

Read REPORT.md, LOG.md and PROOF.md in the original, round 3, round 4
and round 5 folders. Discovered their files with
`OMP_NUM_THREADS=1 nice -n 15 rg --files <four predecessor folders> .`.
There are no mathematical scripts in these folders. Reads used
`OMP_NUM_THREADS=1 nice -n 15 cat <absolute paths>`; an oversized combined
output was truncated, so the round 3, 4 and 5 files were read separately.
The original proof was visible in the second read; its report will receive
a separate short read to avoid relying on truncated output.

Read startup identity through brain.py recall/node and the compute state.
The latter was ok / owner_away_open, with about 50 percent free memory.
The sandbox reports `nice: setpriority: Operation not permitted` even for
simple reads. No numerical workload will be launched. Work is analytic.
The folder-only instruction overrides external mesh, checklist and memory
updates. No git or subagents are used. No earlier folder is edited.

## Brief literature check

Used the web search tool for `Gaussian free field lattice critical
exponents 2026 level set percolation h star`, `2610.03703`, `2406.02397`,
and `Gaussian free field lattice critical exponent 2026 2025`.
Opened arXiv:2610.03703, arXiv:2406.02397 and the full HTML of
arXiv:2206.10724v2, and then re-opened the two abstracts together with
arXiv:2611.05357 to keep the scope check visible. No lattice solution
was found. The recent cluster papers concern metric graphs. The brief
search ends here; it does not certify novelty. Exact source statements
used below will be recorded in LITERATURE.md.

## Recheck underway

Round 5's main claim is the two-sided sandwich
`kappa R <= cap(B_R) <= kappa (R+1/2)` for SRW Green covariance.
Its other quantitative claim is the decrement
`486 pi^2 C_cube^2/(24+16 pi)^4` from a face-supported variation.
An independent energy calculation will be recorded before choosing and
proving the extension.

## Independent recheck: the round 5 result holds

For the upper sandwich, a different construction from cell averaging is
random shifted sampling. Given F=1 on Q_(R+1/2), let f_z(x)=F(x+z), with
z uniform in [-1/2,1/2]^3. Every f_z is finitely supported and equals one
on B_R. Tiling gives

    E_z E_Z(f_z) = (1/6) sum_i integral (F(y+e_i)-F(y))^2 dy
                <= (1/6) integral |grad F|^2.

The last inequality is Cauchy–Schwarz along a unit segment, followed by
translation invariance of the integral. Since cap(B_R)<=E_Z(f_z) for
every z, this proves the upper bound without averaging F first.

For the lower sandwich, write the trilinear interpolant as a sum of
products of one-dimensional tents. The one-dimensional mass symbol is
m(theta)=(2+cos theta)/3, because a tent has squared integral 2/3 and
overlap integral 1/6 with either neighbor. Its derivative symbol is
4 sin^2(theta/2). Thus the continuum gradient energy is the lattice
Fourier integral with multiplier

    (1/6) sum_i 4 sin^2(theta_i/2) product_(j!=i) m(theta_j).

Since 1/3<=m<=1, this is at most the lattice energy multiplier. The
interpolant equals one on Q_R. Scaling and the lattice variational formula
give kappa R<=cap(B_R). Both inequalities hold for every integer R>=1;
there is no asymptotic discretization assumption.

Rechecked the face decrement directly: the normal and tangential energies
on one face are 16/9 and 8/9, hence six-face energy 16. The negative cross
term has magnitude at least I0=216 pi C/D^2, D=24+16 pi. The fixed
amplitude b=I0/16 gives normalized improvement at least
I0^2/96=486 pi^2 C^2/D^4. Finite outer cutoffs make every trial admissible.

For the relative radius, optimized Gaussian likelihood moments give loss
t sqrt(2 a log(1/p))+a t^2/2. With a<=kappa(R+1/2),
log(1/p_R(h_*))<=(2+epsilon)log R and R=c/(t^2 log(1/t)), its leading
value is sqrt(8 kappa c) as epsilon decreases to zero. This independently
recovers the coefficient (log 2)^2/(8 kappa). The original report and round
5 AUDIT.md have now also been read separately. The earlier result holds.

Muirhead's opened Theorems 1.2 and 1.10 explicitly allow density exponent
q>4 in d=3 and subcritical stretched exponential decay. The endpoint q=4
is excluded, as the earlier workers correctly stated.

## Chosen extension, recorded before proof

Choose the connection-score direction, rather than another capacity
constant. Prove an exact reduction to the equilibrium-charge boundary
average. The anticipated structure is a Gaussian martingale M_R with
variance cap(B_R), independent increments outside the field already seen
in B_R, and an independent common-mode decomposition of the field in B_R.
Use it to replace the earlier uniform near-critical score target by a
single endpoint conditional-mean estimate at h_*. Derive the exact
constant that such an endpoint estimate would give for t^2 L_rel(t).

This is one reduction of the missing connection-specific estimate. It
does not assume the endpoint estimate or claim an exponent. The audit
will test whether nesting, monotonicity and the existing polynomial arm
lower bound could already imply it, by constructing nested increasing
events on the same Gaussian field. A counterexample there would locate
precisely why actual path geometry remains necessary.

Reason: the preceding capacity coefficient is already identified. The
new reduction can change the hypothesis needed to remove the logarithm,
and exposes the random quantity that a geometric argument must bound.
No computation is needed; all mathematical outputs will be full proofs.

## Exact identities and a stronger obstruction found

Let e_R=G_(B_R)^(-1)1, a_R=cap(B_R), and M_R=sum e_R(x) phi_x.
Last exit gives Cov(M_R,phi_x)=1 for x in B_R. Hence
Cov(M_R,M_S)=a_min(R,S), and M_S-M_R is independent of the entire field
in B_R when S>=R. Also e_R vanishes away from the inner boundary.
This verifies the proposed Gaussian boundary martingale exactly.

For A_R(h), Gaussian translation gives the exact identity

    p_R(h+t)/p_R(h)
      = exp(-a_R t^2/2) E[exp(-t M_R) | A_R(h)].

Consequently m_R(h)=-d/dh log p_R(h)=E[M_R|A_R(h)] and
m_R'(h)=a_R-Var(M_R|A_R(h))<=a_R. Jensen shows that a bounded normalized
endpoint mean m_R(h_*)/sqrt(a_R) is enough for a logarithm-free bound.
The independent common mode M_R/a_R makes the same mean an explicit
ratio of Gaussian density/tail averages of a residual path threshold.

The adversarial construction can do more than make this mean unbounded.
At sparse radii R_n=2^(2^(2^n)), require all earlier boundary martingales
to exceed 2 sqrt(a_(R_j) log R_j). These events are increasing and nested,
and have critical probabilities at least R^(-2-epsilon) eventually for
every epsilon>0. Positive association follows directly from independent
Gaussian increments. At each R_n the conditional score is at least
2 sqrt(a_(R_n) log R_n), and the exact translation identity gives a
half-ratio at t_n=(log 2)/(2 sqrt(a_(R_n) log R_n)).

Thus t_n^2 log(1/t_n) R_n tends to (log 2)^2/(8 kappa), while
t_n^2 R_n tends to zero. Together with the old universal lower bound,
this will prove its coefficient is sharp even with nesting and
monotonicity added. The construction concerns artificial events on the
same field, not lattice paths; it does not rule out a stronger arm bound.
This is the concrete extension pursued below: identify the exact
endpoint statistic and prove that the existing non-geometric information
cannot control it. Full details and separate audits are still required.

## Proof written

Created PROOF.md with full proofs of the boundary Gaussian martingale,
the exact conditional translation identity, the first two logarithmic
derivatives, the residual path-threshold formula, and the endpoint-score
criterion. If M=limsup m_R(h_*)/sqrt(cap(B_R)) is finite, the proved
conditional conclusion is

    liminf t^2 L_rel(t)
      >= (sqrt(M^2+2 log 2)-M)^2/kappa.

The missing hypothesis M<infinity remains unproved for actual arms.

The same proof constructs nested increasing events D_R on the actual
lattice Gaussian marginals and establishes exactly

    liminf t^2 log(1/t) L_D(t)=(log 2)^2/(8 kappa),
    liminf t^2 L_D(t)=0.

Their probabilities satisfy the same eventual lower bounds
R^(-2-epsilon) as the known arm input. This strengthens the earlier
non-nested half-space obstruction: even adding nesting and the exact
boundary martingale leaves the universal coefficient sharp. These are
not connection events, and the original exponent question is unchanged.

No mathematical script or numerical computation was run. The enormous
radii in the construction are symbolic integers, never allocated or
enumerated. All written objects are mathematical proofs in this folder.

## Independent and adversarial checks completed

Created AUDIT.md. The covariance is rechecked by cross-Green-matrix
multiplication. Expanding the exact conditional Laplace transform gives
the score and variance formulas independently of differentiating the
Gaussian density. Integrating the variance inequality also gives the
endpoint bound independently of Jensen. Completing the square and
rationalizing both verify its positive root and constant.

Re-derived the construction's polynomial probability lower bound by
requiring sufficiently large independent Gaussian increments, without
using positive association. The sparse radii make the extra cost
negligible in log R_n. A separate Gaussian bridge calculation gives the
same half-ratio upper bound as the likelihood identity. A general
threshold b^2=2 rho log R gives coefficient (log 2)^2/(4 rho kappa);
rho=2 independently reproduces the denominator 8.

Checked radii between the sparse selected ones, first-radius rather than
monotone-ratio logic, the liminf rather than limit conclusion, finite
small radii, whole-space events, the singular residual covariance,
Brownian time versus inverse time, finite positive event probabilities,
and the absence of any asserted independence between different residual
fields. The construction does not have to have a critical probability
exponent at every radius. It meets exactly the polynomial lower bound
used by the old method. The endpoint score bound remains unproved for
actual connection events, and the synthetic example is explicitly
distinguished from them.

Created LITERATURE.md listing only papers actually opened. A final direct
read of Muirhead's author line and equation (1.8) confirms the author
Stephen Muirhead and the SRW covariance normalization. No normalization
conversion or cable-system theorem is used.

Intermediate read-only check:

    OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md

Output at that point: LOG.md 178 lines, PROOF.md 423 lines, 601 total;
the usual sandbox priority warning preceded it. These counts predate
the final additions. No numerical script, simulation, decimal constant
evaluation, or workload followed the denied priority change.

## Final deliverable and verification

Created REPORT.md with verdict PARTIAL, distinguishing the proved
nested-event sharpness theorem from the unproved endpoint bound for
actual connections. Added the check that P(D_R) decreases to zero;
the obstruction does not rely on critical percolation. No exponent or
equivalence with a conventional correlation length is asserted.

Final independent read-only calls (run in parallel and all inspected):

```sh
OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
OMP_NUM_THREADS=1 nice -n 15 sh -c 'for f in LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; do
if test -s "$f"; then
printf "%s: present\n" "$f"
else
printf "%s: MISSING\n" "$f"
fi
done
wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md
head -n 1 REPORT.md
date "+%Y-%m-%d %H:%M:%S %z"'
OMP_NUM_THREADS=1 nice -n 15 rg -n -C 2 'These probabilities|sum_\(j=1\)|t_n=|a_n/R_n|This is a conditional|M=limsup|No estimate' PROOF.md REPORT.md AUDIT.md
```

Output that matters:

```text
nice: setpriority: Operation not permitted
LOG.md: present
PROOF.md: present
AUDIT.md: present
LITERATURE.md: present
REPORT.md: present
220 LOG.md
432 PROOF.md
207 AUDIT.md
27 LITERATURE.md
82 REPORT.md
968 total
VERDICT: PARTIAL an endpoint boundary-score reduction and sharpness of the comparison coefficient for nested increasing events
2026-11-15 11:01:31 +0400
```

The line counts precede this final append. The text search confirms
the sparse-radius formula, the matching coefficient, the vanishing
critical probabilities and the conditional status of the actual-arm
conclusion. The final wording specifies exactly which universal
logarithm-free inference the construction rules out. No further
mathematical checks or computations are needed for the stated result.

All authored artifacts are LOG.md, PROOF.md, AUDIT.md, LITERATURE.md and
REPORT.md in this folder. No earlier folder was edited. No git,
subagents, accounts, messages, publishing, or numerical workloads were used.
