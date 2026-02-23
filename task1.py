def main():
    #Collect Input for each
    #Variable: first Prompt: Child's First Name:
    first = input("Child's First name: ")
    #Variable: last Prompt: Child's Last Name:
    last = input(f"Child's last name: ")
    print(f"Camper's Name: {first} {last}")

    #Variable: birth Prompt: In what year was {first} {last} born:
    birth = input(f"How many days will {first} attend? ")
    print(f"Birth Year: {birth}")

    #Variable: days Prompt: How many days will {first} attend?
    birth = input(f"How many days will {first} attend? ")
    print(f"Camp Duration: {days} days")

    #Variable: p_first Prompt: Parent's First Name:
    p_first = input(f"Parent's First Name: ")
    #Variable: p_last Prompt: Parent's Last Name:
    
    p_last = input("Parent's Last Name: ")
    print(f"Parent's Name: {p_first} {p_last}")

    #Variable: phone Prompt: Parent's Phone #:
    phone = input("Parent's Phone #: ")
    print(f"Phone Number: {phone}")

    #Variable: street Prompt: Street Address:
    street = input("Street Address: ")
    print(f"Street Address: {street}")
    #Variable: city Prompt: City:
    City = input("City: ")
    print(f"City: {city}")
    #Variable: state Prompt: State Abbreviation:
    state = input("State Abbreviation: ")
    print(f"State Abbreviation: {state}")
    #Variable: zip Prompt: Zip Code:
    print(f"Zip Code: {zip}")
    print(f"Address:\n{street}\n{city}, {state}, {zip}")

if __name__ == "__main__":
    main()
