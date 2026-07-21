from story_generator import StoryGenerator

generator = StoryGenerator()

while True:

    print("\n===== RANDOM STORY GENERATOR =====")
    print("1. Generate Story")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(generator.generate_story())

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")