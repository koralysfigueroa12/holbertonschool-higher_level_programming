
#!/usr/bin/python3
"""Print all names defined by the module `hidden_4` that do not
start with double underscores.

This follows the Holberton School "hidden discovery" exercise behavior:
import the module and print every attribute name that is not a dunder.
"""

if __name__ == "__main__":
	try:
		import hidden_4
	except Exception:
		# If the module is not available, do nothing (keeps behavior quiet)
		# You can raise or print an error if you prefer.
		raise

	for name in dir(hidden_4):
		if not name.startswith("__"):
			print(name)

