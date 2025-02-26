# not-json
 There's no json parser here

 This project is inspired in the json parser challenge from [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-json-parser/)
 
 # Introduction

 I really don't like the quotation marks in the name of a field, so i will remove it (joking)

 I will make a json-like parser with some changes, more for study than anything else

 The parser will accept something like this:

```
 {
    number: 3
    string: 'str'
    bool: false
    list: [23, 's']
    object: {
        title: 'name'
    }
 }
```

# What we have for now

I already make the parser works for literals like strings, numbers and booleans. And in the last update, i achieved, with a lot of effort, to make the list work on. Futhermore, i make little changes in the code and also add a new function call 'loads', inspired by python json lib, that read a json text and return a python dict.

Update v1.0
Now we have loads and dumps functions, and we support objects.
I think that's the v1.0 os the not-json lib

## References

My primary reference to write a parser is the book [Crafting Interpreters](https://craftinginterpreters.com) by [Robert Nystrom](https://github.com/munificent)

