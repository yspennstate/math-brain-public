# Independent mathematical audit of w534

Verdict: KEEP the short-range Lemmas A and B, under s>3, with the exact normalization below. KEEP Lemma C only as a result about its explicitly defined heat-relative integral. This verdict does not establish P0309, BCC/FCC stability, or identification with a long-range Gibbs specification. Designated referee w536 remains separate.

The reviewed assertions are recorded by formula and assumption here. PAIRED_PROOF_RECEIPT.json identifies the accompanying snapshot; later changes are not covered. This is a direct proof audit, not a review of another review. My DLR derivation was already saved before reading the paired proof.

## Independent reconstruction of the decisive steps

1. The cell [0,1) x [0,1) x [0,2) has two basis sites, (0,0,0) and (a,0,1). Density is one. Even-plane and odd-plane particles see the same energy after m -> -m. Therefore the mean unordered-pair energy difference is exactly one half of the odd-n sum in A1. There is no extra factor one half for the two particle types and no zero separation in this sum. Integral shifts a give the same unlabeled configuration; no other shift does.

2. At s>3 each Riesz energy converges absolutely, since a shifted lattice has O(R^3) points in a radius-R ball and its tail is sum R^(2-s). The gamma representation may therefore be applied to each positive energy sum before subtracting. Factoring the Gaussian sums gives A2 with one factor Theta(t,0), one odd-plane factor O(t), and the shifted theta difference.

3. Compute the kth Fourier coefficient of the periodized Gaussian directly: integrate exp(-t x^2) exp(-2 pi i k x) over the real line. It equals sqrt(pi/t) exp(-pi^2 k^2/t). The coefficients have an absolutely convergent Fourier series, so reconstruction is legitimate. Pairing k with -k gives A3. Each cos(2 pi k a)-1 is nonpositive. The k=1 term is strictly negative whenever a is nonintegral. All other factors in A2 are positive. This proves the strict global inequality and the exact equality set, rather than a numerical local sign check.

4. Two derivatives in a multiply the paired Fourier term by -(2 pi k)^2. This gives Theta_aa(t,0)=-8 pi^2 sqrt(pi/t) sum_{k>=1} k^2 exp(-pi^2 k^2/t). Multiplying by 1/(2 Gamma(s/2)) in A2 gives the coefficient -4 pi^2 sqrt(pi)/Gamma(s/2) and power t^(s/2-3/2) in A4. Both the sign and the factor are correct.

5. Differentiation under the integral has a uniform integrable majorant. For t<=1 the two unshifted Gaussian sums are O(t^-1/2), while every shifted-difference derivative through order two is O(t^-1/2 exp(-pi^2/t)). For t>=1 and a in a neighborhood of zero, the primal derivative sums have polynomial growth in t and O(t) decays as exp(-t). These two bounds justify the claimed curvature and Taylor expansion. A positive radial integral alone would not prove lattice stability; the computed curvature is in fact negative here.

6. Independently differentiate |r|^-s twice in the e1 direction. The result is h_s(r)=-s|r|^(-s-2)+s(s+2)r_1^2|r|^(-s-4), as in B1. In the finite-support relative energy every changed pair is included twice in the ordered x,r sum, hence the factor one half in B2. The gradient sum is absolutely convergent for s>3 and cancels by r -> -r, so the first derivative vanishes.

7. For fixed r, the interior of Q_L gives (p_{x+r}-p_x)^2=1 when r_3 is odd and zero when r_3 is even. The boundary fraction tends to zero. The full sum divided by |Q_L| is at most two because its support lies in Q_L union (Q_L-r). Also sum |h_s(r)| is finite. Dominated convergence gives K_L/|Q_L| -> (1/2) sum_{r_3 odd} h_s(r), which is the same E_s''(0)<0 from A1. Thus some finite L has negative curvature. With zero first derivative, sufficiently small nonzero displacements lower the relative energy while every outside particle remains fixed. This closes the infinite-support-versus-local-ground-state issue.

## Boundary and scope checks

The exclusion s>3 is essential for the separately defined raw energies, although some relative expressions admit weaker ranges. a=0 and all integral a are equality cases; half-integral a is strict. Scaling to density rho multiplies energy by rho^(s/3), preserving the sign. The bound permits L to depend on s; no uniform cutoff, numerical threshold, or concrete L is claimed.

For 0<s<=3 the separate raw energies cannot be used. The stated heat-relative integral is finite by the same exponential endpoint bounds and has a strictly negative sign away from integral a. That statement is valid by definition of the regularization. Any identification with a neutralized Coulomb or other thermodynamic/DLR energy is an additional premise, not supplied by this audit. The assertion makes no s=0 claim.

The proved counterexample is to force balance implying nonnegative displacement Hessian/local ground-state stability. The prior at-p0309 card already assumes a stable crystal and explicitly disclaims phase construction; it is not refuted. The hardest remaining P0309 piece is a uniform nonlinear free-energy/order estimate controlling defects and competing phases for a genuinely stable candidate.

No numerical experiment or formal proof assistant was used. Trusted mathematical tools are Gaussian Fourier inversion, the gamma integral, dominated convergence, absolutely convergent lattice sums, and Taylor expansion.
