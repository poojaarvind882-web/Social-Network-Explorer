# -------- MINI SOCIAL NETWORK SYSTEM --------

from collections import defaultdict, deque


# -------- DATABASE --------
people = {}                     # user details store karega
connections = defaultdict(set)  # friend connections store karega


# -------- NEW USER CREATE --------
def create_user(username, hobbies):
    people[username] = {
        "hobbies": hobbies
    }


# -------- CONNECT TWO USERS --------
def connect_users(user1, user2):
    connections[user1].add(user2)
    connections[user2].add(user1)


# -------- REMOVE CONNECTION --------
def disconnect_users(user1, user2):
    connections[user1].discard(user2)
    connections[user2].discard(user1)


# -------- USER DETAILS --------
def display_user(username):
    print(f"\n===== {username} PROFILE =====")
    print("Hobbies :", ", ".join(people[username]["hobbies"]))

    if connections[username]:
        print("Connections :", ", ".join(connections[username]))
    else:
        print("Connections : No Friends")


# -------- SHORTEST CONNECTION PATH --------
def shortest_connection(source, target):

    q = deque([source])
    visited = {source}
    previous = {}

    while q:
        current = q.popleft()

        if current == target:
            break

        for friend in connections[current]:
            if friend not in visited:
                visited.add(friend)
                previous[friend] = current
                q.append(friend)

    # path build karna
    route = []
    node = target

    while node != source:
        route.append(node)
        node = previous[node]

    route.append(source)
    route.reverse()

    print("\nFastest Connection Path:")
    print(" => ".join(route))


# -------- DEPTH SEARCH --------
def depth_search(node, limit, visited=None):

    if visited is None:
        visited = set()

    if limit < 0:
        return

    visited.add(node)
    print(node, end=" ")

    for friend in connections[node]:
        if friend not in visited:
            depth_search(friend, limit - 1, visited)


# -------- MATCHING HOBBIES --------
def hobby_match(u1, u2):

    h1 = set(people[u1]["hobbies"])
    h2 = set(people[u2]["hobbies"])

    return len(h1.intersection(h2))


# -------- FRIEND SUGGESTION --------
def suggest_friends(username):

    suggestion_list = []

    for person in people:

        # खुद को skip karo
        if person == username:
            continue

        # already friend hai to skip karo
        if person in connections[username]:
            continue

        score = hobby_match(username, person)
        suggestion_list.append((person, score))

    # highest score first
    suggestion_list.sort(key=lambda x: x[1], reverse=True)

    print(f"\nSuggested Friends for {username}:")
    for person, score in suggestion_list:
        print(f"{person} --> Common Interests: {score}")


# -------- MAIN PROGRAM --------
def run_system():

    # users add
    create_user("Rahul", ["Coding", "Music"])
    create_user("Priya", ["Sports", "Coding"])
    create_user("Aman", ["Travel", "Music"])
    create_user("Sneha", ["Sports", "Travel"])
    create_user("Karan", ["AI", "Coding"])

    # connections add
    connect_users("Rahul", "Priya")
    connect_users("Rahul", "Aman")
    connect_users("Priya", "Sneha")
    connect_users("Aman", "Karan")

    # profiles
    display_user("Rahul")
    display_user("Priya")

    # shortest path
    shortest_connection("Rahul", "Sneha")

    # dfs
    print("\nDepth Limited Traversal:")
    depth_search("Rahul", 2)

    # recommendations
    suggest_friends("Rahul")

    # remove friendship
    disconnect_users("Rahul", "Priya")

    print("\n\nAfter Removing Rahul-Priya Connection:")
    display_user("Rahul")


# -------- START --------
if __name__ == "__main__":
    run_system()