# Create 'docs' directory if it doesn't exist
if (-not (Test-Path -Path "docs" -PathType Container)) {
    Write-Host "Creating 'docs' directory..."
    New-Item -ItemType Directory -Path "docs"
} else {
    Write-Host "'docs' directory already exists."
}

# Navigate into 'docs' directory
Push-Location "docs"

# Check if package.json exists, if not, initialize a new Node.js project
if (-not (Test-Path -Path "package.json")) {
    Write-Host "package.json not found in 'docs'. Initializing new Node.js project..."
    npm init -y
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to initialize Node.js project in 'docs'."
        Pop-Location
        exit 1
    }
} else {
    Write-Host "package.json already exists in 'docs'."
}

# Install Docusaurus in the current directory ('docs')
Write-Host "Installing Docusaurus in 'docs'..."
npx create-docusaurus@latest . classic --typescript
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to install Docusaurus in 'docs'."
    Pop-Location
    exit 1
}

Write-Host "Docusaurus installation complete in 'docs' subdirectory."

# Navigate back to the original location
Pop-Location
