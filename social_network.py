class Person:
   
    def __init__(self, name):
        self.name = name
        self.friends = [] # List to store the person's friends

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend) # Add friend to the list


class SocialNetwork:
    # Dictionary to store all people in the network, keyed by their names
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name) # Add person to the network

    def add_friendship(self, person1_name, person2_name): # Add friendship between two people
        if person1_name not in self.people: # Check if person1 exists in the network
            print(f"Friendship not added: {person1_name} is not in the network.")
        elif person2_name not in self.people: # Check if person2 exists in the network
            print(f"Friendship not added: {person2_name} is not in the network.")
        else: # Add friendship between the two people if passed validation
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)

    def print_network(self): # Print the network of people and their friends
        for person in self.people.values():
            friends = ", ".join([friend.name for friend in person.friends]) # Get the names of the person's friends
            print(f"{person.name} is friends with: {friends}")



# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
print(network.people)  # {'Alex': <__main__.Person object at 0x1004c7380>,'Jordan': <__main__.Person object at 0x10503d810>}
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Edge case: Dupes
network.add_friendship("Alex", "Jordan") # Dupe friendship
network.add_person("Alex") # Dupe person
print(len(network.people)) # 6

network.print_network()