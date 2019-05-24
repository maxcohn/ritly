# ritly

## link shortener

There's really nothing special about this at all. I was at my internship in which
I am doing way more SQL than I ever had before (which just means more than none),
and I figured a little project would be a neat way to get an understanding of SQL,
and more specifically databases as a tool.

A link shortener popped in my mind, so I figured I'd make a bit of a game out of it
to see how fast I could make a basic one. Overall, I'm pleasantly surprised how quick
this was.

## How to use it

This is a standard Flask project where everything is stored in the main package.
There is also a `create.sql` file that builds the initial database (this project
uses MySQL).

In the same directory as the package directory, create a `config.json` file.
This is going to store the database login info. The layout is as follows:

```json
{
    "host": "hostname",
    "user": "username",
    "passwd": "password"
}
```

If I didn't follow any best practices, please let me know, I'm new to databases,
so I'd love to learn!