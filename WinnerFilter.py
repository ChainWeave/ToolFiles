import tkinter as tk


def search_address():
    search_text = address_entry.get("1.0", "end-1c")
    search_lines = search_text.split("\n")
    search_lines = [line.strip() for line in search_lines if line.strip()]

    winner_text = winners_entry.get("1.0", "end-1c")
    winner_lines = winner_text.split("\n")
    winner_lines = [line.strip() for line in winner_lines if line.strip()]

    found_addresses = [line for line in search_lines if line in winner_lines]
    if found_addresses:
        output_text.delete(1.0, "end")
        output_text.insert("end", "\n".join(found_addresses))
    else:
        output_text.delete(1.0, "end")
        output_text.insert("end", "No Address is Winner!")


root = tk.Tk()
root.title("Winner Filter - Autor Twitter：@chainweave")
root.geometry('650x380')
root.resizable(False, False)

winners_label = tk.Label(root, text="Winner：")
winners_label.pack(pady=5, padx=40, anchor='w')
winners_entry = tk.Text(root, width=80, height=5)
winners_entry.pack(pady=1)

address_label = tk.Label(root, text="Your Address：")
address_label.pack(pady=5, padx=40, anchor='w')
address_entry = tk.Text(root, width=80, height=5)
address_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_address, width=30, height=1)
search_button.pack(pady=10)

output_label = tk.Label(root, text="Winner Address：")
output_label.pack(pady=1, padx=40, anchor='w')
output_text = tk.Text(root, width=80, height=5)
output_text.insert("1.0", "Show Winner Address Here")
output_text.pack(pady=1)
output_text.tag_configure("custom_color", foreground="gray")
output_text.tag_add("custom_color", "1.0", "end")

root.mainloop()
