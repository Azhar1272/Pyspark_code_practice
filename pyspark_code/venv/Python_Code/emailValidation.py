import re

def validate_info(data):

    # Check for null or empty fields
    if not data["email"] or not data.get('phone') or not data.get('address'):
        return False, "One or more fields are empty or missing."

    # Validate email format using regex
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_pattern, data['email']):
        return False, "Invalid email format."

    # Validate phone number length (10 digits)
    if not data['phone'].isdigit() or len(data['phone']) != 10:
        return False, "Phone number must be 10 digits."

    # Validate address (basic non-empty string check, can be extended)
    if len(data['address'].strip()) == 0:
        return False, "Invalid address."

    # All validations passed
    return True, "Validation successful."


# Test data
info = {
    "email": "test@example.com",
    "phone": "1234567890",
    "address": "123 Main Street"
}

# Call the function
is_valid, message = validate_info(info)

# Output the result
print("Validation Result:", is_valid)
print("Message:", message)