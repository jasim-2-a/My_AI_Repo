def get_input(prompt):
    return input(prompt).strip()

def get_multiple_entries(section_name):
    entries = []
    print(f"\nEnter your {section_name} (type 'done' when finished):")
    while True:
        entry = input(f"- ").strip()
        if entry.lower() == 'done':
            break
        if entry:
            entries.append(entry)
    return entries

def create_resume():
    print(" Resume Generator\n---------------------")

    # Personal Info
    name = get_input("Full Name: ")
    email = get_input("Email: ")
    phone = get_input("Phone Number: ")
    summary = get_input("Brief Summary/About You: ")

    # Resume Sections
    education = get_multiple_entries("education history")
    experience = get_multiple_entries("work experience")
    skills = get_multiple_entries("skills")

    # Anime question
    watch_anime = get_input("Do you watch anime? (yes/no): ").lower()
    favorite_anime = ""
    show_taunt = False

    if watch_anime == "yes":
        favorite_anime = get_input("Which anime is your favorite? ")
    else:
        show_taunt = True

    # Formatting resume
    resume_lines = [
        f"{name.upper()}",
        f"Email: {email} | Phone: {phone}",
        "-" * 40,
        "SUMMARY:",
        f"{summary}",
        "",
        "EDUCATION:"
    ] + [f"- {edu}" for edu in education] + [
        "",
        "EXPERIENCE:"
    ] + [f"- {exp}" for exp in experience] + [
        "",
        "SKILLS:"
    ] + [f"- {skill}" for skill in skills]

    if favorite_anime:
        resume_lines += ["", "FAVORITE ANIME:", f"- {favorite_anime}"]
    elif show_taunt:
        resume_lines += ["", "P.S.:", "You are like a filler episode skippable. "]

    # Save to file
    filename = f"{name.replace(' ', '_').lower()}_resume.txt"
    with open(filename, "w") as file:
        file.write("\n".join(resume_lines))

    print(f"\n Resume saved to '{filename}'!")

# Run the app
if __name__ == "__main__":
    create_resume()
