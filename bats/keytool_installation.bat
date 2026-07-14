@echo off
setlocal enabledelayedexpansion

REM ============================================================
REM  keytool_installation.bat
REM  keytool is NOT a standalone program and NOT a pip package.
REM  It ships inside the Java JDK. This script makes keytool
REM  available on your PATH, installing a JDK if necessary.
REM ============================================================

echo(
echo === Step 1: Check if keytool is already on PATH ===
where keytool >nul 2>&1
if %errorlevel%==0 (
    echo keytool is already available:
    where keytool
    goto :verify
)
echo keytool not found on PATH.

echo(
echo === Step 2: Look for an existing JDK installation ===
set "JDKBIN="
for /d %%D in ("C:\Program Files\Java\jdk*") do (
    if exist "%%D\bin\keytool.exe" set "JDKBIN=%%D\bin"
)
for /d %%D in ("C:\Program Files\Eclipse Adoptium\jdk*") do (
    if exist "%%D\bin\keytool.exe" set "JDKBIN=%%D\bin"
)

if defined JDKBIN (
    echo Found existing JDK: "!JDKBIN!"
    goto :addpath
)

echo No JDK found.

echo(
echo === Step 3: Install a JDK via winget (includes keytool) ===
where winget >nul 2>&1
if not %errorlevel%==0 (
    echo winget is not available on this system.
    echo Please install a JDK manually from https://adoptium.net/ and re-run this script.
    goto :end
)
winget install --id EclipseAdoptium.Temurin.21.JDK --accept-source-agreements --accept-package-agreements
if not %errorlevel%==0 (
    echo winget install failed. Install a JDK manually from https://adoptium.net/.
    goto :end
)

REM Re-scan for the freshly installed JDK
for /d %%D in ("C:\Program Files\Eclipse Adoptium\jdk*") do (
    if exist "%%D\bin\keytool.exe" set "JDKBIN=%%D\bin"
)
for /d %%D in ("C:\Program Files\Java\jdk*") do (
    if exist "%%D\bin\keytool.exe" set "JDKBIN=%%D\bin"
)
if not defined JDKBIN (
    echo JDK installed, but keytool.exe was not located automatically.
    echo Open a NEW terminal; winget usually adds it to PATH.
    goto :end
)

:addpath
echo(
echo === Step 4: Add "!JDKBIN!" to your user PATH (persistent) ===
powershell -NoProfile -Command ^
  "$dir='!JDKBIN!';" ^
  "$cur=[Environment]::GetEnvironmentVariable('Path','User');" ^
  "if (($cur -split ';') -notcontains $dir) {" ^
  "  [Environment]::SetEnvironmentVariable('Path', ($cur.TrimEnd(';') + ';' + $dir), 'User');" ^
  "  Write-Host 'Added to user PATH.'" ^
  "} else { Write-Host 'Already on user PATH.' }"

REM Make keytool usable in THIS session too
set "PATH=%PATH%;!JDKBIN!"

:verify
echo(
echo === Verify ===
keytool -help >nul 2>&1
if %errorlevel%==0 (
    echo SUCCESS: keytool is working.
    echo NOTE: Open a NEW terminal so the PATH change applies everywhere.
) else (
    echo keytool still not found in this session. Open a new terminal and run: keytool -help
)

:end
echo(
pause
endlocal
