print("=== Welcome to Mad Libs ===")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
verb = input("Enter a verb ending with -ing: ")
adjective = input("Enter an adjective: ")

story = f"""
One day, {name} went to {place}.
Suddenly, a {adjective} {animal} appeared.
It started {verb} while eating {food}.
Everyone was surprised, but {name} started laughing.
It became the funniest day ever!
"""

print(story)