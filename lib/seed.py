
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.painting import Painting
from models.movement import Movement

movements = ["'85 New Wave", 'Abstract Expressionism', 'American Impressionism', 
             'Ancient Egyptian', 'Arab Modernism', 'Art Deco', 'Art Noveau', 
             'Arte Povera', 'Arts and Crafts', 'Asuka', 'Azuchi-Momoyama', 
             'Baroda Group of Artists', 'Bauhaus', 'Bengal School', 
             'Bombay Progressives', 'Byzantine', 'Calcutta Group', 
             'Colonial Era', 'Constructivism', 'Contemporary Art', 
             'Cretan School', 'Cubism', 'Dada', 'De Stijl', 'Deconstructivism', 
             'E-maki', 'Edo', 'Expressionism', 'Fauvism', 
             'Five Dynasties and Ten Kingdoms', 'Fujiwara', 'Fururism', 'Gothic', 
             'Guohua', 'Gutai', 'Han Dynasty', 'Harlem Renaissance', 
             'Heidelberg School', 'Hellenistic', 'Heptanese School', 
             'Hudson River School', 'Hurufiyya', 'Impressionism', 'Jin Dynasty', 
             'Kamakura', 'Kano School', 'Kofun', 'Lowbrow', 'Luminism', 
             'Mannerism', 'Meiji', 'Mesopotamian', 'Ming Dynasty', 'Minimalism', 
             'Modern Woodcut', 'Mughal Era', 'Muromachi', 'Naqqashikatt', 
             'Nara', 'Naturalism', 'Neo-impressionism', 'Neoclassicism', 
             'New Objectivity', 'Northern Dynasty', 'Op Art', 'Photorealism', 
             'Pop Art', 'Post-Impressionism', 'Postmodernism', 'Pre-Raphaelite', 
             'Precisionism', 'Prehistoric', 'Progressive Artists Group', 
             'Qin Dynasty', 'Qing Dynasty', 'Rayonism', 
             'Rococo', 'Romanesque', 'Romanticism', 'Russian Futurism', 
             'Russian avant-garde', 'Saqqakhaneh', 'Shang Dynasty', 
             'Song Dynasty', 'Southern Dynasty', 'Stone Age', 'Sui Dynasty', 
             'Suprematism', 'Symbolism', 'Tang Dynasty', 
             'Three Kingdoms', 'Tonalism', 'Xia Dynasty', 'Yuan Dynasty', 
             'Zhou Dynasty', 'Socialist Realism']

def seed_database():
    Artist.drop_table()
    Painting.drop_table()
    Movement.drop_table()
    Artist.create_table()
    Painting.create_table()
    Movement.create_table()

    academicism = Movement.create("Academicism")
    baroque = Movement.create("Baroque")
    neo_expressionism = Movement.create("Neo-Expressionism")
    surrealism = Movement.create("Surrealism")
    realism = Movement.create("Realism")
    renaissance = Movement.create("Renaissance")

    for movement in movements:
        Movement.create(movement)

    basquiat = Artist.create("Jean-Michel Basquiat", neo_expressionism.id)
    cabanel = Artist.create("Alexandre Cabanel", academicism.id)
    dali = Artist.create("Salvador Dali", surrealism.id)
    gentileschi = Artist.create("Artemisia Gentileschi", baroque.id)
    magritte = Artist.create("René Magritte", surrealism.id)
    hopper = Artist.create("Edward Hopper", realism.id)
    
    Artist.create("Leonardo da Vinci", renaissance.id)
    Artist.create("Raphael", renaissance.id)
    Artist.create("Edouard Manet", realism.id)

    Painting.create("Judith Slaying Holofernes", "1620", "oil", gentileschi.id)
    Painting.create("The Elephants", "1948", "oil", dali.id)
    Painting.create("The Fallen Angel", "1847", "oil", cabanel.id)
    Painting.create("The Temptation of St. Anthony", "1946", "oil", dali.id)
    Painting.create("Untitled (Skull)", "1981", "acrylic", basquiat.id)
    Painting.create("The Son of Man", "1964", "oil", magritte.id)
    Painting.create("The Treachery of Images", "1929", "oil", magritte.id)
    Painting.create("Nighthawks", "1942", "oil", hopper.id)
    Painting.create("Time Transfixed", "1938", "oil", magritte.id)

seed_database()
print("Seeded database")
