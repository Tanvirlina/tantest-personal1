# List of popular web browsers
browsers = [
    "Google Chrome",
    "Apple Safari",
    "Microsoft Edge",
    "Mozilla Firefox",
    "Samsung Internet"
]

print("Top 5 Web Browsers")
print("------------------------")

for number, browser in enumerate(browsers, start=1):
    print(f"{number}. {browser}")