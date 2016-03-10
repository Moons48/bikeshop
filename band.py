class Musician(object):
    def __init__(self, name, sounds):
        self.sounds = sounds
        self.name = name
        
    def join_band(self, band_name):
        self.name.hire_member(self)

    def solo(self, length):
        for i in range(length):
            print self.sounds

        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self, name, sounds):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(name, sounds)

        
class Guitarist(Musician):
    def __init__(self, name, sounds):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self, name, sounds):
        #call the __init__ method of the parent class
        super(Drummer, self).__init__(name, sounds)
        
    def count(self):
        for count in range(1,5):
            print count
            
    def combust(self):
        print "The drummer exploded"
        
        
class Band():
    def __init__(self, name, genre="rock"):
        self.name = name
        self.genre = genre
        self.members = []
        
        
    def hire_member(self, name):
        self.members.append(name)
        print "the band now consists of:"
        for num, name in enumerate(self.members):
            print i, v
        
        
    def fire_members(self, name):
        self.members.remove(name)
        print "the band now consists of:"
        for num, name in enumerate(self.members):
            print i, v
            
    def introduce_band(self):
        print "We are %s! The best %s band in the world!"%(self.name, self.genre)

Metallica = Band("Metallica")
Metallica.introduce_band()
Lars = Drummer("Lars",["bam", "bam"])
Lars.join_band(Metallica)
Lars.solo(6)
