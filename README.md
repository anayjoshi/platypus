# Platypus

Platypus is a is *truely* minimal language. In its entirety, it consists of:

* variable assignment
* binary operations
* if conditional
* if-else conditional
* while loops

## Grammar

Platypus uses PLY to write the grammar.

    program: function

    function: FUNCTION ( var_list ) { summary stmt_list RETURN ( var_list ) }

    summary: SUMMARY

    var_list: VAR var_list

    var_list:

    stmt_list: stmt stmt_list

    stmt_list:

    value: VAR

    value: NUMBER

    condn: value comparison_op value

    condn: value

    stmt: VAR = value

    stmt: VAR = value comparison_op value

    stmt: VAR = value arithmatic_op value

    stmt: WHILE ( condn ) { stmt_list }

    stmt: IF ( condn ) { stmt_list }

    stmt: IF ( condn ) { stmt_list } ELSE { stmt_list }

    comparison_op: < | > | <= | >= | == | !=

    arithmatic_op: + | * | / | - | %

## Installation

```
$ pip install platypus
```

## Usage

Example *platypus* programs can be looked up in the `tests/examples/` folder in this repository. As an example, to simulate the *platypus* program `tests/examples/sum_till_N.platypus`, run

```
$ platypus -i sum_till_N.platypus
```

You would be presented with a **shell**. To execute the function, simply enter the argument(s) in the shell. In case of `sum_till_N()`, the only argument is `N`.

Enter the following in the shell 

```
platypus $ 12
```

The result, ie the sum of first 12 natural numbers, would be printed on
the screen

	
Similarly, if you want to simulate `examples/fibo_sum.platypus`, execute:

```
platypus $ 1 1 10
```

Note that the first argument is first fibonacci number, second argument
is second fibonacci number, third argument is `N` for `Nth` fibonacci number. The result would be a tuple containing the  `Nth` fibonacci number and sum of first `N` fibonacci numbers

