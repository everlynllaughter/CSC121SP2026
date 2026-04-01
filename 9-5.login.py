class User:
  """A class to represent a user."""

  def __init__(self, first_name, last_name, username, email):
    """Initialize user attributes."""
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.email = email
    self.login_attempts = 0

  def describe_user(self):
    """Display a summary of the user's information."""
    print(f"Name: {self.first_name} {self.last_name}")
    print(f"Username: {self.username}")
    print(f"Email: {self.email}")

  def greet_user(self):
    """Display a personalized greeting."""
    print(f"Hello, {self.first_name}!")

  def increment_login_attempts(self):
    """Increment the number of login attempts by 1."""
    self.login_attempts += 1

  def reset_login_attempts(self):
    """Reset login attempts to 0."""
    self.login_attempts = 0


# Create a user
user = User("Isla", "Rex", "isla_rex", "isla@email.com")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login attempts
print(user.login_attempts)

# Reset login attempts
user.reset_login_attempts()

# Print login attempts again
print(user.login_attempts)