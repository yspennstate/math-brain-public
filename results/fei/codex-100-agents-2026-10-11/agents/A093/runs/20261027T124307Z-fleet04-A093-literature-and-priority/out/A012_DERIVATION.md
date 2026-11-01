# Projection inheritance pays every finite history from one supplied source

All logarithms are base 2 unless marked ln. The initial reference is normalized. Full FEI remains open.

## 1. Statement and accounting convention

Let f be any Boolean function on a finite uniform cube, P its squared Fourier law, and Q a probability law covering P. Put c=2/ln 2. At a physical query i, inherit the reference by the spectral projection pi_i(S)=S minus {i}: both actual children receive Q'=pi_i Q. The true child laws are P_+ and P_-; their average is P'=pi_i P. Define the FULL projection contraction

    L_i = D(P||Q)-D(P'||Q') >= 0.

This is a KL contraction for the explicitly specified spectral projection, not an unspecified reference-inheritance charge. Define J_i=(D(P_+||P')+D(P_-||P'))/2.

At any node one may also partition the spectral atoms into any finite collection of cells. Write p and q for the true and reference cell masses. For any real t in [0,1], replace q by r=(1-t)q+t p, keeping the old conditional reference inside each cell. Denote the resulting complete reference R, and charge its FULL conversion fee D(R||Q). No renormalizer or reference-only atom is discarded. There may be arbitrarily many such updates, provided the decision tree is finite. Each physical coordinate is queried at most once per path.

For EVERY such adaptive tree, let w_v be its actual physical reach probabilities. With a fixed old booking b, the transaction bill is

    B = b + sum_queries w_v [H(P_v)-avg H(P_children)+L_v]
          + sum_updates w_v D(R_v||Q_v)
          + E_terminal CE(P_terminal,Q_terminal).

Then, with all full terminal laws retained,

    B <= b + CE(P_root,Q_root) + c I(f).                 (1)

In particular one supplied CE<=C0 I certificate pays all these histories at the ONE fixed initial rate C0+c, with b separately retained. The rate does not increase with depth or with the number of profile updates. Existing v9's better fixed-seed rate and margin are not weakened or re-certified here.

## 2. Exact physical-query identity

Write the child Fourier coefficients as a_T and b_T. The parent coefficients in the two i-sectors are (a_T+b_T)/2 and (a_T-b_T)/2. Therefore

    P'(T)=(a_T^2+b_T^2)/2=(P_+(T)+P_-(T))/2.

Every required child true atom is covered by Q'. The KL chain rule on the fibers of pi_i gives L_i>=0, including zero fibers by omission only when their true mass is zero. The mixture identity gives

    avg D(P_children||Q') = D(P'||Q')+J_i,
    avg D(P_children||Q')-D(P||Q) = J_i-L_i.             (2)

These are exact equalities for arbitrary normalized covering Q, regardless of its mass on atoms where P is zero.

The standard two-point logarithmic Sobolev bound gives

    0 <= J_i <= c Inf_i(f).                             (3)

For completeness, this constant has an elementary scalar proof. For real a,b put

    e(a,b)=[a^2 ln(2a^2/(a^2+b^2))+b^2 ln(2b^2/(a^2+b^2))]/2.

Then e(a,b)<=(a-b)^2/2. Replace a,b by their absolute values first; this leaves e unchanged and can only decrease their squared difference. If a+b>0 write a=m(1+t), b=m(1-t), |t|<=1. For j(t)=e(1+t,1-t), j(0)=j'(0)=0 and, on (-1,1),

    j''(t)=2 ln((1-t^2)/(1+t^2))+4/(1+t^2) <= 4.

Twice integrating from zero proves j(t)<=2t^2; continuity supplies the endpoints. The case a=b=0 is zero. Summing over T and dividing by ln 2 proves (3), since Inf_i=sum_T(a_T-b_T)^2/4. All sums are finite.

## 3. Every full profile fee pays for itself

Assume first 0<t<1. Omit q-cell mass zero: cover forces its p-cell mass to be zero too. All remaining r-cell masses are positive. Conditional reference laws cancel from the difference, so exact summation gives

    D(P||Q)-D(P||R)-D(R||Q)
      = ((1-t)/t) [D(r||q)+D(q||r)] >= 0.              (4)

This is A012 v8's paid partial-profile identity, applied to an arbitrary finite partition. At t=0 the update and fee are zero. At t=1, R has p as its profile, the fee is D(p||q), and the left side is exactly zero. A p-cell mass zero may remove reference mass at t=1; its true contribution is zero and the removed mass is accounted for by the full normalized divergence. No division by p-cell mass is required. The identity is not a statement that converting an arbitrary R is free.

## 4. One potential proves all policies

Telescope (2) across the physical queries and the actual changes D(P||R)-D(P||Q) at conversions. Exactly

    E D_terminal + sum_queries w L + sum_updates w fee
      = D_root + sum_queries w J
        + sum_updates w [D_after-D_before+fee].        (5)

Each last bracket is nonpositive by (4). Physical influence obeys

    I(parent)=Inf_i(parent)+avg I(children).

Updates change only Q, so they change no influence. Consequently sum_queries w Inf_i=I(root)-E I_terminal<=I(root). Equations (3)--(5) prove

    E D_terminal + sum_queries w L + sum_updates w fee
       <= D_root + c I(root).                         (6)

The entropy increments in B telescope to H_root-E H_terminal. Substituting (6) proves (1). This argument includes both children, reference-only atoms, constant terminal costs, every old booking b and every executed fee. It proves all finite adaptive policies, not merely all policies in the small census. Equivalently D(P||Q)+c I(current) is a Bellman upper potential for the future terminal-KL-plus-contraction-plus-conversion bill.

The references after different query histories need not be fresh influence-priced child sources. This is an original-root theorem. At an optional stopping node the terminal divergence stays in the potential; it is never reset to zero. The dependence on the actual physical history is retained in w and in the current calibration profile.

## 5. Arbitrary activation references still expose the core

Let g be balanced and let A be an r-control point event, r>=1, p=2^-r, on fresh physical variables. Set F=1-A+Ag. The nonempty-data sector of P_F has mass p, and its conditional law is Uniform(control Fourier sets) times P_g. Exactly

    H(F)=A_r+p H(g),  I(F)=p[I(g)+r],
    A_r=2rp(2-p)-(1-p)^2 log2((1-p)^2).                (7)

For ANY normalized Q_F covering P_F, let q_D be its mass on the nonempty-data sector and define R_g(T)=sum_U Q_F(U,T)/q_D there. This is a normalized reference covering P_g. The sector chain rule followed by projection inside the data sector gives

    D(P_F||Q_F) >= p D(P_g||R_g),
    CE(P_F,Q_F) >= A_r+p CE(P_g,R_g).                 (8)

This retains arbitrary correlations in Q_F; product or calibration hypotheses are unnecessary. Equality is possible for Q_F=P_F. Thus rarity alone does not produce an initial source certificate. For arbitrary h, g=z times a product of m disjoint copies of h is balanced, H(g)=m H(h), I(g)=1+m I(h). Any universal initial CE<=K I supplier for those activated functions implies

    H(h)<=K I(h)+[K(1+r)-A_r/p]/m.

Letting the integer m tend to infinity proves full FEI(K). No unbounded family is brute-force extrapolated: this is the analytic reduction. Projection/profile history stability by itself therefore cannot make the initial supplier noncircular. The prior syntactic grammar still requires actual certificates for both collision children; no arbitrary core is admitted here.

## 6. A scope obstruction that must survive downstream use

For AND2, +1 only at (1,1), the root spectral law has mass 1/4 at all four sets. Query its first coordinate. One true child is constant, P_child=delta_empty. The projected root reference Q'=pi_i P_root has masses (1/2,1/2) on empty and the remaining singleton. By contrast the true-kernel normalized inheritance starting from Q=P yields the actual child law delta_empty. Therefore D(Q'||Q_true-kernel)=infinity.

Projection inheritance is an explicit convention in (1). It cannot be substituted at no charge for a prescribed true-kernel reference. This actual Boolean witness prevents importing (1) into an incompatible moving-witness interface. Additional mandatory floors, arbitrary resets, positive parts of entropy increments, or unspecified execution costs require their own payment. The new theorem addresses their absence, not their cost.

## 7. Proof rung and remaining line

The identities and inequalities above have an analytic proof with exhaustive exact local checks through three variables, rational logarithm bounds, and boundary/negative controls. Independent-agent review remains pending. The attempted Lean target concerns only the integer accounting rearrangement and order transitivity; the checker returned RUNTIME_UNVERIFIED after 45.9 seconds. It supplies no formal certificate. Relative entropy, the two-point inequality, and Boolean Fourier projection are not formalized here.

FIRST UNSUPPORTED LINE: construct an explicit, noncircular initial normalized full reference with CE<=C0 I for every arbitrary Boolean core, compatible with a required productive stopping policy, or supply an influence-priced conversion into the required reference interface. Choosing Q=P proves the source inequality only if FEI is already known. Theorem (1) isolates history stability from that initial-source problem; it does not solve it.
