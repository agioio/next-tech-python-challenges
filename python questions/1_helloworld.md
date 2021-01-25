Welcome to the classical introductory challenge: say "Hello, World!".

"Hello, World!" is the traditional first program for beginning programming in a new language or environment.

The objectives are simple:

    Write a function that returns the string "Hello, World!".
    Run the test suite and make sure that it succeeds.
    Submit your solution and check it at the website.

If everything goes well, you will be ready to fetch your first real challenge.
Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every challenge will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

```raise Exception("Meaningful message indicating the source of the error")```