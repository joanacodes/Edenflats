# Pictures for the EdenFlats website (Midjourney)

**The prompts are in `IMAGES-MIDJOURNEY-BATCHES.md`**, grouped for Midjourney batches (at most 3 grids per prompt), in the order to make them. They aim for realistic, lived-in pictures rather than glossy ones, with people of the many backgrounds you meet in France. The people are invented: never present them as the EdenFlats team or as real clients.

**29 picture spots**: 27 used by both versions, and 2 used only by version B (the template version, published in `maquette/`). Until a picture arrives, the main pages show the old site's photos and the other spots a « Photo à venir » frame with the file name.

| File name | Version A (current) | Version B (template) | Format |
|---|---|---|---|
| `accueil-hero` | Home, top | Home, photo grid | 4:5 |
| `voyageurs-hero` | Guest management, top | Same, and the tall photo of the home grid | 4:5 |
| `logement-hero` | Property management, top | Same, and the home « Pour les propriétaires » card | 4:5 |
| `formules-hero` | Plans, top | Same, and the home plans carousel | 4:5 |
| `accueil-voyageurs` | Home, « Des voyageurs choisis avec soin » | Home, photo grid | 6:5 |
| `accueil-logement` | Home, « Votre bien entre de bonnes mains » | Home, « Tout savoir » panel | 6:5 |
| `accueil-faq` | Home, questions | Home, contact card | 6:5 |
| `voyageurs-annonce` | Guest management, the listing | Same, and the home services grid | 6:5 |
| `voyageurs-selection` | Guest management, guest screening | Same, and the home questions | 6:5 |
| `logement-menage` | Property management, cleaning | Same, and the home services grid | 6:5 |
| `logement-reassort` | Property management, restocking | Same, and the home plans carousel | 6:5 |
| `maquette-voyageurs` | – | Home, « Pour les voyageurs » card | 6:5 |
| `paris` | Paris page | Same, and the home « Où nous intervenons » | 5:4 |
| `paris-marais` | Le Marais page, and its card | Same | 5:4 |
| `paris-montmartre` | Montmartre page, and its card | Same | 5:4 |
| `paris-saint-germain-des-pres` | Saint-Germain-des-Prés page, and its card | Same | 5:4 |
| `paris-quartier-latin` | Latin Quarter page, and its card | Same | 5:4 |
| `paris-tour-eiffel` | Eiffel Tower area page, and its card | Same | 5:4 |
| `paris-champs-elysees` | Champs-Élysées page, and its card | Same | 5:4 |
| `paris-opera` | Opéra page, and its card | Same | 5:4 |
| `paris-louvre` | Louvre page, and its card | Same | 5:4 |
| `paris-canal-saint-martin` | Canal Saint-Martin page, and its card | Same | 5:4 |
| `paris-bastille` | Bastille page, and its card | Same | 5:4 |
| `paris-montparnasse` | Montparnasse page, and its card | Same | 5:4 |
| `paris-trocadero` | Trocadéro page, and its card | Same | 5:4 |
| `ville-creteil` | Créteil page | Same | 5:4 |
| `ville-saint-maur` | Saint-Maur-des-Fossés page | Same | 5:4 |
| `og-image` | Preview when a link is shared (WhatsApp, Facebook, LinkedIn) | Same, and the home full-width banner | 1.91:1 |
| `maquette-contact` | – | Home, background behind the contact card | 1.91:1 |

## How to add the pictures

Send them to me under their file names (PNG or JPG), or do it yourself:

1. Put each picture, named exactly as above (e.g. `paris-marais.png`), in `_generator/sources/`.
2. In `_generator/`, run `py images.py`: each picture is cropped to its format and saved in two sizes in `assets/img/`.
3. Run `py build.py`, check with `py serve.py` (http://localhost:8001), then commit and push. Version B's pictures go through the same steps on its branch, then into `maquette/` on `main`.

Commercial use: check Midjourney's current terms for your plan before publishing the pictures on a business website.
