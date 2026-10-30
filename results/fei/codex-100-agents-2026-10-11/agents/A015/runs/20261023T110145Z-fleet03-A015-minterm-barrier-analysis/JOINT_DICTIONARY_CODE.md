# A shared dictionary is transmitted once, not at each child visit

All costs are base-two ideal cross-entropies. This is a NEW normalized
whole-set reference, not the original prime queue, a thinning of that queue,
or a reference reset along a history. No entropy upper bound is used to
pay its cost. The family is the actual obstruction supplied by A008, with
an additional independent mixed-width generalization.

## General exact two-component code identity

Let U(X),V(Y) be nonconstant {0,1}-valued functions on DISJOINT uniform
blocks. Put a=E U, b=E V, g=2U-1, h=2V-1 and F=2UV-1. Let q_g,q_h be
ANY fixed positive normalized references on the nonempty subsets of their
blocks. Write C_g=sum_(S!=empty) ghat(S)^2 log(1/q_g(S)), and similarly C_h.
Define a normalized nonempty output reference Q by choosing uniformly one
of the THREE sectors X-only, Y-only and both. In a used block sample its
nonempty set from q_g or q_h independently. Thus

    Q(S,empty)=q_g(S)/3,
    Q(empty,T)=q_h(T)/3,
    Q(S,T)=q_g(S)q_h(T)/3.                              (1)

The decoder knows the two physical dictionaries; the sector identifies
which are used and is paid ONCE. Each reference is fixed before sampling.
The sector masses under the actual Fourier law are

    (2ab-1)^2, b^2 v_g, a^2 v_h, v_g v_h/4,
    v_g=4a(1-a), v_h=4b(1-b).

Indeed nonempty Fourier coefficients are b ghat(S), a hhat(T), and
ghat(S)hhat(T)/2. Therefore the EXACT complete nonempty cost and influence
are

    C_Q(F)=Var(F)log3+b C_g+a C_h,
    I(F)=b I(g)+a I(h).                                (2)

For example, the coefficient of C_g is b^2+v_h/4=b. This is a statement
about the complete normalized reference, not merely selected witnesses.
If C_g<=K I(g) and C_h<=K I(h), (2) gives

    C_Q(F)<=(K+log3)I(F),                               (3)

using Var(F)<=I(F), directly from Parseval and |S|>=1 on nonempty sets.
This is a reusable one-level paid dictionary interface, not a dimension-free
closure under unlimited composition: repeatedly paying log3 needs an
original surplus account. DISJOINTNESS is essential. In particular U=V=OR2
on the same two bits has actual I(2UV-1)=1 while the invalid independent
formula would give3/2. Shared-variable versions are not inferred.

## A fixed explicit clause dictionary, with its full normalizer

For integer w>=4 let r=2^w. Partition a block into r disjoint clauses with
widths d_j in{w,w+1}; choose any pattern BEFORE sampling. Put

    U=prod_j OR_(d_j), epsilon_j=2^-d_j,
    p_j=1-epsilon_j, a=prod_j p_j, g=2U-1.

The fixed clause reference uses rho=1/(2r), independent of the width pattern:
draw independent Bernoulli(rho) clause activations, condition the WHOLE mask
on being nonempty, then in each active clause choose one nonempty coordinate
subset uniformly. Clause identities are communicated by that mask once;
there are no repeated child-name draws, branching counts or attachments in
this NEW sampler. For nonempty physical S, let J(S) be its active clauses.
Its exact probability is

    q_rho(S)= [rho^|J| (1-rho)^(r-|J|)
                prod_(j in J)(2^d_j-1)^-1] / Z_rho,
    Z_rho=1-(1-rho)^r.                                 (4)

Every nonempty S has positive mass; summing the independent subsets and
then all nonempty masks gives exactly1. The negative log of (4) includes
log Z_rho with its proper NEGATIVE sign, each inactive clause, each active
clause name and each within-clause subset. Nothing is omitted as a free
gate normalization or posterior refund. No actual Fourier law is substituted
for q_rho: rho=1/(2r), whereas epsilon_j may be1/r or1/(2r).

Bernoulli's inequality gives (1-1/(2r))^r>=1/2, hence
r log(1/(1-rho))<=1. Since log(1/rho)=w+1 and
log(2^d_j-1)<d_j, (4) implies the pointwise full length bound

    log(1/q_rho(S))
      <=1+sum_(j in J)(w+1+d_j)
      <=1+(9/4)sum_(j in J)d_j.                        (5)

To obtain (5), discard the nonpositive log Z_rho and the nonpositive
|J|log(1-rho) only AFTER retaining them in (4). Because d_j>=w>=4,
w+1+d_j<=2d_j+d_j/4. No asymptotic logarithm estimate is used.

## Actual Boolean Fourier moments pay every code factor

The squared Fourier coefficients of the indicator U, divided by its total
mass a=E U, form an independent product measure: clause j is empty with
probability p_j, and every one of its2^d_j-1 nonempty subsets has mass
epsilon_j^2/p_j. Its total nonempty probability is epsilon_j because
(2^d_j-1)epsilon_j^2=epsilon_j p_j. This product law is used ONLY to compute
the actual spectral moments, not as the code reference.

On nonempty S, ghat(S)^2=4a times that product probability. Direct pivotal
counting and the active-clause moment give

    I(g)=2a sum_j d_j epsilon_j/p_j,
    sum_(S!=empty) ghat(S)^2 sum_(j in J(S))d_j
        =4a sum_j d_j epsilon_j <=2I(g).                (6)

A positive active clause already forces S nonempty, so no extra conditioning
factor is lost in the second identity. With Var(g)<=I(g), (5)--(6) prove

    C_g(q_rho)<=(11/2)I(g).                            (7)

This pays the ENTIRE local reference, including the mask and its successful
nonempty normalization, not only a chosen clause tag or a residual.

## Complete joint-sector payment on the actual obstruction

Take independent blocks with possibly DIFFERENT integers w_X,w_Y>=4 and
their own r_X=2^w_X,r_Y=2^w_Y and arbitrary width patterns. Define U_X,U_Y
as above, V_Y=1-U_Y(-Y), and F=2U_X V_Y-1. The nonempty spectrum of
h=2V_Y-1 differs from that of g_Y only by coefficient signs. Use its Y
dictionary q_rhoY on the same physical subsets. Apply (1), with each local
mask sampled only once. Equations(2),(7) yield

    C_Q(F)<=[11/2+log3]I(F)<8I(F).                      (8)

This includes ALL X-only, Y-only and joint sectors, every subset in every
used clause, and the sector/dictionary tag. It includes A008's original
family w_X=w_Y=w, all widths w. Its fixed two-polarity queue mixture still
has cost/I>w/2592 for w>=32; that theorem concerns a DIFFERENT reference
and is not contradicted by (8).

For a FULL code, add the actual empty/nonempty wrapper:
Q_full(empty)=1-v and Q_full(A)=v Q(A), v=Var(F). Its cost is h2(v)+C_Q(F).
For completeness I(F)>1 here. Each local a_i exceeds1/4: since
(1+1/(r-1))^(r-1)<sum_(j>=0)1/j!<3, we have
(1-1/r)^(r-1)>1/3, and r>=4 gives(1-1/r)^r>1/4.
Every pattern has a_i>=that product. Also sum d_j epsilon_j>=w_i/2,
so I(g_i)>=a_i w_i. Writing a=a_X and b=1-a_Y, exact physical composition
gives

    I(F)=b I(g_X)+a I(g_Y)
       >=a[b w_X+a_Y w_Y]>=4a>1.

Thus h2(v)<=1<I(F), and

    C_full(F)<[13/2+log3]I(F)<9I(F).                    (9)

The infinite-series bound above is elementary: j!>=2^(j-1) for j>=2,
strict from j>=3, so sum1/j!<3. Binomial coefficients in the preceding
finite product are bounded by1/j! termwise. No giant truth table or giant
exact rational power is required for these all-parameter estimates.

## Connection to the universal bridge and exact unpaid line

The new reference pays precisely the WHOLE-SET shared-dictionary feature
missing from the refuted original queues. It is a fresh root representation,
not a free reset or retuning from an already spent source. Once supplied,
its positive normalized nonempty Q can be projected with the SAME original
reference through arbitrary restriction histories by A015 stage8's transport
theorem; that application remains conditional on its pending independent
review and does not create or renew a bank.

For arbitrary Boolean covers, disjoint clause factorization and the moment
identity(6) need not hold. No universal rule finds or pays such dictionaries
under physical overlap, and (3) alone accumulates a tag cost at repeated
composition levels. The first unsupported line is a full influence-paid
joint dictionary reference for overlapping, nonsymmetric physical supports,
retaining joint conditioning and every output ambiguity. Full FEI is OPEN.
