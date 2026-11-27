# 3. Exponentials and logarithms

*Equal time steps needn't remove equal amounts.*

Suppose a studio testing a catalog workflow has 32 unresolved records on Monday. A week later there are 16 and another week later there are 8. The backlog has lost 16, then 8. A line cannot reproduce both changes over equal spans. A repeated factor of one half does.

**By the end:** fit a constant-factor model to equally spaced measurements, solve for time with a logarithm and check where a continuous prediction is useful.

## Fit the ratio before fitting a curve

Write $N(t)=N_0b^t$, with starting level $N_0$, factor $b>0$ per time unit, and $t$ measured in that unit. With $t$ in weeks the first two points give $N_0=32$ and $b=16/32=1/2$. The third point checks the assumed mechanism: $32(1/2)^2=8$. A constant ratio is the signature to look for, not simply a descending curve. A zero or negative level in this example would contradict the positive model.

To find when it reaches 4, divide by 32 to get $(1/2)^t=1/8$. The exponent is 3. When no convenient integer power appears, take natural logs of the positive ratio:
$$t=\frac{\ln(N/N_0)}{\ln b}.$$
A logarithm gives the exponent that reaches a positive argument. Its numerator here uses the dimensionless ratio of two counts. Its denominator is nonzero because $b\ne1$. A result of 3 means three weeks, not three records.

## Check the decision convention

At what time does a continuous extension predict 6 records? It gives $t=\ln(6/32)/\ln(1/2)\approx2.415$ weeks. Technical support checks only on Mondays. The actual scheduled check predicted to be at or below 6 is the next whole week, week 3. Round the time upward for this decision and confirm $N(2)=8>6$ and $N(3)=4\le6$. Rounding to the nearest week silently changes the claim.

For growth with $b>1$ the function increases; for decay $0<b<1$ it decreases. If $b=1$ it is constant and fitting a time by dividing by $\ln 1$ makes no sense. A prediction between 0 and 1 can represent a smooth level, not a literal fraction of a particular record. The model never predicts zero at a finite time; a verified zero backlog would require a different account of the final stage.

## Practice before using a tool

1. Convert a 20% decrease per week into a factor. Starting at 50, give the predicted level after two weeks.
2. A quantity rises from 40 to 60 in two weeks at a constant factor. Find the weekly factor and estimate the level at week four. Check your result by using the two-week factor directly.
3. In the backlog model, find the first weekly check at or below one. Explain why the same equation cannot answer when the last record is cleared.

If you ask a model to justify a rounding choice, independently bracket the result with the two adjacent whole weeks. A calculator or table is enough. [Practice and answers](../practice/README.md) · [Next: feasible systems](04-systems-and-feasible-regions.md)
