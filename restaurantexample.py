# We have TABLES of various sorts in a room
# Associated with each table we have a waitress and multiple customers

# We're running a restuarant, seating guests, etc!

# to example t6, we have added some further OO demos
#       - a factory method (static call that returns a constructor)
#       - a comparator to compare two objects derived from the same base
#       - a static method to compare a whole list of similar objects
#       - a method to print out an object by overriding the default

class person (object):
        def getname(self):
                return self.name

class customer(person):
        def __init__(self,name,partysize):
                self.name = name
                self.partysize = partysize
        def getsize(self):
                return self.partysize

class waitress(person):
        def __init__(self,name,capacity):
                self.name = name
                self.capacity = capacity
                self.ccc = 0            # self customer count / not yet used

# ---------------------------------------------------

class table(object):
        def __init__(self,material,w,h,wt):
                self._sng(material,wt)
                self.w = w
                self.h = h
                self.place = 925
        def getbums(self):
                side = int(self.w/self.place)
                wide = int(self.h/self.place)
                return 2 * (side + wide)
        def setplace(self,p):
                self.place = p
        def getdoggie(self):
                if self.w < self.h:
                        return self.w/2
                return self.h/2
        def _sng(self,material,wt):
                self.wt = wt
                self.m = material
                self.parties = []
        def getwaitstaff(self):
                return self.wt.getname()
        def seatguests(self,pname):
                so_far = self.getseated()       # already at table
                adding = pname.getsize()        # wanting to join
                holds = self.getbums()          # capacity of table

                if holds >= so_far + adding:
                        self.parties.append(pname)
                        return True

                return None

        def getseated(self):
                so_far = 0
                for pty in self.parties:
                        so_far += pty.getsize()
                return so_far

        def findplace(tablist,client):
                for t in tablist:
                        if t.seatguests(client):
                                placed = 1
                                break
                else:
                        placed = None
                return placed
        findplace = staticmethod(findplace)     # Now an oldfashioned way, still works

        @staticmethod                   # self is the new way - a.k.a. "decorator"
        def myFactory(sourcestring):
                els = sourcestring.split(" ")
                print els
                if els[0] == "Re":
                        server = waitress(els[3],10)
                        # Should really have called method to search for self waitress
                        # and then re-used her!
                        return recttable(els[4],int(els[1]),int(els[2]),server)
                elif els[0] == "Ro":
                        # code to be written
                        pass
                elif els[0] == "Sq":
                        # code to be written
                        pass
                else:
                        print "oops"
                        return None

        def __str__(self):
                whattype = self.__class__.__name__
                # Above would be better as call to "gettype" on object to return English text
                rz = "A " + whattype + " made of " + self.m + "."
                return rz

        def getmore(self,that):
                s1 = self.getbums()
                s2 = that.getbums()
                if s1 > s2: return self
                return that

        @staticmethod
        def getmost(these):
                sofar = these[0]
                for maybe in these[1:]:
                        sofar = sofar.getmore(maybe)
                return sofar

class recttable(table):
        pass

class squaretable(table):
        def __init__(self,material,w,wt):
                self._sng(material,wt)
                self.w = w
                self.h = w
                self.place = 925

class roundtable(table):
        def __init__(self,material,w,wt):
                self._sng(material,wt)
                self.w = w
                self.h = w
                self.place = 800
        def getbums(self):
                side = int(self.w * 3.14159265 / self.place)
                return side

# ----------------------------------------------

if __name__ == "__main__":

        lead = waitress("Heather",12)
        assist = waitress("Poppy",10)

        cafe = [recttable("Cherry",2100,980,lead),
                recttable("Plastic",1800,750,assist),
                roundtable("Ash",1500,lead),
                squaretable("oak",5000,assist) ]

# line of data that needs converting to object:
        fromfile = "Re 1500 2100 Rachel Teak 2005"
        cafe.append(table.myFactory(fromfile))

        for tab in cafe:
                ps1 = tab.getbums()
                dog = tab.getdoggie()
                order = tab.getwaitstaff()
                print "We can seat",ps1,"and doggie distance is",dog,"order from",order

        if not table.findplace(cafe,customer("Alex",4)): print "nowhere for Alex"
        if not table.findplace(cafe,customer("Simon",3)): print "nowhere for Simon"
        if not table.findplace(cafe,customer("Bob",2)): print "nowhere for Bob"
        if not table.findplace(cafe,customer("Santa",122)): print "nowhere for Santa"
        if not table.findplace(cafe,customer("Sally",3)): print "nowhere for Sal"

        for tab in cafe:
                ps1 = tab.getbums()
                ps2 = tab.getseated()
                order = tab.getwaitstaff()
                print tab,"We have",ps2,"at a table for",ps1,"looked after by",order

# comparator

        moreseats = cafe[2].getmore(cafe[4])
        print "More seats on",moreseats

        mostseats = table.getmost(cafe)
        print "Most seats on",mostseats