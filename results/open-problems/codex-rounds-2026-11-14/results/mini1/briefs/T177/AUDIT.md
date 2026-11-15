# Checks and attempted failures

The main proof is in PROOF.md. The following checks concern the estimates and
their scope, rather than the unsolved survival asymptotic.

1. **Single positive input.** If exactly one of m inputs is positive, the output
   equals k>=1 precisely when that input equals k+1. The coefficient is
   m(1-q_n)^{m-1}. At least two positive integer inputs always give a positive
   output. Thus the collision measure's mass is exactly the binomial probability
   used in (4); there is no omitted event producing zero.

2. **Quadratic constant.** The two positive measures r_n and b_n have masses
   R_n<=m(m-1)q_n^2/2 and B_n<=m(m-1)q_n^2. The error correction has disjoint
   first-coordinate and shifted parts. Its l1 norm divided by two is bounded
   by (|R_n-B_n|+R_n+B_n)/(2m)=max(R_n,B_n)/m. This recovers exactly
   (m-1)q_n^2; bounding the two masses separately would give a worse constant.

3. **Boundary and factor two.** The coefficient variation contributes twice
   each interior |q_{n+j}-q_n| and once the last one. The boundary norm is at
   most m^{-L}(q_{n+L}+q_n). Combining these before dividing by 2q_n produces
   m^{-L}max(q_{n+L},q_n)/q_n. This independently checks the finite-window
   remainder and the convention for total variation.

4. **First correction by a second route.** The finite-window proof obtains
   h_beta from the coefficients in the future expansion. Linearizing instead
   the forward equation gives

   \[
   h(k)-mh(k+1)=\beta g(k),\qquad \sum_kh(k)=0.
   \]

   The proposed h_beta satisfies this recurrence directly. Its normalization
   fixes the homogeneous solution C m^{-k}. Alternatively its generating
   function is

   \[
   H(s)=\frac{\beta m s(1-s)}{(m-s)^2},\qquad |s|<m,
   \]

   whose Taylor coefficient is precisely
   beta m^{-k}[m-(m-1)k]. Geometric sums give total mass zero. Its only strictly
   positive entry is h_beta(1)=beta/m (the entry at k=2 is zero when m=2).
   Thus ||h_beta||_1/2=beta/m. The audit script also checks the recurrence
   exactly for m=2,...,12, three rational beta values and k=1,...,99.

   A further scalar check comes directly from (7): the conditional mass at
   1 is 1-q_{n+1}/(m q_n)+s_n/(m q_n). Under (11) this is
   (m-1)/m+beta/(mn)+o(1/n), since |s_n|<=m(m-1)q_n^2. The event {1}
   therefore gives a matching lower bound beta/(mn)+o(1/n) on TV,
   independently of summing the correction sequence.

5. **Interchanging limits.** The proof of Theorem 3 does not interchange a
   coordinatewise asymptotic and an infinite sum without a bound. Equation
   (14) supplies the summable majorant C m^{-(k-1)}(k-1+k/m). The collision
   correction has norm at most 2m q_n^2, so its normalized first-order error
   tends to zero precisely using n q_n->0. This is why that hypothesis was
   retained.

6. **Hypotheses that cannot be dropped in this argument.** An asymptotic
   q_n~A n^{-2} does not imply q_{n+1}/q_n=1-2/n+o(1/n). For example, the
   positive scalar sequence A n^{-2}(1+(-1)^n n^{-1/2}), for n>=2, has the
   former property but its adjacent ratio has an oscillatory error of order
   n^{-1/2}. This sequence is not claimed to arise from the model. It shows
   the logical distinction. Likewise, q_n=n^{-2+o(1)} alone is insufficient
   even to infer ratio convergence: multiplying n^{-2} by alternating factors
   1 and 2 gives a counterexample at the scalar-sequence level.

7. **Degenerate and zero cases.** The finite-window theorem excludes q_n=0
   because the conditional law is undefined; the zero law is nevertheless
   checked in the unnormalized identities. q_n=1 is allowed. In particular,
   m=2, X_n=1 is tested exactly and has TV distance 1/2 from g. Theorems 2
   and 3 do not apply to it because q_n does not tend to zero. The proof
   classifies this as the only critical law with no atom at zero.

8. **No moment inference from TV.** Total-variation convergence alone does
   not establish convergence of conditional means. No such inference is
   used. The sharp critical mean and survival constants remain unproved here.

9. **Exact computational checks.** The script uses Fraction arithmetic and
   full finite supports. It checks 147 finite-window identities and bounds
   on 24 examples. Forward distributions are independently verified by tuple
   enumeration on 58 generations. Critical moment equalities are checked on
   28 distributions. No floating-point claim enters the proof. The displayed
   decimals in the CSV are convenience columns only.

No counterexample to the proved bounds or conditional expansion was found.
These finite tests do not verify the asymptotic smoothness assumption (11),
which remains a proposed target for the critical model. Novelty relative to
all prior literature has not been established.
