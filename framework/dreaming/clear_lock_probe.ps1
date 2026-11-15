# clear_lock_probe.ps1 - run Clear-StaleIndexLock from a given copy of dream_git_sync.ps1 on one repo and print the
# result as one JSON line. Used by test_clear_stale_index_lock.py and for a hand run on a real clone.
param(
    [Parameter(Mandatory = $true)][string] $Lib,
    [Parameter(Mandatory = $true)][string] $Repo,
    [int] $Min = 10,
    [int] $Max = 60,
    [int] $SetBackMinutes = 0
)
$ErrorActionPreference = 'Stop'
. $Lib
$lock = Join-Path $Repo '.git\index.lock'
if ($SetBackMinutes -gt 0 -and (Test-Path -LiteralPath $lock)) {
    $t = (Get-Date).AddMinutes(-$SetBackMinutes)
    $fi = Get-Item -LiteralPath $lock -Force
    $fi.CreationTime = $t
    $fi.LastWriteTime = $t
}
$said = New-Object System.Collections.Generic.List[string]
$r = Clear-StaleIndexLock -Repo $Repo -MinAgeMinutes $Min -MaxAgeMinutes $Max -Logger { param($m) $said.Add([string] $m) }
$aside = ''
if ($r.SetAside) { $aside = Split-Path $r.SetAside -Leaf }
[pscustomobject]@{
    present = [bool] $r.Present; cleared = [bool] $r.Cleared; reason = [string] $r.Reason; aside = $aside
    lock_left = [bool] (Test-Path -LiteralPath $lock); said = ($said -join ' | ')
} | ConvertTo-Json -Compress
