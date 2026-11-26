# Pictures for the EdenFlats website (Midjourney)

**The prompts are in `IMAGES-MIDJOURNEY-BATCHES.md`**, grouped for Midjourney batches (at most 3 grids per prompt), in the order to make them. They aim for realistic, lived-in pictures rather than glossy ones, with people of the many backgrounds you meet in France. The people are invented: never present them as the EdenFlats team or as real clients.

**27 picture spots.** Until a picture arrives, the main pages show the old site's photos and the other spots a « Photo à venir » frame with the file name.

| File name | Where it goes | Format |
|---|---|---|
| `accueil-hero` | Home, top | 4:5 |
| `voyageurs-hero` | Guest management, top | 4:5 |
| `logement-hero` | Property management, top | 4:5 |
| `formules-hero` | Plans, top | 4:5 |
| `accueil-voyageurs` | Home, « Des voyageurs choisis avec soin » | 6:5 |
| `accueil-logement` | Home, « Votre bien entre de bonnes mains » | 6:5 |
| `accueil-faq` | Home, questions | 6:5 |
| `voyageurs-annonce` | Guest management, the listing | 6:5 |
| `voyageurs-selection` | Guest management, guest screening | 6:5 |
| `logement-menage` | Property management, cleaning | 6:5 |
| `logement-reassort` | Property management, restocking | 6:5 |
| `paris` | Paris page | 5:4 |
| `paris-marais` | Le Marais page, and its card | 5:4 |
| `paris-montmartre` | Montmartre page, and its card | 5:4 |
| `paris-saint-germain-des-pres` | Saint-Germain-des-Prés page, and its card | 5:4 |
| `paris-quartier-latin` | Latin Quarter page, and its card | 5:4 |
| `paris-tour-eiffel` | Eiffel Tower area page, and its card | 5:4 |
| `paris-champs-elysees` | Champs-Élysées page, and its card | 5:4 |
| `paris-opera` | Opéra page, and its card | 5:4 |
| `paris-louvre` | Louvre page, and its card | 5:4 |
| `paris-canal-saint-martin` | Canal Saint-Martin page, and its card | 5:4 |
| `paris-bastille` | Bastille page, and its card | 5:4 |
| `paris-montparnasse` | Montparnasse page, and its card | 5:4 |
| `paris-trocadero` | Trocadéro page, and its card | 5:4 |
| `ville-creteil` | Créteil page | 5:4 |
| `ville-saint-maur` | Saint-Maur-des-Fossés page | 5:4 |
| `og-image` | Preview when a link is shared (WhatsApp, Facebook, LinkedIn) | 1.91:1 |

## How to add the pictures

Send them to me under their file names (PNG or JPG), or do it yourself:

1. Put each picture, named exactly as above (e.g. `paris-marais.png`), in `_generator/sources/`.
2. In `_generator/`, run `py images.py`: each picture is cropped to its format and saved in two sizes in `assets/img/`.
3. Run `py build.py`, check with `py serve.py` (http://localhost:8001), then commit and push.

Commercial use: check Midjourney's current terms for your plan before publishing the pictures on a business website.
