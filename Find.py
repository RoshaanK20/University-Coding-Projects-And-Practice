# Creating List for multiple users info
users = []

# Function to define user input
def user_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print(f"{prompt} is mandatory.")

# Collect information for 20 users
for i in range(20):
    print(f"\nEnter details for user {i + 1}:")
    name = user_input("Enter name: ")
    contact = user_input("Enter contact number: ")
    age = user_input("Enter Age: ")
    users.append({'name': name, 'contact': contact, 'age': age})

# Collect professions for the 20 users
for user in users:
    user['specialization'] = user_input(f"Enter Specialization for {user['name']}")

# Function to search user by name or contact number
def search_user(query):
    for user in users:
        if user['name'].lower() == query.lower() or user['contact'] == query:
            return user['specialization']
    return "User not found."

while True:
    search = input("\nEnter name or contact number to search for a user's specialization (or type 'exit' to quit): ")
    if search.lower() == 'exit':
        break
    print(f"Profession: {search_user(search)}")
