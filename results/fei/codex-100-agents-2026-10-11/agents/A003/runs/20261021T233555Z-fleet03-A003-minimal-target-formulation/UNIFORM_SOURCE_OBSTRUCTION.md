# No edit-mass price for canonical resets, even with a fixed source price

The first eight-bit counterexample only settles the sign. The following family rules out any universal reset allowance proportional to the size of the edit, while keeping the ORIGINAL source reference uniformly influence-priced. It still does not refute A096's paid whole-bank theorem.

For every integer m>=4 set a=r=m, b=1, s=2^-m and e=s^2. Thus the actual Boolean function on 2m+1 physical coordinates is

    F_m=1-2 A_m+2 A_(2m+1).

The underlying source is g_m=1-2 A_m on m+1 coordinates, one of them dummy. Its source law is P_g(0)=(1-2s)^2 and P_g(T)=4s^2 on the 2^m-1 nonempty active Fourier sets. Its total influence is 2ms. Give it exactly the reference from DERIVATION section2: use the actual e=s^2, a singleton j of the active block and the dummy singleton d,

    R(0)=(1-2s)^2,
    R(T)=e^3 P_g(T) for T!=0,
    R(j)+=4s(1-s)(1-e-e^3),
    R(d)+=4s(1-s)e.

All positive source atoms have positive reference mass. The reference is calibrated and normalized. Both joint floors after completion have full support on their actual finite Fourier cubes. Use the SAME incoming floor and the SAME canonical on-cell reset, retaining the full complementary constant-child reference as in DERIVATION section3.

## Uniform source cost

Let c_m=CE(P_g,R). For s<=1/16, 1-e-e^3>3/4 and 4s(1-s)>=15s/4, so R(j)>=s. Also -(1-2s)^2 log2((1-2s)^2)<=4s/ln2<6s. Every nonempty active atom other than j has reference mass 4s^8 and code length 8m-2. Consequently

    c_m <=6s+4s^2 m+4s(8m-2)
         =32ms-2s+4ms^2
         <=34ms=17 I(g_m).

The final inequality uses s<=1/2, so 4ms^2<=2ms. No source-vacuum or source-positive atom is omitted. Thus ONE C0=17 works for every m>=4. A096's supplied-source original-bank rate is the same K=44 for this entire family.

## Exact grouped likelihood and its scaling

Set k=1-s, mu=1-2s, v=4s(1-s), L=1/s and

    Rj=v(1-s^2-s^6)+4s^8,
    beta=2(1-2s)/[s^2(1-s+s^4(1-2s))],
    qj=s^2(4-3s), u=k Rj+s^3,
    p0=(1-4s+2s^2)^2,
    o0=(1-2s+s^2)^2+u(2s-s^2)^2/qj.

All expressions have positive denominators for 0<s<=1/16. The squared child Fourier law and old/new complete references split into these five groups. The first column is total true mass; the second is old-reference/new-reference ratio:

| True mass | Reference ratio |
|---|---|
| p0 | o0/p0 |
| (L-1)4s^4 | (1+u/qj)/4 |
| (1/(2s)-1)4qj | (k 8s^8+2s^3)/(k beta 8s^8+4s^3) |
| 4s^3 | (k v s^2+2s^3)/(k beta v s^2+4s^3) |
| (1/(2s)-1)4s^3 | 1/2 |

Their masses sum exactly to one. Twice the expected reset Z_m is the mass-weighted sum of the logarithms of these ratios. This is the physical on-child half reach; the unchanged complementary child has zero reset cost and retains its entire inherited CE.

As s decreases to zero through s=2^-m, o0=1+O(s^2) and p0=1-8s+O(s^2). Therefore the first group's contribution divided by s tends to 8/ln2 (the derivative of log at1). The third group's mass divided by s tends to8 and its ratio tends to1/2, yielding -8. The second group's mass is O(s^3) and its ratio is comparable to1/s. The fourth group's mass is 4s^3 and its ratio is comparable to s^2. Their contributions divided by s tend to zero by s^2 log(s)->0. The fifth group's mass is O(s^2), and its ratio is fixed. Thus

    Z_m/s -> 4/ln2-4 >0,
    Z_m/Inf_j(F_m) -> 2/ln2-2 >0,
    Z_m/e -> +infinity,

since the actual query influence is Inf_j(F_m)=2s-s^2. The strict positivity uses 0<ln2<1. These are limits of FIVE explicit rational-log expressions, not a limit interchanged with a growing atom sum. Rational Taylor expansions at s=0 justify the O terms; every residual logarithm has the displayed polynomial comparison, so no hidden nonuniform remainder is assumed.

The constant 2/ln2-2 equals the earlier A003 sharp point-shadow allowance, but it is a different bill: here it is the limiting canonical reset cost per actual query influence. Its derivation is the grouped likelihood calculation above, not an identification of reset cost with retained shadow or discarded mask KL.

It follows that for every finite A>=0 there is an actual m and a calibrated finite-cost source reference with c_m<=17 I(g_m) for which Z_m>Ae. Thus the statement 'every canonical active reset on a uniformly paid source has signed cost at most A times the edit mass' is FALSE for every finite A. The weaker statement Z<=0 is also false. The unchanged K=44 WHOLE bank still pays these prescribed active histories by A096's conditional theorem; conditional occupancy refund and inherited surplus must be retained. No unbounded Boolean H/I ratio follows.

## Validation and first unpaid step

The frozen six-case checker uses m=4,5,6,8,16,32. Literal roots and both actual child references are rebuilt at m=4 and6 (dimensions9 and13); the other entries use the proved grouped formulas and exact rational-log arithmetic only. These checks validate finite formulas and source certificates, not the limit by extrapolation. The limit argument above supplies the all-dimensional separation. The prior AND2 tensor construction in DERIVATION section5 preserves an actual positive earlier debit and both whole tensor terminals for this family too.

The useful next question is the NET signed cost Z-rho from the SAME reference, rather than another bound on positive Z in isolation. A universal useful-reset theorem must bound that net cost against one unused original reserve, including old erasures and complete terminal CE. This family shows why the edit mass alone cannot be substituted for the real query/occupancy account, even when the source price is a fixed absolute constant.
