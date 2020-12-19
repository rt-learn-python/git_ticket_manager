#!/bin/bash
# Original Script Below
# https://makandracards.com/makandra/333510-linux-shell-script-to-easily-update-chromedriver

VERSION_URL="https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
VERSION=$(curl -f --silent $VERSION_URL)
if [ -z "$VERSION" ]; then
  echo "Failed to read current version from $VERSION_URL. Aborting."
  exit 1
else
  echo "Current version is $VERSION"
fi

# Abort script if any of the next commands fails.
set -e
set -o pipefail

ZIPFILEPATH="$HOME/Desktop/Delete Daily/chromedriver-$VERSION.zip"
rm "$ZIPFILEPATH" || true

echo "Downloading to $ZIPFILEPATH"
curl -f --silent "https://chromedriver.storage.googleapis.com/$VERSION/chromedriver_mac64.zip" > "$ZIPFILEPATH"

BINFILEPATH="/Applications/DevApps/chromedriver"

# Create a backup then delete
mv "$BINFILEPATH" "$BINFILEPATH-previous"

echo "Extracting to $BINFILEPATH"
unzip -p "$ZIPFILEPATH" chromedriver > "$BINFILEPATH"

echo Setting execute flag
chmod +x "$BINFILEPATH"

echo Removing ZIP file
rm "$ZIPFILEPATH"
rm "$BINFILEPATH-previous"

echo Done
chromedriver -v
