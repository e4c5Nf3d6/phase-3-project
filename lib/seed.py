
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.painting import Painting
from models.movement import Movement

movements = ["'85 New Wave", 'American Impressionism', 'Ancient Egyptian', 
             'Arab Modernism', 'Art Deco', 'Art Noveau', 'Arte Povera', 
             'Arts and Crafts', 'Asuka', 'Azuchi-Momoyama', 
             'Baroda Group of Artists', 'Bauhaus', 'Bengal School', 
             'Bombay Progressives', 'Byzantine', 'Calcutta Group', 
             'Colonial Era', 'Constructivism', 'Cretan School', 'Cubism', 
             'Dada', 'De Stijl', 'Deconstructivism', 'E-maki', 'Edo', 
             'Five Dynasties and Ten Kingdoms', 'Fujiwara', 'Fururism', 
             'Gothic', 'Guohua', 'Gutai', 'Han Dynasty', 'Harlem Renaissance', 
             'Heidelberg School', 'Hellenistic', 'Heptanese School', 
             'Hudson River School', 'Hurufiyya', 'Jin Dynasty', 'Kamakura', 
             'Kano School', 'Kofun', 'Lowbrow', 'Luminism', 'Mannerism', 
             'Meiji', 'Mesopotamian', 'Ming Dynasty', 'Minimalism', 
             'Mughal Era', 'Muromachi', 'Naqqashikatt', 'Nara', 'Naturalism', 
             'Neo-impressionism', 'Neoclassicism', 'New Objectivity', 
             'Northern Dynasty', 'Op Art', 'Photorealism', 'Pop Art', 
             'Postmodernism', 'Pre-Raphaelite', 'Precisionism', 
             'Prehistoric', 'Progressive Artists Group', 'Qin Dynasty', 
             'Qing Dynasty', 'Rayonism', 'Rococo', 'Romanesque', 
             'Russian Futurism', 'Russian avant-garde', 'Saqqakhaneh', 
             'Shang Dynasty', 'Song Dynasty', 'Southern Dynasty', 'Stone Age', 
             'Sui Dynasty', 'Suprematism', 'Symbolism', 'Tang Dynasty', 
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
    post_impressionism = Movement.create("Post-Impressionism")
    expressionism = Movement.create("Expressionism")
    romanticism = Movement.create("Romanticism")
    contemporary_art = Movement.create("Contemporary Art")
    impressionism = Movement.create("Impressionism")
    fauvism = Movement.create("Fauvism")
    abstract_expressionism = Movement.create("Abstract Expressionism")

    for movement in movements:
        Movement.create(movement)

    basquiat = Artist.create("Jean-Michel Basquiat", neo_expressionism.id)
    cabanel = Artist.create("Alexandre Cabanel", academicism.id)
    dali = Artist.create("Salvador Dali", surrealism.id)
    gentileschi = Artist.create("Artemisia Gentileschi", baroque.id)
    magritte = Artist.create("René Magritte", surrealism.id)
    hopper = Artist.create("Edward Hopper", realism.id)
    goya = Artist.create("Francisco Goya", romanticism.id)
    ivchenkova = Artist.create("Tatiana Ivchenkova", contemporary_art.id)
    durer = Artist.create("Albrecht Durer", renaissance.id)
    sargent = Artist.create("John Singer Sargent", impressionism.id)
    rothko = Artist.create("Mark Rothko", abstract_expressionism.id)
    kline = Artist.create("Martin Kline", contemporary_art.id)
    raphael = Artist.create("Raphael", renaissance.id)

    Artist.create("Vincent van Gogh", post_impressionism.id) 
    Artist.create("Leonardo da Vinci", renaissance.id)
    Artist.create("Edouard Manet", realism.id)
    Artist.create("Frida Kahlo", surrealism.id)
    Artist.create("Edvard Munch", expressionism.id)
    Artist.create("Henri Matisse", fauvism.id)

    Painting.create("Judith Slaying Holofernes", "1620", "oil", gentileschi.id)
    Painting.create("The Elephants", "1948", "oil", dali.id)
    Painting.create("The Fallen Angel", "1847", "oil", cabanel.id)
    Painting.create("The Temptation of St. Anthony", "1946", "oil", dali.id)
    Painting.create("Untitled (Skull)", "1981", "acrylic", basquiat.id)
    Painting.create("The Son of Man", "1964", "oil", magritte.id)
    Painting.create("The Treachery of Images", "1929", "oil", magritte.id)
    Painting.create("Nighthawks", "1942", "oil", hopper.id)
    Painting.create("Time Transfixed", "1938", "oil", magritte.id)
    Painting.create("Witches' Sabbath", "1798", "oil", goya.id)
    Painting.create("Brown", "2020", "watercolor", ivchenkova.id)
    Painting.create("Wing Of A European Roller", "1512", "watercolor", durer.id)
    Painting.create("Muddy Alligators", "1917", "watercolor", sargent.id)
    Painting.create("Untitled (Brown and Gray)", "1969", "acrylic", rothko.id)
    Painting.create("Dorian Gray", "2011", "encaustic", kline.id)
    Painting.create("The School of Athens", "1511", "fresco", raphael.id)

seed_database()
print("Seeded database")
