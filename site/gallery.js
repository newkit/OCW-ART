// The OCW Build Diary gallery (docs/ART-PROJECT.md §6): the lightbox of a
// day page. Without JavaScript every thumbnail still links to its web copy.
(function () {
  "use strict";
  var data = document.getElementById("items");
  var box = document.getElementById("lightbox");
  if (!data || !box) return;
  var day = JSON.parse(data.textContent);
  var items = day.items;
  var img = box.querySelector("img");
  var media = box.querySelector(".lb-media");
  var cap = box.querySelector(".lb-cap");
  var links = box.querySelector(".lb-links");
  var cur = -1;

  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text) e.textContent = text;
    return e;
  }

  function show(i) {
    if (i < 0 || i >= items.length) return;
    cur = i;
    var it = items[i];
    var video = it.k === "video";
    box.classList.toggle("video", video);
    img.src = it.w || it.t || "";
    img.alt = it.c;
    cap.textContent = "";
    cap.appendChild(el("time", {}, it.time));
    cap.appendChild(document.createTextNode(" " + it.c + (it.s ? " · " + Math.round(it.s) + " s" : "") +
      "  (" + (i + 1) + " / " + items.length + ")"));
    if (it.n) { cap.appendChild(el("br", {})); cap.appendChild(document.createTextNode(it.n)); }
    links.textContent = "";
    if (video && day.video) {
      media.href = day.download + encodeURIComponent(day.video);
      links.appendChild(el("a", {"class": "btn", href: media.href}, "▶ Day video"));
    } else {
      media.href = it.w || it.t || "#";
    }
    if (day.zip) {
      links.appendChild(el("a", {"class": "btn", href: day.download + encodeURIComponent(day.zip)},
        "⇩ Full size: day zip"));
      links.appendChild(el("small", {}, (video ? "The clip " : "The file ") + day.day + "/" + it.f +
        " is in the day zip."));
    } else {
      links.appendChild(el("small", {}, "Full size: " + it.f + " goes into the day zip when the day is published (" +
        "release build-history)."));
    }
    box.hidden = false;
    if (location.hash !== "#" + (i + 1)) history.replaceState(null, "", "#" + (i + 1));
    [i - 1, i + 1].forEach(function (j) { // preload the neighbours
      if (j >= 0 && j < items.length && (items[j].w || items[j].t)) new Image().src = items[j].w || items[j].t;
    });
  }

  function close() {
    box.hidden = true;
    img.removeAttribute("src");
    cur = -1;
    history.replaceState(null, "", location.pathname);
  }

  document.querySelector(".grid").addEventListener("click", function (e) {
    var a = e.target.closest("a[data-i]");
    if (!a || e.ctrlKey || e.metaKey || e.shiftKey) return;
    e.preventDefault();
    show(parseInt(a.getAttribute("data-i"), 10));
  });
  box.querySelector(".lb-prev").addEventListener("click", function () { show(cur - 1); });
  box.querySelector(".lb-next").addEventListener("click", function () { show(cur + 1); });
  box.querySelector(".lb-close").addEventListener("click", close);
  box.addEventListener("click", function (e) { if (e.target === box) close(); });
  document.addEventListener("keydown", function (e) {
    if (box.hidden) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowLeft") show(cur - 1);
    else if (e.key === "ArrowRight") show(cur + 1);
  });
  var x0 = null; // swipe on phones
  box.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, {passive: true});
  box.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1));
    x0 = null;
  });
  var m = /^#(\d+)$/.exec(location.hash); // deep link: #N opens picture N
  if (m) show(parseInt(m[1], 10) - 1);
})();
