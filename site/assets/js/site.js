/* Coolmax Wholesale: language choice, geo banner, product gallery, sizing calculator, inquiry form. No dependencies. */
(function () {
  var body = document.body;
  var lang = body.getAttribute('data-lang');
  var WA = body.getAttribute('data-wa');
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  // Remember an explicit language choice so auto-detection never overrides it.
  document.querySelectorAll('[data-setlang]').forEach(function (a) {
    a.addEventListener('click', function () { store.set('cm_lang', a.getAttribute('data-setlang')); });
  });

  // Arabic page reached by auto-detection: offer English once (useful for English-speaking expats in the Gulf).
  var banner = document.getElementById('geo-banner');
  if (banner && lang === 'ar' && !store.get('cm_lang') && !store.get('cm_banner')) {
    banner.hidden = false;
    banner.querySelector('.geo-x').addEventListener('click', function () { banner.hidden = true; store.set('cm_banner', '1'); });
  }

  // Header turns solid once the page scrolls past the dark hero
  var header = document.querySelector('.site-header');
  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Range list: hovering or focusing an item previews its picture and description
  var svcImg = document.querySelector('.svc-media img');
  var svcCap = document.querySelector('.svc-media figcaption');
  document.querySelectorAll('.svc-list a').forEach(function (a, i) {
    if (i === 0) a.classList.add('on');
    function show() {
      if (svcImg.getAttribute('src') !== a.getAttribute('data-img')) { svcImg.src = a.getAttribute('data-img'); svcImg.alt = a.querySelector('.svc-t').textContent; }
      svcCap.textContent = a.getAttribute('data-desc');
      document.querySelectorAll('.svc-list a').forEach(function (x) { x.classList.toggle('on', x === a); });
    }
    a.addEventListener('mouseenter', show);
    a.addEventListener('focus', show);
  });

  // Product gallery thumbnails
  var main = document.querySelector('.pmain img');
  document.querySelectorAll('.thumbs button').forEach(function (b, i) {
    if (i === 0) b.setAttribute('aria-pressed', 'true');
    b.addEventListener('click', function () {
      main.src = b.getAttribute('data-src');
      main.removeAttribute('srcset');
      document.querySelectorAll('.thumbs button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    });
  });

  // Sizing calculator: units = area × height × air changes per hour ÷ airflow
  document.querySelectorAll('.calc').forEach(function (calc) {
    var models = JSON.parse(calc.getAttribute('data-models'));
    var units = calc.querySelector('[data-units]').getAttribute('data-units');
    var nf = new Intl.NumberFormat('en-US');
    function run() {
      var area = parseFloat(calc.querySelector('[name=area]').value) || 0;
      var h = parseFloat(calc.querySelector('[name=height]').value) || 0;
      var achSel = calc.querySelector('[name=ach]');
      var need = Math.round(area * h * parseFloat(achSel.value));
      calc.querySelector('[data-out=need]').textContent = nf.format(need) + ' m³/h';
      var rows = models.map(function (m) {
        var n = need > 0 ? Math.max(1, Math.ceil(need / m.airflow)) : 0;
        return '<tr><td><a href="' + m.href + '">' + m.name + '</a></td><td dir="ltr">' + nf.format(m.airflow) + '</td><td>' + n + '</td></tr>';
      });
      calc.querySelector('[data-out=rows]').innerHTML = rows.join('');
      var msg = area + ' m², h ' + h + ' m, ' + achSel.options[achSel.selectedIndex].text + ' → ' + nf.format(need) + ' m³/h';
      var send = calc.querySelector('[data-out=send]');
      send.href = calc.getAttribute('data-contact') + '?message=' + encodeURIComponent(msg);
    }
    calc.addEventListener('input', run);
    run();
    void units;
  });

  // Prefill the inquiry form from ?model=&brand=&message=
  var form = document.querySelector('form.inq');
  if (!form) return;
  var params = new URLSearchParams(location.search);
  ['model', 'message'].forEach(function (k) { if (params.get(k)) form.elements[k].value = params.get(k); });
  var b = (params.get('brand') || '').toLowerCase();
  if (b) Array.prototype.forEach.call(form.elements.brand.options, function (o) { if (o.value.toLowerCase() === b) o.selected = true; });
  try {
    var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var map = { 'Asia/Karachi': 'Pakistan', 'Asia/Riyadh': 'Saudi Arabia', 'Asia/Dubai': 'UAE', 'Asia/Qatar': 'Qatar', 'Asia/Kuwait': 'Kuwait', 'Asia/Muscat': 'Oman', 'Asia/Bahrain': 'Bahrain', 'Asia/Baghdad': 'Iraq' };
    if (map[tz]) form.elements.country.value = map[tz];
  } catch (e) {}

  var status = form.querySelector('.form-status');
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var bad = Array.prototype.filter.call(form.querySelectorAll('[required]'), function (el) { return !el.value.trim(); });
    if (bad.length) { bad[0].focus(); bad[0].reportValidity && bad[0].reportValidity(); return; }
    var endpoint = body.getAttribute('data-form');
    var data = new FormData(form);
    if (endpoint) {
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw 0; status.className = 'form-status ok'; status.textContent = status.getAttribute('data-ok'); form.reset(); })
        .catch(function () { status.className = 'form-status err'; status.textContent = status.getAttribute('data-err'); });
      return;
    }
    var labels = {};
    form.querySelectorAll('label').forEach(function (l) {
      var el = l.querySelector('input,select,textarea');
      if (el) labels[el.name] = l.firstChild.textContent.replace('*', '').trim();
    });
    var lines = [];
    data.forEach(function (v, k) { if (v && labels[k]) lines.push(labels[k] + ': ' + v); });
    window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    status.className = 'form-status ok';
    status.textContent = status.getAttribute('data-ok');
  });
})();
