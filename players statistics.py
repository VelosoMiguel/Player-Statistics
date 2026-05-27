import tkinter as tk

def add_stats():
    name = entry_name.get()
    points = entry_points.get()
    passes = entry_passes.get()
    errors = entry_errors.get()
    blocks = entry_blocks.get()

    if name: 
        stats = f"{name} - Points: {points}, Passes: {passes}, Errors: {errors}, Blocks: {blocks}\n"
        text_area.insert(tk.END, stats)

        entry_name.delete(0, tk.END)
        entry_points.delete(0, tk.END)
        entry_passes.delete(0, tk.END)
        entry_errors.delete(0, tk.END)
        entry_blocks.delete(0, tk.END)

window = tk.Tk()
window.title("Player Statistics")

tk.Label(window, text="Player Name:").grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Points:").grid(row=1, column=0)
entry_points = tk.Entry(window)
entry_points.grid(row=1, column=1)

tk.Label(window, text="Passes:").grid(row=2, column=0)
entry_passes = tk.Entry(window)
entry_passes.grid(row=2, column=1)

tk.Label(window, text="Errors:").grid(row=3, column=0)
entry_errors = tk.Entry(window)
entry_errors.grid(row=3, column=1)

tk.Label(window, text="Blocks:").grid(row=4, column=0)
entry_blocks = tk.Entry(window)
entry_blocks.grid(row=4, column=1)

add_button = tk.Button(window, text="Add Statistics", command=add_stats)
add_button.grid(row=5, columnspan=2, pady=10)

text_area = tk.Text(window, height=10, width=50)
text_area.grid(row=6, columnspan=2)

window.mainloop()
