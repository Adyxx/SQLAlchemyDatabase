from database import *
db = Database(dbtype='sqlite', username='root', password='', dbname='animals.db')

typee = Type()
typee.full_name = "ryby"
db.create_type(typee)

animal = Animal()
animal.name = "Klaun Očkatý"
animal.typee = 1
animal.info = "Klaun očkatý (Amphiprion ocellaris) je druh tropické ryby z čeledi sapínovití (Pomacentridae) a rodu Amphiprion. Druh popsal roku 1830 Georges Cuvier."
db.create_animal(animal)

photo = Photo()
photo.title = "Klaun Očkatý"
photo.source = "https://www.zoohit.cz/magazin/wp-content/uploads/2018/12/Klaunni-ryba.jpg"
db.create_photo(photo)

typee = Type()
typee.full_name = "savci"
db.create_type(typee)

animal = Animal()
animal.name = "Kočka domácí"
animal.typee = 2
animal.info = "Kočka domácí (Felis silvestris f. catus) je domestikovaná forma kočky plavé, která je již po tisíciletí průvodcem člověka. Stejně jako její divoká příbuzná patří do podčeledi malé kočky, a je typickým zástupcem skupiny."
db.create_animal(animal)

photo = Photo()
photo.title= "Kočka domácí"
photo.source = "https://www.zooo.cz/content/fck/images/kocka-domaci.jpg"
db.create_photo(photo)