"""Independent checks of original College Algebra fixtures; standard library only."""
import csv
from fractions import Fraction as F
from math import isclose, log, sqrt
from pathlib import Path
import unittest


def demand(price):
    if not 2 <= price <= 9:
        raise ValueError("outside observed price window")
    return 32 - 2 * price if price <= 5 else 42 - 4 * price


def schedules(extended=4, minutes=42):
    return [(s, e) for s in range(21) for e in range(extended, 21 - s)
            if 2 * s + 3 * e <= minutes]


def first_price(extended=4, minutes=42):
    possible = {s + e for s, e in schedules(extended, minutes)}
    return next(p for p in range(2, 10) if demand(p) in possible)


def rational(x):
    return F(x*x-36, x-6)


class AlgebraChecks(unittest.TestCase):
    def test_duration_and_charge(self):
        self.assertEqual(12 + 8 * F(195, 60), 38)
        self.assertLess(F(45, 60), 1)
        self.assertEqual([12 + 8*h for h in range(1, 5)], [20, 28, 36, 44])

    def test_quadratic_context(self):
        self.assertTrue(all(w*(w+2)==48 for w in (-8,6)))
        self.assertEqual([w for w in (-8,6) if w > 0], [6])

    def test_roots_and_domain(self):
        self.assertEqual(rational(8), 14)
        with self.assertRaises(ZeroDivisionError):
            rational(6)
        self.assertEqual([x for x in (4,-1) if sqrt(x+5)==x-1], [4])
        self.assertEqual([x for x in (0,3) if sqrt(x+1)==x-1], [3])
        self.assertEqual([q**3 for q in (-2,2) if q*q == 4], [-8,8])

    def test_decay_threshold(self):
        self.assertEqual(32*F(1,2)**3,4)
        self.assertEqual(32*F(1,2)**5,1)
        t=log(F(6,32))/log(F(1,2))
        self.assertTrue(2 < t < 3 and isclose(32*0.5**t,6))
        self.assertEqual([32*F(1,2)**k for k in (2,3)], [8,4])

    def test_compounding(self):
        self.assertEqual(50*F(4,5)**2,32)
        self.assertEqual(40*F(3,2)**2,90)

    def test_schedule_maximum_and_uniqueness(self):
        self.assertEqual(len(schedules()),91)
        self.assertFalse(any(s+e>19 for s,e in schedules()))
        self.assertEqual([(s,e) for s,e in schedules() if s+e==19],[(15,4)])

    def test_worksheet_transfer(self):
        for minimum, minutes, cap, price in [(4,42,19,6),(8,42,17,7),(5,41,18,6),(6,42,18,6),(4,44,20,6)]:
            with self.subTest(minimum=minimum,minutes=minutes):
                self.assertEqual(max(map(sum,schedules(minimum,minutes))),cap)
                self.assertEqual(first_price(minimum,minutes),price)

    def test_join_and_fitting_observations(self):
        with Path(__file__).with_name("reservations.csv").open(newline="") as source:
            rows=list(csv.DictReader(source))
        fitting=[(int(r["price_dollars"]),int(r["requested_reservations"])) for r in rows if r["role"]=="fit"]
        self.assertEqual(fitting,[(2,28),(5,22),(9,6)])
        self.assertEqual([demand(p) for p,_ in fitting],[v for _,v in fitting])
        self.assertEqual(32-2*5,42-4*5)
        self.assertEqual([(r["price_dollars"],r["requested_reservations"]) for r in rows if r["role"]=="challenge"],[("8","10")])

    def test_countermodels(self):
        endpoint=lambda price: 28-F(22,7)*(price-2)
        self.assertEqual(endpoint(5),F(130,7))
        self.assertEqual(10-endpoint(8),F(6,7))
        self.assertEqual(10-(32-2*8),-6)
        self.assertEqual(10-demand(8),0)
        self.assertEqual(42-4*12,-6)
        for price in (-1,12):
            with self.assertRaises(ValueError):
                demand(price)


if __name__=="__main__":
    unittest.main(verbosity=2)
