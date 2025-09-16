import mysql.connector
from colorama import init, Fore, Style
import time 

init()

class dadabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root123',
            database = 'db'
        )

        self.cursor = self.connection.cursor()
        print("Data base connect successfully")
    
    def add_product(self):
        new_name = input("Enter the new name : ")
        names_list = (new_name,)
        self.cursor.execute(f"INSERT INTO laptops (name) VALUE (%s)", names_list)
        self.connection.commit()
        print(f"{new_name} was added successfully")
    
    def update_product(self):
        id_product = input("Enter the article ID : ")
        new_price = input("Enter new price : ")
        self.cursor.execute(f"UPDATE laptops SET price = %s WHERE id = %s ", (new_price, id_product))
        self.connection.commit()
        print(f"The price with ID :{id_product} was updated to : {new_price}")
    
    def delete_product(self):
        id = input("Enter the ID that you want to delete its article : ")
        self.cursor.execute(f"DELETE FROM laptops WHERE id= {id}")
        self.connection.commit()
        print(f"Article with id : {id}, was deleted")
    
    def fetch_articles_by_name(self):
        self.cursor.execute("SELECT name FROM laptops ORDER BY name ASC") # Fetch names by order from A to Z
        names = self.cursor.fetchall()
        print("\nAll data in table :")
        for i, name in enumerate(names):
            print(f"Name {i} : {name[0]}")
    
    def fetch_article_by_price(self):
        self.cursor.execute("SELECT * FROM laptops WHERE price >= 30 ORDER BY price DESC") # Fetch prices >=30 by order from the biggest to the little
        prices = self.cursor.fetchall()
        print("\nPrices fetched from tha table : ")
        for price in prices:
            print(f"Article Id : {price[0]}, Price : {price[2]}")
        
    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

def main():
    print(Fore.CYAN + "\n🎮 Welcome to the Laptop Shop Manager Game! 🎮" + Style.RESET_ALL)
    print("Manage your laptop inventory like a pro! Choose an action to level up.")
    
    db = None
    try:
        db = dadabase()
        
        while True:
            print(Fore.YELLOW + "\n=== Main Menu ===" + Style.RESET_ALL)
            print("1. 📦 Add a new product")
            print("2. 💰 Update a product's price")
            print("3. 🗑️ Delete a product")
            print("4. 📋 List all products (by name)")
            print("5. 💸 List products with price >= 30")
            print("6. 🚪 Exit the game")
            choice = input(Fore.GREEN + "Enter your choice (1-6): " + Style.RESET_ALL)
            
            if choice == '1':
                print(Fore.MAGENTA + "\nLet's add a new laptop to the shop!" + Style.RESET_ALL)
                db.add_product()
                print(Fore.CYAN + "Nice! Back to the menu for more action!" + Style.RESET_ALL)
                time.sleep(1)
            
            elif choice == '2':
                print(Fore.MAGENTA + "\nTime to update a price!" + Style.RESET_ALL)
                db.update_product()
                print(Fore.CYAN + "Price updated! Ready for the next mission?" + Style.RESET_ALL)
                time.sleep(1)
            
            elif choice == '3':
                print(Fore.MAGENTA + "\nRemoving a product from the inventory!" + Style.RESET_ALL)
                db.delete_product()
                print(Fore.CYAN + "Product zapped! What's next, boss?" + Style.RESET_ALL)
                time.sleep(1)
            
            elif choice == '4':
                print(Fore.MAGENTA + "\nChecking out the product catalog!" + Style.RESET_ALL)
                db.fetch_articles_by_name()
                print(Fore.CYAN + "Catalog displayed! Ready for more?" + Style.RESET_ALL)
                time.sleep(1)
            
            elif choice == '5':
                print(Fore.MAGENTA + "\nFinding premium products (price >= 30)!" + Style.RESET_ALL)
                db.fetch_article_by_price()
                print(Fore.CYAN + "Premium list ready! What's your next move?" + Style.RESET_ALL)
                time.sleep(1)
            
            elif choice == '6':
                print(Fore.RED + "\nThanks for playing Laptop Shop Manager! Closing the shop..." + Style.RESET_ALL)
                db.close()
                break
            
            else:
                print(Fore.RED + "Invalid choice! Pick a number between 1 and 6." + Style.RESET_ALL)
                time.sleep(1)
    
    except Exception as e:
        print(Fore.RED + f"Game over! Error: {e}" + Style.RESET_ALL)
        if db:
            db.close()

if __name__ == "__main__":
    main()



