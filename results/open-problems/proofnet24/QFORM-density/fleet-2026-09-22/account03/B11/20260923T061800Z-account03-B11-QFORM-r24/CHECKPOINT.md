# B11 r24 early substantive checkpoint

Target remains the full quadratic-form bounded-density conjecture. This checkpoint records a new structural fact for the surviving one-sign/pair-PSD/sign-balanced chamber; it is not a full proof.

Let A be real symmetric and suppose, after multiplying coordinates by fixed signs, that A_ii>0 and 0<=A_ij<=sqrt(A_ii A_jj) for all i,j. Put u_i=sqrt(A_ii) and F=uu^T-A. Then F is symmetric, F_ii=0, F_ij>=0, and A=uu^T-F.

If s_3(A)>=s, rank-one perturbation interlacing gives s_2(F)>=s. Hence the second exterior volume

V2(F)=e_2(F^T F)=sum_{p<q}s_p(F)^2 s_q(F)^2

obeys V2(F)>=s^4.

For q_i=sum_{j!=i}F_ij^2 and W the sum of det(F_{I,J})^2 over ordered disjoint 2-subsets I,J, exact Cauchy-Binet classification by |I intersect J| gives

V2(F)=W+sum_i q_i^2-sum_{i<j}F_ij^4.

Therefore either sum_i q_i^2>=V2(F)/2, in which case

max_i q_i >= V2(F)/(2||F||_F^2) >= s_2(F)^2/4 >= s^2/4,

or W>=V2(F)/2. In the latter case a random bipartition S,T captures each ordered disjoint 2x2 minor with probability 1/16, so some cut satisfies

V2(F_{S,T})>=W/16>=s^4/32.

Thus the vague balanced hidden-minority survivor has a scale-free dichotomy: a physical defect star of l2 norm at least s/2, or a disjoint original-coordinate cross block with second exterior volume at least s^4/32. No diagonal lower bound, moment/support assumption, or spectral-coordinate independence is used.

Next in this run: quantify when the rank-one baseline u_S u_T^T lifts a rank-two defect cross block to actual third cross-volume; non-lift should force one-sided alignment/grouped-bank geometry. Then apply a completed account04/B11 result on the frustrated-sign complement and record the exact remaining gap.

Source control refreshed before this write: math-research-brain main b876a4590e19ecac249244c80cd242d801e32501, OWNER CONTROL revision 2026-09-22.15. Execution label WITHOUT_VERIFIED_BRAIN.
