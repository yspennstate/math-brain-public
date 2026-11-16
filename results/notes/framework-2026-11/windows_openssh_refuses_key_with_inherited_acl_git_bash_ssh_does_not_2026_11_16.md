---
name: windows_openssh_refuses_key_with_inherited_acl_git_bash_ssh_does_not_2026_11_16
description: "Scheduled task's ssh says 'Permission denied (publickey)' but Git Bash ssh works? Windows OpenSSH ignores a private key with inherited ACL entries; fix with icacls /inheritance:r. It silently broke a nightly data pull."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

A scheduled task's ssh fails with "Permission denied (publickey)" while the same alias works from Git Bash? Look at
the key file's Windows permissions first.

What happened. A nightly Windows scheduled task (wscript launching a Python script) pulls data from a remote Linux
machine with `ssh -o BatchMode=yes <alias> bash -s`. On 15 Nov its pull ended "rc 255 ... Permission denied
(publickey)", and a dashboard fed by it quietly went stale. Interactive ssh to the same alias from Git Bash had
worked all day.

Cause. Two different ssh programs. Git Bash's ssh does not look at Windows file permissions. Windows OpenSSH
(C:/Windows/System32/OpenSSH/ssh.exe), which a scheduled task or a Python subprocess gets, refuses a private key
that anyone besides the owner, SYSTEM and Administrators can read, then offers no key at all, so the server answers
publickey denied. The key had inherited two extra entries from its folder (a sandbox users group and one more SID).

Fix. `icacls <key> /save <file>` for the before-state, then
`icacls <key> /inheritance:r /grant:r "<user>:(F)" "SYSTEM:(F)" "Administrators:(F)"`. Windows ssh then connected,
and the next nightly pull ended rc 0.

How to check next time. Run the failing command with the Windows binary by full path, not from Git Bash. `icacls
<key>` must list only those three principals. A key written by a tool inherits the folder's entries, so do this for
every key a scheduled task uses.

Wider lesson. "It works when I run it" was said from a different program than the one the task runs. A dashboard
that goes stale quietly needs its producer's own log read, not a test from an interactive shell.
