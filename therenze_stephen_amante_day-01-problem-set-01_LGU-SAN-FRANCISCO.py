
name = 'therenze stephen amante'
email = 'sample@gmail.com'
phone = '1234567890'
country = 'Philippines'
city = 'san francisco'
barangay = 'poblacion'
citizenship = 'filipino'


institution = 'SSCT'
degree = 'BSIT'

company = 'LGU san francisco'
department = 'MPDO'
function = 'ICT Specialist & GIS Specialist'

technical_skills = 'frontend development ● graphic designing ● gis specialist ● database management ● cybersecurity'
soft_skills = 'communication ● problem-solving ● teamwork'
certifications = 'isc2 certified in cybersecurity and former CCNA'

a_experience = '1yr web developer'
a_address = 'davao city'
b_experience = '2yr freelance graphic designer'
b_address = 'home-based'
c_experience = 'freelance GIS Consultant'
c_address = 'home-based'
c_clients = 'LGU Taganaan and LGU San Francisco Agusan del Sur'



resume = f"""
============================================================
                {name}
                {function}
============================================================

CONTACT & PERSONAL DETAILS
--------------------------
Email:       {email}
Phone:       {phone}
Address:     Brgy. {barangay}, {city}, {country}
Citizenship: {citizenship}

CURRENT EMPLOYMENT
------------------
Company:     {company}
Department:  {department}
Position:    {function}

EDUCATION
---------
Institution: {institution}
Degree:      {degree}

WORK EXPERIENCE
---------------
* {c_experience}
  Location: {c_address}
  Clients:  {c_clients}

* {b_experience}
  Location: {b_address}

* {a_experience}
  Location: {a_address}

SKILLS & CERTIFICATIONS
-----------------------
Technical:   {technical_skills}
Soft Skills: {soft_skills}
Certs:       {certifications}

============================================================
"""

print(resume)


# # Print to the Text File
# # Note: encoding="utf-8" handles the ● symbols correctly
# output_file = open("resume_output.txt", "w", encoding="utf-8")
# print(resume, file=output_file)
# output_file.close()

# print("\n[System]: Resume successfully saved to resume_output.txt")