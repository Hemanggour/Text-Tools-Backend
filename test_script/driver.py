import test_file
from getpass import getpass

def display_menu():
    print("\n=== Text Tool API Testing Menu ===")
    print("1. Summarize Text")
    print("2. Paraphrase Text")
    print("3. Grammar Check")
    print("4. AI Reply")
    print("5. Text to Speech")
    print("6. Exit")
    return input("Select an option (1-6): ")

def get_api_key_flow(email, password):
    """Handle login and API key retrieval"""
    login_response = test_file.login(email, password)
    if not login_response:
        print("Login failed!")
        return None
    
    api_key = test_file.get_api_key()
    if not api_key or "api_key" not in api_key:
        print("Failed to get API key. Generating new one...")
        api_key = test_file.generate_api_key()
        if not api_key or "api_key" not in api_key:
            print("Failed to generate API key!")
            return None
    
    return api_key.get("api_key")

def main():
    # First time setup
    print("=== Text Tool API Testing ===")
    email = input("Enter email: ")
    password = getpass("Enter password: ")
    
    api_key = get_api_key_flow(email, password)
    if not api_key:
        print("Failed to initialize. Exiting...")
        return

    while True:
        choice = display_menu()
        
        if choice == "1":
            text = input("Enter text to summarize: ")
            response = test_file.summarize_api(api_key, text)
            print("\nSummary:", response)
            
        elif choice == "2":
            text = input("Enter text to paraphrase: ")
            response = test_file.paraphase_api(api_key, text)
            print("\nParaphrased:", response)
            
        elif choice == "3":
            text = input("Enter text for grammar check: ")
            response = test_file.grammar_check_api(api_key, text)
            print("\nGrammar check:", response)
            
        elif choice == "4":
            text = input("Enter your question: ")
            response = test_file.ai_reply_api(api_key, text)
            print("\nAI Reply:", response)
            
        elif choice == "5":
            text = input("Enter text for speech: ")
            voice = input("Enter voice (optional, press Enter to skip): ").strip() or None
            emotion = input("Enter emotion (optional, press Enter to skip): ").strip() or None
            
            response = test_file.text_to_speech_api(
                api_key=api_key,
                query=text,
                voice=voice,
                emotion=emotion
            )
            print("\nAudio saved at:", response)
            
        elif choice == "6":
            print("Logging out...")
            test_file.logout()
            break
            
        else:
            print("Invalid option! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()