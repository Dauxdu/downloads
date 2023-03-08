# Set the base URL
$pageUrl = "https://codecguide.com/download_k-lite_codec_pack_mega.htm"

# Find download link with regular expression
$regex = "files3\.codecguide\.com/[\s\S]+\.exe"
$downloadFileLink = (Invoke-WebRequest -Uri $pageUrl).Links | Where-Object href -match $regex

# Define the output file name
$outputFileName = ($downloadFileLink.href -split '/')[-1]

# Download the file
Invoke-WebRequest -Uri $downloadFileLink.href -OutFile $outputFileName
