# P0162 affine-indicator boundary packet

Author: w510. Date: 2026-10-10. Referee: w512; independent adversary: w511. Status: author proofs of special cases and counterexamples to stronger auxiliary statements; independent review pending. No solution of unrestricted FEI and no novelty claim.

## Target and conventions

Use STATEMENT.md: uniform input x in F_2^n, Boolean f(x) in {-1,+1}, normalized Walsh coefficients fhat(s)=E[f(x)(-1)^(s dot x)], spectral random vector Z with Pr[Z=s]=fhat(s)^2. H(f)=H(Z) in bits; I(f)=E|Z|. Zero terms contribute zero. The target asks for an absolute finite C with H(f)<=C I(f) for every n and f, including arbitrarily biased and constant functions.

Primary statement: O'Donnell-Wright-Zhou, author PDF https://www.cs.cmu.edu/~odonnell/papers/fei.pdf, introduction and Section 2.1. The coordinate AND/OR limit giving a lower bound 4 is explicitly folklore there, Section 1.2. The present calculation supplies a complete affine-orientation formula and normalization counterexamples, not a novel lower bound for FEI.

## C001: exact spectrum and influence of affine indicators

Let A=a+V be a nonempty affine subspace of F_2^n of codimension r>=1. Write U=V^perp (dimension r), p=2^(-r), and m=|{i: there exists u in U with u_i=1}|. Set f=1-2 1_A. Then

* fhat(0)=1-2p;
* fhat(u)=-2p (-1)^(u dot a) for nonzero u in U;
* fhat(s)=0 for s not in U;
* I_i(f)=2p for each of the m active coordinates, zero for all others; I(f)=2pm;
* with q=(1-2p)^2, H(f)=-q log2(q)+8p(1-p)(r-1).

Proof. The average of a character over a+V is p(-1)^(s dot a) if s annihilates V, and zero otherwise: if s does not annihilate V, translating the summation by a v in V with s dot v=1 negates the sum. This gives the coefficients. For an active coordinate i, u -> u_i is a nonzero linear functional on U, so exactly 2^(r-1) elements of U have u_i=1. Each contributes Fourier square 4p^2; hence I_i=4p^2 2^(r-1)=2p. There are 2^r-1 nonzero coefficients of square 4p^2. Their entropy contribution is (2^r-1)4p^2(2r-2)=8p(1-p)(r-1). The empty coefficient contributes the stated remaining term. This proves all formulas without any independence assertion about Z.

The sign-reversed f has the same entropy and influence. For r=0, f is constant and H=I=0. For r=1, f is a signed parity, q=0, H=0 and I=m.

## C002: sharp FEI constant 4 for the entire affine-indicator class

For all functions in C001 and constants, H(f)<=4 I(f). No smaller uniform constant works for this class. For a fixed r>=2, the maximum ratio is

M_r=[-(1-2p)^2 log2((1-2p)^2)+8p(1-p)(r-1)]/(2pr), p=2^(-r),

and is attained exactly when A is a coordinate subcube, up to translation. For each affine indicator H(f)/I(f)=(r/m) M_r, and M_r tends to 4 as r tends to infinity.

Proof. An r-dimensional subspace supported on m coordinates injects into F_2^m, so m>=r. For r>=2, 0<q<1 and -q ln(q)<=1-q (apply ln(t)<=t-1 to t=1/q). Since 1-q=4p(1-p),

H(f)<=4p(1-p)/ln(2)+8p(1-p)(r-1).

After division by I=2pm, this is

H(f)/I(f) <= 4(r/m)(1-p)[1-(1-1/(2 ln(2)))/r] < 4.

Here ln(2)>1/2, for example by integrating 1/t>1/2 on (1,2), and r/m<=1. The cases r<=1 were already handled. For a fixed r>=2, H(f)>0 is fixed and I=2pm is minimized exactly at m=r. In that case U is an r-dimensional subspace of its r-coordinate support and therefore is that entire coordinate space; A fixes those r coordinates and leaves the others free. Conversely any such coordinate subcube has m=r. For coordinate subcubes the nonempty entropy term divided by I is 4(1-p)(r-1)/r ->4. The remaining nonnegative empty term is at most 2(1-p)/(r ln(2)) ->0. Thus M_r->4 and any C<4 fails for some r. No estimate on general Boolean functions follows from this special class.

## C003: conditioning away the empty spectrum must retain its mass

For any nonconstant Boolean f, let v=Pr[Z!=0]=Var(f)>0 and Q be the law of Z conditioned on Z!=0. The exact identities are

H(f)=h2(v)+v H(Q), and I(f)=v E_Q|Z|.

Proof. At 0 the spectral mass is 1-v; each nonzero spectral mass is v Q(s). Expanding -sum p log2 p gives the entropy identity, and the expectation identity follows since |0|=0. When v=1 these identities use h2(1)=0; for constants Q is undefined and must not be used.

The stronger bridge H(Q)<=C I(f) with absolute C is false even for coordinate subcube indicators. In C001 with m=r, Q is uniform on the 2^r-1 nonzero dual vectors, so H(Q)=log2(2^r-1) and I(f)=r 2^(1-r). For r>=2,

H(Q)/I(f)>=((r-1)/r) 2^(r-1)->infinity.

This refutes only the bridge with the wrong denominator. The mass-weighted quantity v H(Q)/I(f) stays bounded here, as C002 proves for the full entropy.

## C004: uniform per-coordinate entropy charging and spectral independence fail

Let f_r=1-2 1_{x_1=...=x_r=0} on F_2^r, r>=2, and Z its spectral random vector. Every coordinate has a=Pr[Z_i=1]=I_i(f_r)=2^(1-r). Thus for the first coordinate in ANY deterministic ordering,

H(Z_i)/I_i(f_r)=h2(a)/a>=log2(1/a)=r-1.

Therefore no absolute C can make every chain-rule increment H(Z_i | previously exposed coordinates)<=C I_i(f) for all Boolean functions and all steps; the first step already fails for every ordering of f_r. Also sum_i h2(I_i)/I=h2(a)/a is unbounded, even though H/I tends to 4. A bound by sum_i h2(I_i) cannot be converted to a dimension-free FEI bound merely by a universal scalar inequality for its summands.

For distinct i,j and r>=2, exactly 2^(r-2) dual vectors contain both coordinates, so Pr[Z_i=Z_j=1]=p, where p=2^(-r). The product of the marginal probabilities is 4p^2. For r>=3 these differ, with covariance p-4p^2>0. Independent input bits do not imply independent spectral-coordinate bits. All these assertions follow from C001's exact spectrum, not numerical extrapolation.

## Hardest remaining gap

Unrestricted FEI still needs a dimension-free estimate on the MASS-WEIGHTED conditional spectral entropy v H(Q) for arbitrary Boolean f. The affine proof uses a uniform dual-subspace spectrum and cannot bound a general nonuniform, non-affine Q. Neither the unweighted conditioned entropy nor uniform per-coordinate chain charging supplies this estimate. This is the single unclosed step in the broader route; no claim here closes it.

Next concrete proof step: formulate a block exposure rule for the nonempty spectral sample and test whether its conditional entropy budget can be charged to v E_Q|Z|, preserving the factor v and allowing correlated spectral coordinates.

## Prior-attempt digest and validation

The 2026-09-07 ranking calls P0162 tier 5 / attempted_un. Exact intake entries were recovered at brain_bundle_C006p01.json, key op-p0162, and brain_bundle_C006a04.json, key at-p0162. The latter constructs the uniform law on singleton subsets, whose entropy is log2(n) but expected size is one, then explains why it is NOT a Boolean squared spectrum: a linear function supported on those singletons has nonzero cross terms in f^2. Its hardest gap is a dimension-free inequality exploiting the Boolean convolution identities. The present lane is disjoint: every counterexample here is an actual Boolean function. Targeted searches in the named H/I attempt directories produced no P0162 or Fourier entropy/influence hit. The F0090 report claims only the planar percolation crossing case and explicitly distinguishes it from general FEI; it is not evidence that P0162 is solved. Recent primary literature includes a general bound with an extra sum_i I_i log(1/I_i) term (A New Bound for the Fourier-Entropy-Influence Conjecture, Combinatorica 2024), an induction bridge for selected separated classes (Gonzalez-MacManus-Pereyra, arXiv:2606.00246v2), and plateaued/partially bent special cases (Potapov, arXiv:2609.21563v1). Their statements do not justify promoting C002 to a universal result. A complete up-to-date solved/retired audit is unavailable; current openness remains UNKNOWN.

Small exact Fourier-transform checks are corroboration only. Independent mathematical review by w512 is pending. No Lean theorem or formal-check receipt is claimed.

Independent mathematical verdict received at 2026-10-10 05:35 UTC: w511 KEEP C001-C004, including fixed-r equality, r=0/1, conditioning mass, and spectral dependence. Evidence: ~/brain_workers/w511/AUDIT_W510.md. This is one independent verdict; account separation and the required further keep are not certified. Referee routing receipt: delivered via existing-worker registration helper.
