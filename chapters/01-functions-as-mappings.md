# 1. Functions as mappings

*An expression can produce a number without producing an answer.*

Imagine a community studio that rents worktables. It charges a 12-dollar setup fee and 8 dollars per hour for studio sessions between one and four hours. Its checkout accepts fractional hours. The equation $C(h)=12+8h$ is a compact description of the charge in dollars. Plug in five and the arithmetic gives 52. The checkout still cannot sell five hours. The algebra did what it was told. The model forgot part of the contract.

**By the end:** evaluate a function from a table, formula or graph; distinguish formula domain from contextual domain; trace the allowable inputs of a composition.

## Work from the input out

A function assigns exactly one output to each allowed input. It need not assign a different output to every input. Two sessions can cost the same if there is a flat-rate band. One session length cannot yield both 20 dollars and 28 dollars under a function that has only length as its input. If weekday and weekend rates differ, include the day as an input or use separate functions. A graph with two heights at the same horizontal coordinate identifies that problem. This is the vertical-line test, not a test of whether the graph is straight.

| Hours $h$ | Charge $C(h)$ (dollars) |
| ---: | ---: |
| 1 | 20 |
| 2 | 28 |
| 2.5 | 32 |
| 4 | 44 |

Draw the table as points. The equation and continuous-hour policy justify a straight segment connecting them, with solid ends at one and four; the points alone do not. The slope is 8 dollars per hour and the output range is $[20,44]$ dollars. The number 12 is the formula's intercept on an extended line, not an available zero-hour purchase.

## Follow a composed machine

The desk accepts requests in minutes. Set $H(m)=m/60$, where $m$ is the duration in minutes. The charge from a request in minutes is $(C\circ H)(m)=12+8(m/60)$. The outer function requires its input to lie in $[1,4]$. So the composition accepts $60\le m\le240$, even if the converter itself can convert any nonnegative duration. At 150 minutes, $H(150)=2.5$ hours and the charge is 32 dollars. At 30 minutes the converter works; the charge function is not defined for the converted input. A composition's domain requires both a lawful inner input and an admissible inner output.

If $C(h)=36$, then $h=(36-12)/8=3$. You can recover duration from price here because each accepted duration has a distinct price. An inverse is a function only on outputs that have a unique original input; the inverse price-to-duration rule accepts prices in $[20,44]$. At a price of 48 dollars, its formal calculation gives 4.5 hours, which the studio won't book.

## Practice before using a tool

1. Give the charge and its units for 195 minutes. What does the model say about a 45-minute request?
2. Suppose the studio switches to whole-hour bookings without changing rates. List the four possible prices. Explain what has to change in the graph and in the inverse domain.
3. Let $S(x)=\sqrt{x}$ and $J(t)=t-3$ on the reals. Find the domain of $S\circ J$, then reverse the order. Check both at $t=1$.

After your own trace, you can ask a model to propose one input at each boundary and one just outside. Use the rules above to check every example; the prompt is not the test. The paper equivalent is a partner supplying their own edge cases. Keep the original and corrected domains. [Practice and answers](../practice/README.md) · [Next: equations](02-equations-and-domains.md)
