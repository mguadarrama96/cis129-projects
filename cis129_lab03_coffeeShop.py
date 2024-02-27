{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b9efb3c-7601-4155-936a-9d668a4f08d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My Coffee and Muffin Shop\n"
     ]
    }
   ],
   "source": [
    "print('My Coffee and Muffin Shop')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a6257048-c7f7-4100-bed7-02e9a20aa0ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of coffees bought?\n"
     ]
    }
   ],
   "source": [
    "print('Number of coffees bought?')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f805ab84-4629-42fd-95c7-29a8f45c1d45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n"
     ]
    }
   ],
   "source": [
    "coffees = int(input())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1c90d0fe-b649-47c9-918f-d658025190c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of muffins bought?\n"
     ]
    }
   ],
   "source": [
    "print('Number of muffins bought?')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cbab2ba1-5d6c-4ca0-b1d7-21d492e106b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n"
     ]
    }
   ],
   "source": [
    "muffins = int(input())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ae64be2b-cdd9-4c9c-b8d9-962b783b3a2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "coffee_price = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "00548413-7798-4802-892f-b9446a682286",
   "metadata": {},
   "outputs": [],
   "source": [
    "muffin_price = 4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0073670b-e87d-491e-acae-a7e07ad2b035",
   "metadata": {},
   "outputs": [],
   "source": [
    "subtotal = (coffees * coffee_price) + (muffins * muffin_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c2311028-cb6b-4589-8d41-0a35ed420d88",
   "metadata": {},
   "outputs": [],
   "source": [
    "coffee_subtotal = (coffees * coffee_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "29f821cd-700d-45de-80c5-12c39fa35e86",
   "metadata": {},
   "outputs": [],
   "source": [
    "fcoffee_subtotal = f'{coffee_subtotal: .2f}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "875399ef-c37e-4ac5-af78-49cc967af608",
   "metadata": {},
   "outputs": [],
   "source": [
    "muffin_subtotal = (muffins * muffin_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9c33a0e8-3146-4388-8a05-f89037d79d1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "fmuffin_subtotal = f'{muffin_subtotal: .2f}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fefd7548-b6e2-45b3-adc7-6aa61145ff11",
   "metadata": {},
   "outputs": [],
   "source": [
    "tax_rate = .06"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0457f1b2-b019-4b13-8928-f5a182052985",
   "metadata": {},
   "outputs": [],
   "source": [
    "tax = subtotal * tax_rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7294803d-7c68-413f-9ba9-2a8f9dc1df96",
   "metadata": {},
   "outputs": [],
   "source": [
    "total = subtotal + tax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "53cabeb3-fe40-431f-8786-dd2325ceb0fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My Coffee and Muffin Shop Receipt\n"
     ]
    }
   ],
   "source": [
    "print('My Coffee and Muffin Shop Receipt') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "80fa2db6-29de-4a47-8e76-17966a4e4753",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 Coffee at $ 5 each: $  5.00\n"
     ]
    }
   ],
   "source": [
    "print(coffees, 'Coffee at $' ,coffee_price, 'each: $' ,fcoffee_subtotal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "79a1af67-ecd9-451f-a8ee-95cda375526d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 Muffins at $ 4 each: $  8.00\n"
     ]
    }
   ],
   "source": [
    "print(muffins, 'Muffins at $' ,muffin_price, 'each: $' ,fmuffin_subtotal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cc32828a-b6f0-4765-9cf4-2be11a3723c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6% tax: $ 0.78\n"
     ]
    }
   ],
   "source": [
    "print('6% tax: $' ,tax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "acfc7f4b-c964-47f7-8db1-3b4425c40126",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print('-------------------------')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4d84f079-d2db-4843-8d87-632d533ec3a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total: $ 13.78\n"
     ]
    }
   ],
   "source": [
    "print('total: $' ,total)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
