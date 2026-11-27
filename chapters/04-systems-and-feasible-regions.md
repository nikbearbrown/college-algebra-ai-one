# 4. Systems and feasible regions

*A point can fit the drawing and still fail the job.*

Imagine the community studio has space for 20 reservations and 42 setup minutes. A standard reservation takes two minutes to set up; an extended one takes three. At least four extended reservations must be offered and filled for the schedule in this exercise. Can the room actually serve 20 people?

**By the end:** translate resource limits into inequalities, construct their intersection, and verify integer candidates when half a reservation is not a choice.

## Read each limit as a test

Let $s$ and $e$ be nonnegative integer counts of standard and extended reservations. The limits are
$$s+e\le20,\qquad 2s+3e\le42,\qquad e\ge4.$$
A feasible point satisfies all the limits at once. On axes with $s$ horizontal, draw $s+e=20$, $2s+3e=42$ and $e=4$ as solid lines; equality is allowed. The point $(0,4)$ is a convenient check for which side of the first two lines qualifies. The first quadrant, and the region at or above $e=4$, restrict the drawing further.

The capacity lines intersect at $(18,2)$: double the first equation and subtract it from the second to get $e=2$. That point is outside the allowed region. An intersection of two boundaries is a candidate, not a certificate. For the continuous picture, the feasible triangle has corners $(0,4)$, $(15,4)$, and $(0,14)$; all satisfy the seat constraint. Only whole-number points in that triangle are actual schedules.

## Bound the answer before enumerating

Setup is $2(s+e)+e$. If at least four are extended, setup is at least $2(s+e)+4$. Since only 42 minutes are available, there can be no more than 19 reservations. At $(15,4)$, exactly 42 minutes are used and 19 seats are filled, so the bound is attainable. For 19 reservations, the setup condition also forces $e\le4$; with the minimum of four, this is the only 19-reservation split. Increasing the seat limit alone won't help. At this solution the setup time is the binding resource.

Distinguish the bound from a forecast. A schedule with $(15,4)$ is feasible. If the requests arrive in a split of $(12,7)$, 19 requests consume 45 minutes. The same total does not imply feasibility. [The capstone](../practice/worksheet.md) will require you to say what control the studio has over its mix.

## Practice before using a tool

1. Test $(14,5)$, $(14,4)$ and $(16,3)$. State the failed test for each infeasible point.
2. If setup rises to 44 minutes, can the studio serve 20 people? Give a feasible split or a proof none exists.
3. With the original setup time but at least six extended reservations, find the new maximum and exhibit a feasible integer split.
4. Pick a point on a boundary with a fractional coordinate. Explain the difference between an admissible graph point and a reservation schedule.

A spreadsheet enumeration can check your maximum after you derive a bound. Test the first prohibited point as well as the optimum. [Practice and answers](../practice/README.md) · [Next: piecewise models](05-building-and-challenging-models.md)
