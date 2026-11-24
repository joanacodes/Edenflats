# EdenFlats — site web

Site statique bilingue de la conciergerie Airbnb EdenFlats (Paris et Île-de-France), qui remplace le site Squarespace. Français à la racine, anglais sous `/en/`. **Ce qui est dans le dépôt est le site** : il se publie tel quel.

Éditeur : EDENEL PATRIMOINE GESTION RESEAUX & SERVICES (EPGRS), SAS, 14 rue de Champigny, 94370 Sucy-en-Brie, SIRET 104 632 591 00012.

Coordonnées (confirmées) : edenflats.paris@gmail.com, +33 7 84 54 48 61, et WhatsApp sur le même numéro, comme sur l'ancien site.

## Identité visuelle

**Version « maquette »** (branche `claude/edenflats-layout-template`) : la mise en page de la maquette de référence, section par section, avec le contenu d'EdenFlats. La version précédente, plus proche de Bridge, est sur la branche `claude/edenflats-website-redesign-4i4x4w` ; les deux partagent les mêmes pages, adresses, textes et photos.

| Rôle | Couleur |
|---|---|
| En-tête, textes, sections sombres (bleu nuit de la maquette) | `#1B1B4B` |
| Héros, en-têtes de pages, pied de page (pervenche) | `#A9C2FF` |
| Cartes, étiquettes, pictogrammes sur bleu nuit (vert anis) | `#E4FBC0` |
| Panneaux (crème de l'ancien site, à la place du beige de la maquette) | `#FBF2E8` |
| Point du logo (corail de l'ancien site) | `#FC585C` |

Polices : Public Sans (titres et texte) et Instrument Serif (mots en italique dans les titres, titres des cartes), hébergées sur le site (licence SIL OFL). Sections à angles droits, une grande courbe par photo, boutons en pilule.

Illustrations : 21 dessins au trait dans `assets/illus.svg` (calendrier, porte, ménage, linge, outils, casque 24/7, balance, services à la carte, clés, serrure connectée, appareil photo, langues FR/EN, pièce d'identité, valise, maison et revenus, graphique, café-croissant, lampe, rouleau, téléphone, tour Eiffel). Ils prennent la couleur de leur carte ; ils se modifient dans `_generator/illus.py`.

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
| Conditions générales de vente | `/conditions-generales-de-vente` (ancienne adresse) | `/en/terms-and-conditions` |
| Confidentialité et cookies | `/politique-de-cookies` (ancienne adresse) | `/en/privacy` |
| Plan du site | `/plan-du-site` | `/en/sitemap` |

Anciennes adresses sans équivalent, redirigées : `/accueil` → `/`, `/boutique` → `/`, `/erreur-404` → `/`. Sur GitHub Pages, ce sont des pages qui redirigent aussitôt ; le fichier `_redirects` donne de vraies redirections 301 sur Cloudflare Pages ou Netlify.

## Sur toutes les pages

- **En-tête en verre dépoli** : translucide, la page se devine floutée dessous quand on défile. Sur téléphone, il devient une barre arrondie qui flotte au-dessus de la page, et le menu s'ouvre en verre lui aussi.
- **Bouton « Nous contacter »** en bas à droite de l'écran (comme sur mlkwebstudio.fr) : il arrive une fois le haut de page passé, repart quand l'appel final ou le pied de page arrive, et n'existe pas sur la page Contact.
- **Langue** : une page française ouverte par un navigateur qui n'est pas en français propose la version anglaise de la même page (« It looks like you don't speak French… »), et une page anglaise ouverte par un navigateur en français propose la version française. Jamais de redirection automatique ; le choix est retenu et n'est plus demandé.
- **Bandeau cookies** : « Refuser » et « Accepter » ont le même poids, comme le demande la CNIL ; le choix est gardé six mois ; « Gérer les cookies » (pied de page et page Confidentialité) rouvre le bandeau. S'il y a aussi la proposition de langue, le bandeau attend la réponse, pour s'afficher dans la langue choisie.
- **Mesure d'audience** : Google Analytics 4 ne se charge qu'après « Accepter », et seulement quand `SITE["analytics"]["ga4"]` contient l'identifiant (ex. `G-ABC123XYZ9`). Ses cookies sont limités à treize mois ; un refus efface ceux déjà déposés. Changer d'identifiant redemande l'accord.
- **Réseaux sociaux** : Instagram, Facebook, LinkedIn et YouTube dans le pied de page et sur la page Contact. Les adresses se renseignent dans `SITE["social"]` (`kit.py`) ; tant qu'une adresse est vide, l'icône s'affiche sans lien et n'est pas déclarée aux moteurs de recherche. TikTok est prêt, en commentaire.

## Référencement

- **Titres et descriptions** écrits page par page autour des mots-clés ci-dessous ; le générateur signale tout titre de plus de 65 caractères et toute description hors de 110–170.
- **Données structurées** (JSON-LD) : l'entreprise (`ProfessionalService` avec adresse, zones desservies, SIRET), le site, un `Service` par page de service et par quartier, la FAQ (`FAQPage`), le fil d'Ariane sur chaque page.
- **Partage** : chaque page a sa propre image (photo du quartier, photo de la page), son texte alternatif, les balises Open Graph et Twitter, la langue et sa variante.
- **Maillage interne** : chaque quartier renvoie aux services, aux formules, à la FAQ, à la page Paris et à ses voisins ; les pages de services ont un bloc « Où nous intervenons » vers tous les quartiers ; les réponses de la FAQ renvoient aux pages concernées ; le pied de page liste tous les quartiers.
- **Plan du site** `sitemap.xml` : toutes les pages, date de mise à jour, traduction de chaque page (hreflang) et image principale. La page `/plan-du-site` (et `/en/sitemap`) relie aussi toutes les pages pour les visiteurs.
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

- `kit.py` : coordonnées, informations légales, réseaux sociaux et mesure d'audience (bloc `SITE`), adresses des pages, gabarit, en-tête, pied de page, bandeau cookies, proposition de langue, données structurées.
- `pages.py` : accueil, gestion des voyageurs et du logement, formules, FAQ, contact, pages légales (mentions, CGV, confidentialité, crédits) et plan du site. Chaque texte est écrit `t("français", "English")`.
- `assets/main.js` : menu, bouton de contact, bandeau cookies et chargement de Google Analytics, proposition de langue.
- `quartiers.py` : les 12 quartiers, Créteil, Saint-Maur et la page Paris.
- `faq.py` : questions et réponses ; `{formules}`, `{voyageurs}`… deviennent des liens vers ces pages.
- `illus.py` : les illustrations. `photos.py` : photos de la page Paris, des quartiers et des communes (nom de fichier et texte alternatif). `placeholders.py` : cadres « Photo à venir ».

```powershell
cd _generator
py -m pip install pillow   # une seule fois
py build.py                # génère le site
py serve.py                # aperçu sur http://localhost:8001
```

Les couleurs et les polices sont dans `assets/style.css`, bloc `:root`.

## Images (Midjourney)

Toutes les photos du site sont des images Midjourney faites par MLK Web Studio : 27 emplacements, un prompt chacun dans `IMAGES-MIDJOURNEY.md` (nom de fichier, page, section, format). Elles montrent des voyageurs, des propriétaires, l'équipe au travail et des appartements, jamais un monument ni une rue réelle. Déposez les images dans `_generator/sources/`, lancez `py images.py` (recadrage et deux tailles), puis `py build.py`.

En attendant, les pages principales montrent les photos de l'ancien site, et la page Paris, les quartiers et les communes un cadre « Photo à venir » qui porte le nom du fichier attendu. Les textes alternatifs décrivent déjà ce que montrent les prompts : si une image s'en écarte, corrigez-le (`pages.py` pour les pages principales, `photos.py` pour les quartiers).

## Mise en ligne

Le dépôt est privé : GitHub Pages n'y est disponible qu'avec un compte GitHub payant, et servirait le site sous `/Edenflats/`, que les liens (qui commencent par `/`) ne gèrent pas. Le site est prêt pour **Vercel** :

1. vercel.com/new → importer `joanacodes/Edenflats` (préréglage « Other », aucune commande de build) → Deploy.
2. Dans le projet : Settings → Git (ou Environments → Production) → branche de production `claude/edenflats-website-redesign-4i4x4w` (ou fusionner cette branche dans `main`), puis redéployer.

`vercel.json` sert les pages sans « .html », reprend les redirections des anciennes adresses et demande aux moteurs de ne pas indexer les adresses en `.vercel.app` ; `.vercelignore` ne publie pas le générateur. Pour la mise en ligne définitive : ajouter le domaine `www.edenflats.com` dans Vercel, faire pointer le DNS, et mettre l'hébergeur à jour dans `SITE["host"]` (`kit.py`, mentions légales : Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, USA). Sur Netlify ou Cloudflare Pages, `_redirects` donne les mêmes redirections ; sur GitHub Pages avec le domaine, `_config.yml` empêche Jekyll de publier le générateur.

## À vérifier avant la mise en ligne

- **Mentions légales** : capital social, immatriculation RCS (en principe RCS Créteil, à lire sur le Kbis) et numéro de TVA (le calcul à partir du SIREN donne FR62104632591, à confirmer) sont affichés « à compléter » ; les renseigner dans `SITE["company"]`.
- **Loi Hoguet** : si la société encaisse des loyers pour le compte des propriétaires, indiquer la carte professionnelle (numéro, CCI) et la garantie financière.
- **Avis clients** : les six témoignages de l'ancien site ne sont pas repris (photos de banque d'images, un nom qui ne correspond pas à sa photo). De vrais avis peuvent être ajoutés, avec l'accord des clients.
- **CGV** : reprises de l'ancien site (version du 7 avril 2025) sous le nom de la société, avec les trous comblés quand l'information était connue. Restent en cadre pointillé : le délai de confirmation et d'annulation (« [nombre] heures », deux fois), l'assureur de la responsabilité civile professionnelle et le médiateur de la consommation (obligatoire dès qu'on a des clients particuliers). Ajoutés, à faire valider par un juriste : droit de rétractation de quatorze jours pour un particulier qui signe à distance (lui remettre aussi le formulaire type de rétractation avec le contrat), médiation, pénalités de retard pour les clients professionnels, et tribunaux (l'ancien texte attribuait les litiges aux « tribunaux de Sucy-en-Brie », clause sans effet face à un particulier). Mettre à jour `CGV_MAJ` (`pages.py`) une fois le texte validé.
- **FAQ** : la réponse sur la législation a été mise à jour (Paris : 90 jours par an depuis le 1er janvier 2025) ; « nous prenons tout en charge » (dédommagement) est devenu « nous nous chargeons de toutes les démarches ».
- **Mesure d'audience** : le bandeau cookies est en place et demande l'accord pour Google Analytics, mais aucun identifiant GA4 n'est encore renseigné : rien n'est mesuré. Soit renseigner `SITE["analytics"]["ga4"]`, soit, si EdenFlats ne veut pas de mesure d'audience, mettre `SITE["cookie_banner"]` à `False` : le bandeau disparaît (il n'est alors plus nécessaire) et la politique de confidentialité s'adapte.
- **Réseaux sociaux** : renseigner les adresses des pages dans `SITE["social"]`.
