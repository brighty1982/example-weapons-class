import weapons

# craft a random spear
print("Crafting a random spear...")
print("")
my_spear = weapons.craft_random_spear()


# creaft a spear of a specific type
print("Crafting a Master Spear")
my_master_spear = weapons.craft_spear("Master Spear")
my_master_spear.show_stats()



