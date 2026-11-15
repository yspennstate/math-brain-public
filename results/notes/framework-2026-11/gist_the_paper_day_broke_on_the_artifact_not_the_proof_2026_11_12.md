---
name: gist_the_paper_day_broke_on_the_artifact_not_the_proof_2026_11_12
description: "Where do our papers actually fail - the mathematics or the artifact? The 12 Nov pass says the artifact: of the 13 memories it filed, 10 are defects in the ARTIFACT around correct mathematics (a missed citation on ten posted papers, a constant's digits, an untracked input so the pushed commit does not build, 286 dead private links before a permanent DOI, CRLF checksums, an empty Zenodo references field, 24 lagging files, a decline for an unedited introduction), 2 are the rule machinery, 1 is the mathematics (paper13 Thm 1.1 false on a second read) - the checking effort sits on the proof and the risk sits one layer out"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T10:35:51+02:00
  status: verified
  evidence: "the 13 paper memories dated 2026-11-12 in the memory dir, counted and split; his 05:59 and 06:30 prompts of the same morning"
---

On 12 November the brain spent the day turning math-store results into posted papers - five got their own
repositories and Zenodo DOIs, three were held - and filed thirteen memories about that pass. Reading them
together: TEN are about the artifact around the mathematics, TWO are about the rule machinery, and ONE is
about the mathematics itself.

The ten: a citation every one of ten posted FEI papers misses (Li and G. Han, arXiv:2512.03117); a constant
copied with the wrong digits (Sen-Virag is 0.828843, square 0.686981); a main.tex that pulls in a notation
appendix git never tracked, so the paper builds here and not from the pushed commit (ising-perceptron-margin
711afce, fixed at 0815fbd); 286 dead placeholder links to a private repository, caught and rewritten in the
hour before a permanent DOI (pseudo-cognitive-dynamics e54cd02); checksum receipts that hashed the CRLF
working copy instead of the stored blob, and a read loop that wrote empty hashes; a Zenodo record whose
references field had to be filled by a metadata edit after the deposition; twenty-four files on GitHub
lagging their Zenodo copies across two old repositories; and a journal declining a paper for an unedited
introduction - explicitly not for its mathematics. The one mathematical defect: paper13's Theorem 1.1 is
false, found by a second independent read, not by the writer.

The shape: the brain's checking effort sits on the proof, and the day's failures sat one layer out, between
a correct proof and a correct public object. That layer is cheap to check and expensive to get wrong - a
Zenodo DOI cannot be withdrawn, and a missing citation is a public mistake under his name. It is also
exactly where he was pointing the same morning, twice, before any of this was filed: 05:59, on the
rejection letter, "more editing, more auditing, less self introspeciton ... publishable as is"; 06:30,
"another 1k hooks ... about how to actually write papers". The 1,101 pw1k rules and the citation hooks that
landed that morning are the machinery for this layer; the audit of them found their own pattern lists
matching their own prose, which is the same error one level up - a checker measuring itself rather than
the thing.

What to do with it: a paper is not done when the proof is right. Before a push or a DOI, the artifact gets
its own pass - every citation, every constant against its source, the pushed tree building on its own,
every link public and live, the receipt hashing the stored blob, the record's reference field, the PDF
rebuilt from the pushed source - and the mathematics gets a reader who did not write it.

Where this would read wrong: it is one day's thirteen memories, and a day spent posting naturally fills
with posting defects. The claim is about the RATIO of effort to risk, not about the mathematics being
sound in general - paper13 says it is not. The check that would break it: take the next twenty paper
memories and count the same split; if the artifact share falls below half once the pw1k machinery is
running, the machinery is working and this gist is history.

Related: [[pw1k_thousand_paper_writing_rules_one_word_one_thing_2026_11_12]],
[[paper_hooks_audit_pattern_lists_measure_their_own_sentences_2026_11_12]],
[[ptrf_declined_for_unedited_introduction_not_for_mathematics_2026_11_12]],
[[paper13_fusion_thm_1_1_false_second_read_2026_11_12]],
[[public_edition_papers_carry_dead_private_repo_links_rewrite_before_doi_2026_11_12]],
[[paper_commit_inputs_an_untracked_file_builds_locally_only_2026_11_12]],
[[fei_papers_miss_li_han_sharp_constants_2512_03117_2026_11_12]],
[[sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12]],
[[five_math_brain_papers_got_own_repos_and_zenodo_dois_three_held_2026_11_12]],
[[research_writing_human_voice_2026_06_10]]

