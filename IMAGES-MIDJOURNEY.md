# Midjourney prompts for the EdenFlats website

One prompt per picture slot on the site. Copy a prompt, generate, pick the best image, save it under the **file name** shown, and the site picks it up automatically (see "How to add the images" at the end).

Every prompt shares the same look so the pictures feel like one series and match the site's colours: warm cream walls, coral and terracotta touches, sage green plants, a little soft periwinkle blue, Parisian Haussmann details, soft natural light.

**Tips**
- Generate `accueil-hero` first. When you like it, copy its image URL and add `--sref <url>` at the end of every other prompt: Midjourney will keep the same colours and mood across the whole set.
- People are shown from behind or as hands only. That avoids AI faces that could pass for your team or your clients.
- `--ar` sets the format each slot needs. Don't change it: the pages crop to that shape.
- The line illustrations (keys, calendar, cleaning spray…) are already drawn in the site (`assets/illus.svg`). There is nothing to generate for them.

---

## Home page (`/`)

### 1. `accueil-hero` — top of the home page, tall photo with the white cards on it

```
Two travellers seen from behind walking up to the tall carved wooden door of a Haussmann apartment building in Paris, one pulling a cabin suitcase, cream limestone facade, wrought-iron balconies, a terracotta planter with an olive tree by the entrance, soft golden morning light, warm editorial travel photography, natural colours, 35mm --ar 4:5 --style raw --no text, logo, watermark
```

### 2. `accueil-voyageurs` — section "Des voyageurs choisis avec soin"

```
Close-up of a host's hand giving a set of brass keys on a coral leather key ring to a guest's open hand, in the bright entrance hall of a Parisian apartment, cream walls, herringbone oak floor, a sage green plant in the background, shallow depth of field, warm editorial lifestyle photography --ar 6:5 --style raw --no text, logo, watermark, faces
```

### 3. `accueil-logement` — section "Votre bien entre de bonnes mains"

```
Freshly made bed with crisp white linen, a folded throw in soft periwinkle blue and a coral cushion, a stack of rolled white towels at the foot of the bed, in a Parisian Haussmann bedroom with ceiling mouldings and a tall French window, soft morning light, warm editorial interior photography --ar 6:5 --style raw --no text, logo, watermark, people
```

### 4. `accueil-faq` — FAQ section, photo with the WhatsApp card

```
Bright Parisian living room with ornate ceiling mouldings and tall French windows opening onto a wrought-iron balcony, cream linen sofa with terracotta and sage green cushions, indoor plants, a coffee cup and a croissant on a round wooden coffee table, warm morning light, editorial interior photography --ar 6:5 --style raw --no text, logo, watermark, people
```

## Guest management (`/gestion-des-voyageurs-conciergerie-airbnb-ile-de-france`)

### 5. `voyageurs-hero` — top of the page

```
A guest seen from behind pulling a suitcase across a sunny cobbled Paris courtyard towards an apartment entrance, cream stone facades, green wooden shutters, potted plants, warm golden light, editorial travel photography, natural colours --ar 4:5 --style raw --no text, logo, watermark
```

### 6. `voyageurs-annonce` — section "Une annonce qui donne envie de réserver"

```
Behind-the-scenes shot of a photographer on a tripod photographing a staged Parisian living room for a rental listing, seen from behind, softbox light, cream walls, coral armchair, sage green plants, herringbone parquet, warm editorial photography --ar 6:5 --style raw --no text, logo, watermark, faces
```

### 7. `voyageurs-selection` — section "Pourquoi sélectionner les voyageurs ?"

```
Over-the-shoulder view of hands typing on a laptop on a wooden desk, the screen showing an abstract booking calendar, a notebook, a cup of coffee and a set of keys beside it, warm daylight from a Parisian window, cream and sage green tones, editorial workplace photography --ar 6:5 --style raw --no text, readable text, logo, watermark, faces
```

## Property management (`/gestion-de-propriete-conciergerie-airbnb-ile-de-france`)

### 8. `logement-hero` — top of the page

```
Elegant Haussmann apartment living room in Paris, white marble fireplace with a gilded mirror, herringbone parquet, cream linen sofa with coral and soft periwinkle cushions, sage green plants, tall windows with afternoon light, warm editorial interior photography --ar 4:5 --style raw --no text, logo, watermark, people
```

### 9. `logement-menage` — section "On s'occupe du ménage"

```
Housekeeper's hands smoothing a crisp white duvet on a bed in a bright Parisian bedroom, a stack of folded white towels and a small basket of toiletries on the bedside table, warm daylight, cream and sage green tones, editorial lifestyle photography --ar 6:5 --style raw --no text, logo, watermark, faces
```

### 10. `logement-reassort` — section "Une sérénité assurée" (restocking and upkeep)

```
Bright Parisian bathroom with a wooden shelf of rolled white towels, amber glass bottles of shampoo and shower gel without labels, a sprig of eucalyptus in a small vase, terracotta zellige tiles and cream walls, soft window light, warm editorial still life photography --ar 6:5 --style raw --no text, labels, logo, watermark
```

## Plans (`/nos-formules`)

### 11. `formules-hero` — top of the page

```
Sunlit Parisian apartment with a small round wooden dining table, a set of keys, a coffee cup and a closed document folder on the table, view of zinc rooftops and chimneys through the open French window, cream walls, terracotta and sage green accents, warm editorial interior photography --ar 4:5 --style raw --no text, readable text, logo, watermark, people
```

## Share image (Facebook, LinkedIn, WhatsApp previews)

### 12. `og-image`

```
Wide view of a warm Parisian Haussmann living room with tall open windows overlooking zinc rooftops and the Eiffel Tower in the distance, cream walls, coral and sage green accents, soft periwinkle cushions, morning light, editorial interior photography --ar 191:100 --style raw --no text, logo, watermark, people
```

---

## Optional: neighbourhood pages

The neighbourhood pages already use **real photos** from Wikimedia Commons, credited under each photo. Real places look right in real photos; AI images of landmarks often get details wrong. Replace them only if you prefer a uniform AI style. If you do, empty the `"author"` of that photo in `_generator/photos.py` so the Wikimedia credit disappears.

| File | Page |
|---|---|
| `paris-marais` | Le Marais |
| `paris-montmartre` | Montmartre |
| `paris-saint-germain-des-pres` | Saint-Germain-des-Prés |
| `paris-quartier-latin` | Quartier latin |
| `paris-tour-eiffel` | Tour Eiffel |
| `paris-champs-elysees` | Champs-Élysées |
| `paris-opera` | Opéra |
| `paris-louvre` | Louvre |
| `paris-canal-saint-martin` | Canal Saint-Martin |
| `paris-bastille` | Bastille |
| `paris-montparnasse` | Montparnasse |
| `paris-trocadero` | Trocadéro |
| `paris-toits` | Paris hub page |
| `ville-creteil` | Créteil |
| `ville-saint-maur` | Saint-Maur-des-Fossés |

`paris-marais`
```
The Place des Vosges in Le Marais, Paris, red brick and stone arcades with steep slate roofs, linden trees, people relaxing on the lawn around the fountain, warm late-afternoon light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-montmartre`
```
Cobbled street in Montmartre climbing towards the white domes of the Sacré-Cœur basilica, a café terrace with rattan chairs, ivy-covered facades, warm morning light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-saint-germain-des-pres`
```
Café terrace with rattan chairs and round marble tables facing the Romanesque bell tower of the church of Saint-Germain-des-Prés, Paris, autumn light, editorial travel photography --ar 5:4 --style raw --no text, readable signs, logo, watermark
```
`paris-quartier-latin`
```
The dome of the Panthéon seen down rue Soufflot in the Latin Quarter, Paris, Haussmann facades, people walking, clear morning light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-tour-eiffel`
```
The Eiffel Tower framed by blossoming trees on the Champ de Mars in spring, soft morning light, a few people walking, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-champs-elysees`
```
Avenue des Champs-Élysées leading to the Arc de Triomphe at golden hour, rows of trees, light traffic, warm light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-opera`
```
Facade of the Palais Garnier opera house in Paris with its gilded statues and green dome, blue sky, people on the steps, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-louvre`
```
The Louvre glass pyramid and palace reflected in a fountain basin at sunrise, Paris, calm water, soft pink sky, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-canal-saint-martin`
```
Green iron footbridge over the Canal Saint-Martin in Paris, plane trees, a lock with calm water, cafés along the quay, morning light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-bastille`
```
The bronze July Column on Place de la Bastille in Paris against a blue sky, café terraces and Haussmann buildings around, warm light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-montparnasse`
```
Art deco facade of a historic brasserie with a red awning on Boulevard du Montparnasse, Paris, terrace with wicker chairs, evening light, editorial travel photography --ar 5:4 --style raw --no text, readable signs, logo, watermark
```
`paris-trocadero`
```
View of the Eiffel Tower from the Trocadéro esplanade at sunrise, the wings of the Palais de Chaillot in the foreground, fountains, soft pink light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`paris-toits`
```
Paris zinc rooftops and chimney pots at golden hour, Haussmann buildings, the Sacré-Cœur in the distance, warm light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`ville-creteil`
```
Lake of Créteil near Paris on a sunny morning, small sailboats, willow trees and modern residential towers on the far bank, calm water, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```
`ville-saint-maur`
```
Banks of the Marne river at Saint-Maur-des-Fossés near Paris, a rowing boat, weeping willows and houses with gardens on the bank, soft morning light, editorial travel photography --ar 5:4 --style raw --no text, logo, watermark
```

---

## How to add the images

1. Generate with the prompt, upscale the image you prefer and download it (PNG or JPG).
2. Rename it exactly as listed (for example `accueil-hero.png`) and put it in `_generator/sources/`.
3. In `_generator/`, run `py images.py`: each image is cropped to its format and saved in two sizes in `assets/img/`.
4. Run `py build.py`, preview with `py serve.py` (http://localhost:8001), then commit and push.

Until you replace them, the slots show the photos from the old Squarespace site. They are stock photos: check their licences before launch, or replace them all.

Commercial use: check Midjourney's current terms for your plan before publishing the images on a business website.
