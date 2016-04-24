# Rage's Sublime Utils
Some handy tools to use at work when you need to process results from other programs to use them in other programs.

- [Utilities](#utilities)
    - [SQL Listify](#sql-listify)
    - [JSON Listify](#json-listify)

# Utilities

## SQL Listify
**SQL Listify** lets you turn a newline separated list into a format you can put in an SQL `IN` clause.

### Example
Let's say you have a list like this

```
1239595
1235123
123599
2131235
```

To use the plugin, just

1. Highlight the list
2. Open the command palette
3. Look for ** SQL Listify **
4. Press Enter and you'll get a list like this.

`("1239595","1235123","123599","2131235")`

## JSON Listify
**JSON Listify** works the same way as **SQL Listify** but it uses square brackets `[]` instead of parentheses.

### Example
With a list like this

```
1239595
1235123
123599
2131235
```

Using **JSON Listify**, you'll get this

`["1239595","1235123","123599","2131235"]`
