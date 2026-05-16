import secrets
import string
import math


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password, chars


def calculate_entropy(length, pool_size):
    entropy = length * math.log2(pool_size)
    return entropy


def get_entropy_strength(entropy):
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        try:
            length = int(input("\nEnter desired password length (minimum 8): "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    password, chars = generate_password(length)
    pool_size = len(chars)
    entropy = calculate_entropy(length, pool_size)
    strength = get_entropy_strength(entropy)

    print("\n" + "-" * 45)
    print(f"Generated Password : {password}")
    print(f"Password Length    : {length}")
    print(f"Character Pool Size: {pool_size}")
    print(f"Entropy Score      : {entropy:.2f} bits")
    print(f"Strength           : {strength}")
    print("-" * 45)


if __name__ == "__main__":
    main()
