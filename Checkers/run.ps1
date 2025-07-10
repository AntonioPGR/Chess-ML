param (
  [string]$cppFile
)

clear
$exeName = [System.IO.Path]::GetFileNameWithoutExtension($cppFile) + ".exe"

g++ $cppFile -o $exeName 2>$null

& .\${exeName}
Remove-Item $exeName
