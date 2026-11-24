# Pages principales, en français et en anglais côte à côte : t("texte français", "English text").
# Les textes reprennent ceux de l'ancien site (services, FAQ, formules), réécrits sans les doublons.
import re
from html import escape
from kit import (SITE, tr, url, icon, illu, chip, btn, more, todo, fcard, photo, sticker, ticks, head, faq_list, crumbs,
                 crumbs_ld, contact_buttons, org_ld, website_ld, service_ld, social_links, OTHER)
import faq
import photos
import quartiers as Q


def services(L):
    t = tr(L)
    return [
        ("green-s", "calendrier", t("Gestion des réservations", "Reservations"),
         t("Nous prenons en charge tout le processus de réservation, de la mise en ligne de l'annonce à la confirmation, avec des tarifs ajustés pour garantir la rentabilité.",
           "We handle the whole booking process, from publishing the listing to confirming each stay, with prices adjusted to keep your property profitable."), "voyageurs"),
        ("coral-s", "porte", t("Accueil des voyageurs", "Guest welcome"),
         t("Un accueil chaleureux, une remise de clés sécurisée et une présentation complète du logement, pour que les voyageurs s'y sentent chez eux dès le premier instant.",
           "A warm welcome, a secure key handover and a full tour of the home, so guests feel at home from the first minute."), "voyageurs"),
        ("blue-s", "menage", t("Ménage et entretien", "Cleaning and upkeep"),
         t("Après chaque séjour, nos équipes rendent le logement impeccable, et des vérifications régulières le gardent en parfait état.",
           "After every stay, our teams leave the home spotless, and regular checks keep it in perfect condition."), "logement"),
        ("sand-s", "linge", t("Blanchisserie du linge", "Linen service"),
         t("Draps, serviettes et linge de maison sont lavés et repassés à chaque séjour, prêts pour les voyageurs suivants.",
           "Sheets, towels and household linen are washed and ironed for every stay, ready for the next guests."), "logement"),
        ("green-s", "outils", t("Maintenance et réparation", "Maintenance and repairs"),
         t("Une ampoule à changer ou un dépannage plus complexe : notre équipe technique intervient rapidement pour la pérennité de votre bien.",
           "A bulb to change or a more complex repair: our technical team steps in quickly to keep your property in good shape."), "logement"),
        ("coral-s", "casque", t("Assistance aux voyageurs", "Guest support"),
         t("Une question, un imprévu ? Notre assistance répond aux voyageurs 24h/24 et 7j/7, des conseils locaux à l'aide d'urgence.",
           "A question or a problem? Our support team answers guests 24/7, from local tips to emergency help."), "voyageurs"),
        ("blue-s", "balance", t("Gestion des litiges", "Dispute handling"),
         t("En cas de désaccord, nous servons de médiateur et protégeons les intérêts du propriétaire, en cherchant un règlement équitable.",
           "If a disagreement arises, we mediate and protect the owner's interests while seeking a fair settlement."), "logement"),
        ("sand-s", "carte", t("Conciergerie à la carte", "À la carte"),
         t("Gestion complète, ou seulement le ménage, la maintenance ou les réservations : vous choisissez les services qui vous conviennent.",
           "Full management, or only cleaning, maintenance or bookings: you choose the services that suit you."), "formules"),
    ]


def service_cards(L, items, link=True):
    t = tr(L)
    out = []
    for tone, ic, h, p, target in items:
        m = more(url(target, L), t("En savoir plus", "Learn more")) if link else ""
        out.append(f'<div class="card {tone} reveal">{illu(ic)}<h3>{h}</h3><p>{p}</p>{m}</div>')
    return "".join(out)


def marquee(L):
    names = [a[L]["name"] for a in Q.AREAS] + [a[L]["name"] for a in Q.TOWNS] + ["Versailles", "Vincennes", "Boulogne-Billancourt",
                                                                                  "Neuilly-sur-Seine", "Levallois-Perret", "Rueil-Malmaison", "Sucy-en-Brie"]
    row = "".join(f"<span>{n}</span>" for n in names)
    # La liste est doublée pour que le défilement boucle sans saut ; la copie est masquée aux lecteurs d'écran.
    return f'<div class="marquee"><div aria-label="{tr(L)("Secteurs", "Areas")}">{row}</div><div aria-hidden="true">{row}</div></div>'


def steps(L):
    t = tr(L)
    items = [
        ("green-s", "telephone", t("Vous nous présentez votre logement", "You tell us about your home"),
         t("Par téléphone, sur WhatsApp ou par e-mail : adresse, nombre de couchages, dates où vous souhaitez le louer.",
           "By phone, WhatsApp or email: address, number of beds, the dates you want to let it.")),
        ("coral-s", "graphique", t("Nous estimons vos revenus", "We estimate your income"),
         t("Après une évaluation détaillée du logement et de vos objectifs, nous vous remettons une projection réaliste et transparente.",
           "After a detailed assessment of the home and your goals, we give you a realistic, transparent projection.")),
        ("blue-s", "appareil", t("Nous préparons l'annonce", "We prepare the listing"),
         t("Photos prises par nos soins, annonce en français et en anglais, publiée sur Airbnb, Booking.com, Vrbo et Expedia.",
           "Photos taken by us, a listing in French and English, published on Airbnb, Booking.com, Vrbo and Expedia.")),
        ("sand-s", "cles", t("Nous gérons tout", "We handle everything"),
         t("Réservations, voyageurs, clés, ménage et entretien. Vous gardez l'accès à votre compte Airbnb.",
           "Bookings, guests, keys, cleaning and upkeep. You keep access to your Airbnb account.")),
    ]
    return '<ol class="steps">' + "".join(f'<li class="step {c} reveal">{illu(i)}<h3>{h}</h3><p>{p}</p></li>' for c, i, h, p in items) + "</ol>"


def phead(L, trail, label, h1, lead, visual="", actions=True):
    t = tr(L)
    acts = ""
    if actions:
        acts = (f'<div class="cta-row">{btn(url("contact", L), t("Parlez-nous de votre projet", "Tell us about your property"))}'
                f'{btn(url("formules", L), t("Voir nos formules", "See our plans"), "ghost")}</div>')
    solo = "" if visual else " solo"
    vis = f"<div>{visual}</div>" if visual else ""
    return f"""<section class="phead">
  <div class="phead-panel panel">
    <div class="wrap phead-grid{solo}">
      <div>{crumbs(L, trail)}{chip(label)}<h1>{h1}</h1><p class="lead">{lead}</p>{acts}</div>
      {vis}
    </div>
  </div>
</section>"""


def faq_ld(items):
    def plain(s):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in items]}


# ── Accueil ─────────────────────────────────────────────────────────────────
def home(L):
    t = tr(L)
    s = SITE
    rail = "".join(Q.area_card(a, L) for a in Q.AREAS)
    body = f"""<section class="hero">
  <div class="hero-panel panel">
    <div class="wrap hero-grid">
      <div class="hero-text">
        {chip(t("Conciergerie Airbnb · Paris et Île-de-France", "Airbnb management · Paris and Île-de-France"))}
        <h1>{t("Votre bien loué sur Airbnb, <mark>sans le moindre tracas</mark>", "Your property on Airbnb, <mark>without the hassle</mark>")}</h1>
        <p class="lead">{t("Nous gérons la location saisonnière de votre résidence secondaire ou de votre bien locatif, à Paris et en Île-de-France : annonce, voyageurs, clés, ménage, linge et entretien. Vous choisissez entre un revenu garanti et un revenu réel.",
                          "We run short-term rentals of second homes and buy-to-let apartments in Paris and Île-de-France: listing, guests, keys, cleaning, linen and upkeep. You choose between a guaranteed income and your actual income.")}</p>
        <div class="cta-row">{btn(url("contact", L), t("Parlez-nous de votre projet", "Tell us about your property"))}{btn(url("formules", L), t("Voir nos formules", "See our plans"), "ghost")}</div>
      </div>
      <div class="hero-visual">
        <figure class="hero-photo">{photo("accueil-hero", t("Deux voyageurs accueillis avec leurs valises devant la porte d'un immeuble parisien", "Two guests with suitcases welcomed at the door of a Paris apartment building"), sizes="(max-width: 900px) 100vw, 40vw", lazy=False)}</figure>
        {fcard(t("Revenu garanti", "Guaranteed income"), "t-green", t("Versé que le logement soit loué ou non.", "Paid whether or not the home is booked."), "fc-1", "chart")}
        {fcard(t("Voyageurs", "Guests"), "t-coral", t("Pièce d'identité vérifiée avant chaque séjour.", "ID checked before every stay."), "fc-2", "id")}
        {fcard(t("Ménage", "Cleaning"), "t-blue", t("Après chaque départ, linge compris.", "After every check-out, linen included."), "fc-3", "sparkle")}
        {sticker("cles")}
      </div>
    </div>
  </div>
  <div class="band" role="region" aria-label="{t("Secteurs où nous gérons des logements", "Areas where we manage homes")}">{marquee(L)}</div>
</section>

<section class="sec"><div class="wrap">
  <div class="stats">
    <div class="stat reveal"><b>{t("15 %", "15%")}</b><span>{t("de marge moyenne avec le contrat au revenu garanti", "average margin on the guaranteed-income contract")}</span></div>
    <div class="stat reveal"><b>{t("18 à 25 %", "18–25%")}</b><span>{t("de commission avec le contrat au revenu réel, selon la durée de location", "commission on the actual-income contract, depending on rental length")}</span></div>
    <div class="stat reveal"><b>{t("24h/24", "24/7")}</b><span>{t("d'assistance pour les voyageurs, 7 jours sur 7", "guest support, every day of the week")}</span></div>
  </div>
</div></section>

<section class="sec tight" aria-labelledby="services-t"><div class="wrap">
  {head(t("Nos services", "Our services"), t("Une gestion complète, <mark>pour un rendement sans tracas</mark>", "Full management, <mark>for a hassle-free return</mark>"),
        t("De la mise en ligne de l'annonce à la blanchisserie, chaque étape de la location est prise en charge par notre équipe. Vous pouvez aussi ne choisir que certains services.",
          "From publishing the listing to washing the linen, our team handles every step of the rental. You can also pick only the services you need."), center=True, hid="services-t")}
  <div class="cards">{service_cards(L, services(L))}</div>
</div></section>

<section class="sec split"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("accueil-voyageurs", t("Une famille de voyageurs accueillie dans l'entrée d'un appartement parisien", "A family of travellers welcomed in the hallway of a Paris apartment"))}</figure>
    {fcard(t("Identité", "Identity"), "t-green", t("Pièce d'identité vérifiée", "ID checked"), "a", "id")}
    {fcard(t("Profil", "Profile"), "t-coral", t("Commentaires positifs et profil vérifié", "Positive reviews and verified profile"), "b", "star")}
    {fcard(t("Familles", "Families"), "t-blue", t("Réservations des familles facilitées", "Family bookings made easy"), "c", "family")}
    {sticker("identite", cls="low")}
  </div>
  <div class="split-text reveal">
    {chip(t("Gestion des voyageurs", "Guest management"))}
    <h2>{t("Des voyageurs choisis avec soin", "Guests chosen with care")}</h2>
    <p>{t("Une équipe se consacre uniquement à la sélection, à la communication et à la gestion des voyageurs. Nous n'acceptons pas n'importe qui dans votre logement.",
          "A dedicated team handles only guest screening, communication and management. We don't let just anyone into your home.")}</p>
    {ticks([t("Âge et raison du séjour demandés, en insistant pour les voyageurs sans commentaire", "Age and reason for the stay requested, insisting with guests who have no reviews"),
            t("Priorité aux profils vérifiés et aux commentaires positifs", "Priority to verified profiles and positive reviews"),
            t("Pièce d'identité obligatoire pour réserver", "ID required to book"),
            t("Assistance 24h/24 pendant tout le séjour", "24/7 support throughout the stay")])}
    {btn(url("voyageurs", L), t("La gestion des voyageurs", "Guest management"))}
  </div>
</div></section>

<section class="sec split flip"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("accueil-logement", t("Lit fait avec du linge blanc propre dans une chambre parisienne lumineuse", "A bed made with crisp white linen in a bright Paris bedroom"))}</figure>
    {fcard(t("Réapprovisionnement", "Restocking"), "t-blue", t("Draps, serviettes et articles de toilette remis en place.", "Sheets, towels and toiletries put back in place."), "a", "linen")}
    {fcard(t("Entretien", "Upkeep"), "t-sand", t("Vérifications régulières des équipements.", "Regular checks of all equipment."), "b", "wrench")}
    {sticker("linge")}
  </div>
  <div class="split-text reveal">
    {chip(t("Gestion du logement", "Property management"))}
    <h2>{t("Votre bien entre de bonnes mains", "Your property in good hands")}</h2>
    <p>{t("Ménage après chaque départ, linge, réapprovisionnement, petits travaux et décoration : nous gardons votre logement prêt à accueillir, séjour après séjour.",
          "Cleaning after every check-out, linen, restocking, small repairs and decoration: we keep your home ready for guests, stay after stay.")}</p>
    {ticks([t("Ménage en profondeur après chaque séjour", "Deep clean after every stay"),
            t("Linge lavé et repassé, consommables remplacés", "Linen washed and ironed, consumables restocked"),
            t("Maintenance, petits travaux et réaménagement", "Maintenance, small works and refurbishment"),
            t("Décoration pour des photos qui donnent envie de réserver", "Decoration for photos that make guests want to book")])}
    {btn(url("logement", L), t("La gestion du logement", "Property management"))}
  </div>
</div></section>

<section class="sec tight" aria-labelledby="plans-t"><div class="wrap">
  {head(t("Nos formules", "Our plans"), t("Revenu garanti ou revenu réel : <mark>à vous de choisir</mark>", "Guaranteed or actual income: <mark>your choice</mark>"),
        t("Un revenu fixé à l'avance, ou les revenus réels du logement moins notre commission : dans les deux cas, nous gérons tout.",
          "An income agreed in advance, or the home's actual income minus our commission: either way, we handle everything."), center=True, hid="plans-t")}
  {Q.plans_strip(L)}
</div></section>

<section class="sec blue-band" aria-labelledby="areas-t" data-rail>
  <div class="wrap">
    <div class="rail-head">
      {head("Paris", t("Les quartiers que les voyageurs viennent chercher", "The neighbourhoods guests come looking for"),
            t("Nous gérons des logements dans tout Paris et en Île-de-France. Voici ce qui attire les voyageurs dans chaque quartier.",
              "We manage homes all over Paris and Île-de-France. Here is what draws guests to each neighbourhood."), hid="areas-t")}
      {illu("tour-eiffel")}
      <div class="rail-btns"><button class="prev" type="button" aria-label="{t("Quartiers précédents", "Previous")}">{icon("arrow")}</button><button class="next" type="button" aria-label="{t("Quartiers suivants", "Next")}">{icon("arrow")}</button></div>
    </div>
    <div class="rail">{rail}</div>
    <div class="rail-foot">{btn(url("paris", L), t("Conciergerie Airbnb à Paris : tous les quartiers", "Airbnb management in Paris: all neighbourhoods"))}</div>
  </div>
</section>

<section class="sec" aria-labelledby="steps-t"><div class="wrap">
  {head(t("Comment ça marche", "How it works"), t("De votre premier appel à vos premiers voyageurs", "From your first call to your first guests"), center=True, hid="steps-t")}
  {steps(L)}
</div></section>

<section class="sec tight" aria-labelledby="faq-t"><div class="wrap faq-wrap">
  <div class="faq-side">
    {head("FAQ", t("Les questions des propriétaires", "Owners' questions"), hid="faq-t")}
    <p class="intro">{t("Les réponses à ce qu'on nous demande avant de nous confier un logement.", "Answers to what owners ask us before handing over their keys.")}</p>
    <div class="split-visual">
      <figure class="ph">{photo("accueil-faq", t("Une propriétaire écrit un message depuis son salon", "An owner sending a message from her living room"))}</figure>
      {fcard("WhatsApp", "t-green", t("Une autre question ? Écrivez-nous.", "Another question? Message us."), "b", "chat")}
    </div>
  </div>
  <div>{faq_list(faq.pick(L, ["tarifs", "revenu", "cles", "selection", "legislation"]))}
    <p style="margin-top:28px">{btn(url("faq", L), t("Toutes les questions", "All questions"), "ghost")}</p></div>
</div></section>

<section class="sec tight"><div class="wrap">
  <div class="travel panel coral-s" style="margin:0">
    {illu("cafe")}
    <div><h2>{t("Vous voyagez à Paris ?", "Travelling to Paris?")}</h2>
      <p>{t("Découvrez les logements EdenFlats disponibles et réservez directement.", "Browse the EdenFlats homes available and book directly.")}</p></div>
    {btn(s["booking"], t("Voir les logements", "See the homes"), ext=True, ico="out")}
  </div>
</div></section>"""
    return {"title": t("Conciergerie Airbnb à Paris et en Île-de-France | EdenFlats", "Airbnb Management in Paris & Île-de-France | EdenFlats"),
            "desc": t("Conciergerie Airbnb à Paris et en Île-de-France : annonce, voyageurs, clés, ménage et entretien de votre résidence secondaire. Revenu garanti ou réel.",
                      "Airbnb management in Paris and Île-de-France for second homes and buy-to-let flats: listing, guests, keys, cleaning. Guaranteed or actual income."),
            "body": body, "ld": [org_ld(L), website_ld(L)], "og_image": "/assets/img/og-image.jpg", "image": "/assets/img/accueil-hero.jpg"}


# ── Gestion des voyageurs ───────────────────────────────────────────────────
def voyageurs(L):
    t = tr(L)
    trail = [(t("Gestion des voyageurs", "Guest management"), url("voyageurs", L))]
    visual = f"""<div class="hero-visual">
        <figure class="hero-photo">{photo("voyageurs-hero", t("Une voyageuse récupère ses clés dans une boîte à clés à l'entrée d'un appartement", "A guest collecting her keys from a key box at an apartment door"), sizes="(max-width: 900px) 100vw, 45vw", lazy=False)}</figure>
        {fcard(t("Accueil", "Welcome"), "t-coral", t("Remise des clés en main propre ou à distance.", "Keys handed over in person or remotely."), "fc-1", "key")}
        {fcard(t("Assistance", "Support"), "t-green", t("Voyageurs accompagnés 24h/24 et 7j/7.", "Guests supported 24/7."), "fc-3", "headset")}
        {sticker("cles")}
      </div>"""
    four = [
        ("green-s", "langues", t("Mise en ligne de votre annonce", "Publishing your listing"),
         t("Une annonce soignée, publiée sur Airbnb et les grandes plateformes, pour une visibilité optimale.", "A carefully written listing on Airbnb and the main platforms, for the best visibility."), "voyageurs"),
        ("coral-s", "identite", t("Sélection des voyageurs", "Guest screening"),
         t("Misez sur la tranquillité et la sécurité grâce à une sélection rigoureuse des voyageurs.", "Peace of mind and security, thanks to careful guest screening."), "voyageurs"),
        ("blue-s", "cles", t("Remise de clés", "Key handover"),
         t("Chaque échange de clés se fait simplement : en main propre, par un café partenaire ou à distance.", "Every key exchange is simple: in person, via a partner café or remotely."), "voyageurs"),
        ("sand-s", "casque", t("Assistance voyageur", "Guest support"),
         t("Un accueil chaleureux et professionnel, puis une assistance disponible 24h/24 et 7j/7.", "A warm, professional welcome, then support available 24/7."), "voyageurs"),
    ]
    body = phead(L, trail, t("Gestion des voyageurs", "Guest management"),
                 t("Des voyageurs choisis, accueillis et <mark>accompagnés</mark>", "Guests screened, welcomed and <mark>looked after</mark>"),
                 t("Chez EdenFlats, héberger est plus qu'un art de vivre : c'est un savoir-faire, un plaisir et une passion. Nous publions votre annonce, sélectionnons les voyageurs, les accueillons et restons joignables pendant tout leur séjour.",
                   "At EdenFlats, hosting is more than a way of life: it is a skill, a pleasure and a passion. We publish your listing, screen guests, welcome them and stay reachable throughout their stay."),
                 visual) + f"""
<section class="sec"><div class="wrap">
  {head(t("On s'occupe de tout", "We take care of everything"), t("Du premier message au départ des voyageurs", "From the first message to check-out"), center=True)}
  <div class="cards">{service_cards(L, four, link=False)}</div>
</div></section>

<section class="sec tight split"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("voyageurs-annonce", t("Séance photo d'un salon parisien pour une annonce de location", "Photo shoot of a Paris living room for a rental listing"))}</figure>
    {fcard("FR · EN", "t-blue", t("Annonce rédigée en français et en anglais.", "Listing written in French and English."), "a", "globe")}
    {fcard(t("Photos", "Photos"), "t-green", t("Prises par nos soins, sous les meilleurs angles.", "Taken by us, from the best angles."), "b", "camera")}
    {sticker("appareil", cls="low")}
  </div>
  <div class="split-text reveal">
    {chip(t("Mise en ligne", "Listing"))}
    <h2>{t("Une annonce qui donne envie de réserver", "A listing that makes guests want to book")}</h2>
    <p>{t("La première impression est essentielle : nous photographions nous-mêmes votre logement pour en montrer les meilleurs angles, et rédigeons l'annonce en français et en anglais pour toucher une clientèle internationale.",
          "First impressions matter: we photograph your home ourselves to show its best angles, and write the listing in French and English to reach international guests.")}</p>
    {ticks([t("Publication sur Airbnb, Booking.com, Vrbo, Expedia et d'autres plateformes", "Published on Airbnb, Booking.com, Vrbo, Expedia and other platforms"),
            t("Calendriers synchronisés automatiquement, pour éviter les doubles réservations", "Calendars synced automatically, to avoid double bookings"),
            t("Pas de compte Airbnb ? Nous créons l'annonce pour vous", "No Airbnb account? We create the listing for you"),
            t("Déjà hôte ? Vous gardez votre compte, vos commentaires et l'accès à vos réservations", "Already a host? You keep your account, your reviews and access to your bookings")])}
  </div>
</div></section>

<section class="sec split flip"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("voyageurs-selection", t("Deux membres de l'équipe étudient une demande de réservation", "Two team members reviewing a booking request"))}</figure>
    {fcard(t("Accepté", "Accepted"), "t-green", t("Profil vérifié, commentaires positifs, identité contrôlée.", "Verified profile, positive reviews, ID checked."), "a", "check")}
    {fcard(t("Questions", "Questions"), "t-coral", t("Âge et raison du séjour demandés.", "Age and reason for the stay requested."), "b", "users")}
    {sticker("identite", cls="low")}
  </div>
  <div class="split-text reveal">
    {chip(t("Sélection des voyageurs", "Guest screening"))}
    <h2>{t("Pourquoi sélectionner les voyageurs ?", "Why screen guests?")}</h2>
    <p>{t("Notre expérience nous a permis de mettre au point des mécanismes pour distinguer les bons voyageurs de ceux qui pourraient poser problème. Nous vérifions les profils, recueillons les évaluations et dialoguons avec les voyageurs pour comprendre l'objet de leur séjour : vos intérêts sont protégés, et chaque réservation se passe bien pour tout le monde.",
          "Experience has taught us how to tell good guests from those who could cause problems. We check profiles, read reviews and talk with guests to understand the purpose of their stay: your interests are protected, and every booking goes well for everyone.")}</p>
    {ticks([t("Âge et raison de la réservation demandés, en insistant pour les voyageurs sans commentaire", "Age and reason for the booking requested, insisting with guests who have no reviews"),
            t("Priorité aux voyageurs avec des commentaires positifs et des profils vérifiés", "Priority to guests with positive reviews and verified profiles"),
            t("Réservations des familles facilitées", "Family bookings made easy"),
            t("Pièce d'identité obligatoire : l'identité de chaque voyageur est vérifiée", "ID required: every guest's identity is checked")])}
  </div>
</div></section>

<section class="sec tight"><div class="wrap">
  {head(t("Accueil et remise de clés", "Welcome and key handover"), t("Des arrivées simples, pour vous comme pour les voyageurs", "Easy arrivals, for you and your guests"), center=True)}
  <div class="cards two">
    <div class="card coral-s reveal">{illu("porte")}<h3>{t("L'accueil en personne", "A personal welcome")}</h3>
      <p>{t("À leur arrivée, notre équipe accueille les voyageurs, les guide dans le logement et répond à leurs questions, pour leur confort et leur sécurité dès le premier instant.",
            "When guests arrive, our team welcomes them, shows them around and answers their questions, for their comfort and safety from the first minute.")}</p>
      <p>{t("Il nous faut deux jeux de clés : la veille de la location, vous déposez le premier dans l'un de nos cafés partenaires ; le second reste dans le logement, sur le plan de travail de la cuisine. Pendant la location, un jeu est confié à notre prestataire de ménage, l'autre aux voyageurs.",
            "We need two sets of keys: the day before the rental, you drop the first at one of our partner cafés; the second stays in the home, on the kitchen worktop. During the rental, one set goes to our cleaning provider and the other to the guests.")}</p></div>
    <div class="card green-s reveal">{illu("serrure")}<h3>{t("Les systèmes Smart Key", "Smart Key systems")}</h3>
      <p>{t("Pour des arrivées simplifiées, nous pouvons aussi ouvrir à distance, avec des serrures connectées (SmartKey) ou des boîtes à clés (LockBox).",
            "For easier arrivals, we can also open remotely, with smart locks (SmartKey) or key boxes (LockBox).")}</p>
      <p>{t("L'utilisation de ces systèmes dépend de vous : nous l'adaptons à votre logement et à votre immeuble.",
            "Whether to use them is up to you: we adapt to your home and your building.")}</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cards two">
    <div class="card blue-s reveal">{illu("casque")}<h3>{t("Assistance voyageurs, 24h/24 et 7j/7", "Guest support, 24/7")}</h3>
      <p>{t("Notre objectif : un revenu et une tranquillité totale pour vous, et une expérience exceptionnelle pour chaque voyageur. Nous répondons à tous leurs besoins, des conseils locaux à l'aide d'urgence, et restons disponibles à chaque étape de leur séjour.",
            "Our goal: income and complete peace of mind for you, and an exceptional stay for every guest. We answer all their needs, from local tips to emergency help, and stay available at every step of their stay.")}</p></div>
    <div class="card sand-s reveal">{illu("maison")}<h3>{t("Et vous ? L'assistance propriétaire", "And you? Owner support")}</h3>
      <p>{t("Posséder et gérer un bien peut être complexe : questions, préoccupations ou attentes particulières, notre équipe vous accompagne tout au long de la collaboration.",
            "Owning and running a property can be complex: whatever your questions, concerns or expectations, our team supports you throughout.")}</p>
      <p>{t("Vous gardez un accès complet à votre compte Airbnb : réservations, commentaires et revenus, en temps réel.",
            "You keep full access to your Airbnb account: bookings, reviews and income, in real time.")}</p></div>
  </div>
</div></section>

{Q.where(L)}
<section class="sec tight"><div class="wrap faq-wrap">
  <div>{head("FAQ", t("Questions sur les voyageurs", "Questions about guests"))}</div>
  <div>{faq_list(faq.pick(L, ["selection", "reservations", "acces-compte", "annulation", "cles"]))}</div>
</div></section>"""
    title = t("Gestion des voyageurs Airbnb à Paris | EdenFlats", "Airbnb Guest Management in Paris | EdenFlats")
    desc = t("Annonce Airbnb en français et en anglais, sélection des voyageurs, accueil et remise des clés, assistance 24h/24 : la gestion des voyageurs à Paris.",
             "Airbnb listing in French and English, guest screening, check-in and key handover, 24/7 support: EdenFlats guest management in Paris and Île-de-France.")
    return {"title": title, "desc": desc, "body": body, "og_image": "/assets/img/voyageurs-hero.jpg", "image": "/assets/img/voyageurs-hero.jpg",
            "ld": [crumbs_ld(L, trail), service_ld(L, t("Gestion des voyageurs Airbnb", "Airbnb guest management"), desc, url("voyageurs", L))]}


# ── Gestion du logement ─────────────────────────────────────────────────────
def logement(L):
    t = tr(L)
    trail = [(t("Gestion du logement", "Property management"), url("logement", L))]
    visual = f"""<div class="hero-visual">
        <figure class="hero-photo">{photo("logement-hero", t("Un propriétaire fait le tour de son appartement avec la conciergerie", "An owner showing their apartment to the concierge"), sizes="(max-width: 900px) 100vw, 45vw", lazy=False)}</figure>
        {fcard(t("Ménage", "Cleaning"), "t-blue", t("Après chaque départ des voyageurs.", "After every check-out."), "fc-1", "sparkle")}
        {fcard(t("Entretien", "Upkeep"), "t-sand", t("Petits travaux et réparations.", "Small works and repairs."), "fc-3", "wrench")}
        {sticker("linge")}
      </div>"""
    three = [
        ("green-s", "linge", t("Réapprovisionnement", "Restocking"),
         t("Nous remettons en place les petits éléments indispensables après chaque départ des voyageurs.", "We restock the small essentials after every check-out."), "logement"),
        ("coral-s", "menage", t("Ménage", "Cleaning"),
         t("Le ménage est assuré après chaque départ des voyageurs, pour un logement impeccable à chaque arrivée.", "Cleaning is done after every check-out, so the home is spotless for every arrival."), "logement"),
        ("blue-s", "outils", t("Entretien et travaux", "Upkeep and works"),
         t("Nous réalisons les petits travaux nécessaires au bon fonctionnement de votre logement.", "We carry out the small works needed to keep your home running smoothly."), "logement"),
    ]
    body = phead(L, trail, t("Gestion de votre propriété", "Property management"),
                 t("Votre bien <mark>entre de bonnes mains</mark>", "Your property <mark>in good hands</mark>"),
                 t("Optimisez votre bien sans effort : ménage, linge, réapprovisionnement, entretien, travaux et décoration, nous gardons votre logement prêt à accueillir, séjour après séjour.",
                   "Get the most from your property without lifting a finger: cleaning, linen, restocking, upkeep, works and decoration, we keep your home ready for guests, stay after stay."),
                 visual) + f"""
<section class="sec"><div class="wrap">
  <div class="cards three">{service_cards(L, three, link=False)}</div>
</div></section>

<section class="sec tight split"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("logement-menage", t("Ménage d'un salon parisien après le départ des voyageurs", "Cleaning a Paris living room after the guests leave"))}</figure>
    {fcard(t("Ménage", "Cleaning"), "t-blue", t("Fait après chaque passage des voyageurs.", "Done after every stay."), "a", "sparkle")}
    {sticker("menage")}
  </div>
  <div class="split-text reveal">
    {chip(t("Ménage et linge", "Cleaning and linen"))}
    <h2>{t("On s'occupe du ménage", "We take care of the cleaning")}</h2>
    <p>{t("Des espaces impeccables comptent autant pour vous que pour vos voyageurs. C'est pourquoi le ménage est fait après chaque séjour, et qu'il est complet :",
          "Spotless rooms matter as much to you as to your guests. That is why cleaning is done after every stay, and done thoroughly:")}</p>
    {ticks([t("Nettoyage en profondeur de chaque pièce", "A deep clean of every room"),
            t("Lavage et repassage des draps, des serviettes et du linge de maison", "Sheets, towels and household linen washed and ironed"),
            t("Remplacement des consommables : shampoing, gel douche, papier toilette", "Consumables restocked: shampoo, shower gel, toilet paper"),
            t("Aération du logement et vérification des appareils et des équipements", "The home aired, appliances and equipment checked")])}
  </div>
</div></section>

<section class="sec split flip"><div class="wrap split-grid">
  <div class="split-visual">
    <figure class="ph">{photo("logement-reassort", t("Serviettes et produits d'accueil remis en place dans une salle de bains", "Towels and toiletries restocked in a bathroom"))}</figure>
    {fcard(t("Réapprovisionnement", "Restocking"), "t-green", t("Articles de toilette de qualité, prêts avant chaque arrivée.", "Quality toiletries, ready before every arrival."), "a", "check")}
    {sticker("outils", cls="low")}
  </div>
  <div class="split-text reveal">
    {chip(t("Réapprovisionnement", "Restocking"))}
    <h2>{t("Une sérénité assurée", "Peace of mind, guaranteed")}</h2>
    <p>{t("Nous changeons les draps et les serviettes et remettons en place des articles de toilette de qualité supérieure. Tout est prêt avant l'arrivée des voyageurs, qui profitent pleinement de leur séjour sans se soucier des corvées ménagères.",
          "We change sheets and towels and restock high-quality toiletries. Everything is ready before guests arrive, so they can enjoy their stay without worrying about chores.")}</p>
    <p>{t("Entre deux séjours, des vérifications régulières gardent tout en parfait état ; et si un imprévu survient, d'une ampoule à changer à un dépannage plus complexe, notre équipe technique intervient rapidement.",
          "Between stays, regular checks keep everything in perfect condition; and if something goes wrong, from a bulb to change to a more complex repair, our technical team steps in quickly.")}</p>
  </div>
</div></section>

<section class="sec tight"><div class="wrap">
  {head(t("Déco et travaux", "Decoration and works"), t("Décoration, petits travaux et gros travaux de réaménagement", "Decoration, small works and larger refurbishments"), center=True)}
  <div class="cards two">
    <div class="card sand-s reveal">{illu("lampe")}<h3>{t("Pourquoi décorer ?", "Why decorate?")}</h3>
      <p>{t("La première impression que votre logement fait aux voyageurs est réelle. Si nécessaire, nous travaillons avec vous sur sa décoration, pour qu'il soit réservé plus facilement et suscite d'excellents commentaires.",
            "The first impression your home makes on guests is real. Where needed, we work with you on its decoration, so it gets booked more easily and earns excellent reviews.")}</p></div>
    <div class="card blue-s reveal">{illu("rouleau")}<h3>{t("Besoin de travaux ? Petits ou gros", "Need works done? Small or large")}</h3>
      <p>{t("Besoins courants de votre logement ou travaux imposés par la loi pour la location saisonnière : réparations mineures, ajustements ou améliorations pour respecter les exigences légales, notre équipe s'en charge, sans tracas pour vous ni pour vos voyageurs.",
            "Everyday needs or works required by law for short-term letting: minor repairs, adjustments or improvements to meet legal requirements, our team takes care of it, with no hassle for you or your guests.")}</p></div>
  </div>
</div></section>

{Q.where(L, "maison", "green-s")}
<section class="sec"><div class="wrap split-grid">
  <div class="split-text reveal">
    {illu("balance")}
    {chip(t("Litiges et dommages", "Disputes and damage"))}
    <h2>{t("Si un problème survient, nous nous en occupons", "If a problem arises, we handle it")}</h2>
    <p>{t("En cas de désaccord, nous servons de médiateur, en protégeant vos intérêts tout en cherchant un règlement équitable pour toutes les parties.",
          "If a disagreement arises, we mediate, protecting your interests while seeking a fair settlement for everyone.")}</p>
    <p>{t("Si un voyageur cause un dommage, nous le documentons avec des photos, une description détaillée et, si nécessaire, des devis de réparation, puis nous engageons la demande de dédommagement auprès de la plateforme ou de l'assurance du voyageur.",
          "If a guest causes damage, we document it with photos, a detailed description and, where needed, repair quotes, then file the claim with the platform or the guest's insurer.")}</p>
    <p>{t("Nous conseillons à tous nos clients une assurance adaptée à la location de courte durée.", "We advise all our clients to take out insurance suited to short-term rentals.")}</p>
  </div>
  <div>{faq_list(faq.pick(L, ["menage", "dommages", "acces-logement", "risques", "carte"]))}</div>
</div></section>"""
    title = t("Gestion de propriété Airbnb : ménage, linge | EdenFlats", "Airbnb Property Management: Cleaning, Linen | EdenFlats")
    desc = t("Ménage Airbnb après chaque départ, blanchisserie du linge, réapprovisionnement, maintenance, décoration et travaux : EdenFlats garde votre logement prêt à louer à Paris.",
             "Airbnb cleaning after every check-out, linen service, restocking, maintenance, decoration and works: EdenFlats keeps your Paris home ready to let.")
    return {"title": title, "desc": desc, "body": body, "og_image": "/assets/img/logement-hero.jpg", "image": "/assets/img/logement-hero.jpg",
            "ld": [crumbs_ld(L, trail), service_ld(L, t("Gestion de propriété Airbnb", "Airbnb property management"), desc, url("logement", L))]}


# ── Nos formules ────────────────────────────────────────────────────────────
def formules(L):
    t = tr(L)
    trail = [(t("Nos formules", "Our plans"), url("formules", L))]
    visual = f"""<div class="hero-visual">
        <figure class="hero-photo">{photo("formules-hero", t("Un propriétaire et la conciergerie relisent un contrat autour d'un café", "An owner and the concierge going over a contract over coffee"), sizes="(max-width: 900px) 100vw, 45vw", lazy=False)}</figure>
        {fcard(t("Revenu garanti", "Guaranteed income"), "t-green", t("≈ 15 % de marge moyenne.", "≈ 15% average margin."), "fc-1", "chart")}
        {fcard(t("Revenu réel", "Actual income"), "t-blue", t("18 à 25 % de commission.", "18–25% commission."), "fc-3", "sliders")}
      </div>"""
    rows = [
        (t("Ce que vous touchez", "What you receive"),
         t("Un revenu calculé à l'avance, versé que le logement soit loué ou non", "An income calculated in advance, paid whether or not the home is booked"),
         t("Les revenus de location du logement, moins notre commission", "The home's rental income, minus our commission")),
        (t("Rémunération d'EdenFlats", "EdenFlats' fee"),
         t("Une marge de 15 % en moyenne", "An average margin of 15%"),
         t("Une commission de 18 à 25 %, selon la durée de la location", "A commission of 18% to 25%, depending on rental length")),
        (t("Si le logement n'est pas loué", "If the home is not booked"),
         t("Vous touchez votre revenu garanti", "You still receive your guaranteed income"),
         t("Vous ne touchez rien, ce qui reste assez rare", "You receive nothing, which is fairly rare")),
        (t("Prix des nuits", "Nightly prices"),
         t("Votre revenu ne dépend pas du prix des nuits", "Your income does not depend on nightly prices"),
         t("Ajustés selon l'offre et la demande, jamais sous le prix minimum que vous fixez", "Adjusted to supply and demand, never below the minimum price you set")),
        (t("Pour qui", "Best for"),
         t("Les propriétaires qui veulent un revenu prévisible", "Owners who want a predictable income"),
         t("Les propriétaires qui veulent profiter des périodes de forte demande", "Owners who want to benefit from high-demand periods")),
    ]
    th_g, th_r = t("Revenu garanti", "Guaranteed income"), t("Revenu réel", "Actual income")
    table = "".join(f'<tr><th scope="row">{a}</th><td data-label="{th_g}">{b}</td><td data-label="{th_r}">{c}</td></tr>' for a, b, c in rows)
    factors = [
        ("green-s", "maison", t("Votre logement", "Your home"), t("Ses caractéristiques : adresse, nombre de couchages, équipements…", "Its features: address, number of beds, amenities…")),
        ("coral-s", "calendrier", t("Vos dates", "Your dates"), t("Le nombre de nuits que vous souhaitez nous confier.", "The number of nights you want to entrust to us.")),
        ("blue-s", "graphique", t("La demande", "Demand"), t("Le taux d'occupation moyen sur Airbnb à cette période, calculé par notre algorithme de tarification dynamique.", "The average Airbnb occupancy rate for that period, calculated by our dynamic pricing algorithm.")),
    ]
    fcards = "".join(f'<div class="card {c} reveal">{illu(i)}<h3>{h}</h3><p>{p}</p></div>' for c, i, h, p in factors)
    body = phead(L, trail, t("Nos formules", "Our plans"),
                 t("Revenu garanti ou revenu réel : <mark>deux façons de nous confier votre bien</mark>", "Guaranteed or actual income: <mark>two ways to work with us</mark>"),
                 t("Vous choisissez la formule qui vous convient : un revenu fixé à l'avance, ou les revenus réels du logement moins notre commission. Dans les deux cas, nous gérons tout, avec des contrats flexibles.",
                   "You choose the plan that suits you: an income agreed in advance, or the home's actual income minus our commission. Either way, we handle everything, with flexible contracts."),
                 visual, actions=False) + f"""
<section class="sec"><div class="wrap">
  <div class="plans">
    <div class="plan green-s reveal">{illu("maison")}{chip(t("Formule 1", "Plan 1"))}<h3>{t("Le contrat au revenu garanti", "The guaranteed-income contract")}</h3>
      <p class="big">{t("≈ 15 %", "≈ 15%")}<small>{t("de marge moyenne pour EdenFlats", "average margin for EdenFlats")}</small></p>
      {ticks([t("Un revenu calculé selon vos dates, votre logement et le taux d'occupation moyen sur Airbnb", "An income based on your dates, your home and the average Airbnb occupancy rate"),
              t("Versé que le logement soit loué ou non", "Paid whether or not the home is booked"),
              t("Un revenu prévisible, sans vous soucier des périodes creuses", "A predictable income, with no worries about quiet periods")])}</div>
    <div class="plan blue-s reveal">{illu("graphique")}{chip(t("Formule 2", "Plan 2"))}<h3>{t("Le contrat au revenu réel", "The actual-income contract")}</h3>
      <p class="big">{t("18 à 25 %", "18–25%")}<small>{t("de commission sur les revenus, selon la durée de location", "commission on income, depending on rental length")}</small></p>
      {ticks([t("Plus le logement est loué, plus vous y gagnez", "The more the home is booked, the more you earn"),
              t("Prix ajustés à la hausse ou à la baisse selon l'offre et la demande", "Prices moved up or down with supply and demand"),
              t("Un prix minimum par nuit que vous fixez, et sous lequel nous ne descendons pas", "A minimum nightly price that you set, and that we never go below")])}</div>
  </div>
  <table class="compare">
    <thead><tr><th></th><th scope="col">{th_g}</th><th scope="col">{th_r}</th></tr></thead>
    <tbody>{table}</tbody>
  </table>
</div></section>

<section class="sec tight"><div class="wrap">
  {head(t("Le calcul", "How it's calculated"), t("Comment nous calculons votre revenu", "How we calculate your income"),
        t("Le revenu de votre logement dépend de trois facteurs. Après une évaluation détaillée, nous vous remettons une projection réaliste et transparente.",
          "Your income depends on three factors. After a detailed assessment, we give you a realistic, transparent projection."), center=True)}
  <div class="cards three">{fcards}</div>
</div></section>

{Q.where(L, "tour-eiffel", "coral-s")}
<section class="sec tight"><div class="wrap faq-wrap">
  <div>{head("FAQ", t("Questions sur les formules", "Questions about our plans"))}
    <p class="intro">{t("Contrats flexibles et services à la carte : parlons de ce qui convient à votre logement.", "Flexible contracts and à la carte services: let's talk about what suits your home.")}</p>
    <p style="margin-top:22px">{btn(url("contact", L), t("Demander une estimation", "Ask for an estimate"))}</p></div>
  <div>{faq_list(faq.pick(L, ["tarifs", "revenu", "gagner", "prix", "prix-change", "carte"]))}</div>
</div></section>"""
    title = t("Tarifs conciergerie Airbnb : revenu garanti ou réel | EdenFlats", "Airbnb Management Fees: Guaranteed or Actual Income | EdenFlats")
    desc = t("Tarifs de la conciergerie Airbnb EdenFlats : contrat au revenu garanti (marge moyenne de 15 %) ou au revenu réel (commission de 18 à 25 %). Comparez les deux formules.",
             "EdenFlats Airbnb management fees: guaranteed-income contract (15% average margin) or actual-income contract (18–25% commission). Compare the two plans.")
    return {"title": title, "desc": desc, "body": body, "og_image": "/assets/img/formules-hero.jpg", "image": "/assets/img/formules-hero.jpg",
            "ld": [crumbs_ld(L, trail), service_ld(L, t("Conciergerie Airbnb : formules", "Airbnb management plans"), desc, url("formules", L))]}


# ── FAQ ─────────────────────────────────────────────────────────────────────
def faq_page(L):
    t = tr(L)
    trail = [("FAQ", url("faq", L))]
    ids = ["formules", "annonce", "voyageurs", "cles", "reglementation"]
    groups = []
    all_items = []
    for gid, (fr, en, keys) in zip(ids, faq.GROUPS):
        items = faq.pick(L, keys)
        all_items += items
        groups.append(f'<div class="faq-group" id="{gid}"><h2>{t(fr, en)}</h2>{faq_list(items)}</div>')
    nav = "".join(f'<a class="chip" href="#{gid}">{t(fr, en)}</a>' for gid, (fr, en, _) in zip(ids, faq.GROUPS))
    body = phead(L, trail, "FAQ", t("Les questions <mark>des propriétaires</mark>", "Owners' <mark>questions</mark>"),
                 t("Formules, annonce, voyageurs, clés, ménage et réglementation : tout ce qu'on nous demande avant de nous confier un logement.",
                   "Plans, listing, guests, keys, cleaning and regulations: everything owners ask us before handing over their keys."),
                 actions=False) + f"""
<section class="sec"><div class="wrap faq-wrap">
  <aside><div class="facts sand-s"><h3>{t("Thèmes", "Topics")}</h3><div class="cta-row" style="margin-top:14px">{nav}</div>
    <p class="note">{t("Vous ne trouvez pas votre réponse ?", "Can't find your answer?")}</p>
    <p style="margin-top:12px">{btn(url("contact", L), t("Nous contacter", "Contact us"), "small")}</p></div></aside>
  <div>{"".join(groups)}</div>
</div></section>"""
    return {"title": t("FAQ conciergerie Airbnb : tarifs, clés, législation | EdenFlats", "Airbnb Management FAQ: Fees, Keys, Rules | EdenFlats"),
            "desc": t("Tarifs, calcul du revenu, compte Airbnb, sélection des voyageurs, clés, ménage, législation Airbnb à Paris : les réponses de la conciergerie EdenFlats aux propriétaires.",
                      "Fees, income, your Airbnb account, guest screening, keys, cleaning and the Paris Airbnb rules: EdenFlats answers the questions owners ask."),
            "body": body, "ld": [crumbs_ld(L, trail), faq_ld(all_items)], "og_image": "/assets/img/accueil-faq.jpg", "image": "/assets/img/accueil-faq.jpg"}


# ── Contact ─────────────────────────────────────────────────────────────────
def contact(L):
    t = tr(L)
    s = SITE
    trail = [(t("Contact", "Contact"), url("contact", L))]
    cards = [
        ("green-s", "chat", "WhatsApp", t("Écrire sur WhatsApp", "Message us"), f"https://wa.me/{s['whatsapp']}", True),
        ("coral-s", "phone", t("Téléphone", "Phone"), s["phone"], f"tel:{s['phone_href']}", False),
        ("blue-s", "mail", t("E-mail", "Email"), s["email"], f"mailto:{s['email']}", False),
    ]
    blank = ' target="_blank" rel="noopener"'
    cc = "".join(f'<a class="ccard {c}" href="{h}"{blank if ext else ""}>{icon(i)}<small>{k}</small><b>{v}</b></a>'
                 for c, i, k, v, h, ext in cards)
    body = phead(L, trail, t("Contact", "Contact"), t("Parlez-nous de <mark>votre projet</mark>", "Tell us about <mark>your property</mark>"),
                 t("Appelez-nous, écrivez-nous sur WhatsApp ou par e-mail. Si vous avez besoin de plus d'informations ou d'un devis personnalisé, n'hésitez pas à nous contacter.",
                   "Call us, message us on WhatsApp or send an email. If you need more information or a personalised quote, get in touch."),
                 actions=False) + f"""
<section class="sec"><div class="wrap">
  <div class="contact-cards">{cc}</div>
</div></section>
<section class="sec tight"><div class="wrap two">
  <div class="prose">
    <h2>{t("Pour préparer notre échange", "To prepare our conversation")}</h2>
    {ticks([t("La commune ou le quartier, et le type de logement", "The town or neighbourhood, and the type of home"),
            t("Le nombre de couchages", "The number of beds"),
            t("Les dates ou le nombre de nuits que vous souhaitez nous confier", "The dates or number of nights you want to entrust to us"),
            t("S'il est déjà en location, et sur quelles plateformes", "Whether it is already let, and on which platforms"),
            t("Ce que vous souhaitez nous confier : tout, ou certains services", "What you want us to handle: everything, or some services"),
            t("La formule envisagée : revenu garanti ou revenu réel", "The plan you have in mind: guaranteed or actual income")])}
  </div>
  <aside class="facts cream-s"><h3>{t("Vous êtes voyageur ?", "Are you a guest?")}</h3>
    <p style="margin:10px 0 18px">{t("Pour réserver un logement EdenFlats, rendez-vous sur notre page de réservation.", "To book an EdenFlats home, go to our booking page.")}</p>
    {btn(s["booking"], t("Réserver un séjour", "Book a stay"), "small", ext=True, ico="out")}
    <h3 style="margin-top:26px">{t("Suivez-nous", "Follow us")}</h3>
    {social_links(L)}
  </aside>
</div></section>"""
    desc = t("Contactez la conciergerie Airbnb EdenFlats par téléphone, WhatsApp ou e-mail pour confier la gestion de votre logement à Paris et en Île-de-France. Estimation de revenus.",
             "Contact EdenFlats, Airbnb management in Paris, by phone, WhatsApp or email to have your Paris or Île-de-France home managed. Ask for an income estimate.")
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": t("Contact EdenFlats", "Contact EdenFlats"),
          "url": SITE["url"] + url("contact", L), "about": {"@id": SITE["url"] + "/#entreprise"}}
    return {"title": t("Contact conciergerie Airbnb Paris | EdenFlats", "Contact our Paris Airbnb Management Team | EdenFlats"),
            "desc": desc, "body": body, "ld": [crumbs_ld(L, trail), ld]}


# ── Mentions légales ────────────────────────────────────────────────────────
def mentions(L):
    t = tr(L)
    s = SITE
    c = s["company"]
    trail = [(t("Mentions légales", "Legal notice"), url("mentions", L))]
    missing = t("à compléter", "to be completed")

    def val(v, label):
        return v if v else todo(f"{label} : {missing}" if L == "fr" else f"{label}: {missing}")
    rows = [
        (t("Dénomination sociale", "Company name"), f"{escape(c['name'])} ({c['acronym']})"),
        (t("Nom commercial du site", "Trading name"), "EdenFlats"),
        (t("Forme juridique", "Legal form"), c["form"][L]),
        (t("Capital social", "Share capital"), val(c["capital"], t("Capital", "Capital"))),
        (t("Siège social", "Registered office"), c["address"]),
        ("SIREN", c["siren"]),
        ("SIRET", c["siret"]),
        (t("Immatriculation", "Registration"), val(c["rcs"], "RCS")),
        (t("TVA intracommunautaire", "EU VAT number"), val(c["vat"], t("Numéro de TVA", "VAT number"))),
        (t("Code NAF", "NAF code"), f"{c['naf']} ({t('agences immobilières', 'real estate agencies')})"),
        (t("Directrice de la publication", "Publication director"), f"{c['director']}, {c['director_role'][L]}"),
        (t("Téléphone", "Phone"), f'<a href="tel:{s["phone_href"]}">{s["phone"]}</a>'),
        (t("E-mail", "Email"), f'<a href="mailto:{s["email"]}">{s["email"]}</a>'),
    ]
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    h = s["host"]
    body = phead(L, trail, t("Informations", "Information"), t("Mentions légales", "Legal notice"),
                 t("Informations sur l'éditeur et l'hébergeur du site, conformément à la loi pour la confiance dans l'économie numérique (LCEN).",
                   "Information about the publisher and host of this website, as required by French law (LCEN)."), actions=False) + f"""
<section class="sec"><div class="wrap doc">
  <h2>{t("Éditeur du site", "Publisher")}</h2>
  <dl>{dl}</dl>
  <h2>{t("Hébergement", "Hosting")}</h2>
  <p>{t("Le site est hébergé par", "The website is hosted by")} {h["name"]}, {h["address"]} (<a href="{h["url"]}" target="_blank" rel="noopener">{h["url"].replace("https://", "")}</a>).</p>
  <h2>{t("Activité", "Activity")}</h2>
  <p>{t("EdenFlats est une conciergerie qui gère des logements en location de courte et moyenne durée pour le compte de leurs propriétaires, sur des plateformes comme Airbnb, Booking.com, Vrbo ou Expedia.",
        "EdenFlats is a property management service that runs homes as short and mid-term rentals on behalf of their owners, on platforms such as Airbnb, Booking.com, Vrbo or Expedia.")}</p>
  <h2>{t("Conception", "Design and development")}</h2>
  <p>{t("Site conçu et réalisé par", "Website designed and built by")} <a href="{s['maker'][1]}" target="_blank" rel="noopener">{s['maker'][0]}</a>.</p>
  <h2>{t("Propriété intellectuelle", "Intellectual property")}</h2>
  <p>{t("Les textes, le logo et la mise en page du site appartiennent à EdenFlats, sauf mention contraire. Toute reproduction, même partielle, est interdite sans autorisation écrite.",
        "The texts, logo and layout of this website belong to EdenFlats unless stated otherwise. Any reproduction, even partial, is prohibited without written permission.")}</p>
  <p>{t("Les photos du site sont des images d'illustration.", "The photos on this website are illustrations.")} {t("Les polices Bricolage Grotesque et Public Sans sont distribuées sous licence SIL Open Font License 1.1.", "The Bricolage Grotesque and Public Sans fonts are distributed under the SIL Open Font License 1.1.")}</p>
  <h2>{t("Données personnelles", "Personal data")}</h2>
  <p>{t("Le traitement de vos données est décrit dans notre", "How we handle your data is described in our")} <a href="{url('confidentialite', L)}">{t("politique de confidentialité", "privacy policy")}</a>.</p>
</div></section>"""
    return {"title": t("Mentions légales | EdenFlats", "Legal notice | EdenFlats"),
            "desc": t("Mentions légales du site EdenFlats : éditeur (EDENEL PATRIMOINE GESTION RESEAUX & SERVICES, Sucy-en-Brie), hébergeur et propriété intellectuelle.",
                      "EdenFlats legal notice: publisher (EDENEL PATRIMOINE GESTION RESEAUX & SERVICES, Sucy-en-Brie), website host and intellectual property."),
            "body": body, "ld": [crumbs_ld(L, trail)], "cta": False}


# ── Confidentialité ─────────────────────────────────────────────────────────
def confidentialite(L):
    t = tr(L)
    s = SITE
    c = s["company"]
    trail = [(t("Confidentialité", "Privacy"), url("confidentialite", L))]
    banner = s["cookie_banner"]
    if banner:
        cookies = f"""<p>{t("Le site ne dépose aucun cookie publicitaire, et aucun cookie sans votre accord. Il garde seulement dans votre navigateur (stockage local) deux préférences nécessaires à son fonctionnement : votre choix dans le bandeau cookies, pendant six mois, et la langue que vous avez choisie quand le site vous la propose. Elles ne vous identifient pas et ne quittent pas votre appareil.",
        "The website sets no advertising cookies, and no cookies at all without your consent. It only keeps two preferences in your browser (local storage) that it needs to work: your choice in the cookie banner, for six months, and the language you picked when the site offered it. They do not identify you and never leave your device.")}</p>
  <h3>{t("Mesure d'audience", "Audience measurement")}</h3>
  <p>{t("Si vous cliquez sur « Accepter » dans le bandeau, nous utilisons Google Analytics, un service de Google Ireland Limited, pour compter les visites et savoir quelles pages sont consultées. Google Analytics dépose alors des cookies (_ga et _ga_…) conservés treize mois au plus. Les données peuvent être transférées aux États-Unis, où Google est certifié au titre du Data Privacy Framework UE–États-Unis. Si vous cliquez sur « Refuser », Google Analytics n'est pas chargé et rien n'est déposé.",
        "If you click “Accept” in the banner, we use Google Analytics, a service of Google Ireland Limited, to count visits and see which pages are read. Google Analytics then sets cookies (_ga and _ga_…) kept for thirteen months at most. Data may be transferred to the United States, where Google is certified under the EU–US Data Privacy Framework. If you click “Decline”, Google Analytics is not loaded and nothing is set.")}</p>
  <p>{t("Vous pouvez changer d'avis à tout moment, ici ou avec le lien « Gérer les cookies » en bas de chaque page. Votre choix vous est redemandé au bout de six mois.",
        "You can change your mind at any time, here or with the “Cookie settings” link at the bottom of every page. You will be asked again after six months.")}</p>
  <p><button class="btn small" type="button" data-consent-open><span>{t("Gérer les cookies", "Cookie settings")}</span><i>{icon("cookie")}</i></button></p>"""
    else:
        cookies = f"""<p>{t("Le site ne dépose aucun cookie et n'utilise aucun outil de mesure d'audience. Il garde seulement dans votre navigateur (stockage local) la langue que vous avez choisie quand le site vous la propose : cette préférence, nécessaire à son fonctionnement, ne vous identifie pas et ne quitte pas votre appareil.",
        "The website sets no cookies and uses no audience measurement tools. It only keeps in your browser (local storage) the language you picked when the site offered it: this preference, which the site needs to work, does not identify you and never leaves your device.")}</p>"""
    body = phead(L, trail, t("Informations", "Information"), t("Politique de confidentialité et cookies", "Privacy and cookie policy"),
                 t("Ce que le site garde dans votre navigateur, ce qui se passe quand vous nous contactez, et vos droits.",
                   "What the website keeps in your browser, what happens when you contact us, and your rights."), actions=False) + f"""
<section class="sec"><div class="wrap doc">
  <h2>{t("Responsable du traitement", "Data controller")}</h2>
  <p>{escape(c['name'])} ({c['acronym']}), {c['address']}, {t("qui exploite la marque EdenFlats. Contact :", "which operates the EdenFlats brand. Contact:")} <a href="mailto:{s['email']}">{s['email']}</a>.</p>
  <h2>{t("Données collectées", "Data collected")}</h2>
  <p>{t("Le site n'a pas de formulaire. Les polices de caractères et les images sont hébergées sur le site, sans appel à un service tiers.",
        "The website has no forms. Fonts and images are hosted on the site, with no call to a third-party service.")}</p>
  <p>{t("Quand vous nous contactez par téléphone, WhatsApp ou e-mail, nous utilisons vos coordonnées et votre message pour vous répondre et, si nous travaillons ensemble, pour préparer et exécuter notre contrat.",
        "When you contact us by phone, WhatsApp or email, we use your contact details and your message to reply and, if we work together, to prepare and perform our contract.")}</p>
  <h2 id="cookies">{t("Cookies et stockage local", "Cookies and local storage")}</h2>
  {cookies}
  <h2>{t("Durée de conservation", "Retention")}</h2>
  <p>{t("Les échanges avec les personnes qui ne deviennent pas clientes sont conservés au plus trois ans après le dernier contact. Les données des clients sont conservées pendant la durée du contrat, puis le temps imposé par nos obligations légales, notamment comptables.",
        "Exchanges with people who do not become clients are kept for at most three years after the last contact. Client data is kept for the duration of the contract, then for as long as our legal obligations require, notably accounting.")}</p>
  <h2>{t("Services tiers", "Third-party services")}</h2>
  <ul>
    <li>{t("WhatsApp est un service de WhatsApp Ireland Limited : si vous nous écrivez par ce biais, sa propre politique de confidentialité s'applique.", "WhatsApp is a service of WhatsApp Ireland Limited: if you message us through it, its own privacy policy applies.")}</li>
    <li>{t("L'hébergeur du site,", "The website host,")} {s['host']['name']}, {t("peut enregistrer l'adresse IP des visiteurs dans ses journaux techniques, à des fins de sécurité.", "may record visitors' IP addresses in its technical logs, for security purposes.")}</li>
    <li>{t("Les liens vers nos réseaux sociaux et vers notre page de réservation mènent à des sites tiers, qui appliquent leurs propres règles.", "Links to our social media pages and to our booking page lead to third-party sites, which apply their own rules.")}</li>
  </ul>
  <h2>{t("Vos droits", "Your rights")}</h2>
  <p>{t("Conformément au RGPD, vous pouvez accéder à vos données, les rectifier, les effacer, en limiter le traitement, vous y opposer et en demander la portabilité, en écrivant à", "Under the GDPR, you can access, correct or erase your data, restrict or object to its processing and request its portability, by writing to")} <a href="mailto:{s['email']}">{s['email']}</a>. {t("Vous pouvez aussi adresser une réclamation à la CNIL", "You can also lodge a complaint with the CNIL")} (<a href="https://www.cnil.fr" target="_blank" rel="noopener">cnil.fr</a>).</p>
</div></section>"""
    return {"title": t("Politique de confidentialité et cookies | EdenFlats", "Privacy and cookie policy | EdenFlats"),
            "desc": t("Politique de confidentialité et de cookies d'EdenFlats : cookies déposés seulement avec votre accord, données de contact, durée de conservation et vos droits RGPD.",
                      "EdenFlats privacy and cookie policy: cookies set only with your consent, how we use your contact details, how long we keep them and your rights under the GDPR."),
            "body": body, "ld": [crumbs_ld(L, trail)], "cta": False}


# ── Conditions générales de vente ───────────────────────────────────────────
# Reprises de l'ancien site (version du 7 avril 2025), complétées : nom de la société, renvois vers les pages,
# droit de rétractation, médiation et tribunaux, qui s'imposent quand le client est un consommateur.
# Les cadres pointillés sont à compléter ; le texte est à faire valider avant la mise en ligne.
CGV_MAJ = ("24 novembre 2026", "24 November 2026")


def cgv(L):
    t = tr(L)
    s = SITE
    c = s["company"]
    trail = [(t("Conditions générales de vente", "Terms and conditions"), url("cgv", L))]
    mail = f'<a href="mailto:{s["email"]}">{s["email"]}</a>'
    hours = todo(t("[nombre] heures", "[number] hours"))

    def ul(items):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    articles = [
        (t("Objet", "Purpose and scope"),
         f"<p>{t('Les présentes conditions générales de vente (CGV) régissent les relations contractuelles entre', 'These terms and conditions govern the contractual relationship between')} {escape(c['name'])} ({c['acronym']}), "
         f"{t('société par actions simplifiée dont le siège est situé', 'a French simplified joint-stock company (SAS) whose registered office is at')} {c['address']}, SIRET {c['siret']}, "
         f"{t('qui exploite la marque EdenFlats (ci-après « EdenFlats »), et toute personne qui lui confie des prestations de conciergerie pour un logement loué en courte ou moyenne durée (ci-après « le Client »).', 'which operates the EdenFlats brand (“EdenFlats”), and any person who entrusts it with concierge services for a home let on a short or mid-term basis (“the Client”).')}</p>"
         f"<p>{t('Le contrat de gestion ou le devis accepté par le Client précise et complète ces conditions ; en cas de contradiction, il prévaut.', 'The management agreement or the quote accepted by the Client details and supplements these terms; where they conflict, it prevails.')}</p>"),
        (t("Prestations", "Services"),
         f"<p>{t('EdenFlats propose notamment les services suivants :', 'EdenFlats offers in particular the following services:')}</p>"
         + ul([t("remise et récupération des clés, accueil des voyageurs (check-in et check-out) ;", "key handover and collection, guest welcome (check-in and check-out);"),
               t("ménage professionnel ;", "professional cleaning;"),
               t("gestion des réservations en ligne ;", "online booking management;"),
               t("communication avec les voyageurs ;", "communication with guests;"),
               t("blanchisserie et fourniture de linge ;", "laundry and linen supply;"),
               t("maintenance de base et gestion des urgences.", "basic maintenance and emergency handling.")])
         + f"<p>{t('Le détail des prestations est présenté sur le site www.edenflats.com, notamment aux pages', 'The services are described on www.edenflats.com, in particular on the')} "
           f"<a href=\"{url('voyageurs', L)}\">{t('Gestion des voyageurs', 'Guest management')}</a>, <a href=\"{url('logement', L)}\">{t('Gestion du logement', 'Property management')}</a> "
           f"{t('et', 'and')} <a href=\"{url('formules', L)}\">{t('Nos formules', 'Plans')}</a>{t(', et précisé dans le contrat ou le devis remis au Client.', ' pages, and set out in the agreement or quote given to the Client.')}</p>"),
        (t("Conditions d'accès aux services", "Eligibility"),
         f"<p>{t('Pour bénéficier des services, le Client doit être propriétaire ou gestionnaire légal d’un bien mis en location de courte durée. Il fournit les informations nécessaires à la bonne exécution des prestations : adresse du logement, accès, calendrier, consignes particulières, etc.', 'To use the services, the Client must own or lawfully manage a property let on a short-term basis. The Client provides the information needed to perform the services: address of the home, access, calendar, specific instructions, etc.')}</p>"
         f"<p>{t('Le Client veille au respect des règles qui s’appliquent à la location de son logement (déclaration en mairie, numéro d’enregistrement, nombre de nuits autorisé, règlement de copropriété). Notre', 'The Client ensures that the rules applying to the letting of the home are complied with (registration with the city, registration number, number of nights allowed, building rules). Our')} "
         f"<a href=\"{url('faq', L)}#reglementation\">{t('FAQ', 'FAQ')}</a> {t('résume les règles en vigueur à Paris.', 'sums up the rules in force in Paris.')}</p>"),
        (t("Tarifs et paiement", "Prices and payment"),
         f"<p>{t('Les tarifs sont communiqués sur devis personnalisé ou sur le site (page', 'Prices are given in a personalised quote or on the website (')} <a href=\"{url('formules', L)}\">{t('Nos formules', 'Plans')}</a>{t('), en euros toutes taxes comprises. Le paiement des prestations peut s’effectuer par virement bancaire, par carte bancaire ou par prélèvement automatique, si celui-ci a été convenu.', ' page), in euros including all taxes. Services can be paid by bank transfer, by card or by direct debit, if agreed.')}</p>"
         f"<p>{t('Toute prestation commencée est due dans son intégralité. Des frais supplémentaires peuvent s’appliquer en cas de demandes spécifiques ou urgentes ; ils sont annoncés au Client avant l’intervention.', 'Any service that has started is due in full. Extra charges may apply to specific or urgent requests; the Client is told about them before the work is done.')}</p>"
         f"<p>{t('Si le Client est un professionnel, tout retard de paiement entraîne de plein droit des pénalités calculées à trois fois le taux d’intérêt légal et une indemnité forfaitaire de 40 € pour frais de recouvrement (article L441-10 du Code de commerce).', 'If the Client is a business, any late payment automatically incurs penalties at three times the French statutory interest rate and a fixed recovery fee of €40 (article L441-10 of the French Commercial Code).')}</p>"),
        (t("Réservation et annulation des prestations", "Booking and cancelling services"),
         f"<p>{t('Toute demande de prestation doit être confirmée au moins', 'Any service request must be confirmed at least')} {hours} {t('à l’avance. Le Client peut annuler sans frais jusqu’à', 'in advance. The Client may cancel free of charge up to')} {hours} "
         f"{t('avant la prestation ; passé ce délai, le montant total est dû.', 'before the service; after that, the full amount is due.')}</p>"),
        (t("Droit de rétractation", "Right of withdrawal"),
         f"<p>{t('Si le Client est un consommateur et que le contrat a été conclu à distance (par téléphone, e-mail ou WhatsApp, par exemple) ou hors établissement, il dispose de quatorze jours à compter de la conclusion du contrat pour se rétracter, sans avoir à motiver sa décision, par une déclaration dénuée d’ambiguïté adressée à EdenFlats, par exemple par e-mail à', 'If the Client is a consumer and the contract was concluded at a distance (by phone, email or WhatsApp, for example) or off-premises, the Client has fourteen days from the conclusion of the contract to withdraw, without giving any reason, by an unambiguous statement sent to EdenFlats, for example by email to')} {mail} "
         f"{t('(articles L221-18 et suivants du Code de la consommation).', '(articles L221-18 et seq. of the French Consumer Code).')}</p>"
         f"<p>{t('Si le Client demande expressément que la prestation commence avant la fin de ce délai, il reste redevable du montant correspondant au service fourni jusqu’à sa rétractation. Une prestation pleinement exécutée avant la fin du délai, à sa demande, ne peut plus faire l’objet d’une rétractation.', 'If the Client expressly asks for the service to start before the end of this period, the Client remains liable for the amount corresponding to the service provided until withdrawal. A service fully performed before the end of the period, at the Client’s request, can no longer be withdrawn from.')}</p>"),
        (t("Engagements d'EdenFlats", "EdenFlats' commitments"),
         f"<p>{t('EdenFlats s’engage à exécuter les prestations avec diligence, professionnalisme et selon les standards de qualité en vigueur. En cas d’impossibilité d’exécution (force majeure, accident, etc.), EdenFlats s’engage à en informer le Client au plus vite.', 'EdenFlats undertakes to perform the services diligently, professionally and to current quality standards. If a service cannot be performed (force majeure, accident, etc.), EdenFlats undertakes to inform the Client as soon as possible.')}</p>"),
        (t("Responsabilités", "Liability"),
         f"<p>{t('EdenFlats ne saurait être tenue responsable :', 'EdenFlats cannot be held liable for:')}</p>"
         + ul([t("des dégâts causés par les voyageurs ;", "damage caused by guests;"),
               t("des vols ou dégradations commis hors de sa présence ;", "theft or damage occurring in its absence;"),
               t("des pertes de revenus dues à des annulations extérieures à sa gestion.", "loss of income due to cancellations beyond its management.")])
         + f"<p>{t('En cas de dégâts causés par des voyageurs, EdenFlats accompagne le Client dans ses démarches auprès de la plateforme de réservation. Le Client reste seul responsable des déclarations fiscales et juridiques liées à la location de son bien.', 'If guests cause damage, EdenFlats helps the Client with the claim to the booking platform. The Client remains solely responsible for the tax and legal declarations relating to the letting of the property.')}</p>"),
        (t("Assurance", "Insurance"),
         f"<p>{t('Le Client s’engage à disposer d’une assurance multirisque habitation couvrant la location de courte durée. EdenFlats dispose d’une assurance de responsabilité civile professionnelle', 'The Client undertakes to hold home insurance covering short-term letting. EdenFlats holds professional liability insurance')} "
         f"({todo(t('assureur et numéro de contrat à compléter', 'insurer and policy number to be completed'))}).</p>"),
        (t("Données personnelles", "Personal data"),
         f"<p>{t('Les données personnelles du Client sont traitées conformément au règlement général sur la protection des données (RGPD), selon notre', 'The Client’s personal data is processed in accordance with the General Data Protection Regulation (GDPR), as described in our')} "
         f"<a href=\"{url('confidentialite', L)}\">{t('politique de confidentialité', 'privacy policy')}</a>. "
         f"{t('Le Client peut à tout moment demander l’accès à ses données, leur rectification ou leur suppression en écrivant à', 'The Client may at any time ask to access, correct or delete their data by writing to')} {mail}.</p>"),
        (t("Médiation de la consommation", "Consumer mediation"),
         f"<p>{t('Si le Client est un consommateur, il peut recourir gratuitement à un médiateur de la consommation pour résoudre à l’amiable un litige avec EdenFlats, après avoir adressé une réclamation écrite à EdenFlats (articles L612-1 et suivants du Code de la consommation). Médiateur :', 'If the Client is a consumer, they may refer a dispute with EdenFlats to a consumer mediator free of charge, after first sending a written complaint to EdenFlats (articles L612-1 et seq. of the French Consumer Code). Mediator:')} "
         f"{todo(t('nom, adresse et site du médiateur à compléter', 'mediator name, address and website to be completed'))}.</p>"),
        (t("Droit applicable et litiges", "Governing law and disputes"),
         f"<p>{t('Les présentes CGV sont soumises au droit français. En cas de litige, une solution amiable sera recherchée en priorité.', 'These terms are governed by French law. In the event of a dispute, an amicable solution will be sought first.')}</p>"
         f"<p>{t('À défaut, si le Client est un professionnel, le litige sera porté devant les tribunaux compétents dans le ressort du siège social d’EdenFlats, à Sucy-en-Brie. Si le Client est un consommateur, il peut saisir, à son choix, l’une des juridictions territorialement compétentes ou celle du lieu où il demeurait au moment de la conclusion du contrat ou de la survenance du fait dommageable.', 'Failing that, if the Client is a business, the dispute will be brought before the competent courts for the area of EdenFlats’ registered office, in Sucy-en-Brie. If the Client is a consumer, they may choose to bring the matter before any court with territorial jurisdiction or the court for the place where they lived when the contract was concluded or when the damage occurred.')}</p>"),
    ]
    arts = "".join(f'<h2 id="article-{i}">{t("Article", "Article")} {i} – {h}</h2>{b}' for i, (h, b) in enumerate(articles, 1))
    toc = "".join(f'<a class="chip" href="#article-{i}">{i}. {h}</a>' for i, (h, _) in enumerate(articles, 1))
    version = t(f"Dernière mise à jour : {CGV_MAJ[0]}.", f"Last updated: {CGV_MAJ[1]}.")
    translation = "" if L == "fr" else (f'<p class="note">This English version is a translation provided for convenience. '
                                        f'If it differs from the <a href="{url("cgv", "fr")}" hreflang="fr" lang="fr">French version</a>, the French version prevails.</p>')
    body = phead(L, trail, t("Informations", "Information"), t("Conditions générales de vente", "Terms and conditions"),
                 t("Les conditions qui s'appliquent aux prestations de conciergerie EdenFlats : services, tarifs, annulation, responsabilités et litiges.",
                   "The terms that apply to EdenFlats concierge services: services, prices, cancellation, liability and disputes."), actions=False) + f"""
<section class="sec"><div class="wrap doc">
  <p class="note" style="margin-top:0">{version}</p>{translation}
  <nav class="toc cta-row" aria-label="{t("Articles", "Articles")}">{toc}</nav>
  {arts}
</div></section>"""
    return {"title": t("Conditions générales de vente | EdenFlats", "Terms and conditions | EdenFlats"),
            "desc": t("Conditions générales de vente d'EdenFlats, conciergerie Airbnb à Paris et en Île-de-France : prestations, tarifs, annulation, rétractation, responsabilités et litiges.",
                      "EdenFlats terms and conditions for Airbnb management in Paris and Île-de-France: services, prices, cancellation, withdrawal, liability and disputes."),
            "body": body, "ld": [crumbs_ld(L, trail)], "cta": False}


# ── Plan du site ────────────────────────────────────────────────────────────
def plan_du_site(L):
    t = tr(L)
    trail = [(t("Plan du site", "Sitemap"), url("plan", L))]

    def links(items):
        return "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in items)
    main = [(t("Accueil", "Home"), url("home", L)), (t("Gestion des voyageurs", "Guest management"), url("voyageurs", L)),
            (t("Gestion du logement", "Property management"), url("logement", L)), (t("Nos formules", "Our plans"), url("formules", L)),
            (t("Questions fréquentes", "FAQ"), url("faq", L)), (t("Contact", "Contact"), url("contact", L))]
    paris = [(t("Conciergerie Airbnb à Paris", "Airbnb management in Paris"), url("paris", L))] + [
        (f'{a[L]["name"]} <small>{a[L]["arr"]}</small>', Q.area_url(a, L)) for a in Q.AREAS]
    towns = [(a[L]["name"], Q.area_url(a, L)) for a in Q.TOWNS]
    info = [(t("Mentions légales", "Legal notice"), url("mentions", L)), (t("Conditions générales de vente", "Terms and conditions"), url("cgv", L)),
            (t("Confidentialité et cookies", "Privacy and cookies"), url("confidentialite", L))]
    groups = [("green-s", "maison", t("Conciergerie Airbnb", "Airbnb management"), main, ""),
              ("blue-s", "tour-eiffel", "Paris", paris, " cols2"),
              ("coral-s", "carte", t("Île-de-France", "Île-de-France"), towns, ""),
              ("sand-s", "balance", t("Informations", "Information"), info, "")]
    cards = "".join(f'<div class="card {c} sitemap-card">{illu(i)}<h2>{h}</h2><ul class="sitemap-list{x}">{links(items)}</ul></div>'
                    for c, i, h, items, x in groups)
    other = OTHER[L]
    body = phead(L, trail, t("Informations", "Information"), t("Plan du site", "Sitemap"),
                 t("Toutes les pages du site EdenFlats en un coup d'œil : nos services, nos formules, les quartiers de Paris et les communes d'Île-de-France où nous intervenons.",
                   "Every page of the EdenFlats website at a glance: our services, our plans, and the Paris neighbourhoods and Île-de-France towns where we work."),
                 actions=False) + f"""
<section class="sec"><div class="wrap">
  <div class="sitemap">{cards}</div>
  <p class="note">{t("Le site existe aussi en anglais :", "The website is also available in French:")} <a href="{url("plan", other)}" hreflang="{other}" lang="{other}">{t("English sitemap", "plan du site en français")}</a>. {t("Pour les moteurs de recherche et les assistants IA :", "For search engines and AI assistants:")} <a href="/sitemap.xml">sitemap.xml</a> · <a href="/llms.txt">llms.txt</a>.</p>
</div></section>"""
    return {"title": t("Plan du site | EdenFlats", "Sitemap | EdenFlats"),
            "desc": t("Plan du site EdenFlats : toutes les pages de la conciergerie Airbnb, services, formules, FAQ, quartiers de Paris, communes d'Île-de-France et informations légales.",
                      "EdenFlats sitemap: every page of our Airbnb management website, from services, plans and FAQ to Paris neighbourhoods, Île-de-France towns and legal pages."),
            "body": body, "ld": [crumbs_ld(L, trail)]}



def not_found(L):
    body = f"""<section class="phead"><div class="phead-panel panel"><div class="wrap phead-grid solo">
  <div>{chip("404")}<h1>Cette page <mark>n'existe pas</mark></h1>
  <p class="lead">Le lien est peut-être ancien. <span lang="en">This page doesn't exist: the link may be out of date.</span></p>
  <div class="cta-row">{btn("/", "Retour à l'accueil")}{btn("/en/", "English home page", "ghost")}</div></div>
</div></div></section>"""
    return {"title": "Page introuvable | EdenFlats", "desc": "Cette page n'existe pas.", "body": body, "ld": []}
