# ALDA_search

## Description
In this project we create 3 algorithms to find a number in a list, if it is, each one return a boolean value in this case it will be true. The algorithms are linear, binary and ternary search.

## Running locally and testing
* Create virtual enviroment: `virtualenv env`
* To install dependencies: `pip install -r requirements.txt`


## Tests
In this tests we can see 3 different compilations, in each one you can see how with the linear search it takes more time, while in the other 2 they are very similar, in some cases the binary search is better than ternary, but it depends of the list that the generator create.
It is because both have the same complexity

### Linear search
![image](https://user-images.githubusercontent.com/90010884/225796855-28332e1f-f577-4e0c-910d-38e9d56afd25.png)
![image](https://user-images.githubusercontent.com/90010884/225796864-892b244b-7d4a-4aca-8bb4-a727cacdd10b.png)

### Binary search
![image](https://user-images.githubusercontent.com/90010884/225796892-8c1728b3-7fad-4d89-b74f-6c6c2f7d5b9c.png)
![image](https://user-images.githubusercontent.com/90010884/225796899-7a576819-eccd-40c3-ace4-6b4551e36d6e.png)

### Ternary search
![image](https://user-images.githubusercontent.com/90010884/225796949-36082633-3c78-42d3-aa50-790753a0fc00.png)
![image](https://user-images.githubusercontent.com/90010884/225796952-2937873f-22fb-4209-8880-f7dd6d77e726.png)


## Current Coverage

To run `coverage`, make sure that you have it installed in your pc, if not run `pip install coverage`, then run the requirements.txt. After that run `coverage run -m unittest discover` and `coverage report` it show you the following table:

## Code Beautifer

After install Black, run de comand `black . -l 120` to beautifier you code
