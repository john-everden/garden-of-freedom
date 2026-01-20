#!/usr/bin/env sh

BUNDLE="sealed_garden_bundle.tar.gz"

echo "🌿 Verifying Garden Bundle"

echo "→ Verifying PGP signature..."
gpg --verify bundle.sig "$BUNDLE" || {
  echo "❌ Signature verification failed"
  exit 1
}
echo "✔ Signature OK"

echo "→ Verifying checksums..."
sha256sum -c checksums.txt || {
  echo "❌ Checksum mismatch"
  exit 1
}
echo "✔ Checksums OK"
echo "🌿 Bundle verified successfully"
