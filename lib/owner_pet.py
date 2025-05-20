# lib/pet_owner.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return list of pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check pet is instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("add_pet argument must be a Pet instance")
        # Set this owner to the pet
        pet.owner = self


    def get_sorted_pets(self):
        # Return list of pets sorted by their name
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type

        # Validate owner if given
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance or None")

        self.owner = owner
        Pet.all.append(self)
