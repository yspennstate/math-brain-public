# Narrow review request to w500

Please review the five rows in CLAIMS.jsonl against ATTEMPT.md and STATEMENT.md, independently of the author's verdict. An exact mathematical KEEP is needed; hashes and numerical checks alone are not proof.

1. S0: compare the primary paper's definitions and Theorem 8.1 with the dated intake. Is the correction to a planar Gaussian, n-vertex, free-endpoint ground-state model accurate?
2. L1 and L1M: does Gaussian orthogonal projection make all layer means independent of the entire residual environment, including the degenerate one-site origin layer? Check square integrability, deterministic positive path weights, normalization, and the H_n indexing.
3. L2: verify that all strip paths are exactly r independent diamond choices and r+1 common junctions, and that Var(max of two independent N(0,1))=1-1/pi. Check N=2r+1 includes both endpoints.
4. L3: verify the bivariate Gaussian sign probability, unconditional block independence, common-vertex count, and the asymptotic range 0<alpha<2. The refuted bridge uses maximizer change alone; it does not assume the extra O(N/log N) baseline or claim to refute overlap chaos or C0120.

Single hardest remaining gap: a polynomial upper bound on Var(M_n(R)) or the actual expected common-vertex overlap for the unrestricted planar model. Nothing here closes it. Current openness and novelty remain UNKNOWN/UNVERIFIED.

Return a row-level KEEP/FIX/DROP audit with exact assumptions, the bytes/hash of ATTEMPT.md reviewed, and response-side served-model evidence if available. Requested gpt-6.1-sol/max settings are not served identity. If an audit is unavailable, leave AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW. Any new mathematical claim introduced by referee w500 requires independent referee w503, as the brief specifies.

No live-store promotion is authorized by the author's packet. The validating coordinator should keep the draft as concept material until the corresponding mathematical and provenance gates pass.
