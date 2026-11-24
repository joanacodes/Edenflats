# Photos des pages Paris, quartiers et communes (format 5:4). Ce sont des images Midjourney faites par
# MLK Web Studio : le prompt de chacune est dans IMAGES-MIDJOURNEY.md, sous le même nom de fichier.
# Le texte alternatif décrit ce que montre le prompt ; si une image s'en écarte, corrigez-le ici.
# Tant qu'une image n'est pas livrée, son emplacement montre un cadre « Photo à venir » (placeholders.py).
def _p(file, fr, en):
    return {"file": file, "big": 1280, "alt": {"fr": fr, "en": en}}


AREA = {
    "paris": _p("paris", "Remise des clés à un voyageur dans la cage d'escalier d'un immeuble parisien",
                "Keys handed to a guest in the stairwell of a Paris apartment building"),
    "marais": _p("paris-marais", "Des voyageurs s'installent dans un appartement aux poutres apparentes, typique du Marais",
                 "Guests settling into an apartment with exposed beams, typical of Le Marais"),
    "montmartre": _p("paris-montmartre", "Petit-déjeuner sous la verrière d'un atelier d'artiste",
                     "Breakfast under the glass roof of an artist's studio"),
    "saint-germain-des-pres": _p("paris-saint-germain-des-pres", "Lecture près de la fenêtre d'un appartement rive gauche rempli de livres",
                                 "Reading by the window of a book-lined Left Bank apartment"),
    "quartier-latin": _p("paris-quartier-latin", "Un étudiant découvre un studio chaleureux avec son hôte",
                         "A student shown around a cosy studio by the host"),
    "tour-eiffel": _p("paris-tour-eiffel", "Une famille arrive dans un grand appartement haussmannien",
                      "A family arriving in a spacious Haussmann apartment"),
    "champs-elysees": _p("paris-champs-elysees", "Un voyageur d'affaires arrive dans un appartement raffiné",
                         "A business traveller arriving in a refined apartment"),
    "opera": _p("paris-opera", "Un couple se prépare pour une soirée à l'Opéra dans un salon haussmannien",
                "A couple getting ready for a night at the opera in a Haussmann salon"),
    "louvre": _p("paris-louvre", "Deux amis feuillettent un livre d'art dans un appartement décoré de tableaux",
                 "Two friends looking through an art book in an apartment hung with paintings"),
    "canal-saint-martin": _p("paris-canal-saint-martin", "Un jeune couple rentre son vélo dans un loft lumineux",
                             "A young couple bringing a bike into a bright loft"),
    "bastille": _p("paris-bastille", "Des amis préparent l'apéritif dans la cuisine d'un loft",
                   "Friends preparing drinks in a loft kitchen"),
    "montparnasse": _p("paris-montparnasse", "Un voyageur arrive dans un appartement aux détails Art déco",
                       "A traveller arriving in an apartment with Art Deco details"),
    "trocadero": _p("paris-trocadero", "Une grand-mère et sa petite-fille à la fenêtre d'un grand appartement parisien",
                    "A grandmother and her granddaughter at the window of a grand Paris apartment"),
    "creteil": _p("ville-creteil", "Un voyageur d'affaires travaille sur le balcon d'un appartement moderne",
                  "A business traveller working on the balcony of a modern apartment"),
    "saint-maur": _p("ville-saint-maur", "Une famille arrive au portail d'une maison avec jardin",
                     "A family arriving at the garden gate of a house"),
}
