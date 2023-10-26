
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.painting import Painting
from models.movement import Movement

movements = [("'85 New Wave", 1985), ('American Impressionism', 1890), 
             ('Art Deco', 1919), ('Art Noveau', 1890), ('Arte Povera', 1967), ('Arts and Crafts', 1875), 
             ('Asuka', 552), ('Azuchi-Momoyama', 1573), ('Baroda Group of Artists', 1957), ('Bauhaus', 1919), 
             ('Bengal School', 1900), ('Bombay Progressives', 1947), ('Byzantine', 330), 
             ('Calcutta Group', 1943), ('Constructivism', 1915), 
             ('Cretan School', 1400), ('Cubism', 1907), ('Dada', 1916), ('De Stijl', 1917), 
             ('Deconstructivism', 1980), ('E-maki', 735), ('Edo', 1615), 
             ('Five Dynasties and Ten Kingdoms', 907), ('Fujiwara', 897), ('Futurism', 1909), 
             ('Gothic', 1150), ('Guohua', 618), ('Gutai', 1954), ('Han Dynasty', 0), ('Harlem Renaissance', 1918), 
             ('Heidelberg School', 1886), ('Heptanese School', 1650), ('Hudson River School', 1825), 
             ('Hurufiyya', 1400), ('Jin Dynasty', 265), ('Kamakura', 1185), ('Kano School', 1450), ('Kofun', 250), 
             ('Lowbrow', 1965), ('Luminism', 1850), ('Mannerism', 1520), ('Meiji', 1868), ('Ming Dynasty', 1368), 
             ('Minimalism', 1960), ('Mughal Era', 1580), ('Muromachi', 1333), ('Naqqashikatt', 1950), ('Nara', 1990), 
             ('Naturalism', 1875), ('Neo-impressionism', 1886), ('Neoclassicism', 1760), 
             ('New Objectivity', 1920), ('Northern Dynasty', 439), ('Op Art', 1960), ('Photorealism', 1965), 
             ('Pop Art', 1955), ('Postmodernism', 1960), ('Pre-Raphaelite', 1848), ('Precisionism', 1920), 
             ('Progressive Artists Group', 1947), ('Qing Dynasty', 1644), ('Rayonism', 1910), ('Rococo', 1723), 
             ('Romanesque', 1000), ('Russian Futurism', 1912), ('Russian avant-garde', 1912), 
             ('Saqqakhaneh', 1950), ('Song Dynasty', 960), ('Southern Dynasty', 420), ('Sui Dynasty', 581), 
             ('Suprematism', 1915), ('Symbolism', 1880), ('Tang Dynasty', 618), ('Three Kingdoms', 222), 
             ('Tonalism', 1880), ('Yuan Dynasty', 1271), ('Socialist Realism', 1932)]

def seed_database():
    Artist.drop_table()
    Painting.drop_table()
    Movement.drop_table()
    Artist.create_table()
    Painting.create_table()
    Movement.create_table()

    academicism = Movement.create("Academicism", 1560)
    baroque = Movement.create("Baroque", 1585)
    neo_expressionism = Movement.create("Neo-Expressionism", 1970)
    surrealism = Movement.create("Surrealism", 1917)
    realism = Movement.create("Realism", 1840)
    renaissance = Movement.create("Renaissance", 1450)
    post_impressionism = Movement.create("Post-Impressionism", 1886)
    expressionism = Movement.create("Expressionism", 1905)
    romanticism = Movement.create("Romanticism", 1798)
    contemporary_art = Movement.create("Contemporary Art", 1945)
    impressionism = Movement.create("Impressionism", 1874)
    fauvism = Movement.create("Fauvism", 1905)
    abstract_expressionism = Movement.create("Abstract Expressionism", 1943)

    for movement in movements:
        Movement.create(movement[0], movement[1])

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
    boticelli = Artist.create("Sandro Botticelli", renaissance.id)

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
    Painting.create("Self-portrait", "1506", "oil", raphael.id)
    Painting.create("The Birth of Venus", "1486", "tempera", boticelli.id)

seed_database()
print("Seeded database")
