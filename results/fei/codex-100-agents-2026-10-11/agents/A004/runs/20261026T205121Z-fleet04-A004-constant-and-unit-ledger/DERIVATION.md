# Exact cost of a conditional target floor

Bits are used throughout. Full FEI is OPEN. This is a finite-law payment
identity for an already supplied reference, not an influence-priced source.

## Target and conventions

Let P be a probability on a finite spectral label set with distinguished
empty label 0. Let a=1-P(0)>0. Let R be a complete finite-CE reference of
mass s in (0,1], with w=s-R(0)>0. Write pi=P_nonempty/a and
M=R_nonempty/w. Fix a normalized target T on all nonempty labels, including
reference-only labels, and c in (0,1). A permitted replacement preserves
R(0), w, and s, and changes only its conditional tail to x, subject to
x_j >= l_j=c T_j and sum x_j=1. This class permits changing all tail
profiles. An algorithm fixing some of those profiles has a different class.

## Exact minimizer and proof

There is a unique k>0 such that sum_j max(l_j,k pi_j)=1. Indeed the sum
is continuous, equals c<1 at k=0, tends to infinity, and is strictly
increasing at every level greater than c. Set x*_j=max(l_j,k pi_j).
For pi_j=0 this installs exactly l_j, preserving every required ghost
floor. For pi_j>0, x*_j>0, so every logarithm used below is finite.

For any feasible x define g_j=pi_j/x*_j (zero when pi_j=0).
At a free coordinate x*_j>l_j, g_j=1/k. At a floor coordinate,
0<=g_j<=1/k. Since sum_j(x_j-x*_j)=0,

    sum_j g_j (x_j-x*_j)
      =sum_floor (g_j-1/k)(x_j-l_j) <= 0.

The scalar inequality ln u <= u-1, applied only at pi_j>0, now gives

    D_2(pi||x)-D_2(pi||x*)
      >= -sum_j g_j(x_j-x*_j)/ln 2 >= 0.

If an actual-positive x_j is zero, its objective is infinite and the
comparison is immediate. Strictness of ln u<=u-1 gives equality only
when x=x* on actual support. Every ghost is already at its floor in x*,
so mass conservation forces equality on ghosts too. Thus x* is unique.
The optimal signed COMPLETE CE change is exactly

    Delta*=a [D_2(pi||x*)-D_2(pi||M)].                 (1)

The vacuum bill and tail-mass bill cancel because they are identical on
both sides; they are not omitted from either full bill. In particular
the -log2(s) penalty stays. If P is constant (a=0), no tail replacement
changes CE; if w=0 then finite CE forces a=0. At c=0 the optimum is pi;
at c=1 the only feasible profile is T, and finite CE can fail. These
endpoints must not be included in the c in (0,1) existence assertion.

This characterization is standard constrained cross-entropy optimization.
The campaign contribution is the exact arbitrary-incoming-reference
substitution and the Boolean sign reversal below; no novelty claim is made
for the optimization principle.

Let A={j:l_j>=k pi_j}, including ties, and C its complement. Then
pi(C)>0, k=(1-l(A))/pi(C), and the minimum divergence is

    sum_A pi_j log2(pi_j/l_j)
      +pi(C) log2(pi(C)/(1-l(A))),                    (2)

with zero actual terms interpreted as zero. Feasibility of
(1-c)pi+cT gives the useful but possibly loose bound

    Delta* <= a log2(1/(1-c))-a D_2(pi||M).          (3)

Thus previously paid mismatch can fund a necessary floor. A090's corridor
pi>=cT is the special case x*=pi, Delta*=-a D(pi||M)<=0. Outside that
corridor the price can still be negative. No release can be booked twice.

## Boolean comparison: the choice of permitted profiles changes the sign

Take the two-bit Boolean sign +1 only at input index 0. Its full spectrum
is (1/4,1/4,1/4,1/4), hence a=3/4 and pi=(1/3,1/3,1/3).
Use incoming full reference

    R=(1/4,3/16,15/32,3/32), M=(1/4,5/8,1/8).

Require conditional floor x_1>=1/2, equivalently c=1/2 and T=delta_1.
All references have mass 1 and vacuum 1/4. The exact flexible optimum is
x*=(1/2,1/4,1/4), so its signed full price is

    (1/4) log2(5/8) < 0.                             (4)

If instead the profile on {2,3} is required to stay at incoming ratio 5:1,
the exact optimum is (1/2,5/12,1/12) and its signed full price is

    (1/4) log2(9/8) > 0.                             (5)

The additional compatibility requirement therefore costs exactly
(1/4)log2(9/5)>0. Both classes impose the same floor and use the same
current Boolean source. Calling either price the price of an unspecified
policy is unjustified. This example does not show that a useful FEI policy
permits the less expensive class.

## Source reviews

A090-FREE-TARGET-FLOOR-REPAIR-CORRIDOR@1 follows directly from (1) when
pi>=cT. Reconstruct its original AND3 query from signed characters,
including the constant sibling. The installed conditional pi has floor
8/21>1/4 against T=(7/8,1/16,1/16). The full repaired reference is
(659/2484,1825/7452,1825/7452,1825/7452), dominating one quarter of
(7/12,35/96,5/192,5/192). The original fair reach is 1/2, so its complete
owner release is (3/8)D(pi||M)>1/4 bits. The exact checker certifies the
last strict sign with rational logarithm intervals and retains the sibling.
Verdict: HOLDS at the stated conditional scope, independent reconstruction.

A097's profile-preserving signed minimization has the stated minimizer
z*=max(a,ell) and correct price. Its displayed derivative misses a positive
factor t: differentiating a log2(b/z)+(t-a)log2((t-b)/(t-z)) gives
t(z-a)/(z(t-z)ln2), not (z-a)/(z(t-z)ln2). The sign and all minimization
conclusions survive because t>0. This is a source-level erratum already
flagged by A093 on the board, not a new refutation. The exact independent
test checks both forms and the factor, rather than adopting the incorrect
equality. No repaired source file is written by A004.

## Same original owner and the first unpaid universal line

For any finite physical stopping frontier with actual reaches rho_v and
full current references R_v, let its actual unused original margin be
M0=B-U-sum rho_v CE(P_v,R_v). Preserve every earlier bill U. Replacing
each tail by its permitted x*_v changes the SAME margin exactly to

    M0-sum_v rho_v Delta*_v.                          (6)

Both physical outcomes and full terminal bills occur in the sum. If the
tail occupies a disjoint sector with original full weight beta_v, multiply
its local price by beta_v exactly once. The sum can be negative. There is
no reset of B and no substitution of a different terminal's influence.
Natural-log information multiplies (1)--(6) by ln2. For sign f, I_i is
the full flip probability, equal to spectral inclusion; indicator Fourier
nonempty energies are smaller by 4 and do not change that probability.

The first unsupported universal line remains: construct a useful mandatory
policy whose permissible reference class is specified, and an ORIGINAL
arbitrary-core source with a common O(I) price and enough unused margin to
pay its required projection. Formula (1) computes the debt; it does not
bound that initial source by influence. FEI is still OPEN.
