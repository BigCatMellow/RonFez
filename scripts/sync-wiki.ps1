[CmdletBinding()]
param(
    [string]$CommitMessage = "Sync Ron & Fez living-history wiki"
)

$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$SourceDir = Join-Path $RepoRoot "wiki"
$WikiRemote = "https://github.com/BigCatMellow/RonFez.wiki.git"
$TempRoot = Join-Path ([System.IO.Path]::GetTempPath()) "RonFez-wiki-sync"

if (-not (Test-Path $SourceDir)) {
    throw "Canonical wiki source directory not found: $SourceDir"
}

if (Test-Path $TempRoot) {
    Remove-Item -Recurse -Force $TempRoot
}

Write-Host "Cloning GitHub Wiki..."
git clone $WikiRemote $TempRoot
if ($LASTEXITCODE -ne 0) {
    throw "Could not clone $WikiRemote. Confirm that the GitHub Wiki exists and that git authentication is configured."
}

try {
    # Remove current published Markdown pages while preserving the wiki Git repository.
    Get-ChildItem -Path $TempRoot -Force |
        Where-Object { $_.Name -ne ".git" } |
        Remove-Item -Recurse -Force

    # README.md documents the canonical source system and is not meant to become a visible Wiki page.
    Get-ChildItem -Path $SourceDir -Filter "*.md" -File |
        Where-Object { $_.Name -ne "README.md" } |
        ForEach-Object {
            Copy-Item -Path $_.FullName -Destination (Join-Path $TempRoot $_.Name)
        }

    Push-Location $TempRoot
    try {
        git add --all

        $Status = git status --porcelain
        if (-not $Status) {
            Write-Host "GitHub Wiki is already in sync."
            return
        }

        git commit -m $CommitMessage
        if ($LASTEXITCODE -ne 0) {
            throw "git commit failed."
        }

        git push origin HEAD
        if ($LASTEXITCODE -ne 0) {
            throw "git push failed. Confirm that your GitHub credentials have permission to edit the Wiki."
        }

        Write-Host "GitHub Wiki synced successfully."
    }
    finally {
        Pop-Location
    }
}
finally {
    if (Test-Path $TempRoot) {
        Remove-Item -Recurse -Force $TempRoot
    }
}
