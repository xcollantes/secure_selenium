from secure_selenium import SecureSelenium
import time

r = SecureSelenium(
    "", "", False, window_width=1600, window_length=1600)
r.get("https://tools.keycdn.com/geo")
input("Waiting on button...")
r.close()
