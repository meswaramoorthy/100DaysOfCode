MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    """Print name is allowed or not allowed based on MIN_DRIVING_AGE"""

    isAllowed = "is allowed" if age >= MIN_DRIVING_AGE else "is not allowed"

    print(f"{name} {isAllowed} to drive")


allowed_driving("Tom", 21)
allowed_driving("Jerry", 9)

