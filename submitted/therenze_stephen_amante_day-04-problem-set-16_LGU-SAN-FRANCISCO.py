def my_info():
    return {
        "name": "Therenze Stephen Amante",
        "job": "ICT & GIS Specialist",
        "email": "sample@gmail.com",
        "skills": "GIS, Web Dev, Cybersecurity",
        "certs": "ISC2 Certified & CCNA"
    }


def create_resume_text(data):
    return f"""
        ========================================
        NAME: {data['name']}
        ROLE: {data['job']}
        ========================================
        CONTACT: {data['email']}
        SKILLS:  {data['skills']}
        CERTS:   {data['certs']}
        ========================================
        """


def save_resume(text):
    with open("resume_output.txt", "w") as file:
        file.write(text)
    print("Success! Resume saved to file.")



my_data = my_info()
final_resume = create_resume_text(my_data)

print(final_resume)      # Show it on screen
save_resume(final_resume) # Save it to disk