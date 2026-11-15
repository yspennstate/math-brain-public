# Source ledger

Source opened: [arXiv:1911.10579v2](https://arxiv.org/html/1911.10579), dated 7 May 2020. The [journal page](https://link.springer.com/article/10.1007/s00039-020-00544-2) gives Geometric and Functional Analysis 30, 1097–1138 (2020), DOI 10.1007/s00039-020-00544-2. Its body is subscription-only in the available view. I cannot verify whether journal statements or numbering differ.

## Exact mathematical statements from the accessible version

These are transcriptions of mathematical content with domains and quantifiers, rather than quotations of surrounding prose. As defined in §2, log means the natural logarithm. Here F:{0,1}^n→{0,1}, v=var(F), and Ĩ=I[F]/v. The introduction initially defines influence as a pivotal probability; Definition 2.3 changes that convention by a factor of four and gives I[F]=Σ_S |S| F̂(S)^2. The following is the printed notation, including that convention change.

Theorem 1.1, attributed to Kelman, Kindler, Lifshitz, Minzer and Safra:

    ∃ C>0 ∀ F ∃ ∅≠S⊆[n], |S|=O(Ĩ[F]):
      |F̂(S)| ≥ 2^{-C |S| log(1+Ĩ[F])} √var(F).
    H_∞[F] ≤ O(Ĩ[F] log(1+Ĩ[F])).

Theorem 1.2, by the same authors:

    ∀ η>0 ∃ C>0 ∀ F:
      Σ_S F̂(S)^2 1[|F̂(S)| ≤ 2^{-C Ĩ[F] log(1+Ĩ[F])}]
          ≤ η var(F).                                      (1)

Theorem 1.3, by the same authors:

    ∃ absolute K>0 ∀ D∈N ∀ F:
      H[F̂^{≤D}] ≤ K Σ_{|S|≤D} |S| log(|S|+1) F̂(S)^2 + K I[F].

The entropy of the subnormalized squared coefficients means Σ F̂(S)^2 log(1/F̂(S)^2), with no renormalization of a truncated level. Constants require separate trivial treatment when Ĩ has denominator zero. No theorem above asserts an explicit numerical value of K.

## Three carrying results

Theorem 6.6 (the main inductive technical theorem), by the same authors, has the following full parameter statement. Let k∈N, α∈(0,1], ε∈(0,1/2), and d_0,e′=d_1,...,d_k be increasing, d_0=1, with

    d_{j−1} ≥ [3/(α ε²(1−2ε)^k)] log(4(1+ε)d_j/d_{j−1}),  2≤j≤k.

Let 0<δ_k≤...≤δ_1=η and η≤10^{-320√(10e′)}. For Boolean F and real (α,d_k)-almost-homogeneous g,

    <F,g> ≤ C_1 (Σ_{|S|∼d_k}|F̂(S)|^{4/3}|ĝ(S)|^{4/3})^{3/4}
                 +C_2 I[F,g]+C_3 ||g||_2||F||_2.       (15)

For k=1:

    C_1=10d_1 η^{-300e′}, C_2=10d_1 η^{1/16}, C_3=10d_1 η.

For k>1:

    C_1=2^k (2/δ_k)^{((1+ε)/4)(d_k/d_{k−1})},
    C_2=2^k·100d_1² η^{1/16},
    C_3=2^k(1+ε)^k [10d_k η^{-300e′} δ_2^{1/4}
         +Σ_{j=2}^{k−1}(2/δ_j)^{((1+ε)/4)(d_j/d_{j−1})}
                            3^{d_{j+1}}δ_{j+1}^{1/4}].

The three specific supporting statements used below are Lemmas 2.7 and 3.5 and Corollary 6.7.

Lemma 2.7, by the same authors. For real g, I⊆[n], J=[n]\I, S⊆I:

    E_z [ ĝ_{J→z}(S)^2 ] = Σ_{T:T∩I=S} ĝ(T)^2.

The displayed expectation subscript in the HTML says z∈{0,1}^I, although J is restricted. The proof makes its intended domain {0,1}^J unambiguous. This transcription retains the mathematical identity with that domain corrected.

Lemma 3.5, by the same authors. If real h_1,...,h_k have degree at most d:

    E_x max_i h_i(x)^2
      ≤ 3^d max_i ||h_i||_2 ( E_x Σ_i h_i(x)^2 )^{1/2}.

Corollary 6.7, by the same authors. For α∈(0,1], d∈N,
0<δ≤d^{-96000/√α}, Boolean F and real (α,d)-almost-homogeneous g:

    <F,g> ≤ δ^{-10^5 d} ||F||_2^{3/4} ||g||_2^{3/4}
                max_{αd≤|S|≤d} |F̂(S) ĝ(S)|^{1/4}
            + δ^{1/16} I[F,g] + δ ||F||_2 ||g||_2,
    I[F,g] = Σ_i √(I_i[F] I_i[g]).

The statement displays δ^{1/16}. Its subsequent estimate of C_2 displays δ^{1/32}. I do not resolve that discrepancy here: the deduction in PROOFS.md uses the weaker δ^{1/32}, which suffices. The exact printed statement above has not been silently altered.

Supporting facts: Theorem 2.8 is ||h||_q≤(q−1)^{d/2}||h||_2 for degree≤d and q≥2; Lemma 2.6 bounds the expected cross-influence after restriction by the sum over surviving coordinates. Corollary 3.4 supplies a partition into m blocks preserving at least 1−2m exp(−ε²αd/(3m)) of the Fourier inner product in characters balanced across the blocks. These are the degree-reduction mechanism behind Corollary 6.7; I do not claim to have independently re-proved the whole inductive technical theorem.

## Reading the logarithm

The proof in §7.1 uses amplitude bins of width C d log(d+1). At the decisive earlier point, Corollary 6.7 requires δ to be polynomially small in d and multiplies the maximum coefficient term by δ^{-10^5 d}. This is exp(O(d log d)). A coefficient cutoff exp(−C d log d) compensates for it. In §6.3, the choice ε=1/log d and boosted base degree d_1=(1000/α)(log d)^2 produces that admissible polynomial δ scale. This identifies a quantitative loss in this proof, without establishing a sharpness theorem for Boolean functions.
