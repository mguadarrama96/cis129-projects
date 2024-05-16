class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.set_age(age)  # Validate age during initialization

    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        while True:
            try:
                self.__age = int(age)
                break  # Exit the loop if input is a valid integer
            except ValueError:
                print("Invalid input. Age must be an integer. Please try again.")
                age = input("Enter the pet's age: ")

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    # Create a Pet object
    pet_name = input("Enter the pet's name: ")
    pet_type = input("Enter the type of pet (e.g., Dog, Cat, Bird): ")

    while True:
        pet_age = input("Enter the pet's age: ")
        try:
            pet_age = int(pet_age)  # Check if the input is a valid integer
            break
        except ValueError:
            print("Invalid input. Age must be an integer. Please try again.")

    my_pet = Pet(pet_name, pet_type, pet_age)

    # Display the pet's information
    print("\nPet Information:")
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_type()}")
    print(f"Age: {my_pet.get_age()} years")

if __name__ == "__main__":
    main()