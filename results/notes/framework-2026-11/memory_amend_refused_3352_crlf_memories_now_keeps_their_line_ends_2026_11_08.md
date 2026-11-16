---
name: memory_amend_refused_3352_crlf_memories_now_keeps_their_line_ends_2026_11_08
description: "Why did brain.py amend refuse a memory with 'no --- frontmatter block with LF'? It was CRLF (3,352 of 50,991 on the second machine); amend now edits pure-CRLF files and keeps their line ends; 4,844 verified memories still need --evidence to append"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:05:14+04:00
  status: verified
  evidence: "scratch test with BRAIN_MEM_DIR (CRLF prefix kept, 0 bare LF; mixed refused; LF byte-equal); push f3fd0b0969"
---

Why did brain.py amend fail with "no '---' frontmatter block with LF line ends at the top of the file"? The memory was written on Windows and is CRLF throughout. On the second machine on 8 Nov, 3,352 of 50,991 memory files were CRLF, and amend refused every one of them, so none of them could take an appended correction or a status change.

Fix (an agent, 8 Nov): memory_amend.py now reads a file that is CRLF on every line through an LF copy, applies the edit, and writes it back CRLF. The file keeps its line ends, and the bytes before the edit are unchanged. A file with mixed line ends is still refused, because converting it would rewrite lines nobody asked to change. Tested in a scratch folder with BRAIN_MEM_DIR. The CRLF memory's original bytes were kept as a prefix, with 0 bare LFs after the append. The mixed file was refused. An LF memory came out byte-for-byte equal to the old behaviour. The mirror is pushed to 12_cognitive_architecture/dreaming/memory_amend.py (f3fd0b0969), where it had been missing. Pre-fix copy: session memory_amend.pre_crlf.py.

A second refusal of the same kind is not fixed: amend asks for --evidence on any verified or owner-stated memory that has none, even for a plain append. That covers 4,844 of the 15,148 verified memories. The refusal names the flag, so an agent can pass real evidence. Do not paste the evidence of whatever you are appending as the memory's own.

How to apply: when amend refuses a memory, read its first bytes (od -c | head) before assuming the memory is broken. Bulk edits to memories go through amend and keep each file's line ends.

