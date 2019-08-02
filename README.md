# NLP-based-test-generation-engine
It generates test cases based on the natural language based statements you give as input.

Suppose I want to test if a button in a webpage is working, in order to test that we need to write a long code. 
But using the package that I have written you can avoid writing code for almost all test cases and can instead write
in native language(English) and test it.

An example test flow is given below:

'''
https://my.playstation.com/
Click Sign In
Type Sign-In ID (Email Address) as email_address
Type Password as password
Click Sign In
Type What are you up to? as Hi, I am having a blast.
Click Post
Wait 5
'''
