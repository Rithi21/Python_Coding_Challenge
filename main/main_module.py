from entity.policy import Policy
from dao.insurance_service_impl import InsuranceServiceImpl
from exception.policy_not_found_exception import PolicyNotFoundException

def main():
    service = InsuranceServiceImpl()

    while True:
        print("\nWelcome to Insurance Management System ")
        print("1. Create Policy")
        print("2. View Policy by ID")
        print("3. View All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. View Clients who Accessed a Policy")
        print("7. View Client's Insurance Summary")
        print("8. Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            try:
                policy_id = int(input("Enter Policy ID: "))
                policy_name = input("Enter Policy Name: ")
                policy_type = input("Enter Policy Type: ")
                policy_amount = float(input("Enter Policy Amount: "))

                policy = Policy(policy_id, policy_name, policy_type, policy_amount)
                success = service.create_policy(policy)
                if success:
                    print("Policy created successfully.")
                else:
                    print("Failed to create policy.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                policy_id = int(input("Enter Policy ID to view: "))
                policy = service.get_policy(policy_id)
                print(f"\nPolicy Details:\nID: {policy.get_policy_id()}, Name: {policy.get_policy_name()}, Type: {policy.get_policy_type()}, Amount: {policy.get_policy_amount()}")
            except PolicyNotFoundException as e:
                print(e)
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                policies = service.get_all_policies()
                if not policies:
                    print("No policies found.")
                else:
                    for p in policies:
                        print(f"ID: {p.get_policy_id()}, Name: {p.get_policy_name()}, Type: {p.get_policy_type()}, Amount: {p.get_policy_amount()}")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                policy_id = int(input("Enter Policy ID to update: "))
                policy_name = input("Enter new Policy Name : ")
                policy_type = input("Enter new Policy Type : ")
                policy_amount_str = input("Enter new Policy Amount : ")

                if policy_amount_str.strip() == '':
                    policy_amount = None  
                else:
                    try:
                        policy_amount = float(policy_amount_str)
                    except ValueError:
                        print("Error: Invalid Policy Amount. Please enter a valid number.")
                        return  

  
                policy = Policy(policy_id, policy_name if policy_name else None, policy_type if policy_type else None, policy_amount)
                success = service.update_policy(policy)
                if success:
                    print("Policy updated successfully.")
                else:
                    print("Policy update failed.")
            
            except PolicyNotFoundException as e:
                print(e)
            except ValueError as e:
                print("Invalid input. Please try again.", e)
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            try:
                policy_id = int(input("Enter Policy ID to delete: "))
                success = service.delete_policy(policy_id)
                if success:
                    print("Policy deleted successfully.")
            except PolicyNotFoundException as e:
                print(e)
            except Exception as e:
                print("Error:", e)

        elif choice == "6":
            try:
                policy_id = int(input("Enter Policy ID to find associated clients: "))
                clients = service.get_clients_by_policy(policy_id)
                if clients:
                    print(f"\nClients who accessed Policy ID {policy_id}:")
                    for client in clients:
                        print(f"ID: {client['client_id']}, Name: {client['client_name']}, Contact: {client['contact_info']}")
                else:
                    print("No clients found for this policy.")
            except Exception as e:
                print("Error:", e)
                
        elif choice == "7":
            try:
                client_id = int(input("Enter Client ID to view insurance summary: "))
                success = service.get_client_insurance_summary(client_id)
                if not success:
                    print(f"No insurance summary found for client ID {client_id}.")
            except Exception as e:
                print("Error:", e)

        elif choice == '8':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
