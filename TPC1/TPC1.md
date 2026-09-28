**Expressão regular que não aceita strings binárias com 011**

```regex
^(1*|1*0(0|10)*|1*0(0|10)*1)$
```