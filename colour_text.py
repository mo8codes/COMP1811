from colorama import Fore, Style

# Example of colorful output
print(Fore.RED + "This text is red.")
print(Fore.GREEN + "This text is green.")
print(Fore.BLUE + "This text is blue.")

# Reset styles back to normal
print(Style.RESET_ALL + "Back to normal text.")

# Combine styles
print(Fore.YELLOW + Style.BRIGHT + "Bright yellow text!")
