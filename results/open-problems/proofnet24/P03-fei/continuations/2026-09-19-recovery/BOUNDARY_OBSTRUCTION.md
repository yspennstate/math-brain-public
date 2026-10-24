# A certified boundary-decomposition obstruction

19 September 2026. Addendum to [CONTINUATION.md](CONTINUATION.md), Sections 1.2--1.3.

**Status: proved by the identities below and checked with rational logarithm enclosures; independent audit pending. This does not refute FEI. No publication-novelty claim is made for this elementary NAND example.**

The collision-free theorem in the continuation establishes H(f)<=4 I_x(f) for every boundary-separated signed-subcube-parity representation, regardless of repeated parity labels. Such a representation cannot exist for every Boolean function: the following explicit 27-variable example satisfies H(f)>4I(f).

## 1. Explicit function

On {0,1}, put A_0(x)=x. Recursively, on three disjoint blocks, put

    A_(j+1)(x^(1),x^(2),x^(3))
        =1-A_j(x^(1)) A_j(x^(2)) A_j(x^(3)).

Thus A_j is an indicator on 3^j variables. Take

    f=1-2A_3.

This is the depth-three ternary NAND tree, with 27 distinct input variables.

## 2. Exact compressed calculation

For any indicator A, use the normalized Walsh transform and define

    alpha=E A,
    E_A=sum_S Ahat(S)^2 log_2(1/Ahat(S)^2),
    D_A=sum_S |S| Ahat(S)^2,
    t(u)=u log_2(1/u), t(0)=0.

For B=1-A(x^(1))A(x^(2))A(x^(3)) on disjoint blocks, independence and the product Fourier formula give

    beta=alpha^3,
    E B=1-beta,
    D_B=3 alpha^2 D_A,
    E_B=3 alpha^2 E_A-t(beta^2)+t((1-beta)^2).

Indeed taking the product multiplies the squared-coefficient masses, and complementation changes only the constant Fourier coefficient. For g=1-2A, the same calculation gives

    I(g)=4D_A,
    H(g)=t((1-2alpha)^2)+4[E_A-t(alpha^2)]-8alpha(1-alpha).

Start with alpha=1/2, E_A=1, D_A=1/4 and apply the recurrence three times. In particular,

    E A_3=129390919/134217728,
    I(f)=37786203/67108864.

The certified intervals in `boundary_checks.json` imply

    2.49241458996011 < H(f) < 2.49241458996013,
    4.42656574277255 < H(f)/I(f) < 4.42656574277256.

The program encloses each logarithm through a positive rational atanh series and performs all interval arithmetic with Fractions. Its displayed decimal endpoints are rounded outwards. It does not enumerate all 2^27 physical inputs, and no exhaustive 27-dimensional FEI claim is being made.

## 3. Consequences for the continuation strategy

If f had any boundary-separated subcube-parity representation of the type in CONTINUATION.md, then

    H(f)<=4I_x(f)<=4I(f),

contradicting the certificate. Thus the universal existence of that exact representation is **false**, not simply an unproved missing lemma. This includes every partition of the existing input variables into selector and data coordinates covered by the theorem; it does not make claims about transformations that change influence or the domain.

More quantitatively, for any such subcube-parity representation without boundary separation, let A_art be the artificial-boundary quantity in equation (4) of CONTINUATION.md. Then

    H(f)<=4I_x(f)+2A_art<=4I(f)+2A_art,

so

    A_art/I(f)>0.21328287138627.

The important remaining possibilities are a paid nonzero boundary debt, more general cells with a different local cost, or a global signed-cancellation method. Do not ask the scheduled workers to prove zero boundary debt for arbitrary Boolean functions; this example rules it out.

The prior literature already supplies FEI ratios above four (and much stronger lower bounds). This explicit small formula is included to give this repository a self-contained, reproducible obstruction tied directly to the newly sharpened constant-four patching theorem. It must not be marketed as a new best lower bound for the FEI constant.

## 4. Reproduction

Run `python3 check_boundary_obstruction.py > boundary_checks.json` beside `check_recovery.py`. The latter supplies the cached rational logarithm enclosure. No third-party package, network access, proof assistant, or paid compute is needed.
