# C0054 independent derivation, saved before reading w600

Date: 2026-10-10. Paired prover's proof has not been read. This is an obstruction to one proof route, not a disproof of two-dimensional localization.

## Precise diagnostic model

Let Lambda=(Z/LZ)^2 with L>2W, W>=1, and periodic l1 distance. Distinct real Gaussian variables Z_xy=Z_yx for unordered pairs are independent; diagonal Z_xx are independent standard real Gaussians too. Set H_xy=t Z_xy when d(x,y)<=W and zero otherwise, with t=[1+2W(W+1)]^(-1/2). There are D=2W(W+1) off-diagonal neighbors per site and sum_y Var(H_xy)=1. This is a specific model within the real-symmetric normalized band-matrix class described in Bourgade's ICM survey, equations (0.1)-(0.2). It is not asserted that every intake source fixes this exact distribution.

## Single-site reduction with all conditioning exposed

For a principal minor Omega, z=E+i eta with eta>0, and x != y in Omega, let G_Omega=(H_Omega-z)^(-1). The Schur identity is

G_Omega(x,y)=-G_Omega(x,x) sum_{u in Omega\{x}} H_xu G_{Omega\{x}}(u,y).

Fix 0<s<1. Write C_s=sup_{a in R} E|Z-a|^(-s). This constant is finite: split the integral into |v-a|<1 and its complement and use the bounded Gaussian density. A complex shift has no larger integral, since |v-a-ib|>=|v-a|. Condition first on every entry except H_xx. The Schur self-energy is then fixed, so

E_{H_xx}|G_Omega(x,x)|^s <= C_s t^(-s).

Use |sum b_u|^s<=sum |b_u|^s before this conditioning. The minor G_{Omega\{x}} depends on none of the incident row variables H_xu. Thus independence of the original upper-triangular entries gives, term by term,

E|G_Omega(x,y)|^s <= sum_u K_s(x,u) E|G_{Omega\{x}}(u,y)|^s,

where K_s(x,u)=C_s t^(-s) E|H_xu|^s. This factorization is justified only AFTER diagonal averaging removes G_Omega(x,x). No product of conditional per-row bounds is taken.

For general independent entries, with diagonal a-priori constants A_x and K_s(x,u)=A_x E|H_xu|^s, a sufficient input for this route is

q_mu = sup_x sum_{u != x} K_s(x,u) exp(mu d(x,u)) < 1,

uniformly over the inherited principal-minor laws. If A=max_x A_x<infinity, iterating the displayed deleted-site identity produces only self-avoiding paths. Each path ending at y has its remaining diagonal moment at most A. The triangle inequality yields exp(mu d(x,y)) <= product_edges exp(mu d(edge)). Bounding self-avoiding path sums by all walk sums gives

E|G_Omega(x,y)|^s <= A/(1-q_mu) exp[-mu d(x,y)].

The expansion terminates after at most |Omega|-1 edges. This finite-volume reduction is independent of E, eta and volume when its input constants are. The input q_mu<1 remains to be established for the desired model; the next calculation rules it out for this scalar route in the diagnostic model.

## Exact obstruction at the normalized Gaussian scale

The centered Gaussian maximizes the probability of an interval of each fixed length among all translations. The layer-cake identity for |Z-a|^(-s) therefore gives C_s=E|Z|^(-s). Consequently each nonzero off-diagonal K_s(x,u) equals

C_s E|Z|^s = [Gamma((1-s)/2) Gamma((1+s)/2)]/pi = sec(pi s/2).

The Gaussian moment identity E|Z|^r=2^(r/2) Gamma((1+r)/2)/sqrt(pi), valid r>-1, and Euler's reflection identity prove this formula. Therefore

q_0 = 2W(W+1) sec(pi s/2) > 2W(W+1) >= 4

for EVERY 0<s<1 and EVERY W>=1. The common scale t cancels exactly; row variance normalization does not make this iteration contractive. Since q_mu>=q_0 for mu>=0, it cannot establish the sufficient input. Even positive site weights cannot rescue this kernel on the torus: at a site of minimum positive weight, the weighted row sum is at least D sec(pi s/2). Taking the optimum allowed diagonal-averaging constant, rather than a crude upper bound, already yields the obstruction.

This proves failure of this particular absolute-value, one-site, uniform-diagonal-averaging method. It does not bound the true resolvent moments below and does not rule out cancellation, adaptive averaging, or a block multiscale argument. Enlarging diagonal disorder by a factor lambda replaces q_0 by D lambda^(-s) sec(pi s/2); a contraction then requires an additional strong-disorder premise absent from the equal-scale model.

## Hardest missing input for a viable localization route

A block replacement needs an eta-uniform, bulk-uniform crossing estimate at some finite scale L0(W,kappa), with a boundary sum small enough for the chosen geometric resolvent iteration, and with decoupling under the actually revealed exterior. An a-priori moment bound or a Ward identity does not supply that small boundary sum. A concrete sufficient target is: find s in (0,1), A<infinity, mu>0 depending on W,kappa but not volume, E or eta such that E|G_Omega(x,y;E+i eta)|^s <= A exp[-mu d(x,y)] for every appropriate finite-volume law, E in [-2+kappa,2-kappa], eta>0. This sufficient estimate is still UNPROVED here, and identifying it is not a proof of it or an equivalence to every possible formulation of localization.

NEXT: recover the complete intake statement; then read w600's candidate and check whether its central estimate supplies a true contraction or replaces the missing input with an assumption.
