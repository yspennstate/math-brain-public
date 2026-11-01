# Exact erasure/split endpoint table

Default physical encoding is x_i=(-1)^bit_i, so plus slices are bit 0. All rational spectral weights and log-linear information quantities below are exact. Delta_i denotes the physical entropy decrement, not the spectral deficit delta=I-Var. L_i in this table is L_down; B05's L_mismatch is B_i. Empty atoms are included throughout.

| Function | Spectrum | H | I_i on support | B_i | L_down,i | JS_i | Delta_i | DTC | D_char |
|---|---|---|---|---|---|---|---|---|---|
| Constant +/-1 | empty atom 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dictator +/-x_j | singleton atom 1 | 0 | 1 at j | 0 | 0 | 0 | 0 | 0 | 0 |
| Character chi_A, k=|A|>=1 | atom A of mass 1 | 0 | 1 on A | 0 | 0 | 0 | 0 | 0 | 0 |
| Bent, n even | all 2^n atoms 2^-n | n | 1/2 | 1 | 1/2 | 1 | 2 | 0 | n/2 |
| Maj3 | singles and triple each 1/4 | 2 | 1/2 | 0 | 0 | 0 | 0 | 2 | 3/2 |
| Point defect / AND_n / OR_n | empty (1-2p)^2; each nonempty 4p^2, p=2^-n | H_n below | 2p | b_n below | ell_n below | H_n-H_(n-1)/2-b_n | H_n-H_(n-1)/2 | H_n-n b_n | 2np for n>=2; 0 for n=1 |

Take H_0=0 and

    E0=(1-2p)^2 log2(1/(1-2p)^2),
    H_n=E0+8p(1-p)(n-1),
    m0=(1-2p)^2+4p^2,
    b_n=Phi((1-2p)^2,4p^2)+4p(1-2p),
    ell_n=4p^2 log2(m0/(4p^2))+2p(1-2p).

Phi(a,b)=(a+b)h2(b/(a+b)). Weighted zero terms are zero, including the n=1 point-defect endpoint where H=B=L=Delta=JS=0. AND and OR differ from a point defect only by input/output sign reversals, which preserve the squared law. Every coordinate is equivalent in these symmetric endpoint spectra.

Additional rational quantities: constant has Var=I-Var=0; dictator has Var=1 and deficit 0; a k-character has Var=1 and deficit k-1; flat bent has Var=1-2^-n, I=n/2 and deficit n/2-1+2^-n; Maj3 has Var=1, I=3/2 and deficit 1/2; the point defect has Var=4p(1-p), I=2np and deficit 2p[n-2+2p]. The information units of DTC differ from the influence units of D_char.

## Exact regressions

AND2 is bent: H=2, I=1, Var=3/4, B_i=1, L_down,i=1/2, C_up,i=1/2, JS_i=1 and Delta_i=2. Thus neither L_down=B nor Delta=B is a valid alias. The equality B_i=h2(I_i) holds, and every spectral bit is independent of the others. Conditioning away the empty atom changes this: DTC_full=0, DTC_nonempty=log2(3)-4/3>0, root correction T0=1. Positivity is certified by 27>16. The exact formula is DTC_full=h2(3/4)+(3/4)DTC_nonempty-1=0.

For the three-bit point defect the following exact prime-log quantities hold at every coordinate:

    H=4-(9/8)log2(3), I=3/4, Var=7/16,
    B_i=1+(5/8)log2(5)-(9/8)log2(3),
    L_down,i=1/4+(1/16)log2(5),
    C_up,i=3/4+(9/16)log2(5)-(9/8)log2(3),
    Delta_i=3-(9/8)log2(3),
    JS_i=2-(5/8)log2(5),
    DTC=1+(9/4)log2(3)-(15/8)log2(5).

Multiplication by x_i swaps L_down,i and C_up,i while preserving B_i, Delta_i, JS_i, DTC and H. They differ: the equality would require 5^4*2^4=3^9 (the sides are 10000 and 19683). This is an exact character-orientation witness, not a floating comparison.

This same point defect rechecks the known bit-unit regression JS_i>2 I_i, while JS_i<=(2/ln2)I_i remains valid. The strict first sign is equivalent to log2 5<12/5, certified by 5^5=3125<4096=2^12. The false coefficient 2 in bits must not be confused with the valid coefficient 2 in natural units. The source already has this counterexample; this is a normalization regression, not a new obstruction claim.

Maj3 has B=0 with H=2. Its physical children are AND2/OR2 in two bits and each has H=2, so Delta_i=JS_i=0. It is a concrete reason to retain full terminal entropy at a B=0 stopping node. A parity/character has B=0 as well but H=0, so that simpler endpoint alone would miss the issue.

For bent n>=2, every conditional-bit marginal is fair and B_i=h2(1/2)=1; the normalized child spectra have disjoint support and entropy n-2, yielding Delta_i=2 and JS_i=1. These facts hold for every Boolean flat spectrum, not only the chosen quadratic representative.

## Checked inequalities and the universal gap

The finite checker verifies f=psi+x_i phi, psi phi=0, psi^2+phi^2=1, exact Fourier coefficient placement, I_i=||phi||^2, B_i=L_down,i+C_up,i=L_mismatch,i, Delta_i=B_i+JS_i, nonnegativity of TC/DTC/JS, B_i<=h2(I_i), C_up,i<=I_i/ln2, JS_i<=(2/ln2)min(I_i,1-I_i), and the child influence telescope. It checks full-law character invariance and the exact L orientation swap, plus B=vB(R)+T0 and DTC=h2(v)+vDTC(R)-T0.

The marginal inequality is an all-law chain-rule fact; its equality endpoint for Boolean spectra is already source-classified. It does not pay aggregate B by I: on the point-defect family sum h2(I_i)/I grows like n, whereas B/I tends to 2 and H/I tends to 4. No finite violation of a local candidate or omitted-correction surrogate is a disproof of full FEI.

The exact conditional DTC formula and all-n bounds in REPORT.md imply DTC_full/H_full->1/2 but vDTC_nonempty/H_full->0, and their ratio grows like 2^n. This is a genuine Boolean family demonstrating an unbounded normalization error. The source's correctly stated full-law near-erasure target and the nonempty signed-edge payment remain OPEN.

Execution domain: 278 exhaustive truth tables n=0..3 and 53 labeled endpoints at fixed n<=8. Saved records in out/endpoint_records.jsonl use exact rational coefficients of log2 primes; out/validation.json records the assertion count and measured runtime. No exported display approximation is a certificate. Independent review and remote save remain pending.
