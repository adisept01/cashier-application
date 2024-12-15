import datetime

class User:
    #Class to manage user login
    def __init__(self):
        # Predefined users with passwords
        self.users = {"adi": "adimin123", "cashier": "cash123"}

    def login(self):
        print("= Login Sistem =")
        for _ in range(3):  # 3 login attempts
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if username in self.users and self.users[username] == password:
                print(f"Selamat datang, {username}.\n")
                return True
            else:
                print("Username atau password salah. Coba lagi.\n")
        print("Login gagal. Sistem keluar.")
        return False


class Cashier:
    #Class to handle cashier operations
    def __init__(self):
        self.customer_name = None
        self.items = []

    def input_customer_name(self):
        self.customer_name = input("Nama pelanggan: ")

    def add_items(self):
        print("\n- Detail Pesanan -")
        while True:
            item_name = input("Masukkan nama item (atau 'selesai' untuk berhenti): ")
            if item_name.lower() == 'selesai':
                break
            try:
                quantity = int(input(f"Masukkan jumlah untuk {item_name}: "))
                price = float(input(f"Masukkan harga per unit untuk {item_name}: "))
                self.items.append({"name": item_name, "quantity": quantity, "price": price})
            except ValueError:
                print("Input tidak valid, coba lagi.")

    def calculate_total(self):
        return sum(item['quantity'] * item['price'] for item in self.items)

    def apply_discount(self, total, discount_rate):
        #Calculate discount based on percentage
        return total * (discount_rate / 100)

    def apply_tax(self, total, tax_rate):
        #Calculate tax based on percentage
        return total * (tax_rate / 100)

    def display_receipt(self, total, discount, tax, grand_total):
        #Print receipt to console
        print("\n= STRUK PEMBELIAN =")
        print(f"Nama Pelanggan: {self.customer_name}")
        print(f"Tanggal/Waktu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n- Rincian Pesanan -")
        for item in self.items:
            print(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")
        print(f"\nTotal: Rp {total:.2f}")
        print(f"Diskon: Rp {discount:.2f}")
        print(f"Pajak: Rp {tax:.2f}")
        print(f"Total Akhir: Rp {grand_total:.2f}")
        print("\nTerima kasih telah berbelanja!")

    def save_receipt(self, total, discount, tax, grand_total):
        """Save receipt to a file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = f"receipt_{self.customer_name.replace(' ', '_')}_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(f"=== STRUK PEMBELIAN ===\n")
            file.write(f"Nama Pelanggan: {self.customer_name}\n")
            file.write(f"Tanggal/Waktu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("\n--- Rincian Pesanan ---\n")
            for item in self.items:
                file.write(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}\n")
            file.write(f"\nTotal: Rp {total:.2f}\n")
            file.write(f"Diskon: Rp {discount:.2f}\n")
            file.write(f"Pajak: Rp {tax:.2f}\n")
            file.write(f"Total Akhir: Rp {grand_total:.2f}\n")
            file.write("\nTerima kasih telah berbelanja!\n")
        print(f"\nStruk berhasil disimpan ke file: {filename}")


def main():
    # Create User and Cashier objects
    user = User()
    cashier = Cashier()

    # Login process
    if not user.login():
        return  # Exit program if login fails

    # Start cashier process
    cashier.input_customer_name()
    cashier.add_items()

    # Calculate totals
    total = cashier.calculate_total()
    print(f"\nTotal sebelum diskon dan pajak: Rp {total:.2f}")

    discount_rate = float(input("Masukkan persentase diskon: "))
    discount = cashier.apply_discount(total, discount_rate)
    print(f"Diskon ({discount_rate}%): Rp {discount:.2f}")

    tax_rate = float(input("Masukkan persentase pajak: "))
    tax = cashier.apply_tax(total - discount, tax_rate)
    print(f"Pajak ({tax_rate}%): Rp {tax:.2f}")

    grand_total = total - discount + tax
    print(f"Total yang harus dibayar setelah diskon dan pajak: Rp {grand_total:.2f}")

    # Display receipt
    cashier.display_receipt(total, discount, tax, grand_total)

    # Save receipt to file
    cashier.save_receipt(total, discount, tax, grand_total)


if __name__ == "__main__":
    main()
