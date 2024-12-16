# Define the base class first
class BaseProvider:
    # Base class definition
    pass

# HuggingfaceProvider inherits from BaseProvider
class HuggingfaceProvider(BaseProvider):
    def __init__(self):
        # Initialize any necessary attributes
        print("HuggingfaceProvider initialized")

    def some_method(self):
        # Implement methods
        print("Some method of HuggingfaceProvider called")

# OpenaiProvider inherits from BaseProvider
class OpenaiProvider(BaseProvider):
    def __init__(self):
        # Initialize any necessary attributes
        print("OpenaiProvider initialized")

    def some_method(self):
        # Implement methods
        print("Some method of OpenaiProvider called")


# Example of creating instances
huggingface_provider = HuggingfaceProvider()
huggingface_provider.some_method()

openai_provider = OpenaiProvider()
openai_provider.some_method()
