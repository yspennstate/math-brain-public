# FEI: logarithmic child-defect allocation and a sparse-activation obstruction

Date: 2026-09-30. Full FEI remains OPEN. This is an all-dimensional intermediate inequality and a Boolean counterexample to a specific proposed strengthening, not a proof or disproof of FEI. No publication-priority claim is made.

## 1. Dependency and correction boundary

Read fresh from the brain's FEI checkpoint: CURRENT_RESEARCH.md, CORRECTION_INBOX.json, MANIFEST.json and PATHWAYS.md under scheduled_tasks/work/shared/fei-all-team-2026-09-22. The pending fixed-positive-occurrence-reserve obstruction remains binding. The later scheduled audit programme was not changed; this is separately requested interactive FEI research.

Read the current P03 README and the September 30 probability audit. The September 20 minor-child report proves B_i <= C_chi j_i + min I(child), and its character-defect successor already improves the additive term to kappa_min. Those improvements are prior work, not rediscovered results. The certified-core max-splicing report explicitly left B_i <= C j_i + O(j_i I_child) as a plausible but unproved alternative. The obstruction below rejects exactly that alternative. Known bent one-point-flip bad splits and sparse suspension techniques are credited as ingredients; the present output concerns their combination and the precise new rejected quantifiers.

Source files in yspennstate/math-open-problems:
- proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__fei-minor-child-allocation.md
- proofnet24/P03-fei/runs/2026-09-20/2026-09-20T06-31-37+0300__fei-character-defect-curvature-allocation.md
- proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__fei-certified-core-max-splicing.md
- proofnet24/P03-fei/fleet-2026-09-22/interactive/20260922T105045Z-fei-proof-assist/interference/REPORT.md

## 2. Definitions

All cubes are uniform; Boolean outputs are +/-1. Fourier coefficients are normalized. For a physical split i with children g,h, write a_T=ghat(T), b_T=hhat(T),

    q_T=(a_T^2+b_T^2)/2,
    e_T=(a_T-b_T)^2/4,
    B_i(f)=sum_T q_T h2(e_T/q_T),
    epsilon=j_i(f)=min(Pr[g!=h],Pr[g=h]),
    kappa(u)=1-max_T uhat(T)^2,
    kappa_min=min(kappa(g),kappa(h)).

A zero-mass packet contributes zero. I(u)=sum_T |T| uhat(T)^2. Let

    C_log=2+3/(2 ln 2)=4.164042561333445... .

## 3. Universal logarithmic child-defect theorem

For every Boolean function and every physical split with epsilon>0,

    B_i(f) <= epsilon [C_log + log2(1+kappa_min/(2epsilon))].       (1)

For epsilon=0, B_i=0. The result can always be minimized with the previously established bounds B_i<=h2(epsilon) and B_i<=C_chi epsilon+kappa_min. It is an improvement in the large kappa_min/epsilon regime, not a pointwise improvement of the latter bound everywhere.

### Proof

Toggle the queried Fourier bit if necessary by replacing h with -h, so Pr[g!=h]=epsilon<=1/2. This leaves B_i and both kappas unchanged. Exchange children so kappa(g)=kappa_min. Multiply both children by the same character and a common sign so g's largest Fourier coefficient becomes its nonnegative mean. This permutes residual packets, leaves epsilon and B_i unchanged, and gives Var(g)=kappa_min.

Put eta=Pr[g=-1]<=1/2, beta=Pr[h=-1]. Then |eta-beta|<=epsilon. The elementary inequality

    beta(1-beta)<=eta(1-eta)+epsilon(1-epsilon)

follows by considering beta<=eta or beta>=eta, using the monotonicity of t(1-t) for t<=1/2. Therefore the total mass in nonempty residual packets satisfies

    Q=sum_(T nonempty) q_T=(Var(g)+Var(h))/2
      <=kappa_min+2epsilon(1-epsilon)<=Qbar:=kappa_min+2epsilon.

Let E=sum_(T nonempty) e_T<=epsilon. Binary entropy satisfies

    q h2(e/q)<= e log2(euler*q/e).

The logarithmic sum inequality (equivalently Jensen with weights e_T/E) gives

    sum_(T nonempty) q_T h2(e_T/q_T)
      <=E log2(euler*Q/E)
      <=E log2(euler*Qbar/E)
      <=epsilon log2(euler*Qbar/epsilon).                         (2)

The last step uses that x log2(euler*Qbar/x) increases for 0<x<=Qbar and E<=epsilon<=Qbar. Zero masses follow by continuity.

For the exceptional empty packet, e_0=(eta-beta)^2<=epsilon^2 and q_0<=1. The function q h2(e/q) increases in q at fixed e, so this packet is at most

    h2(e_0)<=e_0 log2(euler/e_0)<=epsilon^2 log2(euler/epsilon^2).

The function t log2(euler/t^2) increases on (0,1/2], since its derivative is (-1-2 ln t)/ln2>0 there. Its maximum is 1+1/(2ln2). Thus the exceptional packet is at most epsilon[1+1/(2ln2)]. Combining with (2) gives

    B_i <=epsilon[log2(kappa_min/epsilon+2)+1/ln2+1+1/(2ln2)],

which is exactly (1). QED.

This argument differs from simply capping every nonempty packet by its mass: it retains the mismatch mass E and uses the log-sum inequality before discarding the packet profile.

## 4. Sparse activation defeats mismatch-weighted child influence

### Theorem

For every finite C,K>=0 and every eta>0 there is a genuine Boolean f and a physical coordinate y such that both child influences are below eta but

    B_y(f)>j_y(f)[C+K min(I(f_y^+),I(f_y^-))].                    (3)

The same conclusion holds with min replaced by max or by their sum. More generally no function of the two child influences that is bounded on a neighbourhood of (0,0) can multiply j_y to give a universal upper bound for B_y.

### Explicit construction

Let k>=4 be even, r=2k, delta=2^-k, p=2^-r. On k binary coordinates put

    b(x)=(-1)^(x_1 x_2+x_3 x_4+...+x_(k-1)x_k),
    b'(x)=b(x)-2*1{x=0}.

Both functions are Boolean because b(0)=1. Each two-bit quadratic factor has Walsh coefficients +/-1/2; therefore every coefficient a_T of b has magnitude sqrt(delta). The point flip subtracts 2delta from every Walsh coefficient.

On r further binary coordinates let A(z)=1{z=0}. Define Boolean children

    G(x,z)=1+A(z)(b(x)-1),
    H(x,z)=1+A(z)(b'(x)-1).

Let f select G or H by the physical coordinate y. Its children disagree at exactly x=z=0. Consequently

    j_y(f)=p delta.                                             (4)

For every nonempty data index T and every control index U, the child coefficients are p a_T and p(a_T-2delta). The two parent query coefficients are p(a_T-delta) and pdelta. Hence

    q=p^2[(a_T-delta)^2+delta^2],    e=p^2delta^2.

Since sqrt(delta)<=1/4,

    q/e >= (delta^(-1/2)-1)^2+1 >= 1/(4delta).

Consequently q h2(e/q)>=e log2(q/e)>=p^2delta^2(k-2). Summing these nonnegative contributions over 2^r control indices and 2^k-1 nonempty data indices gives

    B_y(f)/j_y(f)>=(1-delta)(k-2) -> infinity.                   (5)

The omitted empty-data packets are nonnegative; none is assumed to vanish.

For any Boolean u on the data coordinates, direct pivotal-edge counting gives the exact activation identity

    I(1+A(u-1))=p I(u)+r p(1-Eu).                               (6)

Thus both child influences are at most p(k+2r)=5k 2^-2k, which tends to zero. In fact Eb=sqrt(delta), Eb'=sqrt(delta)-2delta, I(b)=k/2, and I(b')=k/2+2kdelta, so the exact influences are

    I(G)=p[k/2+r(1-sqrt(delta))],
    I(H)=p[k/2+2kdelta+r(1-sqrt(delta)+2delta)].                  (7)

Equations (4)-(7) prove all stated quantifiers. QED.

### The logarithmic scale in (1) is necessary

For this construction the largest squared coefficient of either child is its constant coefficient, because p<=1/2, its mean is at least 1-p, and every nonconstant coefficient has magnitude at most p. G has the larger mean. Therefore

    kappa_min=1-[1-p(1-sqrt(delta))]^2,
    kappa_min/(2j_y)
      =[(1-sqrt(delta))-(p/2)(1-sqrt(delta))^2]/delta.

It follows that log2(1+kappa_min/(2j_y))=k+o(1). The lower bound (5) is k-O(1). Thus a uniformly bounded replacement for the logarithm is impossible; its leading coefficient cannot be reduced below one in an inequality with a fixed additive constant and this same logarithmic argument. This sharpness is for the local bound, not a lower bound on a universal FEI constant.

## 5. Full-FEI gap and constructive continuation

For a genuine stopping restriction tree T define

    Lambda_T=sum_internal w_v j_v log2(1+kappa_min,v/(2j_v)),

with zero-j terms zero. The preceding theorem and the already proved recombination payment imply

    H(f)<=E H(leaf)+(C_log+2/ln2) sum_v w_v j_v+Lambda_T.          (8)

The queried ordinary influence plus weighted leaf influence is exactly I(f), and sum w_v j_v is no larger than queried ordinary influence. Thus a real stopping tree with Lambda_T<=K times its consumed ordinary influence, and FEI-certified leaves, would yield one depth-independent constant. No universal such tree is established here.

Blind scalar replacement is insufficient: odd majority has zero actual B_i at every root coordinate while kappa_min is near one and j_i is of order n^-1/2. Exact isospectral matching must be recognized rather than charged by (1). Similarly B_i is exactly invariant under multiplying f by an independent Boolean tensor factor, whereas kappa is not. These facts motivate minimizing the bound after removing independent tensor factors and skipping exact isospectral splits. Those operations do not yet prove the required global summability and are not claimed as a new FEI theorem.

Approaches actually compared: (a) raw min-child amortization, rejected as already-known spectator/parity overcharge; (b) mismatch-weighted child influence, refuted above even with both influences vanishing; (c) log-sum packet aggregation, giving the proved logarithmic replacement. The next substantive question is whether a source-realizable stopping rule has a nonreusing payment for the remaining logarithmic charge. A renamed remainder is not a solution.

## 6. Verification and scope

The accompanying Python checker uses integer Walsh transforms for all Boolean functions in dimensions 1-4 and checks (1) for all 262,948 physical coordinate splits. It also evaluates the explicit sparse-activation formula for even k=4,...,40 without enumerating its exponentially large ambient cube. Its finite numerical checks are not the proof of either universal statement. The proof above gives exact rational lower bounds and analytic inequalities.

Independent mathematical audit is recorded separately. No proof-assistant formalization or publication novelty clearance is claimed. No prior report, owner schedule, or source status was altered.
