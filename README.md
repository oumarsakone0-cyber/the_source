# Site web — THE SOURCE TRANSPORT

Site vitrine statique (HTML / CSS / JavaScript, sans dépendance ni base de données)
pour **THE SOURCE TRANSPORT SARLU**, société de transport et de logistique
immatriculée au RCCM d'Abidjan sous le numéro `CI-ABJ-03-2016-B12-11942`.

Design : nuit bleutée et accents or, sections blanches respirantes.
Logo décliné en or (`logo-or.png`) pour rester cohérent avec la palette ;
les versions violette (`logo.png`) et blanche (`logo-blanc.png`) restent dans `assets/img/`.

---

## 1. Contenu du dossier

```
index.html              Accueil
services.html           Poids lourd, vente & location, VTC, international, léger
flotte.html             Types de véhicules et exploitation du parc
entreprise.html         Histoire, valeurs et fiche légale complète
contact.html            Coordonnées + formulaire de demande de devis
mentions-legales.html   Mentions légales et crédits photo

assets/css/style.css    Feuille de style unique (commentée, 25 sections)
assets/js/main.js       Menu, révélations au scroll, compteurs, FAQ, formulaire
assets/img/             Logo (fond transparent) et favicon
assets/img/photos/      Vos 15 photos + l'image d'attente de la vidéo
assets/video/           presentation.mp4 — la vidéo du parc, section « En images »

build/                  Générateur Python du site (facultatif, voir §5)
robots.txt / sitemap.xml
```

## 2. Mise en ligne

Le site est **entièrement statique** : copiez le contenu du dossier à la racine de
votre hébergement (`public_html`, `www`…) via FTP. Aucune installation, aucun PHP,
aucune base de données.

Hébergements compatibles sans configuration : tout hébergement mutualisé, Netlify,
Vercel, GitHub Pages, Cloudflare Pages.

Avant la mise en ligne, remplacez `https://www.thesourcetransport.ci/` par votre
domaine réel dans `sitemap.xml` et dans le bloc `application/ld+json` de chaque page.

## 3. Photos et vidéo

**Toutes les images du site sont vos propres photographies.** Elles sont
hébergées dans `assets/img/photos/` : le site ne dépend d'aucune banque
d'images ni d'aucun service extérieur pour son contenu visuel.

### Correspondance fichier → emplacement

| Fichier (`assets/img/photos/`) | Où il apparaît |
|---|---|
| `hero.jpg` | Bannière de l'accueil + bannière Mentions légales |
| `partenaire.jpg` | « Votre partenaire de confiance » + Flotte + bannière Contact |
| `lourd.jpg` | « Transport poids lourd » (accueil + Services) |
| `vente.jpg` | « Vente & location de véhicules » (accueil + Services) |
| `vtc.jpg` | « Transport VTC » (accueil, Services, Flotte) |
| `international.jpg` | « Transport international » (accueil, Services, Flotte) |
| `leger.jpg` | « Transport léger & distribution » (accueil, Services, Flotte) |
| `benne.jpg` | Zone d'intervention, bannière Services, Flotte, appel à l'action Entreprise |
| `citerne.jpg` | Appels à l'action accueil et Services, Flotte, bannière Entreprise |
| `parc.jpg` | Bannière de la page Flotte |
| `equipe.jpg` | Page Entreprise + appel à l'action Flotte |
| `iveco.jpg` | En réserve — plus affichée depuis la refonte des services |
| `cabines.jpg` | En réserve — plus affichée depuis la refonte des services |
| `video-poster.jpg` | Image d'attente de la vidéo |

Aucune page n'affiche deux fois la même photo.

> **À remplacer :** `vente.jpg`, `vtc.jpg` et `leger.jpg` réutilisent
> provisoirement des photos de camions. Déposez à leur place vos photos de
> pickups, de véhicules de tourisme et de voitures VTC, en gardant les mêmes
> noms de fichiers.

Pour changer une image : **écrasez le fichier en gardant son nom**, c'est tout.
Le texte alternatif de chaque photo (utile au référencement et aux lecteurs
d'écran) se règle dans le dictionnaire `PHOTOS` de `build/photos.py`.

Format conseillé : paysage, 1600 px de large minimum, JPEG.

### La vidéo du parc

`assets/video/presentation.mp4` alimente la section « Notre parc, filmé sur
place » de l'accueil. Elle **démarre automatiquement, sans son et en boucle** ;
un bouton en bas à droite permet au visiteur d'activer le son. La lecture se met
en pause dès que la vidéo sort de l'écran, pour ménager la batterie sur mobile.

Pour la remplacer, déposez votre fichier sous le même nom. Si elle dépasse une
dizaine de Mo, ré-encodez-la d'abord :

```bash
ffmpeg -i source.mp4 -c:v libx264 -crf 26 -preset slow \
       -c:a aac -b:a 96k -movflags +faststart assets/video/presentation.mp4
```

L'image d'attente s'extrait ensuite ainsi :

```bash
ffmpeg -i assets/video/presentation.mp4 -ss 12 -frames:v 1 -q:v 2 \
       assets/img/photos/video-poster.jpg
```

## 4. Le formulaire de devis

Un site statique ne peut pas envoyer d'e-mail par lui-même. Le formulaire de
`contact.html` ouvre donc la messagerie du visiteur avec un message pré-rempli
adressé à `thesourcetransport@gmail.com`.

Pour recevoir les demandes directement dans votre boîte :

- **Formspree ou Web3Forms** (gratuit) : créez un formulaire, récupérez l'URL
  fournie, puis dans `contact.html` remplacez
  `<form class="form" id="devis-form" novalidate>` par
  `<form class="form" action="https://formspree.io/f/VOTRE_ID" method="POST">`
  et supprimez l'attribut `id="devis-form"`.
- **Hébergement avec PHP** : remplacez l'action par un script `envoi.php` maison.

## 5. Personnalisation courante

| À modifier | Où |
|---|---|
| Téléphones, e-mail, adresses, RCCM | dictionnaire `CO` en haut de `build/build.py`, ou directement dans les `.html` |
| Couleur d'accent (or) | variables `--gold`, `--gold-2`, `--gold-600`, `--gold-700` en haut de `style.css` |
| Fonds sombres | variables `--night`, `--night-2`, `--night-3` |
| Fond clair, textes, bordures | variables `--paper`, `--ink`, `--muted`, `--line` |
| Polices | balise `<link>` Google Fonts + variables `--ff-display` / `--ff-body` |
| Textes | directement dans les fichiers `.html` |

### Régénérer le site

Les pages sont générées à partir de gabarits Python pour garantir un en-tête et un
pied de page identiques partout :

```bash
cd build && python3 build.py
```

Si vous préférez éditer les `.html` à la main, c'est parfaitement possible :
supprimez simplement le dossier `build/`.

## 6. Points techniques

- Contenu large jusqu'à 1500 px puis centré ; responsive de 320 px à écran large, vérifié sans débordement horizontal.
- Images en chargement différé (`loading="lazy"`) et servies en plusieurs tailles
  via `srcset` — l'affichage mobile ne télécharge pas les versions grand écran.
- Animations désactivées automatiquement si le visiteur a activé
  « réduire les animations » dans son système (`prefers-reduced-motion`).
- Navigation au clavier, contrastes conformes, attribut `alt` sur chaque image.
- Données structurées Schema.org (`MovingCompany`) sur chaque page pour le
  référencement local.
- Feuille de style d'impression incluse.
- Aucun script tiers, aucun cookie, aucun traceur.
