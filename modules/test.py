from database import *
db = Database(dbtype='sqlite', username='root', password='', dbname='animals.db')

type1 = Type()
type1.full_name = "ryby"
db.create_type(type1)

animal1 = Animal()
animal1.name = "Klaun Očkatý"
animal1.typee = 1
animal1.info = "Klaun očkatý (Amphiprion ocellaris) je druh tropické ryby z čeledi sapínovití (Pomacentridae) a rodu Amphiprion. Druh popsal roku 1830 Georges Cuvier."
db.create_animal(animal1)

photo1 = Photo()
photo1.title = "Klaun Očkatý"
photo1.source = "https://www.zoohit.cz/magazin/wp-content/uploads/2018/12/Klaunni-ryba.jpg"
db.create_photo(photo1)

type2 = Type()
type2.full_name = "savci"
db.create_type(type2)

animal2 = Animal()
animal2.name = "Kočka domácí"
animal2.typee = 2
animal2.info = "Kočka domácí (Felis silvestris f. catus) je domestikovaná forma kočky plavé, která je již po tisíciletí průvodcem člověka. Stejně jako její divoká příbuzná patří do podčeledi malé kočky, a je typickým zástupcem skupiny."
db.create_animal(animal2)

photo2 = Photo()
photo2.title= "Kočka domácí"
photo2.source = "https://www.zooo.cz/content/fck/images/kocka-domaci.jpg"
db.create_photo(photo2)