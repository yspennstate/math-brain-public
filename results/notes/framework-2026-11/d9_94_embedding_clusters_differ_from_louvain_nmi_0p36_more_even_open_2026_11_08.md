---
name: d9_94_embedding_clusters_differ_from_louvain_nmi_0p36_more_even_open_2026_11_08
description: "No swap: D9 #94 embedding clusters find an the author's memory no better than Louvain (vote10 33/56 vs 26-32/56, seeds swing 9); their edge is only smaller clusters"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:49:19+04:00
  status: verified
  evidence: "communities.tsv x embeddings k=54; user56 routing, 3 k-means seeds; 8 Nov 03:52"
---

1000-ways D9 #94 asks for TOPICS regenerated from embedding clusters, titled by each cluster's medoid. Its measure is find-the-memory success, clustered against keyword. an agent checked it on 8 Nov: the premise at about 03:49 and the find-the-memory test at 03:52. Verdict: no swap. Embedding clusters partition the memories differently, but they do not find an the author's memory any better.

Live TOPICS come from Louvain communities over the association graph (D2 #54, live since 30 Oct; ~/.claude/dreaming/communities.tsv). 46,485 of 46,940 memories have vectors, in 54 communities.
- The communities hang together in embedding space. Random same-community pairs average 0.779 cosine, against 0.693 across communities (20,000 sampled pairs).
- Embedding clusters cut the corpus differently. Spherical MiniBatch k-means with the same k = 54 scores NMI 0.358 and 0.355 against Louvain over two seeds (ARI 0.11). Two k-means seeds agree with each other at NMI 0.699; a shuffled Louvain labelling scores 0.008.
- Embedding clusters are more even. The largest k-means cluster holds 5.3% of memories. The largest Louvain community holds 17.9% (8,326 memories), under the grab-bag label "codex, compaction, claude, music".

Find-the-memory test. Bank: the 56 user questions with gold memories (eval_brain_recall_fresh BANK + BANK_V2_EXTRA). Each question was routed with the live query encoder (bge prefix) to one cluster, applied the same way to Louvain and to k-means at three seeds. A hit means a gold memory sits in the routed cluster. Routing went by the query's meaning rather than by matching titles, so the test is a stand-in for a person scanning titles.
- vote10 (the cluster most common among the query's 10 nearest memories) is neutral between the two. Louvain hits 33/56 and k-means 32, 29 and 26/56. The mean routed share is 5.1% of memories for Louvain and about 2.0% for k-means.
- centroid (the cluster whose mean vector is nearest) is built into k-means, so it favours it. Louvain hits 6/56; k-means hits 24, 22 and 17/56.
- top3 (the three nearest centroids) hits 21/56 for Louvain at 8.5% share, and 40, 31 and 35/56 for k-means at 5-6% share.
- Matched for pool size (Louvain vote10 at 5.1% against k-means top3 at 4.8-6.1%), k-means hits 31-40 against 33. It moves up to 9 questions from seed to seed.

So the embedding partition's advantage is smaller clusters, not better grouping. At an equal pool size it ties Louvain within seed noise, and 56 questions cannot separate them. Nothing in recall routes through clusters, so the only consumer would be the TOPICS view a person reads. That gain does not earn a rebuild. One thing is worth keeping: the 17.9% Louvain grab-bag is what lets centroid routing fail (6/56), so if TOPICS readability ever matters, splitting that one community is the cheaper fix. Related: [[community_super_nodes_equal_shuffled_hubs_d2_77_2026_11_03]] found Louvain community hubs added nothing to the walk over shuffled hubs.

Scripts: d9_94_louvain_vs_embedding_clusters.py (premise) and d9_94_route_eval.py (routing test). BLAS matmul warnings on this worker machine are noise.
