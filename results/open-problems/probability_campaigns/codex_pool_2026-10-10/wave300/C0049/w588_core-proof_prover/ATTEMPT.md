# C0049 core-proof packet (w588)

Date: 2026-10-10. Status: DRAFT mathematical work, independent review pending.
Exact target: STATEMENT.md. No full C0049 solution or novelty claim.

## Prior-attempt digest

The dated ranking labels C0049 attempted_un; that label is not a proof, nor a current openness certificate. PRIOR_RECORDS.json saves the exact C0049 intake and C0049-A001/C0050-A001 attempt rows. A targeted exact-ID search of the cited H/I attempt directories and Lean directory found no further C0049 proof. This is a scoped search result, not a whole-owner-corpus retirement certificate. Team O assigns the related observable-convergence problem C0050 to w339 and the related interface problem P0124 to w341. This packet claims only coefficient identification without an a priori semimartingale assumption, and explicit obstructions to overstrong observable arguments.

The intake's actual primary source is Duminil-Copin's 2017 Ising/Potts lectures, https://www.unige.ch/~duminil/publi/2017PIMS.pdf , section 7, Conjecture 3 (printed p.93 / PDF index92), and Conjecture 4 on the next page. Its section 6.4 proof already identifies the q=2 driver by Laurent coefficients without postulating a semimartingale. L1 explicitly generalizes that algebra in sigma and supplies deterministic common localization; it is not claimed as a new method. The older random-cluster lectures below give the same target with different numbering.

C0049-A001 says the conjecture reduces **exactly** to finding another discrete relation. That necessity/equivalence is unsupported: new regularity estimates or a different route could suffice. C0050-A001 asserts uniqueness with a limit bounded near the marked endpoints; L4 below shows that the stated target itself is unbounded there. Passing boundary conditions and proving a correctly specified uniqueness theorem are missing arguments. One proposed source-row patch qualifies these two statements while preserving the historical attempt and its unsolved status.

The primary lecture source, section 5.3.2, printed pp.45--46, states the square-lattice Dobrushin-interface conjecture and the absolute observable convergence conjecture. Its spin is

    sigma = (2/pi) arcsin(sqrt(q)/2),   kappa = 8/(1+sigma).

The observable is normalized by (2*delta)^(-sigma). The proposed limit is (phi')^sigma, for a conformal map to the strip of height one. In half-plane coordinates phi=(1/pi)log(g-U), so the deterministic factor pi^(-sigma) does not affect a martingale identification argument. The lecture explicitly warns that the weak equations underdetermine the general-q observable. We do not import its dated open-status sentence as a 2026 status verdict.

A fresh endpoint source, arXiv:2610.08507v1, Theorem 1.2, asserts free-boundary q=4 loop convergence to nested CLE(4). This changes the relevant source status but does not itself supply the Dobrushin boundary-change step. We have read the theorem statement, not independently audited that proof.

The public OpenAI/math collection also lists a 5 October 2026 manuscript claiming the chordal square-lattice target for 1<=q<=4, and a September companion for 0<q<1 with smooth boundary assumptions. The primary repository README explicitly treats verification as incomplete. Direct browser access to its PDF failed on content type and the directory view failed; its full proof has not been checked here. w590's separate source-scope packet identifies those claims and is auditing the manuscript's load-bearing step. Current openness remains UNKNOWN; we claim neither a new solution nor a certified refutation of those manuscripts.

## The single hardest missing input for this route: G

Fix q, sigma as above. After mapping the original domain to the upper half-plane, and after a common localization that keeps each fixed probe away from the explored hull, prove that the correctly normalized **conditional FK parafermionic observables in the actual explored slit domains** converge jointly with the exploration histories to

    M_t(z) = (g'_t(z)/(g_t(z)-U_t))^sigma,

up to one fixed, nonzero deterministic multiplier. The normalization must respect conditioning and the original winding convention. For a deterministic sequence z_n=i*R_n with R_n tending to infinity, require convergence at every fixed probe and time, plus uniform integrability, sufficient to pass the martingale identities against bounded functions of past histories. Common stopping and convergence of the stopped histories are part of G. Static-domain convergence alone is not this assertion.

Curve tightness, compatibility of the subsequential curves with continuous capacity drivers, and the original boundary approximation remain separate inputs to the full target. For q<1 we additionally have not established the critical tuning and requisite tightness theory. G is the hardest input of this chosen observable route, not a theorem asserted necessary for every possible proof.

## L1: coefficient identification without a semimartingale hypothesis

**Statement.** Let sigma>0. On a filtered probability space satisfying the usual conditions, let U be a real continuous adapted process with U_0=0. Let g solve the chordal Loewner equation

    d g_t(z)/dt = 2/(g_t(z)-U_t),    g_0(z)=z.

For an unbounded deterministic sequence R_n, assume M_t(iR_n) as defined in G is a complex local martingale, in the same filtration, until the probe's lifetime. Fractional powers are defined by continuous logarithms starting from g'_0=1 and g_0(z)-U_0=z. Then U is a continuous local martingale with quadratic variation 8t/(1+sigma), and hence U has the law of sqrt(8/(1+sigma)) times Brownian motion, in that filtration. No semimartingale hypothesis on U is assumed.

**Proof.** Fix L,T>0 and tau_L=inf{t: |U_t|>=L}. Write theta_t=t wedge tau_L, for t<=T. All expansions below are deterministic and uniform over continuous drivers bounded by L before the stop. Set z=iR, with R^2>=8T and R sufficiently large relative to L.

Write y_t=Im g_t(z). The Loewner ODE gives

    d(y_t^2)/dt = -4*y_t^2/|g_t(z)-U_t|^2 >= -4.

Consequently y_t>=sqrt(R^2-4T)>=R/sqrt(2); the probe survives the entire stopped horizon. Integration of the ODE gives |g_t(z)-z|<=2*sqrt(2)*T/R. Expanding the reciprocal, using this bound and |U|<=L, yields, uniformly on the stopped interval,

    g_theta(z) = z + 2*theta/z + O_(L,T)(R^-2),
    g'_theta(z) = 1 - 2*theta/z^2 + O_(L,T)(R^-3).

The second expansion also follows directly by integrating

    log g'_theta(z) = -2 integral_0^theta (g_s(z)-U_s)^(-2) ds.

The errors follow from the uniformly convergent geometric series for (g-U)^(-1); no derivative or variation bound on U is used. Define

    H_t(z) = z^sigma M_theta_t(z)
           = exp{sigma[log g'_theta_t(z) - log((g_theta_t(z)-U_theta_t)/z)]}.

The logs in this expression are the near-one branches when R is large. The ODE and fractional-power expansion give

    H_t(z) = 1 + sigma*U_theta_t/z
               + [sigma*(sigma+1)*U_theta_t^2/2 - 4*sigma*theta_t]/z^2
               + O_(sigma,L,T)(R^-3).                       (1)

The coefficient -4*sigma*theta includes both factors: -2*sigma*theta from g' and -2*sigma*theta from the denominator. Omitting g' would give the wrong variance.

H_t(z) is a stopped local martingale by assumption. It is deterministically bounded for fixed L,T and all sufficiently large R: |g'|<=exp(2T/(R^2-4T)) and |z/(g-U)|<=R/sqrt(R^2-4T). Since sigma is real, these give the same bound for the chosen powers. Thus H(z) is a true martingale on [0,T].

The true martingales z_n[H(z_n)-1]/sigma converge uniformly, with deterministic error O_(sigma,L,T)(R_n^-1), to U_theta. Passing conditional expectations is valid by this deterministic uniform bound. Hence U_theta is a true martingale. After this step, the processes

    (2*z_n^2/[sigma*(sigma+1)])
      *[H_t(z_n)-1-sigma*U_theta_t/z_n]

are true martingales. Equation (1) makes them converge uniformly to

    U_theta_t^2 - [8/(1+sigma)]*theta_t.

This limit is a true martingale as well. Taking increasing L and T proves that U and U^2-kappa*t are continuous local martingales. Only now invoke the continuous-local-martingale quadratic-variation theorem: U^2-[U] is a local martingale, so [U]-kappa*t is a continuous finite-variation local martingale and is zero. Levy's characterization gives the stated Brownian driver. QED.

Scope: a conditional identification theorem. It does not prove the discrete observables converge, or establish curve tightness. This is an elementary version of the standard observable-identification route; no claim of new research priority is made.

## L2: weak CR, zero boundary data and a scale bound do not imply compactness

**Statement.** On a square grid of mesh delta, assign one complex number F(e) to each unoriented edge. At each interior vertex v impose the weak relation

    F(E)+i*F(N)-F(W)-i*F(S)=0.                   (2)

This is the complex-direction form of the weak contour equation, after rotating and labeling the medial lattice. For any sigma>0 there are fields F_delta supported on four interior edges, vanishing near the boundary, satisfying (2) and |F_delta|<=delta^sigma, whose normalized vertex averages have no locally uniform convergent subsequence.

**Proof.** On one elementary plaquette use bottom/right/top/left values

    delta^sigma * (1, -i, -1, i),

and zero elsewhere. At the bottom-left corner the sum is 1+i*i=0. At bottom-right it is i*(-i)-1=0. At top-right it is -(-1)-i*(-i)=0. At top-left it is -1-i*i=0. Every other vertex has zero incident values. Thus (2) holds everywhere, and all boundary values are zero if the plaquette is interior.

Let A_delta(v)=(1/4)sum_(e incident to v) delta^(-sigma)F_delta(e), using this explicitly defined four-edge mean as an interpolation device. At the four corners it equals (1+i)/4, (1-i)/4, (-1-i)/4, (-1+i)/4. An adjacent vertex outside the plaquette has mean zero. Thus points at distance delta can differ by sqrt(2)/4, uniformly in delta.

Take delta_n=1/(2n) in the unit square and put the bottom-left plaquette corner at z_0=(1/2,1/2). Interpolate these vertex means bilinearly. They are continuous, supported within O(delta_n) of z_0, and have modulus sqrt(2)/4 at z_0 for every n. Any locally uniform limit on a compact neighborhood of z_0 would be continuous and zero at every point other than z_0, hence zero at z_0; this contradicts that fixed value. QED.

This construction is a linear-equation obstruction. It is **not** asserted to be an FK expectation, to obey every probabilistic/winding constraint, or to disprove observable convergence. The four-edge mean is explicitly defined here and is not an assertion about the lecture's vertex normalization. Adding such a homogeneous field preserves prescribed boundary data and weak equations; additional FK-specific structure is needed to exclude it.

## L3: a precise sufficient martingale-transfer criterion

**Statement.** Fix a finite horizon and a common localization. Let U_delta be continuous adapted driver histories, and let X_delta_t be true complex martingales in filtrations containing those histories. Suppose, for all s<=t and finite choices r_j<=s, the vector (U_delta(r_1),...,U_delta(r_k),X_delta_s,X_delta_t) converges in law to (U(r_1),...,U(r_k),X_s,X_t). Assume {X_delta_s} and {X_delta_t} are uniformly integrable. Suppose X is continuous and adapted to the completed natural filtration of the continuous driver U. Then X is a martingale in that natural filtration. Its continuous version is also a martingale under the usual right-continuous augmentation.

**Proof.** For each bounded continuous cylinder function f of the past values, the expectation of (X_delta_t-X_delta_s)*f is zero. Truncate the two X variables; convergence in law handles the bounded continuous product, while uniform integrability removes the truncation uniformly. Thus E[(X_t-X_s)f]=0. Bounded continuous cylinder functions at a countable dense set of past times generate the natural history sigma-field, because U has continuous paths. A monotone-class argument gives the conditional martingale identity. To pass to the right-continuous augmentation, use decreasing times s_m down to s, reverse conditional-expectation convergence, and L1 continuity of X; on a finite horizon that L1 continuity follows from the martingale representation X_t=E[X_T|F_t] together with path continuity and uniform integrability of these conditional expectations. Completion changes no conditional identities. QED.

Joint convergence of stopped histories is an assumption here. Uniform convergence of unstopped drivers alone does not automatically make every hitting-time localization continuous.

**Why uniform integrability matters.** A one-step martingale can have X_n(0)=1 and X_n(1)=n with probability 1/n, otherwise zero. Its expectation at time 1 is 1, but X_n(1) tends to zero in probability. The limit (1,0) is not a martingale. No independence multiplication is used anywhere in this packet.

## Attempt at G and the remaining gap

## L4: the proposed strip-derivative limit is unbounded at marked points

In the unit disk with a=-1 and b=1, take

    phi(z)=(1/pi)log(i*(1+z)/(1-z)).

The Mobius map inside the log maps the disk to the upper half-plane, and the principal log maps that half-plane to a strip of imaginary width pi. Hence phi maps the disk to the strip of height one, with the required marked ends, and

    phi'(z)=2/[pi*(1-z^2)].

For every sigma>0, |phi'(r)|^sigma diverges as r tends to 1 from below, and also as r tends to -1 from above. Thus ordinary boundedness near both marked points excludes the conjectured limit, even in a smooth disk. Appropriate endpoint singularity control must replace that condition. This counterexample concerns the prior attempted reduction, not the FK convergence conjecture. No general boundary-uniqueness theorem is proved here.

## Attempt at G and the remaining gap

The direct route starts with exact conditioning: the discrete terminal winding/visit observable is a conditional expectation along the exploration. It then uses local switching to obtain the weak contour equation. These are useful identities, but L2 proves that weak contour equations, fixed boundary data and even a natural-size bound cannot by themselves establish compactness of the normalized fields. Treating those equations as a complete discrete holomorphic theory is the failed step.

The next plausible input is a bulk modulus of continuity, valid in the explored slit domains, coupled with control of boundary normalization and uniform integrability. For example, after localization, a bound of the form

    E[sup_(z,w in K, |z-w|<=h) |X_delta_t(z)-X_delta_t(w)|]
       <= C_K*h^alpha + o_delta(1),

with alpha>0, together with tight normalization and identification of subsequential holomorphic limits, would rule out the plaquette concentration. No such FK estimate for general q is proved here. Crossing bounds by themselves do not supply this complex winding-sensitive modulus, and we do not use the special q=2 phase/positivity argument at other q values.

**Single hardest remaining gap:** G, the normalized observable convergence and martingale-transfer bounds in actual random FK slit domains. L1 and L3 rigorously reduce identification to that input; L2 blocks one insufficient attempt to establish it. Neither reduction is a solution of C0049.

NEXT: Obtain w589/w590's independent checks of L1--L3; pursue an FK-specific winding/regularity estimate that excludes the compactly supported weak-CR circulations.
