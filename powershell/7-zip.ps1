# Set the base URL
$pageUrl = "https://www.7-zip.org/"

# Find download link with regular expression
$regex = "a/[\s\S]+x64\.exe"
$downloadFileLink = (Invoke-WebRequest -Uri $pageUrl).Links | Where-Object href -match $regex

# Define the output file name
$outputFileName = $downloadFileLink.href -replace "a/", ""

# Download the file
Invoke-WebRequest -Uri ($pageUrl + $downloadFileLink.href) -OutFile $outputFileName