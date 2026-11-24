# Pages des quartiers de Paris et des communes d'Île-de-France.
# Chaque page dit quelque chose de propre au lieu (stations, monuments, voyageurs) : des pages
# identiques où seul le nom change seraient traitées par Google comme des pages satellites.
from kit import (SITE, tr, url, icon, illu, chip, btn, more, fcard, photo, ticks, head, crumbs, crumbs_ld, service_ld)
import photos


AREAS = [
    {"id": "marais", "slug": {"fr": "le-marais", "en": "le-marais"}, "neighbors": ["bastille", "louvre", "canal-saint-martin"],
     "fr": {"name": "Le Marais", "prep": "dans le Marais", "arr": "Paris 3e et 4e",
            "teaser": "Hôtels particuliers, place des Vosges, boutiques ouvertes le dimanche.",
            "lead": "Hôtels particuliers, place des Vosges et boutiques ouvertes le dimanche : le Marais attire des voyageurs toute l'année. Nous gérons votre meublé dans le 3e et le 4e arrondissement.",
            "p1": "Le Marais s'étend sur le 3e et le 4e arrondissement, entre la place de la République, l'Hôtel de Ville et la Bastille. Ses rues étroites gardent de nombreux hôtels particuliers du XVIIe siècle, dont plusieurs abritent des musées : le musée Picasso, le musée Carnavalet, consacré à l'histoire de Paris, ou la maison de Victor Hugo, place des Vosges.",
            "p2": "Les voyageurs y viennent pour un week-end comme pour une semaine de salons ou de défilés. Les logements y sont souvent anciens : poutres apparentes, escaliers sans ascenseur, petites surfaces bien pensées. Une annonce claire sur l'étage et l'accès évite les mauvaises surprises à l'arrivée.",
            "ours": "Nous décrivons précisément l'accès et l'étage dans l'annonce, et organisons la remise des clés selon l'heure d'arrivée : en main propre, par un café partenaire ou avec une serrure connectée, pour que personne n'attende devant la porte.",
            "transit": ["Saint-Paul (ligne 1)", "Chemin Vert (8)", "Saint-Sébastien–Froissart (8)", "Arts et Métiers (3, 11)", "Rambuteau (11)", "Hôtel de Ville (1, 11)"],
            "see": ["Place des Vosges", "Musée Picasso", "Musée Carnavalet", "Rue des Rosiers"],
            "guests": "Couples, week-ends, semaines de la mode et salons"},
     "en": {"name": "Le Marais", "prep": "in Le Marais", "arr": "Paris 3rd and 4th",
            "teaser": "Mansions, the Place des Vosges and shops open on Sundays.",
            "lead": "Seventeenth-century mansions, the Place des Vosges and shops open on Sundays: Le Marais draws guests all year round. We manage furnished apartments in the 3rd and 4th arrondissements.",
            "p1": "Le Marais covers the 3rd and 4th arrondissements, between Place de la République, the Hôtel de Ville and Bastille. Its narrow streets keep many seventeenth-century hôtels particuliers, several of them now museums: the Musée Picasso, the Musée Carnavalet, devoted to the history of Paris, and Victor Hugo's House on the Place des Vosges.",
            "p2": "Guests come for a weekend as well as for a week of trade fairs or fashion shows. Apartments are often in old buildings: exposed beams, stairs without a lift, small but clever layouts. A listing that is clear about the floor and the access avoids bad surprises on arrival.",
            "ours": "We describe the access and the floor precisely in the listing, and arrange the key handover around the arrival time: in person, through a partner café or with a smart lock, so nobody is left waiting at the door.",
            "transit": ["Saint-Paul (line 1)", "Chemin Vert (8)", "Saint-Sébastien–Froissart (8)", "Arts et Métiers (3, 11)", "Rambuteau (11)", "Hôtel de Ville (1, 11)"],
            "see": ["Place des Vosges", "Musée Picasso", "Musée Carnavalet", "Rue des Rosiers"],
            "guests": "Couples, weekends, fashion weeks and trade fairs"}},
    {"id": "montmartre", "slug": {"fr": "montmartre", "en": "montmartre"}, "neighbors": ["opera", "canal-saint-martin", "louvre"],
     "fr": {"name": "Montmartre", "prep": "à Montmartre", "arr": "Paris 18e",
            "teaser": "La butte, le Sacré-Cœur et la vue sur tout Paris.",
            "lead": "La butte, le Sacré-Cœur et la vue sur tout Paris : Montmartre fait partie des quartiers que les voyageurs demandent par leur nom. Nous gérons votre meublé dans le 18e arrondissement.",
            "p1": "Montmartre occupe la butte du 18e arrondissement, couronnée par la basilique du Sacré-Cœur. Autour de la place du Tertre et de ses peintres, les rues pavées descendent vers les Abbesses, le musée de Montmartre et les vignes du Clos Montmartre, vendangées chaque automne lors de la Fête des vendanges.",
            "p2": "C'est un quartier de couples et de séjours de quelques nuits, où la vue et le charme d'un appartement d'artiste comptent autant que la surface. On monte la butte à pied, par ses escaliers, ou en funiculaire : un trajet à anticiper avec des bagages.",
            "ours": "Nous indiquons aux voyageurs le meilleur trajet jusqu'au logement avec leurs bagages, et mettons en avant ce qui fait la valeur d'un appartement à Montmartre : la vue, la lumière, le calme d'une cour.",
            "transit": ["Abbesses (ligne 12)", "Anvers (2)", "Lamarck–Caulaincourt (12)", "Blanche (2)", "Pigalle (2, 12)", "Funiculaire de Montmartre"],
            "see": ["Basilique du Sacré-Cœur", "Place du Tertre", "Musée de Montmartre", "Moulin Rouge"],
            "guests": "Couples, premiers séjours à Paris, courts séjours"},
     "en": {"name": "Montmartre", "prep": "in Montmartre", "arr": "Paris 18th",
            "teaser": "The hill, the Sacré-Cœur and views across Paris.",
            "lead": "The hill, the Sacré-Cœur and views across Paris: Montmartre is one of the neighbourhoods guests ask for by name. We manage furnished apartments in the 18th arrondissement.",
            "p1": "Montmartre is the hill of the 18th arrondissement, crowned by the Sacré-Cœur basilica. Around the Place du Tertre and its painters, cobbled streets lead down to Abbesses, the Musée de Montmartre and the Clos Montmartre vineyard, harvested every autumn during the Fête des Vendanges.",
            "p2": "It is a neighbourhood of couples and short stays, where the view and the charm of an artist's flat matter as much as floor space. Guests climb the hill on foot, by its many stairs, or take the funicular: a route worth planning with luggage.",
            "ours": "We tell guests the best route to the apartment with their luggage, and we highlight what gives a Montmartre flat its value: the view, the light, the quiet of a courtyard.",
            "transit": ["Abbesses (line 12)", "Anvers (2)", "Lamarck–Caulaincourt (12)", "Blanche (2)", "Pigalle (2, 12)", "Montmartre funicular"],
            "see": ["Sacré-Cœur basilica", "Place du Tertre", "Musée de Montmartre", "Moulin Rouge"],
            "guests": "Couples, first-time visitors, short stays"}},
    {"id": "saint-germain-des-pres", "slug": {"fr": "saint-germain-des-pres", "en": "saint-germain-des-pres"},
     "neighbors": ["quartier-latin", "louvre", "montparnasse"],
     "fr": {"name": "Saint-Germain-des-Prés", "prep": "à Saint-Germain-des-Prés", "arr": "Paris 6e",
            "teaser": "Cafés littéraires, galeries d'art et jardin du Luxembourg.",
            "lead": "Cafés littéraires, galeries d'art et jardin du Luxembourg : Saint-Germain-des-Prés attire une clientèle exigeante, souvent pour plusieurs nuits. Nous gérons votre meublé dans le 6e arrondissement.",
            "p1": "Le quartier s'organise autour de l'église de Saint-Germain-des-Prés, l'une des plus anciennes de Paris, et des cafés qui ont fait sa réputation, le Café de Flore et Les Deux Magots. Entre la Seine et le jardin du Luxembourg, les rues de Seine, Jacob ou de Buci alignent galeries d'art, maisons d'édition et antiquaires.",
            "p2": "Les voyageurs y cherchent un appartement de caractère, bien tenu, dans un immeuble ancien ou haussmannien. Les attentes sont élevées : des photos soignées, un linge impeccable et un accueil attentif font la différence dans les commentaires.",
            "ours": "Nous photographions nous-mêmes votre logement, soignons chaque ménage et chaque changement de linge, et accueillons les voyageurs en personne quand ils le souhaitent : c'est ce qui fait les bons commentaires dans ce quartier.",
            "transit": ["Saint-Germain-des-Prés (ligne 4)", "Mabillon (10)", "Odéon (4, 10)", "Saint-Sulpice (4)"],
            "see": ["Église de Saint-Germain-des-Prés", "Jardin du Luxembourg", "Église Saint-Sulpice", "Musée d'Orsay, à pied"],
            "guests": "Amateurs d'art et d'architecture, séjours de plusieurs nuits, clientèle internationale"},
     "en": {"name": "Saint-Germain-des-Prés", "prep": "in Saint-Germain-des-Prés", "arr": "Paris 6th",
            "teaser": "Literary cafés, art galleries and the Luxembourg Gardens.",
            "lead": "Literary cafés, art galleries and the Luxembourg Gardens: Saint-Germain-des-Prés attracts demanding guests, often for several nights. We manage furnished apartments in the 6th arrondissement.",
            "p1": "The neighbourhood grows around the church of Saint-Germain-des-Prés, one of the oldest in Paris, and the cafés that made its name, the Café de Flore and Les Deux Magots. Between the Seine and the Luxembourg Gardens, Rue de Seine, Rue Jacob and Rue de Buci are lined with art galleries, publishers and antique dealers.",
            "p2": "Guests look for an apartment with character, well kept, in an old or Haussmann-era building. Expectations are high: careful photos, spotless linen and an attentive welcome make the difference in reviews.",
            "ours": "We photograph your apartment ourselves, take care over every clean and every linen change, and welcome guests in person when they wish: that is what earns good reviews here.",
            "transit": ["Saint-Germain-des-Prés (line 4)", "Mabillon (10)", "Odéon (4, 10)", "Saint-Sulpice (4)"],
            "see": ["Church of Saint-Germain-des-Prés", "Luxembourg Gardens", "Saint-Sulpice church", "Musée d'Orsay, on foot"],
            "guests": "Art and architecture lovers, multi-night stays, international guests"}},
    {"id": "quartier-latin", "slug": {"fr": "quartier-latin", "en": "latin-quarter"},
     "neighbors": ["saint-germain-des-pres", "marais", "montparnasse"],
     "fr": {"name": "Quartier latin", "prep": "dans le Quartier latin", "arr": "Paris 5e",
            "teaser": "La Sorbonne, le Panthéon et la rue Mouffetard.",
            "lead": "La Sorbonne, le Panthéon et la rue Mouffetard : le Quartier latin accueille autant de chercheurs et de familles d'étudiants que de touristes. Nous gérons votre meublé dans le 5e arrondissement.",
            "p1": "Sur la rive gauche, face à l'île de la Cité et à Notre-Dame, le Quartier latin doit son nom au latin qu'on parlait dans ses universités au Moyen Âge. On y trouve la Sorbonne, le Panthéon, le musée de Cluny, la librairie Shakespeare and Company et, plus au sud, la rue Mouffetard et le Jardin des Plantes.",
            "p2": "Universités, grandes écoles et instituts de recherche y font venir enseignants, chercheurs et parents d'étudiants, souvent pour plusieurs semaines : la location de moyenne durée y a toute sa place. Le RER B, à Saint-Michel–Notre-Dame et à Luxembourg, rejoint directement l'aéroport Charles-de-Gaulle.",
            "ours": "Pour les séjours de plusieurs semaines, nous adaptons l'annonce et les prix à la durée, et gardons le même suivi : assistance 24h/24 pour les voyageurs et vérifications régulières du logement.",
            "transit": ["Saint-Michel–Notre-Dame (ligne 4, RER B et C)", "Cluny–La Sorbonne (10)", "Maubert–Mutualité (10)", "Place Monge (7)", "Luxembourg (RER B)"],
            "see": ["Panthéon", "Sorbonne", "Musée de Cluny", "Jardin des Plantes", "Rue Mouffetard"],
            "guests": "Chercheurs et enseignants, familles d'étudiants, séjours de moyenne durée"},
     "en": {"name": "Latin Quarter", "prep": "in the Latin Quarter", "arr": "Paris 5th",
            "teaser": "The Sorbonne, the Panthéon and Rue Mouffetard.",
            "lead": "The Sorbonne, the Panthéon and Rue Mouffetard: the Latin Quarter hosts as many researchers and students' families as tourists. We manage furnished apartments in the 5th arrondissement.",
            "p1": "On the Left Bank, facing the Île de la Cité and Notre-Dame, the Latin Quarter takes its name from the Latin once spoken in its medieval universities. It is home to the Sorbonne, the Panthéon, the Musée de Cluny, the Shakespeare and Company bookshop and, further south, Rue Mouffetard and the Jardin des Plantes.",
            "p2": "Universities, grandes écoles and research institutes bring lecturers, researchers and students' parents, often for several weeks, so mid-term stays work well here. RER B, at Saint-Michel–Notre-Dame and Luxembourg, runs directly to Charles de Gaulle airport.",
            "ours": "For stays of several weeks, we adapt the listing and the prices to the length of stay, and keep the same follow-up: 24/7 support for guests and regular checks of the apartment.",
            "transit": ["Saint-Michel–Notre-Dame (line 4, RER B and C)", "Cluny–La Sorbonne (10)", "Maubert–Mutualité (10)", "Place Monge (7)", "Luxembourg (RER B)"],
            "see": ["Panthéon", "Sorbonne", "Musée de Cluny", "Jardin des Plantes", "Rue Mouffetard"],
            "guests": "Researchers and lecturers, students' families, mid-term stays"}},
    {"id": "tour-eiffel", "slug": {"fr": "tour-eiffel", "en": "eiffel-tower"},
     "neighbors": ["trocadero", "champs-elysees", "saint-germain-des-pres"],
     "fr": {"name": "Tour Eiffel", "prep": "près de la tour Eiffel", "arr": "Paris 7e",
            "teaser": "Champ-de-Mars, Invalides et rue Cler.",
            "lead": "Se réveiller avec la tour Eiffel à la fenêtre : c'est la demande de nombreux voyageurs qui découvrent Paris. Nous gérons votre meublé dans le 7e arrondissement, autour du Champ-de-Mars.",
            "p1": "Le 7e arrondissement réunit la tour Eiffel et le Champ-de-Mars, les Invalides, le musée Rodin, le musée du quai Branly – Jacques Chirac et, au bord de la Seine, le musée d'Orsay. Entre ces monuments, la rue Cler et ses commerces de bouche donnent au quartier une vie de village.",
            "p2": "Familles et premiers séjours à Paris le demandent sans cesse. Les appartements y sont souvent plus grands qu'au centre, dans des immeubles haussmanniens ; une vue sur la tour, même partielle, mérite d'être montrée dès la première photo.",
            "ours": "Nous mettons la vue et les volumes en avant dès la première photo, facilitons les réservations des familles et préparons le logement pour elles : linge pour chaque couchage, consommables en quantité suffisante.",
            "transit": ["École Militaire (ligne 8)", "La Tour-Maubourg (8)", "Bir-Hakeim (6)", "Champ de Mars–Tour Eiffel (RER C)", "Invalides (8, 13, RER C)"],
            "see": ["Tour Eiffel", "Champ-de-Mars", "Invalides", "Musée Rodin", "Musée du quai Branly"],
            "guests": "Familles, premiers séjours à Paris, séjours d'une semaine"},
     "en": {"name": "Eiffel Tower", "prep": "near the Eiffel Tower", "arr": "Paris 7th",
            "teaser": "Champ de Mars, Les Invalides and Rue Cler.",
            "lead": "Waking up with the Eiffel Tower in the window is what many first-time visitors ask for. We manage furnished apartments in the 7th arrondissement, around the Champ de Mars.",
            "p1": "The 7th arrondissement brings together the Eiffel Tower and the Champ de Mars, Les Invalides, the Musée Rodin, the Musée du quai Branly – Jacques Chirac and, on the banks of the Seine, the Musée d'Orsay. Between the monuments, Rue Cler and its food shops give the area a village feel.",
            "p2": "Families and first-time visitors ask for it all the time. Apartments are often larger than in the centre, in Haussmann-era buildings; a view of the tower, even a partial one, deserves to be in the first photo.",
            "ours": "We put the view and the space forward from the first photo, make bookings easy for families and prepare the apartment for them: linen for every bed, plenty of consumables.",
            "transit": ["École Militaire (line 8)", "La Tour-Maubourg (8)", "Bir-Hakeim (6)", "Champ de Mars–Tour Eiffel (RER C)", "Invalides (8, 13, RER C)"],
            "see": ["Eiffel Tower", "Champ de Mars", "Les Invalides", "Musée Rodin", "Musée du quai Branly"],
            "guests": "Families, first-time visitors, week-long stays"}},
    {"id": "champs-elysees", "slug": {"fr": "champs-elysees", "en": "champs-elysees"}, "neighbors": ["trocadero", "opera", "tour-eiffel"],
     "fr": {"name": "Champs-Élysées", "prep": "autour des Champs-Élysées", "arr": "Paris 8e",
            "teaser": "Arc de Triomphe, Grand Palais et avenue Montaigne.",
            "lead": "Entre l'Arc de Triomphe et le Grand Palais, le 8e arrondissement accueille voyageurs d'affaires et clientèle internationale. Nous gérons votre meublé autour des Champs-Élysées.",
            "p1": "L'avenue des Champs-Élysées relie la place de la Concorde à l'Arc de Triomphe. Autour d'elle, le 8e arrondissement rassemble le Grand Palais et le Petit Palais, les boutiques de l'avenue Montaigne et le « triangle d'or », où de nombreuses entreprises ont leur siège.",
            "p2": "En semaine, les voyageurs d'affaires cherchent un appartement pratique et bien équipé ; le week-end, la clientèle est plus touristique. Le RER A, à Charles-de-Gaulle–Étoile, mène directement à La Défense et à Disneyland Paris.",
            "ours": "Nous publions votre annonce en français et en anglais sur plusieurs plateformes, pour toucher la clientèle d'affaires comme les touristes, et restons joignables 24h/24 pour les voyageurs.",
            "transit": ["Charles-de-Gaulle–Étoile (lignes 1, 2, 6, RER A)", "George V (1)", "Franklin D. Roosevelt (1, 9)", "Champs-Élysées–Clemenceau (1, 13)"],
            "see": ["Arc de Triomphe", "Grand Palais", "Petit Palais", "Pont Alexandre-III"],
            "guests": "Voyageurs d'affaires, clientèle internationale, séjours de shopping"},
     "en": {"name": "Champs-Élysées", "prep": "around the Champs-Élysées", "arr": "Paris 8th",
            "teaser": "Arc de Triomphe, Grand Palais and Avenue Montaigne.",
            "lead": "Between the Arc de Triomphe and the Grand Palais, the 8th arrondissement hosts business travellers and international guests. We manage furnished apartments around the Champs-Élysées.",
            "p1": "The Avenue des Champs-Élysées runs from the Place de la Concorde to the Arc de Triomphe. Around it, the 8th arrondissement gathers the Grand Palais and the Petit Palais, the boutiques of Avenue Montaigne and the “golden triangle”, where many companies have their head offices.",
            "p2": "On weekdays, business travellers look for a practical, well-equipped apartment; at weekends, guests are more often tourists. RER A, at Charles de Gaulle–Étoile, runs directly to La Défense and Disneyland Paris.",
            "ours": "We publish your listing in French and English on several platforms, to reach business travellers as well as tourists, and stay reachable 24/7 for guests.",
            "transit": ["Charles de Gaulle–Étoile (lines 1, 2, 6, RER A)", "George V (1)", "Franklin D. Roosevelt (1, 9)", "Champs-Élysées–Clemenceau (1, 13)"],
            "see": ["Arc de Triomphe", "Grand Palais", "Petit Palais", "Pont Alexandre III"],
            "guests": "Business travellers, international guests, shopping trips"}},
    {"id": "opera", "slug": {"fr": "opera", "en": "opera"}, "neighbors": ["montmartre", "louvre", "champs-elysees"],
     "fr": {"name": "Opéra", "prep": "dans le quartier de l'Opéra", "arr": "Paris 9e et 2e",
            "teaser": "Palais Garnier, grands magasins et passages couverts.",
            "lead": "Le palais Garnier, les grands magasins et les théâtres des Grands Boulevards : le quartier de l'Opéra est l'un des mieux desservis de Paris. Nous gérons votre meublé dans le 9e arrondissement et alentour.",
            "p1": "Autour du palais Garnier, le boulevard Haussmann aligne les Galeries Lafayette et le Printemps ; plus à l'est, les Grands Boulevards gardent leurs théâtres et leurs passages couverts, comme les passages Jouffroy, Verdeau et des Panoramas. Au nord, la rue des Martyrs monte vers Pigalle et Montmartre.",
            "p2": "Le quartier plaît aux voyageurs qui veulent tout faire à pied ou en métro. La gare Saint-Lazare est toute proche : la ligne 14 y rejoint l'aéroport d'Orly sans changement, et le RER A s'arrête à Auber.",
            "ours": "Avec autant de lignes de métro et de trains, les horaires d'arrivée varient beaucoup : la remise des clés par un café partenaire ou une serrure connectée permet d'accueillir chaque voyageur à l'heure qui lui convient.",
            "transit": ["Opéra (lignes 3, 7, 8)", "Chaussée d'Antin–La Fayette (7, 9)", "Havre-Caumartin (3, 9)", "Auber (RER A)", "Saint-Lazare (3, 12, 13, 14)"],
            "see": ["Palais Garnier", "Galeries Lafayette", "Printemps Haussmann", "Passages couverts"],
            "guests": "Shopping, spectacles, voyages d'affaires, courts séjours"},
     "en": {"name": "Opéra", "prep": "in the Opéra district", "arr": "Paris 9th and 2nd",
            "teaser": "Palais Garnier, department stores and covered passages.",
            "lead": "The Palais Garnier, the department stores and the theatres of the Grands Boulevards: the Opéra district is one of the best connected in Paris. We manage furnished apartments in the 9th arrondissement and around.",
            "p1": "Around the Palais Garnier, Boulevard Haussmann is lined by the Galeries Lafayette and Printemps; further east, the Grands Boulevards keep their theatres and covered passages, such as the Passage Jouffroy, Passage Verdeau and Passage des Panoramas. To the north, Rue des Martyrs climbs towards Pigalle and Montmartre.",
            "p2": "The area suits guests who want to do everything on foot or by metro. Saint-Lazare station is close by: line 14 runs from there to Orly airport without changing, and RER A stops at Auber.",
            "ours": "With so many metro and train lines, arrival times vary a lot: key handover through a partner café or a smart lock lets us welcome every guest at the time that suits them.",
            "transit": ["Opéra (lines 3, 7, 8)", "Chaussée d'Antin–La Fayette (7, 9)", "Havre-Caumartin (3, 9)", "Auber (RER A)", "Saint-Lazare (3, 12, 13, 14)"],
            "see": ["Palais Garnier", "Galeries Lafayette", "Printemps Haussmann", "Covered passages"],
            "guests": "Shoppers, theatre-goers, business trips, short stays"}},
    {"id": "louvre", "slug": {"fr": "louvre", "en": "louvre"}, "neighbors": ["opera", "marais", "saint-germain-des-pres"],
     "fr": {"name": "Louvre", "prep": "près du Louvre", "arr": "Paris 1er",
            "teaser": "Le Louvre, les Tuileries et le Palais-Royal.",
            "lead": "Au cœur de Paris, entre le Louvre, les Tuileries et le Palais-Royal : un emplacement que tous les voyageurs comprennent. Nous gérons votre meublé dans le 1er arrondissement.",
            "p1": "Le 1er arrondissement s'étend du musée du Louvre et du jardin des Tuileries jusqu'aux Halles. On y trouve le jardin du Palais-Royal et ses colonnes de Buren, la place Vendôme, la Bourse de Commerce – Pinault Collection et, à la pointe de l'île de la Cité, le Pont-Neuf.",
            "p2": "Les voyageurs choisissent le 1er pour tout faire à pied, du Louvre à Notre-Dame. Les immeubles y sont anciens et les logements souvent compacts : chaque mètre carré doit être bien mis en valeur sur les photos. À Châtelet–Les Halles, les RER A, B et D desservent La Défense, Disneyland Paris, l'aéroport Charles-de-Gaulle et le Stade de France.",
            "ours": "Dans un logement compact, les photos font la réservation : nous les prenons nous-mêmes et, si besoin, nous vous conseillons sur la décoration pour que chaque mètre carré compte.",
            "transit": ["Palais Royal–Musée du Louvre (lignes 1, 7)", "Louvre–Rivoli (1)", "Tuileries (1)", "Pyramides (7, 14)", "Châtelet–Les Halles (RER A, B, D)"],
            "see": ["Musée du Louvre", "Jardin des Tuileries", "Palais-Royal", "Place Vendôme", "Bourse de Commerce"],
            "guests": "Premiers séjours à Paris, courts séjours culturels"},
     "en": {"name": "Louvre", "prep": "near the Louvre", "arr": "Paris 1st",
            "teaser": "The Louvre, the Tuileries and the Palais-Royal.",
            "lead": "In the heart of Paris, between the Louvre, the Tuileries and the Palais-Royal: a location every guest understands. We manage furnished apartments in the 1st arrondissement.",
            "p1": "The 1st arrondissement stretches from the Louvre and the Tuileries Garden to Les Halles. It includes the Palais-Royal garden and its Buren columns, the Place Vendôme, the Bourse de Commerce – Pinault Collection and, at the tip of the Île de la Cité, the Pont Neuf.",
            "p2": "Guests choose the 1st to do everything on foot, from the Louvre to Notre-Dame. Buildings are old and apartments often compact, so every square metre has to show well in the photos. At Châtelet–Les Halles, RER lines A, B and D run to La Défense, Disneyland Paris, Charles de Gaulle airport and the Stade de France.",
            "ours": "In a compact apartment, photos make the booking: we take them ourselves and, where needed, advise you on decoration so that every square metre counts.",
            "transit": ["Palais Royal–Musée du Louvre (lines 1, 7)", "Louvre–Rivoli (1)", "Tuileries (1)", "Pyramides (7, 14)", "Châtelet–Les Halles (RER A, B, D)"],
            "see": ["Louvre Museum", "Tuileries Garden", "Palais-Royal", "Place Vendôme", "Bourse de Commerce"],
            "guests": "First-time visitors, short cultural stays"}},
    {"id": "canal-saint-martin", "slug": {"fr": "canal-saint-martin", "en": "canal-saint-martin"}, "neighbors": ["marais", "bastille", "montmartre"],
     "fr": {"name": "Canal Saint-Martin", "prep": "le long du canal Saint-Martin", "arr": "Paris 10e",
            "teaser": "Écluses, passerelles et gares du Nord et de l'Est.",
            "lead": "Écluses, passerelles en fer et terrasses au bord de l'eau : le canal Saint-Martin attire une clientèle jeune et les voyageurs arrivés en train de Londres ou de Bruxelles. Nous gérons votre meublé dans le 10e arrondissement.",
            "p1": "Ouvert en 1825, le canal Saint-Martin traverse le 10e arrondissement à ciel ouvert, du bassin de la Villette à la place de la République. Ses quais de Valmy et de Jemmapes, bordés de platanes, alignent cafés, boutiques de créateurs et l'Hôtel du Nord, rendu célèbre par le film de Marcel Carné.",
            "p2": "La gare du Nord et la gare de l'Est sont à quelques minutes à pied : c'est un point d'arrivée pratique pour les voyageurs venus en train de Londres, de Bruxelles ou d'Allemagne, et le RER B part de la gare du Nord vers l'aéroport Charles-de-Gaulle.",
            "ours": "Nous rédigeons votre annonce en français et en anglais et donnons aux voyageurs, avant leur arrivée, toutes les indications pour rejoindre le logement depuis la gare.",
            "transit": ["République (lignes 3, 5, 8, 9, 11)", "Jacques Bonsergent (5)", "Goncourt (11)", "Gare de l'Est (4, 5, 7)", "Gare du Nord (4, 5, RER B, D)"],
            "see": ["Écluses et passerelles du canal", "Quai de Valmy", "Hôtel du Nord", "Bassin de la Villette"],
            "guests": "Jeunes voyageurs, arrivées en train depuis Londres ou Bruxelles"},
     "en": {"name": "Canal Saint-Martin", "prep": "along the Canal Saint-Martin", "arr": "Paris 10th",
            "teaser": "Locks, footbridges, Gare du Nord and Gare de l'Est.",
            "lead": "Locks, iron footbridges and terraces by the water: the Canal Saint-Martin attracts younger guests and travellers arriving by train from London or Brussels. We manage furnished apartments in the 10th arrondissement.",
            "p1": "Opened in 1825, the Canal Saint-Martin runs in the open air through the 10th arrondissement, from the Bassin de la Villette to Place de la République. Its plane-tree-lined quays, Quai de Valmy and Quai de Jemmapes, are lined with cafés, designer shops and the Hôtel du Nord, made famous by Marcel Carné's film.",
            "p2": "Gare du Nord and Gare de l'Est are a few minutes' walk away: a convenient arrival point for guests coming by train from London, Brussels or Germany, and RER B runs from Gare du Nord to Charles de Gaulle airport.",
            "ours": "We write your listing in French and English and, before they arrive, send guests clear directions from the station to the apartment.",
            "transit": ["République (lines 3, 5, 8, 9, 11)", "Jacques Bonsergent (5)", "Goncourt (11)", "Gare de l'Est (4, 5, 7)", "Gare du Nord (4, 5, RER B, D)"],
            "see": ["Canal locks and footbridges", "Quai de Valmy", "Hôtel du Nord", "Bassin de la Villette"],
            "guests": "Younger travellers, arrivals by train from London or Brussels"}},
    {"id": "bastille", "slug": {"fr": "bastille", "en": "bastille"}, "neighbors": ["marais", "canal-saint-martin", "quartier-latin"],
     "fr": {"name": "Bastille", "prep": "à Bastille", "arr": "Paris 11e, 12e et 4e",
            "teaser": "Opéra Bastille, marché d'Aligre et Coulée verte.",
            "lead": "Entre l'Opéra Bastille, le marché d'Aligre et la Coulée verte, la Bastille vit à toute heure. Nous gérons votre meublé dans le 11e, le 12e et le 4e arrondissement.",
            "p1": "La place de la Bastille, avec la colonne de Juillet en son centre, se trouve à la jonction du 4e, du 11e et du 12e arrondissement. Autour, l'Opéra Bastille, le port de l'Arsenal, le Viaduc des Arts et la Coulée verte René-Dumont, promenade plantée sur une ancienne voie ferrée, mènent vers le marché d'Aligre et la gare de Lyon.",
            "p2": "Avec la rue de Lappe et la rue de la Roquette, le quartier est connu pour ses bars et sa vie nocturne. Pour un propriétaire, la sélection des voyageurs y compte d'autant plus.",
            "ours": "Nous demandons à chaque voyageur son âge et la raison de son séjour, en insistant pour ceux qui n'ont pas de commentaire, privilégions les profils vérifiés et vérifions l'identité avant chaque séjour.",
            "transit": ["Bastille (lignes 1, 5, 8)", "Ledru-Rollin (8)", "Bréguet-Sabin (5)", "Gare de Lyon (1, 14, RER A, D)"],
            "see": ["Colonne de Juillet", "Opéra Bastille", "Coulée verte René-Dumont", "Marché d'Aligre", "Port de l'Arsenal"],
            "guests": "Jeunes voyageurs, amateurs d'opéra, voyageurs de passage par la gare de Lyon"},
     "en": {"name": "Bastille", "prep": "in Bastille", "arr": "Paris 11th, 12th and 4th",
            "teaser": "Opéra Bastille, Aligre market and the Coulée verte.",
            "lead": "Between the Opéra Bastille, the Aligre market and the Coulée verte, Bastille is lively at any hour. We manage furnished apartments in the 11th, 12th and 4th arrondissements.",
            "p1": "Place de la Bastille, with the July Column at its centre, sits where the 4th, 11th and 12th arrondissements meet. Around it, the Opéra Bastille, the Arsenal marina, the Viaduc des Arts and the Coulée verte René-Dumont, a garden walk on a former railway line, lead to the Aligre market and Gare de Lyon.",
            "p2": "With Rue de Lappe and Rue de la Roquette, the area is known for its bars and nightlife. For an owner, guest screening matters all the more.",
            "ours": "We ask every guest for their age and the reason for their stay, insisting with those who have no reviews, favour verified profiles and check identity before every stay.",
            "transit": ["Bastille (lines 1, 5, 8)", "Ledru-Rollin (8)", "Bréguet-Sabin (5)", "Gare de Lyon (1, 14, RER A, D)"],
            "see": ["July Column", "Opéra Bastille", "Coulée verte René-Dumont", "Aligre market", "Arsenal marina"],
            "guests": "Younger travellers, opera-goers, guests passing through Gare de Lyon"}},
    {"id": "montparnasse", "slug": {"fr": "montparnasse", "en": "montparnasse"}, "neighbors": ["saint-germain-des-pres", "quartier-latin", "tour-eiffel"],
     "fr": {"name": "Montparnasse", "prep": "à Montparnasse", "arr": "Paris 14e, 15e et 6e",
            "teaser": "La gare, les cafés historiques et les Catacombes.",
            "lead": "La gare, les cafés historiques et les Catacombes : Montparnasse accueille voyageurs d'affaires et touristes, souvent arrivés en TGV. Nous gérons votre meublé dans le 14e, le 15e et le 6e arrondissement.",
            "p1": "Le quartier s'est fait un nom dans les années 1920 avec les peintres et les écrivains qui se retrouvaient à La Coupole, au Dôme, à La Rotonde ou au Select, sur le boulevard du Montparnasse. Il s'organise aujourd'hui autour de la tour Montparnasse et de la gare, avec le cimetière du Montparnasse et, à Denfert-Rochereau, l'entrée des Catacombes.",
            "p2": "La gare Montparnasse relie Paris à la Bretagne et au sud-ouest en TGV : beaucoup de voyageurs d'affaires y cherchent un appartement pratique, à quelques minutes du train, pour quelques nuits ou plusieurs semaines de mission.",
            "ours": "Nous adaptons les prix à la durée des séjours, de la nuit isolée à la mission de plusieurs semaines, et nos équipes remettent le logement en état entre chaque séjour.",
            "transit": ["Montparnasse–Bienvenüe (lignes 4, 6, 12, 13)", "Vavin (4)", "Edgar Quinet (6)", "Gaîté (13)", "Denfert-Rochereau (4, 6, RER B)"],
            "see": ["Tour Montparnasse", "Cafés du boulevard du Montparnasse", "Cimetière du Montparnasse", "Catacombes"],
            "guests": "Voyageurs d'affaires, missions de plusieurs semaines, visiteurs des Catacombes"},
     "en": {"name": "Montparnasse", "prep": "in Montparnasse", "arr": "Paris 14th, 15th and 6th",
            "teaser": "The station, historic cafés and the Catacombs.",
            "lead": "The station, the historic cafés and the Catacombs: Montparnasse welcomes business travellers and tourists, many arriving by TGV. We manage furnished apartments in the 14th, 15th and 6th arrondissements.",
            "p1": "The area made its name in the 1920s with the painters and writers who met at La Coupole, Le Dôme, La Rotonde and Le Select, on Boulevard du Montparnasse. Today it centres on the Tour Montparnasse and the station, with the Montparnasse cemetery and, at Denfert-Rochereau, the entrance to the Catacombs.",
            "p2": "Gare Montparnasse links Paris to Brittany and the south-west by TGV: many business travellers look for a practical apartment a few minutes from the train, for a few nights or several weeks on assignment.",
            "ours": "We adapt prices to the length of stay, from a single night to an assignment of several weeks, and our teams get the apartment ready between every stay.",
            "transit": ["Montparnasse–Bienvenüe (lines 4, 6, 12, 13)", "Vavin (4)", "Edgar Quinet (6)", "Gaîté (13)", "Denfert-Rochereau (4, 6, RER B)"],
            "see": ["Tour Montparnasse", "Cafés of Boulevard du Montparnasse", "Montparnasse cemetery", "Catacombs"],
            "guests": "Business travellers, multi-week assignments, Catacombs visitors"}},
    {"id": "trocadero", "slug": {"fr": "trocadero", "en": "trocadero"}, "neighbors": ["tour-eiffel", "champs-elysees", "opera"],
     "fr": {"name": "Trocadéro", "prep": "au Trocadéro", "arr": "Paris 16e",
            "teaser": "Face à la tour Eiffel, musées et grandes avenues.",
            "lead": "Face à la tour Eiffel, entre musées et grandes avenues : le Trocadéro et Passy accueillent des familles et des séjours plus longs. Nous gérons votre meublé dans le 16e arrondissement.",
            "p1": "Depuis l'esplanade du Trocadéro, entre les deux ailes du palais de Chaillot, la tour Eiffel se découvre de l'autre côté de la Seine. Le palais abrite le musée de l'Homme et la Cité de l'architecture et du patrimoine ; le Palais de Tokyo, le musée d'Art moderne de Paris et, un peu plus loin, le musée Marmottan Monet complètent l'offre culturelle du 16e.",
            "p2": "Le 16e est résidentiel, avec de grands appartements familiaux. Fin mai et début juin, le tournoi de Roland-Garros, porte d'Auteuil, fait venir des visiteurs du monde entier, comme les matchs du Parc des Princes : des dates où la demande monte.",
            "ours": "Notre tarification dynamique suit ces pics de demande, de Roland-Garros aux grands matchs, pour que votre logement soit loué au bon prix ces semaines-là.",
            "transit": ["Trocadéro (lignes 6, 9)", "Iéna (9)", "Boissière (6)", "Passy (6)", "La Muette (9)"],
            "see": ["Esplanade du Trocadéro", "Palais de Chaillot", "Palais de Tokyo", "Musée Marmottan Monet"],
            "guests": "Familles, séjours longs, visiteurs de Roland-Garros"},
     "en": {"name": "Trocadéro", "prep": "in Trocadéro", "arr": "Paris 16th",
            "teaser": "Facing the Eiffel Tower, museums and wide avenues.",
            "lead": "Facing the Eiffel Tower, between museums and wide avenues: Trocadéro and Passy welcome families and longer stays. We manage furnished apartments in the 16th arrondissement.",
            "p1": "From the Trocadéro esplanade, between the two wings of the Palais de Chaillot, the Eiffel Tower stands across the Seine. The palace houses the Musée de l'Homme and the Cité de l'architecture et du patrimoine; the Palais de Tokyo, the Musée d'Art Moderne de Paris and, a little further, the Musée Marmottan Monet complete the 16th's cultural offer.",
            "p2": "The 16th is residential, with large family apartments. In late May and early June, the Roland-Garros tournament at Porte d'Auteuil brings visitors from all over the world, as do matches at the Parc des Princes: dates when demand rises.",
            "ours": "Our dynamic pricing follows these demand peaks, from Roland-Garros to the big matches, so your apartment is let at the right price in those weeks.",
            "transit": ["Trocadéro (lines 6, 9)", "Iéna (9)", "Boissière (6)", "Passy (6)", "La Muette (9)"],
            "see": ["Trocadéro esplanade", "Palais de Chaillot", "Palais de Tokyo", "Musée Marmottan Monet"],
            "guests": "Families, long stays, Roland-Garros visitors"}},
]

# Communes d'Île-de-France qui avaient déjà une page sur l'ancien site : leurs adresses sont gardées.
TOWNS = [
    {"id": "creteil", "route": {"fr": "/conciergerie-airbnb-creteil", "en": "/en/airbnb-management-creteil"}, "neighbors": ["saint-maur"],
     "fr": {"name": "Créteil", "prep": "à Créteil", "arr": "Val-de-Marne (94)",
            "teaser": "Préfecture du Val-de-Marne, sur la ligne 8.",
            "lead": "Préfecture du Val-de-Marne, reliée à Paris par la ligne 8 du métro, Créteil attire des voyageurs qui viennent étudier, travailler ou accompagner un proche. Nous gérons votre meublé en location courte et moyenne durée.",
            "p1": "Créteil est reliée au centre de Paris par la ligne 8 du métro, qui la traverse jusqu'à son terminus, Pointe du Lac. La ville accueille l'université Paris-Est Créteil, l'hôpital Henri-Mondor et le centre commercial Créteil Soleil, autour de son lac et de sa base de loisirs.",
            "p2": "On y vient pour étudier, travailler ou accompagner un proche hospitalisé, souvent pour plus que quelques nuits : la location de moyenne durée y a autant de sens que le court séjour. Un parking, un balcon ou la proximité du métro sont des atouts à mettre en avant dans l'annonce.",
            "ours": "Nous adaptons l'annonce et les prix aux séjours de plusieurs semaines, et gérons tout depuis le Val-de-Marne : notre siège est à Sucy-en-Brie, à quelques minutes.",
            "transit": ["Créteil–L'Échat (ligne 8)", "Créteil–Université (8)", "Créteil–Préfecture (8)", "Pointe du Lac (8)"],
            "see": ["Lac de Créteil et base de loisirs", "Créteil Soleil", "Bords de Marne"],
            "guests": "Étudiants et enseignants, proches de patients, missions professionnelles"},
     "en": {"name": "Créteil", "prep": "in Créteil", "arr": "Val-de-Marne (94)",
            "teaser": "Val-de-Marne's prefecture, on metro line 8.",
            "lead": "Val-de-Marne's prefecture, linked to Paris by metro line 8, Créteil attracts guests who come to study, work or be near a relative. We manage furnished homes for short and mid-term stays.",
            "p1": "Créteil is linked to central Paris by metro line 8, which runs through the town to its terminus, Pointe du Lac. The town is home to the Université Paris-Est Créteil, the Henri-Mondor hospital and the Créteil Soleil shopping centre, around its lake and leisure park.",
            "p2": "People come to study, work or stay near a relative in hospital, often for more than a few nights, so mid-term lets make as much sense here as short stays. Parking, a balcony or a short walk to the metro are strengths to highlight in the listing.",
            "ours": "We adapt the listing and the prices to stays of several weeks, and manage everything from Val-de-Marne: our head office is in Sucy-en-Brie, a few minutes away.",
            "transit": ["Créteil–L'Échat (line 8)", "Créteil–Université (8)", "Créteil–Préfecture (8)", "Pointe du Lac (8)"],
            "see": ["Créteil lake and leisure park", "Créteil Soleil", "Banks of the Marne"],
            "guests": "Students and lecturers, patients' relatives, work assignments"}},
    {"id": "saint-maur", "route": {"fr": "/conciergerie-airbnb-saint-maur-des-fosses", "en": "/en/airbnb-management-saint-maur-des-fosses"},
     "neighbors": ["creteil"],
     "fr": {"name": "Saint-Maur-des-Fossés", "prep": "à Saint-Maur-des-Fossés", "arr": "Val-de-Marne (94)",
            "teaser": "Une boucle de la Marne, à une vingtaine de minutes de Paris en RER A.",
            "lead": "Dans une boucle de la Marne, à une vingtaine de minutes du centre de Paris en RER A, Saint-Maur-des-Fossés attire les voyageurs qui cherchent le calme des bords de l'eau. Nous gérons votre logement meublé en location courte et moyenne durée.",
            "p1": "Saint-Maur-des-Fossés occupe presque entièrement une boucle de la Marne, dans le Val-de-Marne. Le RER A y dessert plusieurs gares, dont Saint-Maur–Créteil, Le Parc de Saint-Maur et La Varenne–Chennevières, et rejoint Nation, Châtelet–Les Halles et La Défense sans changement.",
            "p2": "Ses quartiers ont chacun leur caractère, de La Varenne au Vieux Saint-Maur en passant par Le Parc et Champignol : maisons avec jardin, appartements calmes, promenades au bord de la Marne. Une annonce réussie montre ce que le logement offre de mieux : la gare à pied, la rivière ou un jardin.",
            "ours": "Nous connaissons bien l'est parisien : notre siège est à Sucy-en-Brie, à une station de RER de La Varenne. Ménage, linge et petits travaux sont organisés au plus près de votre logement.",
            "transit": ["Saint-Maur–Créteil (RER A)", "Le Parc de Saint-Maur (RER A)", "La Varenne–Chennevières (RER A)"],
            "see": ["Bords de Marne", "Vieux Saint-Maur et tour Rabelais", "Quartier de La Varenne"],
            "guests": "Familles, séjours au calme près de Paris, visites à des proches"},
     "en": {"name": "Saint-Maur-des-Fossés", "prep": "in Saint-Maur-des-Fossés", "arr": "Val-de-Marne (94)",
            "teaser": "A loop of the Marne, about twenty minutes from Paris by RER A.",
            "lead": "In a loop of the Marne, about twenty minutes from central Paris by RER A, Saint-Maur-des-Fossés attracts guests looking for calm by the water. We manage furnished homes for short and mid-term stays.",
            "p1": "Saint-Maur-des-Fossés fills almost an entire loop of the Marne, in Val-de-Marne. RER A serves several stations, including Saint-Maur–Créteil, Le Parc de Saint-Maur and La Varenne–Chennevières, and runs to Nation, Châtelet–Les Halles and La Défense without changing.",
            "p2": "Each neighbourhood has its own character, from La Varenne to the Vieux Saint-Maur by way of Le Parc and Champignol: houses with gardens, quiet apartments, walks along the Marne. A good listing shows what the home does best: the station on foot, the river or a garden.",
            "ours": "We know the east of Paris well: our head office is in Sucy-en-Brie, one RER stop from La Varenne. Cleaning, linen and small repairs are organised close to your home.",
            "transit": ["Saint-Maur–Créteil (RER A)", "Le Parc de Saint-Maur (RER A)", "La Varenne–Chennevières (RER A)"],
            "see": ["Banks of the Marne", "Vieux Saint-Maur and the Tour Rabelais", "La Varenne"],
            "guests": "Families, quiet stays near Paris, visiting relatives"}},
]

# Communes citées sur l'ancien site, sans page dédiée pour l'instant.
IDF = ["Versailles", "Boulogne-Billancourt", "Neuilly-sur-Seine", "Levallois-Perret", "Vincennes", "Saint-Mandé",
       "Rueil-Malmaison", "Suresnes", "Asnières-sur-Seine", "Colombes", "Clamart", "Antony", "Charenton-le-Pont",
       "Joinville-le-Pont", "Sucy-en-Brie", "Boissy-Saint-Léger"]

BY_ID = {a["id"]: a for a in AREAS + TOWNS}

SEO_TITLES = {
    "marais": ("Le Marais, Paris 3e-4e", "Le Marais, Paris 3rd-4th"), "montmartre": ("Montmartre, Paris 18e", "Montmartre, Paris 18th"),
    "saint-germain-des-pres": ("Saint-Germain-des-Prés", "Saint-Germain-des-Prés"),
    "quartier-latin": ("Quartier latin, Paris 5e", "Latin Quarter, Paris 5th"), "tour-eiffel": ("Tour Eiffel, Paris 7e", "Eiffel Tower, Paris 7th"),
    "champs-elysees": ("Champs-Élysées, Paris 8e", "Champs-Élysées, Paris 8th"), "opera": ("Opéra, Paris 9e", "Opéra, Paris 9th"),
    "louvre": ("Louvre, Paris 1er", "Louvre, Paris 1st"), "canal-saint-martin": ("Canal Saint-Martin, Paris 10e", "Canal Saint-Martin, Paris 10th"),
    "bastille": ("Bastille, Paris 11e-12e", "Bastille, Paris 11th-12th"), "montparnasse": ("Montparnasse, Paris 14e", "Montparnasse, Paris 14th"),
    "trocadero": ("Trocadéro, Paris 16e", "Trocadéro, Paris 16th"), "creteil": ("Créteil (94)", "Créteil (94)"),
    "saint-maur": ("Saint-Maur-des-Fossés (94)", "Saint-Maur-des-Fossés (94)"),
}


def seo_desc(a, L):
    """Description unique par page : le quartier, ce qui le caractérise, puis le service (version courte si trop long)."""
    d = a[L]
    if L == "fr":
        options = [f"Conciergerie Airbnb {d['prep']}. {d['teaser']} Annonce, voyageurs, clés et ménage pour votre meublé.",
                   f"Conciergerie Airbnb {d['prep']}. {d['teaser']} Annonce, voyageurs, clés et ménage.",
                   f"Conciergerie Airbnb {d['prep']}. {d['teaser']}"]
    else:
        options = [f"Airbnb management {d['prep']}. {d['teaser']} Listing, guests, keys and cleaning for your furnished home.",
                   f"Airbnb management {d['prep']}. {d['teaser']} Listing, guests, keys and cleaning.",
                   f"Airbnb management {d['prep']}. {d['teaser']}"]
    return next((o for o in options if len(o) <= 158), options[-1])


def area_url(a, L):
    """Adresses à plat, sur le modèle des pages de communes de l'ancien site (/conciergerie-airbnb-creteil)."""
    if "route" in a:
        return a["route"][L]
    return ("/conciergerie-airbnb-" if L == "fr" else "/en/airbnb-management-") + a["slug"][L]


def area_img(a, L, sizes="(max-width: 700px) 90vw, 290px", lazy=True):
    p = photos.AREA[a["id"]]
    return photo(p["file"], p["alt"][L], sizes=sizes, lazy=lazy, big=p["big"])


def area_card(a, L, h="h3"):
    d = a[L]
    return (f'<a class="area-card" href="{area_url(a, L)}"><div class="ph">{area_img(a, L)}</div>'
            f'<{h}>{d["name"]}{icon("arrow")}</{h}><small>{d["arr"]} · {d["teaser"]}</small></a>')


def credit(a, L):
    t = tr(L)
    p = photos.AREA[a["id"]]
    if not p.get("author"):
        return ""
    return (f'<p class="credit">{t("Photo", "Photo")} : <a href="{p["page"]}" target="_blank" rel="noopener">{p["author"]}</a>, '
            f'<a href="{p["license_url"]}" target="_blank" rel="noopener">{p["license"]}</a>, Wikimedia Commons</p>')


def rules(L):
    t = tr(L)
    cards = [
        ("green-s", t("90 jours par an", "90 days a year"),
         t("C'est le maximum pour louer votre résidence principale en meublé de tourisme à Paris, depuis le 1er janvier 2025.",
           "The maximum for letting your main residence as furnished tourist accommodation in Paris, since 1 January 2025.")),
        ("coral-s", t("Numéro d'enregistrement", "Registration number"),
         t("Le logement doit être déclaré à la Ville ; son numéro figure sur chaque annonce.",
           "The property must be declared to the City; its number appears on every listing.")),
        ("blue-s", t("Changement d'usage", "Change of use"),
         t("Louer une résidence secondaire en courte durée demande une autorisation de la Ville, en général avec compensation.",
           "Letting a second home for short stays requires City authorisation, usually with compensation.")),
        ("sand-s", t("Accord du propriétaire", "Landlord's consent"),
         t("Locataire ? Il vous faut l'accord écrit de votre propriétaire pour sous-louer.",
           "Renting? You need your landlord's written consent to sublet.")),
    ]
    items = "".join(f'<div class="rule {c}"><b>{b}</b><span>{s}</span></div>' for c, b, s in cards)
    note = t('Ces règles évoluent : vérifiez-les avant toute mise en location sur <a href="https://www.paris.fr/meubles-touristiques" target="_blank" rel="noopener">paris.fr</a>.',
             'These rules change: check them before letting on <a href="https://www.paris.fr/meubles-touristiques" target="_blank" rel="noopener">paris.fr</a> (in French).')
    return f'<div class="rules">{items}</div><p class="note">{note}</p>'


def minis(L):
    t = tr(L)
    tiles = [
        ("green-s", "appareil", t("Annonce et photos", "Listing and photos"), t("Photos prises par nos soins, annonce en français et en anglais.", "Photos taken by us, listing in French and English."), "voyageurs"),
        ("coral-s", "identite", t("Sélection des voyageurs", "Guest screening"), t("Profils vérifiés, pièce d'identité obligatoire.", "Verified profiles, ID required."), "voyageurs"),
        ("blue-s", "cles", t("Clés et accueil", "Keys and welcome"), t("En main propre, par un café partenaire ou à distance.", "In person, via a partner café or remotely."), "voyageurs"),
        ("sand-s", "menage", t("Ménage et linge", "Cleaning and linen"), t("Après chaque départ, consommables compris.", "After every check-out, consumables included."), "logement"),
    ]
    return '<div class="minis">' + "".join(
        f'<a class="mini {c}" href="{url(p, L)}">{illu(i)}<b>{b}</b><span>{s}</span></a>' for c, i, b, s, p in tiles) + "</div>"


def plans_strip(L):
    t = tr(L)
    return f"""<div class="plans">
  <div class="plan green-s reveal">{illu("maison")}{chip(t("Formule 1", "Plan 1"))}<h3>{t("Revenu garanti", "Guaranteed income")}</h3>
    <p class="big">{t("≈ 15 %", "≈ 15%")}<small>{t("de marge moyenne pour EdenFlats, et un revenu versé que le logement soit loué ou non", "average margin for EdenFlats, with an income paid whether or not the apartment is booked")}</small></p>
    {more(url("formules", L), t("Comparer les formules", "Compare the plans"))}</div>
  <div class="plan blue-s reveal">{illu("graphique")}{chip(t("Formule 2", "Plan 2"))}<h3>{t("Revenu réel", "Actual income")}</h3>
    <p class="big">{t("18 à 25 %", "18–25%")}<small>{t("de commission selon la durée de location, avec un prix minimum par nuit que vous fixez", "commission depending on rental length, with a minimum nightly price that you set")}</small></p>
    {more(url("formules", L), t("Comparer les formules", "Compare the plans"))}</div>
</div>"""


def area_page(a, L):
    t = tr(L)
    d = a[L]
    is_town = "route" in a
    path = area_url(a, L)
    trail = ([(d["name"], path)] if is_town else [("Paris", url("paris", L)), (d["name"], path)])
    h1 = t(f"Conciergerie Airbnb <mark>{d['prep']}</mark>", f"Airbnb management <mark>{d['prep']}</mark>")
    visual = f"""<div class="hero-visual">
        <figure class="hero-photo">{area_img(a, L, sizes="(max-width: 900px) 100vw, 45vw", lazy=False)}</figure>
        {fcard(t("Métro et RER", "Metro and RER") if not is_town else t("Transports", "Transport"), "t-blue", ", ".join(d["transit"][:2]), "fc-1", "train")}
        {fcard(t("À voir", "Nearby"), "t-green", ", ".join(d["see"][:2]), "fc-3", "eye")}
      </div>{credit(a, L)}"""
    facts = [("pin", t("Situation", "Location"), d["arr"]),
             ("train", t("Métro et RER", "Metro and RER") if not is_town else t("Transports", "Transport"), " · ".join(d["transit"])),
             ("eye", t("À voir", "Nearby"), " · ".join(d["see"])),
             ("users", t("Voyageurs", "Guests"), d["guests"])]
    facts_html = "".join(f"<div>{icon(i)}<dt>{k}</dt><dd>{v}</dd></div>" for i, k, v in facts)
    neigh = "".join(area_card(BY_ID[n], L) for n in a["neighbors"])
    neigh_title = t("Communes voisines", "Nearby towns") if is_town else t("Quartiers voisins", "Nearby neighbourhoods")
    rules_block = ""
    if not is_town:
        rules_block = f"""<section class="sec tight"><div class="wrap">
  {head(t("Réglementation", "Regulations"), t("Louer à Paris : l'essentiel", "Letting in Paris: the essentials"))}
  {rules(L)}
</div></section>"""
    else:
        rules_block = f"""<section class="sec tight"><div class="wrap">
  <div class="rule cream-s" style="max-width:780px"><b>{t("Les règles dépendent de la commune", "The rules depend on the town")}</b>
  <span>{t("Déclaration en mairie, numéro d'enregistrement sur l'annonce, autorisation de changement d'usage pour une résidence secondaire : renseignez-vous auprès de votre mairie avant la mise en location.",
           "Declaration to the town hall, registration number on the listing, change-of-use authorisation for a second home: check with your town hall before letting.")}
  {more(url("faq", L) + "#reglementation", t("Lire notre réponse sur la législation", "Read our answer on the rules"))}</span></div>
</div></section>"""
    body = f"""<section class="phead">
  <div class="phead-panel panel">
    <div class="wrap phead-grid">
      <div>{crumbs(L, trail)}{chip(d["arr"])}<h1>{h1}</h1><p class="lead">{d["lead"]}</p>
        <div class="cta-row">{btn(url("contact", L), t("Parlez-nous de votre logement", "Tell us about your property"))}{btn(url("formules", L), t("Voir nos formules", "See our plans"), "ghost")}</div></div>
      <div>{visual}</div>
    </div>
  </div>
</section>
<section class="sec"><div class="wrap two">
  <div class="prose">
    <h2>{t("Louer un meublé", "Letting a furnished home")} {d["prep"]}</h2>
    <p>{d["p1"]}</p><p>{d["p2"]}</p>
    <h2>{t("Votre logement", "Your home")} {d["prep"]}{t(", géré par EdenFlats", ", managed by EdenFlats")}</h2>
    <p>{d["ours"]}</p>
    <p>{t(f'Nous prenons en charge la <a href="{url("voyageurs", L)}">gestion des voyageurs</a> (annonce, sélection, clés, assistance) et la <a href="{url("logement", L)}">gestion du logement</a> (ménage, linge, entretien), avec <a href="{url("formules", L)}">un revenu garanti ou un revenu réel</a>. Les questions des propriétaires sont dans notre <a href="{url("faq", L)}">FAQ</a>.',
          f'We handle <a href="{url("voyageurs", L)}">guest management</a> (listing, screening, keys, support) and <a href="{url("logement", L)}">property management</a> (cleaning, linen, upkeep), with <a href="{url("formules", L)}">a guaranteed or an actual income</a>. Owners’ questions are answered in our <a href="{url("faq", L)}">FAQ</a>.')}</p>
    {minis(L)}
  </div>
  <aside class="facts cream-s" aria-label="{t("Repères", "Key facts")}"><h3>{t("Repères", "Key facts")}</h3><dl>{facts_html}</dl></aside>
</div></section>
<section class="sec tight"><div class="wrap">
  {head(t("Nos formules", "Our plans"), t("Revenu garanti ou revenu réel", "Guaranteed or actual income"))}
  {plans_strip(L)}
</div></section>
{rules_block}
<section class="sec tight"><div class="wrap">
  {head(t("Autour", "Around"), neigh_title)}
  <div class="areas">{neigh}</div>
  <p class="note">{more(url("paris", L), t("Tous les quartiers de Paris", "All Paris neighbourhoods"))}</p>
</div></section>"""
    st = SEO_TITLES[a["id"]]
    title = t(f"Conciergerie Airbnb {st[0]} | EdenFlats", f"Airbnb Management {st[1]} | EdenFlats")
    desc = seo_desc(a, L)
    cta_title = t(f'Un logement {d["prep"]} ? <span class="o">Parlons-en.</span>', f'A property {d["prep"]}? <span class="o">Let\'s talk.</span>')
    p = photos.AREA[a["id"]]
    area_name = d["name"] if is_town else f'{d["name"]}, Paris'
    ld = [crumbs_ld(L, trail), service_ld(L, t(f"Conciergerie Airbnb {d['prep']}", f"Airbnb management {d['prep']}"), desc, path, area=area_name)]
    return {"path": path, "alt_path": area_url(a, "en" if L == "fr" else "fr"), "title": title, "desc": desc, "body": body,
            "ld": ld, "cta_title": cta_title, "og_image": f'/assets/img/{p["file"]}.jpg', "og_alt": p["alt"][L],
            "section": None if is_town else "paris", "image": f'/assets/img/{p["file"]}.jpg'}


def hub(L):
    t = tr(L)
    p = photos.AREA["paris"]
    cards = "".join(area_card(a, L) for a in AREAS)
    town_chips = "".join(f'<a class="chip" href="{area_url(a, L)}">{a[L]["name"]} {icon("arrow")}</a>' for a in TOWNS)
    others = "".join(f'<span class="chip">{n}</span>' for n in IDF)
    cred = ""
    if p.get("author"):
        cred = (f'<p class="credit">{t("Photo", "Photo")} : <a href="{p["page"]}" target="_blank" rel="noopener">{p["author"]}</a>, '
                f'<a href="{p["license_url"]}" target="_blank" rel="noopener">{p["license"]}</a>, Wikimedia Commons</p>')
    trail = [("Paris", url("paris", L))]
    body = f"""<section class="phead">
  <div class="phead-panel panel">
    <div class="wrap phead-grid">
      <div>{crumbs(L, trail)}{chip(t("Paris et Île-de-France", "Paris and Île-de-France"))}
        <h1>{t("Conciergerie Airbnb <mark>à Paris</mark>", "Airbnb management <mark>in Paris</mark>")}</h1>
        <p class="lead">{t("Du Marais à Montmartre, de Saint-Germain-des-Prés au Trocadéro : nous gérons la location saisonnière de votre logement dans les quartiers que les voyageurs viennent chercher.",
                          "From Le Marais to Montmartre, from Saint-Germain-des-Prés to Trocadéro: we manage short-term rentals in the neighbourhoods guests come looking for.")}</p>
        <div class="cta-row">{btn(url("contact", L), t("Parlez-nous de votre logement", "Tell us about your property"))}{btn("#quartiers", t("Voir les quartiers", "See the neighbourhoods"), "ghost")}</div></div>
      <div><div class="hero-visual">
        <figure class="hero-photo">{photo(p["file"], p["alt"][L], sizes="(max-width: 900px) 100vw, 45vw", lazy=False, big=p["big"])}</figure>
        {fcard("Paris", "t-green", t("Résidence principale : 90 jours de location par an au maximum.", "Main residence: up to 90 rental days a year."), "fc-1", "calendar")}
        {fcard(t("Annonce", "Listing"), "t-coral", t("Numéro d'enregistrement affiché sur chaque annonce.", "Registration number shown on every listing."), "fc-3", "id")}
      </div>{cred}</div>
    </div>
  </div>
</section>
<section class="sec" id="quartiers"><div class="wrap">
  {head(t("Les quartiers", "Neighbourhoods"), t("Chaque quartier a ses voyageurs", "Every neighbourhood has its own guests"),
        t("Familles autour de la tour Eiffel, voyageurs d'affaires aux Champs-Élysées, chercheurs au Quartier latin : nous adaptons l'annonce, les prix et l'accueil au quartier de votre logement.",
          "Families around the Eiffel Tower, business travellers on the Champs-Élysées, researchers in the Latin Quarter: we adapt the listing, the prices and the welcome to your neighbourhood."))}
  <div class="areas">{cards}</div>
  <p class="note">{t("Photos : Wikimedia Commons,", "Photos: Wikimedia Commons,")} <a href="{url("credits", L)}">{t("voir les crédits", "see credits")}</a>.</p>
</div></section>
<section class="sec tight"><div class="wrap">
  {head(t("Réglementation", "Regulations"), t("Louer à Paris : les règles à connaître", "Letting in Paris: the rules to know"))}
  {rules(L)}
</div></section>
<section class="sec tight"><div class="wrap">
  {head(t("Île-de-France", "Île-de-France"), t("Et autour de Paris", "And around Paris"),
        t("Nous gérons aussi des logements dans de nombreuses communes d'Île-de-France. Votre commune n'est pas dans la liste ? Demandez-nous si nous intervenons chez vous.",
          "We also manage homes in many towns of Île-de-France. Your town isn't listed? Ask us whether we cover it."))}
  <div class="cta-row">{town_chips}{others}</div>
</div></section>"""
    title = t("Conciergerie Airbnb à Paris : nos quartiers | EdenFlats", "Airbnb management in Paris: our neighbourhoods | EdenFlats")
    desc = t("Conciergerie Airbnb à Paris, du Marais à Montmartre et à la tour Eiffel : annonce, voyageurs, clés, ménage, et les règles de location à Paris (90 jours).",
             "Airbnb management across Paris, from Le Marais to Montmartre and the Eiffel Tower: listing, guests, keys and cleaning, plus the Paris rental rules.")
    ld = [crumbs_ld(L, trail), service_ld(L, t("Conciergerie Airbnb à Paris", "Airbnb management in Paris"), desc, url("paris", L), area="Paris")]
    return {"title": title, "desc": desc, "body": body, "ld": ld, "og_image": f'/assets/img/{p["file"]}.jpg', "og_alt": p["alt"][L],
            "section": "paris", "image": f'/assets/img/{p["file"]}.jpg'}


def where(L, illus_name="tour-eiffel", tone="blue-s"):
    """Bloc de liens vers chaque quartier : il relie les pages de services aux pages locales (maillage interne)."""
    t = tr(L)
    chips = "".join(f'<a class="chip" href="{area_url(a, L)}">{a[L]["name"]}</a>' for a in AREAS + TOWNS)
    text = t(f'Nous gérons des logements dans tout Paris et en Île-de-France. Chaque quartier a sa page : les voyageurs qui y séjournent, les transports, ce que nous faisons pour votre logement. Voir la <a href="{url("paris", L)}">conciergerie Airbnb à Paris</a>.',
             f'We manage homes all over Paris and Île-de-France. Each neighbourhood has its own page: who stays there, transport, what we do for your home. See <a href="{url("paris", L)}">Airbnb management in Paris</a>.')
    return f"""<section class="sec tight"><div class="wrap"><div class="where {tone}">
  {illu(illus_name)}
  <div><h2>{t("Où nous intervenons", "Where we work")}</h2><p>{text}</p><div class="cta-row">{chips}</div></div>
</div></div></section>"""
