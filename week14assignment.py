def create_guest_lookup(guest_list):

    dic = {guest.get("email"): guest.get("name") for guest in guest_list}
    return dic

def categorize_guests(guest_lookup, check_in_emails):
    guest_names_set = {guest_name for guest_name in guest_lookup.keys()}
    check_in_set =  set(check_in_emails)
    no_shows = guest_names_set - check_in_set
    crashers = check_in_set -  guest_names_set
    return no_shows, crashers

def generate_badges(guest_lookup, check_in_emails):
    name_list = [guest_lookup[check_in] for check_in in check_in_emails if check_in in guest_lookup.keys()]
    name_list.sort()
    return [f"Welcome, {name.upper()}!" for name in name_list] 

guests = [
    {'name': "Alice Smith", 'email': "alice@example.com"},
    {'name': "Bob Jones", 'email': "bob@example.com"},
    {'name': "Charlie Brown", 'email': "char@example.com"}
]
check_ins = ["bob@example.com", "char@example.com", "dave@example.com"]

guest_lookup = create_guest_lookup(guests)
no_shows, crashers = categorize_guests(guest_lookup, check_ins)
badges = generate_badges(guest_lookup, check_ins)

print(f"No shows: {no_shows}")
print(f"Crashers: {crashers}")
print(f"Badges: {badges}")
