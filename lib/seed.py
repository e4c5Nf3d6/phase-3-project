
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.painting import Painting
from models.movement import Movement

def seed_database():
    Artist.drop_table()
    Painting.drop_table()
    Movement.drop_table()
    Artist.create_table()
    Painting.create_table()
    Movement.create_table()

seed_database()
print("Seeded database")

movements = ["'85 New Wave", 'Abstract Expressionism', 'American Impressionism', 
             'Ancient Egyptian', 'Arab Modernism', 'Art Deco', 'Art Noveau', 
             'Arte Povera', 'Arts and Crafts', 'Asuka', 'Azuchi-Momoyama', 
             'Baroda Group of Artists', 'Baroque', 'Bauhaus', 'Bengal School', 
             'Bombay Progressives', 'Byzantine', 'Calcutta Group', 
             'Colonial Era', 'Constructivism', 'Contemporary Art', 
             'Cretan School', 'Cubism', 'De Stijl', 'Deconstructivism', 
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
             'Qin Dynasty', 'Qing Dynasty', 'Rayonism', 'Realism', 'Renaissance', 
             'Rococo', 'Romanesque', 'Romanticism', 'Russian Futurism', 
             'Russian avant-garde', 'Saqqakhaneh', 'Shang Dynasty', 
             'Song Dynasty', 'Southern Dynasty', 'Stone Age', 'Sui Dynasty', 
             'SuprematismDadaism', 'Surrealism', 'Symbolism', 'Tang Dynasty', 
             'Three Kingdoms', 'Tonalism', 'Xia Dynasty', 'Yuan Dynasty', 
             'Zhou Dynasty', 'Socialist Realism']

 