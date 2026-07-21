import random
from data import subjects, places, actions, endings


class StoryGenerator:

    def generate_story(self):

        subject = random.choice(subjects)
        place = random.choice(places)
        action = random.choice(actions)
        ending = random.choice(endings)

        story = f"""
{subject} went {place}.
There, they {action},
{ending}
"""

        return story