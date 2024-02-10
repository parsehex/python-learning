# This is a simple but complete example of a DataFrame table using tkinter
# The dataframe stays in sync with the table thru user changes (it's "reactive" as they call it in webdev)
# This code has largely been written by GitHub Copilot, starting with the prompt:
#   I am attempting to create a table in tkinter using a dataframe. First we'll need a test df to show, then I want to be able to view it as a table with basic spreadsheet features to modify cells, the changes will persist back to the actual df and stay in sync with the ui. This is a test file for now but we'll grow it, so keep that in mind as you work. We're not using a pre-made solution here.
# Ask to fix issues as they arrise. Otherwise I selected all of the code and chatted the above prompt again with an extra line:
#   Please update this file to make progress toward my goal.
#
# Ideas to go from here:
# - Explore what a generic DataFrameTreeview class would look like

import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd
import numpy as np

class DataFrameTreeview(ttk.Treeview):
	def __init__(self, parent, df, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.df = df
		self["columns"] = tuple(df.columns)
		self["show"] = 'headings'
		self.item_ids = []
		self.column_names = list(df.columns)
		for column in df.columns:
			self.column(column, width=100)
			self.heading(column, text=column)
		self.insert_data_rows()
		self.bind('<Double-1>', self.on_double_click)
		# Create an Entry widget for inline editing
		self.entry = tk.Entry(self, width=0)
		self.entry.bind('<Return>', self.finish_editing)
		self.entry.bind('<FocusOut>', self.finish_editing)

	def on_double_click(self, event):
		item = self.identify('item', event.x, event.y)
		column = self.identify('column', event.x, event.y)
		value = self.set(item, column)
		# Show the Entry widget at the cell position
		x, y, width, height = self.bbox(item, column)
		self.entry.place(x=x, y=y, width=width, height=height)
		self.entry.delete(0, tk.END)
		self.entry.insert(0, value)  # type: ignore
		self.entry.focus_set()
		# Store the item and column for later use
		self.current_item = item
		self.current_column = column

	def finish_editing(self, event):
		new_value = self.entry.get()
		if new_value:
			column_name = self.column_names[
				int(self.current_column[1:]) - 1]
			dtype = self.df.dtypes[column_name].type
			if dtype == np.int64:
				new_value = int(new_value)
			elif dtype == np.float64:
				new_value = float(new_value)
			self.set(self.current_item, self.current_column, new_value)
			index = self.item_ids.index(self.current_item)
			self.df.loc[index, column_name] = new_value
		# Hide the Entry widget
		self.entry.place_forget()

	def insert_data_rows(self):
		for i, row in self.df.iterrows():
			item_id = self.insert("", tk.END, values=tuple(row))
			self.item_ids.append(item_id)

	def add_row(self):
		new_row = {}
		for column in self.df.columns:
			value = simpledialog.askstring(
				"Add Row", f"Enter value for {column}"
			)
			new_row[column] = value
		self.df = self.df.append(new_row, ignore_index=True)
		item_id = self.insert(
			"", tk.END, values=tuple(new_row.values())
		)
		self.item_ids.append(item_id)

	def debug(self):
		# Use this method for whatever's needed to debug at the time
		# right now just print dataframe
		print(self.df)

if __name__ == "__main__":
	data = {
		'Name': ['John', 'Emma', 'Peter', 'Olivia'],
		'Age': [25, 28, 32, 30],
		'City': ['New York', 'London', 'Paris', 'Tokyo']
	}
	df = pd.DataFrame(data)

	window = tk.Tk()
	window.title("DataFrame Table Example")

	tree = DataFrameTreeview(window, df)
	tree.pack()

	# frame for the buttons
	button_frame = ttk.Frame(window)
	button_frame.pack()

	add_button = tk.Button(
		button_frame, text="Add Row", command=tree.add_row
	)
	add_button.pack(side='left')

	dump_button = tk.Button(
		button_frame, text="Debug", command=tree.debug
	)
	dump_button.pack(side='left')

	window.mainloop()
