from src.app import App

def main():
    url = input("Enter Problem URL: ")
    app = App(url)
    app.start_app()

# Entry Point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")