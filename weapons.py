import random

# default spear class
class spear:

    type_ = "unknown"

    # stats
    stats = {
        "strength" : 1,
        "min_attack" : 1,
        "max_attack" : 1
    }

    # print stats
    def show_stats(self):
        print("")
        print("Spear Stats")
        print ("-------------------------")
        print("Type: " + self.type_)
        print("")
        for key in self.stats:
            print(key + " : " + str(self.stats[key]))
        print ("-------------------------")
        print("")

# basic spear class
#-------------------------------------------------------------------
class basic_spear(spear):
    type_ = "Basic Spear"
    stats = {
        "strength" : 3,
        "min_attack" : 1,
        "max_attack" : 2
        }
#-------------------------------------------------------------------

# Guard spear class
#-------------------------------------------------------------------
class guard_spear(spear):
    type_ = "Guard Spear"
    stats = {
        "strength" : 4,
        "min_attack" : 2,
        "max_attack" : 3
        }
#-------------------------------------------------------------------

# master spear class
#-------------------------------------------------------------------
class master_spear(spear):
    type_ = "Master Spear"
    stats = {
        "strength" : 5,
        "min_attack" : 3,
        "max_attack" : 4
        }
#-------------------------------------------------------------------

# return a list of spear types
#-------------------------------------------------------------------
def generate_spears():
    spear_list = [basic_spear, guard_spear, master_spear]
    return spear_list
#-------------------------------------------------------------------

# get a random spear
#-------------------------------------------------------------------
def craft_random_spear():
    spears = generate_spears()
    random_spear = random.choice(spears)
    print("You crafted a " + random_spear.type_)
    random_spear.show_stats(random_spear)
    return random_spear
#-------------------------------------------------------------------

# craft a spear of the requested type
#-------------------------------------------------------------------
def craft_spear(requested_spear):

    # all available spears
    spears = generate_spears()
    type_list = []
    # get list of spear types
    for spear in spears: 
        type_list.append(spear.type_)

    if(requested_spear in type_list):
        # return the requested spear
        selected_spear = spears[type_list.index(requested_spear)]()
    else:   
        # default spear is basic spear
        print("")
        print(requested_spear + " is not recognised, so you get a Basic Spear!")
        selected_spear = basic_spear()

    return selected_spear
#-------------------------------------------------------------------