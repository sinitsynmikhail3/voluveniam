try:
    # Code that may raise a ValueError or IndexError exception
except ValueError as ve:
    # Code to handle the ValueError exception
    print(f"A ValueError occurred: {ve}")
except IndexError as ie:
    # Code to handle the IndexError exception
    print(f"An IndexError occurred: {ie}")
except Exception as e:
    # Optional: Code to handle any other exception
    print(f"An unexpected error occurred: {e}")
finally:
    # Code that should run regardless of whether an exception occurred or not
    # For example, closing a file or releasing a resource
