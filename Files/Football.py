def main():
    # Prompt the user for their name and the team they support
    name = input("Enter your name: ")
    team = input("Enter the team you support: ")

    # Write the user's name and team to the football.csv file
    with open("football.csv", "a") as file:
        file.write(f"{name},{team}\n")

if __name__ == "__main__":
    main()
def main():
    # Open the football.csv file for reading
    with open("football.csv", "r") as file:
        # Read each line in the file
        for line in file:
            # Remove newline character and split the line into name and team
            name, team = line.strip().split(",")
            # Print the name and team
            print(f"{name} supports {team}")

if __name__ == "__main__":
    main()
