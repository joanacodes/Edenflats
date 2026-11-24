# EdenFlats — site web

Site statique bilingue de la conciergerie Airbnb EdenFlats (Paris et Île-de-France), qui remplace le site Squarespace. Français à la racine, anglais sous `/en/`. **Ce qui est dans le dépôt est le site** : il se publie tel quel.

Éditeur : EDENEL PATRIMOINE GESTION RESEAUX & SERVICES (EPGRS), SAS, 14 rue de Champigny, 94370 Sucy-en-Brie, SIRET 104 632 591 00012.

## Identité visuelle

Une palette chaude qui réunit l'ancien site (crème, ardoise, vert tendre, corail), la pervenche de la maquette de référence et la construction de Bridge : des familles de couleurs claires, chacune avec sa couleur foncée pour le texte et les illustrations, des cartes blanches posées sur les photos, des panneaux arrondis qui se chevauchent.

| Rôle | Couleur |
|---|---|
| Texte, boutons, bandeaux sombres (ardoise de l'ancien site) | `#24485C` |
| Fond des panneaux (crème de l'ancien site) | `#FBF2E8` |
| Famille verte (vert de l'ancien site) | `#B9E89A`, fond `#E9F6DA`, texte `#1D4A35` |
| Famille bleue (pervenche de la maquette) | `#A9C2FF`, fond `#E1E8FF`, texte `#233B7A` |
| Famille corail (corail de l'ancien site, à la place du rose de Bridge) | `#FC585C`, fond `#FFE4DD`, texte `#8E2A24` |
| Famille sable | `#EFD3B2`, fond `#F7EADB`, texte `#6B4423` |
| Surlignage des titres | `#FFC6BA` |

Polices : Bricolage Grotesque (titres) et Public Sans (texte), hébergées sur le site (licence SIL OFL).

Illustrations : 21 dessins au trait dans l'esprit de Bridge, regroupés dans `assets/illus.svg` (calendrier, porte, ménage, linge, outils, casque 24/7, balance, services à la carte, clés, serrure connectée, appareil photo, langues FR/EN, pièce d'identité, valise, maison et revenus, graphique, café-croissant, lampe, rouleau, téléphone, tour Eiffel). Ils prennent la couleur de leur carte. Ils se modifient dans `_generator/illus.py`.

## Pages et adresses

Les adresses françaises de l'ancien site sont reprises **à l'identique** (sans barre finale) : chaque page est un fichier `.html` que GitHub Pages sert sans l'extension (`/faq` sert `faq.html`).

| Page | Français | Anglais |
|---|---|---|
| Accueil | `/` | `/en/` |
| Gestion des voyageurs | `/gestion-des-voyageurs-conciergerie-airbnb-ile-de-france` (ancienne adresse) | `/en/guest-management` |
| Gestion de propriété | `/gestion-de-propriete-conciergerie-airbnb-ile-de-france` (ancienne adresse) | `/en/property-management` |
| Formules | `/nos-formules` | `/en/plans` |
| FAQ | `/faq` (ancienne adresse) | `/en/faq` |
| Paris | `/conciergerie-airbnb-paris` | `/en/airbnb-management-paris` |
| 12 quartiers | `/conciergerie-airbnb-le-marais`, `-montmartre`, `-saint-germain-des-pres`, `-quartier-latin`, `-tour-eiffel`, `-champs-elysees`, `-opera`, `-louvre`, `-canal-saint-martin`, `-bastille`, `-montparnasse`, `-trocadero` | `/en/airbnb-management-le-marais`… (`latin-quarter`, `eiffel-tower`) |
| Créteil, Saint-Maur | `/conciergerie-airbnb-creteil`, `/conciergerie-airbnb-saint-maur-des-fosses` (anciennes adresses) | `/en/airbnb-management-creteil`, `/en/airbnb-management-saint-maur-des-fosses` |
| Contact | `/contact` (ancienne adresse) | `/en/contact` |
| Mentions légales | `/mentions-legales` (ancienne adresse) | `/en/legal-notice` |
| Confidentialité et cookies | `/politique-de-cookies` (ancienne adresse) | `/en/privacy` |
| Crédits photos | `/credits-photos` | `/en/photo-credits` |

Anciennes adresses sans équivalent, redirigées : `/accueil` → `/`, `/conditions-generales-de-vente` → `/mentions-legales`, `/boutique` → `/`, `/erreur-404` → `/`. Sur GitHub Pages, ce sont des pages qui redirigent aussitôt ; le fichier `_redirects` donne de vraies redirections 301 sur Cloudflare Pages ou Netlify.

## Référencement

- **Titres et descriptions** écrits page par page autour des mots-clés ci-dessous ; le générateur signale tout titre de plus de 65 caractères et toute description hors de 110–170.
- **Données structurées** (JSON-LD) : l'entreprise (`ProfessionalService` avec adresse, zones desservies, SIRET), le site, un `Service` par page de service et par quartier, la FAQ (`FAQPage`), le fil d'Ariane sur chaque page.
- **Partage** : chaque page a sa propre image (photo du quartier, photo de la page), son texte alternatif, les balises Open Graph et Twitter, la langue et sa variante.
- **Maillage interne** : chaque quartier renvoie aux services, aux formules, à la FAQ, à la page Paris et à ses voisins ; les pages de services ont un bloc « Où nous intervenons » vers tous les quartiers ; les réponses de la FAQ renvoient aux pages concernées ; le pied de page liste tous les quartiers.
- **Plan du site** `sitemap.xml` : toutes les pages, date de mise à jour, traduction de chaque page (hreflang) et image principale.
- **Pour les assistants IA** : `llms.txt` (résumé du site, informations clés et liste commentée des pages) et `llms-full.txt` (FAQ complète et textes des quartiers, en français et en anglais).
- `robots.txt` ouvre tout le site et indique le plan du site.

| Page | Mots-clés visés (FR) | Keywords (EN) |
|---|---|---|
| Accueil | conciergerie Airbnb Paris, conciergerie Airbnb Île-de-France, gestion locative saisonnière | Airbnb management Paris, short-term rental management Paris |
| Gestion des voyageurs | gestion des voyageurs Airbnb, accueil voyageurs, remise des clés Airbnb | Airbnb guest management Paris, Airbnb check-in |
| Gestion de propriété | ménage Airbnb Paris, gestion de propriété Airbnb, blanchisserie location saisonnière | Airbnb cleaning Paris, Airbnb property management |
| Formules | tarif conciergerie Airbnb, commission conciergerie Airbnb, revenu garanti | Airbnb management fees, guaranteed income |
| FAQ | législation Airbnb Paris, 90 jours, compte Airbnb | Paris Airbnb rules |
| Paris | conciergerie Airbnb Paris, réglementation location courte durée Paris | Airbnb management Paris |
| Quartiers | conciergerie Airbnb + quartier et arrondissement (Marais, Paris 3e…) | Airbnb management + neighbourhood |
| Communes | conciergerie Airbnb Créteil, conciergerie Airbnb Saint-Maur-des-Fossés | Airbnb management Créteil, Saint-Maur |

## Modifier le site

Le site est produit par `_generator/` (Python 3 et Pillow). Il réécrit tous les HTML : modifiez les textes dans le générateur, pas dans les HTML.

- `kit.py` : coordonnées et informations légales (bloc `SITE`), adresses des pages, gabarit, en-tête, pied de page, données structurées.
- `pages.py` : accueil, gestion des voyageurs et du logement, formules, FAQ, contact, pages légales. Chaque texte est écrit `t("français", "English")`.
- `quartiers.py` : les 12 quartiers, Créteil, Saint-Maur et la page Paris.
- `faq.py` : questions et réponses ; `{formules}`, `{voyageurs}`… deviennent des liens vers ces pages.
- `illus.py` : les illustrations. `photos.py` : photos des quartiers, avec auteur et licence.

```powershell
cd _generator
py -m pip install pillow   # une seule fois
py build.py                # génère le site
py serve.py                # aperçu sur http://localhost:8001
```

Les couleurs et les polices sont dans `assets/style.css`, bloc `:root`.

## Images (Midjourney)

`IMAGES-MIDJOURNEY.md` donne un prompt à copier-coller pour chaque emplacement photo, avec son nom de fichier et son format. Déposez les images dans `_generator/sources/`, lancez `py images.py` (recadrage et deux tailles), puis `py build.py`.

En attendant, les emplacements montrent les photos de l'ancien site (photos de banque d'images). Les quartiers utilisent de vraies photos de Wikimedia Commons, créditées sous chaque photo et sur la page Crédits photos.

## Mise en ligne

Pensé pour GitHub Pages avec le domaine `www.edenflats.com` (les liens commencent par `/`, le site doit donc être servi à la racine du domaine). Au moment de quitter Squarespace : ajouter un fichier `CNAME` contenant `www.edenflats.com`, activer Pages sur la branche, puis faire pointer le DNS vers GitHub. `_config.yml` empêche Jekyll de publier le générateur et les fichiers de travail. Si le site est hébergé ailleurs, changer `SITE["host"]` dans `kit.py` (mentions légales).

## À vérifier avant la mise en ligne

- **Mentions légales** : capital social, immatriculation RCS (en principe RCS Créteil, à lire sur le Kbis) et numéro de TVA (le calcul à partir du SIREN donne FR62104632591, à confirmer) sont affichés « à compléter » ; les renseigner dans `SITE["company"]`.
- **Loi Hoguet** : si la société encaisse des loyers pour le compte des propriétaires, indiquer la carte professionnelle (numéro, CCI) et la garantie financière.
- **Coordonnées** : le site utilise edenflats.paris@gmail.com et +33 7 84 54 48 61 (WhatsApp sur le même numéro). L'ancien site affichait aussi info@edenflats.com, contact@edenflats.com et +33 1 83 73 95 96.
- **Avis clients** : les six témoignages de l'ancien site ne sont pas repris (photos de banque d'images, un nom qui ne correspond pas à sa photo). De vrais avis peuvent être ajoutés, avec l'accord des clients.
- **CGV** : non reprises (texte à trous et ancien nom de société) ; `/conditions-generales-de-vente` redirige vers les mentions légales en attendant.
- **FAQ** : la réponse sur la législation a été mise à jour (Paris : 90 jours par an depuis le 1er janvier 2025) ; « nous prenons tout en charge » (dédommagement) est devenu « nous nous chargeons de toutes les démarches ».
- **Mesure d'audience** : le site n'a ni cookie ni traceur ; en ajouter demande un bandeau de consentement et une mise à jour de la page Confidentialité.
