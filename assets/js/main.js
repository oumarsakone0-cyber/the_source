/* =========================================================
   THE SOURCE TRANSPORT — Interactions & animations
   Sobres, performantes, respectueuses de prefers-reduced-motion
   ========================================================= */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. Header : état "collé" au scroll ---------- */
  var header = document.querySelector('.header');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('is-stuck', y > 24);
    var top = document.querySelector('.totop');
    if (top) top.classList.toggle('is-visible', y > 520);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- 2. Menu mobile ---------- */
  var burger = document.querySelector('.burger');
  var menu = document.querySelector('.mobile-menu');
  function closeMenu() {
    if (!burger || !menu) return;
    burger.classList.remove('is-open');
    menu.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ---------- 3. Révélation au scroll ---------- */
  var animated = document.querySelectorAll('[data-anim]');
  if (reduced || !('IntersectionObserver' in window)) {
    animated.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var d = parseInt(el.getAttribute('data-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, d);
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    animated.forEach(function (el) { io.observe(el); });
  }

  /* ---------- 4. Compteurs animés ---------- */
  function fmt(v, el) {
    return el.getAttribute('data-plain') !== null ? String(v) : v.toLocaleString('fr-FR');
  }

  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var dur = 1500, t0 = null;
    function frame(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = Math.round(target * eased);
      el.textContent = prefix + fmt(val, el) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  var counters = document.querySelectorAll('[data-count]');
  if (reduced || !('IntersectionObserver' in window)) {
    counters.forEach(function (el) {
      el.textContent = (el.getAttribute('data-prefix') || '') +
        fmt(parseFloat(el.getAttribute('data-count')), el) +
        (el.getAttribute('data-suffix') || '');
    });
  } else {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        animateCount(en.target);
        cio.unobserve(en.target);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- 5. Parallaxe légère du hero ---------- */
  var heroBg = document.querySelector('.hero__bg');
  if (heroBg && !reduced) {
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = window.scrollY || 0;
        if (y < window.innerHeight * 1.2) {
          heroBg.style.transform = 'translate3d(0,' + (y * 0.16) + 'px,0) scale(1.04)';
        }
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---------- 6. Accordéon (FAQ) ---------- */
  document.querySelectorAll('.acc__btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.acc__item');
      var panel = item.querySelector('.acc__panel');
      var open = item.classList.contains('is-open');
      // fermeture des autres
      item.parentElement.querySelectorAll('.acc__item.is-open').forEach(function (o) {
        o.classList.remove('is-open');
        o.querySelector('.acc__panel').style.maxHeight = null;
        o.querySelector('.acc__btn').setAttribute('aria-expanded', 'false');
      });
      if (!open) {
        item.classList.add('is-open');
        panel.style.maxHeight = panel.scrollHeight + 'px';
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- 7. Duplication du bandeau défilant ---------- */
  document.querySelectorAll('.marquee__track').forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });

  /* ---------- 8. Formulaire de contact ---------- */
  var form = document.querySelector('#devis-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      var labels = {
        nom: 'Nom / Société', email: 'E-mail', tel: 'Téléphone',
        service: 'Service souhaité', depart: 'Enlèvement', arrivee: 'Livraison',
        nature: 'Nature du fret', message: 'Détails'
      };
      Object.keys(labels).forEach(function (k) {
        var v = (data.get(k) || '').toString().trim();
        if (v) lines.push(labels[k] + ' : ' + v);
      });
      var subject = 'Demande de devis — ' + ((data.get('nom') || 'Site web').toString());
      var body = 'Bonjour,\n\nJe souhaite obtenir un devis pour la prestation suivante :\n\n' +
        lines.join('\n') + '\n\nCordialement,';
      var status = document.querySelector('.form-status');
      if (status) {
        status.classList.add('is-visible');
        status.textContent = 'Votre demande est prête. Votre messagerie va s’ouvrir pour l’envoyer à thesourcetransport@gmail.com — vous pouvez aussi nous appeler au +225 07 77 31 76 44.';
      }
      window.location.href = 'mailto:thesourcetransport@gmail.com?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }

  /* ---------- 8 bis. Vidéo du parc : lecture auto, sans son ---------- */
  document.querySelectorAll('.videoblock__player').forEach(function (fig) {
    var video = fig.querySelector('video');
    var sound = fig.querySelector('.videoblock__sound');
    if (!video) return;

    // certains navigateurs n'autorisent la lecture auto que si muted est posé en JS
    video.muted = true;
    var tryPlay = function () {
      var p = video.play();
      if (p && p.catch) p.catch(function () { /* lecture auto refusée : on n'insiste pas */ });
    };
    tryPlay();

    // on n'anime la vidéo que lorsqu'elle est visible, pour épargner la batterie
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) tryPlay();
          else video.pause();
        });
      }, { threshold: 0.25 }).observe(video);
    }

    if (!sound) return;
    sound.addEventListener('click', function () {
      video.muted = !video.muted;
      fig.classList.toggle('has-sound', !video.muted);
      sound.setAttribute('aria-pressed', String(!video.muted));
      sound.setAttribute('aria-label', video.muted ? 'Activer le son de la vidéo'
                                                   : 'Couper le son de la vidéo');
      if (!video.muted) tryPlay();
    });
  });

  /* ---------- 9. Retour en haut ---------- */
  var toTop = document.querySelector('.totop');
  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    });
  }

  /* ---------- 10. Année courante ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
