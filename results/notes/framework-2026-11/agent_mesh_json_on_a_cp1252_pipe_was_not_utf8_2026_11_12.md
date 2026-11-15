---
name: agent_mesh_json_on_a_cp1252_pipe_was_not_utf8_2026_11_12
description: "[VERIFIED] agent_mesh --json status output fails json.load with UnicodeDecodeError 0x97 on Windows? Raw text on a cp1252 pipe; fixed 12 Nov, JSON now ASCII unless stdout is UTF-8 (c045d7773c9a)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T15:34:19+02:00
  status: provisional
  evidence: ""
---

`python agent_mesh.py --json status > file` (or any --json call read through a pipe on Windows) wrote the JSON with
ensure_ascii=False into a cp1252 stdout, so an em dash in a task line came out as the single byte 0x97 and
`json.load(open(file, encoding='utf-8'))` died with UnicodeDecodeError at byte 691,397 of 786 kB. A character cp1252
cannot hold would have raised inside the CLI instead. Fixed 12 Nov 15:1x: the three JSON print sites (print_human and
both --json branches) write ASCII-escaped JSON unless stdout is UTF-8; escaped JSON reads back to the same text.

Control: old file under PYTHONIOENCODING=cp1252 fails to parse, new file parses (0 non-ASCII bytes, 24-25 agents);
under utf-8 both parse and the output is unchanged. Live sha 0c195c827f9a0fde, backup agent_mesh.py.bak_jsonascii_20261112,
commit c045d7773c9a.

**How to apply:** a reader of an older copy's --json output on Windows should decode with errors='replace' or set
PYTHONIOENCODING=utf-8 on the call. Any new CLI that prints JSON to a pipe: ensure_ascii unless stdout is UTF-8.

