
class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Error: Add a team lead first.")
            return

        side = side.lower()

        if side not in ("left", "right"):
            print("Error: Choose left or right.")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print("Error: The left side is already occupied.")
                    return
                current_node.left = EmployeeNode(employee_name)
            else:
                if current_node.right is not None:
                    print("Error: The right side is already occupied.")
                    return
                current_node.right = EmployeeNode(employee_name)

            print(
                f"Success: {employee_name} added to the "
                f"{side.upper()} of {manager_name}."
            )
            return

        # Search the left subtree.
        if current_node.left is not None:
            self.insert(
                manager_name, employee_name, side, current_node.left
            )
            if self._contains(current_node.left, manager_name):
                return

        # Search the right subtree.
        if current_node.right is not None:
            self.insert(
                manager_name, employee_name, side, current_node.right
            )
            if self._contains(current_node.right, manager_name):
                return

        if current_node == self.root:
            print(f"Error: Manager '{manager_name}' was not found.")

    def _contains(self, node, name):
        if node is None:
            return False
        if node.name == name:
            return True
        return (
            self._contains(node.left, name)
            or self._contains(node.right, name)
        )

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The team is empty.")
            return

        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input(
                "Should this employee be on the LEFT or RIGHT of the manager? "
            )
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()
