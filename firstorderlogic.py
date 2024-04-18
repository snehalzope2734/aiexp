# this is chatgpt code i am not sure about this

pip install pyDatalog
from pyDatalog import pyDatalog

def create_rules():
    # Define the rules here based on user input
    rule_input = input("Enter logical rule (e.g., ancestor(X, Y) <= parent(X, Y) & ancestor(Y, Z)): ")
    pyDatalog.load(rule_input)

def query():
    # Perform queries based on user input
    query_input = input("Enter query (e.g., ancestor('John', Y)): ")
    result = pyDatalog.ask(query_input)
    print(result)

if __name__ == "__main__":
    while True:
        choice = input("Enter 1 to add rule, 2 to query, or any other key to exit: ")
        if choice == '1':
            create_rules()
        elif choice == '2':
            query()
        else:
            break
