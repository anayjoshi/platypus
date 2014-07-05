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

The following program computes the sum of the first `N` numbers and returns it. Save this file as say `sum_till_N.platypus`

```C
function(N) {
    
# this function calculates the sum of first n numbers #
    i = 0
    sum = 0
    c = 1
    while (c) {
        sum = sum + i
        i = i + 1
        if(i >= N) {
            c = 0
        }
    }
    
    return(sum)
}
```

Now, run

```
$ platypus -i sum_till_N.platypus
```

You would be presented with a **shell**. To execute the function, simply enter the argument(s) in the shell. In case of `sum_till_N()`, the only argument is `N`.


```
platypus $ 12
```

The result would look like

```
[66]
```

	
Another example. The following function returns the greatest number among the arguments `a1`, `a2` & `a3`. Save this file as `greater.platypus`

```C
function (a1 a2 a3) {
# this function calculates the greatest amongst the three entered numbers #
    
    ans = a1
    if (a2 > a1) {
        ans = a2
        if(a3 > a2) {
            ans = a3
        }
    }
    else {
        if(a3 > a1) {
        ans = a3
        }
    }
    return (ans)
}
```

Again run *platypus* and pass in the arguments in the shell.

```
platypus $ 1 1 10
```

The result would look like

```
[10]
```

Platypus can also be used to return multiple values. Save the following program as `fibo_sum.platypus`

```C
function (a1 a2 N) {
# a1, a2 = first and second fibonacci numbers. 
This function returns the Nth fibonacci number and 
the sum of the first N fibonacci numbers #

    if (N == 1) {
        fibo = a1
        sum = a1
    }
    else {
        if (N == 2) {
            fibo = a2
            sum = a1 + a2
        }
        else {
        i = 3
        sum = a1 + a2
        anow = a2
        aprev = a1
            while (i <= N) {
                temp = anow
                anow = anow + aprev
                aprev = temp
                i = i + 1
                sum = sum + anow
            }
            fibo = anow
        }
    }

return (fibo sum)
}
```

Running this program,
            
```
platypus $ 1 1 8
```

should output

```
[21, 54]
```
