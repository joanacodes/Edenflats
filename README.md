# EdenFlats — site web

Site statique en français pour EdenFlats (EF Group), conciergerie Airbnb à Paris et en Île-de-France. Il remplace le site Squarespace. **Ce qui est dans le dépôt est le site** : aucun build côté hébergeur, il se publie tel quel (GitHub Pages, Cloudflare Pages…).

## Pages

- `/` accueil
- `/gestion-des-voyageurs/` et `/gestion-du-logement/`
- `/faq/`
- `/conciergerie-airbnb-creteil/` et `/conciergerie-airbnb-saint-maur-des-fosses/`
- `/contact/`
- `404.html`, `sitemap.xml`, `robots.txt`

## Modifier le site

Les pages sont produites par `_generator/build.py` (Python, sans dépendance). Il réécrit tous les HTML : modifiez les textes dans `build.py`, pas dans les HTML.

```powershell
cd _generator
py build.py
cd ..
py -m http.server 8001   # puis http://localhost:8001
```

Les couleurs et les polices sont dans `assets/style.css`, bloc `:root`.

## À compléter avant la mise en ligne

Le site a été écrit sans accès au site Squarespace actuel. Les textes viennent de la description du projet ; ce qui suit n'a pas pu être repris et doit l'être :

- **Coordonnées** : téléphone, WhatsApp et e-mail, dans le bloc `SITE` de `build.py`. Tant qu'elles sont vides, la page Contact affiche « à compléter ».
- **FAQ** : les réponses sur le contrat, la tarification et l'accès au compte Airbnb sont volontairement générales. Les remplacer par celles du site actuel (liste `FAQ`).
- **Secteurs** : seules Créteil et Saint-Maur-des-Fossés ont une page. Ajouter les autres communes du site actuel (liste `TOWNS` et un appel à `town(...)`).
- **Mentions légales et politique de confidentialité** : pages à créer avec les informations de la société.
- **Couleurs** : la palette (bleu nuit, bleu pervenche, vert tendre, crème) vient de la maquette de référence ; celles de bridgeapi.io n'ont pas pu être relevées.
- **Redirections** : relever les adresses des pages Squarespace et les rediriger vers les nouvelles avant de changer le domaine.

## Images

`assets/img/*.svg` sont des illustrations provisoires, dessinées par `_generator/illustrations.py`. Pour mettre de vraies photos, déposez-les dans `assets/img/` et remplacez les noms `salon.svg`, `facade.svg`, `cles.svg`, `linge.svg`, `marne.svg`, `accueil.svg` dans `build.py`.
