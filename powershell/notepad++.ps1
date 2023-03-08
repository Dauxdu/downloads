# Set the base URL
$pageUrl = "https://notepad-plus-plus.org"

# Find download link with regular expression
$downloadPageRegex = "(/downloads/)[\s\S]"
$downloadPageLink = (Invoke-WebRequest -Uri $pageUrl).Links | Where-Object href -match $downloadPageRegex

$downloadLinkRegex = "[\s\S]Installer\.x64\.exe.sig"
$downloadFileLink = (Invoke-WebRequest -Uri ($pageUrl + $downloadPageLink.href)).Links | Where-Object href -match $downloadLinkRegex

# Define the output file name
$outputFileName = $downloadFileLink.href.split("/", 9)[8].replace(".sig", "")

# Downloading file
Invoke-WebRequest ($downloadFileLink.href.replace(".sig", "")) -OutFile $outputFileName
