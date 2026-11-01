param(
    [string]$Main = "main.tex"
)

$ErrorActionPreference = "Stop"

$base = Split-Path -Parent $MyInvocation.MyCommand.Path

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Exe,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    & $Exe @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Exe failed with exit code $LASTEXITCODE"
    }
}

Push-Location $base
try {
    Invoke-Checked -Exe "pdflatex" -Arguments @("-interaction=nonstopmode", "-halt-on-error", $Main)
    Invoke-Checked -Exe "bibtex" -Arguments @([System.IO.Path]::GetFileNameWithoutExtension($Main))
    Invoke-Checked -Exe "pdflatex" -Arguments @("-interaction=nonstopmode", "-halt-on-error", $Main)
    Invoke-Checked -Exe "pdflatex" -Arguments @("-interaction=nonstopmode", "-halt-on-error", $Main)
}
finally {
    Pop-Location
}
