from dao.ipolicy_service import IPolicyService
from util.db_connection import DBConnection
from entity.policy import Policy
from exception.policy_not_found_exception import PolicyNotFoundException

class InsuranceServiceImpl(IPolicyService):
    def create_policy(self, policy):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO policy (policy_id, policy_name, policy_type, policy_amount) VALUES (?, ?, ?, ?)"
            cursor.execute(query, policy.get_policy_id(), policy.get_policy_name(), policy.get_policy_type(), policy.get_policy_amount())
            conn.commit()
            return True
        except Exception as e:
            print("Error creating policy:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def get_policy(self, policy_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM policy WHERE policy_id = ?"
            cursor.execute(query, policy_id)
            row = cursor.fetchone()
            if row:
                return Policy(row[0], row[1], row[2], row[3])
            else:
                raise PolicyNotFoundException(f"Policy with ID {policy_id} not found.")
        except PolicyNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error fetching policy:", e)
        finally:
            cursor.close()
            conn.close()

    def get_all_policies(self):
        policies = []
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM policy"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                policies.append(Policy(row[0], row[1], row[2], row[3]))
            return policies
        except Exception as e:
            print("Error fetching policies:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def update_policy(self, policy):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            updates = []
            values = []
            if policy.get_policy_name() is not None and policy.get_policy_name() != '':
                updates.append("policy_name = ?")
                values.append(policy.get_policy_name())
                
            if policy.get_policy_type() is not None and policy.get_policy_type() != '':
                updates.append("policy_type = ?")
                values.append(policy.get_policy_type())
                
            if policy.get_policy_amount() is not None:
                try:
                    policy_amount = float(policy.get_policy_amount())
                    updates.append("policy_amount = ?")
                    values.append(policy_amount)
                except ValueError:
                    print("Error: Invalid Policy Amount.")
                    return False

            if not updates:
                print("No fields to update.")
                return False
            
            query = f"UPDATE policy SET {', '.join(updates)} WHERE policy_id = ?"
            values.append(policy.get_policy_id())
            
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                raise PolicyNotFoundException(f"Policy with ID {policy.get_policy_id()} not found.")
        
            print(f"Policy with ID {policy.get_policy_id()} updated successfully.")
            return True

        except PolicyNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error updating policy:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def delete_policy(self, policy_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM client WHERE policy_id = ?", (policy_id,))
            count = cursor.fetchone()[0]
            if count > 0:
                print(f"Cannot delete policy {policy_id}. It is currently assigned to {count} client(s).")
                confirm = input("Do you still want to delete the policy and its associated clients? (yes/no): ").strip().lower()
                if confirm != 'yes':
                    print("Deletion cancelled.")
                    return False
                
                cursor.execute("DELETE FROM claim WHERE client_id IN (SELECT client_id FROM client WHERE policy_id = ?)", (policy_id,))
                print(f"Claims associated with policy {policy_id} deleted.")

                cursor.execute("DELETE FROM payment WHERE client_id IN (SELECT client_id FROM client WHERE policy_id = ?)", (policy_id,))
                

                cursor.execute("DELETE FROM client WHERE policy_id = ?", (policy_id,))
                print(f"{count} client(s) associated with policy {policy_id} deleted.")

                
            cursor.execute("DELETE FROM policy WHERE policy_id = ?", (policy_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise PolicyNotFoundException(policy_id)

            print(f"Policy {policy_id} deleted successfully.")
            return True

        except Exception as e:
            print("Error deleting policy:", e)
            return False
        finally:
            cursor.close()
            conn.close()



    def get_clients_by_policy(self, policy_id):
        clients = []
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = """ SELECT c.client_id, c.client_name, c.contact_info FROM client c 
            JOIN policy p ON c.policy_id = p.policy_id
            WHERE p.policy_id = ?
        """
            cursor.execute(query, (policy_id,))
            rows = cursor.fetchall()
            for row in rows:
                clients.append({"client_id": row[0],"client_name": row[1],"contact_info": row[2]})
                return clients
        except Exception as e:
            print("Error retrieving clients by policy:", e)
            return []
        
        finally:
            cursor.close()
            conn.close()

    def get_client_insurance_summary(self, client_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """ SELECT c.client_id,c.client_name,c.contact_info,p.policy_name,p.policy_type,cl.claim_number,cl.date_filed,cl.claim_amount,
                cl.status AS claim_status,pay.payment_date,pay.payment_amount
                 FROM 
                client c
            JOIN policy p ON c.policy_id = p.policy_id
            LEFT JOIN claim cl ON c.client_id = cl.client_id
            LEFT JOIN payment pay ON c.client_id = pay.client_id
            WHERE c.client_id = ?
        """

            cursor.execute(query, (client_id,))
            rows = cursor.fetchall()

            if not rows:
                print(f"No data found for client ID {client_id}")
                return False
            print("\n====== Client Insurance Summary ======")
            for row in rows:
                print(f"Client ID       : {row[0]}")
                print(f"Client Name     : {row[1]}")
                print(f"Contact Info    : {row[2]}")
                print(f"Policy Name     : {row[3]}")
                print(f"Policy Type     : {row[4]}")
                print(f"Claim Number    : {row[5]}")
                print(f"Claim Date      : {row[6]}")
                print(f"Claim Amount    : {row[7]}")
                print(f"Claim Status    : {row[8]}")
                print(f"Payment Date    : {row[9]}")
                print(f"Payment Amount  : {row[10]}")
                print("--------------------------------------")
                return True

        except Exception as e:
            print("Error fetching client insurance summary:", e)
            return False
        finally:
            cursor.close()
            conn.close()

