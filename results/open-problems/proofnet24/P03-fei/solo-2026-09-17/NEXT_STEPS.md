# Precise continuation after the first solo session

## Final update: an exact interference patching theorem

Read `INTERFERENCE_PATCHING_THEOREM_2026-09-18.md`. It subsumes the two
subcube-parity results. For arbitrary selector cells `C_j`, arbitrary signs
`sigma_j` on each cell, and parity labels `D_j`, let `E_j` be the normalized
Fourier entropy of `v_j=1_(C_j)sigma_j`. Let `Lambda` be the maximum
pointwise coherent/incoherent spectral ratio within a repeated data label.
Then

    H(f)<=Lambda[H(J)+sum_j delta_j E_j].

If every cross-cell edge separates the data fibers on at least half the data
cube, two exact nonreuse bounds hold:

    sum_j D(v_j)<=I_x(f),
    H(J)<=2I_x(f).

Consequently local leaf estimates

    E_j<=C D(v_j)/delta_j

patch to the global estimate

    H(f)<=Lambda(C+2)I_x(f).

For subcube cells whose free-coordinate leaf functions already satisfy FEI
with constant `C_0`, one may take `C=max(2,C_0)`. This supplies a recursive
closure mechanism with no repeated influence charge.

The exact missing constructive theorem is now especially concrete: decompose
an arbitrary Boolean function into boundary-separated parity cells with
uniformly bounded `Lambda`, and with leaves in a uniformly FEI-controlled
class. The trivial one-cell decomposition merely restates FEI; point cells
have local constant two but can have unbounded interference and can violate
boundary separation. No such canonical decomposition is proved. The direct
alternative remains the signed multiscale inequality `K<=CI`.

## Update: bounded coherent collisions cost only their interference factor

Read `BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md`. For a
boundary-separated subcube parity multiplexer, repeated data labels may cause
coherent addition of selector Fourier coefficients. If `q_A` is the actual
conditional selector spectrum for data label `A`, `m_A` is the corresponding
incoherent cell mixture, and

    Lambda=max_(A,S:m_A(S)>0) q_A(S)/m_A(S),

then

    H(f)<=4 Lambda I_x(f).

If each data parity occurs on at most `R` cells, Cauchy--Schwarz gives
`Lambda<=R`. The engine is the dimension-free entropy lemma `q<=Lambda m`
implies `H(q)<=Lambda H(m)`, with no additive `log Lambda` term.

This strictly extends the distinct-label theorem, but it does not solve the
decomposition problem. An arbitrary Boolean selector can be represented by
point cells all sharing one data label, so unbounded collision already
contains full FEI. Also, without boundary separation a cell partition can
have large description entropy but zero functional influence. The next
positive target is therefore a canonical decomposition theorem producing
bounded `Lambda` and boundary separation while charging each selector edge
only once. No such theorem is proved.

## Update: exact nonreuse succeeds for subcube parity multiplexers

Read `SUBCUBE_PARITY_MULTIPLEXERS_2026-09-18.md` before trying to generalize
the earlier degree-one selector lemma. If selector space is partitioned into
subcubes `C_j`, and each cell selects a distinct signed data parity, then

    H(f)=2H(J)<=4I_x(f)<=4I(f).

The selected parities may have arbitrary degree and the cells may have unequal
codimensions. Ordinary addressing shows the class constant four is
asymptotically sharp. More generally, for an arbitrary parity multiplexer
`f(x,y)=sigma(x)chi_(D(x))(y)`, without subcube cells,

    B_y(f)<=H(D)<=2I_x(f).

This is the first retained route here that handles genuinely higher-degree
data interactions without reusing selector influence: data Fourier labels are
nonoverlapping, and subcube conditional spectra have exactly the prefix-code
entropy. The boundary is exact. Repeated data labels cause Fourier
interference; arbitrary cells replace the exact conditional entropy by a
partial-Boolean spectrum, which is FEI-hard; arbitrary fiber functions overlap
at many data frequencies.

The most concrete positive continuation is to find a decomposition of a
general Boolean function into a controlled number of nearly nonoverlapping
parity-multiplexer pieces while charging selector boundaries only once. No
such decomposition or approximation theorem is proved.

## Update: favorable-coordinate and aggregate NAND-potential induction also fail

Read `SYMMETRIC_MOD8_RESTRICTION_BARRIER_2026-09-18.md` before attempting any
coordinate-selection repair of the Shannon barrier. For `8|n`, the transitive
indicator

    A_n(x)=1{|x| mod 8 in {0,1,2}}

has the same restriction defect at every coordinate, and for every fixed
singleton correction `W_c=U+cQ`,

    D_i(A_n)/Inf_i(1-2A_n)=gamma n+o(n),

where

    gamma=(3sqrt(2)/8)sin^2(pi/8)log_2(cot^2(pi/8))>0.

Therefore neither choosing a favorable coordinate nor summing all coordinate
defects can give a dimension-free restriction recursion for this potential.
The proof uses an exact eighth-root filter and three separated spectral bands;
the exact rational-interval certificate verifies growth through n=64.

The NAND potential survives only in its proved disjoint-product setting. Do
not try another fixed `Q` retuning or coordinate-selection rule. A remaining
restriction route would have to be genuinely nonlocal at the block level and
not reduce to a sum of one-coordinate defects. The direct full-scope target
`K<=CI` and signed multiscale transport remain open.

## Update: the NAND potential does not extend to Shannon restriction

Read `SHANNON_POTENTIAL_BARRIER_2026-09-18.md` together with `UNEQUAL_NAND_CONTRACTION_2026-09-18.md`.

The potential

    V(A)=K_A-2Q_A log_2(EA)+(2/ln2)Q_A

contracts under arbitrary unequal disjoint NAND, but no universal local restriction inequality

    V(A)<=average[V(A_0),V(A_1)]+C Inf_selector(1-2A)

can hold. More strongly, replacing V by any `U+cQ` with fixed real c does not help. For the explicit even-dimensional bent function with one physical value flipped, exact coefficient formulas give the same leading defect for every such c:

    [V(A)-average(V(A_0),V(A_1))]/Inf_selector
      =[1/4+1/(2ln2)+o(1)]m.

The selector influence is 2^(-m). This is an all-m asymptotic proof, with full exact Walsh checks through m=12 for the actual NAND potential. This bent-marker obstruction by itself is local rather than aggregate and does not refute choosing a favorable coordinate. The later transitive mod-8 family does refute both favorable-coordinate and aggregate versions. Neither family shows `V/I` is unbounded. A genuinely nonlocal block selection theorem or global multiscale payment is not ruled out.

The surviving use of V is therefore composition stability after a seed bound is known. It does not generate a seed bound. Further work should return to a genuinely aggregate non-reusing scale allocation or a proper-block selection theorem, not another local potential of the same restriction form.

## Update: unequal NAND contraction

Read `UNEQUAL_NAND_CONTRACTION_2026-09-18.md` before returning to the composition identity in `NAND_LOG_POTENTIAL_2026-09-18.md`.

The unequal-block correction is now controlled. For an indicator A of mean alpha, singleton-square mass Q_A, and indicator edge functional K_A, define

    V(A)=K_A-2Q_A log_2(alpha)+(2/ln2)Q_A.

If A'=1-product_j A_j on disjoint blocks and w_j=product_{l!=j} alpha_l, then

    V(A')<=sum_j w_j V(A_j),
    I_A'=sum_j w_j I_Aj.

The proof uses `-w log_2 w<=(1-w)/ln2`; the resulting positive correction is paid exactly by the loss from `sum w_j Q_Aj` to `Q_A'=sum w_j^2 Q_Aj`. No equality of child means is needed. Also K(1-2A)<=4V(A).

Consequently every read-once NAND/De Morgan formula satisfies

    K/I<=2+2/ln2,  B/I<=2+4/ln2,  H/I<=2+6/ln2.

This function class was already covered by the O'Donnell--Tan composition theorem, so the class result is not claimed as new. The useful step is that the live logarithmic potential survives arbitrary unequal composition. It still leaves arbitrary Boolean seeds entirely uncontrolled; a composition theorem alone cannot prove full FEI.

## Update: signed cancellation and parity-query barriers

Read `SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md` before proposing a signed-scale or linear-coordinate shortcut.

Booleanity gives an exact fact for every nonzero spectral translation U: same-sign and opposite-sign coefficient pairs have equal total absolute overlap. This is not scale-local. For the one-point defect, those two overlap totals agree exactly in every coordinate direction, but all of the logarithmic edge functional lies on the single opposite-sign edge while all same-sign edges have zero log ratio. A successful argument needs a quantitative transport of cancelling mass across magnitude scales, not merely the unweighted signed convolution identity.

The same family blocks arbitrary fixed linear changes of spectral coordinates. Every nonzero generalized influence is 2/2^n, so any spanning parity family followed by marginal entropy costs at least n h_2(2/2^n), an unbounded factor above I=2n/2^n. Redundant fixed measurements do not help.

Conditioned or adaptive parity queries avoid that particular marginal bound, but their branch spectra are normalized Fourier spectra of partial Boolean functions. This is an exact closure, not a loose relaxation: every {0,+1,-1}-valued function is one projection branch of a Boolean parent after adjoining one bit. The partial class is FEI-hard by the selector lift and tensor amplification. After two projections, even partial Boolean values need not persist. Therefore a viable parity code must exploit the coupled branches and the original Boolean convolution identities globally; it cannot invoke the desired inequality independently on each child.

The remaining direct target is unchanged:

    K=sum_edges min(p_S,p_T)|log_2(p_S/p_T)| <= C I.

The sharpest live question from this update is whether exact signed cancellation supports a non-reusing multiscale transport whose cost is charged to the original degree budget. No such transport inequality is proved.

## Update: block restriction and erasure synergy

Read `ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md` and `BLOCK_RESTRICTION_IDENTITY_2026-09-18.md` before proposing another erasure-based induction.

For every odd m>=3, one selector mixes restriction spectra uniform on even and odd parity. Each restriction has B=0, but the full selector function is bent and has B=m+1, while the selector influence is 1/2. Consequently:

- block erasure cannot be bounded by average fiber erasure plus a constant times selector influence;
- one bit of selector/spectrum mutual information can create m bits of aggregate erasure through parity synergy;
- no fixed potential B+lambda(H-B) with lambda<1 has a dimension-free one-coordinate restriction inequality.

The complementary quantity D=H-B is not an easy remainder. The parity lift

    f(x_1,...,x_n,z)=g(x_1 z,...,x_n z)

has H(f)=D(f)=H(g), B(f)=K(f)=0, and I(f)<=2I(g). Hence a universal D<=C I is equivalent to full FEI up to factor two. More strongly, FEI restricted to functions supported only on even Fourier levels is already FEI-complete up to factor two. Fixing z=+1 recovers g, so this zero-erasure class is not restriction-closed.

The exact general block identity for a physical restriction block A is

    H(f)-E_x H(f_x)
       =H(Z_A|Z_{A^c})+I(X_A;D),
    I(X_A;D)<=(2/ln2) I_A(f).

Here D is the spectral subset on the unrestrained coordinates drawn from the restriction spectrum. Thus a genuine remaining restriction route is to select a proper block A with

    H(Z_A|Z_{A^c})<=K I_A(f)

without hiding the original FEI assertion in A=all coordinates. No such selection theorem is proved. It must survive both the older bent-marker local obstruction and the new parity-synergy obstruction.

The direct logarithmic alternative remains K<=C I for

    K=sum_edges min(p_S,p_T)|log_2(p_S/p_T)|.

Note that the parity lift has no positive spectral edges at its top level, even though one restriction recovers an arbitrary FEI instance. A successful edge proof must therefore be compatible with complexity created under restriction, rather than looking only at the current support graph.

## Update: 2026-09-18 continuation

The proposed interior-moment attack below is now **disproved for every fixed gamma>0**, not only gamma=1/2. Read `ADDRESSING_BARRIER_2026-09-18.md` first. An explicit bent/addressing family has

    I=(m+2)/2,  T_gamma=(m+1+2^(gamma m))/2,  H/I<3.

It also defeats every superlinear majorant of the logarithmic edge contrast along even scales and every universal nonincreasing integrable tail envelope. The actual logarithm is critical. Do not repeat power-moment searches.

The new exact live notation is

    K=sum_edges min(p_S,p_T) |log_2(p_S/p_T)|,
    K<=B<=K+(2/ln2)I.

Thus K<=C I remains a full-scope target, not a proved inequality. The addressing family has K=m/2 and shows how large data-coordinate contrasts can consume selector influence while data influence alone is small.

Two substantive limited steps are retained:

1. `SELECTOR_CHARGING_2026-09-18.md` proves B_data<=H(input selector label)<=2 I_selector whenever f is affine in the data bits. It identifies the precise failure for overlapping higher-degree data terms and the repeated-credit problem. Its final section refutes replacing this special label by the full local sensitivity pattern.
2. `NAND_LOG_POTENTIAL_2026-09-18.md` proves a dimension-free growth bound for the exact indicator logarithmic functional under identical-block NAND of arbitrary changing arity. It also proves why that potential fails for unequal blocks and derives a complement-invariant correction U(A) with an unresolved signed product term.

Next useful work must either construct a non-reusing logarithmic payment for general Boolean spectra, exploit a genuinely different signed structure, or refute another necessary intermediate assertion. A restricted composition proof alone still does not cover arbitrary Boolean seeds. See the newest report for exact certificates, runtime limits and prior-art caveats.

## Historical initial continuation below (preserved for provenance)

Full FEI remains OPEN. The aggregate erasure reduction is proved, but no finite universal upper bound for B/I has been established. The original fixed-dimension P03 atlas was not changed.

## Do not repeat these failures

1. A universal payment for every restriction coordinate is false: the bent-marker family has Delta_i/Inf_i=m+3/ln(2)+o(1).
2. The tentative constant B<=4I is false: the exact 80-variable NAND certificate gives B/I>4.007.
3. The aggregate absolute-overlap estimate R<=CI is false for every C: an explicit all-depth family has R/I>(4/5)d.
4. Jensen averaging of downward spectral ratios loses log(n/I).
5. A convex relaxation of squared Fourier laws alone includes arbitrary probability laws: the Boolean characters supply every point mass. Independent Bernoulli laws already violate a universal B/I bound. The signed Boolean constraints cannot be discarded.

## The actual remaining inequality

For a real coefficient vector a whose inverse Walsh transform is Boolean, and p_S=a_S^2, prove

    sum_S p_S sum_{i in S} log_2(1+p_{S-i}/p_S)
       <= C sum_S |S|p_S

for some finite universal C, or find an actual Boolean family for which the ratio is unbounded. The left-hand side is L(f); ERASURE_REDUCTION.md proves L<=B<=L+I/ln2. The constraints are

    sum_S a_S a_{S xor U}=1_{U=empty}  for every U.

New equivalent notation is not itself further progress. The next contribution should actually control a nontrivial part of this logarithmic term, identify a new obstruction, or find another genuine full-scope proof mechanism.

## Historical moment attack: now disproved as described above

Instead of the failed square-root majorant, introduce

    T_gamma(f)=sum_edges min(p_S,p_T)^(1-gamma) max(p_S,p_T)^gamma,
    0<gamma<1/2.

At gamma=0, T_0<=I by orienting each edge toward its endpoint containing the changed coordinate. At gamma=1/2, T_{1/2}=R/2, and its normalized ratio is unbounded by the theorem already proved. This does not decide any interior gamma.

For 0<gamma<=1/2, the scalar estimate

    E(r,s)<=[exp(2gamma-1)/(gamma ln2)]
                   min(r,s)^(1-gamma) max(r,s)^gamma

is elementary: put q=ln(max/min)>=0, bound E/min in nats by q+2, then maximize (q+2)exp(-gamma q). Thus a universal bound for T_{1/4}/I would imply FEI. This is a **stronger sufficient target**, not an established equivalent conjecture; it may be false. Try to refute it first with structurally chosen Boolean examples.

For disjoint NAND of k identical indicator functions with mean alpha and singleton coefficients t_i, the exact homogeneous recursion is

    T_gamma(A')=k alpha^(k-1) T_gamma(A)
       +k alpha^((2-2gamma)(k-1))
          [(1-alpha^k)^(2gamma)-alpha^(2k gamma)]
          sum_i |t_i|^(2-2gamma).

Here T_gamma(A) uses the unnormalized squared Fourier coefficients of the indicator. The ordering required for this formula is valid: both a function and its complement bound the absolute value of each of their nonempty Fourier coefficients by their own mean. Product coefficients inherit this property.

Near the NAND fixed point alpha=phi, the extra singleton moment divided by influence contracts geometrically for gamma<1/2, whereas the gamma=1/2 correction does not contract. That explains the proved overlap obstruction and suggests testing whether the interior moment can be controlled in more general Boolean functions. It is not a universal proof.

Suggested next methods: (5) vary gamma, (13) look for an amortized potential retaining signed Boolean cancellations, (30) separate spectral-mass scales. Avoid treating floating-point plateaus as bounds. If the stronger moment fails, return to the logarithmic residual rather than insisting on it.

## Other routes still available

- Derive a signed transport or cancellation estimate directly from the convolution constraints, with no reused credit.
- Investigate whether a random restriction can reduce the logarithmic residual on average while retaining its actual influence cost.
- Use the precise near-fixed-point NAND recurrence as an adversarial test for any new scalar majorant or amortized potential.

Search primary literature before claiming novelty. Existing coordinate-restriction and composition frameworks are acknowledged in the accompanying notes.
