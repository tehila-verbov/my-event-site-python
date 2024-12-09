import json
from datetime import datetime

class EventRegistrationSystem:
    def __init__(self, event_name):
        self.event_name = event_name
        self.participants = []
        self.file_path = f"{event_name}_participants.json"
        self.load_participants()

    def load_participants(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.participants = json.load(file)
        except FileNotFoundError:
            self.participants = []

    def save_participants(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.participants, file, ensure_ascii=False, indent=4)

    def register_participant(self, name, email, phone):
        # בדיקה אם המשתתף כבר רשום
        for participant in self.participants:
            if participant['email'] == email:
                print("משתתף עם אימייל זה כבר רשום!")
                return False

        # יצירת רשומת משתתף
        participant = {
            'name': name,
            'email': email,
            'phone': phone,
            'registration_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # הוספת המשתתף לרשימה ושמירה
        self.participants.append(participant)
        self.save_participants()
        print(f"ברוכים הבאים, {name}! נרשמת בהצלחה.")
        return True

    def list_participants(self):
        print(f"\nרשימת משתתפים באירוע '{self.event_name}':")
        print("=" * 50)
        for i, participant in enumerate(self.participants, 1):
            print(f"{i}. שם: {participant['name']}")
            print(f"   אימייל: {participant['email']}")
            print(f"   טלפון: {participant['phone']}")
            print(f"   זמן הרשמה: {participant['registration_time']}")
            print("-" * 50)
        print(f"סה״כ משתתפים: {len(self.participants)}")

    def search_participant(self, email):
        for participant in self.participants:
            if participant['email'] == email:
                print("פרטי משתתף:")
                print(f"שם: {participant['name']}")
                print(f"אימייל: {participant['email']}")
                print(f"טלפון: {participant['phone']}")
                return participant
        print("לא נמצא משתתף עם אימייל זה.")
        return None

def main():
    # יצירת מופע של מערכת הרשמה לאירוע
    event = EventRegistrationSystem("סדנת יצירת אתרים עם Claude")

    while True:
        print("\n--- מערכת הרשמה לאירועים ---")
        print("1. הרשמה לאירוע")
        print("2. הצגת רשימת משתתפים")
        print("3. חיפוש משתתף")
        print("4. יציאה")

        choice = input("בחר פעולה (1-4): ")

        if choice == '1':
            name = input("הזן שם מלא: ")
            email = input("הזן כתובת אימייל: ")
            phone = input("הזן מספר טלפון: ")
            event.register_participant(name, email, phone)

        elif choice == '2':
            event.list_participants()

        elif choice == '3':
            email = input("הזן כתובת אימייל לחיפוש: ")
            event.search_participant(email)

        elif choice == '4':
            print("תודה ולהתראות!")
            break

        else:
            print("בחירה לא חוקית. אנא נסה שוב.")

if __name__ == "__main__":
    main()
