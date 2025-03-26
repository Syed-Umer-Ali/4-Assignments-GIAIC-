import tkinter as tk

class EraseCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Canvas")

        # Canvas dimensions
        self.canvas_width = 500
        self.canvas_height = 500
        self.cell_size = 20

        # Create canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = []
        for y in range(0, self.canvas_height, self.cell_size):
            row = []
            for x in range(0, self.canvas_width, self.cell_size):
                rect = self.canvas.create_rectangle(
                    x, y, x + self.cell_size, y + self.cell_size,
                    fill="Cyan", outline="black"
                )
                row.append(rect)
            self.cells.append(row)

        # Create eraser rectangle
        self.eraser_size = 40
        self.eraser = self.canvas.create_rectangle(
            0, 0, self.eraser_size, self.eraser_size,
            fill="red", outline="black"
        )

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        # Move eraser to mouse position
        x1, y1 = event.x - self.eraser_size // 2, event.y - self.eraser_size // 2
        x2, y2 = event.x + self.eraser_size // 2, event.y + self.eraser_size // 2
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase cells that intersect with the eraser
        for row in self.cells:
            for cell in row:
                if self.rectangles_intersect(self.canvas.coords(cell), [x1, y1, x2, y2]):
                    self.canvas.itemconfig(cell, fill="red")

    @staticmethod
    def rectangles_intersect(rect1, rect2):
        # Check if two rectangles intersect
        return not (
            rect1[2] <= rect2[0] or  # rect1 is to the left of rect2
            rect1[0] >= rect2[2] or  # rect1 is to the right of rect2
            rect1[3] <= rect2[1] or  # rect1 is above rect2
            rect1[1] >= rect2[3]     # rect1 is below rect2
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = EraseCanvasApp(root)
    # Create a side panel
    side_panel = tk.Frame(root, width=200, bg="yellow")
    side_panel.pack(side=tk.RIGHT, fill=tk.Y)

    # Add a label to the side panel
    status_label = tk.Label(side_panel, text="Status: Drawing", bg="yellow", font=("Arial", 12))
    status_label.pack(pady=20)

    def check_completion():
        # Check if all cells are erased
        all_erased = all(
            app.canvas.itemcget(cell, "fill") == "orange"
            for row in app.cells for cell in row
        )
        if all_erased:
            status_label.config(text="Status: Complete!")
        else:
            root.after(100, check_completion)

    # Start checking for completion
    check_completion()

    root.mainloop()