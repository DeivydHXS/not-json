# not-json
 There's no json parser here

 This project is inspired in the json parser challenge from [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-json-parser/)
 
 # Introduction

 I will make a json-like parser with some changes
 I really don't like the quotation marks in the name of a field, so i will remove it
 
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


## References

My primary reference to write a parser is the book [Crafting Interpreters](https://craftinginterpreters.com) by [Robert Nystrom](https://github.com/munificent)

