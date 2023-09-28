A **.env** file is used to store environment variables that your application or script needs to use. Environment variables are values that can be accessed by our Python code and are used to store sensitive information like API keys, database credentials, or configuration settings.

The .env file is **NOT TO BE COMMITED** in a repository and it can be ignored using a .gitignore file. for this example i am commiting the .env file to the repository.

Here's how you can work with a .env file in Python:

1. Create a .env File:
Create a file in your project directory and name it .env. You can use any plain text editor to create this file.


2. Add Environment Variables:
In the .env file, you can define your environment variables in the following format:

```makefile
VARIABLE_NAME=variable_value
SECRET_KEY=mysecretkey
API_KEY=yourapikey
DB_PASSWORD=yourpassword
```

3. Load Environment Variables in Python:
To access these environment variables in your Python script, we will need a library like python-dotenv to load them from the .env file. You can install this library using pip:

```bash
pip install python-dotenv
```

Then, in your Python script, import and load the environment variables like this:

```python
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv("SECRET_KEY")
print(secret)   
```

![](../.assets/02/1.png)


