#This provides a witty retort for a simple question each time it is run
import random

print("What is your quest?")
quest = input()

outcomes = ["'Tisn't the grandest truth, 'tis?",
            "Well, what for, y'know?",
            "Might be right, if ya squint…",
            "Tell me again and see what happens, mate.",
            "Ain't got a clue this'n, buddy.",
            "Shut it 'n' ship it!",
            "Right you are, skippy!",
            "Prove it."]

print(quest + ', eh?')
print(outcomes[random.randint(0, len(outcomes) - 1)])