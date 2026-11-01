# Signed noisy derivatives and an exact resolvent entropy bound

Date: 2026-09-30 UTC. Status: proved elementary extension; no novelty claim. Full Fourier entropy–influence remains open.

## Source and scope

The starting point is the positive smoothing calculation in Mahdavifar–Beirami, arXiv:2609.26444, Sections IV.A and IV.C. The fetched unversioned PDF identifies itself as v1, while the abstract page lists a later revision. This note pins the calculation to the PDF labelled v1 and does not certify the paper's full Courtade–Kumar proof. Its scalar channel estimates, tail closure, and computational appendix have not been independently audited here.

Primary source: https://arxiv.org/pdf/2609.26444v1 . Older relevant background: Falik–Samorodnitsky, *Edge-isoperimetric inequalities and influences*, https://arxiv.org/abs/math/0512636 . The norm/entropy lower bound and the logarithmic Sobolev upper bound are standard; their directions must not be interchanged.

The theorem below extends the positive-kernel calculation to signed derivatives by freezing a noisy L1 norm. It gives physical-space entropy control, not Fourier-coefficient entropy control. The limiting corollary is of Talagrand/Falik–Samorodnitsky type. Repository searches under signed derivative/resolvent, pivotal entropy, positive smoothing, and Falik–Samorodnitsky found no matching P03 statement; this bounded search establishes no novelty.

## Definitions

Use the uniform cube, normalized Walsh coefficients, and natural logarithms. Let f be Boolean, p_S=fhat(S)^2, a_i=Inf_i(f), and V=Var(f). The derivative on the other n−1 coordinates is

    d_i f(x_−i) = [f(x_−i,+1)−f(x_−i,−1)]/2.

Thus d_i f takes values in {−1,0,1}, and both E|d_i f| and E(d_i f)^2 equal a_i. Write T_r for ordinary cube noise, and L for the cube number operator, L chi_S=|S| chi_S.

Fix 0<r≤1 and gamma>0. Define

    b_i = ||T_r d_i f||_1,
    U = sum_(S nonempty) r^(2(|S|−1)) p_S,
    z_i = (gamma+1) sum_(S contains i)
          r^(2(|S|−1)) p_S / [|S|(gamma+|S|)],
    Z = sum_i z_i.

A zero b_i implies d_i f=0, because T_r is invertible when r>0. Hence z_i=a_i=0 as well. Omit these coordinates from all logarithms. For a constant f every quantity vanishes.

## Theorem

For every Boolean f and every permitted r,gamma,

    0 ≤ z_i ≤ b_i ≤ a_i ≤ 1−|Ef| ≤ V,
    0 ≤ Z ≤ U ≤ V,                                      (1)

and

    sum_i z_i ln(z_i/b_i^2)
        ≤ 2(gamma+1)(U−Z).                              (2)

Individual summands on the left of (2) can be negative. In fact the stronger bound also holds:

    sum_i [z_i ln(z_i/b_i^2)]_+
        ≤ 2(gamma+1)(U−Z).                              (2+)

Here [x]_+=max(x,0). No positivity of a derivative and no monotonicity of f are assumed.

### Proof

Put g_i=d_i f and, for 0≤t≤r^2,

    w_i(t)=T_sqrt(t) g_i,
    s_i(t)=E w_i(t)^2,
    k(t)=(gamma+1)/(gamma r^2) [1−(t/r^2)^gamma].

The kernel k is nonnegative and integrates to one. Since

    w_i(t)=T_(sqrt(t)/r)(T_r g_i),

L1 contraction gives ||w_i(t)||_1≤b_i. Also ||w_i(t)||_infinity≤1, because g_i is bounded by one. Consequently s_i(t)≤||w_i(t)||_1≤b_i. Direct integration of each Walsh coefficient gives

    z_i = integral_0^(r^2) k(t)s_i(t) dt.                 (3)

This proves z_i≤b_i. Noise contraction gives b_i≤a_i. Each pivotal edge has one endpoint in each Boolean level set; counting either endpoint yields a_i≤2 min(P(f=1),P(f=−1))=1−|Ef|. The remaining last inequality in (1) is elementary. Summing the displayed Fourier formula for z_i gives

    Z=(gamma+1) sum_(S nonempty)
      r^(2(|S|−1)) p_S/(gamma+|S|),

which proves Z≤U≤V.

For any real cube function w, let s=Ew^2 and c=E|w|. If s>0, Jensen under the density w^2/s gives

    Ent(w^2) ≥ s ln(s/c^2).

One may apply Jensen to |w|; points with w=0 carry zero density. Gross's cube logarithmic Sobolev inequality, in the present number-operator normalization, gives the opposite-direction estimate

    Ent(w^2) ≤ 2 E[w L w].

Apply both to w_i(t), then weaken c≤b_i:

    2 E[w_i(t)Lw_i(t)] ≥ s_i(t) ln(s_i(t)/b_i^2).

The statement includes s_i=0 by continuity. Integrate against k and use convexity of s ln(s/b_i^2), separately for each i:

    2 integral k(t) E[w_i(t)Lw_i(t)] dt
        ≥ z_i ln(z_i/b_i^2).                             (4)

There is an exact energy identity

    sum_i integral k(t) E[w_i(t)Lw_i(t)] dt
        = (gamma+1)(U−Z).                               (5)

Indeed, for a Fourier set S of size j≥1, the j derivatives have degree j−1. Each contributes

    (j−1)(gamma+1)r^(2(j−1))p_S/[j(gamma+j)].

Their sum agrees with that coefficient on the right of (5). Sum (4) to prove (2). To prove (2+), observe that each left side of (4) is a nonnegative Dirichlet energy. It therefore also bounds the positive part of its right side, before summing. No subtraction between coordinates is required.

## Two direct consequences

Log-sum gives the collective version

    Z ln[Z / sum_i b_i^2] ≤ 2(gamma+1)(U−Z).              (6)

At r=1, let gamma tend to infinity. Put

    c_i=sum_(S contains i) p_S/|S|,
    sum_i c_i=V.

The limit of (2), a finite sum for each f, is

    sum_i c_i ln(c_i/a_i^2) ≤ 2(I(f)−V).                 (7)

The same bound holds with each summand in (7) replaced by its positive part. Its log-sum corollary is

    V ln[V / sum_i a_i^2] ≤ 2(I(f)−V).                  (8)

Equations (7)–(8) are weighted influence/variance inequalities, not an upper bound on spectral entropy. They are recorded for orientation, without a claim of being new.

## Signed summands and positive parts

For an n-coordinate parity with n≥2,

    b_i=r^(n−1),
    z_i=(gamma+1)r^(2(n−1))/[n(gamma+n)].

Thus z_i/b_i^2=(gamma+1)/[n(gamma+n)]<1, so every logarithmic summand is strictly negative. This checks that replacing signed derivatives by physical noisy L1 norms changes a positivity property present in the monotone case. The proof above never requires that property. The positive-part strengthening (2+) instead follows from nonnegativity of each coordinate energy. This is different from simply declaring every entropy-like summand nonnegative.

## The unproved transfer needed for FEI

The entropy in the proof is Ent(w_i(t)^2) under the physical uniform measure. FEI asks for

    H_spec(f)=sum_S p_S log2(1/p_S) ≤ C sum_S |S|p_S.

These are different entropies. The spectral identities (3) and (5) collect squared coefficients with weights depending on their degrees and incidences. They do not recover the coefficientwise logarithm. No inequality has been proved here that transfers H_spec into the left side of (2), or into an integral of such left sides with a bounded influence budget.

The physical mismatch tariff in the current FEI restriction route instead involves the distribution of differences of child Fourier magnitudes and a KL correction. No identification of that distribution with the noisy physical fields w_i(t) is available. An unproved identification or reuse of the same energy at multiple scales would be a substantive gap.

Even monotone rearrangement cannot be imported as an entropy-preserving shortcut. Let g(y1,y2)=1−2*1_(y1=y2=+1), a two-bit bent phase, and let f(z,y)=z g(y). Then H_spec(f)=2 and I(f)=2. Sorting each z-fiber produces a dictator, with entropy zero and influence one. Thus the sorting used for a physical-information extremum need not preserve spectral entropy.

## Claim ledger

- PROVED: signed derivative positive-kernel bound (1)–(5) and its positive-part strengthening (2+), including zero cases and negative summands.
- PROVED: direct log-sum and limiting corollaries (6)–(8).
- RECOVERED BACKGROUND: Jensen norm/entropy estimate, Gross LSI, and the Talagrand/Falik–Samorodnitsky influence/variance mechanism.
- SOURCE-CREDITED EXTENSION: freezing b_i=||T_r d_i f||_1 allows signed derivatives in the resolvent calculation.
- NOT CERTIFIED HERE: the complete Courtade–Kumar claim of arXiv:2609.26444 or its revisions.
- OPEN: coefficientwise entropy transfer and non-reusing global influence payment; full FEI.
- NOVELTY: unverified.

No executable code or numerical interval certificate is part of this note. All claims marked proved have analytic proofs above.

Revision note: the first archived text stated too narrowly that the positive-part version was not established. The coordinatewise nonnegative energy in (4) proves (2+) immediately; this version includes that stronger consequence. The original signed bound and the FEI transfer gap are unchanged.
