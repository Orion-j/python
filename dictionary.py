#  working with dictionary.
# details of a worker.

identification = {
    "name": "Joe Boadi",
    "age": 25,
    "job": "Snr. Software Engineer",
    "level": "Executive",
    "company": "Google"
}

print(f"\nWelcome Exec. {identification['name']}, a {identification['job']} at {identification['company']}.\n")
print(f"A dictionary {identification}\n")
for identity in identification.values():
    print(identity)  # access only value(assigned to a key) in the dictionary specified.
