# Questions fréquentes, reprises de l'ancien site (doublons fusionnés).
# La réponse sur la législation a été mise à jour : l'ancienne datait de 2017 (120 jours partout),
# alors que Paris limite à 90 jours depuis le 1er janvier 2025 (loi Le Meur du 19 novembre 2024).

SP = "https://www.service-public.gouv.fr/particuliers/vosdroits/F2719"

ITEMS = {
    "tarifs": {
        "fr": ("Quels sont vos tarifs ?",
               "<p>Nous proposons deux formules :</p><ul>"
               "<li><b>Le contrat au revenu garanti</b> : selon vos dates, les caractéristiques de votre logement et le taux d'occupation moyen sur Airbnb, nous calculons un revenu qui vous est garanti et versé, que le logement soit loué ou non. Nous prenons en moyenne une marge de 15 %.</li>"
               "<li><b>Le contrat au revenu réel</b> : nous prenons une commission de 18 à 25 % sur les revenus générés par votre logement, selon la durée de la location. Plus le logement est loué, plus vous y gagnez ; s'il n'est pas loué, ce qui reste assez rare, vous ne touchez rien.</li></ul>"
               "<p>Avec le revenu réel, nous faisons varier le prix des nuits à la hausse ou à la baisse selon l'offre et la demande sur Airbnb, pour maximiser les chances de louer. Vous pouvez fixer un prix minimum par nuit, en dessous duquel nous ne descendrons pas.</p>"
               "<p><a href='{formules}'>Comparer les deux formules</a></p>"),
        "en": ("What are your fees?",
               "<p>We offer two plans:</p><ul>"
               "<li><b>The guaranteed-income contract</b>: based on your dates, your property and the average Airbnb occupancy rate, we calculate an income that is guaranteed and paid to you whether or not the apartment is booked. Our average margin is 15%.</li>"
               "<li><b>The actual-income contract</b>: we take a commission of 18% to 25% on the income your property generates, depending on the length of the rental. The more it is booked, the more you earn; if it is not booked, which is fairly rare, you receive nothing.</li></ul>"
               "<p>With actual income, we move nightly prices up or down with supply and demand on Airbnb to maximise bookings. You can set a minimum nightly price below which we will not go.</p>"
               "<p><a href='{formules}'>Compare the two plans</a></p>"),
    },
    "revenu": {
        "fr": ("Comment calculez-vous mon revenu ?",
               "<p>Le revenu de votre logement dépend de plusieurs facteurs : ses caractéristiques (adresse, nombre de couchages…), le nombre de nuits que vous souhaitez nous confier et le taux d'occupation moyen sur Airbnb à cette période. Ce taux est calculé par notre algorithme de tarification dynamique, à partir de l'offre et de la demande sur Airbnb. Vous choisissez ensuite entre <a href='{formules}'>un revenu garanti et un revenu réel</a>.</p>"),
        "en": ("How do you calculate my income?",
               "<p>Your income depends on several factors: the property itself (address, number of beds…), the number of nights you want to entrust to us and the average Airbnb occupancy rate for that period. That rate is calculated by our dynamic pricing algorithm, from supply and demand on Airbnb. You then choose between <a href='{formules}'>a guaranteed income and your actual income</a>.</p>"),
    },
    "gagner": {
        "fr": ("Combien puis-je espérer gagner ?",
               "<p>La rentabilité de votre logement dépend de nombreux paramètres : son emplacement, sa taille, sa qualité, la saison… Nous combinons des outils d'analyse et notre connaissance du marché local pour estimer vos gains. Après une évaluation détaillée de votre logement et de vos objectifs, nous vous remettons une projection réaliste et transparente de vos revenus. <a href='{contact}'>Demandez votre estimation</a>.</p>"),
        "en": ("How much can I expect to earn?",
               "<p>Your return depends on many things: location, size, quality, the season… We combine analysis tools with our knowledge of the local market to estimate your earnings. After a detailed assessment of your property and your goals, we give you a realistic, transparent projection of your income. <a href='{contact}'>Ask for your estimate</a>.</p>"),
    },
    "prix": {
        "fr": ("Comment le prix de mon logement est-il fixé ?",
               "<p>Nous utilisons des outils d'analyse qui suivent en temps réel les tendances du marché, la demande, les événements locaux et la saisonnalité. Nous les croisons avec notre connaissance du quartier et de votre logement pour fixer un prix compétitif, qui vise à la fois un bon taux d'occupation et de bons revenus.</p>"),
        "en": ("How is my nightly price set?",
               "<p>We use analysis tools that follow market trends, demand, local events and seasonality in real time. We combine them with our knowledge of the area and of your property to set a competitive price that aims for both good occupancy and good income.</p>"),
    },
    "prix-change": {
        "fr": ("Pourquoi le prix de mon logement change-t-il au cours de l'année ?",
               "<p>La demande varie avec les saisons, les vacances, les événements et les tendances touristiques. Avec la tarification dynamique, le prix monte quand la demande est forte et s'ajuste pour attirer des réservations pendant les périodes plus calmes. Cela aide à garder un bon taux d'occupation toute l'année tout en maximisant vos revenus.</p>"),
        "en": ("Why does my price change during the year?",
               "<p>Demand moves with the seasons, school holidays, events and travel trends. With dynamic pricing, the price rises when demand is high and adjusts to attract bookings in quieter periods. This helps keep occupancy high all year while maximising your income.</p>"),
    },
    "carte": {
        "fr": ("Proposez-vous une conciergerie à la carte ?",
               "<p>Oui. Chaque propriétaire a des besoins différents : vous pouvez nous confier la gestion complète de votre logement, ou seulement <a href='{logement}'>la maintenance, le ménage</a> ou <a href='{voyageurs}'>la gestion des réservations</a>.</p>"),
        "en": ("Can I choose only some services?",
               "<p>Yes. Every owner's needs are different: you can hand us full management of your property, or only <a href='{logement}'>maintenance, cleaning</a> or <a href='{voyageurs}'>bookings</a>.</p>"),
    },
    "pas-de-compte": {
        "fr": ("Je n'ai pas de compte Airbnb, que dois-je faire ?",
               "<p>Rien : vous n'avez pas besoin de créer de profil. Notre équipe s'occupe de toute <a href='{voyageurs}'>la création de l'annonce</a> et vous donne des conseils pour renforcer la confiance des futurs voyageurs.</p>"),
        "en": ("I don't have an Airbnb account. What do I need to do?",
               "<p>Nothing: you don't need to create a profile. Our team handles <a href='{voyageurs}'>the whole listing set-up</a> and gives you tips to build trust with future guests.</p>"),
    },
    "garder-compte": {
        "fr": ("Puis-je garder mon compte hôte Airbnb ?",
               "<p>Oui. Si vous avez déjà construit votre profil et vos commentaires sur Airbnb, vous les conservez : nous gérons vos réservations depuis ce compte, en veillant à maintenir et à améliorer votre réputation.</p>"),
        "en": ("Can I keep my Airbnb host account?",
               "<p>Yes. If you have already built your profile and reviews on Airbnb, you keep them: we manage your bookings from that account, taking care to maintain and improve your reputation.</p>"),
    },
    "acces-compte": {
        "fr": ("Puis-je toujours utiliser mon compte et voir mes réservations ?",
               "<p>Oui. Vous gardez un accès complet à votre compte Airbnb : réservations, commentaires des voyageurs et revenus, en temps réel. Pour éviter les conflits et les doubles réservations, signalez-nous simplement toute modification que vous souhaitez y faire.</p>"),
        "en": ("Can I still use my account and see my bookings?",
               "<p>Yes. You keep full access to your Airbnb account: bookings, guest reviews and income, in real time. To avoid conflicts and double bookings, just let us know about any change you want to make.</p>"),
    },
    "plateformes": {
        "fr": ("Sur quelles plateformes mon annonce est-elle publiée ?",
               "<p>Sur Airbnb, mais aussi sur Booking.com, Vrbo, Expedia et d'autres plateformes. Chacune attire des voyageurs différents : cette présence sur plusieurs canaux élargit votre public et augmente vos chances de réservation toute l'année.</p>"),
        "en": ("Which platforms is my listing published on?",
               "<p>On Airbnb, and also on Booking.com, Vrbo, Expedia and other platforms. Each one attracts different travellers: being on several channels widens your audience and increases your chances of bookings all year.</p>"),
    },
    "photos": {
        "fr": ("Qui prend les photos de mon annonce ?",
               "<p>Nous. La première impression est essentielle : nous photographions nous-mêmes votre logement pour en montrer les meilleurs angles et donner confiance aux voyageurs.</p>"),
        "en": ("Who takes the photos for my listing?",
               "<p>We do. First impressions matter: we photograph your property ourselves to show its best angles and build guests' trust.</p>"),
    },
    "langues": {
        "fr": ("En quelles langues mon annonce est-elle publiée ?",
               "<p>En général en français et en anglais, pour toucher une clientèle internationale.</p>"),
        "en": ("Which languages is my listing written in?",
               "<p>Usually French and English, to reach international travellers.</p>"),
    },
    "selection": {
        "fr": ("Sélectionnez-vous les voyageurs ?",
               "<p>Oui. Une équipe se consacre uniquement à la sélection, à la communication et à <a href=\"{voyageurs}\">la gestion des voyageurs</a>, pour que votre logement soit loué à des personnes de confiance. Nous examinons l'historique et les évaluations de chaque voyageur, et dialoguons souvent avec lui pour comprendre l'objet de son séjour. Un algorithme développé par nos soins nous aide aussi à les sélectionner selon des critères précis :</p><ul>"
               "<li>nous demandons l'âge et la raison de la réservation, en insistant pour les voyageurs sans commentaire ;</li>"
               "<li>nous privilégions les voyageurs avec des commentaires positifs et des profils vérifiés ;</li>"
               "<li>nous facilitons les réservations des familles ;</li>"
               "<li>une pièce d'identité est obligatoire pour réserver : l'identité de chaque voyageur est vérifiée.</li></ul>"),
        "en": ("Do you screen guests?",
               "<p>Yes. A dedicated team handles only guest screening, communication and <a href=\"{voyageurs}\">guest management</a>, so your property is let to people you can trust. We look at each guest's history and reviews, and often talk with them to understand the purpose of their stay. An algorithm we developed also helps us select guests against specific criteria:</p><ul>"
               "<li>we ask for their age and the reason for the booking, insisting with guests who have no reviews;</li>"
               "<li>we favour guests with positive reviews and verified profiles;</li>"
               "<li>we make bookings easier for families;</li>"
               "<li>an ID is required to book: every guest's identity is checked.</li></ul>"),
    },
    "reservations": {
        "fr": ("Comment mes réservations sont-elles gérées ?",
               "<p>Notre système se synchronise automatiquement avec toutes les plateformes où votre annonce est publiée : les calendriers sont à jour en temps réel, ce qui évite les doubles réservations. Notre équipe reste en contact avec les voyageurs, répond à leurs questions et leur donne toutes les informations avant leur arrivée. Pour l'arrivée, nous convenons de l'horaire avec eux et vérifions que le logement est impeccable. En cas d'imprévu, nous sommes disponibles pour régler le problème rapidement.</p>"),
        "en": ("How are my bookings managed?",
               "<p>Our system syncs automatically with every platform your listing is on, so calendars are up to date in real time and double bookings are avoided. Our team stays in touch with guests, answers their questions and sends them everything they need before arrival. For check-in, we agree the time with them and make sure the apartment is spotless. If anything unexpected happens, we are available to sort it out quickly.</p>"),
    },
    "annulation": {
        "fr": ("Que se passe-t-il quand des voyageurs annulent ?",
               "<p>Nous appliquons les conditions d'annulation strictes des plateformes pour limiter les annulations de dernière minute. Si une réservation est annulée, nous remettons aussitôt les dates en ligne et les mettons en avant pour retrouver des voyageurs ; grâce à notre présence sur plusieurs plateformes, c'est souvent possible en peu de temps.</p>"),
        "en": ("What happens when guests cancel?",
               "<p>We use the platforms' strict cancellation policies to limit last-minute cancellations. If a booking is cancelled, we put the dates back online straight away and promote them to find new guests; because we are on several platforms, this is often possible at short notice.</p>"),
    },
    "acces-logement": {
        "fr": ("Puis-je accéder à mon logement pendant le séjour d'un voyageur ?",
               "<p>Le logement vous appartient, mais la vie privée des voyageurs compte : nous vous demandons de nous prévenir avant toute visite pendant un séjour. En cas d'urgence, nous organisons la visite avec le voyageur pour qu'elle le dérange le moins possible.</p>"),
        "en": ("Can I visit my property while a guest is staying?",
               "<p>It is your home, but guests' privacy matters: please let us know before any visit during a stay. If it is urgent, we arrange the visit with the guest so that it disturbs them as little as possible.</p>"),
    },
    "cles": {
        "fr": ("Comment se passe la gestion des clés ?",
               "<p>Nous nous occupons de <a href=\"{voyageurs}\">la remise des clés</a> pendant toute la période de location confiée. Il nous faut deux jeux de clés : la veille de la location, vous déposez le premier dans l'un de nos cafés partenaires ; le second reste dans le logement, sur le plan de travail de la cuisine. Pendant la location, un jeu est confié à notre prestataire de ménage, l'autre aux voyageurs.</p>"
               "<p>Si vous le souhaitez, nous pouvons aussi ouvrir à distance, avec une serrure connectée ou une boîte à clés.</p>"),
        "en": ("How are the keys handled?",
               "<p>We look after <a href=\"{voyageurs}\">the key handover</a> for the whole rental period. We need two sets: the day before the rental, you drop the first one at one of our partner cafés; the second stays in the apartment, on the kitchen worktop. During the rental, one set goes to our cleaning provider and the other to the guests.</p>"
               "<p>If you prefer, we can also open remotely, with a smart lock or a key box.</p>"),
    },
    "menage": {
        "fr": ("Qu'est-ce qui est inclus dans le ménage ?",
               "<p>Le ménage comprend :</p><ul>"
               "<li>le nettoyage en profondeur de chaque pièce ;</li>"
               "<li>le lavage et le repassage des draps, des serviettes et du linge de maison ;</li>"
               "<li>le remplacement des consommables : shampoing, gel douche, papier toilette ;</li>"
               "<li>l'aération du logement ;</li>"
               "<li>la vérification du bon fonctionnement des appareils et des équipements.</li></ul>"
               "<p>Chaque nouveau voyageur entre ainsi dans un logement frais, propre et accueillant. Tout le détail sur <a href=\"{logement}\">la gestion du logement</a>.</p>"),
        "en": ("What does the cleaning include?",
               "<p>Cleaning includes:</p><ul>"
               "<li>a deep clean of every room;</li>"
               "<li>washing and ironing sheets, towels and household linen;</li>"
               "<li>restocking consumables: shampoo, shower gel, toilet paper;</li>"
               "<li>airing the apartment;</li>"
               "<li>checking that appliances and equipment work properly.</li></ul>"
               "<p>Every new guest walks into a fresh, clean and welcoming home. More on <a href=\"{logement}\">property management</a>.</p>"),
    },
    "dommages": {
        "fr": ("Quelles sont les procédures de dédommagement ?",
               "<p>En cas de dommage causé par un voyageur, nous le documentons avec des photos, une description détaillée et, si nécessaire, des devis de réparation. Nous engageons ensuite la demande de dédommagement auprès de la plateforme concernée ou de l'assurance du voyageur. À défaut d'accord à l'amiable, nous nous chargeons de toutes les démarches.</p>"),
        "en": ("How do damage claims work?",
               "<p>If a guest causes damage, we document it with photos, a detailed description and, where needed, repair quotes. We then file the claim with the platform concerned or the guest's insurer. If no amicable agreement is possible, we handle the whole procedure.</p>"),
    },
    "risques": {
        "fr": ("Quels sont les risques de la location courte durée ?",
               "<p>La location courte durée comporte des risques : dommages accidentels, différends avec des voyageurs ou périodes sans location. Nous les limitons en sélectionnant les voyageurs, en entretenant régulièrement le logement et en ajustant les prix pour maximiser l'occupation. Nous conseillons aussi à tous nos clients de souscrire une assurance adaptée à la location de courte durée.</p>"),
        "en": ("What are the risks of short-term letting?",
               "<p>Short-term letting carries risks: accidental damage, disputes with guests or empty periods. We limit them by screening guests, maintaining the property regularly and adjusting prices to maximise occupancy. We also advise all our clients to take out insurance suited to short-term rentals.</p>"),
    },
    "legislation": {
        "fr": ("Quelle est la législation Airbnb en France ?",
               "<p>Les règles dépendent de la commune et de votre situation. Les principales :</p><ul>"
               "<li><b>Résidence principale</b> : vous pouvez la louer en meublé de tourisme 120 jours par an au maximum. Les communes peuvent abaisser ce plafond : à Paris, il est de 90 jours depuis le 1er janvier 2025.</li>"
               "<li><b>Déclaration</b> : dans les communes qui l'exigent, comme Paris, le logement doit être déclaré en mairie et son numéro d'enregistrement affiché sur chaque annonce.</li>"
               "<li><b>Résidence secondaire ou bien locatif</b> : à Paris, en petite couronne et dans d'autres communes, le louer de façon répétée pour de courtes durées demande en général une autorisation de changement d'usage.</li>"
               "<li><b>Locataire</b> : il vous faut l'accord écrit de votre propriétaire pour sous-louer.</li></ul>"
               f'<p>Ces règles évoluent : vérifiez celles qui s\'appliquent à votre logement (voir aussi <a href="{{paris}}">les règles à Paris</a>) auprès de votre mairie ou sur <a href="{SP}" target="_blank" rel="noopener">service-public.gouv.fr</a> avant de le mettre en location.</p>'),
        "en": ("What are the rules for Airbnb in France?",
               "<p>The rules depend on the town and on your situation. The main ones:</p><ul>"
               "<li><b>Main residence</b>: you can let it as furnished tourist accommodation for up to 120 days a year. Towns can lower this cap: in Paris it has been 90 days since 1 January 2025.</li>"
               "<li><b>Registration</b>: in towns that require it, including Paris, the property must be declared to the town hall and its registration number shown on every listing.</li>"
               "<li><b>Second home or buy-to-let</b>: in Paris, the inner suburbs and other towns, letting it repeatedly for short stays generally requires a change-of-use authorisation.</li>"
               "<li><b>Tenants</b>: you need your landlord's written consent to sublet.</li></ul>"
               f'<p>These rules change: check the ones that apply to your property (see also <a href="{{paris}}">the Paris rules</a>) with your town hall or on <a href="{SP}" target="_blank" rel="noopener">service-public.gouv.fr</a> (in French) before you start letting it.</p>'),
    },
}

GROUPS = [
    ("Formules et revenus", "Plans and income", ["tarifs", "revenu", "gagner", "prix", "prix-change", "carte"]),
    ("Votre annonce et votre compte Airbnb", "Your listing and Airbnb account",
     ["pas-de-compte", "garder-compte", "acces-compte", "plateformes", "photos", "langues"]),
    ("Voyageurs et réservations", "Guests and bookings", ["selection", "reservations", "annulation", "acces-logement"]),
    ("Clés, ménage et entretien", "Keys, cleaning and upkeep", ["cles", "menage", "dommages", "risques"]),
    ("Réglementation", "Regulations", ["legislation"]),
]


def links(html, L):
    from kit import url
    for key in ("formules", "contact", "logement", "voyageurs", "paris", "faq"):
        html = html.replace("{" + key + "}", url(key, L))
    return html


def pick(L, ids):
    return [(q, links(a, L)) for q, a in (ITEMS[i][L] for i in ids)]
