# -*- coding: utf-8 -*-
"""Générateur statique du site THE SOURCE TRANSPORT."""
import os, sys, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import photos as P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# ---------------------------------------------------------------- Données
CO = {
    'name': 'THE SOURCE TRANSPORT',
    'form': 'SARLU',
    'capital': '100 000 000 F CFA',
    'rccm': 'CI-ABJ-03-2016-B12-11942',
    'ncc': '1623412Q',
    'imm': '03/05/2016',
    'siege': 'Bingerville — FEH KESSE, 26 BP 849 Abidjan 26',
    'addr': 'Riviera, Saint-Bernard Attoban, Rue L23 — Abidjan',
    'mail': 'thesourcetransport@gmail.com',
    'tel1': '+225 07 77 31 76 44',
    'tel2': '+225 01 60 09 04 60',
    'gerant': 'M. LOBOUHO Arnaud',
}
TEL1 = CO['tel1'].replace(' ', '')
TEL2 = CO['tel2'].replace(' ', '')

NAV = [
    ('index.html', 'Accueil'),
    ('services.html', 'Services'),
    ('flotte.html', 'Flotte'),
    ('entreprise.html', 'Entreprise'),
    ('contact.html', 'Contact'),
]

# ---------------------------------------------------------------- Icônes
def ico(p):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % p)

I = {
 'truck': ico('<path d="M1 3h13v13H1z"/><path d="M14 8h4l3 4v4h-7z"/><circle cx="6" cy="19" r="2"/><circle cx="17" cy="19" r="2"/>'),
 'box':   ico('<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/>'),
 'ware':  ico('<path d="M3 21V9l9-6 9 6v12"/><path d="M8 21v-8h8v8"/><path d="M8 17h8"/>'),
 'globe': ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.7 2.6 15.3 0 18-2.6-2.7-2.6-15.3 0-18z"/>'),
 'route': ico('<circle cx="6" cy="18" r="3"/><circle cx="18" cy="6" r="3"/><path d="M9.5 17.5h5a4 4 0 0 0 0-8h-5a4 4 0 0 1 0-8"/>'),
 'shield':ico('<path d="M12 2l8 3v6c0 5-3.4 9.4-8 11-4.6-1.6-8-6-8-11V5z"/><path d="M9 12l2 2 4-4"/>'),
 'clock': ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>'),
 'pin':   ico('<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>'),
 'phone': ico('<path d="M22 16.9v2.6a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 0 0 1-6-6A19.6 19.6 0 0 1 2.4 4 2 2 0 0 1 4.4 2H7a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/>'),
 'mail':  ico('<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>'),
 'users': ico('<path d="M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 20v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>'),
 'chart': ico('<path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/>'),
 'doc':   ico('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h6"/>'),
 'gear':  ico('<circle cx="12" cy="12" r="3.2"/><path d="M19.4 15a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.6 1.6 0 0 0-1.8-.3 1.6 1.6 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1A1.6 1.6 0 0 0 9 19.4a1.6 1.6 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.6 1.6 0 0 0 .3-1.8 1.6 1.6 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1A1.6 1.6 0 0 0 4.6 9a1.6 1.6 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.6 1.6 0 0 0 1.8.3H9a1.6 1.6 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.6 1.6 0 0 0 1 1.5 1.6 1.6 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 1.6 0 0 0-.3 1.8V9a1.6 1.6 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.6 1.6 0 0 0-1.5 1z"/>'),
 'leaf':  ico('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.6 5-7"/>'),
 'up':    ico('<path d="M12 19V5M6 11l6-6 6 6"/>'),
 'head':  ico('<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><path d="M20 16.5a2 2 0 0 1-2 2h-1v-5h1a2 2 0 0 1 2 2z"/><path d="M4 16.5a2 2 0 0 0 2 2h1v-5H6a2 2 0 0 0-2 2z"/>'),
 'tag':   ico('<path d="M20.6 13.4 12 22l-9-9V3h10z"/><circle cx="7.5" cy="7.5" r="1.6"/>'),
 'car':   ico('<path d="M5 17h14M4 17v-4.2L6 8h12l2 4.8V17"/><path d="M3 12.8h18"/><circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/>'),
 'key':   ico('<circle cx="7.5" cy="15.5" r="4"/><path d="M10.5 12.5 20 3l1.5 1.5-1.5 1.5 1.5 1.5-2 2-1.5-1.5-1.5 1.5"/>'),
 'soundoff': ico('<path d="M11 5 6 9H3v6h3l5 4z"/><path d="M22 9l-6 6M16 9l6 6"/>'),
 'soundon':  ico('<path d="M11 5 6 9H3v6h3l5 4z"/><path d="M16 8.5a5 5 0 0 1 0 7"/><path d="M19 5.5a9 9 0 0 1 0 13"/>'),
 'play':  ico('<path d="M7 4.5v15l13-7.5z"/>'),
 'track': ico('<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/><path d="M4.5 19.5c1.6 1 4.3 1.6 7.5 1.6s5.9-.6 7.5-1.6"/>'),
}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')

# ---------------------------------------------------------------- Gabarit
def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{CO['name']}">
<meta name="theme-color" content="#0E131C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{CO['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{P.url('hero', 1200, 630)}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"MovingCompany",
  "name":"{CO['name']}",
  "legalName":"{CO['name']} {CO['form']}",
  "url":"https://www.thesourcetransport.ci/",
  "logo":"assets/img/logo-or.png",
  "image":"{P.url('hero', 1200, 630)}",
  "email":"{CO['mail']}",
  "telephone":"{CO['tel1']}",
  "foundingDate":"2016-05-03",
  "taxID":"{CO['ncc']}",
  "address":{{"@type":"PostalAddress","streetAddress":"Riviera, Saint-Bernard Attoban, Rue L23","addressLocality":"Abidjan","addressCountry":"CI"}},
  "areaServed":["Côte d'Ivoire","Burkina Faso","Mali","Ghana"],
  "description":"{desc}"
}}
</script>
</head>
<body>
"""

def header(over=False):
    links = ''.join(
        f'<a class="nav__link{" is-active" if h == page_active else ""}" href="{h}">{t}</a>'
        for h, t in NAV)
    mlinks = ''.join(f'<a class="m-link" href="{h}">{t}</a>' for h, t in NAV)
    return f"""
<a class="skip" href="#main" style="position:absolute;left:-9999px">Aller au contenu</a>
<header class="header{" header--over" if over else ""}">
  <div class="wrap header__inner">
    <a class="brand" href="index.html" aria-label="{CO['name']} — accueil">
      <img src="assets/img/logo-or.png" alt="{CO['name']}" width="120" height="88">
      <span class="brand__txt">
        <span class="brand__name">THE SOURCE</span>
        <span class="brand__sub">Transport &amp; Logistique</span>
      </span>
    </a>
    <nav class="nav" aria-label="Navigation principale">{links}</nav>
    <div class="header__cta">
      <a class="btn btn--ghost" href="tel:{TEL1}">{CO['tel1']}</a>
      <a class="btn" href="contact.html">Demander un devis</a>
      <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu-mobile">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="menu-mobile">
  {mlinks}
  <div class="mobile-menu__foot">
    <span>Parlons de votre fret</span>
    <a href="tel:{TEL1}">{CO['tel1']}</a>
    <a href="mailto:{CO['mail']}">{CO['mail']}</a>
  </div>
</div>
<main id="main">
"""

def footer():
    cols = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="assets/img/logo-or.png" alt="{CO['name']}" width="120" height="88">
        <p>Transport de marchandises et solutions logistiques en Côte d'Ivoire et sur les corridors ouest-africains. Société {CO['form']} au capital de {CO['capital']}.</p>
      </div>
      <div><h4>Navigation</h4><ul>{cols}</ul></div>
      <div>
        <h4>Nos services</h4>
        <ul>
          <li><a href="services.html#poids-lourd">Transport poids lourd</a></li>
          <li><a href="services.html#vente-location">Vente &amp; location de véhicules</a></li>
          <li><a href="services.html#international">Transport international</a></li>
          <li><a href="services.html#vtc">Transport VTC</a></li>
          <li><a href="services.html#leger">Transport léger &amp; distribution</a></li>
        </ul>
      </div>
      <div>
        <h4>Nous joindre</h4>
        <ul>
          <li><a href="https://maps.google.com/?q=Riviera+Saint+Bernard+Attoban+Abidjan" target="_blank" rel="noopener">{CO['addr']}</a></li>
          <li><a href="tel:{TEL1}">{CO['tel1']}</a></li>
          <li><a href="tel:{TEL2}">{CO['tel2']}</a></li>
          <li><a href="mailto:{CO['mail']}">{CO['mail']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year></span> {CO['name']} {CO['form']} — Tous droits réservés.</span>
      <div class="footer__legal">
        <span>RCCM : {CO['rccm']}</span>
        <span>NCC : {CO['ncc']}</span>
        <a href="mentions-legales.html">Mentions légales</a>
      </div>
    </div>
  </div>
</footer>
<button class="totop" aria-label="Revenir en haut de page">{I['up']}</button>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def pagehead(title, desc, crumb, photo):
    return f"""
<section class="pagehead">
  <div class="pagehead__bg">{P.img(photo, 2000, 900, sizes="100vw", eager=True)}</div>
  <div class="wrap">
    <div class="pagehead__inner">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span>/</span><span>{crumb}</span></nav>
      <h1 data-anim="up">{title}</h1>
      <p data-anim="up" data-delay="80">{desc}</p>
    </div>
  </div>
</section>
"""

MARQUEE = """
<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
    <span class="marquee__item">Abidjan</span><span class="marquee__item">San Pedro</span>
    <span class="marquee__item">Yamoussoukro</span><span class="marquee__item">Bouaké</span>
    <span class="marquee__item">Korhogo</span><span class="marquee__item">Man</span>
    <span class="marquee__item">Ferkessédougou</span><span class="marquee__item">Ouagadougou</span>
    <span class="marquee__item">Bamako</span><span class="marquee__item">Accra</span>
    <span class="marquee__item">Lomé</span><span class="marquee__item">Conakry</span>
  </div>
</div>
"""

def cta(title, text, photo='citerne'):
    return f"""
<section class="section">
  <div class="wrap">
    <div class="cta-band" data-anim="zoom">
      <div class="cta-band__bg">{P.img(photo, 1800, 700, sizes="100vw")}</div>
      <span class="eyebrow eyebrow--light">Passons à l'action</span>
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="btn-row">
        <a class="btn" href="contact.html">Demander un devis {ARROW}</a>
        <a class="btn btn--outline-light" href="tel:{TEL1}">{CO['tel1']}</a>
      </div>
    </div>
  </div>
</section>
"""

def svc(anchor, num, icon, title, intro, bullets, tags, photo, rev=False):
    lis = ''.join(f'<li>{b}</li>' for b in bullets)
    tg = ''.join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""
<article class="svc{' svc--rev' if rev else ''}" id="{anchor}">
  <div class="svc__media" data-anim="{'right' if rev else 'left'}">
    <span class="num">{num}</span>
    {P.img(photo, 940, 705, sizes="(max-width:1080px) 100vw, 47vw")}
  </div>
  <div class="svc__body" data-anim="{'left' if rev else 'right'}" data-delay="90">
    <div class="icon-box">{icon}</div>
    <h3>{title}</h3>
    <p class="lead">{intro}</p>
    <ul class="checks">{lis}</ul>
    <div class="tag-list">{tg}</div>
  </div>
</article>
"""

# ================================================================ PAGES
pages = {}

# ---------------------------------------------------------------- ACCUEIL
pages['index.html'] = dict(
    over=True,
    title=f"{CO['name']} — Transport de marchandises &amp; logistique en Côte d'Ivoire",
    desc="Transporteur agréé basé à Abidjan : transport poids lourd, vente et location de véhicules et de pickups, transport VTC, corridors ouest-africains et distribution urbaine. Société SARLU au capital de 100 000 000 F CFA.",
    body=f"""
<section class="hero">
  <div class="hero__bg">{P.img('hero', 2000, 1150, sizes="100vw", eager=True)}</div>
  <div class="wrap">
    <div class="hero__content">
      <span class="badge anim-in"><span class="badge__dot"></span> Votre fret, notre priorité</span>
      <h1 class="anim-in">Transport sécurisé,<br>livraison assurée.</h1>
      <p class="hero__lead anim-in">Poids lourd, vente et location de véhicules, VTC : depuis Abidjan vers toute la Côte d'Ivoire et les corridors ouest-africains. Une flotte suivie, des délais tenus, un interlocuteur unique.</p>
      <div class="btn-row anim-in">
        <a class="btn" href="services.html">Nos services {ARROW}</a>
        <a class="btn btn--outline-light" href="contact.html">Demander un devis</a>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="hero__strip">
      <div class="hero__strip-item"><span class="ring">{I['shield']}</span><span><b>Sécurité garantie</b><span>Vos marchandises entre de bonnes mains.</span></span></div>
      <div class="hero__strip-item"><span class="ring">{I['clock']}</span><span><b>Livraison à temps</b><span>Respect des délais, notre engagement.</span></span></div>
      <div class="hero__strip-item"><span class="ring">{I['track']}</span><span><b>Suivi des expéditions</b><span>Informé à chaque étape du trajet.</span></span></div>
      <div class="hero__strip-item"><span class="ring">{I['head']}</span><span><b>Un interlocuteur</b><span>Un chargé de compte qui connaît votre dossier.</span></span></div>
    </div>
  </div>
</section>

{MARQUEE}

<!-- Qui sommes-nous -->
<section class="section">
  <div class="wrap">
    <div class="panel panel--bleed" data-anim="up">
      <div class="panel__body">
        <span class="eyebrow eyebrow--light">À propos de nous</span>
        <h2>Votre partenaire<br>de confiance</h2>
        <p class="lead lead--light" style="margin-top:20px">Née à Abidjan en 2016, <strong style="color:#fff">{CO['name']}</strong> s'est recentrée en 2023 sur un métier unique : déplacer des marchandises avec méthode, pour les industriels et les distributeurs ivoiriens.</p>
        <ul class="checks checks--light">
          <li>Société {CO['form']} au capital de {CO['capital']}, entièrement libéré</li>
          <li>Réseau national et corridors sous-régionaux</li>
          <li>Poids lourd, pickups, VTC, vente et location de véhicules</li>
        </ul>
        <div class="btn-row" style="margin-top:32px">
          <a class="btn" href="entreprise.html">En savoir plus {ARROW}</a>
        </div>
      </div>
      <div class="panel__media">{P.img('partenaire', 1000, 900, sizes="(max-width:1080px) 100vw, 46vw")}</div>
    </div>
  </div>
</section>

<!-- Chiffres -->
<section class="section section--tight">
  <div class="wrap">
    <div class="statband" data-anim="up">
      <div class="statband__item"><span class="ring">{I['doc']}</span><span><b data-count="2016" data-plain>0</b><span>Immatriculée au RCCM</span></span></div>
      <div class="statband__item"><span class="ring">{I['chart']}</span><span><b data-count="100" data-suffix=" M">0</b><span>F CFA de capital social</span></span></div>
      <div class="statband__item"><span class="ring">{I['globe']}</span><span><b data-count="4" data-suffix=" pays">0</b><span>Corridors desservis</span></span></div>
      <div class="statband__item"><span class="ring">{I['truck']}</span><span><b data-count="5" data-suffix=" services">0</b><span>Prestations couvertes</span></span></div>
    </div>
  </div>
</section>

<!-- Vidéo du parc -->
<section class="section dark">
  <div class="wrap">
    <div class="videoblock">
      <div class="videoblock__text" data-anim="left">
        <span class="eyebrow eyebrow--light">En images</span>
        <h2 class="title-bar">Notre parc, filmé sur place</h2>
        <p class="lead lead--light" style="margin-top:22px">Pas de mise en scène : nos ensembles routiers sur le parc, prêts au départ. Tracteurs, bennes et semi-remorques que nous affectons chaque jour aux chargements de nos clients.</p>
        <ul class="checks checks--light">
          <li>Tracteurs et porteurs entretenus et contrôlés avant chaque mission</li>
          <li>Bennes et semi-remorques adaptées au fret industriel et au BTP</li>
          <li>Chauffeurs affectés nommément à chaque véhicule</li>
        </ul>
        <div class="btn-row" style="margin-top:32px">
          <a class="btn" href="flotte.html">Découvrir la flotte {ARROW}</a>
          <a class="btn btn--outline-light" href="contact.html">Demander un devis</a>
        </div>
      </div>
      <figure class="videoblock__player" data-anim="right" data-delay="110">
        <video id="video-parc" poster="assets/img/photos/video-poster.jpg"
               autoplay muted loop playsinline preload="metadata"
               aria-label="Vidéo du parc de véhicules de THE SOURCE TRANSPORT">
          <source src="assets/video/presentation.mp4" type="video/mp4">
          Votre navigateur ne peut pas lire cette vidéo.
          <a href="assets/video/presentation.mp4">Télécharger la vidéo</a>.
        </video>
        <button class="videoblock__sound" type="button" aria-pressed="false"
                aria-label="Activer le son de la vidéo">
          <span class="videoblock__sound-on">{I['soundon']}</span>
          <span class="videoblock__sound-off">{I['soundoff']}</span>
        </button>
      </figure>
    </div>
  </div>
</section>

<!-- Métiers -->
<section class="section section--soft">
  <div class="wrap">
    <div class="section-head center" data-anim="up">
      <span class="eyebrow">Nos métiers</span>
      <h2>Deux expertises au cœur de notre activité</h2>
      <p class="lead" style="margin-inline:auto">Le reste de notre offre gravite autour de ces deux piliers : acheminer lourd et loin, et mettre les bons véhicules à la disposition de nos clients.</p>
    </div>

    {svc('poids-lourd', '01', I['truck'], 'Transport poids lourd',
      "Notre cœur de métier. Tracteurs et porteurs pour vos charges lourdes, volumineuses ou hors gabarit, sur l'ensemble du réseau ivoirien et vers le Sahel. Chargement encadré, itinéraire validé, arrivée confirmée.",
      ["Fret industriel, matériaux de construction, vrac conditionné",
       "Semi-remorques bâchées, plateaux, porte-conteneurs 20' et 40'",
       "Chauffeurs expérimentés, formés aux procédures de sécurité",
       "Point de situation à chaque étape clé du trajet"],
      ["Longue distance", "Hors gabarit", "Conteneurs", "Vrac"], 'lourd')}

    {svc('vente-location', '02', I['key'], 'Vente &amp; location de véhicules',
      "Au-delà du transport, nous vendons et louons des véhicules : tracteurs, porteurs, pickups et véhicules de tourisme. Avec ou sans chauffeur, à la journée, au mois ou en longue durée.",
      ["Vente de tracteurs, porteurs et semi-remorques",
       "Vente de pickups double cabine et de véhicules de tourisme",
       "Location courte et longue durée, avec ou sans conducteur",
       "Entretien, assurance et gestion administrative pris en charge"],
      ["Vente", "Location", "Pickups", "Longue durée"], 'vente', rev=True)}

    <div class="grid grid-3" style="margin-top:34px">
      <article class="pcard" data-anim="up">
        <div class="pcard__vis"><span class="pcard__badge">International</span>{P.img('international', 700, 438, sizes="(max-width:1080px) 100vw, 32vw")}</div>
        <div class="pcard__body"><h3>Transport international</h3><p>Acheminement vers le Burkina Faso, le Mali et les pays côtiers voisins, avec accompagnement des formalités de corridor.</p><a class="link-arrow" href="services.html#international">En savoir plus {ARROW}</a></div>
      </article>
      <article class="pcard" data-anim="up" data-delay="90">
        <div class="pcard__vis"><span class="pcard__badge">Distribution</span>{P.img('leger', 700, 438, sizes="(max-width:1080px) 100vw, 32vw")}</div>
        <div class="pcard__body"><h3>Transport léger &amp; distribution</h3><p>Pickups et utilitaires pour la messagerie, la distribution urbaine et les livraisons sensibles dans le Grand Abidjan.</p><a class="link-arrow" href="services.html#leger">En savoir plus {ARROW}</a></div>
      </article>
      <article class="pcard" data-anim="up" data-delay="180">
        <div class="pcard__vis"><span class="pcard__badge">VTC</span>{P.img('vtc', 700, 438, sizes="(max-width:1080px) 100vw, 32vw")}</div>
        <div class="pcard__body"><h3>Transport VTC</h3><p>Mise à disposition de véhicules de tourisme avec chauffeur : transferts aéroport, déplacements d'affaires et mises à disposition à la journée.</p><a class="link-arrow" href="services.html#vtc">En savoir plus {ARROW}</a></div>
      </article>
    </div>
  </div>
</section>

<!-- Engagements -->
<section class="section dark">
  <div class="wrap">
    <div class="section-head" data-anim="up">
      <span class="eyebrow">Nos engagements</span>
      <h2>Ce que vous obtenez en travaillant avec nous</h2>
    </div>
    <div class="grid grid-4">
      <article class="card" data-anim="up"><div class="icon-box">{I['clock']}</div><h3>Délais annoncés</h3><p>Un créneau d'enlèvement et une date de livraison contractualisés dès l'acceptation du devis.</p></article>
      <article class="card" data-anim="up" data-delay="80"><div class="icon-box">{I['shield']}</div><h3>Marchandise couverte</h3><p>Arrimage vérifié, véhicules entretenus et couverture de responsabilité du transporteur.</p></article>
      <article class="card" data-anim="up" data-delay="160"><div class="icon-box">{I['users']}</div><h3>Interlocuteur unique</h3><p>Un chargé d'exploitation joignable, qui connaît votre dossier et vos contraintes.</p></article>
      <article class="card" data-anim="up" data-delay="240"><div class="icon-box">{I['doc']}</div><h3>Traçabilité documentaire</h3><p>Lettre de voiture, bon de livraison émargé et archivage numérique de chaque expédition.</p></article>
    </div>
  </div>
</section>

<!-- Méthode -->
<section class="section">
  <div class="wrap">
    <div class="section-head" data-anim="up">
      <span class="eyebrow">Notre méthode</span>
      <h2>Quatre étapes, aucune zone d'ombre</h2>
    </div>
    <div class="grid grid-4">
      <div class="step" data-anim="up"><span class="step__num">01</span><h3>Analyse du besoin</h3><p>Nature du fret, tonnage, itinéraire et contraintes de délai. Nous validons la faisabilité avant de chiffrer.</p></div>
      <div class="step" data-anim="up" data-delay="90"><span class="step__num">02</span><h3>Devis &amp; planification</h3><p>Proposition détaillée sous 24 à 48 h, affectation du véhicule et du chauffeur, créneau confirmé.</p></div>
      <div class="step" data-anim="up" data-delay="180"><span class="step__num">03</span><h3>Enlèvement &amp; transport</h3><p>Chargement contrôlé, arrimage sécurisé, suivi du convoi et information en cas d'aléa.</p></div>
      <div class="step" data-anim="up" data-delay="270"><span class="step__num">04</span><h3>Livraison &amp; preuve</h3><p>Déchargement, émargement du bon de livraison et transmission des documents sous 24 h.</p></div>
    </div>
  </div>
</section>

<!-- Couverture -->
<section class="section section--soft">
  <div class="wrap">
    <div class="grid grid-2" style="gap:clamp(38px,5.5vw,68px);align-items:center">
      <div data-anim="left">
        <span class="eyebrow">Zone d'intervention</span>
        <h2>D'Abidjan aux corridors du Sahel</h2>
        <p class="lead" style="margin-top:18px">Notre objet social nous autorise à opérer en Côte d'Ivoire et à l'étranger. Concrètement, nous couvrons quotidiennement l'axe côtier et les grands corridors qui relient le port d'Abidjan aux pays de l'hinterland.</p>
        <ul class="checks">
          <li><strong>Côte d'Ivoire</strong> — Abidjan, San Pedro, Yamoussoukro, Bouaké, Korhogo, Man</li>
          <li><strong>Burkina Faso</strong> — corridor Abidjan / Ouagadougou</li>
          <li><strong>Mali</strong> — corridor Abidjan / Bamako via Ferkessédougou</li>
          <li><strong>Pays côtiers</strong> — Ghana, Togo, Guinée sur demande</li>
        </ul>
      </div>
      <div data-anim="right" data-delay="110">
        <div class="svc__media">{P.img('benne', 940, 705, sizes="(max-width:1080px) 100vw, 47vw")}</div>
      </div>
    </div>
  </div>
</section>

{cta("Un chargement à faire partir ?", "Envoyez-nous les caractéristiques de votre fret : nous revenons vers vous avec un devis chiffré et un créneau d'enlèvement sous 24 à 48 heures ouvrées.", 'citerne')}
""")

# ---------------------------------------------------------------- SERVICES
pages['services.html'] = dict(
    title=f"Nos services — {CO['name']}",
    desc="Transport poids lourd, vente et location de véhicules et de pickups, transport VTC, corridors internationaux et distribution urbaine depuis Abidjan.",
    body=pagehead("Des solutions de transport taillées pour votre chaîne d'approvisionnement",
                  "De l'enlèvement en usine à la livraison finale, nous couvrons chaque maillon du parcours de votre marchandise.",
                  "Services", 'benne') + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head" data-anim="up">
      <span class="eyebrow">Prestations</span>
      <h2>Cinq prestations, une seule logique : la fiabilité</h2>
      <p class="lead">Chaque prestation est cadrée par un devis écrit, un délai annoncé et une preuve de livraison. Rien n'est laissé à l'appréciation du moment.</p>
    </div>

    {svc('poids-lourd', '01', I['truck'], 'Transport poids lourd de marchandises',
      "Notre activité principale. Nous acheminons vos charges lourdes et volumineuses sur l'ensemble du territoire ivoirien et vers les pays limitrophes, avec des ensembles routiers adaptés à la nature de votre fret.",
      ["Fret industriel, matériaux de construction, équipements et machines",
       "Transport de conteneurs 20' et 40' depuis et vers le port d'Abidjan",
       "Charges hors gabarit avec étude d'itinéraire préalable",
       "Arrimage contrôlé et vérification avant départ systématique",
       "Chauffeurs titulaires des permis et habilitations requis"],
      ["Longue distance", "Conteneurs", "Hors gabarit", "Vrac conditionné"], 'lourd')}

    {svc('vente-location', '02', I['key'], 'Vente &amp; location de véhicules',
      "Nous vendons et louons des véhicules à nos clients professionnels : ensembles routiers, porteurs, pickups double cabine et véhicules de tourisme. Une réponse rapide quand acheter n'est pas la bonne option, ou quand il faut renforcer un parc.",
      ["Vente de tracteurs, porteurs et semi-remorques",
       "Vente de pickups double cabine et de véhicules de tourisme",
       "Location à la journée, au mois ou en longue durée",
       "Mise à disposition avec ou sans conducteur",
       "Entretien, assurance et gestion administrative inclus dans la location"],
      ["Vente", "Location", "Pickups", "Avec chauffeur", "Longue durée"], 'vente', rev=True)}

    {svc('vtc', '03', I['car'], 'Transport VTC &amp; mise à disposition',
      "Des véhicules de tourisme avec chauffeur pour vos collaborateurs et vos visiteurs. Transferts aéroport, déplacements d'affaires dans Abidjan, missions en région : le conducteur, le véhicule et le carburant sont de notre côté.",
      ["Transferts aéroport Félix-Houphouët-Boigny, arrivées et départs",
       "Déplacements d'affaires dans le Grand Abidjan",
       "Mise à disposition à la demi-journée, à la journée ou au mois",
       "Véhicules de tourisme récents et entretenus",
       "Chauffeurs affectés nommément, ponctualité contractualisée"],
      ["Transferts aéroport", "Mise à disposition", "Déplacements d'affaires"], 'vtc')}

    {svc('international', '04', I['globe'], 'Transport international &amp; corridors',
      "Notre objet social couvre les opérations de transport en Côte d'Ivoire et à l'étranger. Nous opérons sur les corridors reliant le port d'Abidjan aux pays de l'hinterland, avec accompagnement des formalités de passage.",
      ["Corridor Abidjan — Ouagadougou (Burkina Faso)",
       "Corridor Abidjan — Bamako (Mali) via Ferkessédougou",
       "Liaisons vers le Ghana, le Togo et la Guinée sur demande",
       "Assistance sur les documents de transit et de passage frontalier",
       "Coordination avec vos transitaires et commissionnaires en douane"],
      ["Burkina Faso", "Mali", "Ghana", "Corridors", "Transit"], 'international', rev=True)}

    {svc('leger', '05', I['route'], 'Transport léger &amp; distribution urbaine',
      "Pour les flux fractionnés et les livraisons sensibles, nos pickups et véhicules utilitaires assurent la messagerie et la distribution capillaire dans le Grand Abidjan et les villes de l'intérieur.",
      ["Distribution vers points de vente, agences et chantiers",
       "Enlèvements et livraisons express en zone urbaine",
       "Tournées régulières planifiées à la semaine ou au mois",
       "Livraison contre signature avec preuve numérique"],
      ["Messagerie", "Distribution", "Express", "Tournées"], 'leger')}
  </div>
</section>

<!-- Secteurs -->
<section class="section section--soft">
  <div class="wrap">
    <div class="section-head center" data-anim="up">
      <span class="eyebrow">Secteurs servis</span>
      <h2>Des filières aux exigences différentes</h2>
      <p class="lead" style="margin-inline:auto">Nous adaptons le véhicule, le conditionnement et le protocole d'exploitation à la réalité de votre secteur.</p>
    </div>
    <div class="grid grid-3">
      <article class="card" data-anim="up"><div class="icon-box">{I['ware']}</div><h3>BTP &amp; matériaux</h3><p>Ciment, agrégats, ferraillage et équipements de chantier livrés au pied de l'ouvrage, dans des fenêtres horaires contraintes.</p></article>
      <article class="card" data-anim="up" data-delay="80"><div class="icon-box">{I['box']}</div><h3>Industrie &amp; agro-industrie</h3><p>Matières premières entrantes et produits finis sortants, avec cadencement adapté à vos lignes de production.</p></article>
      <article class="card" data-anim="up" data-delay="160"><div class="icon-box">{I['chart']}</div><h3>Distribution &amp; négoce</h3><p>Réapprovisionnement de réseaux de points de vente et livraisons en tournée régulière.</p></article>
      <article class="card" data-anim="up" data-delay="240"><div class="icon-box">{I['globe']}</div><h3>Import-export</h3><p>Post-acheminement portuaire, mise à quai, dépotage et évacuation de conteneurs depuis Abidjan.</p></article>
      <article class="card" data-anim="up" data-delay="320"><div class="icon-box">{I['leaf']}</div><h3>Agriculture</h3><p>Collecte et évacuation de productions agricoles vers les usines de transformation et les ports.</p></article>
      <article class="card" data-anim="up" data-delay="400"><div class="icon-box">{I['gear']}</div><h3>Énergie &amp; mines</h3><p>Acheminement d'équipements et de consommables vers des sites isolés, avec étude d'accès préalable.</p></article>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section">
  <div class="wrap wrap--narrow">
    <div class="section-head center" data-anim="up">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Ce que nos clients demandent avant de signer</h2>
    </div>
    <div class="acc" data-anim="up">
      <div class="acc__item">
        <button class="acc__btn" aria-expanded="false">Sous quel délai obtient-on un devis ?<span class="acc__ico"></span></button>
        <div class="acc__panel"><p>Sous 24 à 48 heures ouvrées pour une demande standard, dès lors que nous disposons de la nature du fret, du tonnage ou du volume, des points d'enlèvement et de livraison et de la date souhaitée. Pour les charges hors gabarit, comptez quelques jours supplémentaires liés à l'étude d'itinéraire.</p></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn" aria-expanded="false">Travaillez-vous au coup par coup ou sous contrat ?<span class="acc__ico"></span></button>
        <div class="acc__panel"><p>Les deux. Nous traitons des expéditions ponctuelles comme des flux réguliers. Pour les clients contractuels, nous mettons en place une grille tarifaire annuelle, un chargé de compte dédié et un reporting périodique des expéditions réalisées.</p></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn" aria-expanded="false">Comment suit-on une expédition en cours ?<span class="acc__ico"></span></button>
        <div class="acc__panel"><p>Votre chargé d'exploitation vous confirme le chargement, vous informe au passage des points clés de l'itinéraire et vous signale immédiatement tout aléa. La preuve de livraison émargée vous est transmise dans les 24 heures suivant le déchargement.</p></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn" aria-expanded="false">Quels documents sont établis pour chaque transport ?<span class="acc__ico"></span></button>
        <div class="acc__panel"><p>Une lettre de voiture accompagne systématiquement la marchandise, complétée d'un bon de livraison émargé au déchargement. Pour les corridors internationaux, nous coordonnons avec votre transitaire les documents de transit et de passage frontalier.</p></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn" aria-expanded="false">Prenez-vous en charge le chargement et le déchargement ?<span class="acc__ico"></span></button>
        <div class="acc__panel"><p>Le chargement est réalisé sous notre contrôle avec les moyens du site expéditeur, sauf convention contraire. Nous pouvons organiser les moyens de manutention nécessaires ; cette prestation est alors chiffrée séparément dans le devis.</p></div>
      </div>
    </div>
  </div>
</section>

{cta("Décrivez-nous votre flux, nous le chiffrons.", "Un enlèvement ponctuel ou un contrat annuel : dans les deux cas, la démarche commence par un échange de dix minutes.", 'citerne')}
""")

# ---------------------------------------------------------------- FLOTTE
def fleet(photo, badge, name, desc, specs):
    sp = ''.join(f'<div class="spec"><span>{a}</span><span>{b}</span></div>' for a, b in specs)
    return f"""
<article class="pcard" data-anim="up">
  <div class="pcard__vis"><span class="pcard__badge">{badge}</span>{P.img(photo, 700, 438, sizes="(max-width:1080px) 100vw, 32vw")}</div>
  <div class="pcard__body"><h3>{name}</h3><p>{desc}</p>{sp}</div>
</article>
"""

pages['flotte.html'] = dict(
    title=f"Notre flotte — {CO['name']}",
    desc="Semi-remorques, porte-conteneurs, bennes, citernes et véhicules utilitaires : les moyens roulants mobilisés par THE SOURCE TRANSPORT.",
    body=pagehead("Des véhicules choisis pour la nature de votre fret",
                  "Nous mobilisons le matériel adapté à chaque chargement, en propre ou via notre réseau de partenaires affrétés, sous notre entière responsabilité d'exploitation.",
                  "Flotte", 'parc') + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head" data-anim="up">
      <span class="eyebrow">Types de véhicules</span>
      <h2>Le bon outil pour le bon chargement</h2>
      <p class="lead">Le choix du véhicule n'est jamais anodin : il détermine le temps de chargement, la sécurité de l'arrimage et le coût final au kilomètre. Nous le proposons avec le devis.</p>
    </div>
    <div class="grid grid-3">
      {fleet('international', 'Portuaire', "Porte-conteneurs", "Châssis 20' et 40' pour le post-acheminement portuaire et l'évacuation de conteneurs depuis Abidjan.", [("Format","20' / 40'"),("Usage","Import-export"),("Zone","Port &amp; corridors")])}
      {fleet('partenaire', 'Longue distance', "Tracteurs &amp; semi-remorques", "Ensembles routiers pour le fret palettisé et les marchandises générales sur longue distance.", [("Type","Tautliner / plateau"),("Usage","Fret général"),("Zone","National &amp; sous-région")])}
      {fleet('benne', 'Chantier', "Bennes &amp; plateaux", "Transport de matériaux de construction, d'agrégats et d'équipements de chantier.", [("Type","Benne / plateau"),("Usage","BTP &amp; carrières"),("Zone","Chantiers")])}
      {fleet('citerne', 'Spécifique', "Convois &amp; citernes", "Transport de charges spéciales et de produits en vrac, avec protocoles de sécurité renforcés.", [("Type","Citerne / convoi"),("Usage","Charges spéciales"),("Zone","Sur étude")])}
      {fleet('leger', 'Urbain', "Pickups &amp; utilitaires", "Pickups double cabine et véhicules utilitaires pour la distribution, les chantiers et les missions en région.", [("Type","Pickup / utilitaire"),("Usage","Distribution &amp; chantier"),("Zone","Urbain &amp; régional")])}
      {fleet('vtc', 'Tourisme', "Véhicules de tourisme", "Berlines et véhicules de tourisme mis à disposition avec chauffeur, ou proposés à la vente et à la location.", [("Type","Berline / tourisme"),("Usage","VTC &amp; location"),("Zone","Abidjan &amp; intérieur")])}
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="grid grid-2" style="gap:clamp(38px,5.5vw,68px);align-items:center">
      <div data-anim="left">
        <span class="eyebrow eyebrow--light">Exploitation</span>
        <h2>Un parc suivi, pas seulement possédé</h2>
        <p class="lead lead--light" style="margin-top:18px">Posséder des véhicules ne suffit pas : ce qui tient les délais, c'est la discipline d'exploitation. Chaque unité mobilisée passe par les mêmes contrôles avant de prendre la route.</p>
        <ul class="checks checks--light">
          <li>Contrôle avant départ : pneumatiques, freinage, éclairage, arrimage</li>
          <li>Entretien préventif planifié et carnet de suivi par véhicule</li>
          <li>Documents de bord et visites techniques tenus à jour</li>
          <li>Chauffeurs affectés nommément à chaque mission</li>
          <li>Capacité d'affrètement pour absorber les pics de charge</li>
        </ul>
      </div>
      <div data-anim="right" data-delay="110">
        <div class="grid grid-2" style="gap:18px">
          <div class="card"><div class="icon-box">{I['shield']}</div><h3 style="font-size:1rem">Contrôle systématique</h3><p style="font-size:.87rem">Aucun départ sans validation du point de contrôle avant mission.</p></div>
          <div class="card"><div class="icon-box">{I['gear']}</div><h3 style="font-size:1rem">Entretien préventif</h3><p style="font-size:.87rem">Un planning d'entretien par véhicule, indépendant des pannes.</p></div>
          <div class="card"><div class="icon-box">{I['users']}</div><h3 style="font-size:1rem">Chauffeurs formés</h3><p style="font-size:.87rem">Habilitations à jour et sensibilisation continue à la sécurité routière.</p></div>
          <div class="card"><div class="icon-box">{I['clock']}</div><h3 style="font-size:1rem">Disponibilité</h3><p style="font-size:.87rem">Réseau de partenaires affrétés mobilisable en cas de forte demande.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

{cta("Vous ne savez pas quel véhicule choisir ?", "Décrivez-nous votre marchandise et vos points d'enlèvement : nous vous recommandons la configuration la plus économique et la plus sûre.", 'equipe')}
""")

# ---------------------------------------------------------------- ENTREPRISE
pages['entreprise.html'] = dict(
    title=f"L'entreprise — {CO['name']}",
    desc="Histoire, valeurs et informations légales de THE SOURCE TRANSPORT SARLU, société de transport et de logistique immatriculée au RCCM d'Abidjan.",
    body=pagehead("Une société ivoirienne qui a choisi son métier",
                  "De la restauration au transport : l'histoire d'un recentrage assumé sur une activité unique, exercée avec rigueur.",
                  "Entreprise", 'citerne') + f"""
<section class="section">
  <div class="wrap">
    <div class="grid grid-2" style="gap:clamp(38px,5.5vw,72px);align-items:start">
      <div data-anim="left">
        <span class="eyebrow">Notre histoire</span>
        <h2>Dix ans de terrain, une trajectoire assumée</h2>
        <p class="lead" style="margin-top:18px">Immatriculée au Registre du Commerce et du Crédit Mobilier d'Abidjan le {CO['imm']}, la société a d'abord exercé dans la restauration. En 2023, ses associés ont opéré un changement complet de cap : nouvelle dénomination, nouvel objet social, capital porté à {CO['capital']} et transformation en {CO['form']}.</p>
        <p>Ce recentrage n'a rien d'anecdotique. Il traduit une conviction simple : le transport de marchandises est un métier exigeant, qui ne se pratique pas à temps partiel. Depuis, l'intégralité de nos moyens humains et financiers est consacrée à une seule chose — faire arriver la marchandise de nos clients.</p>

        <div class="timeline">
          <div class="tl-item" data-anim="up"><time>MAI 2016</time><h3>Immatriculation au RCCM d'Abidjan</h3><p>Création de la société sous la forme SARL, sous le numéro {CO['rccm']}.</p></div>
          <div class="tl-item" data-anim="up" data-delay="80"><time>JUIN 2023</time><h3>Changement de dénomination et d'objet social</h3><p>La société devient {CO['name']} et adopte un objet social entièrement dédié au transport et à la logistique.</p></div>
          <div class="tl-item" data-anim="up" data-delay="160"><time>JUIN 2023</time><h3>Augmentation de capital et transformation</h3><p>Le capital social est porté de 1 000 000 à {CO['capital']} et la société adopte la forme {CO['form']}.</p></div>
          <div class="tl-item" data-anim="up" data-delay="240"><time>AOÛT 2023</time><h3>Nomination d'un nouveau gérant</h3><p>{CO['gerant']} prend la direction de la société en qualité d'associé-gérant.</p></div>
          <div class="tl-item" data-anim="up" data-delay="320"><time>AUJOURD'HUI</time><h3>Transport, véhicules, corridors</h3><p>Une activité structurée autour du poids lourd, de la vente et location de véhicules et du VTC, au service des entreprises ivoiriennes.</p></div>
        </div>
      </div>

      <div data-anim="right" data-delay="110">
        <div class="svc__media" style="margin-bottom:24px">{P.img('equipe', 920, 660, sizes="(max-width:1080px) 100vw, 46vw")}</div>
        <div class="legal-card">
          <div class="legal-card__head"><span class="eyebrow">Fiche d'identité</span><h3>Informations légales</h3></div>
          <dl>
            <div class="legal-row"><dt>Dénomination sociale</dt><dd>{CO['name']}</dd></div>
            <div class="legal-row"><dt>Forme juridique</dt><dd>{CO['form']} — Société à responsabilité limitée unipersonnelle</dd></div>
            <div class="legal-row"><dt>Capital social</dt><dd>{CO['capital']}</dd></div>
            <div class="legal-row"><dt>Numéro RCCM</dt><dd>{CO['rccm']}</dd></div>
            <div class="legal-row"><dt>Date d'immatriculation</dt><dd>{CO['imm']} — Tribunal de Commerce d'Abidjan</dd></div>
            <div class="legal-row"><dt>Numéro de compte contribuable</dt><dd>{CO['ncc']}</dd></div>
            <div class="legal-row"><dt>Siège social</dt><dd>{CO['siege']}</dd></div>
            <div class="legal-row"><dt>Adresse de correspondance</dt><dd>{CO['addr']}</dd></div>
            <div class="legal-row"><dt>Gérant</dt><dd>{CO['gerant']}</dd></div>
            <div class="legal-row"><dt>Objet social</dt><dd>Toutes opérations de transport et de logistique ; transport poids lourd et léger de marchandises, en Côte d'Ivoire et à l'étranger.</dd></div>
          </dl>
        </div>
        <p class="form-note" style="margin-top:12px">Informations extraites du registre du commerce. Vérifiables auprès du greffe du Tribunal de Commerce d'Abidjan.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section-head center" data-anim="up">
      <span class="eyebrow">Nos valeurs</span>
      <h2>Quatre principes qui tiennent nos engagements</h2>
      <p class="lead" style="margin-inline:auto">Dans le transport, la confiance se construit par la répétition. Voici ce que nous répétons.</p>
    </div>
    <div class="grid grid-4">
      <article class="card" data-anim="up"><div class="icon-box">{I['clock']}</div><h3>Ponctualité</h3><p>Un horaire annoncé est un engagement. En cas d'aléa, l'information circule avant que le client ne la demande.</p></article>
      <article class="card" data-anim="up" data-delay="80"><div class="icon-box">{I['shield']}</div><h3>Sécurité</h3><p>Contrôle avant départ, arrimage vérifié, chauffeurs formés. La marchandise arrive dans l'état où elle est partie.</p></article>
      <article class="card" data-anim="up" data-delay="160"><div class="icon-box">{I['doc']}</div><h3>Transparence</h3><p>Un devis lisible, sans coût caché, et une documentation complète pour chaque expédition.</p></article>
      <article class="card" data-anim="up" data-delay="240"><div class="icon-box">{I['users']}</div><h3>Proximité</h3><p>Un interlocuteur identifié, joignable, qui connaît vos sites, vos horaires et vos contraintes.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center" data-anim="up">
      <span class="eyebrow">En résumé</span>
      <h2>La société en quelques repères</h2>
    </div>
    <div class="stats">
      <div class="stat" data-anim="up"><b data-count="2016" data-plain>0</b><span>Année d'immatriculation au RCCM</span></div>
      <div class="stat" data-anim="up" data-delay="80"><b data-count="100" data-suffix=" M">0</b><span>Capital social en F CFA</span></div>
      <div class="stat" data-anim="up" data-delay="160"><b data-count="5">0</b><span>Prestations couvertes</span></div>
      <div class="stat" data-anim="up" data-delay="240"><b data-count="4">0</b><span>Pays desservis depuis Abidjan</span></div>
    </div>
  </div>
</section>

{cta("Envie de travailler avec nous ?", "Que vous soyez chargeur, industriel ou distributeur, nous sommes disponibles pour étudier vos flux et construire une offre adaptée.", 'benne')}
""")

# ---------------------------------------------------------------- CONTACT
pages['contact.html'] = dict(
    title=f"Contact &amp; devis — {CO['name']}",
    desc="Demandez un devis de transport ou de logistique. Bureau à Abidjan Riviera Saint-Bernard Attoban. Téléphone, e-mail et formulaire de demande.",
    body=pagehead("Parlons de votre prochain chargement",
                  "Un devis chiffré sous 24 à 48 heures ouvrées. Décrivez votre besoin, nous nous occupons du reste.",
                  "Contact", 'partenaire') + f"""
<section class="section">
  <div class="wrap">
    <div class="grid grid-2" style="gap:clamp(32px,4.5vw,60px);align-items:start">

      <div data-anim="left">
        <span class="eyebrow">Demande de devis</span>
        <h2>Dites-nous ce qu'il y a à transporter</h2>
        <p class="lead" style="margin-top:16px;margin-bottom:26px">Plus votre description est précise, plus notre chiffrage sera juste. Les champs marqués d'un astérisque sont nécessaires pour vous répondre.</p>

        <div class="form-wrap">
          <form class="form" id="devis-form" novalidate>
            <div class="form-row">
              <div class="field">
                <label for="nom">Nom / Société <span>*</span></label>
                <input type="text" id="nom" name="nom" placeholder="Ex. Société ivoirienne de négoce" required>
              </div>
              <div class="field">
                <label for="tel">Téléphone <span>*</span></label>
                <input type="tel" id="tel" name="tel" placeholder="+225 ..." required>
              </div>
            </div>
            <div class="field">
              <label for="email">Adresse e-mail <span>*</span></label>
              <input type="email" id="email" name="email" placeholder="contact@votre-societe.ci" required>
            </div>
            <div class="field">
              <label for="service">Prestation souhaitée</label>
              <select id="service" name="service">
                <option>Transport poids lourd</option>
                <option>Vente de véhicule</option>
                <option>Location de véhicule (avec ou sans chauffeur)</option>
                <option>Transport VTC / mise à disposition</option>
                <option>Transport international / corridor</option>
                <option>Transport léger &amp; distribution</option>
                <option>Autre / je ne sais pas encore</option>
              </select>
            </div>
            <div class="form-row">
              <div class="field">
                <label for="depart">Lieu d'enlèvement</label>
                <input type="text" id="depart" name="depart" placeholder="Ex. Port d'Abidjan, Vridi">
              </div>
              <div class="field">
                <label for="arrivee">Lieu de livraison</label>
                <input type="text" id="arrivee" name="arrivee" placeholder="Ex. Bouaké, zone industrielle">
              </div>
            </div>
            <div class="field">
              <label for="nature">Nature et volume du fret</label>
              <input type="text" id="nature" name="nature" placeholder="Ex. 2 conteneurs 40' — 24 tonnes">
            </div>
            <div class="field">
              <label for="message">Précisions utiles</label>
              <textarea id="message" name="message" placeholder="Dates souhaitées, contraintes d'accès, horaires de réception, fréquence des expéditions..."></textarea>
            </div>
            <div class="form-status" role="status"></div>
            <div class="btn-row">
              <button class="btn" type="submit">Envoyer ma demande {ARROW}</button>
              <a class="btn btn--ghost" href="tel:{TEL1}">Appeler directement</a>
            </div>
            <p class="form-note">En envoyant ce formulaire, votre messagerie s'ouvre avec un message pré-rempli à destination de {CO['mail']}. Vos informations ne sont utilisées que pour l'établissement du devis.</p>
          </form>
        </div>
      </div>

      <div data-anim="right" data-delay="110">
        <div class="dark" style="border-radius:var(--radius-lg);padding:clamp(28px,3.6vw,42px)">
          <div style="position:relative;z-index:2">
            <span class="eyebrow eyebrow--light">Coordonnées</span>
            <h2 style="font-size:clamp(1.45rem,2.3vw,1.85rem)">Nous joindre directement</h2>
            <div style="margin-top:20px">
              <div class="info-item"><span class="ring">{I['pin']}</span><div><h4>Bureau &amp; correspondance</h4><p>{CO['addr']}</p></div></div>
              <div class="info-item"><span class="ring">{I['ware']}</span><div><h4>Siège social</h4><p>{CO['siege']}</p></div></div>
              <div class="info-item"><span class="ring">{I['phone']}</span><div><h4>Téléphone</h4><p><a href="tel:{TEL1}">{CO['tel1']}</a><br><a href="tel:{TEL2}">{CO['tel2']}</a></p></div></div>
              <div class="info-item"><span class="ring">{I['mail']}</span><div><h4>E-mail</h4><p><a href="mailto:{CO['mail']}">{CO['mail']}</a></p></div></div>
              <div class="info-item"><span class="ring">{I['clock']}</span><div><h4>Horaires d'exploitation</h4><p>Lundi — Vendredi : 07h30 — 18h00<br>Samedi : 08h00 — 13h00<br>Départs longue distance : selon planning</p></div></div>
              <div class="info-item"><span class="ring">{I['doc']}</span><div><h4>Références légales</h4><p>RCCM : {CO['rccm']}<br>NCC : {CO['ncc']}</p></div></div>
            </div>
            <div class="btn-row" style="margin-top:26px">
              <a class="btn" href="https://maps.google.com/?q=Riviera+Saint+Bernard+Attoban+Rue+L23+Abidjan" target="_blank" rel="noopener">Ouvrir dans Google&nbsp;Maps {ARROW}</a>
            </div>
          </div>
        </div>

        <div class="card" style="margin-top:22px">
          <div class="icon-box">{I['clock']}</div>
          <h3>Urgence ou enlèvement le jour même ?</h3>
          <p>Appelez-nous plutôt que d'écrire. Selon la disponibilité de la flotte, nous pouvons positionner un véhicule dans la journée sur le Grand Abidjan.</p>
          <div class="btn-row" style="margin-top:16px"><a class="link-arrow" href="tel:{TEL1}">{CO['tel1']} {ARROW}</a></div>
        </div>
      </div>

    </div>
  </div>
</section>

{MARQUEE}
""")

# ---------------------------------------------------------------- MENTIONS
pages['mentions-legales.html'] = dict(
    title=f"Mentions légales — {CO['name']}",
    desc="Mentions légales du site de THE SOURCE TRANSPORT SARLU, société immatriculée au RCCM d'Abidjan sous le numéro CI-ABJ-03-2016-B12-11942.",
    body=pagehead("Mentions légales",
                  "Informations relatives à l'éditeur du site et aux conditions d'utilisation.",
                  "Mentions légales", 'hero') + f"""
<section class="section">
  <div class="wrap wrap--narrow">
    <div data-anim="up">
      <span class="eyebrow">Éditeur du site</span>
      <h2>Identification de la société</h2>
      <div class="legal-card" style="margin-top:24px">
        <dl>
          <div class="legal-row"><dt>Dénomination sociale</dt><dd>{CO['name']}</dd></div>
          <div class="legal-row"><dt>Forme juridique</dt><dd>{CO['form']}</dd></div>
          <div class="legal-row"><dt>Capital social</dt><dd>{CO['capital']}</dd></div>
          <div class="legal-row"><dt>RCCM</dt><dd>{CO['rccm']}</dd></div>
          <div class="legal-row"><dt>Compte contribuable</dt><dd>{CO['ncc']}</dd></div>
          <div class="legal-row"><dt>Siège social</dt><dd>{CO['siege']}</dd></div>
          <div class="legal-row"><dt>Adresse de correspondance</dt><dd>{CO['addr']}</dd></div>
          <div class="legal-row"><dt>Représentant légal</dt><dd>{CO['gerant']}, gérant</dd></div>
          <div class="legal-row"><dt>Contact</dt><dd>{CO['mail']} — {CO['tel1']}</dd></div>
        </dl>
      </div>
    </div>

    <div data-anim="up" style="margin-top:46px">
      <h2>Propriété intellectuelle</h2>
      <p class="lead" style="margin-top:14px">L'identité visuelle, les textes, les photographies et la vidéo de ce site sont la propriété de {CO['name']}. Les images représentent son parc et ses véhicules. Toute reproduction, représentation ou adaptation, totale ou partielle, sans autorisation écrite préalable est interdite.</p>
    </div>

    <div data-anim="up" style="margin-top:46px">
      <h2>Données personnelles</h2>
      <p class="lead" style="margin-top:14px">Les informations transmises via le formulaire de demande de devis sont utilisées exclusivement pour traiter votre demande et vous adresser une proposition commerciale. Elles ne font l'objet d'aucune cession à des tiers. Vous pouvez demander leur rectification ou leur suppression en écrivant à {CO['mail']}.</p>
    </div>

    <div data-anim="up" style="margin-top:46px">
      <h2>Responsabilité</h2>
      <p class="lead" style="margin-top:14px">Les informations diffusées sur ce site sont fournies à titre indicatif et n'ont pas valeur contractuelle. Seuls le devis accepté et les documents de transport émis engagent {CO['name']}. La société s'efforce de maintenir le site accessible et à jour sans pouvoir le garantir de manière continue.</p>
    </div>

    <div data-anim="up" style="margin-top:46px">
      <h2>Droit applicable</h2>
      <p class="lead" style="margin-top:14px">Le présent site est régi par le droit ivoirien. En cas de litige relatif à son utilisation, compétence est attribuée aux juridictions d'Abidjan, sous réserve des dispositions impératives applicables.</p>
    </div>
  </div>
</section>
""")

# ================================================================ Écriture
for page_active, cfg in pages.items():
    html = head(cfg['title'], cfg['desc']) + header(over=cfg.get('over', False)) + cfg['body'] + footer()
    with io.open(os.path.join(OUT, page_active), 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK', page_active, len(html))
