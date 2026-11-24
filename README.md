# EdenFlats — site web

Site statique bilingue de la conciergerie Airbnb EdenFlats (Paris et Île-de-France), qui remplace le site Squarespace. Français à la racine, anglais sous `/en/`. **Ce qui est dans le dépôt est le site** : il se publie tel quel, sans étape de build chez l'hébergeur.

Couleurs, polices (Bricolage Grotesque, Public Sans) et cartes blanches posées sur les photos reprennent le style de bridgeapi.io ; les textes, la FAQ et les formules viennent de l'ancien site edenflats.com.

## Pages (48, dans les deux langues)

| Français | Anglais |
|---|---|
| `/` | `/en/` |
| `/gestion-des-voyageurs-conciergerie-airbnb-ile-de-france/` | `/en/guest-management/` |
| `/gestion-de-propriete-conciergerie-airbnb-ile-de-france/` | `/en/property-management/` |
| `/nos-formules/` | `/en/plans/` |
| `/faq/` | `/en/faq/` |
| `/conciergerie-airbnb-paris/` et 12 quartiers (`/conciergerie-airbnb-paris/le-marais/`…) | `/en/airbnb-management-paris/` et 12 quartiers |
| `/conciergerie-airbnb-creteil/`, `/conciergerie-airbnb-saint-maur-des-fosses/` | `/en/airbnb-management-creteil/`, `/en/airbnb-management-saint-maur-des-fosses/` |
| `/contact/`, `/mentions-legales/`, `/confidentialite/`, `/credits-photos/` | `/en/contact/`, `/en/legal-notice/`, `/en/privacy/`, `/en/photo-credits/` |

Quartiers : Le Marais, Montmartre, Saint-Germain-des-Prés, Quartier latin, Tour Eiffel, Champs-Élysées, Opéra, Louvre, Canal Saint-Martin, Bastille, Montparnasse, Trocadéro.

Les adresses françaises de l'ancien site sont gardées. Celles qui n'ont plus d'équivalent (`/accueil`, `/conditions-generales-de-vente`, `/politique-de-cookies`, `/boutique`, `/erreur-404`) redirigent vers la page la plus proche. `sitemap.xml` relie chaque page à sa traduction (hreflang).

## Modifier le site

Les pages sont produites par `_generator/` (Python 3 et Pillow). Il réécrit tous les HTML : modifiez les textes dans le générateur, pas dans les HTML.

- `kit.py` : coordonnées et informations légales (bloc `SITE`), adresses des pages, gabarit, en-tête et pied de page.
- `pages.py` : accueil, gestion des voyageurs et du logement, formules, FAQ, contact, pages légales. Chaque texte est écrit `t("français", "English")`.
- `quartiers.py` : les 12 quartiers, Créteil et Saint-Maur, la page Paris.
- `faq.py` : les questions et réponses.
- `photos.py` : photos des quartiers, avec auteur et licence.

```powershell
cd _generator
py -m pip install pillow   # une seule fois
py build.py
cd ..
py -m http.server 8001     # puis http://localhost:8001
```

Les couleurs et les polices sont dans `assets/style.css`, bloc `:root`.

## Mise en ligne

Pensé pour GitHub Pages avec le domaine `www.edenflats.com` (les liens commencent par `/`, le site doit donc être servi à la racine d'un domaine). Au moment de quitter Squarespace : ajouter un fichier `CNAME` contenant `www.edenflats.com`, activer Pages sur la branche, puis faire pointer le DNS vers GitHub. Si le site est hébergé ailleurs, changer `SITE["host"]` dans `kit.py` (mentions légales).

## À vérifier avant la mise en ligne

- **Société éditrice.** Les mentions légales citent la société du SIRET fourni, 104 632 591 00012 : EDENEL PATRIMOINE GESTION RESEAUX & SERVICES (EPGRS), SAS, 14 rue de Champigny, Sucy-en-Brie, présidente Flore Hountondji. L'ancien site citait une autre société, EDEN-FLATS SAS (SIREN 851 967 984, nom commercial EF CONCIERGERIE, siège transféré à Thiais). Confirmer laquelle exploite EdenFlats.
- **À compléter dans `SITE["company"]`** (affichés « à compléter » en attendant) : capital social, immatriculation RCS (en principe RCS Créteil, à lire sur le Kbis), numéro de TVA (le calcul à partir du SIREN donne FR62104632591, à confirmer).
- **Loi Hoguet.** Si la société encaisse des loyers pour le compte des propriétaires, les mentions légales doivent indiquer la carte professionnelle (numéro, CCI) et la garantie financière.
- **Coordonnées.** Le site utilise edenflats.paris@gmail.com et +33 7 84 54 48 61 (WhatsApp sur le même numéro, comme sur l'ancien site). L'ancien site affichait aussi info@edenflats.com, contact@edenflats.com (adresse réelle du lien « e-mail ») et +33 1 83 73 95 96.
- **Avis clients.** Les six témoignages de l'ancien site n'ont pas été repris : leurs photos sont des photos de banque d'images et un nom ne correspond pas à sa photo. Publier de faux avis est une pratique commerciale trompeuse ; on peut ajouter de vrais avis, avec l'accord des clients.
- **CGV.** Non reprises : l'ancien texte contient des trous (« [X] heures », « [Nom de la conciergerie] ») et l'ancien nom de société. À compléter puis à ajouter.
- **Législation.** La réponse de la FAQ a été mise à jour (Paris : 90 jours par an depuis le 1er janvier 2025, loi Le Meur). À relire par la cliente.
- **Dédommagement.** « Si un accord à l'amiable n'est pas possible, nous prenons tout en charge » est devenu « nous nous chargeons de toutes les démarches », pour ne pas promettre de payer les dégâts, ce que les CGV excluent.
- **Mesure d'audience.** L'ancien site déclarait Google Analytics et Microsoft Clarity. Le nouveau n'a ni cookie ni traceur ; en ajouter demande un bandeau de consentement et une mise à jour de la page Confidentialité.

## Images

- Photos d'intérieurs et objets détourés (`photo-*.jpg`, `objet-*.webp`) : reprises de l'ancien site. Plusieurs sont des photos de banque d'images (Pexels, Unsplash, libres de droits) ; vérifier la licence des autres, car les images achetées via Squarespace (Getty) ne peuvent pas servir ailleurs. L'idéal : de vraies photos des logements gérés, en gardant les mêmes noms de fichiers (1600 px, plus une copie de 800 px suffixée `-800`).
- Photos des quartiers (`paris-*.jpg`, `ville-*.jpg`) : Wikimedia Commons, licences CC BY et CC BY-SA. L'auteur et la licence s'affichent sous chaque photo et sur la page Crédits photos ; ne pas les retirer.
- Polices : Bricolage Grotesque et Public Sans, licence SIL Open Font License 1.1 (fichiers de licence dans `assets/fonts/`).
