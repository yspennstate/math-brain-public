SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T09:58:34Z.
attacking: random-slope mass-homogeneous localization—keep a whole smoothing coordinate inside a conjugate shear, derive a translation-uniform logarithmic potential for an arbitrarily correlated remainder, then pay the completed physical-pair kernel without fragment/support/moment loss.

# Early substantive checkpoint — random-slope logarithmic localization

Status: new supporting derivation; FULL QFORM OPEN; continuity separate.

Let X be an independent cap-one probability variable, V an arbitrary bank component of total mass m, and

Y = X S(V) + R(V),

where R may be arbitrarily correlated with the slope S(V). Suppose the slope pushforward is absolutely continuous with density g_S satisfying

0 <= g_S <= m H,   integral g_S = m.

Conditioning on V gives, for every t and rho>0,

nu_Y{|Y-t|<=rho} <= integral min(1,2rho/|s|) g_S(s) ds.

After dividing by m, the bathtub extremizer for the even decreasing kernel min(1,2rho/|s|) is the density H on the centered interval of length 1/H. Hence, with q=4H rho,

nu_Y{|Y-t|<=rho} <= m F(q),
F(q)=q[1+log(1/q)] for 0<q<=1, and F(q)=1 for q>=1.

Layer cake therefore gives the translation-uniform logarithmic potential

integral log_+(A/|t-y|) dnu_Y(y) <= m Omega_0(4HA),

Omega_0(y)=y[2+log(1/y)] for 0<y<=1, and Omega_0(y)=log y+2 for y>=1.

Now let an outer ORIGINAL-coordinate physical pair have invertible indefinite block B, D=|det B| and kappa=sigma_min(B). The completed physical-pair logarithmic envelope, used linearly for this subprobability component, gives

p_Q^sub(t) <= 2sqrt(2)m/r + D^(-1/2) integral log_+(2r^2/(kappa|t-y|)) dnu_Y(y).

Thus

||p_Q^sub||_infinity <= m inf_{z>0}{8 sqrt(H/(kappa z)) + D^(-1/2) Omega_0(z)},

and at z=1,

||p_Q^sub||_infinity <= m[8 sqrt(H/kappa)+2D^(-1/2)].

The mass m stays outside the entire reciprocal/logarithmic payment. Therefore any countable positive decomposition for which the slope-density cap scales as mH can be performed BEFORE this smoother with exactly zero constant loss. No hypothesis on R, moments, support radius, fragment count/separation, or translations is used.

Partner account03/B14 r32 supplies an exact source-valid way to obtain such mass scaling. For a shear W=aX3+bX4-beta with |b|>=|a|, if X3 is replaced by any positive subdensity fragment of mass m while X4 remains a full cap-one probability law, the shear submeasure has density cap <=m/|b|. For the hub slope S=s0+2dW this becomes <=m/(2|db|), so H=1/(2|db|) and

||p_Q^sub||_infinity <= m[4sqrt(2)/sqrt(|db| kappa)+2/sqrt(D)].

Summing arbitrary countably many remote X3 fragments is therefore exact-zero-loss while R may depend arbitrarily on the same shear bank.

Required newest-Claude source applied at an actual inequality: Theorem H in math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 gives, for a one-hub diagonal-leaf star with leaf coefficient vector c satisfying max_i c_i^2/||c||_2^2<=1/2,

|phi_Y(t)| <= 2pi/(||c||_2 |t|).

Feeding this critical Fourier constant into the already completed physical-pair critical-Fourier/log compiler yields the concrete comparison

||p_Q||_infinity <= 4 sqrt(2pi/(kappa||c||_2)) + sin(1/2)^(-2) D^(-1/2).

The new slope-cap route removes Theorem H's diagonal-leaf restriction whenever the actual slope law has the stated density cap, because R(V) is allowed to be fully correlated and nonseparable.

First unpaid implication: in each surviving no-pivot/N3 branch, expose before fragment normalization either (i) an invertible indefinite pair whose Schur remainder contains an exact zero-self original-coordinate hub with a whole-bank slope cap of the above mass-homogeneous type, or (ii) a whole-law D'/D5/ridge/mixed-hub exit. A merely small nonzero hub self-coefficient cannot be discarded perturbatively under arbitrary unbounded supports.
