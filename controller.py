from model import insert_into_db

def validate_input(name, email, message):
    try:
        if name == '' or email == '' or message == '':
            return {
                "message": "Required fields cannot be null",
                "status": False
            }
        elif '@' not in email:
            return {
                "message": "Invalid email format",
                "status": False
            }
        else:
            response = insert_into_db(name, email, message)
            return {
                "response": response,
                "message": "Your message has been inserted successfully",
                "status": 200
            }
    except Exception as e:
        return {
            "response": str(e),
            "message": "An error occurred while inserting into the database",
            "status": 500
        }
