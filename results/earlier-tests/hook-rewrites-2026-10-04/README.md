# Does the math hook survive a reworded question? (4 October 2026)

A metamorphic test of the math brain's prompt hook. Each of the 218 questions of the fresh bank (178 whose
answer is in the store, 40 whose answer is not) was rewritten in ways that keep its meaning, and the live hook
was run on every version, 1,427 calls in all. A rewrite should not change whether the hook serves the stored
answer, and it should not make the hook fire on a question the store cannot answer. The bank's questions are not
published.

## Rewrites

| rewrite | what changes |
|---|---|
| typo | lower case, and up to three words of five letters or more each get one slip (two letters swapped, one dropped or doubled, a neighbouring key), never inside notation |
| dict_typo | a word is spelled the way a reviewed list of the owner's habitual misspellings records it; the hook is built to read these, so this is a positive control |
| lower_nopunct | lower case, sentence punctuation removed, notation kept |
| prefix_ops | an unrelated operational sentence in front of the question |
| suffix_ops | the same kind of sentence after it |
| wrapper | "can you tell me ..." around the question |
| clause_swap | two sentences in the other order |

Every rewrite is deterministic from a fixed seed and the item. The hook's own time limit cut no call short.

## Results

On the original wording the hook served the stored answer on 158 of the 178 answerable questions (139 of them
as the first card) and fired on 27 of the 40 questions the store cannot answer.

| rewrite | pairs | served | first card | silent | lost | gained | absent pairs | fired | new fires | quieted |
|---|---|---|---|---|---|---|---|---|---|---|
| original | 178 | 158 | 139 | 9 | | | 40 | 27 | | |
| typo | 178 | 96 | 80 | 68 | 66 | 4 | 40 | 20 | 5 | 12 |
| dict_typo | 100 | 91 | 79 | 3 | 0 | 0 | 15 | 11 | 0 | 0 |
| lower_nopunct | 178 | 156 | 134 | 11 | 2 | 0 | 40 | 26 | 0 | 1 |
| prefix_ops | 178 | 129 | 112 | 41 | 30 | 1 | 40 | 11 | 1 | 17 |
| suffix_ops | 178 | 137 | 121 | 35 | 23 | 2 | 40 | 14 | 1 | 14 |
| wrapper | 178 | 155 | 136 | 14 | 3 | 0 | 40 | 20 | 1 | 8 |
| clause_swap | 4 | 3 | 3 | 0 | 0 | 0 | 0 | | | |

"Lost" counts questions where the original served the stored answer and the rewrite did not; "gained" the
reverse. On the dict_typo pairs the original served 91 and so did the rewrite, with the same first card on 98 of
100.

## Reading

Case, punctuation, a polite wrapper and the misspellings the hook already knows cost almost nothing. Ordinary
typing slips are the hook's weak point: one slip in each of up to three longer words cost 66 of 158 served
answers, and most of those questions went silent rather than to a wrong card. An unrelated sentence in the same
prompt costs 23 to 30 answers, about as much in front as behind, and also quiets the hook on questions it should
not answer (fires on the absent questions fall from 27 to 11 and 14), so in a mixed prompt the hook is more
cautious, not more confused.
