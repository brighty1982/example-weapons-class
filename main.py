import weapons
import combat

# craft a random spear
print("Crafting a random spear...")
print("")
my_spear = weapons.craft_random_spear()
my_spear.show_stats()



# creaft a spear of a specific type
print("Crafting a Master Spear")
my_master_spear = weapons.craft_spear("Master Spear")
my_master_spear.show_stats()


# Pass the randomly created spear to attack function
combat.attack(my_spear)

# Pass the sepecifically created Master Spear to attack function
combat.attack(my_master_spear)



