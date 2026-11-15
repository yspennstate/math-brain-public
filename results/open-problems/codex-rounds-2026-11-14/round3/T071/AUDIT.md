# Independent checks of the four-label criterion

All checks are analytic. No simulated data or numerical workload is used.

## 1. Generator calculation independent of route conditioning

Lump the target B_4 into states 4,3,31,22,1. Here 3 necessarily has block
sizes 2+1+1, while 31 and 22 specify the two possible two-block shapes.
The generator is

    Q = [ -3    2    2/3     0    1/3
           0   -2     1     1/2   1/2
           0    0    -1      0     1
           0    0     0     -1     1
           0    0     0      0     0 ].

Rows sum to zero. From three blocks the two pairs involving the existing
doubleton produce 31 at total rate one; the pair of singleton blocks
produces 22 at rate 1/2. This checks that block sizes do not change the
specified block-merger rates.

Discount at rate s while in 4, r while in 3, and q while in a two-block
state. With terminal payoff one, the backward equations are

    f_31=f_22=1/(q+1),
    (r+2)f_3=1/2+f_31+(1/2)f_22,
    (s+3)f_4=1/3+2f_3+(2/3)f_31.

Substitution gives exactly PROOF.md (1). This derivation uses neither the
route probabilities nor the claimed independence of holding times.

For a payoff restricted to absorption through 22, replace f_31 by zero,
set the direct absorption payoffs from 4 and 3 to zero, keep
f_22=1/(q+1), and use

    g_3 = (1/2)/((r+2)(q+1)),
    g_4 = 2g_3/(s+3) = 1/((s+3)(r+2)(q+1)).

This is the target transform with the canonical mark D. Subtract its values
at q and zero to obtain

    g_4(s,r,0)-g_4(s,r,q)
       = q/((s+3)(r+2)(q+1)),

which independently checks the marked transform (2). In particular the
probability of ever visiting 22 is g_4(0,0,0)=1/6.

## 2. Forward equations and a root-time check

Writing u=exp(-t), the forward equations from Q give

    p_4=u^3,
    p_3=2(u^2-u^3),
    p_22=(1/2)u-u^2+(1/2)u^3,
    p_31=(4/3)u-2u^2+(2/3)u^3,
    p_1=1-(11/6)u+u^2-(1/6)u^3.

For example p_22'+p_22=(1/2)p_3 and
p_31'+p_31=(2/3)p_4+p_3, both with zero initial values. These identities
verify the formulas by differentiation. They sum to one and are nonnegative,
also evident from their integral forms with nonnegative incoming fluxes.
At t=log 2 the probabilities in the order 4,3,31,22,1 are

    1/8, 1/4, 1/4, 1/16, 5/16.

The integrated entry flux into 22 is

    integral_0^infinity (1/2)p_3(t)dt = 1/2-1/3 = 1/6,

agreeing with the independent marked-transform value.

The absorption time V has density

    (11/6)exp(-t)-2exp(-2t)+(1/2)exp(-3t).

Its Laplace transform is

    11/(6(s+1))-2/(s+2)+1/(2(s+3)).

This equals F(s,s,s), as required by V=S+H+G. At s=1 both give 3/8.
Integrating the tail gives E V=11/6-1/2+1/18=25/18.
Separately the route law gives

    E S=1/3,  E H=1/3,  E G=13/18,

which sum to 25/18. These are target moments; no convergence of finite-n
moments is asserted without uniform integrability.

## 3. Dependence and transform spot checks

The correct H marginal is (1/3)delta_0+(2/3)Exp(2). The correct G marginal
is (5/18)delta_0+(13/18)Exp(1). Their expectations agree with Section 2.
They are not independent. Only the route 4 to 3 to 2 to 1 contributes to HG,
so E HG=(1/2)(1/2)(1)=1/4 and

    Cov(H,G)=1/4-(1/3)(13/18)=1/108.

The target first time S is independent of (H,G), as the s factor in F
also shows. Assuming all three times independent would be an error.

| (s,r,q) | F(s,r,q) | M(s,r,q) |
|---|---:|---:|
| (0,0,0) | 1 | 0 |
| (1,0,0) | 3/4 | 0 |
| (0,1,0) | 7/9 | 0 |
| (0,0,1) | 23/36 | 1/12 |
| (0,1,1) | 1/2 | 1/18 |
| (1,1,1) | 3/8 | 1/24 |

These are substitutions in the displayed rational formulas. Independently,
the first three F entries follow from Exp(3) and the H marginal, the fourth
from the G marginal, and the last from the absorption density in Section 2.
The M entries follow from mass 1/6 and independent Exp(3),Exp(2),Exp(1)
coordinates conditional on D=1, by (3) of PROOF.md.

## 4. Burst constant checked two ways

Integrating the target balanced-shape subdensity gives

    integral_0^T exp(-3u)du
      * integral_0^h exp(-2v)dv
      * integral_epsilon^infinity exp(-w)dw
      = (1-exp(-3T))(1-exp(-2h))exp(-epsilon)/6.

Alternatively condition on ever visiting 22, which has probability 1/6.
Its conditional S,H,G laws are independent exponentials with rates 3,2,1.
Multiplying their three CDF/tail factors gives the same constant. Since
1-exp(-2h) divided by h tends to 2, the linear coefficient is
(1-exp(-3T))exp(-epsilon)/3. The iterated zero limit in the proof is correct.

## 5. Counterexample checked by exhaustive coin counts

On four blocks there are sixteen equally likely coin assignments:

- Two all-equal assignments give a quadruple.
- Eight assignments give a triple and singleton: two for each of four splits.
- Six assignments give two pairs: two for each of three pairings.

There is no assignment producing one pair and two separate singleton blocks.
At event rate 2/3 this gives rates 1/12 for each specified split and for the
quadruple. Add the rate-1/3 star event and rate-1/3 pair clocks. The aggregate
rates out of four blocks are then

    to 3: 2;  to 31: 1/3;  to 22: 1/4;  to 1: 5/12.

Their sum is 3. On three blocks, two of eight assignments are all equal and
each specified pair/singleton split occurs twice. On two blocks, two of four
assignments agree. This checks all restricted rates independently of the
four-block table and confirms exact B_3 laws. In particular all individual
pair MRCA times are Exp(1), too.

Replace the first row of Q by (-3,2,1/3,1/4,5/12). Other rows are unchanged,
since three-block rates are exactly those of B_3. The forward equation gives

    p_22^counter=(5/8)u-u^2+(3/8)u^3.

Subtracting the target expression gives (u-u^3)/8. Independently, only
the extra direct entry flux (1/4)p_4 contributes to this difference; convolving
it with Exp(1) survival gives

    (1/4) integral_0^t exp(-3v)exp(-(t-v))dv = (u-u^3)/8.

At t=log 2, target p_22=1/16=4/64 and counterexample p_22=7/64, a gap 3/64.

Finally, the probability the first event is a direct two-pair event is
(1/4)/3=1/12. Its time is independent Exp(3), and its positive two-block
holding time is Exp(1). Thus its disjoint-burst atom is
(1-exp(-3T))exp(-epsilon)/12. Integrating the direct first-event density
(1/4)exp(-3t) gives the same value. Ordinary successive pair events have
strictly positive spacing with a density and add no atom at H=0.

## 6. Attempts to invalidate the criterion

- The second-smallest pair time must count multiplicity. A first triple
  creates three equal pair times; a quadruple creates six. With multiplicity,
  it is exactly U. Without multiplicity the assertion would be false.
- Two block shapes exhaust binary four-label chains: 2+2 has six ordered
  chains and 3+1 has twelve. Label permutations are transitive on each set.
  This justifies conditional uniformity without finite-n Markov dynamics.
- At H=0<G, a uniform nested chain gives a uniform triple because each triple
  contains three possible first pairs. At G=0 the shape of the two-block
  state is invisible; both choices give the same law of the visible states.
- A raw D_n transform is too strong: binary resolutions of a quadruple can
  choose balanced or nested intermediate states arbitrarily. The weighted
  statistic suppresses precisely this freedom. The finite measure in the
  sufficiency proof is uniquely determined including its total mass.
- Neither division by 1-exp(-G) on {G>0} nor the compactification proof assumes
  a lower bound on G. Division identifies a measure on each {G>=1/m}, then
  their union identifies it on {G>0}. There is no division at zero.
- Excluding G near zero in the burst event is necessary; a valid quadruple
  burst can contain two disjoint binary mergers and then a third merger.
- Binary resolution times in the counterexample remain ordered across
  distinct original events: the last merger of event j has delay R_j/n,
  while the first merger of event j+1 has delay (R_j+1)/n. Their original
  times are strictly ordered. Total delay for four labels is at most 3/n.
- The counterexample's unresolved rules are consistent across arbitrary
  finite samples. Only fixed-sample binary approximations are claimed;
  no construction of an N-BBM population, or of consistent binary refinements
  simultaneously for all sample sizes, is asserted.
- Samples from bounded rescaled history do not determine these global time
  transforms. Increasing available history or an explicit stationary regime
  is still needed for applying the criterion to the intended conjecture.

No failure was found in the auxiliary theorem. The finite-N estimates (1)
and (2), even for four labels, remain unproved for N-BBM.
