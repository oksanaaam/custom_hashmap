# Custom HashMap

This project implements a custom HashMap data structure in Python.  
The HashMap class provides methods for storing and retrieving key-value pairs efficiently.

## Requirements

- Python 3

### Installation

1. Clone the repo
`git clone https://github.com/oksanaaam/custom_hashmap.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```

## Usage

To use the HashMap class, you can create an instance of the class and then use its methods to interact with the key-value pairs stored in the hashmap.  

### Here are the available methods:

- put(key, value)  
This method adds a key-value pair to the hashmap.  
The key parameter represents the key, and the value parameter represents the corresponding value.  


- get(key)  
This method retrieves the value associated with the specified key from the hashmap.  
If the key is not found, a KeyError is raised.


- contains_key(key)  
This method checks if the hashmap contains the specified key.  
It returns True if the key is found and False otherwise.


- keys()  
This method returns a list of all the keys in the hashmap.


- values()  
This method returns a list of all the values in the hashmap.


- items()  
This method returns a list of tuples representing all the key-value pairs in the hashmap.


- remove(key)  
This method removes the key-value pair with the specified key from the hashmap.  
If the key is not found, a KeyError is raised.


- __len__()  
This method returns the number of key-value pairs in the hashmap.


- __iter__()  
This method allows iterating over the keys of the hashmap using a loop or a comprehension.

You can use these methods to add, retrieve, remove, and perform other operations on the key-value pairs in the hashmap.

## Testing

The tests.py file contains unit tests for testing the functionality of the HashMap class.  
To run the tests, use the following command:

`python tests.py`

![result_testing.png](images%20for%20README.md%2Fresult_testing.png)

The test results will be displayed, showing which tests passed and which ones failed..
