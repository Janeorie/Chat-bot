import nltk
from nltk.chat.util import Chat, reflections

# Ensure necessary NLTK data is downloaded
def download_nltk_data():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
    except Exception as e:
        print(f"Warning: Could not download NLTK data: {e}")

download_nltk_data()

# FUTO and Nigerian University specific conversation pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today regarding FUTO or Nigerian universities?",]
    ],
    [
        r"what is futo|tell me about futo",
        ["FUTO stands for the Federal University of Technology, Owerri. It is the oldest university of technology in Nigeria, established in 1980.",]
    ],
    [
        r"who is the (vc|vice chancellor)",
        ["The current Vice-Chancellor of FUTO is Professor Nnenna Oti. She is the first female VC of the institution.",]
    ],
    [
        r"what is the motto of futo",
        ["The motto of FUTO is 'Technology for Service'.",]
    ],
    [
        r"when was futo founded",
        ["FUTO was established in 1980 by the executive fiat of President Shehu Shagari.",]
    ],
    [
        r"where is futo located",
        ["FUTO is located in Ihiagwa, Owerri West Local Government Area of Imo State, Nigeria.",]
    ],
    [
        r"what are the schools in futo|list schools",
        ["FUTO has several schools: SEET (Engineering), SAAT (Agriculture), SOHT (Health), SOPS (Physical), SOBS (Biological), SICT (ICT), SMAT (Management), SESET (Electrical Systems), and SOES (Environmental).",]
    ],
    [
        r"(.*)seet(.*)",
        ["SEET is the School of Engineering and Engineering Technology. It is the largest school in FUTO, offering courses like Mechanical, Civil, Chemical, and Petroleum Engineering.",]
    ],
    [
        r"(.*)sict(.*)",
        ["SICT is the School of Information and Communication Technology. It houses Computer Science, Cyber Security, Software Engineering, and Information Technology.",]
    ],
    [
        r"(.*)hostel(.*)|where to stay",
        ["FUTO has on-campus hostels like Hostel A, B, C, D, E, F, and the NDDC hostel. Many students also live off-campus in Ihiagwa, Obinze, or Eziobodo.",]
    ],
    [
        r"(.*)admission(.*)|how to get into futo",
        ["Admission into FUTO is primarily through JAMB. You need to meet the cut-off mark and participate in the Post-UTME screening.",]
    ],
    [
        r"what is jamb|jamb",
        ["JAMB (Joint Admissions and Matriculation Board) is the body responsible for conducting entrance examinations for tertiary institutions in Nigeria.",]
    ],
    [
        r"(.*)strike(.*)|asuu",
        ["Strikes by the Academic Staff Union of Universities (ASUU) are a common challenge in Nigerian federal universities, often related to funding and welfare issues.",]
    ],
    [
        r"(.*)(gp|cgpa)(.*)",
        ["GP (Grade Point) and CGPA (Cumulative Grade Point Average) measure your academic performance. In FUTO, the maximum CGPA is 5.0.",]
    ],
    [
        r"(.*)carryover(.*)",
        ["A carryover is a course you failed and must retake in the next available semester. Avoid them to maintain a high GP!",]
    ],
    [
        r"(.*)clearance(.*)",
        ["Clearance is the process of verifying your documents (O'level results, admission letter, etc.) after gaining admission. It is mandatory for all freshers.",]
    ],
    [
        r"(.*)portal(.*)",
        ["The official FUTO portal is portal.futo.edu.ng. You can register for courses and check results there.",]
    ],
    [
        r"what are futo colors",
        ["FUTO's traditional colors are Gold and Blue.",]
    ],
    [
        r"how are you",
        ["I am doing great! Ready to help you with FUTO related inquiries. How about you?", "I'm functional and optimized! How can I assist you today?"]
    ],
    [
        r"who (created|made) you",
        ["I was created as part of the CSC 309 Mini Projects to assist students with university information.",]
    ],
    [
        r"hi|hello|hey",
        ["Hello! I am your FUTO and Nigerian University Assistant. How can I help you?", "Hi there! Do you have any questions about FUTO?"]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye! Technology for Service. Have a great day!", "Bye! Hope I was helpful."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't quite understand that. Could you ask about FUTO's VC, location, motto, or specific schools like SEET or SICT?", "I am still learning. Try asking about FUTO hostels, GP, or the school portal."]
    ]
]

class FUTOChatbot:
    def __init__(self):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)

    def start_console_chat(self):
        print("--- FUTO Assistant Chatbot ---")
        print("Type 'quit' to exit.")
        self.chat.converse()

if __name__ == "__main__":
    bot = FUTOChatbot()
    bot.start_console_chat()
