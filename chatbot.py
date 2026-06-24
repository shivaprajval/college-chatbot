# College FAQ Chatbot

faq_dict = {
    # Admission
    "admission":"The admission criteria include a valid entrance exam score and 12th-grade marks. Selection may also involve personal interviews depending on the program.",
    "criteria": "The admission criteria include a valid entrance exam score and 12th-grade marks. Selection may also involve personal interviews depending on the program.",

    # Location
    "campus": "The campus is located at Beedupalli Knowledgepark, Behind SSSIHMS, Puttaparthi, Sri Sathya Sai District, AP - 515134.",
    "location": "The campus is located at Beedupalli Knowledgepark, Behind SSSIHMS, Puttaparthi, Sri Sathya Sai District, AP - 515134.",
    "located": "The campus is located at Beedupalli Knowledgepark, Behind SSSIHMS, Puttaparthi, Sri Sathya Sai District, AP - 515134.",

    # Courses
    "courses": "We offer B.Tech in CSE, ECE, EEE, MECH, CIVIL, along with M.Tech, MBA, and BBA programs.",
    "courses offered": "We offer B.Tech in CSE, ECE, EEE, MECH, CIVIL, along with M.Tech, MBA, and BBA programs.",

    # Fee Structure
    "fees": "The fee structure varies depending on the course and category. Please contact the admissions office for detailed information.",
    "fee": "The fee structure varies depending on the course and category. Please contact the admissions office for detailed information.",

    # Contact
    "contact": "You can contact us at enquiry@sseptp.org / hr@sseptp.org or call +91 9100064545 / 74545 during office hours (Mon-Sat: 9:00 AM to 5:00 PM).",
    "phone": "You can contact us at enquiry@sseptp.org / hr@sseptp.org or call +91 9100064545 / 74545 during office hours (Mon-Sat: 9:00 AM to 5:00 PM).",
    "email": "You can contact us at enquiry@sseptp.org / hr@sseptp.org or call +91 9100064545 / 74545 during office hours (Mon-Sat: 9:00 AM to 5:00 PM).",

    # Facilities
    "hostel": "Yes, we provide separate hostel facilities for boys and girls with all basic amenities.",
    "accommodation": "Yes, we provide separate hostel facilities for boys and girls with all basic amenities.",
    "placement": "We have a dedicated placement cell that assists students with internships and job placements in reputed companies.",
    "scholarship": "Scholarships are available for meritorious and economically weaker students. Please contact the scholarship office for details.",
    "wifi": "Wi-Fi is available across the campus for all students and staff.",

    # Additional FAQs
    "ragging": "Ragging is strictly prohibited on campus. We follow anti-ragging policies as per UGC guidelines with strict disciplinary actions.",
    "lab": "Our college has well-equipped labs for all departments including CSE, ECE, MECH, and CIVIL to support practical learning.Our labs are modern and fully equipped for hands-on experiments and projects.",
    "mess food": "The college mess provides hygienic and nutritious food for all hostel students with both North and South Indian menu options.",
    "faculty": "Our faculty members are well-qualified with rich academic and industry experience and are committed to student success.",
    "classrooms": "All classrooms are spacious and equipped with digital boards, projectors, and proper ventilation.",
    "rules and regulations": "Students are expected to follow college rules and maintain discipline on campus. Ragging, misconduct, and academic dishonesty are strictly prohibited.",
    "timings": "College timings are from 9:00 AM to 4:30 PM, Monday to Saturday. Fridays usually have half-day sessions.",
    "holidays": "College observes all major national holidays. A detailed holiday calendar is provided at the beginning of the academic year.",
    "fest": "The college organizes cultural fests, technical fests, and annual sports meets to encourage student participation.",
    "culturalevents": "The college organizes cultural fests, technical fests, and annual sports meets to encourage student participation.",
    "events": "The college organizes cultural fests, technical fests, and annual sports meets to encourage student participation.",
    "sports": "We have facilities for cricket, volleyball, badminton, and indoor games. Annual sports day is a major event.",
    "digital": "We use digital tools like smart boards, projectors, and learning platforms for interactive classes.our college uses smart classrooms and online platforms to deliver digital learning",
    "workshops and guest lectures": "Various workshops are conducted regularly to enhance technical and soft skills of students.Industry experts and alumni are invited for guest lectures and knowledge-sharing sessions",
    "library": "Our library has a wide collection of academic books, journals, e-resources, and study materials. It is open from 8 AM to 7 PM.",
    # Trips and Industrial Visits
    "industrial visit": "Yes, the college organizes regular industrial visits to provide students with exposure to real-world industry practices and environments.",
    "industrial visits": "Yes, the college organizes regular industrial visits to provide students with exposure to real-world industry practices and environments.",
    "iv": "Yes, the college organizes regular industrial visits to provide students with exposure to real-world industry practices and environments.",
    "trips": "Educational field trips and industrial visits are arranged periodically as part of experiential learning. These include visits to industries, research labs, and technical expos.",
    "tours": "We conduct educational field trips to enhance practical knowledge in various disciplines.",
   

}


# Get answer based on keyword match
def get_response(user_input):
    user_input = user_input.lower()
    for keyword, answer in faq_dict.items():
        if keyword in user_input:
            return answer
    return "Sorry, I didn't understand that. Please ask about admission, courses, facilities, or contact information."


# Display menu
def show_menu():
    print("\n--- MENU ---")
    print("0. Exit")
    print("1. What are the admission criteria?")
    print("2. Where is the campus located?")
    print("3. What courses are offered?")
    print("4. What is the fee structure?")
    print("5. How can I contact the college?")
    print("6. Is hostel/accommodation available?")
    print("7. Are scholarships available?")
    print("8. How are placements handled?")
    print("9. Is Wi-Fi available on campus?")
    print("10. Is ragging allowed?")
    print("11. What lab facilities are available?")
    print("12. How is the mess food?")
    print("13. Tell me about the faculty.")
    print("14. Describe the classrooms.")
    print("15. What are the college rules and regulations?")
    print("16. What are the college timings?")
    print("17. Are there holidays?")
    print("18. What cultural/sports events are held?")
    print("19. Are there digital classes?")
    print("20. Any workshops or guest lectures?")
    print("21. Is there a library?")
    print("22. Are there industrial visits?")
    print("23. Are educational trips conducted?")


# Main chatbot loop
while True:
    show_menu()
    choice = input("Select an option (0-23): ").strip()

    if choice == "0" or choice.lower() == "exit":
        print("Bot: Thank you for visiting Sanskrithi School of Engineering. Goodbye!")
        break
    elif choice == "1":
        user_input = "What are the admission criteria?"
    elif choice == "2":
        user_input = "Where is the campus located?"
    elif choice == "3":
        user_input = "What courses are offered?"
    elif choice == "4":
        user_input = "What is the fee structure?"
    elif choice == "5":
        user_input = "How can I contact the college?"
    elif choice == "6":
        user_input = "Is hostel accommodation available?"
    elif choice == "7":
        user_input = "Are scholarships available?"
    elif choice == "8":
        user_input = "How are placements handled?"
    elif choice == "9":
        user_input = "Is Wi-Fi available on campus?"
    elif choice == "10":
        user_input = "Is ragging allowed?"
    elif choice == "11":
        user_input = "What lab facilities are available?"
    elif choice == "12":
        user_input = "How is the mess food?"
    elif choice == "13":
        user_input = "Tell me about the faculty."
    elif choice == "14":
        user_input = "Describe the classrooms."
    elif choice == "15":
        user_input = "What are the college rules and regulations?"
    elif choice == "16":
        user_input = "What are the college timings?"
    elif choice == "17":
        user_input = "Are there holidays?"
    elif choice == "18":
        user_input = "What cultural/sports events are held?"
    elif choice == "19":
        user_input = "Are there digital classes?"
    elif choice == "20":
        user_input = "Any workshops or guest lectures?"
    elif choice == "21":
        user_input = "Is there a library?"
    elif choice == "22":
        user_input = "Are there industrial visits?"
    elif choice == "23":
        user_input = "Are educational trips conducted?"

    else:
        print("Invalid option. Please try again.")
        continue

    print(f"\nUser: {user_input}")
    print("Bot:", get_response(user_input))
