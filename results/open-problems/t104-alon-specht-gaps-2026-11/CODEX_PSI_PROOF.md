# Results for the Psi inequality

Task: “prove one explicit inequality, or to find a counterexample, or failing both to prove the strongest rigorous partial result you can.” Work begun 2026-11-11 at 08:00 +04.

## 1. Statements proved

**PROVED.** For the expression in the question, Psi(x)>=0 holds:

1. for every feasible vector when 5<=n<=8;
2. for every n>=5 when at most eight coordinates are nonzero;
3. for every n>=5 when x has at most three distinct coordinate values;
4. for every n>=5 when m>=1/(n(n-1)).

The proof for n=5 is complete and has been checked by two independent exact expansions, one using only Python integers. Equality for n=5 occurs only at the star and edge, up to sign and permutation. No assertion of uniqueness of equality is made here for the other dimensions.

**PROVED.** The proposed stronger statement Phi'>=0 on the whole feasible set is false: an explicit exact example occurs at n=14. This is not a counterexample to Psi>=0.

**NUMERICAL.** Independent local minimization for n=5,...,9 found no negative Psi beyond floating-point rounding. The final scaled run converged from all 465 starts, with recomputed minima between -4.5e-16 and 1.2e-15; each dimension's best vector was also evaluated at 65 decimal digits. This evidence is not used in any proof.

Every argument below labelled PROVED is either a mathematical derivation or an exact polynomial coefficient check with the complete script supplied. There are no unlabelled numerical steps in the proofs.

## 2. Algebra and the weighted bound — PROVED

Write p=p3 and

    K=n^2-6n+6+2nq,
    D=q-1/n-p^2.

Expansion gives exactly

    Psi=K((n-1)m-1/n)+2(n-3)D.                 (2.1)

Since q>=1/n, K>=(n-2)(n-4)>0. Also

    p=<x,x^2-(1/n)1>,
    ||x^2-(1/n)1||^2=q-1/n,

so Cauchy–Schwarz gives D>=0. Equality D=0 means x_i^2-1/n=p*x_i for every i, hence x has exactly two values. Conversely any two-value feasible vector has D=0. Formula (2.1) proves assertion 4.

After changing sign and permuting, take S=x_1=max_i |x_i|>0 and put c_i=S-x_i>=0. Then

    sum c_i=nS,           sum c_i^2=nS^2+1,
    sum c_i*x_i=-1,       sum c_i^2*x_i^2=S^2-2Sp+q.

Consequently

    2 sum_{i<j} c_i*c_j = n(n-1)S^2-1 = A,
    2 sum_{i<j} c_i*c_j*x_i*x_j = 1-q+2Sp-S^2.

Here A>=n-2>0, since S^2>=1/n. Every product in this weighted average is at most m, so

    m >= M=(1-q+2Sp-S^2)/A.                  (2.2)

The exact equality condition is that every pair with c_i*c_j>0 has product m. Merely requiring those products to be equal to one another is insufficient: at (3,3,-2,-2,-2)/sqrt(30), they all equal 2/15, but m=3/10 and M=2/15.

For completeness, with S chosen as above, equality in (2.2) occurs at the star, the edge, and, for even n, the vector with n/2 entries S and n/2 entries -S. To see this, there are at least three coordinates below S: otherwise at least n-2 coordinates equal S, inconsistent with sum zero and all moduli at most S when n>=5. If all their pair products equal a positive number, those coordinates all equal the same negative t. If k coordinates equal S, zero sum gives t=-kS/(n-k). When k=1 this is the star; when k>=2 the maximum also includes S^2, forcing |t|=S and k=n/2. If their common product is zero, at most one is nonzero; zero sum and the modulus bound force the edge. A negative common product among three coordinates is impossible.

Substitute M in (2.1). Because the coefficient of m is positive, we obtain

    n*A*Psi >= Phi,
    Phi=K*N+2n(n-3)A*D,
    N=n(n-1)(1-q+2Sp-2S^2)+1.               (2.3)

This Phi is the question's Phi'. All these identities, including both equality vectors for symbolic n, are checked in audit_algebra.py.

The star has

    q=(n^2-3n+3)/(n(n-1)),
    p^2=(n-2)^2/(n(n-1)), m=1/(n(n-1));

the edge has q=1/2, p=0, m=0. Substitution in the original Psi gives zero in both cases. Substitution in (2.2) gives M=m in both cases as well.

## 3. The exact polynomial used for certification — PROVED

Let y be a nonzero, zero-sum, unnormalized vector, with a=y_1=max |y_i|. Define

    T=sum y_i^2, P=sum y_i^3, Q=sum y_i^4,
    Kh=(n^2-6n+6)T^2+2nQ.

The following degree-eight polynomial has integer coefficients:

    H_n(y) = Kh * [n(n-1)(T^2-Q+2aP-2a^2T)+T^2]
             + 2(n-3)(n(n-1)a^2-T)(nQT-T^3-nP^2).       (3.1)

For x=y/sqrt(T), direct substitution gives

    H_n(y)=T^4*Phi(x).                                  (3.2)

Thus H_n>=0 on the ordered cone implies Psi>=0 by (2.3). The symbolic normalization check in audit_algebra.py verifies (3.2) independently of the coefficient computations.

## 4. Covering the ordered cone — PROVED

Consider y_1>=...>=y_n, sum y_i=0, y_1+y_n>=0. For 1<=j<n put

    r_j=(n-j repeated j times, -j repeated n-j times).

If d_j=y_j-y_{j+1}>=0, then

    y=sum_j (d_j/n)*r_j,
    y_1+y_n=sum_j (n-2j)*d_j/n.             (4.1)

The following rays generate the cone:

* r_i with n-2i>=0;
* (2j-n)r_i+(n-2i)r_j with i<n/2<j.

Here is an explicit coverage argument. Write alpha_j=d_j/n. Positive indices i<n/2 supply (n-2i)alpha_i, and negative indices j>n/2 require (2j-n)alpha_j. Their total supply is at least total demand by (4.1). Allocate the demand among the supplies, with nonnegative allocations b_ij and no supply exceeded. Such an allocation exists by successively filling demands from the remaining supplies. Each b_ij gives the nonnegative multiple

    b_ij / ((n-2i)(2j-n))

of the second kind of ray. Its components account for b_ij/(n-2i) of alpha_i and b_ij/(2j-n) of alpha_j. Remaining positive alpha_i multiply r_i. Any index n/2, when integral, already multiplies the first kind of ray. This reconstructs y and proves coverage.

Every vector in the problem can be put in this cone by choosing the sign of a coordinate of largest modulus and then sorting.

## 5. Complete certificate for n=5 — PROVED

The six rays from section 4, in the order used in both verifiers, are

    v0=(4,-1,-1,-1,-1),
    v1=(3,3,-2,-2,-2),
    v2=(10,5,5,-10,-10),
    v3=(15,0,0,0,-15),
    v4=(5,5,0,-5,-5),
    v5=(10,10,-5,-5,-10).

Substitute y=sum_{j=0}^5 z_j*v_j in (3.1). The script cone_certificate.py expands it over the integers and stores every nonzero coefficient in cone_coefficients.json. The independent script verify_n5.py reconstructs the entire polynomial using its own dictionary addition and multiplication, using only Python integer arithmetic. It checks equality to the stored polynomial and checks positivity of every coefficient.

Exact results:

    Degree: 8.
    Positive coefficients: 1277.
    Absent degree-eight monomials: 10.
    Least positive coefficient: 22500000.

Since all z_j>=0, H_5(y)>=0. Sections 2–4 now prove Psi>=0 for every feasible x at n=5. This is a full computer-assisted proof, not a grid or floating-point check: the scripts compute finite exact polynomial identities and sign checks. A reader can reproduce the standalone integer check with

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 verify_n5.py

The file cone_coefficients.json is checked rather than trusted: the verifier reconstructs H before reading it. The SHA256 of the canonical coefficient list is

    aee1c72e9e8fea08e1fe95a03cd9a213e0bdd41b88f4bdf95e0c217628a13271.

Equality is also determined exactly. The pure z_j^8 coefficients are

    [0,22500000,167062500000,0,2500000000,428062500000].

Therefore H=0 forces z1=z2=z4=z5=0. The coefficient of z0*z3^7 is 984150000000>0, so z0 and z3 cannot both be positive. A nonzero zero must lie on v0 or v3. These are precisely the star and edge rays. Since Psi=0 implies H=0 by (2.3), and both specified vectors have Psi=0, these are all equality cases at n=5.

## 6. Dimensions 6, 7 and 8 — PROVED

The same cone-generation proof applies unchanged. cone_extensions.py constructs every generating ray from the formulas in section 4, substitutes their nonnegative linear combination into (3.1), expands in the exact domain ZZ, and counts negative coefficients. Its saved outputs give:

| n | Generating rays | Nonzero coefficients | Negative coefficients |
|---|---:|---:|---:|
| 6 | 7 | 2991 | 0 |
| 7 | 12 | 75561 | 0 |
| 8 | 13 | 125947 | 0 |

The outputs are cone_extension_6.out, cone_extension_7.out, and cone_extension_8_retry.out. For each row every nonzero coefficient is a positive integer. Thus (3.2), cone coverage, and (2.3) prove the inequality in that dimension. No floating-point computation is used. The n=8 expansion took about 32 seconds and used about 151 MB of peak resident memory on this Mac. An earlier rejected resource-limit setup is retained in cone_extension_8.out and contributes no result.

## 7. Adding zero coordinates — PROVED

Fix q,p,m from a feasible vector with at least five coordinates; appending zeros preserves these quantities, including m>=0. Set

    rho=2q-1, B=p^2, t=2B-rho,
    C_n=(n-1)(n^2+(rho-5)n+6).

Then

    Psi_n=C_n*m-[(n-4)t+2B].               (7.1)

We have -1<=rho<=1 because 0<=q<=1. For n>=5, C_n>0 and C_{n+1}>C_n: indeed

    C_5=4(1+10q)>0,
    C_{n+1}-C_n=3n^2+(2rho-9)n+6
                  >=3n^2-11n+6>0.

If t<0, (7.1) strictly increases with n, since m>=0. If t>=0, it suffices to see that both 1/C_n and (n-4)/C_n decrease. For the latter comparison put h=n-5>=0; exact expansion gives

    (n-4)C_{n+1}-(n-3)C_n
      =2h^3+(15+rho)h^2+(31+3rho)h+12-10rho>0.

Every displayed coefficient is positive for -1<=rho<=1. Consequently the required lower bound

    [(n-4)t+2B]/C_n

decreases with n. Thus Psi_n>=0 implies Psi_{n+1}>=0 in both cases. The algebraic comparisons are independently checked in audit_algebra.py.

Any vector with at most eight nonzero coordinates in dimension n>=8 can be obtained by padding a feasible eight-coordinate vector with zeros. Dimensions 5 through 8 were already proved. This proves assertion 2, including supports of size less than five by first padding them to dimension five or eight.

## 8. All three-value vectors in every dimension — PROVED

Two-value vectors are already covered: if one sign occurs once, the vector is the star; otherwise the largest-modulus value occurs at least twice and m>=1/n>1/(n(n-1)).

For exactly three distinct values, choose the sign and order so they are a>b>c, a>=|c|, with positive integer multiplicities r,s,t. Necessarily r<n/2: if r>=n/2, zero sum and the modulus bound force r=n/2 and every remaining coordinate to be -a, leaving only two values.

Let d=a-b>=0, e=b-c>=0. Multiplying all coordinates by n, which is harmless for the homogeneous certificate, expresses their three values as

    a0=(s+t)d+t*e,
    b0=-r*d+t*e,
    c0=-r*d-(r+s)e.                        (8.1)

The largest-modulus condition is exactly

    (n-2r)d+(2t-n)e>=0.                   (8.2)

Here are three exhaustive integer parametrizations. R,U,V are nonnegative integers and z,w are nonnegative real numbers.

| Case | Multiplicities | Gaps in (8.1) |
|---|---|---|
| t>=n/2 | r=R+1, s=U+1, t=r+s+V | d=z, e=w |
| r<=t<n/2 | r=R+1, t=r+U, s=U+V+1 | d=z+(V+1)w, e=(2U+V+1)w |
| t<=r<n/2 | t=R+1, r=t+U, s=U+V+1 | d=z+(2U+V+1)w, e=(V+1)w |

For the second and third rows, V+1=s-|r-t|>0. Solving (8.2) gives precisely the indicated nonnegative gap parametrizations. Overlap when r=t causes no problem.

three_value_certificate.py substitutes (8.1) and each row into (3.1), including multiplicities in T,P,Q, and expands exactly over ZZ.

In the first row, all 7837 nonzero coefficients in R,U,V,z,w are positive. Thus H>=0 throughout that row.

In the last two rows, raw coefficients have some negative entries. We use integrality: independently partition each of R,U,V into the cases 0, 1, or >=2. There are 27 cells. For a variable in the last case, replace it by a new nonnegative variable plus 2; for the other cases substitute the exact integer. The script checks all coefficients after these exact substitutions.

For the third row all 27 resulting polynomials have nonnegative coefficients. This is recorded in three_value_top_partition.out.

For the second row, 26 of the 27 polynomials have nonnegative coefficients. The only exception is

    R=0, U=1, V>=2,
    equivalently r=1, t=2, s>=4.           (8.3)

The script checks this exact exception list; see three_value_bottom_asserted.out. The attempted further subdivision does not certify the remaining cell and is not used. The final asserted output for the third row is three_value_top_asserted.out, and the final first-row output is three_value_heavy_final.out. These runs also check zero sum, coordinate ordering through the gap identities, and the largest-modulus condition as exact polynomial identities or nonnegative coefficient tests.

The exception (8.3) is covered directly by (2.1), without asserting H>=0. For x=(a,b repeated s times,c,c), put n=s+3>=7. If b<=0, then every coordinate except a is negative or zero and has modulus at most -c. Hence

    a<= (n-1)(-c),
    1<=a^2+(n-1)c^2<=n(n-1)c^2.

So m>=c^2>=1/(n(n-1)). If b>0, zero sum gives -2c=a+s*b>=a, while a^2>=1/n. Therefore

    m>=c^2>=a^2/4>=1/(4n)>=1/(n(n-1)).

Again (2.1) proves Psi>=0. This completes every row and proves assertion 3. The integer partition is essential to this certificate; replacing these multiplicities by arbitrary small positive real weights is not justified.

## 9. A checked reduction and the failure of the stronger bound

**PROVED (reduction).** For fixed S and n>=5, a minimum of Phi over feasible vectors can be attained with at most two distinct coordinate values strictly between -S and S. Thus it has at most three values in total unless both S and -S occur, in which case it has at most four. This is a statement about Phi, not a reduction of Psi by itself.

Here is the proof. As a function F(q,p)=Phi, the Hessian has entries

    F_qq=-4n^2(n-1), F_qp=4n^2(n-1)S,
    F_pp=-4n(n-3)(n(n-1)S^2-1),

and determinant

    16n^3(n-1)[(n-4)n(n-1)S^2-(n-3)]>0.

The bracket is at least (n-4)(n-1)-(n-3)=n^2-6n+7>0 for n>=5. Thus F is strictly concave in its two moments.

Fix a minimizing vector, keep its endpoint coordinates fixed, and suppose there are at least three distinct interior values. The first two moment constraints on the interior coordinates have independent gradients. With alpha=F_q and beta=F_p, Lagrange multipliers give, for every interior value u,

    h'(u)=4alpha*u^3+3beta*u^2-2lambda*u-mu=0.

If alpha=0 and beta!=0, this quadratic has at most two roots, a contradiction. If alpha=beta=0, take one coordinate at each of three distinct values r<s<t and a tangent proportional to (s-t,t-r,r-s). Its third-moment derivative is nonzero, and strict concavity makes the constrained second derivative negative, again a contradiction.

For alpha!=0 there are exactly three distinct interior roots r<s<t, and

    h'(u)=4alpha(u-r)(u-s)(u-t).

Let their multiplicities be k,l,j, and set A0=s-r>0, B0=t-r=A0+C0, C0=t-s>0. If a root of negative h'' occurs twice, varying those two equal coordinates in opposite directions is a feasible tangent with zero first moment derivatives but negative constrained second variation. Thus when alpha>0 we must have l=1; when alpha<0 we must have k=j=1.

Now take equal variations within each group with group values

    delta_r=(s-t)/k, delta_s=(t-r)/l, delta_t=(r-s)/j.

This preserves sum and squared norm to first order. The contribution from h to the second variation is exactly

    4alpha*A0*B0*C0*(C0/k-B0/l+A0/j).      (9.1)

When alpha>0 and l=1, the bracket is <=C0-B0+A0=0. When alpha<0 and k=j=1, the bracket is B0(1-1/l)>=0. Thus (9.1) is nonpositive in both cases. The third-moment derivative is -3A0B0C0, which is nonzero; the strictly negative Hessian term of F therefore makes the complete second variation negative. This contradicts minimality on the smooth plane/sphere intersection of the interior variables. All these tangents are realized by local feasible curves because the two constraint gradients are independent and the coordinates are strictly inside the interval. This proves the reduction. The curvature and moment identities are also checked in audit_algebra.py.

**PROVED (obstruction).** The reduced three-value family already disproves unrestricted Phi>=0 for large n. Let s be a positive integer and take the unnormalized vector

    y=(s, 1 repeated s times, -s, -s), n=s+3.

Then T=3s^2+s, P=-s^3+s, Q=3s^4+s, a=s. Substitution in (3.1) factors exactly as

    H_n(y)=-2s^2(s-1)(s+1)^4(s+3)
                 *(s^2-11s+6)*(s^2+4s-1).              (9.2)

At s=11, n=14, normalization gives

    x=(11, 1 repeated 11 times, -11, -11)/sqrt(374),
    Phi=-357073920/10106041<0,
    Psi=28579680/54043>0,
    m=11/34.

diagnose_phi.py checks (9.2) symbolically and the displayed values using Python Fractions. No rounding is involved. There are two coordinates of largest negative modulus, so the original inequality is comfortably in the easy region of (2.1). A proof of the original claim may still use Phi conditionally on small m; it cannot establish unrestricted Phi>=0.

The obstruction is not an artifact of a tie for the largest modulus: replace a=s by s+epsilon and each of the s middle coordinates by 1-epsilon/s, leaving both -s coordinates fixed. Zero sum is preserved, the positive maximum becomes unique, and H remains negative for all sufficiently small positive epsilon by continuity and the strict inequality in (9.2).

## 10. What remains open

The full statement for arbitrary n>=9 remains open here. The unproved region can be restricted to vectors with at least nine nonzero coordinates, at least four distinct coordinate values, and m<1/(n(n-1)). No counterexample to the original inequality was found.

**UNCHECKED:** Phi>=0 might still hold on the restricted small-m region. It is not proved here. The reduction in section 9 does not justify this restricted claim: imposing bounds on pair products changes the constraint boundary, and a minimum of unrestricted Phi can lie in the easy region for Psi. No inference transferring the three-value proof to all vectors is made.

The main exact obstacle is therefore a bound on D in the small-m region that respects the active pair constraints, or an exact certificate for Psi on the remaining coordinate patterns. The unsuccessful coefficient expansions and the exact failure of the stronger global bound are retained rather than hidden.

## 11. Reproduction and files

All scripts use one process. BLAS thread variables are set to 1 in numerical scripts. No script trains a model, uses a network, or launches a window. Nice priority changes and one attempted resource limit were denied by the sandbox; the failed commands and their outputs remain in the log. The n=8 dense expansion used about 151 MB and 32 seconds; all completed runs remained well below the stated resource limits.

* reproduce.py: local numerical searches and direct random identity checks; reproduce.out, reproduce_bounded.out, reproduce_scaled.out, minimizations.jsonl, minimizations_bounded.jsonl, minimizations_scaled.jsonl. **NUMERICAL only.** The first run's unsuccessful optimizer exits and overflow trial steps are recorded; valid variable bounds were added for the second run, and a positive objective scaling gave convergence from every start in the third run.
* audit_algebra.py: exact identities, equality vectors, padding comparisons, and reduction identities; audit_algebra.out and audit_algebra_final.out.
* cone_certificate.py: exact n=5 expansion; cone_certificate.out, cone_coefficients.json.
* verify_n5.py: independent integer reconstruction; verify_n5.out.
* cone_extensions.py: exact n=4,6,7,8 experiments. The n=4 check was exploratory; the stated theorem only needs n>=5.
* three_value_certificate.py: exact multiplicity expansions and integer partitions. All failed, intermediate and successful outputs have distinct .out names.
* diagnose_phi.py: the exact auxiliary-bound counterexample; diagnose_phi.out.
* four_value_certificate.py was prepared as a next experiment but was not run: the unrestricted Phi route was abandoned after (9.2). It supports no claimed result.

LOG.md records progress and failed routes. RESULT.md gives the final status.

To rerun the general three-value certificates, use these three invocations (each completed in seconds here):

    python3 three_value_certificate.py heavy-bottom
    python3 three_value_certificate.py bottom-at-least-top --partition
    python3 three_value_certificate.py top-at-least-bottom --partition

The bottom-at-least-top invocation deliberately reports the one unresolved coefficient cell (8.3), with an assertion that this is the exact exception list. The elementary m-bound in section 8 completes that cell. A nonempty raw negative-coefficient list is not a failure of this combined proof.
