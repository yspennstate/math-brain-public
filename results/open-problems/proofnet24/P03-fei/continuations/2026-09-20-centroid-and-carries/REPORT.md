# Polynomial-support pairing, the centroid bound, and Walsh carries

20 September 2026. Research continuation for Yitzchak Shmalo.

**Full Friedgut–Kalai FEI is not proved here.** This note proves the centroid candidate explicitly left unproved in the current affine-symmetric worklog, strengthens it to ordered-distance pairing with arbitrary nonnegative coordinate costs, and applies it to a restricted class of Boolean spectra. It also proves that a proposed linear growth bound for higher Walsh amplitude digits is false. These are mathematical additions to this project, not a claim of publication priority or resolution of unrestricted FEI. The proofs below are independent of the finite searches.

## 1. A weighted support-pairing theorem

Let P be a nonzero multilinear polynomial over F_2 in n binary variables, and A={x:P(x)=1}, of size M. Choose nonnegative real coordinate costs c_1,...,c_n and define

    |x|_c = sum_i c_i x_i,
    T_c = sum_i c_i,
    D_c(P) = max_{S: coefficient of x_S in P is 1} sum_{i in S} c_i.

The constant monomial has cost zero. For any center b in F_2^n, sort the M distances |x+b|_c, x in A, as a_1 <= ... <= a_M. Then

\[
\boxed{a_j+a_{M+1-j}\ge T_c-D_c(P)\quad(1\le j\le M).}
\tag{1}
\]

In particular,

\[
\boxed{\frac1M\sum_{x\in A}|x+b|_c\ge\frac{T_c-D_c(P)}2.}
\tag{2}
\]

With all c_i=1 and ordinary algebraic degree d, this gives the conjectured centroid bound

\[
\boxed{\frac1{|A|}\sum_{x\in A}|x|\ge\frac{n-d}{2}.}
\tag{3}
\]

It holds about every center, not only zero. It is sharp: P=prod_{i=1}^d(1+x_i) has A a coordinate subcube with mean weight (n-d)/2. In the weighted statement the analogous coordinate subcube attains equality in (2).

### 1.1 Orthogonality of evaluation spaces

It suffices to prove (1) at b=0. Translation P(x+b) does not increase weighted degree because every resulting monomial is a subset of an original monomial, and c_i>=0. Its support is A+b. Applying the zero-center result with its actual degree gives at least the asserted lower bound.

For a real threshold u>=0, let E_u be the F_2 vector space of evaluations on A of polynomials whose monomials have cost at most u. Set h_u=dim E_u. If u+v<T_c-D_c(P), then

\[
E_u\perp E_v\quad\text{in }\mathbb F_2^A,
\qquad h_u+h_v\le M.
\tag{4}
\]

Indeed, for polynomials R,S in the respective spaces, their evaluation inner product is

    sum_{x in A} R(x)S(x) = sum_{x in F_2^n} P(x)R(x)S(x)   in F_2.

After multilinear reduction, the product has weighted degree strictly less than T_c. Its full monomial x_1...x_n is therefore absent. The sum over the binary cube of any proper multilinear monomial is zero in F_2, whereas the full monomial sums to one. Thus the displayed inner product vanishes. The standard dot product on F_2^A is nondegenerate, giving the dimension inequality. This works even when some c_i are zero; the strict weighted-degree inequality still excludes the full monomial.

### 1.2 Evaluation rank dominates the low-distance count

Write N_u=|{x in A: |x|_c<=u}|. Then

\[
h_u\ge N_u.
\tag{5}
\]

To see this, for each such x use the monomial with variable set supp(x). Its cost is at most u. Restrict their evaluation matrix to these same N_u points. The entry in row y and column x is one exactly when supp(x) is contained in supp(y). Ordering the points by cardinality makes this matrix triangular with diagonal one. Hence the evaluation vectors are independent. This proof does not assume that A is downward closed.

### 1.3 Pairing and the centroid

If (1) failed for index j, take u=a_j and v=a_{M+1-j}. Then u+v<T_c-D_c(P), but (5) gives h_u>=j and h_v>=M+1-j, contradicting (4). This proves (1). Sum (1) over j to obtain (2), and specialize the costs for (3).

This is an all-dimensional proof. It does not infer a theorem from the previous 71,368,704 finite parameter checks or the additional local search preserved here.

### 1.4 A marginal formulation

For X uniform on A, let beta_i=|E(-1)^{X_i}|. Minimize (2) over b, choosing each b_i separately. Since min_b E|X+b|_c=(1/2)sum_i c_i(1-beta_i),

\[
\boxed{\sum_i c_i\beta_i\le D_c(P).}
\tag{6}
\]

This holds for every nonnegative cost vector. It is stronger than merely bounding the sum of the biases by d. No statement is made here that the squared Fourier masses of a general Boolean function are uniform on one polynomial support.

## 2. The bottom Walsh digit: inherited observation and new consequences

For Boolean f:F_2^n->{-1,1}, use normalized Walsh coefficients a_S=fhat(S) and integers W(S)=2^n a_S. Suppose f is not a character. Let r be the minimum 2-adic valuation of a nonzero W(S). Then 1<=r<n. Put k=n-r and

    Q(S)=(W(S)/2^r) mod 2.

The current affine-symmetric worklog already proves that Q is a nonzero binary polynomial of degree at most r-1. We retain and credit that observation. Here is its proof for completeness.

As an integer multilinear polynomial in the frequency bits S,

    W(S)=sum_x f(x) prod_{i:x_i=1}(1-2S_i).

The coefficient at monomial U is (-2)^|U| sum_{x:x_U=1} f(x). When |U|<n the latter sum is even. All integer polynomial coefficients are divisible by 2^r, because they are integer linear combinations of the values W(S). After division by 2^r, coefficients of degree at least r vanish modulo two: proper monomials have an extra factor of two, and the full monomial has factor 2^n with n>r. Therefore deg Q<=r-1. If r=n, Parseval would allow only a single nonzero coefficient, the character case excluded above.

Applying (1) and (3) to the odd layer A_0={S:Q(S)=1} yields

\[
\frac1{|A_0|}\sum_{S\in A_0}|S+b|\ge\frac{k+1}{2},
\tag{7}
\]

and the stronger reversed-distance pairing with threshold k+1, for every b. The elementary minimum-weight bound gives |A_0|>=2^(k+1). It can be proved by induction: for a nonzero degree-d polynomial P=A+x_i B with B nonzero, its support has density at least half that of B, hence at least 2^-d.

The resulting first-layer influence lower bound

    I(f)>=2^-2k * |A_0| * (k+1)/2 >= (k+1)2^-k

was already available by physical edge isoperimetry, as the earlier worklog explains. It is not counted here as a new general FEI bound. The new result is the actual centroid/pairing theorem, including (6), rather than this already-known numerical consequence.

## 3. A complete constant-four theorem for uniform nonzero spectra

Call a Boolean function plateaued here when all its nonzero Fourier coefficients have equal absolute value; the Fourier support need not be affine. If such a function is not a character, its common absolute coefficient is 2^-k for an integer k>=1, and its support size is 2^(2k). Indeed, if |W(S)|=m at every nonzero coefficient, Parseval gives L m^2=2^(2n), so m and L are powers of two.

For this function the odd layer in Section 2 is exactly the full Fourier support. Since the squared spectrum is uniform on it,

\[
H(f)=2k,\qquad J(f)\ge\frac{k+1}{2},
\]

where J=sum_i min(Inf_i,1-Inf_i). Thus

\[
\boxed{H(f)\le\frac{4k}{k+1}J(f)<4J(f)\le4I(f).}
\tag{8}
\]

There is also the stronger affine-minimum conclusion

\[
\boxed{H(f)\le\frac{4k}{k+1}\mathfrak I(f),}
\tag{9}
\]

where Ifrak is the minimum of total influence over invertible affine input changes and multiplication by output characters. Such operations preserve entropy and the plateaued property. Apply (8) after every such change and take the minimum. This does not assert that physical influence itself is invariant under input changes.

The class constant four is optimal in the limit. For the addressing function with k address bits and 2^k independent data bits, f(y,z)=z_y, expanding each address indicator gives exactly 2^(2k) Fourier coefficients of magnitude 2^-k. Its entropy is 2k. Each address bit has influence 1/2, and the data-bit influences sum to one, so

    I(f)=k/2+1,       H(f)/I(f)=4k/(k+2) -> 4.

The addressing example and its Fourier calculation are standard; no novelty is claimed for that example, or for the independent publication priority of the plateaued theorem. The precise constant 4k/(k+1) in (8) is not asserted sharp at fixed k. The genuinely new-to-this-project proof uses the centroid statement that its current worklog had left unproved.

### A bounded-odd-amplitude extension

Suppose every nonzero Fourier coefficient is 2^-k times an odd integer of magnitude at most R. The same support polynomial applies. The support has at least 4^k/R^2 points, and each point has squared mass at least 4^-k. Hence J>=(k+1)/(2R^2), while H<=2k. The same affine argument proves

\[
H(f)\le\frac{4R^2k}{k+1}\mathfrak I(f).
\tag{10}
\]

This is parameterized by R and assumes a single valuation across all nonzero coefficients. It is not a theorem for arbitrary amplitudes or arbitrary numbers of valuation layers.

## 4. Why the simplest higher-digit continuation fails

The first Walsh digit is low degree. A tempting extension is that successive normalized amplitude digits have degree growing only linearly in their index. That extension is false even for symmetric, genuine Boolean functions.

For odd n>=5, let

    f_n(x)=1-2*1_{|x|=1}.

Its exact integer Walsh transform is

\[
W(S)=2^n\mathbf1_{S=0}-2(n-2|S|).
\tag{11}
\]

Every W(S)/2 is odd, so r=1 and the bottom digit Q is the constant one. Let B_ell(S) be binary digit ell of the signed integer W(S)/2, with ell>=1; equivalently take residues modulo 2^(ell+1) before selecting the digit. If ell<=n-2 and m=2^(ell-1)<=n, then

\[
\boxed{\deg_{\mathbb F_2} B_\ell=2^{\ell-1}.}
\tag{12}
\]

### Proof

The exceptional term 2^(n-1) at S=0 does not affect digit ell<=n-2. Put c=(n+1)/2. The remaining integer is

    2|S|-n = 1+2(|S|-c).

Thus B_ell is digit ell-1 of |S|-c. For any integer t and m=2^(ell-1), this digit equals binom(t,m) modulo two. For nonnegative t this follows by expanding (1+z)^t over F_2 as the product of (1+z^(2^j)) for its binary digits. It extends to arbitrary integers because both sides depend only on t modulo 2^ell; this periodicity of the coefficient of z^m also follows from (1+z)^(2^ell)=1+z^(2^ell).

Vandermonde's identity for generalized integer binomial coefficients gives

\[
B_\ell(S)=\sum_{j=0}^{m}
\left[\binom{-c}{m-j}\bmod2\right]e_j(S),
\tag{13}
\]

where e_j is the elementary symmetric binary polynomial and e_j(S)=binom(|S|,j) modulo two. The coefficient of e_m is one and all other terms have degree less than m. Since m<=n, the polynomial has degree exactly m. This proves (12).

For example, n=17 gives digit degrees 1,2,4,8,16. Consequently no bound of the form A*r+B*ell+C, with fixed finite constants, controls all such digit degrees. This disproves the linear-degree carry shortcut, not FEI or every possible multiscale argument. The source function is fully symmetric and belongs to an already certified FEI class. The exploratory square-digit output is preserved but is not promoted to an additional general theorem.

## 5. What remains missing for full FEI

The centroid theorem controls a uniform distribution on a polynomial support. A general squared Boolean Fourier spectrum is not that distribution: it has unequal amplitudes and potentially multiple 2-adic layers. Equation (7) does not license replacing its unweighted average by an arbitrary mass-weighted average. Section 4 shows that paying each higher digit by a linearly increasing degree is not a valid way around that difference.

The retained full-scope target is still a dimension-independent finite K with

    sum_i H(S_i | S_-i) <= K I(f)

for every Boolean f. The existing erasure reduction then implies FEI with K+2/ln 2. No such universal estimate is assumed or proved here. In particular, the class constant four in (8) cannot be substituted for a general constant; the literature already supplies Boolean examples whose H/I exceeds 6.45.

The preceding exact-Booleanity package is also recovered in this delivery. Its real-valued counterexamples show why replacing the full Boolean identities by finitely many low-order ones plus closeness is invalid. The positive theorem here retains genuine Booleanity. Neither the centroid theorem nor the earlier restricted rigidity classification controls the remaining general amplitude weights.

## 6. Executed checks and preserved failed approaches

Run `python verify_centroid.py` with Python 3.10+ and NumPy. Every mathematical assertion in this checker uses integer arithmetic; no floating-point comparison certifies a sign.

Actual checks:

- All 65,812 binary functions in dimensions one through four, interpreted as polynomial truth tables, and all centers for each nonzero support.
- Every degree-at-most-two polynomial on five variables (65,536 coefficient vectors), with all centers. Zero supports are excluded from mean statements.
- 600 additional seeded polynomial cases in dimensions five through ten, with eight centers each. Across these overlapping families there are 3,152,586 center profiles and 42,622,160 ordered pair assertions. Ordered pairs count both directions; these counts are not counts of distinct Boolean FEI instances.
- 144 evaluation-rank checks and 84 orthogonal-dimension checks on 24 selected polynomial supports.
- All 65,812 Boolean sign functions through dimension four for the bottom Walsh digit and all-center support bounds; 2,136 noncharacter plateaued functions satisfy the asserted exact folded bound.
- 240 further polynomial cases with 720 nonnegative integer cost vectors, including zero costs: 2,880 weighted center profiles and 163,272 weighted ordered-pair checks.
- 23 exact digit-polynomial identities for genuine Boolean functions in dimensions 5,7,9,11,13,17, plus exact addressing calibrations in dimensions 3,6,11. The n=17 computation is one actual 131,072-entry truth table, not exhaustive Boolean coverage at that dimension.

The final checker was copied into a separate directory and rerun. Its verification output was byte-identical. This is reproducibility, not independent review or Lean verification. An initial empty-batch programming error in the n=1 noncharacter family was fixed before the successful output; it was not a mathematical counterexample.

The `exploratory/` directory preserves the earlier centroid and Walsh-carry probes and their actual outputs. Their random local searches are not all-dimensional proofs. The centroid probe found no violation; the rank proof above resolves the candidate independently. The carry probe led to (12), whose proof is now supplied rather than inferred from a few degrees.

## 7. Sources and provenance

Consumed current repository source: `proofnet24/P03-fei/continuations/2026-09-20-affine-symmetric-stopping/WORKLOG.md`, blob `3e98b23319d234477d890e6ffdead574bfc251d2`, read in full. Section 2 supplies the bottom-digit observation; Section 3 explicitly labels the centroid candidate (C) unproved. This note proves (C) and the stronger weighted pairing. Its first-layer influence corollary was already noted as obtainable by isoperimetry and is not reclassified as a new universal advance.

Current FEI entrypoint read: `proofnet24/P03-fei/README.md`, blob `d226f1c4a460a0f90ba25f40a8a6b6a8d03ab2e9`. Its existing affine-symmetric stopping result and endpoint quantifier obstruction are retained; they are not needed as uninspected premises in Sections 1--4.

The actual conversation file `FEI_Exact_Booleanity_2026-09-20.md` was read in full, and the original ZIP was extracted. Its full report, checker, saved output, exploratory scripts/output, manifest and handoff are being restored under their original paths. The recovered checker was rerun and reproduced its old output byte-for-byte. The original pending-delivery wording is historical; the separate delivery record gives the current status.

Primary-source context checked on 20 September 2026: Gonzalez--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026, https://arxiv.org/abs/2606.00246 ; Rani Hod, *Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions*, arXiv:1711.00762, https://arxiv.org/abs/1711.00762 . The first still treats general FEI as a conjecture and proves restricted stopping-tree classes. The second gives the lower bound exceeding 6.454784. These are context and scope checks, not premises in the elementary rank proof.

Bounded searches did not establish publication priority for the centroid/pairing theorem, its plateaued consequence or the exact digit-degree statement. Reed--Muller evaluation orthogonality, triangular monomial evaluation, Walsh transforms, Vandermonde's identity and binary binomial-coefficient identities are standard ingredients and are not claimed as new. No schedules, ownership, permissions, repository visibility or unrelated research files are changed.
