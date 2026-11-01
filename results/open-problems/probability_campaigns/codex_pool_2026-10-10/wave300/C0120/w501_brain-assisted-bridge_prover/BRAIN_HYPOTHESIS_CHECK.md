# Four complete cards compared with the proof need

Evidence files: selected_export_cards.json contains the four complete export rows; selected_live_cards.json contains four full indexed read-only store lookups, including body, metadata and claim payload. Raw indexed lookup completed in 0.0041898 s. It does not certify that serving would return these revisions or that every card is independently verified.

1. Hypercontractivity (claim_0737ca41c6ea0a974d06054742cc0b45): vocabulary card says a Markov semigroup satisfies ||P_t f||_q<=||f||_p when q-1<=exp(2t/C)(p-1), with C=1 for OU. Its provenance explicitly says not reviewed. This identifies the bridge but is not proof authority. Chatterjee Lemma 4.1 supplies the complete bounded-function Gaussian version used in L2; f_v are [0,1]-valued indicators, g is a finite independent standard Gaussian vector, and the OU normalization matches.

2. Mehler formula (claim_3a7f53cc4f4c10093c8e4e07c223f18d52212a9c7d6f98c1196f104f16111a3d): standard Gaussian measure, self-adjoint L2 semigroup, generator Laplacian-x.grad. The source triangle gives a finite standard Gaussian vector. M_n is Lipschitz and has square-integrable gradient of squared norm n; it meets the covariance lemma's Sobolev/integrability need. Time is not rescaled. This is useful for L1's monotonicity and covariance formula.

3. Talagrand L1-L2 (claim_19af561bcf040b56cc9b3aa80d52d5dd62e1e00c1b7ecb97b574cbacb19b5603): its exact hypotheses are uniform product measure on {-1,1}^m, coordinate flip derivatives, square-integrable f, and universal C. Our variables are continuous Gaussian and derivatives are weak partial derivatives. The cube theorem cannot be applied directly. The card's mention of analogues supplies no complete Gaussian theorem or a power rate. No use of that unsupported extrapolation appears in the proof.

4. C0120 (claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d): current lookup reproduces the intake's general-dimensional Var(log Z_n) attribution. Its metadata says statement_fidelity_reviewed=false and truth_status=unverified. The cited source instead defines Gaussian planar free-endpoint M_n in Section 8. The exact differing text and a correction request will be saved in STORE_CORRECTION.json; no store write is authorized.

Brain contribution: retrieval pointed to hypercontractivity and OU, while hypothesis comparison excluded the cube shortcut and exposed the source mismatch. L3 then refutes the direct per-site envelope as a route to a power improvement. The measurable improvement offered here is a bounded read-only fallback and a source/certificate-scope repair; no global recall improvement is claimed.

NEXT: Referee L3's certificate/variance distinction and the correction request; seek a coupled-path geometric estimate stronger than per-site hypercontractivity.
