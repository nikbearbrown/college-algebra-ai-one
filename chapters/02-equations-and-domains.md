# 2. Equations and domains

*Keep the condition under which the shortcut works.*

The expression $\frac{x^2-36}{x-6}$ and the expression $x+6$ give the same result for every real $x$ except 6. At 6 one is undefined and the other is 12. That exception is not a formatting problem. Canceling a factor changes the expression you see, not the inputs the original expression allowed.

**By the end:** select a solving operation, mark where it is reversible, and test candidate roots in the original equation.

## Turn an equation into alternatives

Suppose a rectangular exhibit must have area 48 square meters, and its length is two meters greater than its width. If $w$ is width in meters, $w(w+2)=48$, with $w>0$. Move 48 to the left and factor:

$$w^2+2w-48=(w+8)(w-6)=0.$$

A product of real numbers is zero only if at least one factor is zero. Both $-8$ and $6$ are genuine roots of the polynomial; only $6$ is a width. Check the accepted rectangle: $6\times8=48$. Factoring is a quick way to see the branches when the factors are recognizable. For $ax^2+bx+c=0$ with $a\ne0$, the quadratic formula $(-b\pm\sqrt{b^2-4ac})/(2a)$ doesn't require a lucky factorization. For example, $x^2-2x-1=0$ gives $1\pm\sqrt{2}$. A negative discriminant $b^2-4ac$ means there are no real roots; zero means one repeated root.

Don't divide by a variable expression without treating its zero case. From $x(x-4)=0$, division by $x$ loses 0. Multiplication by a known nonzero constant, by contrast, can always be reversed.

## Keep the denominator on the page

Solve $(x^2-36)/(x-6)=14$. Record $x\ne6$ first. Then factor the numerator into $(x-6)(x+6)$, cancel within the allowed domain, and solve $x+6=14$. The candidate $8$ checks because $(64-36)/(8-6)=14$. In the variant with right-hand side 12, the shortcut yields 6. The equation has **no solution** because that candidate violates the very rule allowing the cancellation. On a graph the original is the line $y=x+6$ with a hole at $(6,12)$, not the whole line.

Squaring both sides can add solutions, since $u^2=v^2$ allows $u=v$ or $u=-v$. For $\sqrt{x+5}=x-1$, the right side must be nonnegative, so $x\ge1$. Squaring gives $x^2-3x-4=0$, with candidates 4 and −1. At 4 both original sides equal 3. At −1 they equal 2 and −2. The domain check and substitution agree.

Real fractional powers need a declared convention: for $x^{2/3}=(\sqrt[3]{x})^2$, solving $x^{2/3}=4$ gives cube roots $2$ and $-2$, hence inputs $8$ and $-8$. Some software evaluates real fractional powers of negative numbers differently; specify the real cube-root operation instead of relying on the parser.

## Practice before using a tool

1. Solve $x^2-9x+20=0$ and confirm both roots.
2. Solve $(x^2-9)/(x-3)=6$ without erasing the restriction.
3. Solve $\sqrt{x+1}=x-1$. Test every candidate in the original equation, including any rejected one.

If a solver proposes roots, copy the candidates into an independent substitution table. Without a solver, swap candidate lists with a partner. [Practice and answers](../practice/README.md) · [Next: exponentials and logarithms](03-exponentials-and-logarithms.md)
