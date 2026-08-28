# -*- coding: utf-8 -*-
"""
Télécharge toutes les photos du site dans assets/img/photos/,
puis régénère les pages pour qu'elles pointent vers ces fichiers locaux.

    cd build
    python3 telecharger-photos.py

Après cela, le site ne dépend plus d'aucun service extérieur pour ses images.
Pour revenir au CDN : relancer simplement « python3 build.py ».
"""
import os, sys, subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.pop("LOCAL", None)
import photos as P                                    # noqa: E402

DEST = os.path.join(HERE, "..", "assets", "img", "photos")
os.makedirs(DEST, exist_ok=True)

print("Téléchargement de %d photos vers assets/img/photos/\n" % len(P.PHOTOS))
for key in P.PHOTOS:
    out = os.path.join(DEST, key + ".jpg")
    if os.path.exists(out) and os.path.getsize(out) > 20000:
        print("  = %-14s déjà présent" % key)
        continue
    url = P.url(key, w=1800, q=78)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(out, "wb") as f:
            f.write(r.read())
        print("  + %-14s %6.0f Ko" % (key, os.path.getsize(out) / 1024))
    except Exception as e:
        print("  ! %-14s ÉCHEC : %s" % (key, e))

print("\nRégénération des pages en mode local...")
env = dict(os.environ, LOCAL="1")
subprocess.run([sys.executable, os.path.join(HERE, "build.py")], env=env, check=True)
print("\nTerminé. Les pages pointent maintenant vers assets/img/photos/.")
